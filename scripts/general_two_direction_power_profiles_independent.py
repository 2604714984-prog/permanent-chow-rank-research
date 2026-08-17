#!/usr/bin/env python3
"""Independent direct-coefficient replay for two-direction profiles.

This file imports none of the primary generator.  It computes coefficients of
L_0^(p-k)L_1^k directly from the final added subsets, rather than composing
one-step multiplication maps.
"""

from __future__ import annotations

from itertools import combinations, permutations
from math import ceil, factorial


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subsets(n: int, degree: int) -> tuple[tuple[int, ...], ...]:
    return tuple(combinations(range(n), degree))


def reduce_columns(columns: list[dict[int, int]]) -> int:
    basis: dict[int, dict[int, int]] = {}
    for source in columns:
        vector = {row: value % PRIME for row, value in source.items() if value % PRIME}
        while vector:
            pivot = min(vector)
            old = basis.get(pivot)
            if old is None:
                inverse = pow(vector[pivot], PRIME - 2, PRIME)
                basis[pivot] = {
                    row: value * inverse % PRIME for row, value in vector.items()
                }
                break
            factor = vector[pivot]
            for row, value in old.items():
                updated = (vector.get(row, 0) - factor * value) % PRIME
                if updated:
                    vector[row] = updated
                elif row in vector:
                    del vector[row]
    return len(basis)


def boolean_coefficient(
    added: tuple[int, ...],
    left: tuple[int, ...],
    right: tuple[int, ...],
    right_count: int,
) -> int:
    power = len(added)
    total = 0
    for right_positions in combinations(range(power), right_count):
        right_set = set(right_positions)
        value = 1
        for position, variable in enumerate(added):
            value *= right[variable] if position in right_set else left[variable]
        total += value
    return total * factorial(power - right_count) * factorial(right_count)


def boolean_rank(n: int, power: int, degree: int) -> int:
    source = subsets(n, degree - power)
    target = subsets(n, degree)
    target_index = {value: index for index, value in enumerate(target)}
    left = tuple(1 for _ in range(n))
    right = tuple(index + 1 for index in range(n))
    columns: list[dict[int, int]] = []

    for right_count in range(power + 1):
        for initial in source:
            initial_set = set(initial)
            column: dict[int, int] = {}
            for final in target:
                if not initial_set.issubset(final):
                    continue
                added = tuple(value for value in final if value not in initial_set)
                coefficient = boolean_coefficient(added, left, right, right_count) % PRIME
                if coefficient:
                    column[target_index[final]] = coefficient
            columns.append(column)
    return reduce_columns(columns)


def matrices(n: int):
    left = tuple(
        tuple((i + 1) * (j + 2) + (i - j) ** 2 + 1 for j in range(n))
        for i in range(n)
    )
    right = tuple(
        tuple((i + 2) ** 2 + (j + 1) ** 3 + 3 * i * j + 5 for j in range(n))
        for i in range(n)
    )
    return left, right


def permanent_coefficient(
    added_rows: tuple[int, ...],
    added_columns: tuple[int, ...],
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    right_count: int,
) -> int:
    power = len(added_rows)
    total = 0
    for permuted_columns in permutations(added_columns):
        edges = tuple(zip(added_rows, permuted_columns))
        for right_positions in combinations(range(power), right_count):
            right_set = set(right_positions)
            value = 1
            for position, (row, column) in enumerate(edges):
                value *= right[row][column] if position in right_set else left[row][column]
            total += value
    return total * factorial(power - right_count) * factorial(right_count)


def permanent_rank(n: int, power: int, degree: int) -> int:
    source_layer = subsets(n, degree - power)
    target_layer = subsets(n, degree)
    source = tuple((rows, columns) for rows in source_layer for columns in source_layer)
    target = tuple((rows, columns) for rows in target_layer for columns in target_layer)
    target_index = {value: index for index, value in enumerate(target)}
    left, right = matrices(n)
    columns: list[dict[int, int]] = []

    for right_count in range(power + 1):
        for initial_rows, initial_columns in source:
            row_set = set(initial_rows)
            column_set = set(initial_columns)
            column_vector: dict[int, int] = {}
            for final_rows, final_columns in target:
                if not row_set.issubset(final_rows) or not column_set.issubset(final_columns):
                    continue
                added_rows = tuple(value for value in final_rows if value not in row_set)
                added_columns = tuple(value for value in final_columns if value not in column_set)
                coefficient = permanent_coefficient(
                    added_rows,
                    added_columns,
                    left,
                    right,
                    right_count,
                ) % PRIME
                if coefficient:
                    column_vector[target_index[(final_rows, final_columns)]] = coefficient
            columns.append(column_vector)
    return reduce_columns(columns)


def main() -> int:
    decisive = {
        3: (1, 2, 3, 9, 3),
        4: (1, 2, 6, 31, 6),
        5: (1, 3, 10, 100, 10),
        6: (1, 3, 20, 400, 20),
    }
    observed_bounds = []
    for n, (power, degree, expected_boolean, expected_permanent, expected_bound) in decisive.items():
        boolean_value = boolean_rank(n, power, degree)
        permanent_value = permanent_rank(n, power, degree)
        require(boolean_value == expected_boolean, (n, boolean_value))
        require(permanent_value == expected_permanent, (n, permanent_value))
        require(ceil(permanent_value / boolean_value) == expected_bound, n)
        observed_bounds.append(expected_bound)

    higher = [
        (5, 2, 3, 10, 73),
        (6, 2, 3, 16, 106),
        (6, 3, 4, 15, 141),
    ]
    for n, power, degree, expected_boolean, expected_permanent in higher:
        require(boolean_rank(n, power, degree) == expected_boolean, (n, power, degree, "B"))
        require(permanent_rank(n, power, degree) == expected_permanent, (n, power, degree, "P"))

    print("independent_boolean_decisive=3,6,10,20")
    print("independent_permanent_decisive=9,31,100,400")
    print("independent_certified_bounds=" + ",".join(map(str, observed_bounds)))
    print("independent_higher_power_checks=3")
    print("GENERAL_TWO_DIRECTION_POWER_PROFILES_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
