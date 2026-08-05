#!/usr/bin/env python3
"""Exact parity-block diagnostic for the ``n=6`` two-defect sign family.

A two-defect term has one normalized base sign vector in four columns and may
use independent defect sign vectors in two designated columns.  Fourier
transformation in the base label identifies each parity block with the
restriction of the global pairwise-interaction function space.

This script uses exact ``Fraction`` elimination to compute the six canonical
block ranks.  It also verifies an explicit quadratic separator between two
non-target parity fibers and the resulting 24-base aggregate representation
of ``perm_6``.  The aggregate representation is not a 24-term decomposition:
each base aggregate may require several two-defect terms.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

N = 6
BITS = N - 1
GROUP_SIZE = 1 << BITS
TARGET_PARITY = GROUP_SIZE - 1
SEPARATOR_ZERO_PARITY = 7
SEPARATOR_ONE_PARITY = 25
CHECK_PRIME = 1_000_033
PAIRS = tuple(combinations(range(N), 2))
PAIRWISE_DIMENSION = 1 + N * (N - 1) + len(PAIRS) * (N - 1) ** 2

Assignment = tuple[int, ...]
SparseRow = dict[int, Fraction]


def character(left: int, right: int) -> int:
    return -1 if (left & right).bit_count() & 1 else 1


def row_character(row: int) -> int:
    return 0 if row == 0 else 1 << (row - 1)


def assignment_parity(assignment: Assignment) -> int:
    value = 0
    for row in assignment:
        value ^= row_character(row)
    return value


def parity_fibers() -> dict[int, list[Assignment]]:
    result: dict[int, list[Assignment]] = defaultdict(list)
    for assignment in product(range(N), repeat=N):
        result[assignment_parity(assignment)].append(assignment)
    if sum(map(len, result.values())) != N**N:
        raise AssertionError("parity fibers do not partition the ambient basis")
    return dict(result)


def pairwise_feature_row(assignment: Assignment) -> SparseRow:
    """Canonical ANOVA basis: constant, unary contrasts, pure pair features."""

    row: SparseRow = {0: Fraction(1)}
    unary_offset = 1
    for position, value in enumerate(assignment):
        if value:
            row[unary_offset + position * (N - 1) + value - 1] = Fraction(1)

    pair_offset = 1 + N * (N - 1)
    for pair_index, (left, right) in enumerate(PAIRS):
        left_value = assignment[left]
        right_value = assignment[right]
        if left_value and right_value:
            index = (
                pair_offset
                + pair_index * (N - 1) ** 2
                + (left_value - 1) * (N - 1)
                + right_value
                - 1
            )
            row[index] = Fraction(1)
    return row


def sparse_rank_q(rows: Iterable[SparseRow]) -> int:
    """Exact sparse row-echelon rank over ``Q``."""

    pivots: dict[int, SparseRow] = {}
    for raw in rows:
        vector = dict(raw)
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                if coefficient != 1:
                    vector = {
                        column: value / coefficient
                        for column, value in vector.items()
                    }
                pivots[pivot] = vector
                break
            for column, value in existing.items():
                updated = (
                    vector.get(column, Fraction(0))
                    - coefficient * value
                )
                if updated:
                    vector[column] = updated
                else:
                    vector.pop(column, None)
    return len(pivots)


def sparse_rank_mod(rows: Iterable[SparseRow], prime: int = CHECK_PRIME) -> int:
    """Independent finite-field cross-check of the exact rational rank."""

    pivots: dict[int, dict[int, int]] = {}
    for raw in rows:
        vector = {
            column: (value.numerator * pow(value.denominator, prime - 2, prime))
            % prime
            for column, value in raw.items()
            if value
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(coefficient, prime - 2, prime)
                if coefficient != 1:
                    vector = {
                        column: value * inverse % prime
                        for column, value in vector.items()
                    }
                pivots[pivot] = vector
                break
            for column, value in existing.items():
                updated = (vector.get(column, 0) - coefficient * value) % prime
                if updated:
                    vector[column] = updated
                else:
                    vector.pop(column, None)
    return len(pivots)


def canonical_block_rows() -> tuple[list[dict[str, int]], dict[int, list[Assignment]]]:
    fibers = parity_fibers()
    expected_sizes = [2256, 1712, 1712, 1200, 1200, 720]
    expected_ranks = [406, 406, 406, 322, 322, 207]
    rows: list[dict[str, int]] = []

    for weight in range(BITS + 1):
        parity = (1 << weight) - 1 if weight else 0
        assignments = fibers[parity]
        exact_rank = sparse_rank_q(
            pairwise_feature_row(assignment) for assignment in assignments
        )
        modular_rank = sparse_rank_mod(
            pairwise_feature_row(assignment) for assignment in assignments
        )
        observed = (len(assignments), exact_rank, modular_rank)
        expected = (
            expected_sizes[weight],
            expected_ranks[weight],
            expected_ranks[weight],
        )
        if observed != expected:
            raise AssertionError((weight, observed, expected))
        rows.append(
            {
                "parity_weight": weight,
                "canonical_parity": parity,
                "fiber_size": len(assignments),
                "exact_characteristic_zero_rank": exact_rank,
                "modular_crosscheck_rank": modular_rank,
                "kernel_dimension_in_pairwise_space": (
                    PAIRWISE_DIMENSION - exact_rank
                ),
            }
        )
    return rows, fibers


def separator_value(assignment: Assignment) -> Fraction:
    """Quadratic function that is zero on ``X_7`` and one on ``X_25``."""

    indicators = [row in {2, 3} for row in assignment]
    signs = [1 if row == 2 else -1 if row == 3 else 0 for row in assignment]
    value = Fraction(1) - Fraction(sum(indicators), 4)
    value += Fraction(
        sum(
            signs[left] * signs[right]
            for left, right in PAIRS
        ),
        2,
    )
    return value


def separator_certificate(fibers: dict[int, list[Assignment]]) -> dict[str, object]:
    zero_values = Counter(
        separator_value(assignment)
        for assignment in fibers[SEPARATOR_ZERO_PARITY]
    )
    one_values = Counter(
        separator_value(assignment)
        for assignment in fibers[SEPARATOR_ONE_PARITY]
    )
    if zero_values != Counter({Fraction(0): 1200}):
        raise AssertionError(zero_values)
    if one_values != Counter({Fraction(1): 1200}):
        raise AssertionError(one_values)

    return {
        "zero_parity": SEPARATOR_ZERO_PARITY,
        "one_parity": SEPARATOR_ONE_PARITY,
        "zero_fiber_size": 1200,
        "one_fiber_size": 1200,
        "formula": (
            "1 - (1/4)*sum_j 1_{r_j in {2,3}} "
            "+ (1/2)*sum_{j<k} z_j*z_k, "
            "z_j=1_{r_j=2}-1_{r_j=3}"
        ),
        "zero_fiber_values": {"0": 1200},
        "one_fiber_values": {"1": 1200},
    }


def aggregate_coefficients(base: int) -> tuple[int, int]:
    """Numerators of the constant and separator coefficients in ``32 W_a``."""

    target = character(TARGET_PARITY, base)
    one = character(SEPARATOR_ONE_PARITY, base)
    zero = character(SEPARATOR_ZERO_PARITY, base)
    return target - one, one - zero


def aggregate_representation_certificate(
    fibers: dict[int, list[Assignment]],
) -> dict[str, object]:
    zero_bases: list[int] = []
    coefficient_type_histogram: Counter[tuple[int, int]] = Counter()
    for base in range(GROUP_SIZE):
        coefficients = aggregate_coefficients(base)
        coefficient_type_histogram[coefficients] += 1
        if coefficients == (0, 0):
            zero_bases.append(base)

    expected_zero_bases = [0, 1, 6, 7, 24, 25, 30, 31]
    if zero_bases != expected_zero_bases:
        raise AssertionError(zero_bases)

    correct = 0
    for parity, assignments in fibers.items():
        for assignment in assignments:
            separator = separator_value(assignment)
            total = Fraction(0)
            for base in range(GROUP_SIZE):
                constant_numerator, separator_numerator = (
                    aggregate_coefficients(base)
                )
                total += Fraction(character(parity, base), GROUP_SIZE) * (
                    constant_numerator
                    + separator_numerator * separator
                )
            expected = Fraction(
                int(tuple(sorted(assignment)) == tuple(range(N)))
            )
            if total != expected:
                raise AssertionError((assignment, parity, total, expected))
            correct += 1

    if correct != N**N:
        raise AssertionError(correct)
    if len(zero_bases) != 8:
        raise AssertionError(zero_bases)

    return {
        "formula": (
            "W_a=(chi_31(a)-chi_25(a) "
            "+ (chi_25(a)-chi_7(a))*f)/32"
        ),
        "zero_base_labels": zero_bases,
        "nonzero_base_aggregate_count": GROUP_SIZE - len(zero_bases),
        "coefficient_type_histogram": {
            f"{constant},{separator}": count
            for (constant, separator), count in sorted(
                coefficient_type_histogram.items()
            )
        },
        "exact_assignment_checks": correct,
        "logical_role": (
            "exact representation in the sum of 24 base-labelled pairwise "
            "aggregate spaces; not a 24-term decomposition"
        ),
    }


def build_payload() -> dict[str, object]:
    if PAIRWISE_DIMENSION != 406:
        raise AssertionError(PAIRWISE_DIMENSION)
    blocks, fibers = canonical_block_rows()
    separator = separator_certificate(fibers)
    aggregate = aggregate_representation_certificate(fibers)

    unique_terms = (
        GROUP_SIZE
        + N * GROUP_SIZE * (GROUP_SIZE - 1)
        + len(PAIRS) * GROUP_SIZE * (GROUP_SIZE - 1) ** 2
    )
    indexed_terms = len(PAIRS) * GROUP_SIZE**3
    if unique_terms != 467_264 or indexed_terms != 491_520:
        raise AssertionError((unique_terms, indexed_terms))

    block_rank_by_weight = {
        row["parity_weight"]: row["exact_characteristic_zero_rank"]
        for row in blocks
    }
    span_dimension = (
        (1 + 5 + 10) * block_rank_by_weight[0]
        + (10 + 5) * block_rank_by_weight[3]
        + block_rank_by_weight[5]
    )
    if span_dimension != 11_533:
        raise AssertionError(span_dimension)

    return {
        "status": "N6_TWO_DEFECT_SIGN_BLOCK_DIAGNOSTIC_COMPLETE",
        "field": "characteristic zero",
        "family": {
            "global_pairwise_function_dimension": PAIRWISE_DIMENSION,
            "indexed_term_count_with_duplicates": indexed_terms,
            "unique_term_count": unique_terms,
            "canonical_block_rows": blocks,
            "exact_span_dimension": span_dimension,
        },
        "separator_certificate": separator,
        "aggregate_representation_certificate": aggregate,
        "route_decision": {
            "one_defect_32_base_support_argument_extends": False,
            "two_defect_base_aggregate_support_upper_bound": 24,
            "two_defect_term_support_determined": False,
            "decomposition_with_at_most_25_terms_found": False,
            "general_chow_rank_changed": False,
            "broad_sparse_optimization_authorized": False,
        },
        "claim_boundary": (
            "The exact block ranks and 24-base aggregate representation do "
            "not determine the minimum number of two-defect terms. Each base "
            "aggregate can require several rank-one sign products. No new "
            "upper or lower bound for unrestricted Chow rank is claimed."
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
    print("N6_TWO_DEFECT_SIGN_BLOCK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
