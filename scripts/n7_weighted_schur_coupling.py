#!/usr/bin/env python3
"""Exact fixed-code evaluator for W-01 through W-04."""

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


def evaluate_relations(relation3: np.ndarray, relation4: np.ndarray, prime: int) -> dict[str, object]:
    relation3 = np.asarray(relation3, dtype=np.int64) % prime
    relation4 = np.asarray(relation4, dtype=np.int64) % prime
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
    return {
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
        "schema_version": 2,
        "status": "W-01-W-03-COMPLETE-W-04-FIXED-CODE-OPERATOR",
        "maximum_active_matrix_shape": [42, 35],
        "controls": controls,
        "claim_boundary": [
            "The dense-torus equivalence is a theorem over an infinite field for each fixed point code.",
            "Puncture rank drop is exactly unit-vector membership for each fixed Schur span.",
            "Separator indices in the displayed rows are modular control data at the stated prime.",
            "W-04 structural classification of special point subsets remains open.",
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
