#!/usr/bin/env python3
"""Independent replay of the equivariant-K0 orbit barrier.

This implementation imports none of the primary audit. It uses the Frobenius
determinantal dimension formula rather than hook products, a disjoint n-range,
and independently generated deterministic isotype weights.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
from typing import Iterable


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def integer_partitions(n: int, maximum: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    upper = n if maximum is None else min(n, maximum)
    for first in range(upper, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def frobenius_dimension(partition: tuple[int, ...]) -> int:
    length = len(partition)
    numerator = factorial(sum(partition))
    vandermonde = 1
    for left in range(length):
        for right in range(left + 1, length):
            vandermonde *= partition[left] - partition[right] + right - left
    denominator = 1
    for index, value in enumerate(partition):
        denominator *= factorial(value + length - index - 1)
    return numerator * vandermonde // denominator


def main() -> int:
    regular_cells = 0
    regular_checks = 0
    for n in range(11, 14):
        partitions = list(integer_partitions(n))
        dimensions = [frobenius_dimension(value) for value in partitions]
        require(sum(value * value for value in dimensions) == factorial(n), n)
        regular_cells += len(partitions)
        regular_checks += 1

    two_row_checks = 0
    isotype_cells = 0
    weighted_checks = 0
    selected_supports = 0
    block_checks = 0
    ungraded_checks = 0

    for n in range(41, 61):
        block_numerator = 0
        block_denominator = 0
        for degree in range(n + 1):
            dimensions = [
                comb(n, index) - (comb(n, index - 1) if index else 0)
                for index in range(min(degree, n - degree) + 1)
            ]
            level = comb(n, degree)
            require(sum(dimensions) == level, (n, degree))
            for index, value in enumerate(dimensions):
                partition = (n,) if index == 0 else (n - index, index)
                require(value == frobenius_dimension(partition), partition)
                two_row_checks += 1
            isotypes = [left * right for left in dimensions for right in dimensions]
            require(sum(isotypes) == level * level, (n, degree))
            isotype_cells += len(isotypes)

            weights = [
                [1] * len(isotypes),
                [
                    (
                        (index + 5) * 11_400_714_819_323_198_485
                        + 13 * n
                        + 19 * degree
                    )
                    % 17
                    for index in range(len(isotypes))
                ],
            ]
            step = max(1, len(isotypes) // 7)
            for index in range(0, len(isotypes), step):
                singleton = [0] * len(isotypes)
                singleton[index] = 1
                weights.append(singleton)
            for row in weights:
                orbit_weight = sum(weight * dimension for weight, dimension in zip(row, isotypes))
                if orbit_weight == 0:
                    continue
                require(Fraction(sum(row), level * orbit_weight) <= 1, (n, degree, row))
                weighted_checks += 1

            for salt in range(20):
                support = [
                    index
                    for index in range(len(isotypes))
                    if ((index + 1) * 2_654_435_761 + 97 * salt + n + degree) % 7 < 3
                ]
                if not support:
                    continue
                orbit_weight = sum(isotypes[index] for index in support)
                require(Fraction(len(support), level * orbit_weight) <= 1, (n, degree, salt))
                selected_supports += 1

            block_numerator += len(isotypes)
            block_denominator += level * sum(isotypes)

        require(Fraction(block_numerator, block_denominator) <= 1, n)
        block_checks += 1

        dimensions = [
            comb(n, index) - (comb(n, index - 1) if index else 0)
            for index in range(n // 2 + 1)
        ]
        for left_index, left in enumerate(dimensions):
            for right_index, right in enumerate(dimensions):
                multiplicity = n - 2 * max(left_index, right_index) + 1
                require(multiplicity <= (2**n) * left * right, n)
                ungraded_checks += 1

    require(regular_cells == 234, regular_cells)
    require(regular_checks == 3, regular_checks)
    require(two_row_checks == 13_945, two_row_checks)
    require(isotype_cells == 249_945, isotype_cells)
    require(weighted_checks == 9_805, weighted_checks)
    require(selected_supports == 20_143, selected_supports)
    require(block_checks == 20, block_checks)
    require(ungraded_checks == 13_690, ungraded_checks)

    print("independent_regular_partition_cells=234")
    print("independent_regular_dimension_checks=3")
    print("independent_two_row_checks=13945")
    print("independent_isotype_cells=249945")
    print("independent_weighted_checks=9805")
    print("independent_selected_supports=20143")
    print("independent_block_checks=20")
    print("independent_ungraded_checks=13690")
    print("GENERAL_EQUIVARIANT_K0_ORBIT_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
