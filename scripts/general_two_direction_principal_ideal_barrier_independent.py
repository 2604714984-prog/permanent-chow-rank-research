#!/usr/bin/env python3
"""Independent subset-incidence replay for the principal-ideal barrier.

This file imports none of the primary audit.  It constructs the transpose
orientation of every relevant inclusion matrix and computes ranks over a
second prime.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subsets(n: int, size: int) -> list[frozenset[int]]:
    return [frozenset(value) for value in combinations(range(n), size)]


def column_rank_mod_prime(columns: list[list[int]], prime: int) -> int:
    if not columns:
        return 0
    row_count = len(columns[0])
    basis: dict[int, list[int]] = {}

    for column in columns:
        vector = [value % prime for value in column]
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
        require(len(vector) == row_count, row_count)
    return len(basis)


def main() -> int:
    cells = 0
    for n in range(2, 8):
        central = comb(n, n // 2)
        for power in range(1, n + 1):
            for target_degree in range(power, n + 1):
                source_degree = target_degree - power
                source = subsets(n, source_degree)
                target = subsets(n, target_degree)

                # Columns are source subsets; rows are target subsets.
                columns = [
                    [1 if lower <= upper else 0 for upper in target]
                    for lower in source
                ]
                rank = column_rank_mod_prime(columns, PRIME)
                expected = min(len(source), len(target))
                require(rank == expected, (n, power, target_degree, rank, expected))
                require(expected <= central, (n, power, target_degree))
                cells += 1

    require(cells == 83, cells)
    print("independent_principal_profile_cells=83")
    print("independent_prime=1000033")
    print("independent_route_ceiling=central_binomial")
    print("GENERAL_TWO_DIRECTION_PRINCIPAL_IDEAL_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
