#!/usr/bin/env python3
"""Exact audit for the three-term row-normal tangent counterexample.

No finite-field inference is used.  The polynomial is represented by a sparse
integer dictionary.  Derivative-space ranks are computed over Q by Fraction
Gaussian elimination.
"""

from fractions import Fraction
from itertools import combinations


VARIABLES = ("a1", "a2", "a3", "a4", "a5", "a6", "p", "q", "z")
W_COUNT = 8


def monomial(*indices: int) -> frozenset[int]:
    return frozenset(indices)


# F = a4 a5 a6 (a2 a3 p + a1 a3 q - a1 a2 p - a1 a2 q).
F = {
    monomial(1, 2, 3, 4, 5, 6): 1,
    monomial(0, 2, 3, 4, 5, 7): 1,
    monomial(0, 1, 3, 4, 5, 6): -1,
    monomial(0, 1, 3, 4, 5, 7): -1,
}


def add_term(poly: dict[frozenset[int], int], support, coefficient: int) -> None:
    support = frozenset(support)
    poly[support] = poly.get(support, 0) + coefficient
    if poly[support] == 0:
        del poly[support]


def multiply_linear_shift(base_support, shifted_index: int, last_support, sign: int):
    """Return sign*(a_shifted+z)*other_a's*last_support."""
    out: dict[frozenset[int], int] = {}
    base_support = set(base_support)
    add_term(out, base_support | {shifted_index} | set(last_support), sign)
    add_term(out, base_support | {8} | set(last_support), sign)
    return out


def add_polys(*polys):
    out: dict[frozenset[int], int] = {}
    for poly in polys:
        for support, coefficient in poly.items():
            add_term(out, support, coefficient)
    return out


def rational_rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    row_count, column_count = len(rows), len(rows[0])
    pivot_row = pivot_column = 0
    while pivot_row < row_count and pivot_column < column_count:
        pivot = next(
            (r for r in range(pivot_row, row_count) if rows[r][pivot_column]),
            None,
        )
        if pivot is None:
            pivot_column += 1
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][pivot_column]
        rows[pivot_row] = [x / scale for x in rows[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or not rows[r][pivot_column]:
                continue
            scale = rows[r][pivot_column]
            rows[r] = [
                x - scale * y for x, y in zip(rows[r], rows[pivot_row])
            ]
        pivot_row += 1
        pivot_column += 1
    return pivot_row


def derivative_rank(poly: dict[frozenset[int], int], order: int) -> int:
    derivative_indices = list(combinations(range(W_COUNT), order))
    output_degree = 6 - order
    output_monomials = list(combinations(range(W_COUNT), output_degree))
    column = {frozenset(support): j for j, support in enumerate(output_monomials)}
    matrix = []
    for derivative in derivative_indices:
        derivative = frozenset(derivative)
        row = [0] * len(output_monomials)
        for support, coefficient in poly.items():
            if derivative <= support:
                row[column[support - derivative]] += coefficient
        matrix.append(row)
    return rational_rank(matrix)


def main() -> None:
    # a_i indices are 0,...,5; p=6, q=7, z=8.
    # T1=(a1+z)a2...a6 p.
    t1 = multiply_linear_shift({1, 2, 3, 4, 5}, 0, {6}, +1)
    # T2=a1(a2+z)a3...a6 q.
    t2 = multiply_linear_shift({0, 2, 3, 4, 5}, 1, {7}, +1)
    # T3=-a1 a2(a3+z)a4...a6(p+q).
    t3p = multiply_linear_shift({0, 1, 3, 4, 5}, 2, {6}, -1)
    t3q = multiply_linear_shift({0, 1, 3, 4, 5}, 2, {7}, -1)
    total = add_polys(t1, t2, t3p, t3q)
    expected = {frozenset(set(support) | {8}): coefficient for support, coefficient in F.items()}
    assert total == expected, (total, expected)

    profile = [derivative_rank(F, order) for order in range(7)]
    assert profile == [1, 8, 23, 32, 23, 8, 1], profile
    assert profile[1] == W_COUNT
    print("COMMON_FACTOR_TANGENT_AUDIT_PASS")
    print("identity=T1+T2+T3=zF")
    print("derivative_profile=" + ",".join(map(str, profile)))
    print("essential_variables=8>6=one_degree6_chow_atom_cap")


if __name__ == "__main__":
    main()
