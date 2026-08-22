#!/usr/bin/env python3
"""Exact Walsh certificate for the 49-term quadratic-interface counterexample."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


N = 7
TERM_COUNT = 49
INDEPENDENT_ROW_INDICES = [
    0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12,
    16, 17, 18, 20, 24, 32, 33, 34, 36, 40, 48,
]


def normalized_signs() -> list[tuple[int, ...]]:
    """The lexicographically first 49 points of (1,+/-1^6)."""
    return [(1,) + tail for tail in itertools.product((-1, 1), repeat=6)][:TERM_COUNT]


def parity_characters(degree: int) -> list[tuple[int, ...]]:
    return [
        subset
        for size in range(degree % 2, degree + 1, 2)
        for subset in itertools.combinations(range(N), size)
    ]


def evaluation_matrix(
    signs: list[tuple[int, ...]], characters: list[tuple[int, ...]]
) -> list[list[int]]:
    return [
        [math.prod(delta[index] for index in character) for character in characters]
        for delta in signs
    ]


def rational_rank(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    work = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][column]
        work[rank] = [entry / value for entry in work[rank]]
        for row in range(rank + 1, len(work)):
            if work[row][column]:
                value = work[row][column]
                work[row] = [
                    entry - value * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for index in range(size - 1):
        if work[index][index] == 0:
            pivot = next(
                row for row in range(index + 1, size) if work[row][index]
            )
            work[index], work[pivot] = work[pivot], work[index]
            sign *= -1
        value = work[index][index]
        for row in range(index + 1, size):
            for column in range(index + 1, size):
                work[row][column] = (
                    work[row][column] * value
                    - work[row][index] * work[index][column]
                ) // previous
        previous = value
        for row in range(index + 1, size):
            work[row][index] = 0
    return sign * work[-1][-1]


def block_data(degree: int, signs: list[tuple[int, ...]]) -> dict[str, int]:
    characters = parity_characters(degree)
    evaluation = evaluation_matrix(signs, characters)
    selected_rank = rational_rank(evaluation)
    exact_degree_rows = []
    for column, character in enumerate(characters):
        if len(character) == degree:
            row = [0] * len(characters)
            row[column] = 1
            exact_degree_rows.append(row)
    joint_rank = rational_rank(evaluation + exact_degree_rows)
    intersection = selected_rank + len(exact_degree_rows) - joint_rank
    row_block_count = math.comb(N, degree)
    return {
        "character_count": len(characters),
        "selected_walsh_rank": selected_rank,
        "row_block_count": row_block_count,
        "H_dimension": row_block_count * selected_rank,
        "E_block_dimension": len(exact_degree_rows),
        "E_intersection_block_dimension": intersection,
        "E_intersection_dimension": row_block_count * intersection,
    }


def build_payload() -> dict[str, object]:
    signs = normalized_signs()
    degree_rows = {str(degree): block_data(degree, signs) for degree in range(1, 7)}
    quadratic_characters = parity_characters(2)
    quadratic_evaluation = evaluation_matrix(signs, quadratic_characters)
    witness = [quadratic_evaluation[index] for index in INDEPENDENT_ROW_INDICES]
    determinant = bareiss_determinant(witness)
    h_profile = {
        degree: degree_rows[str(degree)]["H_dimension"] for degree in range(1, 7)
    }
    intersection_profile = {
        degree: degree_rows[str(degree)]["E_intersection_dimension"]
        for degree in range(1, 7)
    }
    erasure_lower_bounds = {2: 448, 3: 1293, 4: 1494, 5: 853, 6: 294}
    return {
        "schema_version": 1,
        "status": "EXACT_COUNTEREXAMPLE_TO_QUADRATIC_INTERFACE_ONLY",
        "field": "characteristic zero",
        "n": N,
        "term_count": TERM_COUNT,
        "family": "lexicographically first 49 normalized Glynn sign terms",
        "normalization": "delta_1=1 and tails ordered by product((-1,1), repeat=6)",
        "all_terms_are_chow": True,
        "factor_rank_per_term": 7,
        "pairwise_factor_span_intersection": 0,
        "degree_rows": degree_rows,
        "H_profile_degrees_1_through_6": [h_profile[d] for d in range(1, 7)],
        "E_intersection_profile_degrees_1_through_6": [
            intersection_profile[d] for d in range(1, 7)
        ],
        "quadratic_interface": {
            "explicit_independent_row_indices_zero_based": INDEPENDENT_ROW_INDICES,
            "explicit_minor_determinant": determinant,
            "explicit_minor_determinant_power_of_two": 36,
            "H2_dimension": h_profile[2],
            "E2_dimension": 441,
            "E2_contained_in_H2": intersection_profile[2] == 441,
            "rho_rank": h_profile[2] - 441,
            "degree_two_defect": 0,
            "rho_plus_defect": h_profile[2] - 441,
        },
        "erasure_lower_bounds": {str(k): v for k, v in erasure_lower_bounds.items()},
        "all_erasure_dimension_bounds_satisfied": all(
            h_profile[degree] >= lower
            for degree, lower in erasure_lower_bounds.items()
        ),
        "complementary_sums": {
            "1_6": {"actual": h_profile[1] + h_profile[6], "permanent_upper": 392},
            "2_5": {"actual": h_profile[2] + h_profile[5], "permanent_upper": 1470},
            "3_4": {"actual": h_profile[3] + h_profile[4], "permanent_upper": 2940},
        },
        "E6_contained_in_H6": intersection_profile[6] == 49,
        "E6_intersection_dimension": intersection_profile[6],
        "minimal_surviving_interface": [
            "retain all 49 term labels and Chow multiplication",
            "use the full identity sum_i T_i = perm_7 across complementary degrees",
            "in particular retain E_6 subset H_6, which this counterexample violates",
        ],
        "claim_boundary": [
            "This family is not a 49-term decomposition of perm_7.",
            "It disproves a lower bound rho+Delta_2 >= 177 derived only from the factor packet, E_2 containment, and scalar erasure bounds.",
            "It does not disprove a coupled degree-two/degree-six theorem using the full polynomial identity.",
            "It proves no Chow-rank or border-rank bound.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    assert payload["H_profile_degrees_1_through_6"] == [49, 462, 1330, 1645, 1029, 343]
    assert payload["E_intersection_profile_degrees_1_through_6"] == [49, 441, 1085, 875, 231, 14]
    quadratic = payload["quadratic_interface"]
    assert quadratic["explicit_minor_determinant"] == 2**36
    assert quadratic["rho_rank"] == 21
    assert quadratic["rho_plus_defect"] == 21
    assert payload["all_erasure_dimension_bounds_satisfied"] is True
    assert payload["complementary_sums"]["2_5"] == {"actual": 1491, "permanent_upper": 1470}
    assert payload["complementary_sums"]["3_4"] == {"actual": 2975, "permanent_upper": 2940}
    assert payload["E6_contained_in_H6"] is False
    assert payload["E6_intersection_dimension"] == 14


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    validate(payload)
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("N7_GLYNN49_QUADRATIC_INTERFACE_COUNTEREXAMPLE_PASS")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
