#!/usr/bin/env python3
"""Independent replay of the row-column projection denominator witness.

This file does not construct Johnson primitive idempotents.  It obtains every
Johnson constituent as the nullspace of one adjacency eigenvalue, constructs a
nowhere-zero vector in that stable subspace, and verifies that pointwise
multiplication by the vector is injective on every other constituent.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


PRIME = 1_000_033


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def matrix_rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next((index for index in range(rank, row_count) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        pivot_row = rows[rank]
        for index in range(row_count):
            if index == rank:
                continue
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    (value - coefficient * pivot_value) % prime
                    for value, pivot_value in zip(rows[index], pivot_row, strict=True)
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def nullspace_mod(matrix: list[list[int]], prime: int = PRIME) -> list[list[int]]:
    rows = [[value % prime for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next((index for index in range(pivot_row, row_count) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        rows[pivot_row] = [(value * inverse) % prime for value in rows[pivot_row]]
        for index in range(row_count):
            if index == pivot_row:
                continue
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    (value - coefficient * pivot_value) % prime
                    for value, pivot_value in zip(rows[index], rows[pivot_row], strict=True)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(column_count) if column not in pivot_set]
    basis = []
    for free in free_columns:
        vector = [0] * column_count
        vector[free] = 1
        for row_index, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = (-rows[row_index][free]) % prime
        basis.append(vector)
    return basis


def johnson_adjacency(n: int, m: int) -> list[list[int]]:
    subsets = tuple(combinations(range(n), m))
    sets = tuple(set(value) for value in subsets)
    size = len(subsets)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if len(sets[i] & sets[j]) == m - 1:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


def nowhere_zero_vector(basis: list[list[int]], prime: int = PRIME) -> list[int]:
    require(basis, "empty stable constituent")
    length = len(basis[0])
    vector = [0] * length
    for coordinate in range(length):
        if vector[coordinate]:
            continue
        witness = next((row for row in basis if row[coordinate]), None)
        require(witness is not None, ("zero evaluation", coordinate))
        forbidden = {0}
        for current, value in zip(vector, witness, strict=True):
            if current and value:
                forbidden.add((-current * pow(value, prime - 2, prime)) % prime)
        coefficient = next(value for value in range(1, length + 3) if value not in forbidden)
        vector = [
            (current + coefficient * value) % prime
            for current, value in zip(vector, witness, strict=True)
        ]
    require(all(vector), "nowhere-zero construction failed")
    return vector


def main() -> int:
    eigenspace_checks = 0
    nowhere_zero_checks = 0
    multiplication_injection_checks = 0
    route_ceiling_checks = 0

    for n in range(3, 9):
        for m in range(1, n // 2 + 1):
            adjacency = johnson_adjacency(n, m)
            size = len(adjacency)
            eigenvalues = [(m - i) * (n - m - i) - i for i in range(m + 1)]
            dimensions = [comb(n, i) - (comb(n, i - 1) if i else 0) for i in range(m + 1)]
            bases = []
            witnesses = []
            for theta, expected_dimension in zip(eigenvalues, dimensions, strict=True):
                shifted = [row[:] for row in adjacency]
                for diagonal in range(size):
                    shifted[diagonal][diagonal] = (shifted[diagonal][diagonal] - theta) % PRIME
                basis = nullspace_mod(shifted)
                require(len(basis) == expected_dimension, (n, m, theta, len(basis), expected_dimension))
                bases.append(basis)
                eigenspace_checks += 1
                witness = nowhere_zero_vector(basis)
                witnesses.append(witness)
                nowhere_zero_checks += 1

            for i, (basis_i, witness_i) in enumerate(zip(bases, witnesses, strict=True)):
                for j, (basis_j, witness_j) in enumerate(zip(bases, witnesses, strict=True)):
                    products_j = [
                        [(a * b) % PRIME for a, b in zip(witness_i, vector, strict=True)]
                        for vector in basis_j
                    ]
                    require(matrix_rank_mod(products_j) == len(basis_j), (n, m, i, j, "right injection"))
                    multiplication_injection_checks += 1

                    products_i = [
                        [(a * b) % PRIME for a, b in zip(witness_j, vector, strict=True)]
                        for vector in basis_i
                    ]
                    require(matrix_rank_mod(products_i) == len(basis_i), (n, m, i, j, "left injection"))
                    multiplication_injection_checks += 1

                    denominator = max(len(basis_i), len(basis_j))
                    numerator = len(basis_i) * len(basis_j)
                    require(-(-numerator // denominator) <= size, (n, m, i, j))
                    route_ceiling_checks += 1

    print(f"independent_eigenspace_checks={eigenspace_checks}")
    print(f"independent_nowhere_zero_checks={nowhere_zero_checks}")
    print(f"independent_multiplication_injection_checks={multiplication_injection_checks}")
    print(f"independent_route_ceiling_checks={route_ceiling_checks}")
    print("GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
