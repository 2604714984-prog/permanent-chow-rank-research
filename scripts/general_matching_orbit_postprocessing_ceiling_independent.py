#!/usr/bin/env python3
"""Independent kernel-intersection replay of the matching-orbit theorem.

This implementation imports none of the primary audit. It represents a fixed
linear postprocessing map by its kernel, computes intersections with every
matching graph subspace via dimension formulas, and verifies the averaged
kernel-intersection inequality over a second prime.
"""
from __future__ import annotations

from itertools import combinations, permutations
from math import comb

PRIME = 1_000_033


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def rank_mod(matrix, prime=PRIME):
    rows = [[x % prime for x in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    row_count = len(rows)
    column_count = len(rows[0])
    for column in range(column_count):
        pivot = next((i for i in range(rank, row_count) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [(x * inverse) % prime for x in rows[rank]]
        for i in range(row_count):
            if i != rank and rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [
                    (x - coefficient * y) % prime
                    for x, y in zip(rows[i], rows[rank], strict=True)
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def action_tables(n, m):
    subsets = tuple(combinations(range(n), m))
    index = {subset: i for i, subset in enumerate(subsets)}
    perms = tuple(permutations(range(n)))
    actions = tuple(
        tuple(index[tuple(sorted(p[i] for i in subset))] for subset in subsets)
        for p in perms
    )
    return subsets, perms, actions


def graph_basis(left, right, module_dimension, auxiliary_dimension, domain_dimension):
    rows = []
    for subset in range(module_dimension):
        for auxiliary in range(auxiliary_dimension):
            vector = [0] * domain_dimension
            vector[
                ((left[subset] * module_dimension + right[subset]) * auxiliary_dimension + auxiliary)
            ] = 1
            rows.append(vector)
    return rows


def deterministic_kernel(rows, columns, seed):
    return [
        [
            ((i + 2) * (j + 5) + seed * (3*i*i + 7*j*j + 11*i*j + 13)) % PRIME
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def main():
    coverage = 0
    intersection_checks = 0
    average_checks = 0
    rank_checks = 0
    for n in range(3, 5):
        for m in range(1, n//2 + 1):
            _, perms, actions = action_tables(n, m)
            module_dimension = comb(n, m)
            group_size = len(perms)
            counts = [[0] * module_dimension for _ in range(module_dimension)]
            for left in actions:
                for right in actions:
                    for subset in range(module_dimension):
                        counts[left[subset]][right[subset]] += 1
            expected = group_size * group_size // module_dimension
            require(all(value == expected for row in counts for value in row), (n, m))
            coverage += module_dimension * module_dimension

            for auxiliary_dimension in (1, 2):
                domain_dimension = module_dimension * module_dimension * auxiliary_dimension
                for seed in (3, 7):
                    kernel_rows = deterministic_kernel(
                        max(1, domain_dimension//4),
                        domain_dimension,
                        seed + 17*n + 5*m + auxiliary_dimension,
                    )
                    kernel_rank = rank_mod(kernel_rows)
                    full_rank = domain_dimension - kernel_rank
                    total_restriction = 0
                    best = 0
                    total_intersection = 0
                    for left in actions:
                        for right in actions:
                            graph = graph_basis(
                                left,
                                right,
                                module_dimension,
                                auxiliary_dimension,
                                domain_dimension,
                            )
                            graph_dimension = module_dimension * auxiliary_dimension
                            sum_rank = rank_mod(kernel_rows + graph)
                            intersection = kernel_rank + graph_dimension - sum_rank
                            restriction = graph_dimension - intersection
                            require(0 <= intersection <= graph_dimension, (n, m, auxiliary_dimension, seed))
                            best = max(best, restriction)
                            total_restriction += restriction
                            total_intersection += intersection
                            intersection_checks += 1
                    require(module_dimension * best >= full_rank, (n, m, auxiliary_dimension, seed, full_rank, best))
                    require(
                        total_intersection * module_dimension <= kernel_rank * group_size * group_size,
                        (n, m, auxiliary_dimension, seed, "average kernel"),
                    )
                    require(
                        total_restriction * module_dimension >= full_rank * group_size * group_size,
                        (n, m, auxiliary_dimension, seed, "average rank"),
                    )
                    average_checks += 2
                    rank_checks += 1

    require(coverage == 61, coverage)
    require(intersection_checks == 4_752, intersection_checks)
    require(average_checks == 24, average_checks)
    require(rank_checks == 12, rank_checks)
    print("independent_coverage_checks=61")
    print("independent_kernel_intersection_checks=4752")
    print("independent_average_checks=24")
    print("independent_rank_bound_checks=12")
    print("GENERAL_MATCHING_ORBIT_POSTPROCESSING_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
