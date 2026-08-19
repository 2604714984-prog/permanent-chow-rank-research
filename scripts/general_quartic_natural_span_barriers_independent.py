#!/usr/bin/env python3
"""Independent finite replay for the quartic natural-span barriers.

This file imports none of the primary implementation. It expands the six
Laplace summands as sparse monomial dictionaries, differentiates them directly,
and computes rational ranks. It also reconstructs the eight sign tensors on
all 256 ordered coordinates and enumerates the low-mode-rank projective points
over several odd prime fields as a diagnostic for the characteristic-zero
parity proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product, permutations
from typing import Mapping, Sequence


def check(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_q(rows: Sequence[Sequence[int | Fraction]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    if not matrix:
        return 0
    columns = len(matrix[0])
    pivot_row = 0
    for column in range(columns):
        pivot = None
        for candidate in range(pivot_row, len(matrix)):
            if matrix[candidate][column] != 0:
                pivot = candidate
                break
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for candidate in range(pivot_row + 1, len(matrix)):
            value = matrix[candidate][column]
            if value:
                matrix[candidate] = [
                    left - value * right
                    for left, right in zip(
                        matrix[candidate], matrix[pivot_row], strict=True
                    )
                ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def variable(row: int, column: int) -> int:
    return 4 * row + column


def laplace_polynomials() -> tuple[
    tuple[tuple[int, int], dict[tuple[int, ...], int]], ...
]:
    result = []
    all_columns = set(range(4))
    for left in combinations(range(4), 2):
        right = tuple(sorted(all_columns - set(left)))
        polynomial: dict[tuple[int, ...], int] = {}
        for top in permutations(left):
            for bottom in permutations(right):
                monomial = tuple(
                    sorted(
                        (
                            variable(0, top[0]),
                            variable(1, top[1]),
                            variable(2, bottom[0]),
                            variable(3, bottom[1]),
                        )
                    )
                )
                polynomial[monomial] = polynomial.get(monomial, 0) + 1
        check(
            len(polynomial) == 4 and set(polynomial.values()) == {1},
            polynomial,
        )
        result.append((left, polynomial))
    return tuple(result)


def derivative(
    polynomial: Mapping[tuple[int, ...], int], selected: int
) -> dict[tuple[int, ...], int]:
    output: dict[tuple[int, ...], int] = {}
    for monomial, coefficient in polynomial.items():
        if selected in monomial:
            reduced = tuple(value for value in monomial if value != selected)
            output[reduced] = output.get(reduced, 0) + coefficient
    return {
        monomial: coefficient
        for monomial, coefficient in output.items()
        if coefficient
    }


def essential_rank(polynomial: Mapping[tuple[int, ...], int]) -> int:
    derivative_rows = [
        derivative(polynomial, selected) for selected in range(16)
    ]
    monomials = sorted(set().union(*(set(row) for row in derivative_rows)))
    matrix = [
        [row.get(monomial, 0) for monomial in monomials]
        for row in derivative_rows
    ]
    return rank_q(matrix)


def independent_laplace_audit() -> dict[str, object]:
    basis = laplace_polynomials()
    all_supports = [set(polynomial) for _, polynomial in basis]
    check(len(set().union(*all_supports)) == 24, all_supports)
    check(sum(map(len, all_supports)) == 24, "Laplace monomial overlap")

    distribution: Counter[int] = Counter()
    profile_distribution: Counter[tuple[int, int, int]] = Counter()
    for mask in range(1, 1 << 6):
        polynomial: dict[tuple[int, ...], int] = {}
        chosen_edges = []
        for index, (edge, summand) in enumerate(basis):
            if mask >> index & 1:
                chosen_edges.append(edge)
                for monomial, coefficient in summand.items():
                    polynomial[monomial] = polynomial.get(monomial, 0) + coefficient
        rank = essential_rank(polynomial)
        top = set().union(*(set(edge) for edge in chosen_edges))
        bottom = set().union(
            *(set(range(4)) - set(edge) for edge in chosen_edges)
        )
        formula = 2 * len(top) + 2 * len(bottom)
        check(rank == formula, (mask, rank, formula))
        distribution[rank] += 1
        profile_distribution[(len(top), len(bottom), rank)] += 1

    check(
        distribution == Counter({8: 6, 12: 12, 14: 8, 16: 37}),
        distribution,
    )
    return {
        "basis_size": 6,
        "monomials_per_basis_vector": 4,
        "permanent_monomials": 24,
        "supports_checked": 63,
        "essential_dimension_distribution": {
            str(key): distribution[key] for key in sorted(distribution)
        },
        "support_profile_distribution": {
            f"top_{top}_bottom_{bottom}_ess_{rank}": count
            for (top, bottom, rank), count in sorted(
                profile_distribution.items()
            )
        },
        "minimum_nonzero_essential_dimension": 8,
        "degree_six_chow_component_essential_cap": 6,
        "internal_intersection_zero": True,
    }


def signs() -> tuple[tuple[int, int, int, int], ...]:
    return tuple((1, a, b, c) for a, b, c in product((-1, 1), repeat=3))


def tensor_entry(sign: tuple[int, ...], indices: tuple[int, ...]) -> int:
    value = 1
    for index in indices:
        value *= sign[index]
    return value


def parity(indices: tuple[int, ...]) -> tuple[int, int, int]:
    return tuple(
        sum(index == value for index in indices) % 2 for value in (1, 2, 3)
    )


def normalized_projective_vectors(prime: int):
    for vector in product(range(prime), repeat=4):
        if not any(vector):
            continue
        first = next(value for value in vector if value)
        inverse = pow(first, -1, prime)
        normalized = tuple(value * inverse % prime for value in vector)
        if normalized == vector:
            yield vector


def parity_constant_power(vector: tuple[int, ...], prime: int) -> bool:
    values: dict[tuple[int, int, int], int] = {}
    for indices in product(range(4), repeat=4):
        entry = 1
        for index in indices:
            entry = entry * vector[index] % prime
        label = parity(indices)
        if label in values and values[label] != entry:
            return False
        values[label] = entry
    return True


def independent_glynn_audit() -> dict[str, object]:
    sign_list = signs()
    coordinates = tuple(product(range(4), repeat=4))
    matrix = [
        [tensor_entry(sign, indices) for sign in sign_list]
        for indices in coordinates
    ]
    check(rank_q(matrix) == 8, "sign tensor rank")

    coefficients = tuple(
        Fraction(sign[1] * sign[2] * sign[3], 8) for sign in sign_list
    )
    for indices, row in zip(coordinates, matrix, strict=True):
        value = sum(
            coefficient * entry
            for coefficient, entry in zip(coefficients, row, strict=True)
        )
        target = Fraction(int(len(set(indices)) == 4))
        check(value == target, (indices, value, target))

    finite_counts = {}
    for prime in (3, 5, 7, 11):
        solutions = [
            vector
            for vector in normalized_projective_vectors(prime)
            if parity_constant_power(vector, prime)
        ]
        expected = {
            (1, a % prime, b % prime, c % prime)
            for a, b, c in product((-1, 1), repeat=3)
        }
        check(set(solutions) == expected, (prime, solutions, expected))
        finite_counts[str(prime)] = len(solutions)

    return {
        "basis_size": 8,
        "ordered_tensor_coordinates": 256,
        "parity_classes": 8,
        "walsh_rank": 8,
        "normalized_low_essential_lines": [list(sign) for sign in sign_list],
        "low_essential_line_count": 8,
        "degree_six_chow_component_essential_cap": 6,
        "glynn_coefficients": [str(value) for value in coefficients],
        "all_glynn_coefficients_nonzero": True,
        "internal_minimum_terms": 8,
        "finite_field_projective_solution_counts": finite_counts,
    }


def core() -> dict[str, object]:
    glynn = independent_glynn_audit()
    glynn.pop("finite_field_projective_solution_counts")
    return {
        "schema": "general_quartic_natural_span_compression_barriers/v1",
        "field": "characteristic_zero",
        "laplace_22": independent_laplace_audit(),
        "glynn_span": glynn,
        "claim_boundary": {
            "mu_6_4_exact_value": "OPEN_IN_[5,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
            "laplace_internal_recombination": "IMPOSSIBLE",
            "glynn_internal_minimum": 8,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expect-sha256")
    args = parser.parse_args()
    theorem = core()
    digest = hashlib.sha256(
        json.dumps(theorem, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if args.expect_sha256 is not None:
        check(digest == args.expect_sha256, (digest, args.expect_sha256))
    diagnostics = independent_glynn_audit()[
        "finite_field_projective_solution_counts"
    ]
    print("GENERAL_QUARTIC_NATURAL_SPAN_BARRIERS_INDEPENDENT_PASS")
    print(digest)
    print(
        json.dumps(
            {"finite_field_solution_counts": diagnostics}, sort_keys=True
        )
    )


if __name__ == "__main__":
    main()
