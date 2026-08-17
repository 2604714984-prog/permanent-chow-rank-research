#!/usr/bin/env python3
"""Independent matrix replay for the split Boolean two-plane."""

from __future__ import annotations

from itertools import combinations
from math import comb


PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subset_masks(n: int, degree: int) -> list[int]:
    return [
        sum(1 << value for value in subset)
        for subset in combinations(range(n), degree)
    ]


def modular_rank(columns: list[list[int]], prime: int) -> int:
    if not columns:
        return 0
    basis: dict[int, list[int]] = {}
    for original in columns:
        vector = [value % prime for value in original]
        while True:
            pivot = next((index for index, value in enumerate(vector) if value), None)
            if pivot is None:
                break
            if pivot not in basis:
                inverse = pow(vector[pivot], prime - 2, prime)
                basis[pivot] = [(value * inverse) % prime for value in vector]
                break
            factor = vector[pivot]
            vector = [
                (left - factor * right) % prime
                for left, right in zip(vector, basis[pivot])
            ]
    return len(basis)


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


def expected_split_rank(n: int, degree: int) -> int:
    first = n // 2
    second = n - first
    quotient = convolution(primitive_hilbert(first), primitive_hilbert(second))
    quotient_dimension = quotient[degree] if degree < len(quotient) else 0
    return comb(n, degree) - quotient_dimension


def split_columns(n: int, degree: int) -> list[list[int]]:
    sources = subset_masks(n, degree - 1)
    targets = subset_masks(n, degree)
    target_index = {value: index for index, value in enumerate(targets)}
    first_mask = (1 << (n // 2)) - 1
    all_mask = (1 << n) - 1
    second_mask = all_mask ^ first_mask

    columns: list[list[int]] = []
    for source in sources:
        missing_first = first_mask & ~source
        missing_second = second_mask & ~source
        for allowed in (missing_first, missing_second):
            column = [0] * len(targets)
            cursor = allowed
            while cursor:
                least = cursor & -cursor
                column[target_index[source | least]] = 1
                cursor ^= least
            columns.append(column)
    return columns


def main() -> int:
    cells = 0
    for n in range(2, 9):
        for degree in range(1, n + 1):
            rank = modular_rank(split_columns(n, degree), PRIME)
            expected = expected_split_rank(n, degree)
            require(rank == expected, (n, degree, rank, expected))
            cells += 1

    require(cells == 35, cells)
    print("independent_split_boolean_cells=35")
    print("independent_prime=1000033")
    print("independent_split_quotient_formula=PASS")
    print("GENERAL_TWO_DIRECTION_MAXIMAL_IDEAL_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
