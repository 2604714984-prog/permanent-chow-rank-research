#!/usr/bin/env python3
"""Independent incidence-projector replay for row/column isotype projections.

This implementation imports none of the primary audit. It constructs the
nested Johnson incidence spaces, obtains the primitive projectors by exact
Gram inversion modulo a second prime, reconstructs all Krein support masks,
and checks every arbitrary union of row/column isotype pairs through n=8.
"""
from __future__ import annotations

import itertools
from math import comb

PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    columns = list(zip(*b))
    return [
        [
            sum(x * y for x, y in zip(row, column)) % PRIME
            for column in columns
        ]
        for row in a
    ]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(column) for column in zip(*a)]


def rank_mod(a: list[list[int]]) -> int:
    if not a:
        return 0
    a = [row[:] for row in a]
    row_count = len(a)
    column_count = len(a[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (
                index
                for index in range(rank, row_count)
                if a[index][column] % PRIME
            ),
            None,
        )
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][column], PRIME - 2, PRIME)
        a[rank] = [value * inverse % PRIME for value in a[rank]]
        for index in range(row_count):
            if index == rank or not a[index][column]:
                continue
            multiplier = a[index][column]
            a[index] = [
                (left - multiplier * right) % PRIME
                for left, right in zip(a[index], a[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def inverse_mod(a: list[list[int]]) -> list[list[int]]:
    size = len(a)
    augmented = [
        [a[i][j] % PRIME for j in range(size)]
        + [1 if i == j else 0 for j in range(size)]
        for i in range(size)
    ]
    rank = 0
    for column in range(size):
        pivot = next(
            (
                index
                for index in range(rank, size)
                if augmented[index][column]
            ),
            None,
        )
        require(pivot is not None, ("singular", column))
        augmented[rank], augmented[pivot] = augmented[pivot], augmented[rank]
        inverse = pow(augmented[rank][column], PRIME - 2, PRIME)
        augmented[rank] = [
            value * inverse % PRIME for value in augmented[rank]
        ]
        for index in range(size):
            if index == rank or not augmented[index][column]:
                continue
            multiplier = augmented[index][column]
            augmented[index] = [
                (left - multiplier * right) % PRIME
                for left, right in zip(augmented[index], augmented[rank])
            ]
        rank += 1
    return [row[size:] for row in augmented]


def incidence_projectors(n: int, m: int):
    subsets = list(itertools.combinations(range(n), m))
    subset_sets = [set(value) for value in subsets]
    size = len(subsets)
    maximum_index = min(m, n - m)
    nested_projectors = []
    for index in range(maximum_index + 1):
        lower_subsets = list(itertools.combinations(range(n), index))
        incidence = [
            [
                1 if set(lower) <= subset_sets[column] else 0
                for column in range(size)
            ]
            for lower in lower_subsets
        ]
        gram = matmul(incidence, transpose(incidence))
        gram_inverse = inverse_mod(gram)
        nested_projectors.append(
            matmul(transpose(incidence), matmul(gram_inverse, incidence))
        )

    projectors = []
    previous = [[0] * size for _ in range(size)]
    for index, nested in enumerate(nested_projectors):
        projector = [
            [
                (nested[row][column] - previous[row][column]) % PRIME
                for column in range(size)
            ]
            for row in range(size)
        ]
        require(
            matmul(projector, projector) == projector,
            (n, m, index, "idempotence"),
        )
        dimension = comb(n, index) - (comb(n, index - 1) if index else 0)
        require(
            rank_mod(projector) == dimension,
            (n, m, index, rank_mod(projector), dimension),
        )
        projectors.append(projector)
        previous = nested
    return size, projectors


def main() -> int:
    projector_checks = 0
    rectangle_checks = 0
    arbitrary_union_checks = 0
    maxima = []
    for n in range(2, 9):
        best = 0
        for m in range(1, n):
            if m > n - m:
                continue
            size, projectors = incidence_projectors(n, m)
            dimensions = [
                comb(n, index) - (comb(n, index - 1) if index else 0)
                for index in range(len(projectors))
            ]
            projector_checks += len(projectors)
            pair_rows = []
            for i, left in enumerate(projectors):
                for j, right in enumerate(projectors):
                    gram = [
                        [
                            left[row][column]
                            * right[row][column]
                            % PRIME
                            for column in range(size)
                        ]
                        for row in range(size)
                    ]
                    diagonal_rank = rank_mod(gram)
                    support_mask = 0
                    for k, projector in enumerate(projectors):
                        trace = sum(
                            projector[row][column] * gram[column][row]
                            for row in range(size)
                            for column in range(size)
                        ) % PRIME
                        if trace:
                            support_mask |= 1 << k
                    support_dimension = sum(
                        dimensions[k]
                        for k in range(len(dimensions))
                        if support_mask & (1 << k)
                    )
                    require(
                        diagonal_rank == support_dimension,
                        (n, m, i, j, diagonal_rank, support_mask),
                    )
                    require(
                        diagonal_rank
                        >= max(dimensions[i], dimensions[j]),
                        (n, m, i, j, diagonal_rank),
                    )
                    ceiling = (
                        dimensions[i] * dimensions[j]
                        + diagonal_rank
                        - 1
                    ) // diagonal_rank
                    require(
                        ceiling <= size,
                        (n, m, i, j, ceiling, size),
                    )
                    best = max(best, ceiling)
                    pair_rows.append(
                        (dimensions[i] * dimensions[j], support_mask)
                    )
                    rectangle_checks += 1

            for mask in range(1, 1 << len(dimensions)):
                denominator = sum(
                    dimensions[k]
                    for k in range(len(dimensions))
                    if mask & (1 << k)
                )
                numerator = sum(
                    weight
                    for weight, support in pair_rows
                    if support & ~mask == 0
                )
                require(
                    numerator <= size * denominator,
                    (n, m, mask, numerator, denominator, size),
                )
                best = max(
                    best,
                    (numerator + denominator - 1) // denominator,
                )
                arbitrary_union_checks += 1
        maxima.append(best)

    require(
        (
            projector_checks,
            rectangle_checks,
            arbitrary_union_checks,
        )
        == (46, 146, 132),
        (projector_checks, rectangle_checks, arbitrary_union_checks),
    )
    require(maxima == [2, 3, 6, 10, 20, 35, 70], maxima)
    print(f"independent_projector_checks={projector_checks}")
    print(f"independent_rectangle_checks={rectangle_checks}")
    print(f"independent_arbitrary_union_checks={arbitrary_union_checks}")
    print("independent_maxima_n2_to_n8=" + ",".join(map(str, maxima)))
    print(
        "GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_"
        "INDEPENDENT_PASS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
