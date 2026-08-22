#!/usr/bin/env python3
"""Exact centroid audit for F = a*y*z + b*x*z + c*x*y.

The cubic has ordinary Chow rank three and border Chow rank at most two.
The load-bearing finite calculation is that its trilinear centroid is
two-dimensional, spanned by I and a square-zero map N, so it has no
nontrivial idempotent and hence no 3+3 direct-sum decomposition.
"""

from fractions import Fraction
from itertools import permutations, product


N_VARS = 6
TRIPLES = [(3, 1, 2), (4, 0, 2), (5, 0, 1)]  # (a,y,z), (b,x,z), (c,x,y)


def centroid_matrix() -> list[list[Fraction]]:
    tensor = {
        permutation: 1
        for triple in TRIPLES
        for permutation in set(permutations(triple))
    }
    rows: list[list[Fraction]] = []
    for i, j, k in product(range(N_VARS), repeat=3):
        for slot in (1, 2):
            row = [Fraction(0) for _ in range(N_VARS**2)]
            for q in range(N_VARS):
                row[q * N_VARS + i] += tensor.get((q, j, k), 0)
                if slot == 1:
                    row[q * N_VARS + j] -= tensor.get((i, q, k), 0)
                else:
                    row[q * N_VARS + k] -= tensor.get((i, j, q), 0)
            if any(row):
                rows.append(row)
    return rows


def rref(rows: list[list[Fraction]]) -> tuple[int, list[int], list[list[Fraction]]]:
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    col_count = len(matrix[0])
    pivot_row = 0
    pivots: list[int] = []
    for col in range(col_count):
        selected = next(
            (row for row in range(pivot_row, row_count) if matrix[row][col]),
            None,
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not matrix[row][col]:
                continue
            scale = matrix[row][col]
            matrix[row] = [
                entry - scale * pivot
                for entry, pivot in zip(matrix[row], matrix[pivot_row])
            ]
        pivots.append(col)
        pivot_row += 1
    return pivot_row, pivots, matrix


def nullspace_basis(
    rank: int, pivots: list[int], matrix: list[list[Fraction]]
) -> list[list[Fraction]]:
    free = [col for col in range(N_VARS**2) if col not in pivots]
    basis: list[list[Fraction]] = []
    for free_col in free:
        vector = [Fraction(0) for _ in range(N_VARS**2)]
        vector[free_col] = 1
        for row, pivot_col in enumerate(pivots[:rank]):
            vector[pivot_col] = -matrix[row][free_col]
        basis.append(vector)
    return basis


def identity() -> list[Fraction]:
    return [
        Fraction(int(row == col))
        for row in range(N_VARS)
        for col in range(N_VARS)
    ]


def nilpotent() -> list[Fraction]:
    # N(x)=a, N(y)=b, N(z)=c, and N(a)=N(b)=N(c)=0.
    return [
        Fraction(int(row == col + 3 and col < 3))
        for row in range(N_VARS)
        for col in range(N_VARS)
    ]


def main() -> None:
    equations = centroid_matrix()
    rank, pivots, reduced = rref(equations)
    basis = nullspace_basis(rank, pivots, reduced)
    assert len(equations) == 276
    assert rank == 34
    assert len(basis) == 2
    expected = {tuple(identity()), tuple(nilpotent())}
    assert {tuple(vector) for vector in basis} == expected
    print("PASS tangent-cubic centroid: 276 equations, rank 34, centroid = <I,N>, N^2=0")


if __name__ == "__main__":
    main()
