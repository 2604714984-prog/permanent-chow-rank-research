#!/usr/bin/env python3
"""Exact replay of a two-term central/Koszul transversality separation.

The construction uses two products of six independent linear forms in six
variables.  Their middle derivative spaces are disjoint, while their ordinary
first-Koszul images intersect in dimension 18.  All ranks are computed over
``Fraction`` from coefficient constraints; no finite field or floating point
is used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path


N = 6
Monomial = tuple[int, ...]


def monomials(degree: int) -> list[Monomial]:
    return list(combinations_with_replacement(range(N), degree))


MONOMIALS = {degree: monomials(degree) for degree in (2, 3, 4)}
INDEX = {
    degree: {monomial: position for position, monomial in enumerate(items)}
    for degree, items in MONOMIALS.items()
}


def multiply(forms: list[list[int]]) -> dict[Monomial, int]:
    polynomial: dict[Monomial, int] = {(): 1}
    for form in forms:
        product: dict[Monomial, int] = {}
        for monomial, coefficient in polynomial.items():
            for variable, scalar in enumerate(form):
                if scalar == 0:
                    continue
                lifted = tuple(sorted((*monomial, variable)))
                product[lifted] = product.get(lifted, 0) + coefficient * scalar
        polynomial = product
    return polynomial


def coefficient_vector(forms: list[list[int]], degree: int) -> list[Fraction]:
    vector = [Fraction(0) for _ in MONOMIALS[degree]]
    for monomial, coefficient in multiply(forms).items():
        vector[INDEX[degree][monomial]] = Fraction(coefficient)
    return vector


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def rref(
    matrix: list[list[Fraction]],
) -> tuple[list[list[Fraction]], list[int]]:
    reduced = [row[:] for row in matrix]
    if not reduced:
        return reduced, []
    row = 0
    pivots: list[int] = []
    for column in range(len(reduced[0])):
        pivot = next(
            (index for index in range(row, len(reduced)) if reduced[index][column]),
            None,
        )
        if pivot is None:
            continue
        reduced[row], reduced[pivot] = reduced[pivot], reduced[row]
        scale = reduced[row][column]
        reduced[row] = [entry / scale for entry in reduced[row]]
        for other in range(len(reduced)):
            if other == row or not reduced[other][column]:
                continue
            factor = reduced[other][column]
            reduced[other] = [
                left - factor * right
                for left, right in zip(reduced[other], reduced[row])
            ]
        pivots.append(column)
        row += 1
        if row == len(reduced):
            break
    return reduced, pivots


def rank(matrix: list[list[Fraction]]) -> int:
    return len(rref(matrix)[1])


def nullspace(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    columns = len(matrix[0])
    free = [column for column in range(columns) if column not in pivots]
    basis: list[list[Fraction]] = []
    for free_column in free:
        vector = [Fraction(0) for _ in range(columns)]
        vector[free_column] = 1
        for pivot_row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[pivot_row][free_column]
        basis.append(vector)
    return basis


def factor_families() -> tuple[list[list[int]], list[list[int]]]:
    coordinate = [
        [int(row == column) for column in range(N)] for row in range(N)
    ]
    transformed = [
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1],
    ]
    return coordinate, transformed


def derivative_basis(factors: list[list[int]], degree: int) -> list[list[Fraction]]:
    return [
        coefficient_vector([factors[index] for index in subset], degree)
        for subset in combinations(range(6), degree)
    ]


def prolongation_dimension(central_columns: list[list[Fraction]]) -> int:
    central_matrix = transpose(central_columns)
    annihilators = nullspace(transpose(central_matrix))
    if len(annihilators) != 16:
        raise AssertionError(len(annihilators))

    constraints: list[list[Fraction]] = []
    for direction in range(N):
        for annihilator in annihilators:
            row = [Fraction(0) for _ in MONOMIALS[4]]
            for position, monomial in enumerate(MONOMIALS[4]):
                multiplicity = monomial.count(direction)
                if multiplicity == 0:
                    continue
                derivative = list(monomial)
                derivative.remove(direction)
                row[position] = (
                    multiplicity * annihilator[INDEX[3][tuple(derivative)]]
                )
            constraints.append(row)
    return len(MONOMIALS[4]) - rank(constraints)


def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def internal_koszul_rank(
    central_columns: list[list[Fraction]],
    wedge_degree: int,
) -> int:
    if wedge_degree == N:
        return 0
    source_wedges = list(combinations(range(N), wedge_degree))
    target_wedges = list(combinations(range(N), wedge_degree + 1))
    target_wedge_index = {
        wedge: index for index, wedge in enumerate(target_wedges)
    }
    columns: list[list[Fraction]] = []
    row_count = len(MONOMIALS[2]) * len(target_wedges)
    for cubic in central_columns:
        for wedge in source_wedges:
            wedge_set = set(wedge)
            column = [Fraction(0) for _ in range(row_count)]
            for position, monomial in enumerate(MONOMIALS[3]):
                coefficient = cubic[position]
                if not coefficient:
                    continue
                for variable in set(monomial):
                    if variable in wedge_set:
                        continue
                    derivative = list(monomial)
                    multiplicity = derivative.count(variable)
                    derivative.remove(variable)
                    output_wedge = tuple(sorted((variable,) + wedge))
                    row = (
                        INDEX[2][tuple(derivative)] * len(target_wedges)
                        + target_wedge_index[output_wedge]
                    )
                    column[row] += (
                        coefficient
                        * multiplicity
                        * insertion_sign(variable, wedge)
                    )
            columns.append(column)
    return rank(transpose(columns))


def ambient_rank(
    internal_ranks: list[int],
    wedge_degree: int,
    ambient_dimension: int = 36,
) -> int:
    inactive = ambient_dimension - N
    return sum(
        comb(inactive, inactive_wedge)
        * internal_ranks[wedge_degree - inactive_wedge]
        for inactive_wedge in range(wedge_degree + 1)
        if 0 <= wedge_degree - inactive_wedge < len(internal_ranks)
    )


def determinant(matrix: list[list[int]]) -> int:
    rational = [[Fraction(entry) for entry in row] for row in matrix]
    value = Fraction(1)
    sign = 1
    for column in range(len(rational)):
        pivot = next(index for index in range(column, len(rational)) if rational[index][column])
        if pivot != column:
            rational[column], rational[pivot] = rational[pivot], rational[column]
            sign *= -1
        diagonal = rational[column][column]
        value *= diagonal
        for row in range(column + 1, len(rational)):
            factor = rational[row][column] / diagonal
            for other in range(column, len(rational)):
                rational[row][other] -= factor * rational[column][other]
    result = sign * value
    if result.denominator != 1:
        raise AssertionError(result)
    return result.numerator


def build_payload() -> dict[str, object]:
    first, second = factor_families()
    first_central = derivative_basis(first, 3)
    second_central = derivative_basis(second, 3)
    central_columns = first_central + second_central
    central_rank = rank(transpose(central_columns))
    if central_rank != 40:
        raise AssertionError(central_rank)

    first_fourth = derivative_basis(first, 4)
    second_fourth = derivative_basis(second, 4)
    fourth_literal_rank = rank(transpose(first_fourth + second_fourth))
    if fourth_literal_rank != 30:
        raise AssertionError(fourth_literal_rank)

    prolongation = prolongation_dimension(central_columns)
    if prolongation != 48:
        raise AssertionError(prolongation)

    one_term_rank = N * 20 - 15
    combined_rank = N * central_rank - prolongation
    intersection = 2 * one_term_rank - combined_rank
    if (one_term_rank, combined_rank, intersection) != (105, 192, 18):
        raise AssertionError((one_term_rank, combined_rank, intersection))

    internal_profile = [
        internal_koszul_rank(central_columns, wedge_degree)
        for wedge_degree in range(N + 1)
    ]
    expected_internal_profile = [40, 192, 336, 280, 120, 21, 0]
    if internal_profile != expected_internal_profile:
        raise AssertionError(internal_profile)
    one_term_internal_profile = [20, 105, 216, 190, 84, 15, 0]
    internal_intersections = [
        2 * one_term - combined
        for one_term, combined in zip(
            one_term_internal_profile,
            internal_profile,
            strict=True,
        )
    ]
    expected_internal_intersections = [0, 18, 96, 100, 48, 9, 0]
    if internal_intersections != expected_internal_intersections:
        raise AssertionError(internal_intersections)
    ambient_third_rank = ambient_rank(internal_profile, 3)
    one_term_ambient_third_rank = 133_545
    ambient_third_intersection = (
        2 * one_term_ambient_third_rank - ambient_third_rank
    )
    if (ambient_third_rank, ambient_third_intersection) != (256_280, 10_810):
        raise AssertionError((ambient_third_rank, ambient_third_intersection))

    triangle = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    square_coefficient_map = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    return {
        "status": "EXACT_TWO_CHOW_CENTRAL_KOSZUL_COLLISION_REPLAY",
        "field": "Q",
        "method": "exact coefficient constraints over Fraction",
        "three_factor_change_determinant": determinant(triangle),
        "pencil_conciseness_square_map_determinant": determinant(
            square_coefficient_map
        ),
        "individual_middle_ranks": [20, 20],
        "combined_literal_middle_rank": central_rank,
        "middle_image_intersection_dimension": 0,
        "individual_fourth_derivative_ranks": [15, 15],
        "combined_literal_fourth_rank": fourth_literal_rank,
        "central_sum_first_prolongation_dimension": prolongation,
        "individual_first_koszul_ranks": [one_term_rank, one_term_rank],
        "combined_first_koszul_image_rank": combined_rank,
        "first_koszul_image_intersection_dimension": intersection,
        "all_internal_wedge_koszul_ranks": internal_profile,
        "one_term_internal_wedge_koszul_ranks": one_term_internal_profile,
        "all_internal_wedge_intersection_dimensions": internal_intersections,
        "ambient_36_middle_third_koszul_rank": ambient_third_rank,
        "ambient_36_two_individual_third_koszul_rank_sum": (
            2 * one_term_ambient_third_rank
        ),
        "ambient_36_third_koszul_intersection_dimension": (
            ambient_third_intersection
        ),
        "claim_boundary": (
            "This is a two-term counterexample to inferring Koszul "
            "transversality at either first or higher wedge degree from "
            "central-image transversality. It is not a decomposition of a "
            "permanent and gives no Chow-rank upper bound."
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
    print("TWO_CHOW_CENTRAL_KOSZUL_COLLISION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
