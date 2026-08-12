#!/usr/bin/env python3
"""Exact small Koszul profiles for four rank-20 sextic Chow terms.

The computation is deliberately local.  Every polynomial lives in its
four-, five-, or six-dimensional factor span.  Integer derivative and Koszul
columns are rebuilt from the displayed linear factors and ranked by exact
``Fraction`` elimination.  No floating point or finite-field arithmetic is
used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path
from typing import Iterable


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]
SparseColumn = dict[tuple[object, ...], int | Fraction]


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
            key = tuple(target)
            result[key] = result.get(key, 0) + coefficient * entry
    return result


def product_of_linears(
    linears: Iterable[tuple[int, ...]],
    variable_count: int,
) -> Polynomial:
    polynomial: Polynomial = {(0,) * variable_count: 1}
    for linear in linears:
        polynomial = multiply_by_linear(polynomial, linear)
    return polynomial


def differentiated_coefficient(
    polynomial: Polynomial,
    operator: Exponent,
    output: Exponent,
) -> int:
    source = tuple(a + b for a, b in zip(operator, output, strict=True))
    coefficient = polynomial.get(source, 0)
    if coefficient == 0:
        return 0
    for source_power, output_power in zip(source, output, strict=True):
        coefficient *= factorial(source_power) // factorial(output_power)
    return coefficient


def sparse_rank_fraction(columns: Iterable[SparseColumn]) -> int:
    """Column rank over Q, with sparse normalized pivot columns."""

    pivots: dict[tuple[object, ...], dict[tuple[object, ...], Fraction]] = {}
    for column in columns:
        work = {
            row: Fraction(value)
            for row, value in column.items()
            if value != 0
        }
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = work[pivot]
                pivots[pivot] = {
                    row: value / scale for row, value in work.items()
                }
                break
            scale = work[pivot]
            old = pivots[pivot]
            for row, value in old.items():
                updated = work.get(row, Fraction(0)) - scale * value
                if updated:
                    work[row] = updated
                else:
                    work.pop(row, None)
    return len(pivots)


def determinant_fraction(matrix: list[list[int]]) -> int:
    """Exact determinant of a small integer square matrix."""

    work = [[Fraction(entry) for entry in row] for row in matrix]
    determinant = Fraction(1)
    size = len(work)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant *= pivot_value
        for entry in range(column, size):
            work[column][entry] /= pivot_value
        for row in range(column + 1, size):
            scale = work[row][column]
            if not scale:
                continue
            for entry in range(column, size):
                work[row][entry] -= scale * work[column][entry]
    if determinant.denominator != 1:
        raise AssertionError(determinant)
    return determinant.numerator


def derivative_space_basis(
    polynomial: Polynomial,
    output_degree: int,
    variable_count: int,
) -> list[Polynomial]:
    outputs = compositions(output_degree, variable_count)
    operators = compositions(6 - output_degree, variable_count)
    candidates: list[Polynomial] = []
    for operator in operators:
        column = {
            output: coefficient
            for output in outputs
            if (
                coefficient := differentiated_coefficient(
                    polynomial,
                    operator,
                    output,
                )
            )
        }
        if column:
            candidates.append(column)

    basis: list[Polynomial] = []
    rank = 0
    for candidate in candidates:
        new_rank = sparse_rank_fraction([*basis, candidate])
        if new_rank > rank:
            basis.append(candidate)
            rank = new_rank
    return basis


def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def differentiate_polynomial(
    polynomial: Polynomial,
    variable: int,
) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[variable]
        if power == 0:
            continue
        target = list(exponent)
        target[variable] -= 1
        key = tuple(target)
        result[key] = result.get(key, 0) + power * coefficient
    return result


def koszul_columns(
    derivative_basis: list[Polynomial],
    wedge_degree: int,
    variable_count: int,
) -> list[SparseColumn]:
    columns: list[SparseColumn] = []
    for polynomial in derivative_basis:
        derivatives = [
            differentiate_polynomial(polynomial, variable)
            for variable in range(variable_count)
        ]
        for wedge in combinations(range(variable_count), wedge_degree):
            column: SparseColumn = {}
            for variable, derivative in enumerate(derivatives):
                if variable in wedge or not derivative:
                    continue
                output_wedge = tuple(sorted((variable,) + wedge))
                sign = insertion_sign(variable, wedge)
                for exponent, coefficient in derivative.items():
                    row = (exponent, output_wedge)
                    column[row] = column.get(row, 0) + sign * coefficient
            columns.append({row: value for row, value in column.items() if value})
    return columns


def determinant_3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def wedge_of_three(
    linears: list[tuple[int, ...]],
    variable_count: int,
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for wedge in combinations(range(variable_count), 3):
        value = determinant_3(
            [[linear[index] for linear in linears] for index in wedge]
        )
        if value:
            result[wedge] = value
    return result


def tensor_column(
    polynomial: Polynomial,
    wedge: dict[tuple[int, ...], int],
) -> SparseColumn:
    return {
        (exponent, exterior): coefficient * wedge_coefficient
        for exponent, coefficient in polynomial.items()
        for exterior, wedge_coefficient in wedge.items()
        if coefficient * wedge_coefficient
    }


def koszul_of_tensor_column(
    polynomial: Polynomial,
    wedge_vector: dict[tuple[int, ...], int],
    variable_count: int,
) -> SparseColumn:
    output: SparseColumn = {}
    derivatives = [
        differentiate_polynomial(polynomial, variable)
        for variable in range(variable_count)
    ]
    for wedge, wedge_coefficient in wedge_vector.items():
        for variable, derivative in enumerate(derivatives):
            if variable in wedge or not derivative:
                continue
            output_wedge = tuple(sorted((variable,) + wedge))
            sign = insertion_sign(variable, wedge)
            for exponent, coefficient in derivative.items():
                row = (exponent, output_wedge)
                output[row] = (
                    output.get(row, 0)
                    + wedge_coefficient * sign * coefficient
                )
    return {row: value for row, value in output.items() if value}


def koszul_of_sparse_domain_column(
    column: SparseColumn,
    variable_count: int,
) -> SparseColumn:
    """Apply the Koszul differential to a general sparse tensor column."""

    output: SparseColumn = {}
    for row, coefficient in column.items():
        exponent, wedge = row
        for variable in range(variable_count):
            power = exponent[variable]
            if power == 0 or variable in wedge:
                continue
            target = list(exponent)
            target[variable] -= 1
            output_wedge = tuple(sorted((variable,) + wedge))
            output_row = (tuple(target), output_wedge)
            output[output_row] = (
                output.get(output_row, 0)
                + coefficient
                * power
                * insertion_sign(variable, wedge)
            )
    return {row: value for row, value in output.items() if value}


def labelled_cycle_columns(
    factors: list[tuple[int, ...]],
) -> list[SparseColumn]:
    variable_count = len(factors[0])
    result: list[SparseColumn] = []
    for subset in combinations(range(6), 3):
        chosen = [factors[index] for index in subset]
        polynomial = product_of_linears(chosen, variable_count)
        wedge = wedge_of_three(chosen, variable_count)
        if not wedge:
            raise AssertionError(("dependent labelled triple", subset))
        if koszul_of_tensor_column(polynomial, wedge, variable_count):
            raise AssertionError(("labelled vector is not a cycle", subset))
        result.append(tensor_column(polynomial, wedge))
    return result


def configurations() -> list[dict[str, object]]:
    basis_five = [
        tuple(1 if index == coordinate else 0 for index in range(5))
        for coordinate in range(5)
    ]
    return [
        {
            "name": "span6_independent",
            "classification": "full factor-span orbit",
            "factors": [
                tuple(1 if index == coordinate else 0 for index in range(6))
                for coordinate in range(6)
            ],
        },
        {
            "name": "span5_support5",
            "classification": "five-span dependence normal form, support 5",
            "factors": [*basis_five, (1, 1, 1, 1, 1)],
        },
        {
            "name": "span5_support4",
            "classification": "five-span dependence normal form, support 4",
            "factors": [*basis_five, (1, 1, 1, 1, 0)],
        },
        {
            "name": "span4_uniform_witness",
            "classification": (
                "exact witness in the bracket-open four-span stratum; "
                "not a normal form for every point of that stratum"
            ),
            "factors": [
                (1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
                (1, 1, 1, 1),
                (1, 2, 3, 4),
            ],
        },
    ]


def audit_configuration(configuration: dict[str, object]) -> dict[str, object]:
    factors = list(configuration["factors"])
    variable_count = len(factors[0])
    polynomial = product_of_linears(factors, variable_count)
    bases = {
        degree: derivative_space_basis(polynomial, degree, variable_count)
        for degree in (2, 3, 4)
    }
    dimensions = {str(degree): len(bases[degree]) for degree in bases}
    if dimensions["3"] != 20:
        raise AssertionError((configuration["name"], dimensions))

    middle_ranks: list[int] = []
    preceding_ranks: list[int] = []
    homology: list[int] = []
    for wedge_degree in range(4):
        middle_rank = sparse_rank_fraction(
            koszul_columns(bases[3], wedge_degree, variable_count)
        )
        preceding_rank = (
            sparse_rank_fraction(
                koszul_columns(bases[4], wedge_degree - 1, variable_count)
            )
            if wedge_degree
            else 0
        )
        middle_ranks.append(middle_rank)
        preceding_ranks.append(preceding_rank)
        homology.append(
            dimensions["3"] * comb(variable_count, wedge_degree)
            - middle_rank
            - preceding_rank
        )

    inactive = 36 - variable_count
    ambient_rank = sum(
        comb(inactive, 3 - active_wedge) * middle_ranks[active_wedge]
        for active_wedge in range(4)
    )
    ambient_homology = sum(
        comb(inactive, 3 - active_wedge) * homology[active_wedge]
        for active_wedge in range(4)
    )

    cycles = labelled_cycle_columns(factors)
    boundaries = koszul_columns(bases[4], 2, variable_count)
    triple_products = [
        product_of_linears(
            [factors[index] for index in subset],
            variable_count,
        )
        for subset in combinations(range(6), 3)
    ]
    triple_product_rank = sparse_rank_fraction(triple_products)
    triple_products_in_middle_space = all(
        sparse_rank_fraction([*bases[3], product]) == dimensions["3"]
        for product in triple_products
    )
    if triple_product_rank != 20 or not triple_products_in_middle_space:
        raise AssertionError(
            (
                configuration["name"],
                triple_product_rank,
                triple_products_in_middle_space,
            )
        )
    boundaries_are_cycles = all(
        not koszul_of_sparse_domain_column(column, variable_count)
        for column in boundaries
    )
    if not boundaries_are_cycles:
        raise AssertionError((configuration["name"], "delta squared nonzero"))
    cycle_rank = sparse_rank_fraction(cycles)
    boundary_rank = sparse_rank_fraction(boundaries)
    combined_rank = sparse_rank_fraction([*boundaries, *cycles])

    profile = {
        "name": configuration["name"],
        "classification": configuration["classification"],
        "active_variable_count": variable_count,
        "active_derivative_dimensions": dimensions,
        "active_delta_3_ranks_wedge_0_to_3": middle_ranks,
        "active_preceding_delta_4_ranks_wedge_0_to_3": preceding_ranks,
        "active_homology_dimensions_wedge_0_to_3": homology,
        "ambient_36_variable_middle_third_koszul_rank": ambient_rank,
        "ambient_36_variable_H_3_6_dimension": ambient_homology,
        "labelled_factor_triple_cycles": {
            "count": len(cycles),
            "factor_triple_product_span_rank": triple_product_rank,
            "all_factor_triple_products_lie_in_D3": (
                triple_products_in_middle_space
            ),
            "all_are_cycles": True,
            "preceding_image_is_in_the_kernel": boundaries_are_cycles,
            "cycle_span_rank": cycle_rank,
            "boundary_rank_at_active_wedge_3": boundary_rank,
            "cycle_image_rank_modulo_boundaries": combined_rank
            - boundary_rank,
        },
    }
    if configuration["name"] == "span4_uniform_witness":
        bracket_minors = {
            "".join(str(index) for index in subset): determinant_fraction(
                [[factors[column][row] for column in subset] for row in range(4)]
            )
            for subset in combinations(range(6), 4)
        }
        if len(bracket_minors) != 15 or not all(bracket_minors.values()):
            raise AssertionError(bracket_minors)
        profile["four_span_bracket_open_certificate"] = {
            "minor_count": len(bracket_minors),
            "all_nonzero": True,
            "determinants": bracket_minors,
        }
    return profile


def build_payload() -> dict[str, object]:
    profiles = [audit_configuration(entry) for entry in configurations()]
    expected = {
        "span6_independent": ([0, 0, 0, 20], 133_545, 20, 20),
        "span5_support5": ([0, 0, 10, 10], 133_245, 320, 10),
        "span5_support4": ([0, 1, 20, 20], 133_055, 1_105, 16),
        "span4_uniform_witness": ([0, 25, 48, 25], 122_682, 13_961, 20),
    }
    for profile in profiles:
        wanted = expected[profile["name"]]
        observed = (
            profile["active_homology_dimensions_wedge_0_to_3"],
            profile["ambient_36_variable_middle_third_koszul_rank"],
            profile["ambient_36_variable_H_3_6_dimension"],
            profile["labelled_factor_triple_cycles"][
                "cycle_image_rank_modulo_boundaries"
            ],
        )
        if observed != wanted:
            raise AssertionError((profile["name"], observed, wanted))

    return {
        "status": "G035_EXACT_RANK20_CHOW_HOMOLOGY_PROFILES",
        "arithmetic": "integer reconstruction and exact Fraction elimination over Q",
        "profiles": profiles,
        "theorem": (
            "Central catalectic rank 20 does not determine scalar H_3,6: "
            "the four exact representatives have ambient dimensions "
            "20, 320, 1105, and 13961."
        ),
        "candidate_interface": (
            "The twenty factor-triple-labelled cycles define a natural "
            "labelled map, but their images modulo boundaries have ranks "
            "20, 10, 16, and 20. A universal labelled family over the "
            "factor-parameter ring, its Fitting ideals, and its colored "
            "coupling remain candidate invariants."
        ),
        "claim_boundary": (
            "These are exact characteristic-zero profiles for four displayed "
            "rank-20 configurations. The span-four entry is one bracket-open "
            "witness, not a classification of that whole stratum. The result "
            "rejects the naive scalar-homology-per-full-rank-term route; it "
            "does not prove ChowRank(perm_6)>=27 and makes no border-rank claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    if arguments.json:
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("G035_RANK20_CHOW_HOMOLOGY_PROFILES_PASS")


if __name__ == "__main__":
    main()
