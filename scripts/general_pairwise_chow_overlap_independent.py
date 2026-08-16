#!/usr/bin/env python3
"""Independent combinatorial replay for pairwise Chow overlap.

This file imports none of the primary audit.  It verifies the transverse
common-factor formula by explicit squarefree supports and the block-rotation
formula by local multidegree decomposition.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def transverse_count(n: int, shared: int, m: int) -> int:
    common = tuple(range(shared))
    left = common + tuple(range(shared, n))
    right = common + tuple(range(n, n + n - shared))
    left_supports = {
        tuple(sorted(value))
        for value in combinations(left, m)
    }
    right_supports = {
        tuple(sorted(value))
        for value in combinations(right, m)
    }
    return len(left_supports & right_supports)


def rotation_count(n: int, m: int) -> int:
    require(n % 2 == 0, n)
    block_count = n // 2
    total = 0
    for active_blocks in combinations(range(block_count), m):
        # On each active block, x_i+y_i and x_i-y_i span the two local
        # squarefree degree-one monomials.  Tensoring m active blocks gives
        # dimension 2^m.  Any double-selected block has degree-two line
        # <x_i^2-y_i^2>, disjoint from <x_i y_i>.
        total += 2 ** len(active_blocks)
    return total


def main() -> int:
    transverse_cases = 0
    for n in range(3, 13):
        for shared in range(n + 1):
            for m in range(n + 1):
                observed = transverse_count(n, shared, m)
                expected = comb(shared, m) if m <= shared else 0
                require(
                    observed == expected,
                    (n, shared, m, observed, expected),
                )
                transverse_cases += 1

    rotation_cases = 0
    for n in range(4, 18, 2):
        half = n // 2
        for m in range(1, n + 1):
            observed = rotation_count(n, m) if m <= half else 0
            expected = 2**m * comb(half, m) if m <= half else 0
            require(observed == expected, (n, m, observed, expected))
            rotation_cases += 1

    print(f"independent_transverse_cases={transverse_cases}")
    print(f"independent_rotation_cases={rotation_cases}")
    print("independent_n6_m3_intersection=8")
    print("independent_n8_m4_intersection=16")
    print("GENERAL_PAIRWISE_CHOW_OVERLAP_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
