#!/usr/bin/env python3
"""Independent finite replay for factor-span zero blocks.

This file intentionally imports none of the primary audit.  It reconstructs
the order-(m-1) derivatives of an m x m permanent from explicit permutations
and independently recomputes the central and pair exactness tables.
"""

from __future__ import annotations

from itertools import permutations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def derivative_linear_support_of_permanent(m: int) -> set[tuple[int, int]]:
    """Variables appearing after all order-(m-1) derivatives of perm_m."""

    require(m >= 1, m)
    variables: set[tuple[int, int]] = set()
    rows = tuple(range(m))
    for sigma in permutations(rows):
        matching = tuple((row, sigma[row]) for row in rows)
        for survivor in matching:
            variables.add(survivor)
    return variables


def central_degree(n: int) -> int:
    return (n + 1) // 2


def pair_rows(n: int, m: int) -> list[tuple[int, int, bool, int]]:
    rows = []
    for intersection in range(n + 1):
        union = 2 * n - intersection
        exact = union < m * m
        literal_cap = comb(intersection, m) if intersection >= m else 0
        rows.append((intersection, union, exact, literal_cap))
    return rows


def main() -> int:
    for m in range(1, 8):
        support = derivative_linear_support_of_permanent(m)
        require(len(support) == m * m, (m, len(support)))

    central = []
    for n in range(3, 21):
        m = central_degree(n)
        same_span_zero = n < m * m
        universal_pair_exact = 2 * n < m * m
        central.append((n, m, same_span_zero, universal_pair_exact))

    require(
        [n for n, _, same, _ in central if same]
        == [3] + list(range(5, 21)),
        central,
    )
    require(
        [n for n, _, _, pair in central if pair]
        == [7] + list(range(9, 21)),
        central,
    )

    n8 = pair_rows(8, 4)
    require([row[2] for row in n8] == [False] + [True] * 8, n8)
    require([row[3] for row in n8[:4]] == [0, 0, 0, 0], n8)

    n6 = pair_rows(6, 3)
    require([row[2] for row in n6] == [False] * 4 + [True] * 3, n6)

    n7 = pair_rows(7, 4)
    require(all(row[2] for row in n7), n7)

    print("independent_permanent_linear_shadow_m1_to_m7=PASS")
    print("independent_same_span_zero_n=3,5..20")
    print("independent_universal_pair_exact_n=7,9..20")
    print("independent_n8_positive_intersection_exact=PASS")
    print("GENERAL_FACTOR_SPAN_ZERO_BLOCKS_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
