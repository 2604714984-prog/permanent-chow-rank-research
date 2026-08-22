#!/usr/bin/env python3
"""Exact G-044 counterexample to a central defect-parity shortcut.

Two independent-factor sextic Chow terms have 20-dimensional middle spaces
whose sum has dimension 39.  Their unique middle relation is nonisotropic,
and the middle catalectic of the sum has the odd rank 39.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import factorial
from pathlib import Path


N = 6
TRIPLES = list(combinations(range(N), 3))
TRIPLE_INDEX = {triple: index for index, triple in enumerate(TRIPLES)}
FRAME = (
    (1, 1, 0, -1, 0, 0),
    (0, 0, 0, -1, 1, 0),
    (0, 0, 0, -1, 0, -1),
    (-1, 0, -1, 0, 0, 0),
    (0, 0, 1, 0, -1, 0),
    (-1, 0, 0, -1, 0, 1),
)
RELATION = (
    0, -1, 1, 0, 0, 0, 0, 0, -3, 3,
    -1, 1, 0, 0, 0, 0, 0, -3, 3, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    -2, 0, 0, 0, 1, 0, 0, 0, 0, 0,
)


def compositions(total: int, variables: int = N) -> list[tuple[int, ...]]:
    answer: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], remaining: int) -> None:
        if len(prefix) == variables - 1:
            answer.append(prefix + (remaining,))
            return
        for value in range(remaining + 1):
            rec(prefix + (value,), remaining - value)

    rec((), total)
    return answer


CUBIC_MONOMIALS = compositions(3)
CUBIC_INDEX = {monomial: index for index, monomial in enumerate(CUBIC_MONOMIALS)}


def exact_rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(rank + 1, len(work)):
            coefficient = work[row][column]
            if not coefficient:
                continue
            work[row] = [
                value - coefficient * pivot_value
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        for row in range(column + 1, len(work)):
            coefficient = work[row][column] / value
            for index in range(column, len(work)):
                work[row][index] -= coefficient * work[column][index]
    if result.denominator != 1:
        raise AssertionError(result)
    return result.numerator


def multiply_linear_forms(forms: tuple[tuple[int, ...], ...]) -> dict[tuple[int, ...], int]:
    polynomial = {(0,) * N: 1}
    for form in forms:
        new: dict[tuple[int, ...], int] = {}
        for exponent, coefficient in polynomial.items():
            for variable, value in enumerate(form):
                if not value:
                    continue
                target = list(exponent)
                target[variable] += 1
                key = tuple(target)
                new[key] = new.get(key, 0) + coefficient * value
        polynomial = new
    return {key: value for key, value in polynomial.items() if value}


def triple_product_columns(frame: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    columns: list[list[int]] = []
    for first, second, third in TRIPLES:
        column = [0] * len(CUBIC_MONOMIALS)
        for i, left in enumerate(frame[first]):
            for j, middle in enumerate(frame[second]):
                for k, right in enumerate(frame[third]):
                    value = left * middle * right
                    if not value:
                        continue
                    exponent = [0] * N
                    exponent[i] += 1
                    exponent[j] += 1
                    exponent[k] += 1
                    column[CUBIC_INDEX[tuple(exponent)]] += value
        columns.append(column)
    return columns


def catalectic_matrix(polynomial: dict[tuple[int, ...], int]) -> list[list[int]]:
    matrix: list[list[int]] = []
    for operator in CUBIC_MONOMIALS:
        row = []
        for output in CUBIC_MONOMIALS:
            source = tuple(a + b for a, b in zip(operator, output, strict=True))
            coefficient = polynomial.get(source, 0)
            for source_power, output_power in zip(source, output, strict=True):
                coefficient *= factorial(source_power) // factorial(output_power)
            row.append(coefficient)
        matrix.append(row)
    return matrix


def complement_pairing(vector: tuple[int, ...]) -> int:
    return sum(
        vector[index]
        * vector[TRIPLE_INDEX[tuple(value for value in range(N) if value not in triple)]]
        for index, triple in enumerate(TRIPLES)
    )


def audit() -> dict[str, object]:
    identity = tuple(
        tuple(1 if row == column else 0 for column in range(N))
        for row in range(N)
    )
    if determinant(FRAME) != 1:
        raise AssertionError(determinant(FRAME))

    first_columns = triple_product_columns(identity)
    second_columns = triple_product_columns(FRAME)
    concatenated = [
        [column[row] for column in first_columns + second_columns]
        for row in range(len(CUBIC_MONOMIALS))
    ]
    first_rank = exact_rank(
        [[column[row] for column in first_columns] for row in range(56)]
    )
    second_rank = exact_rank(
        [[column[row] for column in second_columns] for row in range(56)]
    )
    sum_rank = exact_rank(concatenated)
    relation_residual = [
        sum(row[column] * RELATION[column] for column in range(40))
        for row in concatenated
    ]
    if any(relation_residual):
        raise AssertionError(relation_residual)
    if (first_rank, second_rank, sum_rank) != (20, 20, 39):
        raise AssertionError((first_rank, second_rank, sum_rank))

    first_polynomial = multiply_linear_forms(identity)
    second_polynomial = multiply_linear_forms(FRAME)
    total_polynomial = dict(first_polynomial)
    for exponent, coefficient in second_polynomial.items():
        total_polynomial[exponent] = total_polynomial.get(exponent, 0) + coefficient
    direct_catalectic_rank = exact_rank(catalectic_matrix(total_polynomial))
    if direct_catalectic_rank != 39:
        raise AssertionError(direct_catalectic_rank)

    first_pairing = complement_pairing(RELATION[:20])
    second_pairing = complement_pairing(RELATION[20:])
    total_pairing = first_pairing + second_pairing
    if (first_pairing, second_pairing, total_pairing) != (-24, 0, -24):
        raise AssertionError((first_pairing, second_pairing, total_pairing))

    return {
        "status": "EXACT_N6_PAIRING_PARITY_COUNTEREXAMPLE",
        "arithmetic": "integer construction and exact rational elimination",
        "terms": {
            "T1": "x0*x1*x2*x3*x4*x5",
            "T2_factor_coefficient_rows": [list(row) for row in FRAME],
            "T2_factor_matrix_determinant": 1,
        },
        "middle_derivative_data": {
            "individual_ranks": [first_rank, second_rank],
            "sum_of_spaces_dimension": sum_rank,
            "intersection_dimension": first_rank + second_rank - sum_rank,
            "relation_dimension": 40 - sum_rank,
            "explicit_relation": list(RELATION),
            "explicit_relation_residual_is_zero": True,
        },
        "relation_pairing": {
            "first_component_value": first_pairing,
            "second_component_value": second_pairing,
            "total_value": total_pairing,
            "restricted_pairing_rank": 1,
            "relation_is_nonisotropic": True,
        },
        "direct_middle_catalectic_rank_of_T1_plus_T2": direct_catalectic_rank,
        "strict_conclusion": (
            "A one-dimensional central relation among full-middle-rank sextic "
            "Chow terms need not be isotropic. The central rank defect can be "
            "one, so neither even-defect nor relation-parity alone excludes "
            "the lower-28 b=34 endpoint."
        ),
        "claim_boundary": (
            "This is a two-term route counterexample. It is not a 27-term "
            "decomposition of perm_6, does not realize the b=34 relative "
            "position against E3(perm_6), and neither proves nor refutes the "
            "ordinary lower bound 28 or any border-rank statement."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = audit()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(f"middle_sum_dimension={payload['middle_derivative_data']['sum_of_spaces_dimension']}")
    print(f"relation_pairing={payload['relation_pairing']['total_value']}")
    print(f"direct_catalectic_rank={payload['direct_middle_catalectic_rank_of_T1_plus_T2']}")
    print("N6_PAIRING_PARITY_COUNTEREXAMPLE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
