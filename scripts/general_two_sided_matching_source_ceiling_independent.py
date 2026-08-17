#!/usr/bin/env python3
"""Independent replay of the two-sided matching-source ceiling.

This file imports none of the primary audit. It explicitly enumerates partial
matchings, graph-coordinate supports and a second family of dense rational
subspaces, then checks disjoint large-n block arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_fraction(matrix: list[list[Fraction]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for index in range(row_count):
            if index == rank or not rows[index][column]:
                continue
            factor = rows[index][column]
            rows[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[index], rows[rank], strict=True)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def multiply(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        [
            sum(
                Fraction(left[row][index]) * Fraction(right[index][column])
                for index in range(len(right))
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    rows = [
        [Fraction(matrix[row][column]) for column in range(size)]
        + [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column]),
            None,
        )
        require(pivot is not None, ("singular", column))
        rows[column], rows[pivot] = rows[pivot], rows[column]
        pivot_value = rows[column][column]
        rows[column] = [value / pivot_value for value in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[row], rows[column], strict=True)
            ]
    return [row[size:] for row in rows]


def gram(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return multiply(transpose(matrix), matrix)


def graph_data(
    n: int,
    degree: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    subsets = tuple(combinations(range(n), degree))
    index = {subset: position for position, subset in enumerate(subsets)}
    maps = []
    for permutation in permutations(range(n)):
        maps.append(
            tuple(
                index[tuple(sorted(permutation[value] for value in subset))]
                for subset in subsets
            )
        )
    return subsets, tuple(maps)


def explicit_partial_matching_checks() -> tuple[int, int]:
    checks = 0
    surviving = 0
    for n in range(2, 6):
        for degree in range(1, n):
            subsets = tuple(combinations(range(n), degree))
            for sigma in permutations(range(n)):
                for rows in subsets:
                    row_set = set(rows)
                    row_complement = tuple(
                        value for value in range(n) if value not in row_set
                    )
                    sigma_rows = tuple(sorted(sigma[value] for value in rows))
                    for columns in subsets:
                        column_set = set(columns)
                        column_complement = tuple(
                            value for value in range(n) if value not in column_set
                        )
                        count = 0
                        for image in permutations(column_complement):
                            partial = dict(zip(row_complement, image, strict=True))
                            if all(partial[value] == sigma[value] for value in row_complement):
                                count += 1
                        expected = int(columns == sigma_rows)
                        require(count == expected, (n, degree, rows, columns, sigma))
                        checks += 1
                        surviving += count
    return checks, surviving


def coordinate_support_checks() -> tuple[int, int]:
    rank_checks = 0
    average_checks = 0
    modulus = 4_294_967_291

    for n in range(2, 8):
        for degree in range(1, n):
            subsets, maps = graph_data(n, degree)
            width = len(subsets)
            ambient = width * width
            sizes = sorted(
                {
                    1,
                    width,
                    max(1, ambient // 4),
                    max(1, ambient // 2),
                    ambient - 1,
                    ambient,
                }
            )
            for salt, size in enumerate(sizes):
                order = sorted(
                    range(ambient),
                    key=lambda value: (
                        (value + 1) * 2_654_435_761 + salt * 97_531
                    )
                    % modulus,
                )
                support = set(order[:size])
                hits = []
                for graph_map in maps:
                    graph = {
                        source * width + graph_map[source]
                        for source in range(width)
                    }
                    hits.append(len(support & graph))
                    rank_checks += 1
                average = Fraction(sum(hits), len(hits))
                require(average == Fraction(size, width), (n, degree, size, average))
                require(max(hits) >= ceil(size / width), (n, degree, size, hits))
                average_checks += 1

    return rank_checks, average_checks


def dense_checks() -> tuple[int, int]:
    computations = 0
    average_checks = 0

    for n in range(3, 6):
        for degree in range(1, n // 2 + 1):
            subsets, maps = graph_data(n, degree)
            width = len(subsets)
            ambient = width * width
            ranks = sorted({2, min(width + 1, ambient), min(2 * width - 1, ambient)})
            for subspace_rank in ranks:
                basis = [
                    [
                        Fraction(comb(coordinate + power + 1, power + 1))
                        for power in range(subspace_rank)
                    ]
                    for coordinate in range(ambient)
                ]
                require(rank_fraction(basis) == subspace_rank, (n, degree, subspace_rank))
                gram_inverse = inverse(gram(basis))
                traces = []
                ranks_seen = []
                for graph_map in maps:
                    mask = [
                        source * width + graph_map[source]
                        for source in range(width)
                    ]
                    restricted = [basis[index] for index in mask]
                    compression = multiply(gram_inverse, gram(restricted))
                    traces.append(
                        sum(compression[index][index] for index in range(subspace_rank))
                    )
                    ranks_seen.append(rank_fraction(restricted))
                    computations += 1
                average = sum(traces, Fraction(0)) / len(traces)
                require(average == Fraction(subspace_rank, width), (n, degree, average))
                require(max(ranks_seen) >= ceil(subspace_rank / width), ranks_seen)
                average_checks += 1

    return computations, average_checks


def disjoint_block_arithmetic() -> tuple[int, int]:
    support_checks = 0
    block_checks = 0
    for n in range(31, 46):
        central = comb(n, n // 2)
        numerator = 0
        denominator = Fraction(0)
        for degree in range(1, n):
            width = comb(n, degree)
            for dimension in (width, width * (width + 1) // 2, width * width):
                term_rank = ceil(dimension / width)
                require(ceil(dimension / term_rank) <= width, (n, degree, dimension))
                support_checks += 1
            numerator += width * width
            denominator += width
        require(Fraction(numerator, 1) / denominator <= central, n)
        block_checks += 1
    return support_checks, block_checks


def main() -> int:
    partial_checks, surviving = explicit_partial_matching_checks()
    coordinate_ranks, coordinate_averages = coordinate_support_checks()
    dense_ranks, dense_averages = dense_checks()
    support_checks, block_checks = disjoint_block_arithmetic()

    require((partial_checks, surviving) == (31_748, 3_976), (partial_checks, surviving))
    require((coordinate_ranks, coordinate_averages) == (206_384, 122), (coordinate_ranks, coordinate_averages))
    require((dense_ranks, dense_averages) == (882, 15), (dense_ranks, dense_averages))
    require((support_checks, block_checks) == (1_665, 15), (support_checks, block_checks))

    print("independent_partial_matching_checks=31748")
    print("independent_surviving_partial_matchings=3976")
    print("independent_coordinate_restriction_ranks=206384")
    print("independent_coordinate_average_checks=122")
    print("independent_dense_restriction_ranks=882")
    print("independent_dense_average_checks=15")
    print("independent_large_n_support_checks=1665")
    print("independent_large_n_block_checks=15")
    print("GENERAL_TWO_SIDED_MATCHING_SOURCE_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
