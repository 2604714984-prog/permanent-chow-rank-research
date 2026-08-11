#!/usr/bin/env python3
"""Exact audit of a six-term central relation-pairing counterexample.

All ranks are computed over ``Q`` with ``fractions.Fraction``.  The example
concerns a presentation by six squarefree degree-six Chow terms.  It is not
claimed that this presentation is a minimum Chow decomposition.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import ceil
from pathlib import Path


SUPPORTS = (
    (0, 2, 3, 4, 8, 9),
    (0, 1, 3, 6, 8, 9),
    (0, 4, 6, 7, 8, 9),
    (0, 2, 3, 6, 7, 9),
    (0, 1, 2, 7, 8, 9),
    (0, 1, 2, 4, 6, 9),
)


def pivot_columns_q(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    data = [[Fraction(value) for value in row] for row in matrix]
    rows = len(data)
    columns = len(data[0])
    pivot_row = 0
    pivots: list[int] = []
    for column in range(columns):
        source = next(
            (row for row in range(pivot_row, rows) if data[row][column]),
            None,
        )
        if source is None:
            continue
        data[pivot_row], data[source] = data[source], data[pivot_row]
        scale = data[pivot_row][column]
        data[pivot_row] = [value / scale for value in data[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not data[row][column]:
                continue
            scale = data[row][column]
            data[row] = [
                data[row][index] - scale * data[pivot_row][index]
                for index in range(columns)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivots


def rank_q(matrix: list[list[int]]) -> int:
    return len(pivot_columns_q(matrix))


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []
    return [list(column) for column in zip(*matrix)]


def bareiss_determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    if size == 0:
        return 1
    data = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(size - 1):
        source = next(
            (row for row in range(column, size) if data[row][column]),
            None,
        )
        if source is None:
            return 0
        if source != column:
            data[column], data[source] = data[source], data[column]
            sign *= -1
        pivot = data[column][column]
        for row in range(column + 1, size):
            for target in range(column + 1, size):
                numerator = (
                    data[row][target] * pivot
                    - data[row][column] * data[column][target]
                )
                if numerator % previous:
                    raise AssertionError((numerator, previous))
                data[row][target] = numerator // previous
        previous = pivot
    return sign * data[-1][-1]


def exact_rank_certificate(matrix: list[list[int]]) -> dict[str, object]:
    columns = pivot_columns_q(matrix)
    column_basis = [[row[column] for column in columns] for row in matrix]
    rows = pivot_columns_q(transpose(column_basis))
    minor = [[matrix[row][column] for column in columns] for row in rows]
    determinant = bareiss_determinant(minor)
    if determinant == 0 or len(rows) != len(columns):
        raise AssertionError((rows, columns, determinant))
    return {
        "rank_over_Q": len(columns),
        "minor_rows_zero_based": rows,
        "minor_columns_zero_based": columns,
        "minor_determinant": determinant,
    }


def relation_basis(degree: int) -> tuple[
    list[tuple[int, tuple[int, ...]]],
    dict[tuple[int, tuple[int, ...]], int],
    list[list[int]],
]:
    coordinates: list[tuple[int, tuple[int, ...]]] = []
    occurrences: dict[tuple[int, ...], list[int]] = {}
    for term, support in enumerate(SUPPORTS):
        for monomial in combinations(support, degree):
            coordinates.append((term, monomial))
            occurrences.setdefault(monomial, []).append(term)
    position = {coordinate: index for index, coordinate in enumerate(coordinates)}
    basis: list[list[int]] = []
    for monomial, terms in sorted(occurrences.items()):
        for term in terms[1:]:
            vector = [0] * len(coordinates)
            vector[position[(terms[0], monomial)]] = -1
            vector[position[(term, monomial)]] = 1
            basis.append(vector)
    return coordinates, position, basis


def occurrence_distribution(degree: int) -> dict[str, int]:
    occurrences: dict[tuple[int, ...], int] = {}
    for support in SUPPORTS:
        for monomial in combinations(support, degree):
            occurrences[monomial] = occurrences.get(monomial, 0) + 1
    distribution: dict[str, int] = {}
    for multiplicity in occurrences.values():
        key = str(multiplicity)
        distribution[key] = distribution.get(key, 0) + 1
    return dict(sorted(distribution.items(), key=lambda item: int(item[0])))


def central_pairing_matrix(
    coordinates: list[tuple[int, tuple[int, ...]]],
    position: dict[tuple[int, tuple[int, ...]], int],
    relation_basis_vectors: list[list[int]],
) -> list[list[int]]:
    support_sets = [set(support) for support in SUPPORTS]

    def pairing(first: list[int], second: list[int]) -> int:
        value = 0
        for index, coefficient in enumerate(first):
            if not coefficient:
                continue
            term, monomial = coordinates[index]
            complement = tuple(sorted(support_sets[term] - set(monomial)))
            value += coefficient * second[position[(term, complement)]]
        return value

    return [
        [pairing(first, second) for second in relation_basis_vectors]
        for first in relation_basis_vectors
    ]


def central_catalectic_matrix(
    supports: tuple[tuple[int, ...], ...], degree: int
) -> list[list[int]]:
    variables = sorted(set().union(*(set(support) for support in supports)))
    monomials = list(combinations(variables, degree))
    position = {monomial: index for index, monomial in enumerate(monomials)}
    matrix = [[0] * len(monomials) for _ in monomials]
    for support in supports:
        support_set = set(support)
        for monomial in combinations(support, degree):
            complement = tuple(sorted(support_set - set(monomial)))
            if len(complement) != degree:
                raise ValueError("central degree required")
            matrix[position[monomial]][position[complement]] += 1
    return matrix


def derivative_shadow() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    coordinates_three, position_three, relations_three = relation_basis(3)
    coordinates_four, _, relations_four = relation_basis(4)
    shadows: list[list[int]] = []
    for relation in relations_four:
        for variable in range(10):
            derivative = [0] * len(coordinates_three)
            for index, coefficient in enumerate(relation):
                if not coefficient:
                    continue
                term, monomial = coordinates_four[index]
                if variable not in monomial:
                    continue
                output = tuple(value for value in monomial if value != variable)
                derivative[position_three[(term, output)]] += coefficient
            if any(derivative):
                shadows.append(derivative)
    return shadows, relations_three, central_pairing_matrix(
        coordinates_three, position_three, relations_three
    )


def build_payload() -> dict[str, object]:
    coordinates_three, position_three, relations_three = relation_basis(3)
    _, _, relations_four = relation_basis(4)
    pairing = central_pairing_matrix(
        coordinates_three, position_three, relations_three
    )
    pairing_certificate = exact_rank_certificate(pairing)
    relation_dimension = len(relations_three)
    pairing_rank = int(pairing_certificate["rank_over_Q"])
    radical_dimension = relation_dimension - pairing_rank

    central_matrix = central_catalectic_matrix(SUPPORTS, 3)
    central_certificate = exact_rank_certificate(central_matrix)
    central_rank = int(central_certificate["rank_over_Q"])
    formula_rank = 6 * 20 - 2 * relation_dimension + pairing_rank
    if central_rank != formula_rank:
        raise AssertionError((central_rank, formula_rank))

    shadows, relations_three_again, pairing_again = derivative_shadow()
    if relations_three_again != relations_three or pairing_again != pairing:
        raise AssertionError("inconsistent reconstruction")
    for shadow in shadows:
        coefficient_sums: dict[tuple[int, ...], int] = {}
        for index, coefficient in enumerate(shadow):
            if coefficient:
                _, monomial = coordinates_three[index]
                coefficient_sums[monomial] = (
                    coefficient_sums.get(monomial, 0) + coefficient
                )
        if any(coefficient_sums.values()):
            raise AssertionError(("shadow is not a relation", coefficient_sums))
    shadow_dimension = rank_q(shadows)
    support_sets = [set(support) for support in SUPPORTS]
    shadow_pairing = []
    for shadow in shadows:
        row = []
        for relation in relations_three:
            value = 0
            for index, coefficient in enumerate(shadow):
                if not coefficient:
                    continue
                term, monomial = coordinates_three[index]
                complement = tuple(
                    sorted(support_sets[term] - set(monomial))
                )
                value += coefficient * relation[
                    position_three[(term, complement)]
                ]
            row.append(value)
        shadow_pairing.append(row)

    common = set.intersection(*(set(support) for support in SUPPORTS))
    residual_supports = tuple(
        tuple(sorted(set(support) - common)) for support in SUPPORTS
    )
    residual_central = central_catalectic_matrix(residual_supports, 2)
    residual_rank = rank_q(residual_central)

    if radical_dimension <= 4 * (len(SUPPORTS) - 1):
        raise AssertionError(radical_dimension)
    if shadow_dimension != relation_dimension:
        raise AssertionError((shadow_dimension, relation_dimension))

    return {
        "method": "exact-rational-central-relation-pairing",
        "field": "Q",
        "degree": 6,
        "term_count": len(SUPPORTS),
        "supports": [list(support) for support in SUPPORTS],
        "central_relation_dimension": relation_dimension,
        "central_triple_occurrence_distribution": occurrence_distribution(3),
        "central_pairing": pairing_certificate,
        "central_pairing_radical_dimension": radical_dimension,
        "naive_four_times_q_minus_one_cap": 4 * (len(SUPPORTS) - 1),
        "central_catalectic": central_certificate,
        "central_rank_from_pairing_identity": formula_rank,
        "degree_four_relation_dimension": len(relations_four),
        "degree_four_occurrence_distribution": occurrence_distribution(4),
        "raw_derivative_shadow_generator_count": len(shadows),
        "raw_derivative_shadow_dimension": shadow_dimension,
        "raw_derivative_shadow_equals_central_relation_space": True,
        "shadow_to_central_relation_pairing_rank": rank_q(shadow_pairing),
        "common_factor_variables": sorted(common),
        "residual_quartic_supports": [list(support) for support in residual_supports],
        "residual_quartic_C22_rank_over_Q": residual_rank,
        "residual_quartic_flattening_lower_bound": ceil(residual_rank / 6),
        "strict_scope": (
            "This disproves the radical cap for arbitrary six-term presentations. "
            "The six-term presentation is not proved minimum, so it does not "
            "disprove a version restricted to minimum Chow decompositions."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
