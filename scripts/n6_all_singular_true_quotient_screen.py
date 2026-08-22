#!/usr/bin/env python3
"""Bounded F_3 screen inside the all-block-singular b=50 pair locus.

The screen uses the actual 441-axis basis of Sym^2(V)/E_2 from N6-038.
It is deliberately restricted to the direct sum of two disjoint permutation
matchings.  It is a finite-field diagnostic, not an exclusion theorem.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))
import n6_b64_common_quotient_rigidity as quotient  # noqa: E402


N = 6
PRIME = 3
PROJECTIVE_LINES = ((1, 0), (0, 1), (1, 1), (1, 2))
ORDERED_COMPLEMENTARY_LINE_PAIRS = tuple(
    (left, right)
    for left in PROJECTIVE_LINES
    for right in PROJECTIVE_LINES
    if left != right
)
CYCLE_TYPES = {
    "6": (1, 2, 3, 4, 5, 0),
    "4+2": (1, 2, 3, 0, 5, 4),
    "3+3": (1, 2, 0, 4, 5, 3),
    "2+2+2": (1, 0, 3, 2, 5, 4),
}


def projective_normalize(vector, axis_kind=None):
    if axis_kind is not None:
        vector = {axis: value for axis, value in vector.items() if axis[0] == axis_kind}
    vector = {axis: value % PRIME for axis, value in vector.items() if value % PRIME}
    if not vector:
        return ()
    axes = sorted(vector, key=repr)
    inverse = pow(vector[axes[0]], PRIME - 2, PRIME)
    return tuple((axis, vector[axis] * inverse % PRIME) for axis in axes)


def block_vector(
    first_column: int,
    first_rows: tuple[int, int],
    first_coefficients: tuple[int, int],
    second_column: int,
    second_rows: tuple[int, int],
    second_coefficients: tuple[int, int],
):
    """The true quotient vector of one product in a column-pair block."""

    answer = {}
    for row, left_coefficient in zip(first_rows, first_coefficients, strict=True):
        for other_row, right_coefficient in zip(
            second_rows, second_coefficients, strict=True
        ):
            coefficient = left_coefficient * right_coefficient
            if not coefficient:
                continue
            left = row * N + first_column
            right = other_row * N + second_column
            axis, sign = quotient.quotient_axis(min(left, right), max(left, right))
            if axis[0] not in {"row", "rectangle"}:
                raise AssertionError(axis)
            answer[axis] = (answer.get(axis, 0) + coefficient * sign) % PRIME
    return {axis: value for axis, value in answer.items() if value}


def pair_vectors(permutation, first_column, first_state, second_column, second_state):
    rows_first = (first_column, permutation[first_column])
    rows_second = (second_column, permutation[second_column])
    p_first, q_first = ORDERED_COMPLEMENTARY_LINE_PAIRS[first_state]
    p_second, q_second = ORDERED_COMPLEMENTARY_LINE_PAIRS[second_state]
    p_vector = block_vector(
        first_column, rows_first, p_first, second_column, rows_second, p_second
    )
    q_vector = block_vector(
        first_column, rows_first, q_first, second_column, rows_second, q_second
    )
    return p_vector, q_vector


def csp_screen(permutation):
    compatibility = {}
    for first_column, second_column in combinations(range(N), 2):
        allowed = set()
        for first_state in range(len(ORDERED_COMPLEMENTARY_LINE_PAIRS)):
            for second_state in range(len(ORDERED_COMPLEMENTARY_LINE_PAIRS)):
                p_vector, q_vector = pair_vectors(
                    permutation,
                    first_column,
                    first_state,
                    second_column,
                    second_state,
                )
                if projective_normalize(p_vector) == projective_normalize(q_vector):
                    allowed.add((first_state, second_state))
        compatibility[first_column, second_column] = allowed

    visited_prefixes = [0] * (N + 1)
    solution_count = 0

    def search(chosen):
        nonlocal solution_count
        column = len(chosen)
        visited_prefixes[column] += 1
        if column == N:
            solution_count += 1
            return
        for state in range(len(ORDERED_COMPLEMENTARY_LINE_PAIRS)):
            if all(
                (chosen[earlier], state) in compatibility[earlier, column]
                for earlier in range(column)
            ):
                search((*chosen, state))

    search(())
    histogram = Counter(len(values) for values in compatibility.values())
    return {
        "ordered_state_space": len(ORDERED_COMPLEMENTARY_LINE_PAIRS) ** N,
        "visited_prefixes_by_length": visited_prefixes,
        "pair_compatibility_count_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "common_true_quotient_pairs": solution_count,
    }


def coordinate_signature(factors):
    axes = [
        quotient.quotient_axis(left, right)[0]
        for left, right in combinations(sorted(factors), 2)
    ]
    return frozenset(axes) if len(set(axes)) == 15 else None


def coordinate_split_screen(permutation):
    support = tuple(range(0, N * N, N + 1)) + tuple(
        permutation[column] * N + column for column in range(N)
    )
    if len(set(support)) != 12:
        raise AssertionError("the two matchings are not disjoint")
    support_set = frozenset(support)
    tested = both_w15 = common = 0
    for chosen in combinations(support, N):
        first = frozenset(chosen)
        if min(support) not in first:
            continue
        second = support_set - first
        tested += 1
        first_signature = coordinate_signature(first)
        second_signature = coordinate_signature(second)
        if first_signature is not None and second_signature is not None:
            both_w15 += 1
            common += first_signature == second_signature
    return {
        "unordered_six_plus_six_splits": tested,
        "both_individual_quotient_dimensions_15": both_w15,
        "common_true_quotient_splits": common,
    }


def diagonal_only_false_positive():
    permutation = CYCLE_TYPES["2+2+2"]
    states = (0, 0, 0, 0, 1, 7)
    diagonal_equal = diagonal_nonzero_equal = full_equal = 0
    rejected_pairs = []
    for first_column, second_column in combinations(range(N), 2):
        p_vector, q_vector = pair_vectors(
            permutation,
            first_column,
            states[first_column],
            second_column,
            states[second_column],
        )
        p_diagonal = projective_normalize(p_vector, "row")
        q_diagonal = projective_normalize(q_vector, "row")
        diagonal_equal += p_diagonal == q_diagonal
        diagonal_nonzero_equal += p_diagonal == q_diagonal and bool(p_diagonal)
        equal = projective_normalize(p_vector) == projective_normalize(q_vector)
        full_equal += equal
        if not equal:
            rejected_pairs.append([first_column, second_column])
    return {
        "cycle_type": "2+2+2",
        "state_indices": list(states),
        "ordered_line_pairs": [
            [list(ORDERED_COMPLEMENTARY_LINE_PAIRS[state][0]),
             list(ORDERED_COMPLEMENTARY_LINE_PAIRS[state][1])]
            for state in states
        ],
        "diagonal_projections_equal_out_of_15": diagonal_equal,
        "nonzero_diagonal_equal_out_of_15": diagonal_nonzero_equal,
        "full_diag_plus_wedge_lines_equal_out_of_15": full_equal,
        "pairs_rejected_only_after_full_test": rejected_pairs,
    }


def build_payload():
    if quotient.quotient_axis_count() != 441:
        raise AssertionError("wrong ambient quotient")
    csp = {name: csp_screen(permutation) for name, permutation in CYCLE_TYPES.items()}
    splits = {
        name: coordinate_split_screen(permutation)
        for name, permutation in CYCLE_TYPES.items()
    }
    if any(result["common_true_quotient_pairs"] for result in csp.values()):
        raise AssertionError("unexpected CSP candidate")
    if any(result["common_true_quotient_splits"] for result in splits.values()):
        raise AssertionError("unexpected coordinate candidate")
    guard = diagonal_only_false_positive()
    if guard["diagonal_projections_equal_out_of_15"] != 15:
        raise AssertionError("diagonal guard")
    if guard["full_diag_plus_wedge_lines_equal_out_of_15"] == 15:
        raise AssertionError("wedge guard")
    return {
        "status": ["FINITE_FIELD_BOUNDED_DIAGNOSTIC", "G-051"],
        "field": "F_3",
        "ambient_quotient_axis_count": 441,
        "family": (
            "U is the coordinate span of the identity matching and one disjoint "
            "permutation matching. In each of the six column fibres, L and M "
            "choose an ordered pair of distinct P1(F_3) lines."
        ),
        "all_block_singular_reason": (
            "Each complete row and column contains two coordinates of U, so every "
            "two-row and two-column projection has dimension at most 4<12."
        ),
        "ordered_complementary_line_pair_count_per_column": 12,
        "cycle_type_representatives": {
            name: list(permutation) for name, permutation in CYCLE_TYPES.items()
        },
        "csp_screens": csp,
        "coordinate_split_screens": splits,
        "coordinate_splits_tested_total": sum(
            result["unordered_six_plus_six_splits"] for result in splits.values()
        ),
        "diagonal_only_false_positive_guard": guard,
        "claim_boundary": (
            "This exhausts only the displayed two-matching family over F_3 and its "
            "coordinate 6+6 splits. It is not a characteristic-zero theorem, does "
            "not exclude the general all-row/all-column-block-singular layer, does "
            "not exclude the b=50 endpoint, does not prove ChowRank(perm_6)>=28, "
            "and makes no border-rank claim."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(rendered, end="")


if __name__ == "__main__":
    main()
