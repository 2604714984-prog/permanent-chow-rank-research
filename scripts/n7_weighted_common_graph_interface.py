#!/usr/bin/env python3
"""Exact modular interface for weighted common-graph Packet B."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as coupled  # noqa: E402
import n7_packet_b_curve_coupling_probe as curve_coupling  # noqa: E402


EQUALITY_RANK_STRATA = tuple((rank3, 72 - rank3) for rank3 in range(30, 37))
TARGET_COMPATIBLE_NUMERICAL_STRATA = tuple(
    pair for pair in EQUALITY_RANK_STRATA if pair[1] <= 40
)
TARGET_COMPATIBLE_GEOMETRIC_STRATA = tuple(
    pair for pair in TARGET_COMPATIBLE_NUMERICAL_STRATA if pair != (36, 36)
)
CONTROLS = (
    ("unit_30_42", (1, 2, 3, 4, 5, 12), "unit"),
    ("weighted_31_41", (1, 2, 3, 6, 9, 10), "kernel_relation"),
)
CURVE_UNION_CONSTRUCTIONS = (
    (8, 35, 7, (32, 40)),
    (6, 28, 14, (33, 39)),
    (4, 21, 21, (34, 38)),
    (2, 14, 28, (35, 37)),
)
CURVE_TAIL_EXPONENTS = {
    8: (1, 2, 3, 4, 7, 8),
    6: (1, 2, 3, 4, 5, 6),
    4: (1, 2, 3, 4, None, None),
    2: (1, 2, None, None, None, None),
}


def degree_six_permanent_targets() -> np.ndarray:
    exponents = curve_coupling.monomial_exponents(6)
    index = {exponent: column for column, exponent in enumerate(exponents)}
    targets = np.zeros((7, len(exponents)), dtype=np.int64)
    targets[0, index[(1, 1, 1, 1, 1, 1)]] = 1
    for excluded_tail in range(6):
        exponent = tuple(
            0 if coordinate == excluded_tail else 1 for coordinate in range(6)
        )
        targets[excluded_tail + 1, index[exponent]] = 1
    return targets


def rational_curve_union_tails(
    curve_degree: int,
    curve_point_count: int,
    off_curve_point_count: int,
    prime: int,
    seed: int = 20260822,
) -> list[tuple[int, ...]]:
    if curve_point_count + off_curve_point_count != 42:
        raise ValueError("the construction must contain forty-two points")
    exponents = CURVE_TAIL_EXPONENTS[curve_degree]
    tails = [
        tuple(
            pow(parameter, exponent, prime) if exponent is not None else 0
            for exponent in exponents
        )
        for parameter in range(1, curve_point_count + 1)
    ]
    rng = np.random.default_rng(seed + curve_degree)
    off_curve = rng.integers(
        1, 1000, size=(off_curve_point_count, 6), dtype=np.int64
    )
    tails.extend(tuple(int(value % prime) for value in row) for row in off_curve)
    if len(set(tails)) != 42:
        raise AssertionError("construction contains repeated points")
    return tails


def exact_curve_union_rank_upper_bound(
    curve_degree: int,
    curve_point_count: int,
    off_curve_point_count: int,
    degree: int,
) -> int:
    return min(
        42,
        min(curve_point_count, curve_degree * degree + 1)
        + off_curve_point_count,
    )


def evaluate_interface(
    tails: list[tuple[int, ...]], term_weights: list[int], prime: int
) -> dict[str, object]:
    if len(tails) != 42 or len(term_weights) != 42:
        raise ValueError("the interface requires forty-two points and weights")
    diagonal = np.asarray(term_weights, dtype=np.int64) % prime
    if np.any(diagonal == 0):
        raise ValueError("term weights must be nonzero")
    degree3 = curve_coupling.point_code_matrix(tails, 3, prime)
    degree4 = curve_coupling.point_code_matrix(tails, 4, prime)
    degree5 = curve_coupling.point_code_matrix(tails, 5, prime)
    degree6 = curve_coupling.point_code_matrix(tails, 6, prime)
    targets = degree_six_permanent_targets() % prime
    ranks = {
        degree: coupled.modular_rank(matrix, prime)
        for degree, matrix in (
            (3, degree3),
            (4, degree4),
            (5, degree5),
            (6, degree6),
        )
    }
    weighted_coupling = degree4.T @ (diagonal[:, None] * degree3 % prime) % prime
    coupling_rank = coupled.modular_rank(weighted_coupling, prime)
    target_augmented_rank = coupled.modular_rank(
        np.vstack((degree6, targets)), prime
    )
    target_increment = target_augmented_rank - ranks[6]
    return {
        "prime": prime,
        "rank_e3": ranks[3],
        "rank_e4": ranks[4],
        "rank_e5": ranks[5],
        "rank_e6": ranks[6],
        "weighted_coupling_rank": coupling_rank,
        "degree_six_seven_target_increment_in_one_missing_row_block": target_increment,
        "middle_equality_holds": ranks[3] + ranks[4] == 72,
        "coupling_holds_on_equality_stratum": (
            ranks[3] + ranks[4] == 72 and coupling_rank == 30
        ),
        "degree_six_target_containment_holds": target_increment == 0,
        "matrix_shapes": {
            "e3": list(degree3.shape),
            "e4": list(degree4.shape),
            "e6": list(degree6.shape),
            "targets": list(targets.shape),
            "weighted_coupling": list(weighted_coupling.shape),
        },
    }


def build_payload() -> dict[str, object]:
    rows = []
    for name, curve_weights, weight_mode in CONTROLS:
        for prime in coupled.PRIMES:
            tails = curve_coupling.moment_curve_tails(curve_weights, prime)
            if weight_mode == "unit":
                term_weights = [1] * 42
            else:
                term_weights = curve_coupling.rank_31_41_coupling_weights(
                    tails, prime
                )
            row = evaluate_interface(tails, term_weights, prime)
            row.update(
                {
                    "control": name,
                    "curve_weights": list(curve_weights),
                    "term_weight_mode": weight_mode,
                }
            )
            rows.append(row)
    for row in rows:
        if not row["middle_equality_holds"]:
            raise AssertionError("control left the middle-equality locus")
        if not row["coupling_holds_on_equality_stratum"]:
            raise AssertionError("control failed the weighted coupling equation")
        if row["degree_six_seven_target_increment_in_one_missing_row_block"] != 7:
            raise AssertionError("control did not miss all seven permanent targets")
    constructions = []
    for curve_degree, curve_count, off_count, expected_profile in CURVE_UNION_CONSTRUCTIONS:
        prime_rows = []
        for prime in coupled.PRIMES:
            tails = rational_curve_union_tails(
                curve_degree, curve_count, off_count, prime
            )
            rank3 = curve_coupling.point_code_rank(tails, 3, prime)
            rank4 = curve_coupling.point_code_rank(tails, 4, prime)
            upper3 = exact_curve_union_rank_upper_bound(
                curve_degree, curve_count, off_count, 3
            )
            upper4 = exact_curve_union_rank_upper_bound(
                curve_degree, curve_count, off_count, 4
            )
            if (rank3, rank4) != (upper3, upper4):
                raise AssertionError(
                    (
                        "curve-union construction missed its upper bound",
                        curve_degree,
                        prime,
                        (rank3, rank4),
                        (upper3, upper4),
                    )
                )
            if (rank3, rank4) != expected_profile:
                raise AssertionError("curve-union construction has the wrong profile")
            prime_rows.append(
                {
                    "prime": prime,
                    "rank_e3": rank3,
                    "rank_e4": rank4,
                    "rank_upper_bounds": [upper3, upper4],
                }
            )
        constructions.append(
            {
                "curve_degree": curve_degree,
                "curve_point_count": curve_count,
                "off_curve_point_count": off_count,
                "characteristic_zero_profile": list(expected_profile),
                "prime_rows": prime_rows,
            }
        )
    return {
        "schema_version": 1,
        "status": "B1_WEIGHTED_COMMON_GRAPH_INTERFACE_CHECKPOINT",
        "candidate_cardinality_checked_before_materialization": len(CONTROLS),
        "conservative_peak_memory_mib": 16,
        "equality_rank_strata": [list(pair) for pair in EQUALITY_RANK_STRATA],
        "target_compatible_numerical_strata_after_h5_le_40": [
            list(pair) for pair in TARGET_COMPATIBLE_NUMERICAL_STRATA
        ],
        "target_compatible_geometrically_feasible_strata": [
            list(pair) for pair in TARGET_COMPATIBLE_GEOMETRIC_STRATA
        ],
        "curve_union_constructions": constructions,
        "rows": rows,
        "symbolic_interface": {
            "middle_equality": "rank(E3)+rank(E4)=72",
            "weighted_coupling": "rank(E4^T D E3)=30",
            "degree_six_target": "rank(stack(E6,S6))=rank(E6)",
            "target_matrix_shape": [7, 924],
        },
        "claim_boundary": [
            "The seven equality-rank pairs are the complete numerical list implied by nested 42-point evaluation codes and rank(E3)+rank(E4)=72; geometric realizability is not asserted for every pair.",
            "For a minimal 49-term identity, repeated graph points combine and are excluded; after base change to an algebraic closure of characteristic zero, degree-six target containment implies H_Z(5)<=40 by mixed-partial integrability, leaving five numerical strata; (36,36) is impossible for a reduced length-42 Hilbert function.",
            "The other four target-compatible strata have integer curve-union constructions attaining their characteristic-zero rank upper bounds modulo both displayed primes.",
            "The finite-field rows are deterministic controls of the exact block formulation, not exclusions of arbitrary point configurations.",
            "The weighted rank-(31,41) control satisfies coupling but fails all seven degree-six targets; its characteristic-zero exclusion is separately certified by integer exponent collisions.",
            "No arbitrary common-graph closure, Packet-B closure, lower-50 theorem, or border-rank conclusion follows.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("weighted common-graph interface JSON mismatch")
        print("PASS weighted common-graph interface")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
