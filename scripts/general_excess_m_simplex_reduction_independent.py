#!/usr/bin/env python3
"""Independent replay for the excess-m simplex reduction.

This implementation imports none of the primary helpers.  It scans legal rows
by term count through m=256, constructs the canonical no-private simplex over
finite prime fields for selected m, and independently reconstructs the quartic
three-subset rectangle threshold.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def modular_rank(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = [[value % prime for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if rows[row][column] % prime
            ),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        rows[pivot_row] = [value * inverse % prime for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def canonical_simplex_columns(m: int) -> list[list[list[int]]]:
    """Return m coordinate blocks and one diagonal block in dimension m^2."""

    dimension = m * m
    blocks: list[list[list[int]]] = []
    for block in range(m):
        columns: list[list[int]] = []
        for coordinate in range(m):
            vector = [0] * dimension
            vector[block * m + coordinate] = 1
            columns.append(vector)
        blocks.append(columns)

    diagonal: list[list[int]] = []
    for coordinate in range(m):
        vector = [0] * dimension
        for block in range(m):
            vector[block * m + coordinate] = 1
        diagonal.append(vector)
    blocks.append(diagonal)
    return blocks


def column_matrix(blocks: list[list[list[int]]], selected: tuple[int, ...]) -> list[list[int]]:
    columns = [column for index in selected for column in blocks[index]]
    if not columns:
        return []
    return [list(row) for row in zip(*columns)]


def main() -> int:
    rows: list[tuple[int, int, int]] = []
    arithmetic_checks = 0
    cubic_rows: list[tuple[int, int, int]] = []
    quartic_rows: list[tuple[int, int, int]] = []

    for m in range(3, 257):
        total = m * m + m
        maximum_q = total // m
        for q in range(2, maximum_q + 1):
            arithmetic_checks += 1
            if total % q:
                continue
            n = total // q
            if n < m:
                continue
            rows.append((n, m, q))
            if m == 3:
                cubic_rows.append((n, m, q))
            elif m >= 5:
                require(n < (m - 1) ** 2, (n, m, q))
                require(2 * m < (m - 1) ** 2, (n, m, q))
            elif m == 4:
                quartic_rows.append((n, m, q))

    require(
        cubic_rows == [(6, 3, 2), (4, 3, 3), (3, 3, 4)],
        cubic_rows,
    )
    require(
        quartic_rows == [(10, 4, 2), (5, 4, 4), (4, 4, 5)],
        quartic_rows,
    )

    simplex_checks = 0
    proper_subset_checks = 0
    for m in range(4, 13):
        blocks = canonical_simplex_columns(m)
        full = column_matrix(blocks, tuple(range(m + 1)))
        require(modular_rank(full) == m * m, ("full simplex rank", m))
        require((m + 1) * m - modular_rank(full) == m, ("kernel", m))
        simplex_checks += 1

        for omitted in range(m + 1):
            selected = tuple(index for index in range(m + 1) if index != omitted)
            matrix = column_matrix(blocks, selected)
            require(modular_rank(matrix) == m * m, ("proper directness", m, omitted))
            proper_subset_checks += 1

        # The covector with +1 in one coordinate block and -1 in another
        # vanishes on every diagonal column and has support on exactly 2m
        # ambient coordinate directions.
        for coordinate in range(m):
            diagonal_column = blocks[-1][coordinate]
            value = diagonal_column[coordinate] - diagonal_column[m + coordinate]
            require(value == 0, ("difference does not kill diagonal", m, coordinate))
        require(2 * m < (m - 1) ** 2, ("support gap", m))

    triples = tuple(frozenset(value) for value in combinations(range(10), 3))
    overlap_histogram: Counter[tuple[int, bool]] = Counter()
    labelled_subset_pair_checks = 0
    for left_index, left in enumerate(triples):
        for right_index, right in enumerate(triples):
            overlap_histogram[(len(left & right), left_index == right_index)] += 1
            labelled_subset_pair_checks += 1

    require(labelled_subset_pair_checks == 120**2, labelled_subset_pair_checks)
    require(overlap_histogram[(3, True)] == 120, overlap_histogram)
    require((3, False) not in overlap_histogram, overlap_histogram)

    maximum_distinct_product = 0
    overlap_type_checks = 0
    for (row_overlap, row_equal), (column_overlap, column_equal) in product(
        overlap_histogram,
        repeat=2,
    ):
        if row_equal and column_equal:
            continue
        maximum_distinct_product = max(
            maximum_distinct_product,
            row_overlap * column_overlap,
        )
        overlap_type_checks += 1

    require(maximum_distinct_product == 6, maximum_distinct_product)
    require(18 - maximum_distinct_product == 12, maximum_distinct_product)

    print(f"independent_arithmetic_checks={arithmetic_checks}")
    print(f"independent_excess_m_rows={len(rows)}")
    print(f"independent_simplex_checks={simplex_checks}")
    print(f"independent_proper_subset_checks={proper_subset_checks}")
    print("independent_cubic_rows=(6,3,2),(4,3,3),(3,3,4)")
    print("independent_quartic_rows=(10,4,2),(5,4,4),(4,4,5)")
    print(f"independent_labelled_subset_pair_checks={labelled_subset_pair_checks}")
    print(f"independent_overlap_type_checks={overlap_type_checks}")
    print("independent_quartic_minimum_two_rectangle_union=12")
    print("GENERAL_EXCESS_M_SIMPLEX_REDUCTION_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
