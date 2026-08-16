#!/usr/bin/env python3
"""Independent replay for the same-span Chow overlap theorem.

This implementation imports none of the primary audit.  It computes the sum
of the two dual diagonal-square spaces directly in the symmetric-matrix basis,
uses support-graph components for the sharp constructions, and rebuilds the
colex degree-two shadow profiles from explicit subsets.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import ceil, comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_fraction(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[Fraction(value) for value in row] for row in matrix]
    width = len(rows[0])
    rank = 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][column]
        rows[rank] = [entry / value for entry in rows[rank]]
        for index in range(rank + 1, len(rows)):
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    left - coefficient * right
                    for left, right in zip(rows[index], rows[rank], strict=True)
                ]
        rank += 1
    return rank


def identity(size: int) -> list[list[int]]:
    return [
        [int(i == j) for j in range(size)]
        for i in range(size)
    ]


def block_diagonal(blocks: list[list[list[int]]]) -> list[list[int]]:
    size = sum(len(block) for block in blocks)
    matrix = [[0] * size for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                matrix[offset + i][offset + j] = value
        offset += len(block)
    return matrix


H2 = [[1, 1], [1, -1]]
B3 = [[1, 1, 1], [1, -1, 0], [1, 1, -2]]


def sharp_matrix(n: int, shared: int) -> list[list[int]]:
    remainder = n - shared
    if remainder == 0:
        return identity(n)
    if remainder == 1:
        matrix = identity(n)
        matrix[0][-1] = 1
        return matrix
    blocks = [[[1]] for _ in range(shared)]
    if remainder % 2 == 0:
        blocks.extend(H2 for _ in range(remainder // 2))
    else:
        blocks.extend(H2 for _ in range((remainder - 3) // 2))
        blocks.append(B3)
    return block_diagonal(blocks)


def symmetric_vector(matrix: list[list[int]]) -> list[int]:
    size = len(matrix)
    return [
        matrix[i][j]
        for i in range(size)
        for j in range(i, size)
    ]


def direct_common_quadratic_dimension(transition: list[list[int]]) -> int:
    n = len(transition)
    generators: list[list[int]] = []
    for i in range(n):
        matrix = [[0] * n for _ in range(n)]
        matrix[i][i] = 1
        generators.append(symmetric_vector(matrix))
    for column in range(n):
        vector = [transition[row][column] for row in range(n)]
        matrix = [
            [vector[i] * vector[j] for j in range(n)]
            for i in range(n)
        ]
        generators.append(symmetric_vector(matrix))
    sum_dimension = rank_fraction(generators)
    return comb(n + 1, 2) - sum_dimension


def support_component_count(matrix: list[list[int]]) -> int:
    n = len(matrix)
    graph = {("r", i): set() for i in range(n)}
    graph.update({("c", j): set() for j in range(n)})
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                graph[("r", i)].add(("c", j))
                graph[("c", j)].add(("r", i))
    seen: set[tuple[str, int]] = set()
    count = 0
    for vertex in graph:
        if vertex in seen:
            continue
        count += 1
        stack = [vertex]
        seen.add(vertex)
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    return count


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def degree_two_profile(n: int, m: int) -> list[int]:
    layer = sorted(combinations(range(n), m), key=colex_rank)
    shadow: set[tuple[int, int]] = set()
    profile = [0]
    for subset in layer:
        shadow.update(combinations(subset, 2))
        profile.append(len(shadow))
    return profile


def main() -> int:
    checked = 0
    for n in range(2, 11):
        for shared in range(n + 1):
            matrix = sharp_matrix(n, shared)
            observed = direct_common_quadratic_dimension(matrix)
            expected = comb(n, 2) - ceil((n - shared) / 2)
            require(observed == expected, (n, shared, observed, expected))
            if n - shared not in (1,):
                components = support_component_count(matrix)
                expected_components = shared + (n - shared) // 2
                require(components == expected_components, (
                    n,
                    shared,
                    components,
                    expected_components,
                ))
            checked += 1

    central_expected = {
        6: 11,
        7: 21,
        8: 36,
        9: 71,
        10: 127,
    }
    for n, expected in central_expected.items():
        m = n // 2
        cap = comb(n, 2) - ceil(n / 2)
        profile = degree_two_profile(n, m)
        maximum = max(index for index, value in enumerate(profile) if value <= cap)
        require(maximum == expected, (n, maximum, expected))

    print(f"independent_sharp_cases={checked}")
    print("independent_n6_m3_overlap_cap=11")
    print("independent_n8_m4_overlap_cap=36")
    print("independent_n10_m5_overlap_cap=127")
    print("GENERAL_SAME_SPAN_CHOW_OVERLAP_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
