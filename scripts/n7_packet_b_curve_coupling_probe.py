#!/usr/bin/env python3
"""Exact coupling probe on two packet-B moment-curve equality profiles."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sys
import time

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as coupled  # noqa: E402
import n7_mixed_curve_endpoint_search as curve  # noqa: E402
import n7_packet_b_coupling_probe as packet  # noqa: E402


REPRESENTATIVES = (
    (1, 2, 3, 4, 5, 12),
    (1, 2, 3, 6, 9, 10),
)


def monomial_exponents(maximum_degree: int) -> tuple[tuple[int, ...], ...]:
    answer = []
    for total in range(maximum_degree + 1):
        answer.extend(curve.base.compositions(total, 6))
    return tuple(answer)


def moment_curve_tails(weights: tuple[int, ...], prime: int) -> list[tuple[int, ...]]:
    return [
        tuple(pow(parameter, weight, prime) for weight in weights)
        for parameter in range(1, 43)
    ]


def point_code_matrix(
    tails: list[tuple[int, ...]], degree: int, prime: int
) -> np.ndarray:
    exponents = monomial_exponents(degree)
    matrix = np.ones((len(tails), len(exponents)), dtype=np.int64)
    for row, tail in enumerate(tails):
        for column, exponent in enumerate(exponents):
            value = 1
            for coordinate, power in enumerate(exponent):
                value = value * pow(tail[coordinate], power, prime) % prime
            matrix[row, column] = value
    return matrix


def point_code_rank(tails: list[tuple[int, ...]], degree: int, prime: int) -> int:
    return coupled.modular_rank(point_code_matrix(tails, degree, prime), prime)


def local_point_code_coupling(
    tails: list[tuple[int, ...]], prime: int
) -> dict[str, int | bool]:
    degree3 = point_code_matrix(tails, 3, prime)
    degree4 = point_code_matrix(tails, 4, prime)
    return coupled.kernel_image_defect(degree4.T, degree3, prime)


def run_representative(
    weights: tuple[int, ...], prime: int, seed: int, evaluation_columns: int
) -> dict[str, object]:
    tails = moment_curve_tails(weights, prime)
    h3 = point_code_rank(tails, 3, prime)
    h4 = point_code_rank(tails, 4, prime)
    characteristic_zero_h3 = min(42, len(curve.exponent_sums(weights, 3)))
    characteristic_zero_h4 = min(42, len(curve.exponent_sums(weights, 4)))
    if (h3, h4) != (characteristic_zero_h3, characteristic_zero_h4):
        raise AssertionError("modular point-code rank missed its exact exponent cap")
    if h3 + h4 != 72:
        raise AssertionError("representative is not on the middle equality profile")

    rng = np.random.default_rng(seed + prime + sum(weights))
    output_evaluations = rng.integers(
        0, prime, size=(packet.V_DIM, evaluation_columns), dtype=np.int64
    )
    input_evaluations = rng.integers(
        0, prime, size=(packet.V_DIM, evaluation_columns), dtype=np.int64
    )
    factors = packet.common_graph_packet_factor_coefficients(tails, prime)
    started = time.perf_counter()
    output_map, input_map, dimensions = packet.labelled_middle_maps(
        factors, output_evaluations, input_evaluations, prime
    )
    if dimensions != [25] * 7 + [35] * 42:
        raise AssertionError("unexpected local middle dimensions")
    structural_rank_c = 7 * 25 + 35 * h3
    structural_rank_b = 7 * 25 + 35 * h4
    inclusion = coupled.kernel_image_defect_from_kernel(
        output_map, input_map, prime
    )
    if (inclusion["rank_b"], inclusion["rank_c"]) != (
        structural_rank_b,
        structural_rank_c,
    ):
        raise AssertionError("evaluation maps did not retain the structural ranks")
    rank_bc = packet.modular_composite_rank(output_map, input_map, prime)
    exact_defect = (
        packet.EXPECTED_MIDDLE_DIMENSION
        - structural_rank_b
        - structural_rank_c
        + rank_bc
    )
    if exact_defect != inclusion["coupling_defect"]:
        raise AssertionError("projected and exact defects disagree")
    local = local_point_code_coupling(tails, prime)
    if exact_defect != 35 * int(local["coupling_defect"]):
        raise AssertionError("the 42-point coupling reduction failed")
    if rank_bc != 7 * 25 + 35 * int(local["rank_bc"]):
        raise AssertionError("the 42-point composite-rank reduction failed")
    return {
        "weights": list(weights),
        "prime": prime,
        "point_code_profile": [h3, h4],
        "middle_dimension": packet.EXPECTED_MIDDLE_DIMENSION,
        "rank_b": structural_rank_b,
        "rank_c": structural_rank_c,
        "rank_bc": rank_bc,
        "kernel_b_dimension": inclusion["kernel_b_dimension"],
        "kernel_b_intersection_image_c_dimension": inclusion[
            "kernel_b_intersection_image_c_dimension"
        ],
        "exact_characteristic_zero_coupling_defect": exact_defect,
        "local_42_point_code_coupling": local,
        "condition_holds": exact_defect == 0,
        "elapsed_seconds": time.perf_counter() - started,
    }


def classify_curve_box(max_weight: int) -> dict[str, object]:
    scanned, candidates = curve.scan_weight_profiles(max_weight)
    rows = []
    for weights in candidates:
        prime_rows = []
        for prime in coupled.PRIMES:
            tails = moment_curve_tails(weights, prime)
            h3 = point_code_rank(tails, 3, prime)
            h4 = point_code_rank(tails, 4, prime)
            if h3 + h4 != 72:
                raise AssertionError("approximate curve profile failed exact replay")
            local = local_point_code_coupling(tails, prime)
            prime_rows.append(
                (
                    h3,
                    h4,
                    int(local["rank_bc"]),
                    int(local["coupling_defect"]),
                )
            )
        if prime_rows[0] != prime_rows[1]:
            raise AssertionError("curve coupling classification disagrees by prime")
        h3, h4, rank_bc, local_defect = prime_rows[0]
        characteristic_zero_h3 = min(42, len(curve.exponent_sums(weights, 3)))
        characteristic_zero_h4 = min(42, len(curve.exponent_sums(weights, 4)))
        if (h3, h4) != (characteristic_zero_h3, characteristic_zero_h4):
            raise AssertionError("modular curve ranks missed exact exponent caps")
        if rank_bc != h3:
            raise AssertionError("the curve composite did not reach its upper bound")
        rows.append(
            {
                "weights": list(weights),
                "point_code_profile": [h3, h4],
                "local_composite_rank": rank_bc,
                "local_coupling_defect": local_defect,
                "global_packet_coupling_defect": 35 * local_defect,
            }
        )
    histogram: dict[str, int] = {}
    for row in rows:
        key = (
            f"{row['point_code_profile'][0]},{row['point_code_profile'][1]}"
            f";defect={row['global_packet_coupling_defect']}"
        )
        histogram[key] = histogram.get(key, 0) + 1
    return {
        "max_weight": max_weight,
        "weight_candidate_count": scanned,
        "middle_equality_candidate_count": len(rows),
        "histogram": histogram,
        "rows": rows,
    }


def build_payload(
    seed: int, evaluation_columns: int, max_weight: int = 24
) -> dict[str, object]:
    if evaluation_columns < packet.EXPECTED_MIDDLE_DIMENSION:
        raise ValueError(
            f"evaluation-columns must be at least {packet.EXPECTED_MIDDLE_DIMENSION}"
        )
    rows = [
        run_representative(weights, prime, seed, evaluation_columns)
        for weights in REPRESENTATIVES
        for prime in coupled.PRIMES
    ]
    grouped: dict[tuple[int, ...], set[int]] = {}
    for row in rows:
        key = tuple(row["weights"])
        grouped.setdefault(key, set()).add(
            int(row["exact_characteristic_zero_coupling_defect"])
        )
    if any(len(values) != 1 for values in grouped.values()):
        raise AssertionError("the two primes disagree")
    return {
        "schema_version": 1,
        "status": "EXACT_TWO_CURVE_EQUALITY_PROFILE_COUPLING_CLASSIFICATION",
        "seed": seed,
        "evaluation_columns": evaluation_columns,
        "representatives": [list(item) for item in REPRESENTATIVES],
        "candidate_cardinality_checked_before_materialization": 2,
        "conservative_peak_memory_mib": 320,
        "rows": rows,
        "common_graph_coupling_reduction": (
            "For every common 42-point graph packet, the global coupling "
            "defect is 35 times the defect of ker(ev_4^T) subset im(ev_3)."
        ),
        "curve_box_classification": classify_curve_box(max_weight),
        "claim_boundary": [
            "Each displayed point-code profile has H_Z(3)+H_Z(4)=72 and therefore lies on the scalar packet-B middle equality profile.",
            "The rank-(30,42) representative satisfies coupling because B is injective.",
            "The rank-(31,41) representative is an exact fixed-curve test, not a classification of all point sets with that Hilbert profile.",
            "The complete displayed weight box is classified by the small 42-point coupling matrix; all candidates already fail the separate permanent degree-six and degree-seven target tests.",
            "No classification of arbitrary 42-point sets, lower-50 theorem, or border-rank conclusion follows.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260822)
    parser.add_argument(
        "--evaluation-columns",
        type=int,
        default=packet.EXPECTED_MIDDLE_DIMENSION,
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    parser.add_argument("--max-weight", type=int, default=24)
    args = parser.parse_args()
    payload = build_payload(args.seed, args.evaluation_columns, args.max_weight)
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        for item in (payload, frozen):
            for row in item["rows"]:
                row.pop("elapsed_seconds", None)
        if payload != frozen:
            raise SystemExit("n7 packet-B curve coupling JSON mismatch")
        print("PASS n7 packet-B curve coupling probe")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
