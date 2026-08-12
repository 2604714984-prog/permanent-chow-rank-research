#!/usr/bin/env python3
"""Exact small-matrix barrier for the factor-labelled cycle interface.

The calculation lives in six variables.  Two sparse pairs are eliminated over
``Fraction``.  A five-term witness is certified modulo the prime 1,000,003;
the modular rank reaches the characteristic-independent Koszul upper bound,
so it is an exact characteristic-zero conclusion.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path


PRIME = 1_000_003
Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]
Row = tuple[Exponent, tuple[int, ...]]
Column = dict[Row, int]


def multiply_by_linear(polynomial: Polynomial, linear: tuple[int, ...]) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        for variable, value in enumerate(linear):
            if not value:
                continue
            target = list(exponent)
            target[variable] += 1
            key = tuple(target)
            result[key] = result.get(key, 0) + coefficient * value
    return result


def product_of_linears(linears: list[tuple[int, ...]]) -> Polynomial:
    polynomial: Polynomial = {(0, 0, 0, 0, 0, 0): 1}
    for linear in linears:
        polynomial = multiply_by_linear(polynomial, linear)
    return polynomial


def determinant_integer(matrix: list[list[int]]) -> int:
    """Small exact determinant by Fraction elimination."""

    work = [[Fraction(value) for value in row] for row in matrix]
    determinant = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant *= -1
        scale = work[column][column]
        determinant *= scale
        for entry in range(column, len(work)):
            work[column][entry] /= scale
        for row in range(column + 1, len(work)):
            scale = work[row][column]
            if not scale:
                continue
            for entry in range(column, len(work)):
                work[row][entry] -= scale * work[column][entry]
    if determinant.denominator != 1:
        raise AssertionError(determinant)
    return determinant.numerator


def derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    result: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[variable]
        if not power:
            continue
        target = list(exponent)
        target[variable] -= 1
        key = tuple(target)
        result[key] = result.get(key, 0) + power * coefficient
    return result


def iterated_derivative(polynomial: Polynomial, variables: tuple[int, ...]) -> Polynomial:
    result = polynomial
    for variable in variables:
        result = derivative(result, variable)
    return result


def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(index < variable for index in wedge) % 2 else 1


def koszul_column(polynomial: Polynomial, wedge: tuple[int, ...]) -> Column:
    column: Column = {}
    for variable in range(6):
        if variable in wedge:
            continue
        differentiated = derivative(polynomial, variable)
        output_wedge = tuple(sorted((variable,) + wedge))
        sign = insertion_sign(variable, wedge)
        for exponent, coefficient in differentiated.items():
            row = (exponent, output_wedge)
            column[row] = column.get(row, 0) + sign * coefficient
    return {row: value for row, value in column.items() if value}


def boundary_columns(factors: list[tuple[int, ...]]) -> list[Column]:
    """Columns of d(D_4(T) tensor Lambda^2 V), with harmless redundancy."""

    return [
        koszul_column(
            product_of_linears([factors[index] for index in factor_subset]),
            wedge,
        )
        for factor_subset in combinations(range(6), 4)
        for wedge in combinations(range(6), 2)
    ]


def determinant_3(matrix: list[list[int]]) -> int:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def wedge_three(linears: list[tuple[int, ...]]) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for wedge in combinations(range(6), 3):
        value = determinant_3(
            [[linear[coordinate] for linear in linears] for coordinate in wedge]
        )
        if value:
            result[wedge] = value
    return result


def labelled_cycles(factors: list[tuple[int, ...]]) -> list[Column]:
    columns: list[Column] = []
    for subset in combinations(range(6), 3):
        chosen = [factors[index] for index in subset]
        polynomial = product_of_linears(chosen)
        exterior = wedge_three(chosen)
        if not exterior:
            raise AssertionError(("dependent factor triple", subset))
        column = {
            (exponent, wedge): coefficient * wedge_coefficient
            for exponent, coefficient in polynomial.items()
            for wedge, wedge_coefficient in exterior.items()
            if coefficient * wedge_coefficient
        }
        if koszul_general_column(column):
            raise AssertionError(("labelled vector is not a cycle", subset))
        columns.append(column)
    return columns


def koszul_general_column(column: Column) -> dict[tuple[Exponent, tuple[int, ...]], int]:
    output: dict[tuple[Exponent, tuple[int, ...]], int] = {}
    for (exponent, wedge), coefficient in column.items():
        for variable, power in enumerate(exponent):
            if not power or variable in wedge:
                continue
            target = list(exponent)
            target[variable] -= 1
            output_wedge = tuple(sorted((variable,) + wedge))
            row = (tuple(target), output_wedge)
            output[row] = (
                output.get(row, 0)
                + coefficient * power * insertion_sign(variable, wedge)
            )
    return {row: value for row, value in output.items() if value}


def rank_fraction(columns: list[dict[object, int]]) -> int:
    pivots: dict[object, dict[object, Fraction]] = {}
    for column in columns:
        work = {row: Fraction(value) for row, value in column.items() if value}
        while work:
            pivot = min(work)
            if pivot not in pivots:
                scale = work[pivot]
                pivots[pivot] = {row: value / scale for row, value in work.items()}
                break
            scale = work[pivot]
            for row, value in pivots[pivot].items():
                updated = work.get(row, Fraction(0)) - scale * value
                if updated:
                    work[row] = updated
                else:
                    work.pop(row, None)
    return len(pivots)


def verify_derivative_product_spaces(factors: list[tuple[int, ...]]) -> dict[str, int]:
    """Check that the labelled product models are the actual D3 and D4 spaces."""

    term = product_of_linears(factors)
    result: dict[str, int] = {}
    for output_degree, derivative_order in ((3, 3), (4, 2)):
        factor_products = [
            product_of_linears([factors[index] for index in subset])
            for subset in combinations(range(6), output_degree)
        ]
        derivatives = [
            iterated_derivative(term, operator)
            for operator in combinations_with_replacement(range(6), derivative_order)
        ]
        product_rank = rank_fraction(factor_products)
        derivative_rank = rank_fraction(derivatives)
        combined_rank = rank_fraction([*factor_products, *derivatives])
        if not (product_rank == derivative_rank == combined_rank):
            raise AssertionError(
                (output_degree, product_rank, derivative_rank, combined_rank)
            )
        result[f"D{output_degree}_dimension"] = derivative_rank
    return result


def compositions(total: int, parts: int) -> list[Exponent]:
    if parts == 1:
        return [(total,)]
    return [
        (first,) + rest
        for first in range(total + 1)
        for rest in compositions(total - first, parts - 1)
    ]


def universal_middle_kernel_dimension() -> tuple[int, int]:
    domain = [
        {(exponent, wedge): 1}
        for exponent in compositions(3, 6)
        for wedge in combinations(range(6), 3)
    ]
    differential_rank = rank_fraction(
        [koszul_general_column(column) for column in domain]
    )
    return len(domain), len(domain) - differential_rank


class ModularRankCertificate:
    def __init__(self, prime: int = PRIME) -> None:
        self.prime = prime
        self.pivots: dict[Row, dict[Row, int]] = {}
        self.selected_column_count = 0
        self.pivot_product = 1

    def add(self, columns: list[Column]) -> int:
        for column in columns:
            work = {
                row: value % self.prime
                for row, value in column.items()
                if value % self.prime
            }
            while work:
                pivot = min(work)
                scale = work[pivot]
                if pivot not in self.pivots:
                    self.selected_column_count += 1
                    self.pivot_product = self.pivot_product * scale % self.prime
                    inverse = pow(scale, self.prime - 2, self.prime)
                    self.pivots[pivot] = {
                        row: value * inverse % self.prime
                        for row, value in work.items()
                    }
                    break
                for row, value in self.pivots[pivot].items():
                    updated = (work.get(row, 0) - scale * value) % self.prime
                    if updated:
                        work[row] = updated
                    else:
                        work.pop(row, None)
        return len(self.pivots)


def factor_columns(matrix: list[list[int]]) -> list[tuple[int, ...]]:
    return [tuple(matrix[row][column] for row in range(6)) for column in range(6)]


IDENTITY = [[1 if row == column else 0 for column in range(6)] for row in range(6)]
UPPER_ONES = [[1 if row <= column else 0 for column in range(6)] for row in range(6)]
CYCLIC_NEIGHBOUR = [
    [1 if row == column or row == (column + 1) % 6 else 0 for column in range(6)]
    for row in range(6)
]
SATURATING_MATRICES = [
    IDENTITY,
    [[2, 1, 1, -1, -2, 1], [-2, -1, -1, -1, 1, 0], [1, 2, 2, 1, 1, 1], [-1, 0, -2, -1, 1, 1], [-2, 1, -2, 1, -2, 1], [1, 2, -1, 1, 1, -1]],
    [[-2, 0, 1, -2, -1, -2], [-2, -2, 0, 2, -2, -2], [-2, 1, 0, 0, -1, 0], [-1, -2, -1, -2, -2, 0], [0, 0, 0, -2, -1, 1], [-1, 0, 0, 1, -1, 2]],
    [[1, 2, 1, -1, -1, 1], [1, -1, -1, 1, 1, 2], [0, 1, 1, 0, 2, 1], [-1, 2, -2, 2, 0, 1], [-1, 0, 0, -1, 2, -1], [-1, 1, -2, 0, -1, -1]],
    [[-1, 0, 2, 0, 2, 0], [0, 2, 0, 1, -2, 2], [0, -2, -1, 1, -1, 0], [2, -2, 0, -2, 1, -1], [2, 1, -2, 2, -2, -1], [2, -2, 2, 1, 1, 0]],
]


def pair_profile(second_matrix: list[list[int]], name: str) -> dict[str, object]:
    spaces = []
    derivative_dimensions = []
    for matrix in (IDENTITY, second_matrix):
        factors = factor_columns(matrix)
        derivative_dimensions.append(verify_derivative_product_spaces(factors))
        spaces.append((boundary_columns(factors), labelled_cycles(factors)))
    boundary_0, cycles_0 = spaces[0]
    boundary_1, cycles_1 = spaces[1]
    boundary = boundary_0 + boundary_1
    boundary_rank = rank_fraction(boundary)
    cycle_rank = rank_fraction(cycles_0 + cycles_1)
    survive_0 = rank_fraction(boundary + cycles_0) - boundary_rank
    survive_1 = rank_fraction(boundary + cycles_1) - boundary_rank
    joint = rank_fraction(boundary + cycles_0 + cycles_1) - boundary_rank
    return {
        "name": name,
        "arithmetic": "exact Fraction elimination over Q",
        "verified_derivative_dimensions": derivative_dimensions,
        "individual_boundary_ranks": [rank_fraction(boundary_0), rank_fraction(boundary_1)],
        "boundary_sum_rank": boundary_rank,
        "boundary_intersection_dimension": 380 - boundary_rank,
        "individual_cycle_ranks": [rank_fraction(cycles_0), rank_fraction(cycles_1)],
        "cycle_sum_rank": cycle_rank,
        "cycle_intersection_dimension": 40 - cycle_rank,
        "individual_images_modulo_aggregate_boundary": [survive_0, survive_1],
        "intersection_of_the_two_quotient_images": survive_0 + survive_1 - joint,
        "joint_labelled_presentation_rank": joint,
        "joint_kernel_dimension": 40 - joint,
    }


def build_payload() -> dict[str, object]:
    pair_profiles = [
        pair_profile(UPPER_ONES, "two_full_span_terms"),
        pair_profile(CYCLIC_NEIGHBOUR, "full_span_plus_uniform_five_span_term"),
    ]
    expected_pairs = {
        "two_full_span_terms": (380, [19, 17], 3, 33, 7),
        "full_span_plus_uniform_five_span_term": (380, [20, 10], 2, 28, 12),
    }
    for profile in pair_profiles:
        observed = (
            profile["boundary_sum_rank"],
            profile["individual_images_modulo_aggregate_boundary"],
            profile["intersection_of_the_two_quotient_images"],
            profile["joint_labelled_presentation_rank"],
            profile["joint_kernel_dimension"],
        )
        if observed != expected_pairs[profile["name"]]:
            raise AssertionError((profile["name"], observed))

    certificate = ModularRankCertificate()
    progression = []
    factor_determinants = [determinant_integer(matrix) for matrix in SATURATING_MATRICES]
    if factor_determinants != [1, 184, -68, 9, -15]:
        raise AssertionError(factor_determinants)
    all_cycles: list[Column] = []
    for matrix in SATURATING_MATRICES:
        factors = factor_columns(matrix)
        boundary = boundary_columns(factors)
        all_cycles.extend(labelled_cycles(factors))
        progression.append(certificate.add(boundary))
    if progression != [190, 380, 570, 760, 840]:
        raise AssertionError(progression)
    if certificate.selected_column_count != 840 or certificate.pivot_product == 0:
        raise AssertionError((certificate.selected_column_count, certificate.pivot_product))
    if any(koszul_general_column(column) for column in all_cycles):
        raise AssertionError("a labelled column left the universal kernel")

    universal_domain_dimension, universal_kernel_dimension = (
        universal_middle_kernel_dimension()
    )
    if (universal_domain_dimension, universal_kernel_dimension) != (1120, 840):
        raise AssertionError((universal_domain_dimension, universal_kernel_dimension))

    return {
        "status": "G037_LABELLED_CYCLE_FITTING_ROUTE_BLOCKED",
        "field": "characteristic zero",
        "definition": (
            "For a tuple of factored sextics, the aggregate labelled presentation "
            "is the sum of its twenty factor-triple cycles, mapped to the universal "
            "third-Koszul kernel modulo the sum of the term boundary spaces."
        ),
        "two_term_exact_profiles": pair_profiles,
        "five_full_span_saturation_certificate": {
            "prime": PRIME,
            "factor_matrix_integer_determinants": factor_determinants,
            "boundary_rank_progression_mod_prime": progression,
            "universal_domain_dimension": universal_domain_dimension,
            "universal_kernel_dimension": universal_kernel_dimension,
            "selected_boundary_column_count": certificate.selected_column_count,
            "triangular_minor_diagonal_product_mod_prime": certificate.pivot_product,
            "labelled_cycle_count": len(all_cycles),
            "aggregate_labelled_presentation_rank": 0,
            "positive_fitting_minors": "all vanish because the specialized map is zero",
        },
        "theorem": (
            "Five explicit full-factor-span rank-20 Chow terms have aggregate "
            "boundary sum equal to the entire 840-dimensional universal Koszul "
            "kernel. Consequently all one hundred factor-labelled cycles vanish "
            "in the aggregate quotient and every positive determinantal/Fitting "
            "rank of this quotient presentation is zero."
        ),
        "claim_boundary": (
            "This is a route counterexample, not a permanent decomposition and not "
            "a Chow-rank or border-rank bound. It blocks counting full-middle-rank "
            "summands with the uncolored aggregate-boundary quotient. A genuinely "
            "colored or equation-coupled presentation may still work."
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
    print("G037_LABELLED_CYCLE_FITTING_BARRIER_PASS")


if __name__ == "__main__":
    main()
