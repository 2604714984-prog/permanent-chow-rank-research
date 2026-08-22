#!/usr/bin/env python3
"""Independent exact audit for the N=50 rank-one support restriction."""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb


SURPLUS = (0, 22, 29, 26, 17, 14, 7, 0)
EXPECTED = {
    1: (20, 15),
    2: (20, 15),
    3: (26, 19),
    4: (26, 19),
    5: (30, 21),
    6: (30, 21),
    7: (35, 21),
}


def boolean_rank_formula(support_size: int, degree: int) -> int:
    """Rank of sum_{i <= s} partial_i from B_{7,degree} to B_{7,degree-1}."""
    total = 0
    for outside_degree in range(8 - support_size):
        inside_degree = degree - outside_degree
        if not 0 <= inside_degree <= support_size:
            continue
        total += comb(7 - support_size, outside_degree) * min(
            comb(support_size, inside_degree),
            comb(support_size, inside_degree - 1)
            if inside_degree >= 1
            else 0,
        )
    return total


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    a = [[entry % prime for entry in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][col], prime - 2, prime)
        a[pivot_row] = [(inverse * x) % prime for x in a[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not a[row][col]:
                continue
            scalar = a[row][col]
            a[row] = [
                (x - scalar * y) % prime
                for x, y in zip(a[row], a[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def boolean_matrix(support_size: int, degree: int) -> list[list[int]]:
    source = list(combinations(range(7), degree))
    target = list(combinations(range(7), degree - 1))
    target_index = {monomial: i for i, monomial in enumerate(target)}
    matrix = [[0] * len(source) for _ in target]
    for col, monomial in enumerate(source):
        for factor in monomial:
            if factor < support_size:
                image = tuple(x for x in monomial if x != factor)
                matrix[target_index[image]][col] += 1
    return matrix


def audit_profile() -> None:
    # With k positive increments, deficiency is 7k-49.  For k >= 9,
    # every deficiency unit costs at least 11/3, already exceeding 35.
    ratios = [Fraction(SURPLUS[d], 7 - d) for d in range(1, 7)]
    assert min(ratios) == Fraction(11, 3)
    assert 14 * min(ratios) > 35

    admissible = []
    for profile in combinations_with_replacement(range(1, 8), 8):
        if sum(profile) == 49 and sum(SURPLUS[d] for d in profile) <= 35:
            admissible.append(profile)
    assert admissible == [(1, 6, 7, 7, 7, 7, 7, 7)]


def audit_boolean_ranks() -> None:
    for support_size, expected in EXPECTED.items():
        formula_pair = (
            boolean_rank_formula(support_size, 4),
            boolean_rank_formula(support_size, 3),
        )
        assert formula_pair == expected
        for prime in (1_000_003, 1_000_033):
            explicit_pair = (
                rank_mod(boolean_matrix(support_size, 4), prime),
                rank_mod(boolean_matrix(support_size, 3), prime),
            )
            assert explicit_pair == expected

    # Quotienting the negative target by an at-most-three-dimensional
    # intersection gives the four support-range surplus floors below.
    floors = {
        s: EXPECTED[s][0] + max(0, EXPECTED[s][1] - 3) - 10
        for s in EXPECTED
    }
    assert tuple(floors[s] for s in range(1, 8)) == (22, 22, 32, 32, 38, 38, 43)
    assert floors[3] + SURPLUS[6] > 35


if __name__ == "__main__":
    audit_profile()
    audit_boolean_ranks()
    print("N50_RANK_ONE_SUPPORT_AUDIT_PASS")
