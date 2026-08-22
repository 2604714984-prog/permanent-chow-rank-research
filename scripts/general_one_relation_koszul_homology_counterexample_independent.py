#!/usr/bin/env python3
"""Independent sparse-matrix replay of the full-circuit Koszul H1 gap."""

from __future__ import annotations

from itertools import combinations
from math import comb

PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def subsets(n: int, size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(combinations(range(n), size))


def add_entry(matrix: list[list[int]], row: int, column: int, value: int) -> None:
    matrix[row][column] = (matrix[row][column] + value) % PRIME


def multiplication_terms(label: int, support: tuple[int, ...], n: int):
    chosen = set(support)
    if label not in chosen:
        yield tuple(sorted((*support, label))), 1
    anchor = n - 1
    if anchor not in chosen:
        yield tuple(sorted((*support, anchor))), 1


def replay(n: int) -> dict[str, int]:
    require(n >= 5, n)
    r = n - 1
    source_basis = subsets(n, n - 3)
    middle_poly_basis = subsets(n, n - 2)
    target_poly_basis = subsets(n, n - 1)
    middle_index = {value: index for index, value in enumerate(middle_poly_basis)}
    target_index = {value: index for index, value in enumerate(target_poly_basis)}
    pair_basis = tuple(combinations(range(r), 2))
    pair_index = {value: index for index, value in enumerate(pair_basis)}

    left_rows = r * len(middle_poly_basis)
    left = [[0] * len(source_basis) for _ in range(left_rows)]
    for column, source in enumerate(source_basis):
        for label in range(r):
            for output, coefficient in multiplication_terms(label, source, n):
                row = label * len(middle_poly_basis) + middle_index[output]
                add_entry(left, row, column, coefficient)

    right_rows = len(pair_basis) * len(target_poly_basis)
    right_columns = r * len(middle_poly_basis)
    right = [[0] * right_columns for _ in range(right_rows)]
    for label in range(r):
        for support, support_position in middle_index.items():
            column = label * len(middle_poly_basis) + support_position
            for other in range(r):
                if other == label:
                    continue
                pair = tuple(sorted((label, other)))
                sign = 1 if label == pair[1] else -1
                for output, coefficient in multiplication_terms(other, support, n):
                    row = pair_index[pair] * len(target_poly_basis) + target_index[output]
                    add_entry(right, row, column, sign * coefficient)

    for row in range(right_rows):
        for column in range(len(source_basis)):
            value = sum(
                right[row][middle] * left[middle][column]
                for middle in range(left_rows)
            ) % PRIME
            require(value == 0, (n, row, column, value))

    left_rank = rank_mod(left)
    right_rank = rank_mod(right)
    homology = left_rows - left_rank - right_rank
    require(left_rank == comb(n, 3), (n, left_rank))
    require(right_rank == 2 * comb(n, 3), (n, right_rank))
    require(homology == comb(n, 2), (n, homology))
    return {
        "n": n,
        "left_rank": left_rank,
        "right_rank": right_rank,
        "homology": homology,
        "independent_cap": n - 1,
    }


def main() -> None:
    rows = [replay(n) for n in range(5, 10)]
    require(all(row["homology"] > row["independent_cap"] for row in rows), rows)
    print("GENERAL_ONE_RELATION_KOSZUL_HOMOLOGY_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
