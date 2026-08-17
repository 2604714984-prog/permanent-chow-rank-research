#!/usr/bin/env python3
"""Finite replay for the 2 x 2 linear matrix-image route barrier."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from math import comb
from pathlib import Path
from typing import Any


PRIME = 1_000_003

EXISTING_BOUNDARIES = {
    3: 4,
    4: 8,
    5: 16,
    6: 28,
    7: 49,
    8: 90,
    9: 164,
    10: 307,
}

EXPECTED_MAXIMAL_CEILINGS = {
    3: 3,
    4: 7,
    5: 10,
    6: 20,
    7: 35,
    8: 75,
    9: 126,
    10: 252,
}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def det2(matrix: tuple[int, int, int, int]) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def mixed_det(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
) -> int:
    return (
        left[0] * right[3]
        + right[0] * left[3]
        - left[1] * right[2]
        - right[1] * left[2]
    )


def proportional_vectors(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return all(
        left[i] * right[j] == left[j] * right[i]
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )


def span_dimension_at_most_one(vectors: list[tuple[int, int]]) -> bool:
    return all(
        left[0] * right[1] == left[1] * right[0]
        for index, left in enumerate(vectors)
        for right in vectors[index + 1 :]
    )


def classify_pencil(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
) -> str:
    if det2(left) or mixed_det(left, right) or det2(right):
        return "regular"

    if all(value == 0 for value in left + right):
        return "zero"

    if proportional_vectors(left, right):
        return "principal"

    # Columns of A and B span the common image space.
    columns = [
        (left[0], left[2]),
        (left[1], left[3]),
        (right[0], right[2]),
        (right[1], right[3]),
    ]
    common_image = span_dimension_at_most_one(columns)

    # Rows of A and B span the annihilator of a common kernel line.
    rows = [
        (left[0], left[1]),
        (left[2], left[3]),
        (right[0], right[1]),
        (right[2], right[3]),
    ]
    common_kernel = span_dimension_at_most_one(rows)

    require(common_image != common_kernel, (left, right, common_image, common_kernel))
    return "row_block" if common_image else "column_block"


def exhaustive_small_pencil_classification() -> dict[str, int]:
    counts = {
        "regular": 0,
        "principal": 0,
        "row_block": 0,
        "column_block": 0,
        "zero": 0,
    }
    for values in product((-1, 0, 1), repeat=8):
        category = classify_pencil(values[:4], values[4:])
        require(category in counts, category)
        counts[category] += 1
    require(sum(counts.values()) == 3**8, counts)
    require(all(value > 0 for value in counts.values()), counts)
    return counts


def subset_masks(n: int, degree: int) -> list[int]:
    if not 0 <= degree <= n:
        return []
    return [
        sum(1 << value for value in subset)
        for subset in combinations(range(n), degree)
    ]


def multiplication_matrix(
    n: int,
    source_degree: int,
    coefficients: list[int],
) -> list[list[int]]:
    require(len(coefficients) == n, (n, coefficients))
    source = subset_masks(n, source_degree)
    target = subset_masks(n, source_degree + 1)
    target_index = {mask: index for index, mask in enumerate(target)}
    matrix = [[0] * len(source) for _ in target]

    for column, mask in enumerate(source):
        for variable, coefficient in enumerate(coefficients):
            bit = 1 << variable
            if mask & bit:
                continue
            matrix[target_index[mask | bit]][column] = coefficient
    return matrix


def horizontal(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    require(len(left) == len(right), (len(left), len(right)))
    return [left_row + right_row for left_row, right_row in zip(left, right)]


def vertical(top: list[list[int]], bottom: list[list[int]]) -> list[list[int]]:
    if top and bottom:
        require(len(top[0]) == len(bottom[0]), (len(top[0]), len(bottom[0])))
    return top + bottom


def modular_rank(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = [[value % prime for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0

    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        rows[pivot_row] = [(value * inverse) % prime for value in rows[pivot_row]]

        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def gorenstein_row_column_checks() -> int:
    checks = 0
    for n in range(2, 9):
        first = [index + 1 for index in range(n)]
        second = [(index + 1) ** 2 + 1 for index in range(n)]

        for degree in range(1, n + 1):
            first_column = multiplication_matrix(n, degree - 1, first)
            second_column = multiplication_matrix(n, degree - 1, second)
            column_rank = modular_rank(vertical(first_column, second_column))

            complementary_output = n - degree + 1
            first_row = multiplication_matrix(n, complementary_output - 1, first)
            second_row = multiplication_matrix(n, complementary_output - 1, second)
            row_rank = modular_rank(horizontal(first_row, second_row))

            require(column_rank == row_rank, (n, degree, column_rank, row_rank))
            checks += 1
    require(checks == 35, checks)
    return checks


def primitive_hilbert(size: int) -> list[int]:
    previous = 0
    result = []
    for degree in range(size // 2 + 1):
        current = comb(size, degree)
        result.append(current - previous)
        previous = current
    return result


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def maximal_ideal_degree_ceiling(n: int, degree: int) -> int:
    first = n // 2
    second = n - first
    quotient = convolution(primitive_hilbert(first), primitive_hilbert(second))
    quotient_dimension = quotient[degree] if degree < len(quotient) else 0

    source = comb(n, degree - 1)
    target = comb(n, degree)
    principal_denominator = min(source, target)
    split_denominator = target - quotient_dimension
    denominator = max(principal_denominator, split_denominator)
    numerator = min(target * target, 2 * source * source)
    return ceil_div(numerator, denominator)


def route_ceiling_table() -> tuple[dict[str, Any], int]:
    table: dict[str, Any] = {}
    degree_cells = 0

    for n in range(3, 11):
        adjacent = max(
            min(comb(n, degree - 1), comb(n, degree))
            for degree in range(1, n + 1)
        )
        maximal_by_degree = {
            str(degree): maximal_ideal_degree_ceiling(n, degree)
            for degree in range(1, n + 1)
        }
        maximal = max(maximal_by_degree.values())
        require(maximal == EXPECTED_MAXIMAL_CEILINGS[n], (n, maximal))

        classes = {
            "regular": adjacent,
            "principal": adjacent,
            "row_block": maximal,
            "column_block": maximal,
            "zero": 0,
        }
        overall = max(classes.values())
        require(overall < EXISTING_BOUNDARIES[n], (n, overall, EXISTING_BOUNDARIES[n]))

        table[str(n)] = {
            "central_binomial": comb(n, n // 2),
            "existing_boundary": EXISTING_BOUNDARIES[n],
            "class_ceilings": classes,
            "overall_2x2_linear_ceiling": overall,
            "maximal_ideal_by_degree": maximal_by_degree,
        }
        degree_cells += n

    require(degree_cells == 52, degree_cells)
    return table, degree_cells


def build_payload() -> dict[str, Any]:
    classification = exhaustive_small_pencil_classification()
    duality_checks = gorenstein_row_column_checks()
    table, degree_cells = route_ceiling_table()

    return {
        "status": [
            "GENERAL_MATRIX_IMAGE_SUBQUOTIENT_MONOTONICITY",
            "GENERAL_2X2_LINEAR_PENCIL_CLASSIFICATION",
            "GENERAL_2X2_LINEAR_MATRIX_ROUTE_CEILING",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "monotonicity": (
                "For every homogeneous polynomial matrix Phi, image rank is "
                "additive on direct sums and nonincreasing under submodules "
                "and quotients."
            ),
            "classification": (
                "Every 2x2 linear pencil is regular, principal rank one, a "
                "row Kronecker block, a column Kronecker block, or zero."
            ),
            "regular_ceiling": (
                "Regular and principal classes prove at most "
                "binom(n,floor(n/2)) terms."
            ),
            "singular_blocks": (
                "The row block is the maximal-ideal profile and the column "
                "block is its Gorenstein-dual complementary-degree profile."
            ),
            "overall_ceiling": (
                "R_n^(2x2 linear)<=(1+O(n^(-1/2)))*"
                "binom(n,floor(n/2))."
            ),
        },
        "finite_replay": {
            "small_integer_pencils": 3**8,
            "classification_counts": classification,
            "gorenstein_row_column_rank_checks": duality_checks,
            "route_degree_cells": degree_cells,
            "rows": table,
            "prime": PRIME,
        },
        "claim_boundary": (
            "This is a route ceiling for fixed 2x2 linear matrix-image "
            "invariants, not an upper bound on Chow rank. It introduces no "
            "new numerical lower bound and does not close larger Kronecker "
            "blocks, higher-degree polynomial matrices, representation-valued "
            "modules, Fitting data, Chow-realizability defects, border rank or "
            "exact rank for n>=6. Literature novelty is not established."
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
    print("GENERAL_TWO_DIRECTION_LINEAR_MATRIX_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
