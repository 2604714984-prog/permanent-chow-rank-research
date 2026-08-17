#!/usr/bin/env python3
"""Independent replay of the graded-K0 syzygy barrier.

This implementation imports none of the primary audit. It generates staircase
modules by lattice-path data, recovers monomial ideal generators directly from
the complement boundary, removes maximal cells one at a time, and uses a
disjoint large-n range for the permanent/Boolean ratio checks.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def lower_ideals(width: int, height: int) -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    for sequence in combinations_with_replacement(range(width + 1), height):
        partition = tuple(value for value in reversed(sequence) if value > 0)
        if partition:
            result.append(partition)
    require(len(result) == comb(width + height, height) - 1, len(result))
    require(len(set(result)) == len(result), "duplicate lower ideals")
    return result


def cells(partition: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        (s_degree, t_degree)
        for t_degree, width in enumerate(partition)
        for s_degree in range(width)
    }


def hilbert_from_cells(values: set[tuple[int, int]]) -> list[int]:
    if not values:
        return []
    counts = Counter(left + right for left, right in values)
    return [counts[degree] for degree in range(max(counts) + 1)]


def boundary_generators(partition: tuple[int, ...]) -> list[tuple[int, int]]:
    values = cells(partition)
    maximum_width = max(partition)
    maximum_height = len(partition)
    generators = []
    for left in range(maximum_width + 1):
        for right in range(maximum_height + 1):
            if (left, right) in values:
                continue
            if left > 0 and (left - 1, right) not in values:
                continue
            if right > 0 and (left, right - 1) not in values:
                continue
            generators.append((left, right))
    return sorted(generators, key=lambda value: (value[1], -value[0]))


def hilbert_numerator(hilbert: list[int]) -> list[int]:
    result = [0] * (len(hilbert) + 2)
    for degree, value in enumerate(hilbert):
        result[degree] += value
        result[degree + 1] -= 2 * value
        result[degree + 2] += value
    while result and result[-1] == 0:
        result.pop()
    return result


def resolution_numerator(partition: tuple[int, ...]) -> list[int]:
    generators = boundary_generators(partition)
    syzygies = [
        max(left[0], right[0]) + max(left[1], right[1])
        for left, right in zip(generators, generators[1:])
    ]
    maximum = max([sum(value) for value in generators] + syzygies)
    result = [0] * (maximum + 1)
    result[0] = 1
    for value in generators:
        result[sum(value)] -= 1
    for degree in syzygies:
        result[degree] += 1
    while result and result[-1] == 0:
        result.pop()
    return result


def filtration_checks(partition: tuple[int, ...]) -> int:
    values = cells(partition)
    checks = 0
    while values:
        maximal = [
            value
            for value in values
            if (value[0] + 1, value[1]) not in values
            and (value[0], value[1] + 1) not in values
        ]
        require(maximal, partition)
        removed = max(maximal, key=lambda value: (sum(value), value[1], value[0]))
        before = hilbert_from_cells(values)
        smaller = set(values)
        smaller.remove(removed)
        after = hilbert_from_cells(smaller)
        size = max(len(before), len(after), sum(removed) + 1)
        difference = [
            (before[index] if index < len(before) else 0)
            - (after[index] if index < len(after) else 0)
            for index in range(size)
        ]
        expected = [0] * size
        expected[sum(removed)] = 1
        require(difference == expected, (partition, removed, difference))
        values = smaller
        checks += 1
    return checks


def ratio_checks() -> tuple[int, int]:
    weighted = 0
    for n in range(61, 101):
        levels = [comb(n, degree) for degree in range(n + 1)]
        central = max(levels)
        weights = [
            [1] * (n + 1),
            [degree + 1 for degree in range(n + 1)],
            [(degree + 1) ** 2 + (n - degree + 1) for degree in range(n + 1)],
            [
                ((degree + 3) * 11_400_714_819_323_198_485 + 97 * n) % 17
                for degree in range(n + 1)
            ],
        ]
        for degree in range(n + 1):
            singleton = [0] * (n + 1)
            singleton[degree] = 1
            weights.append(singleton)
        for row in weights:
            denominator = sum(weight * level for weight, level in zip(row, levels))
            if denominator == 0:
                continue
            numerator = sum(weight * level * level for weight, level in zip(row, levels))
            require(Fraction(numerator, denominator) <= central, (n, row))
            weighted += 1
    exhaustive = 0
    for n in (11, 12):
        levels = [comb(n, degree) for degree in range(n + 1)]
        central = max(levels)
        for mask in range(1, 1 << (n + 1)):
            denominator = sum(levels[degree] for degree in range(n + 1) if (mask >> degree) & 1)
            numerator = sum(levels[degree] ** 2 for degree in range(n + 1) if (mask >> degree) & 1)
            require(Fraction(numerator, denominator) <= central, (n, mask))
            exhaustive += 1
    return weighted, exhaustive


def main() -> int:
    partitions = lower_ideals(5, 7)
    numerator_checks = 0
    filtration_cells = 0
    total_cells = 0
    for partition in partitions:
        hilbert = hilbert_from_cells(cells(partition))
        require(hilbert_numerator(hilbert) == resolution_numerator(partition), partition)
        numerator_checks += 1
        total_cells += sum(hilbert)
        filtration_cells += filtration_checks(partition)
    require(len(partitions) == 791, len(partitions))
    require(numerator_checks == 791, numerator_checks)
    require(total_cells == 13_860, total_cells)
    require(filtration_cells == 13_860, filtration_cells)
    weighted, exhaustive = ratio_checks()
    require(weighted == 3_420, weighted)
    require(exhaustive == 12_286, exhaustive)
    print("independent_staircase_modules=791")
    print("independent_hilbert_betti_checks=791")
    print("independent_cell_filtration_checks=13860")
    print("independent_composition_factor_cells=13860")
    print("independent_weighted_ratio_checks=3420")
    print("independent_boolean_supports=12286")
    print("GENERAL_GRADED_K0_SYZYGY_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
