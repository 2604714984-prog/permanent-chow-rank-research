#!/usr/bin/env python3
"""Lightweight exact regression for the pure N6-068 product theorem."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_34_actual_pair_exclusion.json"
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def determinant_polynomial() -> dict[tuple[int, ...], int]:
    """Determinant of the generic zero-diagonal symmetric 4 by 4 matrix."""
    polynomial: dict[tuple[int, ...], int] = {}
    for permutation in permutations(range(4)):
        if any(permutation[row] == row for row in range(4)):
            continue
        monomial = []
        for row, column in enumerate(permutation):
            monomial.append(EDGE_INDEX[tuple(sorted((row, column)))])
        key = tuple(sorted(monomial))
        polynomial[key] = polynomial.get(key, 0) + permutation_sign(permutation)
    return {key: value for key, value in polynomial.items() if value}


def rank_q(matrix: list[list[Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    row = 0
    width = len(work[0]) if work else 0
    for column in range(width):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        value = work[row][column]
        work[row] = [entry / value for entry in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            value = work[index][column]
            work[index] = [
                left - value * right
                for left, right in zip(work[index], work[row])
            ]
        row += 1
    return row


def inverse_q(matrix: list[list[int]]) -> list[list[Fraction]]:
    size = len(matrix)
    work = [
        [Fraction(value) for value in row]
        + [Fraction(index == column) for column in range(size)]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(index for index in range(column, size) if work[index][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for index in range(size):
            if index == column or not work[index][column]:
                continue
            value = work[index][column]
            work[index] = [
                left - value * right
                for left, right in zip(work[index], work[column])
            ]
    return [row[size:] for row in work]


def multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    size = len(left)
    return [
        [sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)]
        for i in range(size)
    ]


def ratio_algebra_dimension() -> int:
    p0 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    p0_inverse = inverse_q(p0)
    generators = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        matrix = [[Fraction(0) for _ in range(3)] for _ in range(3)]
        matrix[i][j] = matrix[j][i] = Fraction(1)
        generators.append(multiply(matrix, p0_inverse))

    basis: list[list[list[Fraction]]] = []

    def add(matrix: list[list[Fraction]]) -> bool:
        flattened = [sum(item, []) for item in basis + [matrix]]
        if rank_q(flattened) == len(basis) + 1:
            basis.append(matrix)
            return True
        return False

    for generator in generators:
        add(generator)
    while True:
        old_dimension = len(basis)
        for left in basis[:]:
            for right in basis[:]:
                add(multiply(left, right))
        if len(basis) == old_dimension:
            return len(basis)


def build_payload() -> dict[str, object]:
    polynomial = determinant_polynomial()
    expected = {
        (0, 0, 5, 5): 1,
        (1, 1, 4, 4): 1,
        (2, 2, 3, 3): 1,
        (0, 1, 4, 5): -2,
        (0, 2, 3, 5): -2,
        (1, 2, 3, 4): -2,
    }
    if polynomial != expected:
        raise AssertionError(polynomial)
    avoiding = {
        str(edge): next(
            list(monomial)
            for monomial, coefficient in polynomial.items()
            if coefficient and EDGE_INDEX[edge] not in monomial
        )
        for edge in EDGES
    }
    branches = [
        [p, q]
        for p in range(4)
        for q in range(7)
        if p * q >= 15
    ]
    algebra_dimension = ratio_algebra_dimension()
    if branches != [[3, 5], [3, 6]] or algebra_dimension != 9:
        raise AssertionError((branches, algebra_dimension))
    return {
        "status": [
            "PURE_PRODUCT_34_ACTUAL_PAIR_EXCLUSION",
            "EXACT_QQ_SYMBOLIC_REGRESSION",
            "N6-068",
        ],
        "dimension_gate": {
            "p_upper_bound": 3,
            "q_upper_bound": 6,
            "minimum_product_dimension": 15,
            "surviving_pairs": branches,
        },
        "s0_four_determinant": {
            "edge_order": [list(edge) for edge in EDGES],
            "monomial_coefficients": {
                ",".join(map(str, monomial)): coefficient
                for monomial, coefficient in sorted(polynomial.items())
            },
            "coordinate_absent_matching_monomial": avoiding,
            "has_no_coordinate_linear_factor": True,
        },
        "s0_three_ratio_algebra": {
            "representative_p0": [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
            "exact_QQ_algebra_dimension": algebra_dimension,
            "full_endomorphism_dimension": 9,
        },
        "q5_projection_contradiction": {
            "actual_projection_rank": 15,
            "forced_product_projection_upper_bound": 9,
        },
        "q6_interface": {
            "recovered_space": "S0(A3) tensor S0(B4)",
            "excluded_by": "N6-063 fixed K3,4 rank-nine Fano theorem",
        },
        "claim_boundary": (
            "This pure theorem excludes actual complementary pairs only when the "
            "twelve-plane shadow is a product A3 tensor B4 or its transpose. It "
            "does not classify arbitrary twelve-planes, exclude the full b=50 "
            "endpoint, prove ChowRank(perm_6)>=28, or make a border-rank claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    actual = build_payload()
    expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit("certificate differs from frozen JSON")
    print("N6-068 PASS")


if __name__ == "__main__":
    main()
