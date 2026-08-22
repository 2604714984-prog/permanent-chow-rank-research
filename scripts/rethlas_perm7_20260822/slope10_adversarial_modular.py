#!/usr/bin/env python3
"""Bounded adversarial diagnostics for the universal slope-ten lemma.

This script is deliberately not a characteristic-zero certificate.  It tests
the claimed inequality on exact finite-field matrices for arbitrary quotient
orientations and arbitrary relation subspaces of dimension at most three.
"""

from __future__ import annotations

import itertools
import random


PRIME = 1_000_033
SEED = 20_260_822
TRIALS = 12


def weak_compositions(total: int, slots: int):
    for bars in itertools.combinations(range(total + slots - 1), slots - 1):
        augmented = (-1, *bars, total + slots - 1)
        yield tuple(
            augmented[index + 1] - augmented[index] - 1
            for index in range(slots)
        )


def rref(rows: list[list[int]]) -> list[list[int]]:
    matrix = [[entry % PRIME for entry in row] for row in rows]
    if not matrix:
        return []
    height = len(matrix)
    width = len(matrix[0])
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, height) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], PRIME - 2, PRIME)
        matrix[pivot_row] = [
            value * inverse % PRIME for value in matrix[pivot_row]
        ]
        for row in range(height):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == height:
            break
    return matrix[:pivot_row]


def rank(rows: list[list[int]]) -> int:
    return len(rref(rows))


def multiply_linear_forms(forms: list[list[int]]) -> dict[tuple[int, ...], int]:
    variables = len(forms[0])
    polynomial = {(0,) * variables: 1}
    for form in forms:
        following: dict[tuple[int, ...], int] = {}
        for exponent, coefficient in polynomial.items():
            for variable, scalar in enumerate(form):
                if scalar == 0:
                    continue
                target = list(exponent)
                target[variable] += 1
                key = tuple(target)
                following[key] = (
                    following.get(key, 0) + coefficient * scalar
                ) % PRIME
        polynomial = following
    return {key: value for key, value in polynomial.items() if value}


def derivative_space(
    polynomial: dict[tuple[int, ...], int],
    variables: int,
    output_degree: int,
) -> tuple[list[list[int]], tuple[tuple[int, ...], ...]]:
    outputs = tuple(weak_compositions(output_degree, variables))
    output_index = {monomial: index for index, monomial in enumerate(outputs)}
    operators = tuple(weak_compositions(7 - output_degree, variables))
    rows = []
    for operator in operators:
        row = [0] * len(outputs)
        for source, coefficient in polynomial.items():
            if any(left < right for left, right in zip(source, operator)):
                continue
            target = tuple(left - right for left, right in zip(source, operator))
            multiplier = 1
            for source_power, target_power in zip(source, target):
                for value in range(target_power + 1, source_power + 1):
                    multiplier = multiplier * value % PRIME
            row[output_index[target]] = (
                row[output_index[target]] + coefficient * multiplier
            ) % PRIME
        rows.append(row)
    return rref(rows), outputs


def derivatives(
    vector: list[int],
    monomials: tuple[tuple[int, ...], ...],
    lower_monomials: tuple[tuple[int, ...], ...],
) -> list[list[int]]:
    lower_index = {monomial: index for index, monomial in enumerate(lower_monomials)}
    variables = len(monomials[0])
    answer = [[0] * len(lower_monomials) for _ in range(variables)]
    for coefficient, exponent in zip(vector, monomials):
        if coefficient == 0:
            continue
        for variable, power in enumerate(exponent):
            if power == 0:
                continue
            target = list(exponent)
            target[variable] -= 1
            index = lower_index[tuple(target)]
            answer[variable][index] = (
                answer[variable][index] + coefficient * power
            ) % PRIME
    return answer


def random_full_rank(rows: int, columns: int, rng: random.Random) -> list[list[int]]:
    if rows == 0:
        return []
    while True:
        matrix = [
            [rng.randrange(PRIME) for _ in range(columns)]
            for _ in range(rows)
        ]
        if rank(matrix) == rows:
            return matrix


def random_relation_space(
    basis: list[list[int]], dimension: int, rng: random.Random
) -> list[list[int]]:
    coefficients = random_full_rank(dimension, len(basis), rng)
    return [
        [
            sum(row[index] * basis[index][column] for index in range(len(basis)))
            % PRIME
            for column in range(len(basis[0]))
        ]
        for row in coefficients
    ]


def symbol_rank(
    source_basis: list[list[int]],
    source_monomials: tuple[tuple[int, ...], ...],
    target_monomials: tuple[tuple[int, ...], ...],
    quotient: list[list[int]],
    relations: list[list[int]] | None = None,
) -> int:
    quotient_rank = len(quotient)
    images = []
    for source in source_basis:
        partials = derivatives(source, source_monomials, target_monomials)
        image = []
        for quotient_row in quotient:
            for target_index in range(len(target_monomials)):
                image.append(
                    sum(
                        quotient_row[variable] * partials[variable][target_index]
                        for variable in range(len(partials))
                    )
                    % PRIME
                )
        images.append(image)
    if relations is None or not relations or quotient_rank == 0:
        return rank(images)
    relation_rows = []
    block_width = len(target_monomials)
    for block in range(quotient_rank):
        for relation in relations:
            row = [0] * (quotient_rank * block_width)
            row[block * block_width : (block + 1) * block_width] = relation
            relation_rows.append(row)
    return rank(relation_rows + images) - rank(relation_rows)


def spaces(polynomial: dict[tuple[int, ...], int], variables: int):
    degree_two, monomials_two = derivative_space(polynomial, variables, 2)
    degree_three, monomials_three = derivative_space(polynomial, variables, 3)
    degree_four, monomials_four = derivative_space(polynomial, variables, 4)
    return (
        degree_two,
        degree_three,
        degree_four,
        monomials_two,
        monomials_three,
        monomials_four,
    )


def test_polynomial(
    label: str,
    polynomial: dict[tuple[int, ...], int],
    variables: int,
    rng: random.Random,
) -> int:
    (
        degree_two,
        degree_three,
        degree_four,
        monomials_two,
        monomials_three,
        monomials_four,
    ) = spaces(polynomial, variables)
    assert len(degree_three) == len(degree_four)
    middle_rank = len(degree_three)
    defect = 35 - middle_rank
    checks = 0
    for quotient_rank in range(variables + 1):
        for relation_dimension in range(4):
            if relation_dimension > len(degree_two):
                continue
            for _ in range(TRIALS):
                quotient = random_full_rank(quotient_rank, variables, rng)
                relations = random_relation_space(
                    degree_two, relation_dimension, rng
                )
                plus = symbol_rank(
                    degree_four,
                    monomials_four,
                    monomials_three,
                    quotient,
                )
                minus = symbol_rank(
                    degree_three,
                    monomials_three,
                    monomials_two,
                    quotient,
                    relations,
                )
                assert plus + minus + defect >= 10 * quotient_rank, (
                    label,
                    middle_rank,
                    quotient_rank,
                    relation_dimension,
                    plus,
                    minus,
                    defect,
                )
                checks += 1
    return checks


def rank_six_form(support_size: int) -> list[list[int]]:
    identity = [
        [int(row == column) for column in range(6)] for row in range(6)
    ]
    last = [int(index < support_size) for index in range(6)]
    return identity + [last]


def random_rank_five_form(rng: random.Random) -> list[list[int]]:
    identity = [
        [int(row == column) for column in range(5)] for row in range(5)
    ]
    extras = []
    for _ in range(2):
        while True:
            row = [rng.randrange(PRIME) for _ in range(5)]
            if any(row):
                extras.append(row)
                break
    return identity + extras


def main() -> None:
    rng = random.Random(SEED)
    total = 0
    for support_size in range(1, 7):
        forms = rank_six_form(support_size)
        polynomial = multiply_linear_forms(forms)
        total += test_polynomial(
            f"rank6_support_{support_size}", polynomial, 6, rng
        )
    squarefree = multiply_linear_forms(
        [[int(row == column) for column in range(7)] for row in range(7)]
    )
    total += test_polynomial("rank7_squarefree", squarefree, 7, rng)
    for sample in range(6):
        forms = random_rank_five_form(rng)
        polynomial = multiply_linear_forms(forms)
        total += test_polynomial(f"rank5_random_{sample}", polynomial, 5, rng)
    print(
        "PASS slope-ten adversarial modular diagnostic "
        f"(prime={PRIME}, seed={SEED}, checks={total})"
    )


if __name__ == "__main__":
    main()
