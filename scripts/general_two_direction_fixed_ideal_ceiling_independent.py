#!/usr/bin/env python3
"""Independent matrix replay for B_m/L^N B_m."""

from __future__ import annotations

from itertools import combinations
from math import comb


PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subsets(n: int, size: int) -> list[frozenset[int]]:
    if not 0 <= size <= n:
        return []
    return [frozenset(value) for value in combinations(range(n), size)]


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


def inclusion_columns(n: int, source_degree: int, target_degree: int) -> list[list[int]]:
    source = subsets(n, source_degree)
    target = subsets(n, target_degree)
    return [
        [1 if lower <= upper else 0 for upper in target]
        for lower in source
    ]


def main() -> int:
    cells = 0
    for size in range(2, 9):
        for power in range(1, min(4, size) + 1):
            for degree in range(size + 1):
                target_dimension = comb(size, degree)
                source_degree = degree - power
                source_dimension = comb(size, source_degree) if source_degree >= 0 else 0
                columns = inclusion_columns(size, source_degree, degree)
                rank = modular_rank(columns, PRIME)
                expected_rank = min(source_dimension, target_dimension)
                expected_quotient = max(0, target_dimension - source_dimension)
                require(rank == expected_rank, (size, power, degree, rank, expected_rank))
                require(target_dimension - rank == expected_quotient, (size, power, degree))
                cells += 1

    require(cells == 158, cells)
    print("independent_boolean_power_quotient_cells=158")
    print("independent_prime=1000033")
    print("independent_power_quotient_formula=PASS")
    print("GENERAL_TWO_DIRECTION_FIXED_IDEAL_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
