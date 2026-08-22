#!/usr/bin/env python3
"""Exact audit for the missing-rank-19 theorem for sextic Chow terms.

The accompanying proof is geometric.  This script replays its two finite
interfaces over the integers/rationals:

* the five-dimensional factor-span normal forms; and
* one nonvanishing four-dimensional central determinant, together with the
  squared bracket product at that witness.

No finite-field or floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import factorial
from pathlib import Path
from typing import Iterable


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def compositions(total: int, parts: int) -> list[Exponent]:
    if parts == 1:
        return [(total,)]
    return [
        (first,) + rest
        for first in range(total + 1)
        for rest in compositions(total - first, parts - 1)
    ]


def multiply_by_linear(
    polynomial: Polynomial,
    linear: tuple[int, ...],
) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        for index, entry in enumerate(linear):
            if entry == 0:
                continue
            target = list(exponent)
            target[index] += 1
            target_exponent = tuple(target)
            result[target_exponent] = (
                result.get(target_exponent, 0) + coefficient * entry
            )
    return result


def product_of_linears(linears: Iterable[tuple[int, ...]]) -> Polynomial:
    linears = list(linears)
    variables = len(linears[0])
    polynomial: Polynomial = {(0,) * variables: 1}
    for linear in linears:
        polynomial = multiply_by_linear(polynomial, linear)
    return polynomial


def middle_catalectic_matrix(polynomial: Polynomial) -> list[list[int]]:
    variables = len(next(iter(polynomial)))
    monomials = compositions(3, variables)
    matrix: list[list[int]] = []
    for operator in monomials:
        row: list[int] = []
        for output in monomials:
            source = tuple(
                operator[index] + output[index]
                for index in range(variables)
            )
            coefficient = polynomial.get(source, 0)
            if coefficient:
                for source_power, output_power in zip(
                    source,
                    output,
                    strict=True,
                ):
                    coefficient *= factorial(source_power) // factorial(
                        output_power
                    )
            row.append(coefficient)
        matrix.append(row)
    return matrix


def exact_rank(matrix: list[list[int]]) -> int:
    data = [[Fraction(entry) for entry in row] for row in matrix]
    if not data:
        return 0
    rows = len(data)
    columns = len(data[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (
                row
                for row in range(pivot_row, rows)
                if data[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        scale = data[pivot_row][column]
        data[pivot_row] = [entry / scale for entry in data[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = data[row][column]
            if scale == 0:
                continue
            data[row] = [
                data[row][index] - scale * data[pivot_row][index]
                for index in range(columns)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def bareiss_determinant(matrix: list[list[int]]) -> int:
    if not matrix:
        return 1
    data = [row[:] for row in matrix]
    size = len(data)
    if any(len(row) != size for row in data):
        raise ValueError("determinant requires a square matrix")
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot_row = next(
            (
                row
                for row in range(column, size)
                if data[row][column] != 0
            ),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            data[column], data[pivot_row] = data[pivot_row], data[column]
            sign *= -1
        pivot = data[column][column]
        for row in range(column + 1, size):
            for target in range(column + 1, size):
                numerator = (
                    data[row][target] * pivot
                    - data[row][column] * data[column][target]
                )
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Bareiss division was not exact")
                data[row][target] = quotient
            data[row][column] = 0
        previous = pivot
    return sign * data[-1][-1]


def bracket(
    linears: list[tuple[int, ...]],
    indices: tuple[int, ...],
) -> int:
    matrix = [
        [linears[column][row] for column in indices]
        for row in range(4)
    ]
    return bareiss_determinant(matrix)


def span_five_profiles() -> dict[str, int]:
    basis = [
        tuple(1 if index == coordinate else 0 for index in range(5))
        for coordinate in range(5)
    ]
    result: dict[str, int] = {}
    for support_size in range(1, 6):
        final = tuple(
            1 if index < support_size else 0 for index in range(5)
        )
        polynomial = product_of_linears([*basis, final])
        result[str(support_size)] = exact_rank(
            middle_catalectic_matrix(polynomial)
        )
    return result


def build_payload() -> dict[str, object]:
    profiles = span_five_profiles()
    expected_profiles = {"1": 14, "2": 14, "3": 18, "4": 20, "5": 20}
    if profiles != expected_profiles:
        raise AssertionError(profiles)

    independent_six = {(1, 1, 1, 1, 1, 1): 1}
    span_six_rank = exact_rank(middle_catalectic_matrix(independent_six))
    if span_six_rank != 20:
        raise AssertionError(span_six_rank)

    witness = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (1, 1, 1, 1),
        (1, 2, 3, 4),
    ]
    witness_matrix = middle_catalectic_matrix(product_of_linears(witness))
    witness_determinant = bareiss_determinant(witness_matrix)
    bracket_values = {
        "".join(str(index + 1) for index in indices): bracket(witness, indices)
        for indices in combinations(range(6), 4)
    }
    bracket_product_squared = 1
    for value in bracket_values.values():
        bracket_product_squared *= value * value
    constant, remainder = divmod(
        witness_determinant,
        bracket_product_squared,
    )
    if remainder or constant != 2304**2:
        raise AssertionError(
            (witness_determinant, bracket_product_squared, constant, remainder)
        )

    dependent_witness = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (1, 1, 1, 0),
        (1, 2, 4, 8),
    ]
    dependent_rank = exact_rank(
        middle_catalectic_matrix(product_of_linears(dependent_witness))
    )
    if dependent_rank != 18:
        raise AssertionError(dependent_rank)

    return {
        "arithmetic": "exact integers and Fraction over Q",
        "theorem": (
            "A nonzero degree-six Chow term over characteristic zero never "
            "has middle catalectic rank 19."
        ),
        "factor_span_at_most_three_rank_cap": 10,
        "factor_span_four": {
            "determinant_formula": (
                "det(C_3,3)=2304^2*product_{|I|=4}[I]^2 in the stated "
                "standard derivative and monomial bases"
            ),
            "full_rank_witness": [list(vector) for vector in witness],
            "witness_rank": exact_rank(witness_matrix),
            "witness_determinant": witness_determinant,
            "bracket_values": bracket_values,
            "bracket_product_squared": bracket_product_squared,
            "formula_constant": constant,
            "dependent_witness_rank": dependent_rank,
            "consequence": (
                "all four-subsets independent gives rank 20; any dependent "
                "four-subset gives corank at least two"
            ),
        },
        "factor_span_five_support_profiles": profiles,
        "factor_span_six_rank": span_six_rank,
        "excluded_middle_rank": 19,
        "claim_boundary": (
            "This is a single-Chow-term rank-gap theorem. It does not prove "
            "ChowRank(perm_6)>=27 or determine ChowRank(perm_6)."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_SINGLE_TERM_MIDDLE_RANK_GAP_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
