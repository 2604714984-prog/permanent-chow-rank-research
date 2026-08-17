#!/usr/bin/env python3
"""Independent replay for the bounded homogeneous matrix ceiling."""

from __future__ import annotations

from itertools import combinations
from math import comb


PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def subsets(n: int, degree: int) -> list[frozenset[int]]:
    if not 0 <= degree <= n:
        return []
    return [frozenset(value) for value in combinations(range(n), degree)]


def transpose_inclusion_columns(
    n: int,
    source_degree: int,
    target_degree: int,
) -> list[list[int]]:
    source = subsets(n, source_degree)
    target = subsets(n, target_degree)
    return [
        [1 if lower <= upper else 0 for upper in target]
        for lower in source
    ]


def column_rank(columns: list[list[int]], prime: int = PRIME) -> int:
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


def main() -> int:
    lefschetz_cells = 0
    for n in range(2, 8):
        for degree_of_entries in range(1, n + 1):
            for output_degree in range(degree_of_entries, n + 1):
                source_degree = output_degree - degree_of_entries
                columns = transpose_inclusion_columns(n, source_degree, output_degree)
                rank = column_rank(columns)
                expected = min(comb(n, source_degree), comb(n, output_degree))
                require(rank == expected, (n, degree_of_entries, output_degree, rank, expected))
                lefschetz_cells += 1
    require(lefschetz_cells == 83, lefschetz_cells)

    arithmetic_cells = 0
    for n in range(3, 9):
        central = comb(n, n // 2)
        for degree_of_entries in range(1, min(3, n) + 1):
            for output_degree in range(degree_of_entries, n + 1):
                source = comb(n, output_degree - degree_of_entries)
                target = comb(n, output_degree)
                for row_count in range(1, 4):
                    for column_count in range(1, 4):
                        for normal_rank in range(1, min(row_count, column_count) + 1):
                            numerator = min(
                                column_count * source * source,
                                row_count * target * target,
                            )
                            denominator = normal_rank * min(source, target)
                            exact = ceil_div(numerator, denominator)
                            coarse = ceil_div(
                                max(row_count, column_count) * central,
                                normal_rank,
                            )
                            require(exact <= coarse, (n, degree_of_entries, output_degree))
                            arithmetic_cells += 1
    require(arithmetic_cells == 1_134, arithmetic_cells)

    print("independent_lefschetz_power_cells=83")
    print("independent_arithmetic_ceiling_cells=1134")
    print("independent_prime=1000033")
    print("independent_matrix_size_barrier=sub_sqrt_n")
    print("GENERAL_TWO_DIRECTION_BOUNDED_MATRIX_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
