#!/usr/bin/env python3
"""Exact coordinate-monomial quotient-gain audit for ``perm_6``.

The script proves and independently replays the following finite statement.

For every degree-six coordinate monomial ``M`` in the 36 variables ``x_ij``,
the central first-Koszul image of ``D_3(M)`` is disjoint from the central
first-Koszul image of ``D_3(perm_6)``. Equivalently, the quotient Koszul gain
of ``M`` equals the full Koszul rank of ``M``.

The proof-facing finite boundary consists of:

* 167 bipartite multigraph orbits with six edges, including multiplicities;
* the exact monomial prolongation dimension for each multiplicity partition;
* sparse rank calculations modulo 1,000,003 used only as characteristic-zero
  lower bounds, paired with matching characteristic-zero upper bounds; and
* two small integer minors of determinant -1 for the unique ``K_{2,3}``
  rectangle-space obstruction.

This is a coordinate fixed-point theorem. It does not by itself prove the
same full-gain statement for an arbitrary non-monomial Chow term, because
Koszul rank can drop non-strictly under torus specialization.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from functools import lru_cache
from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
)
from pathlib import Path
from typing import Iterable

N = 6
VARIABLES = N * N
PRIME = 1_000_003

Monomial = tuple[int, ...]
SparseColumn = dict[int, int]
Matrix = tuple[tuple[int, ...], ...]


def restricted_growth_partitions(size: int = 6) -> list[tuple[int, ...]]:
    """Return all set partitions in restricted-growth-string encoding."""

    out: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], maximum: int) -> None:
        if len(prefix) == size:
            out.append(prefix)
            return
        for value in range(maximum + 2):
            rec(prefix + (value,), max(maximum, value))

    rec((0,), 0)
    return out


def matrix_from_partitions(
    row_partition: tuple[int, ...],
    column_partition: tuple[int, ...],
) -> Matrix:
    rows = max(row_partition) + 1
    columns = max(column_partition) + 1
    matrix = [[0] * columns for _ in range(rows)]
    for row, column in zip(row_partition, column_partition, strict=True):
        matrix[row][column] += 1
    return tuple(tuple(entry for entry in row) for row in matrix)


@lru_cache(maxsize=None)
def row_permutations(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(permutations(range(size)))


def canonical_without_transpose(matrix: Matrix) -> tuple[tuple[int, int], tuple[int, ...]]:
    """Canonicalize a nonnegative matrix under independent row/column permutations."""

    rows = len(matrix)
    columns = len(matrix[0])
    best: tuple[tuple[int, int], tuple[int, ...]] | None = None

    for row_order in row_permutations(rows):
        column_vectors = [
            tuple(matrix[row_order[index]][column] for index in range(rows))
            for column in range(columns)
        ]
        column_order = sorted(range(columns), key=column_vectors.__getitem__)
        flattened = tuple(
            matrix[row_order[row]][column]
            for row in range(rows)
            for column in column_order
        )
        candidate = ((rows, columns), flattened)
        if best is None or candidate < best:
            best = candidate

    if best is None:
        raise AssertionError("empty matrix")
    return best


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def canonical_matrix(matrix: Matrix) -> tuple[tuple[int, int], tuple[int, ...]]:
    return min(
        canonical_without_transpose(matrix),
        canonical_without_transpose(transpose(matrix)),
    )


def orbit_representatives() -> list[Matrix]:
    """Enumerate all bipartite multigraph orbits with six unlabeled edges."""

    partitions = restricted_growth_partitions()
    representatives: dict[tuple[tuple[int, int], tuple[int, ...]], Matrix] = {}
    for row_partition in partitions:
        for column_partition in partitions:
            matrix = matrix_from_partitions(row_partition, column_partition)
            representatives.setdefault(canonical_matrix(matrix), matrix)

    out = list(representatives.values())
    if len(out) != 167:
        raise AssertionError(f"expected 167 orbits, found {len(out)}")
    return out


def edge_multiset(matrix: Matrix) -> list[int]:
    edges: list[int] = []
    for row, entries in enumerate(matrix):
        for column, multiplicity in enumerate(entries):
            edges.extend([row * N + column] * multiplicity)
    if len(edges) != 6:
        raise AssertionError(edges)
    return edges


def support_edges(matrix: Matrix) -> set[tuple[int, int]]:
    return {
        (row, column)
        for row, entries in enumerate(matrix)
        for column, multiplicity in enumerate(entries)
        if multiplicity
    }


def rectangle_count(matrix: Matrix) -> int:
    support = support_edges(matrix)
    count = 0
    for first_row, second_row in combinations(range(len(matrix)), 2):
        for first_column, second_column in combinations(range(len(matrix[0])), 2):
            if all(
                (row, column) in support
                for row in (first_row, second_row)
                for column in (first_column, second_column)
            ):
                count += 1
    return count


def verify_rectangle_classification(matrix: Matrix) -> None:
    """Verify the 0/1/3-cycle classification for supports with at most six edges."""

    count = rectangle_count(matrix)
    if count not in {0, 1, 3}:
        raise AssertionError((matrix, count))

    if count != 3:
        return

    support = support_edges(matrix)
    if len(support) != 6:
        raise AssertionError("three rectangles require six distinct edges")

    row_degrees = sorted(
        Counter(row for row, _ in support).values(),
        reverse=True,
    )
    column_degrees = sorted(
        Counter(column for _, column in support).values(),
        reverse=True,
    )
    valid = {
        (tuple(row_degrees), tuple(column_degrees)),
        (tuple(column_degrees), tuple(row_degrees)),
    }
    if ((3, 3), (2, 2, 2)) not in valid:
        raise AssertionError("three-rectangle support is not K_2,3 or K_3,2")


def pair_maps() -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
    symmetric: dict[tuple[int, int], int] = {}
    index = 0
    for first in range(VARIABLES):
        for second in range(first, VARIABLES):
            symmetric[(first, second)] = index
            index += 1

    wedge: dict[tuple[int, int], int] = {}
    index = 0
    for first in range(VARIABLES):
        for second in range(first + 1, VARIABLES):
            wedge[(first, second)] = index
            index += 1

    if len(symmetric) != 666 or len(wedge) != 630:
        raise AssertionError((len(symmetric), len(wedge)))
    return symmetric, wedge


SYMMETRIC_INDEX, WEDGE_INDEX = pair_maps()


def permanent_cubic(rows: tuple[int, ...], columns: tuple[int, ...]) -> list[Monomial]:
    return [
        tuple(
            sorted(
                rows[index] * N + columns[sigma[index]]
                for index in range(3)
            )
        )
        for sigma in permutations(range(3))
    ]


def delta_column(
    polynomial: Iterable[Monomial],
    tensor_variable: int,
) -> SparseColumn:
    entries: Counter[int] = Counter()
    for monomial in polynomial:
        for position, variable in enumerate(monomial):
            if variable == tensor_variable:
                continue
            remaining = [
                monomial[index]
                for index in range(3)
                if index != position
            ]
            remaining.sort()
            first, second = sorted((variable, tensor_variable))
            sign = 1 if variable < tensor_variable else -1
            row = (
                SYMMETRIC_INDEX[(remaining[0], remaining[1])] * 630
                + WEDGE_INDEX[(first, second)]
            )
            entries[row] += sign
    return {
        row: value % PRIME
        for row, value in entries.items()
        if value % PRIME
    }


def add_column(
    raw_column: SparseColumn,
    base_pivots: dict[int, SparseColumn],
    local_pivots: dict[int, SparseColumn],
) -> bool:
    column = dict(raw_column)
    while column:
        pivot = min(column)
        pivot_column = local_pivots.get(pivot)
        if pivot_column is None:
            pivot_column = base_pivots.get(pivot)

        if pivot_column is None:
            inverse = pow(column[pivot], PRIME - 2, PRIME)
            normalized = {
                row: value * inverse % PRIME
                for row, value in column.items()
                if value * inverse % PRIME
            }
            local_pivots[pivot] = normalized
            return True

        factor = column[pivot]
        for row, value in pivot_column.items():
            updated = (column.get(row, 0) - factor * value) % PRIME
            if updated:
                column[row] = updated
            else:
                column.pop(row, None)
    return False


def permanent_pivots() -> dict[int, SparseColumn]:
    pivots: dict[int, SparseColumn] = {}
    triples = list(combinations(range(N), 3))

    for rows in triples:
        for columns in triples:
            polynomial = permanent_cubic(rows, columns)
            for tensor_variable in range(VARIABLES):
                add_column(
                    delta_column(polynomial, tensor_variable),
                    {},
                    pivots,
                )

    if len(pivots) != 14_175:
        raise AssertionError(len(pivots))
    return pivots


def degree_three_divisors(edges: list[int]) -> list[Monomial]:
    multiplicities = Counter(edges)
    variables = sorted(multiplicities)
    out: list[Monomial] = []

    def rec(index: int, remaining: int, chosen: list[tuple[int, int]]) -> None:
        if index == len(variables):
            if remaining == 0:
                monomial: list[int] = []
                for variable, count in chosen:
                    monomial.extend([variable] * count)
                out.append(tuple(monomial))
            return

        variable = variables[index]
        for count in range(min(multiplicities[variable], remaining) + 1):
            chosen.append((variable, count))
            rec(index + 1, remaining - count, chosen)
            chosen.pop()

    rec(0, 3, [])
    return out


def monomial_prolongation_dimension(edges: list[int]) -> int:
    """Count the degree-four monomials in ``D_3(M)^(1)`` exactly."""

    derivative_basis = set(degree_three_divisors(edges))
    support = sorted(set(edges))
    count = 0

    for monomial in combinations_with_replacement(support, 4):
        if all(
            tuple(monomial[:position] + monomial[position + 1 :])
            in derivative_basis
            for position in range(4)
        ):
            count += 1
    return count


def term_rank_and_quotient_gain(
    edges: list[int],
    base_pivots: dict[int, SparseColumn],
) -> tuple[int, int, int, int]:
    derivative_basis = degree_three_divisors(edges)
    prolongation_dimension = monomial_prolongation_dimension(edges)
    exact_term_rank = (
        VARIABLES * len(derivative_basis) - prolongation_dimension
    )

    term_pivots: dict[int, SparseColumn] = {}
    quotient_pivots: dict[int, SparseColumn] = {}

    for monomial in derivative_basis:
        polynomial = [monomial]
        for tensor_variable in range(VARIABLES):
            column = delta_column(polynomial, tensor_variable)
            add_column(column, {}, term_pivots)
            add_column(column, base_pivots, quotient_pivots)

    modular_term_rank = len(term_pivots)
    modular_quotient_gain = len(quotient_pivots)
    if modular_term_rank != exact_term_rank:
        raise AssertionError(
            (modular_term_rank, exact_term_rank, edges)
        )
    if modular_quotient_gain != exact_term_rank:
        raise AssertionError(
            (modular_quotient_gain, exact_term_rank, edges)
        )

    return (
        len(derivative_basis),
        prolongation_dimension,
        exact_term_rank,
        modular_quotient_gain,
    )


def wedge_sign(values: tuple[int, ...]) -> tuple[tuple[int, ...] | None, int]:
    if len(set(values)) != len(values):
        return None, 0
    inversions = sum(
        values[first] > values[second]
        for first in range(len(values))
        for second in range(first + 1, len(values))
    )
    return tuple(sorted(values)), -1 if inversions % 2 else 1


def k23_local_matrices() -> tuple[list[list[int]], list[list[int]]]:
    """Build the two local integer matrices used in the K_2,3 proof."""

    local_variables = 6
    wedge_two = list(combinations(range(local_variables), 2))
    wedge_three = list(combinations(range(local_variables), 3))
    wedge_two_index = {value: index for index, value in enumerate(wedge_two)}
    wedge_three_index = {value: index for index, value in enumerate(wedge_three)}

    # Variables are a_1,a_2,a_3,b_1,b_2,b_3.
    quadrics = [
        {(0, 4): 1, (1, 3): 1},
        {(0, 5): 1, (2, 3): 1},
        {(1, 5): 1, (2, 4): 1},
    ]

    first = [
        [0 for _ in range(len(quadrics) * local_variables)]
        for _ in range(local_variables * len(wedge_two))
    ]
    for quadric_index, quadric in enumerate(quadrics):
        for tensor_variable in range(local_variables):
            column = quadric_index * local_variables + tensor_variable
            for monomial, coefficient in quadric.items():
                for position, variable in enumerate(monomial):
                    if variable == tensor_variable:
                        continue
                    remaining = monomial[1 - position]
                    wedge, sign = wedge_sign((variable, tensor_variable))
                    if wedge is None:
                        continue
                    row = (
                        remaining * len(wedge_two)
                        + wedge_two_index[wedge]
                    )
                    first[row][column] += coefficient * sign

    second = [
        [0 for _ in range(len(quadrics) * len(wedge_two))]
        for _ in range(local_variables * len(wedge_three))
    ]
    for quadric_index, quadric in enumerate(quadrics):
        for wedge_index_value, pair in enumerate(wedge_two):
            column = quadric_index * len(wedge_two) + wedge_index_value
            for monomial, coefficient in quadric.items():
                for position, variable in enumerate(monomial):
                    remaining = monomial[1 - position]
                    wedge, sign = wedge_sign((variable, pair[0], pair[1]))
                    if wedge is None:
                        continue
                    row = (
                        remaining * len(wedge_three)
                        + wedge_three_index[wedge]
                    )
                    second[row][column] += coefficient * sign

    return first, second


def bareiss_determinant(matrix: list[list[int]]) -> int:
    """Return an exact determinant by fraction-free Bareiss elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    data = [row[:] for row in matrix]
    sign = 1
    previous = 1

    for pivot_index in range(size - 1):
        if data[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if data[row][pivot_index] != 0
                ),
                None,
            )
            if swap is None:
                return 0
            data[pivot_index], data[swap] = data[swap], data[pivot_index]
            sign *= -1

        pivot = data[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    data[row][column] * pivot
                    - data[row][pivot_index] * data[pivot_index][column]
                )
                if numerator % previous:
                    raise ArithmeticError("Bareiss division was not exact")
                data[row][column] = numerator // previous
            data[row][pivot_index] = 0
        previous = pivot

    return sign * data[-1][-1]


K23_FIRST_ROWS = (
    3, 4, 7, 8, 10, 11, 12, 13, 14,
    19, 23, 26, 27, 28, 29, 43, 44, 53,
)
K23_SECOND_ROWS = (
    2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18,
    19, 23, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39,
    48, 49, 54, 55, 57, 58, 59, 63, 71, 72, 73, 74, 75, 77,
    78, 98,
)


def k23_minor_certificate() -> dict[str, int]:
    first, second = k23_local_matrices()
    first_minor = [first[row] for row in K23_FIRST_ROWS]
    second_minor = [second[row] for row in K23_SECOND_ROWS]

    first_det = bareiss_determinant(first_minor)
    second_det = bareiss_determinant(second_minor)
    if (first_det, second_det) != (-1, -1):
        raise AssertionError((first_det, second_det))

    return {
        "quadratic_first_koszul_minor_order": 18,
        "quadratic_first_koszul_minor_determinant": first_det,
        "next_koszul_minor_order": 45,
        "next_koszul_minor_determinant": second_det,
    }


def build_payload() -> dict[str, object]:
    representatives = orbit_representatives()
    base_pivots = permanent_pivots()

    rectangle_distribution: Counter[int] = Counter()
    rank_distribution: Counter[int] = Counter()
    multiplicity_rows: dict[str, dict[str, int]] = {}

    for matrix in representatives:
        verify_rectangle_classification(matrix)
        rectangle_distribution[rectangle_count(matrix)] += 1

        edges = edge_multiset(matrix)
        derivative_dimension, prolongation_dimension, term_rank, gain = (
            term_rank_and_quotient_gain(edges, base_pivots)
        )
        if gain != term_rank:
            raise AssertionError((matrix, term_rank, gain))

        rank_distribution[term_rank] += 1
        partition = tuple(
            sorted(
                (
                    multiplicity
                    for row in matrix
                    for multiplicity in row
                    if multiplicity
                ),
                reverse=True,
            )
        )
        key = ",".join(str(value) for value in partition)
        row = multiplicity_rows.setdefault(
            key,
            {
                "orbit_count": 0,
                "degree_three_derivative_dimension": derivative_dimension,
                "degree_four_prolongation_dimension": prolongation_dimension,
                "exact_term_koszul_rank": term_rank,
                "exact_quotient_koszul_gain": gain,
            },
        )
        row["orbit_count"] += 1
        expected = {
            "degree_three_derivative_dimension": derivative_dimension,
            "degree_four_prolongation_dimension": prolongation_dimension,
            "exact_term_koszul_rank": term_rank,
            "exact_quotient_koszul_gain": gain,
        }
        for field, value in expected.items():
            if row[field] != value:
                raise AssertionError((partition, field, row[field], value))

    expected_rectangle_distribution = {0: 151, 1: 15, 3: 1}
    if dict(rectangle_distribution) != expected_rectangle_distribution:
        raise AssertionError(rectangle_distribution)

    expected_rank_distribution = {
        35: 1,
        70: 2,
        105: 2,
        139: 2,
        140: 6,
        210: 8,
        246: 4,
        280: 17,
        352: 25,
        493: 50,
        705: 50,
    }
    if dict(rank_distribution) != expected_rank_distribution:
        raise AssertionError(rank_distribution)

    return {
        "status": "COMPUTATION_REPLAYED",
        "scope": (
            "all degree-six coordinate-monomial Chow terms modulo "
            "row permutations, column permutations, transpose, and factor order"
        ),
        "prime": PRIME,
        "permanent_central_koszul_rank": len(base_pivots),
        "coordinate_monomial_orbits": len(representatives),
        "rectangle_orbit_distribution": {
            str(key): value
            for key, value in sorted(rectangle_distribution.items())
        },
        "term_rank_and_gain_distribution": {
            str(key): value
            for key, value in sorted(rank_distribution.items())
        },
        "multiplicity_partition_certificates": {
            key: multiplicity_rows[key]
            for key in sorted(
                multiplicity_rows,
                key=lambda item: tuple(-int(value) for value in item.split(",")),
            )
        },
        "k23_exact_minor_certificate": k23_minor_certificate(),
        "characteristic_zero_conclusion": (
            "For every coordinate monomial M of degree six, "
            "im K_3(perm_6) intersects im K_3(M) trivially, so the quotient "
            "Koszul gain equals rank K_3(M)."
        ),
        "claim_boundary": (
            "This theorem covers reduced coordinate fixed points only. "
            "It does not prove full quotient gain for arbitrary Chow terms or "
            "for non-strict torus limits with rank loss."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_COORDINATE_MONOMIAL_FULL_GAIN_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
