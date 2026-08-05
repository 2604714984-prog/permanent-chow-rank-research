#!/usr/bin/env python3
"""Exact atomic-rank audit for the explicit N6-020 two-defect aggregates.

N6-020 constructs a pairwise separator ``f`` and an exact representation of
``perm_6`` in 24 nonzero base-labelled aggregate spaces.  An aggregate is not
a Chow term.  This script determines the minimum number of fixed-base
normalized two-defect sign atoms needed for the three aggregate types that
occur in that construction:

* every nonzero constant has atomic rank 1;
* ``f`` has atomic rank 46; and
* ``1-f`` has atomic rank 46.

Consequently, decompression of the specific 24-base aggregate formula requires
exactly ``8 + 16*46 = 744`` actual sign terms.  This does not lower-bound every
possible two-defect decomposition; it closes only the explicit aggregate
construction from N6-020.

All calculations use the Python standard library and exact ``Fraction``
arithmetic.  The lower bound restricts row values to ``{0,2,3}``, classifies
all 84 three-atom supports in the resulting local pure-interaction dictionary,
and then uses the direct-sum ANOVA pair blocks.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

N = 6
ROW_POSITIVE = 2
ROW_NEGATIVE = 3
LABEL_A = 1 << (ROW_POSITIVE - 1)
LABEL_B = 1 << (ROW_NEGATIVE - 1)
LABEL_C = LABEL_A | LABEL_B
DEFECT_LABELS = (LABEL_A, LABEL_B, LABEL_C)
EDGES = tuple(combinations(range(N), 2))
POSITIVE_EDGES = frozenset(
    (left, right)
    for left in range(3)
    for right in range(3, 6)
)
TARGET_PARITY = 31
SEPARATOR_ONE_PARITY = 25
SEPARATOR_ZERO_PARITY = 7

Vector = tuple[Fraction, ...]
Term = tuple[Fraction, int, int, int, int]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sign_value(label: int, row: int) -> int:
    if row == 0:
        return 1
    return -1 if (label >> (row - 1)) & 1 else 1


def character(parity: int, base: int) -> int:
    return -1 if (parity & base).bit_count() & 1 else 1


def local_pattern(label: int) -> tuple[int, int, int]:
    return (
        sign_value(label, 0),
        sign_value(label, ROW_POSITIVE),
        sign_value(label, ROW_NEGATIVE),
    )


def local_pure_vector(left: int, right: int) -> Vector:
    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    left_difference = (
        left_pattern[1] - left_pattern[0],
        left_pattern[2] - left_pattern[0],
    )
    right_difference = (
        right_pattern[1] - right_pattern[0],
        right_pattern[2] - right_pattern[0],
    )
    return tuple(
        Fraction(left_difference[row] * right_difference[column])
        for row in range(2)
        for column in range(2)
    )


def local_lower_vector(left: int, right: int) -> Vector:
    """Constant, two left-unary and two right-unary ANOVA coordinates."""

    left_pattern = local_pattern(left)
    right_pattern = local_pattern(right)
    constant = Fraction(left_pattern[0] * right_pattern[0])
    return (
        constant,
        Fraction(left_pattern[1] * right_pattern[0]) - constant,
        Fraction(left_pattern[2] * right_pattern[0]) - constant,
        Fraction(left_pattern[0] * right_pattern[1]) - constant,
        Fraction(left_pattern[0] * right_pattern[2]) - constant,
    )


def solve_columns(columns: list[Vector], target: Vector) -> tuple[Vector, int] | None:
    """Return one exact solution and the coefficient-matrix rank."""

    row_count = len(target)
    column_count = len(columns)
    augmented = [
        [Fraction(columns[column][row]) for column in range(column_count)]
        + [Fraction(target[row])]
        for row in range(row_count)
    ]

    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if augmented[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        augmented[pivot_row], augmented[pivot] = (
            augmented[pivot],
            augmented[pivot_row],
        )
        pivot_value = augmented[pivot_row][column]
        augmented[pivot_row] = [
            value / pivot_value for value in augmented[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            coefficient = augmented[row][column]
            if coefficient:
                augmented[row] = [
                    augmented[row][entry]
                    - coefficient * augmented[pivot_row][entry]
                    for entry in range(column_count + 1)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    for row in range(pivot_row, row_count):
        if (
            all(augmented[row][column] == 0 for column in range(column_count))
            and augmented[row][column_count] != 0
        ):
            return None

    solution = [Fraction(0) for _ in range(column_count)]
    for row, column in enumerate(pivot_columns):
        solution[column] = augmented[row][column_count]
    return tuple(solution), len(pivot_columns)


def local_dictionary_certificate() -> dict[str, object]:
    atoms = [
        {
            "left": left,
            "right": right,
            "pure": local_pure_vector(left, right),
            "lower": local_lower_vector(left, right),
        }
        for left in DEFECT_LABELS
        for right in DEFECT_LABELS
    ]
    target = (
        Fraction(1, 2),
        Fraction(-1, 2),
        Fraction(-1, 2),
        Fraction(1, 2),
    )

    support_counts: dict[str, int] = {}
    exact_triples: list[dict[str, object]] = []
    for support_size in (1, 2, 3):
        compatible = 0
        for indices in combinations(range(len(atoms)), support_size):
            result = solve_columns(
                [atoms[index]["pure"] for index in indices],
                target,
            )
            if result is None:
                continue
            compatible += 1
            if support_size != 3:
                continue
            coefficients, rank = result
            lower = tuple(
                sum(
                    coefficients[position]
                    * atoms[index]["lower"][coordinate]
                    for position, index in enumerate(indices)
                )
                for coordinate in range(5)
            )
            exact_triples.append(
                {
                    "support": [
                        [atoms[index]["left"], atoms[index]["right"]]
                        for index in indices
                    ],
                    "coefficients": [
                        fraction_text(value) for value in coefficients
                    ],
                    "coefficient_matrix_rank": rank,
                    "lower_anova": [fraction_text(value) for value in lower],
                }
            )
        support_counts[str(support_size)] = compatible

    expected = [
        {
            "support": [[LABEL_A, LABEL_A], [LABEL_B, LABEL_B], [LABEL_C, LABEL_C]],
            "coefficients": ["1/4", "1/4", "-1/8"],
            "coefficient_matrix_rank": 3,
            "lower_anova": ["3/8", "-1/4", "-1/4", "-1/4", "-1/4"],
        },
        {
            "support": [[LABEL_A, LABEL_B], [LABEL_B, LABEL_A], [LABEL_C, LABEL_C]],
            "coefficients": ["-1/4", "-1/4", "1/8"],
            "coefficient_matrix_rank": 3,
            "lower_anova": ["-3/8", "1/4", "1/4", "1/4", "1/4"],
        },
    ]
    if support_counts != {"1": 0, "2": 0, "3": 2}:
        raise AssertionError(support_counts)
    if exact_triples != expected:
        raise AssertionError(exact_triples)

    return {
        "restricted_rows": [0, ROW_POSITIVE, ROW_NEGATIVE],
        "restricted_nonconstant_sign_labels": list(DEFECT_LABELS),
        "local_atom_count": len(atoms),
        "pure_target": [["1/2", "-1/2"], ["-1/2", "1/2"]],
        "compatible_support_count": support_counts,
        "exact_three_atom_types": exact_triples,
    }


def separator_value(assignment: tuple[int, ...]) -> Fraction:
    signed = [
        1 if row == ROW_POSITIVE else -1 if row == ROW_NEGATIVE else 0
        for row in assignment
    ]
    active = sum(row in {ROW_POSITIVE, ROW_NEGATIVE} for row in assignment)
    return (
        Fraction(1)
        - Fraction(active, 4)
        + Fraction(
            sum(signed[left] * signed[right] for left, right in EDGES),
            2,
        )
    )


def positive_triple(left: int, right: int) -> list[Term]:
    return [
        (Fraction(1, 4), left, right, LABEL_A, LABEL_A),
        (Fraction(1, 4), left, right, LABEL_B, LABEL_B),
        (Fraction(-1, 8), left, right, LABEL_C, LABEL_C),
    ]


def negative_triple(left: int, right: int) -> list[Term]:
    return [
        (Fraction(-1, 4), left, right, LABEL_A, LABEL_B),
        (Fraction(-1, 4), left, right, LABEL_B, LABEL_A),
        (Fraction(1, 8), left, right, LABEL_C, LABEL_C),
    ]


def separator_terms() -> list[Term]:
    terms: list[Term] = []
    for left, right in EDGES:
        if (left, right) in POSITIVE_EDGES:
            terms.extend(positive_triple(left, right))
        else:
            terms.extend(negative_triple(left, right))
    terms.append((Fraction(-1, 8), 0, 1, 0, 0))
    if len(terms) != 46:
        raise AssertionError(len(terms))
    return terms


def one_minus_separator_terms() -> list[Term]:
    separator = separator_terms()
    terms = [
        (-coefficient, left, right, first, second)
        for coefficient, left, right, first, second in separator[:-1]
    ]
    terms.append((Fraction(9, 8), 0, 1, 0, 0))
    if len(terms) != 46:
        raise AssertionError(len(terms))
    return terms


def evaluate_term(term: Term, assignment: tuple[int, ...]) -> Fraction:
    coefficient, left, right, first, second = term
    return (
        coefficient
        * sign_value(first, assignment[left])
        * sign_value(second, assignment[right])
    )


def signed_edge_certificate() -> dict[str, object]:
    unary_matching_assignments = 0
    signed_sum_histogram: Counter[int] = Counter()
    for mask in range(1 << len(EDGES)):
        signed_degrees = [0] * N
        signed_sum = 0
        for index, (left, right) in enumerate(EDGES):
            sign = 1 if (mask >> index) & 1 else -1
            signed_sum += sign
            signed_degrees[left] += sign
            signed_degrees[right] += sign
        if signed_degrees == [1] * N:
            unary_matching_assignments += 1
            signed_sum_histogram[signed_sum] += 1

    if unary_matching_assignments != 70:
        raise AssertionError(unary_matching_assignments)
    if signed_sum_histogram != Counter({3: 70}):
        raise AssertionError(signed_sum_histogram)

    return {
        "pair_block_count": len(EDGES),
        "minimum_pair_atoms_per_block": 3,
        "minimum_pair_atom_total": 45,
        "signed_edge_assignments_matching_all_unary_coefficients": (
            unary_matching_assignments
        ),
        "forced_signed_edge_sum": 3,
        "forced_constant_from_45_pair_atoms": "9/8",
        "separator_target_constant": "1",
        "forty_five_atom_representation_possible": False,
    }


def construction_certificate() -> dict[str, object]:
    separator = separator_terms()
    complement = one_minus_separator_terms()
    separator_checks = 0
    complement_checks = 0
    for assignment in product(range(N), repeat=N):
        target = separator_value(assignment)
        observed = sum(evaluate_term(term, assignment) for term in separator)
        if observed != target:
            raise AssertionError((assignment, observed, target))
        separator_checks += 1

        complement_target = Fraction(1) - target
        complement_observed = sum(
            evaluate_term(term, assignment) for term in complement
        )
        if complement_observed != complement_target:
            raise AssertionError(
                (assignment, complement_observed, complement_target)
            )
        complement_checks += 1

    if separator_checks != N**N or complement_checks != N**N:
        raise AssertionError((separator_checks, complement_checks))

    return {
        "positive_edge_graph": "K3,3 on {0,1,2}|{3,4,5}",
        "positive_edges": [list(edge) for edge in sorted(POSITIVE_EDGES)],
        "negative_edges": [
            list(edge) for edge in EDGES if edge not in POSITIVE_EDGES
        ],
        "pair_atom_count": 45,
        "uniform_correction_for_f": "-1/8",
        "uniform_correction_for_one_minus_f": "9/8",
        "total_atom_count": 46,
        "separator_assignment_checks": separator_checks,
        "one_minus_separator_assignment_checks": complement_checks,
        "separator_atomic_rank": 46,
        "one_minus_separator_atomic_rank": 46,
    }


def aggregate_formula_certificate() -> dict[str, object]:
    histogram: Counter[tuple[int, int]] = Counter()
    zero_bases: list[int] = []
    for base in range(32):
        constant_numerator = (
            character(TARGET_PARITY, base)
            - character(SEPARATOR_ONE_PARITY, base)
        )
        separator_numerator = (
            character(SEPARATOR_ONE_PARITY, base)
            - character(SEPARATOR_ZERO_PARITY, base)
        )
        histogram[(constant_numerator, separator_numerator)] += 1
        if constant_numerator == 0 and separator_numerator == 0:
            zero_bases.append(base)

    expected_histogram = Counter(
        {
            (0, 0): 8,
            (-2, 0): 4,
            (2, 0): 4,
            (0, -2): 4,
            (0, 2): 4,
            (-2, 2): 4,
            (2, -2): 4,
        }
    )
    if histogram != expected_histogram:
        raise AssertionError(histogram)
    if zero_bases != [0, 1, 6, 7, 24, 25, 30, 31]:
        raise AssertionError(zero_bases)

    constant_aggregates = histogram[(-2, 0)] + histogram[(2, 0)]
    nonconstant_aggregates = (
        histogram[(0, -2)]
        + histogram[(0, 2)]
        + histogram[(-2, 2)]
        + histogram[(2, -2)]
    )
    exact_cost = constant_aggregates + 46 * nonconstant_aggregates
    if (constant_aggregates, nonconstant_aggregates, exact_cost) != (8, 16, 744):
        raise AssertionError(
            (constant_aggregates, nonconstant_aggregates, exact_cost)
        )

    return {
        "coefficient_type_histogram": {
            f"{constant},{separator}": count
            for (constant, separator), count in sorted(histogram.items())
        },
        "zero_base_labels": zero_bases,
        "nonzero_constant_aggregate_count": constant_aggregates,
        "nonconstant_aggregate_count": nonconstant_aggregates,
        "exact_actual_term_cost_for_this_aggregate_assignment": exact_cost,
    }


def build_payload() -> dict[str, object]:
    local = local_dictionary_certificate()
    lower_bound = signed_edge_certificate()
    construction = construction_certificate()
    aggregate = aggregate_formula_certificate()

    return {
        "status": "N6_TWO_DEFECT_EXPLICIT_AGGREGATE_ATOMIC_RANK_COMPLETE",
        "field": "characteristic zero",
        "source_formula": "N6-020 quadratic separator and 24-base aggregate representation",
        "local_dictionary_certificate": local,
        "separator_lower_bound_certificate": lower_bound,
        "exact_construction_certificate": construction,
        "aggregate_formula_certificate": aggregate,
        "route_decision": {
            "separator_atomic_rank": 46,
            "one_minus_separator_atomic_rank": 46,
            "specific_24_base_aggregate_formula_actual_term_cost": 744,
            "specific_formula_can_yield_at_most_25_terms": False,
            "all_two_defect_decompositions_lower_bounded_by_744": False,
            "two_defect_minimum_term_support": "open",
            "next_compact_question": (
                "optimize the base-aggregate assignment itself, rather than "
                "decompressing the N6-020 separator formula"
            ),
            "broad_sparse_optimization_authorized": False,
        },
        "claim_boundary": (
            "The rank-46 result is exact for the fixed-base separator f and "
            "1-f. The total 744 is exact only for the explicit N6-020 "
            "base-aggregate assignment. Other aggregate assignments and the "
            "global two-defect minimum remain open."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_TWO_DEFECT_AGGREGATE_ATOMIC_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
