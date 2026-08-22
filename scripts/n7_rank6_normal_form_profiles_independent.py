#!/usr/bin/env python3
"""Independent modular replay of the six rank-six normal-form profiles."""

from __future__ import annotations

import itertools
import math


PRIMES = (1_000_003, 1_000_033)
EXPECTED = {
    1: [1, 6, 16, 25, 25, 16, 6, 1],
    2: [1, 6, 16, 25, 25, 16, 6, 1],
    3: [1, 6, 18, 31, 31, 18, 6, 1],
    4: [1, 6, 19, 34, 34, 19, 6, 1],
    5: [1, 6, 20, 35, 35, 20, 6, 1],
    6: [1, 6, 21, 35, 35, 21, 6, 1],
}


def weak_compositions(total: int, slots: int):
    for bars in itertools.combinations(range(total + slots - 1), slots - 1):
        augmented = (-1, *bars, total + slots - 1)
        yield tuple(
            augmented[index + 1] - augmented[index] - 1
            for index in range(slots)
        )


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[entry % prime for entry in row] for row in rows]
    if not matrix:
        return 0
    height, width = len(matrix), len(matrix[0])
    pivot = 0
    for column in range(width):
        hit = next(
            (row for row in range(pivot, height) if matrix[row][column]),
            None,
        )
        if hit is None:
            continue
        matrix[pivot], matrix[hit] = matrix[hit], matrix[pivot]
        inverse = pow(matrix[pivot][column], prime - 2, prime)
        matrix[pivot] = [
            value * inverse % prime for value in matrix[pivot]
        ]
        for row in range(pivot + 1, height):
            if not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                (left - scale * right) % prime
                for left, right in zip(matrix[row], matrix[pivot])
            ]
        pivot += 1
        if pivot == height:
            break
    return pivot


def degree_rank(support_size: int, output_degree: int, prime: int) -> int:
    outputs = tuple(weak_compositions(output_degree, 6))
    operators = tuple(weak_compositions(7 - output_degree, 6))
    allowed = set()
    for doubled in range(support_size):
        exponent = [1] * 6
        exponent[doubled] = 2
        allowed.add(tuple(exponent))
    rows = []
    for operator in operators:
        row = []
        for output in outputs:
            source = tuple(a + b for a, b in zip(operator, output))
            if source not in allowed:
                row.append(0)
                continue
            value = 1
            for source_power, output_power in zip(source, output):
                value *= (
                    math.factorial(source_power)
                    // math.factorial(output_power)
                )
            row.append(value)
        rows.append(row)
    return rank_mod(rows, prime)


def main() -> None:
    for prime in PRIMES:
        for support_size in range(1, 7):
            profile = [
                degree_rank(support_size, degree, prime)
                for degree in range(8)
            ]
            assert profile == EXPECTED[support_size], (
                prime,
                support_size,
                profile,
            )
    print(
        "PASS independent rank-six normal-form replay "
        f"(primes={','.join(map(str, PRIMES))})"
    )


if __name__ == "__main__":
    main()
