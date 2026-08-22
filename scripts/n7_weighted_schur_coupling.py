#!/usr/bin/env python3
"""Exact fixed-code evaluator for W-01 through W-05 operators."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_coupled_obstruction as coupled  # noqa: E402
import n7_packet_b_curve_coupling_probe as curve  # noqa: E402
import n7_weighted_common_graph_interface as interface  # noqa: E402


PROFILE_CONTROLS = (
    ("F1", 6, 28, 14),
    ("F2-F3", 4, 21, 21),
    ("F4-F5", 2, 14, 28),
)


def schur_columns(relation3: np.ndarray, relation4: np.ndarray, prime: int) -> np.ndarray:
    relation3 = np.asarray(relation3, dtype=np.int64) % prime
    relation4 = np.asarray(relation4, dtype=np.int64) % prime
    if relation3.shape[0] != relation4.shape[0]:
        raise ValueError("relation spaces must use the same coordinates")
    return np.column_stack(
        [
            relation3[:, first] * relation4[:, second] % prime
            for first in range(relation3.shape[1])
            for second in range(relation4.shape[1])
        ]
    )


def coordinate_membership_mask(span: np.ndarray, prime: int) -> list[bool]:
    span = np.asarray(span, dtype=np.int64) % prime
    base_rank = coupled.modular_rank(span, prime)
    mask = []
    for index in range(span.shape[0]):
        unit = np.zeros((span.shape[0], 1), dtype=np.int64)
        unit[index, 0] = 1
        mask.append(coupled.modular_rank(np.column_stack((span, unit)), prime) == base_rank)
    return mask


def puncture_rank_drop_mask(span: np.ndarray, prime: int) -> list[bool]:
    """Detect ``e_i`` in a column span by deleting coordinate ``i``."""
    span = np.asarray(span, dtype=np.int64) % prime
    base_rank = coupled.modular_rank(span, prime)
    return [
        base_rank - coupled.modular_rank(np.delete(span, index, axis=0), prime) == 1
        for index in range(span.shape[0])
    ]


def coordinate_zero_indices(space: np.ndarray, prime: int) -> list[int]:
    """Return coordinates on which every vector in a column space vanishes."""
    space = np.asarray(space, dtype=np.int64) % prime
    return [index for index in range(space.shape[0]) if not np.any(space[index, :])]


def column_basis(space: np.ndarray, prime: int) -> np.ndarray:
    """Select a deterministic independent subset of the input columns."""
    space = np.asarray(space, dtype=np.int64) % prime
    basis = np.zeros((space.shape[0], 0), dtype=np.int64)
    rank = 0
    for index in range(space.shape[1]):
        candidate = np.column_stack((basis, space[:, index]))
        candidate_rank = coupled.modular_rank(candidate, prime)
        if candidate_rank > rank:
            basis = candidate
            rank = candidate_rank
    return basis


def coordinate_stabilizer_dimension(span: np.ndarray, prime: int) -> int:
    """Return dim{x: x star L subset L} for the column span L."""
    basis = column_basis(span, prime)
    n = basis.shape[0]
    annihilator_columns = coupled.modular_nullspace_columns(basis.T, prime)
    if basis.shape[1] == 0:
        return n
    blocks = [
        annihilator_columns.T * basis[:, index][None, :] % prime
        for index in range(basis.shape[1])
    ]
    equations = np.vstack(blocks)
    return n - coupled.modular_rank(equations, prime)


def stabilizer_profile(span: np.ndarray, q3: int, q4: int, prime: int) -> dict[str, object]:
    span = np.asarray(span, dtype=np.int64) % prime
    zero_indices = coordinate_zero_indices(span, prime)
    support = [index for index in range(span.shape[0]) if index not in zero_indices]
    effective = span[support, :]
    rank = coupled.modular_rank(span, prime)
    ambient_stabilizer = coordinate_stabilizer_dimension(span, prime)
    effective_stabilizer = coordinate_stabilizer_dimension(effective, prime)
    return {
        "ambient_stabilizer_dimension_mod_prime": ambient_stabilizer,
        "schur_zero_coordinate_indices_mod_prime": zero_indices,
        "effective_support_size_mod_prime": len(support),
        "effective_support_stabilizer_dimension_mod_prime": effective_stabilizer,
        "effective_support_kneser_lower_bound_mod_prime": q3 + q4 - effective_stabilizer,
        "effective_support_kneser_equality_mod_prime": rank
        == q3 + q4 - effective_stabilizer,
    }


def evaluate_relations(relation3: np.ndarray, relation4: np.ndarray, prime: int) -> dict[str, object]:
    relation3 = np.asarray(relation3, dtype=np.int64) % prime
    relation4 = np.asarray(relation4, dtype=np.int64) % prime
    if coupled.modular_rank(relation3, prime) != relation3.shape[1]:
        raise ValueError("relation3 must be a column basis")
    if coupled.modular_rank(relation4, prime) != relation4.shape[1]:
        raise ValueError("relation4 must be a column basis")
    if coupled.modular_rank(np.column_stack((relation3, relation4)), prime) != coupled.modular_rank(relation3, prime):
        raise ValueError("the fixed-code operator requires R4 to be contained in R3")
    span = schur_columns(relation3, relation4, prime)
    rank = coupled.modular_rank(span, prime)
    mask = coordinate_membership_mask(span, prime)
    puncture_mask = puncture_rank_drop_mask(span, prime)
    if puncture_mask != mask:
        raise AssertionError("puncturing and unit-vector membership disagree")
    weight_space = coupled.modular_nullspace_columns(span.T, prime)
    relation3_zero = coordinate_zero_indices(relation3, prime)
    relation4_zero = coordinate_zero_indices(relation4, prime)
    if any(mask[index] for index in relation4_zero):
        raise AssertionError("a degree-four separator coordinate entered the Schur span")
    answer = {
        "q3": relation3.shape[1],
        "q4": relation4.shape[1],
        "schur_generator_count": span.shape[1],
        "schur_rank": rank,
        "weight_space_dimension": weight_space.shape[1],
        "coordinate_membership_indices": [
            index for index, contained in enumerate(mask) if contained
        ],
        "puncture_rank_drop_indices": [
            index for index, contained in enumerate(puncture_mask) if contained
        ],
        "relation3_coordinate_zero_indices": relation3_zero,
        "relation4_coordinate_zero_indices": relation4_zero,
        "degree4_separator_indices_mod_prime": relation4_zero,
        "no_coordinate_vector_in_schur_span_mod_prime": not any(mask),
    }
    answer.update(stabilizer_profile(span, relation3.shape[1], relation4.shape[1], prime))
    return answer


def evaluate_tails(tails: list[tuple[int, ...]], prime: int) -> dict[str, object]:
    degree3 = curve.point_code_matrix(tails, 3, prime)
    degree4 = curve.point_code_matrix(tails, 4, prime)
    relation3 = coupled.modular_nullspace_columns(degree3.T, prime)
    relation4 = coupled.modular_nullspace_columns(degree4.T, prime)
    row = evaluate_relations(relation3, relation4, prime)
    row["rank_e3"] = coupled.modular_rank(degree3, prime)
    row["rank_e4"] = coupled.modular_rank(degree4, prime)
    return row


def build_payload() -> dict[str, object]:
    controls = []
    for label, curve_degree, curve_count, off_count in PROFILE_CONTROLS:
        prime_rows = []
        for prime in coupled.PRIMES:
            tails = interface.rational_curve_union_tails(
                curve_degree, curve_count, off_count, prime
            )
            row = evaluate_tails(tails, prime)
            row["prime"] = prime
            prime_rows.append(row)
        controls.append(
            {
                "frontier_profiles": label,
                "curve_degree": curve_degree,
                "prime_rows": prime_rows,
            }
        )
    return {
        "schema_version": 3,
        "status": "W-01-W-03-COMPLETE-W-04-W-05-FIXED-CODE-OPERATORS",
        "maximum_active_matrix_shape": [42, 35],
        "controls": controls,
        "claim_boundary": [
            "The dense-torus equivalence is a theorem over an infinite field for each fixed point code.",
            "Puncture rank drop is exactly unit-vector membership for each fixed Schur span.",
            "Separator indices in the displayed rows are modular control data at the stated prime.",
            "W-04 structural classification of special point subsets remains open.",
            "The displayed W-05 stabilizer and Kneser rows are modular fixed-code controls.",
            "A characteristic-zero Kneser proof and equality-case classification remain open.",
            "The displayed modular curve-union rows are orientation controls, not target-compatible frontier components.",
            "No F frontier, Packet B endpoint, lower-50 theorem, or border-rank claim follows.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("WEIGHTED_SCHUR_FROZEN_REPLAY_FAIL")
            return 1
        print("WEIGHTED_SCHUR_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
