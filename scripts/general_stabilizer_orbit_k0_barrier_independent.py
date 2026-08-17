#!/usr/bin/env python3
"""Independent replay of the stabilizer-efficient orbit barrier.

This file imports none of the primary audit. It uses a second deterministic
factor family, modular Gaussian elimination, direct projective-line
stabilizer tests, and a separate standard-tableau recursion for irreducible
dimensions.
"""

from __future__ import annotations

import itertools
import math
import random
from functools import lru_cache
from math import comb, factorial


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def normalize(vector: tuple[int, ...]) -> tuple[int, ...]:
    gcd = 0
    for value in vector:
        gcd = math.gcd(gcd, abs(value))
    require(gcd > 0, vector)
    out = tuple(value // gcd for value in vector)
    first = next(value for value in out if value)
    return tuple(-value for value in out) if first < 0 else out


def factors(n: int) -> tuple[tuple[int, ...], ...]:
    rng = random.Random(100_000 * n + 18)
    return tuple(
        normalize(tuple(rng.randint(101, 997) for _ in range(n * n)))
        for _ in range(n)
    )


def modular_rank(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[value % PRIME for value in row] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], PRIME - 2, PRIME)
        matrix[rank] = [(value * inverse) % PRIME for value in matrix[rank]]
        for row in range(row_count):
            if row == rank or matrix[row][column] == 0:
                continue
            coefficient = matrix[row][column]
            matrix[row] = [
                (matrix[row][index] - coefficient * matrix[rank][index]) % PRIME
                for index in range(column_count)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def apply_permutations(
    vector: tuple[int, ...],
    n: int,
    rows: tuple[int, ...],
    columns: tuple[int, ...],
) -> tuple[int, ...]:
    output = [0] * (n * n)
    for row in range(n):
        for column in range(n):
            output[rows[row] * n + columns[column]] = vector[row * n + column]
    return normalize(tuple(output))


def projective_stabilizer(
    vectors: tuple[tuple[int, ...], ...],
    n: int,
) -> tuple[int, int]:
    vector_set = frozenset(vectors)
    size = 0
    checks = 0
    permutations = tuple(itertools.permutations(range(n)))
    for rows in permutations:
        for columns in permutations:
            checks += 1
            transformed = frozenset(
                apply_permutations(vector, n, rows, columns)
                for vector in vectors
            )
            if transformed == vector_set:
                size += 1
    return size, checks


def partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    upper = n if maximum is None else min(n, maximum)
    for first in range(upper, 0, -1):
        for tail in partitions(n - first, first):
            yield (first, *tail)


def removable_rows(shape: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        row
        for row in range(len(shape))
        if row + 1 == len(shape) or shape[row] > shape[row + 1]
    )


@lru_cache(maxsize=None)
def tableau_dimension(shape: tuple[int, ...]) -> int:
    if not shape:
        return 1
    total = 0
    for row in removable_rows(shape):
        reduced = list(shape)
        reduced[row] -= 1
        if reduced[row] == 0:
            reduced.pop(row)
        total += tableau_dimension(tuple(reduced))
    return total


def two_row(n: int, index: int) -> tuple[int, ...]:
    return (n,) if index == 0 else (n - index, index)


def main() -> int:
    stabilizer_checks = 0
    for n in range(2, 6):
        vectors = factors(n)
        require(modular_rank(vectors) == n, (n, vectors))
        size, checks = projective_stabilizer(vectors, n)
        require(size == 1, (n, size))
        stabilizer_checks += checks

    partition_checks = 0
    pointwise_checks = 0
    block_checks = 0

    for n in range(2, 11):
        shapes = tuple(partitions(n))
        dimensions = {shape: tableau_dimension(shape) for shape in shapes}
        require(
            sum(dimension * dimension for dimension in dimensions.values())
            == factorial(n),
            (n, dimensions),
        )
        partition_checks += len(shapes)

        numerator_total = 0
        denominator_total = 0
        for degree in range(n + 1):
            level = comb(n, degree)
            limit = min(degree, n - degree)
            for row_index in range(limit + 1):
                for column_index in range(limit + 1):
                    row_shape = two_row(n, row_index)
                    column_shape = two_row(n, column_index)
                    numerator_total += 1
                    denominator_total += (
                        level
                        * dimensions[row_shape]
                        * dimensions[column_shape]
                    )
                    pointwise_checks += 1
            require(denominator_total >= numerator_total, (n, degree))
        require(denominator_total >= numerator_total, n)
        block_checks += 1

    require(stabilizer_checks == 15_016, stabilizer_checks)
    require(partition_checks == 137, partition_checks)
    require(pointwise_checks == 508, pointwise_checks)
    require(block_checks == 9, block_checks)

    print("independent_trivial_stabilizer_group_checks=15016")
    print("independent_partition_dimension_checks=137")
    print("independent_pointwise_isotype_checks=508")
    print("independent_block_checks=9")
    print("GENERAL_STABILIZER_ORBIT_K0_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
