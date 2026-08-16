#!/usr/bin/env python3
"""Independent replay of the cross-degree block projection numbers.

This implementation imports none of the primary product-shadow code.  It
reconstructs colex layers, lower shadows and first-container weights from
explicit finite sets, then solves the Ferrers optimization by a separate exact
integer recurrence.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_key(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


class IndependentShadow:
    def __init__(self, n: int, m: int) -> None:
        layer = tuple(sorted(combinations(range(n), m), key=colex_key))
        require(
            tuple(colex_key(value) for value in layer)
            == tuple(range(len(layer))),
            (n, m),
        )
        width = len(layer)

        running: set[tuple[int, ...]] = set()
        profile = [0]
        for subset in layer:
            for position in range(m):
                running.add(subset[:position] + subset[position + 1 :])
            profile.append(len(running))

        weights = [0] * width
        for lower in combinations(range(n), m - 1):
            containing = [
                index
                for index, upper in enumerate(layer)
                if set(lower).issubset(upper)
            ]
            weights[min(containing)] += 1
        require(sum(weights) == comb(n, m - 1), (n, m, weights))

        infinity = 10**30

        @lru_cache(maxsize=None)
        def solve(index: int, upper: int, remaining: int) -> int:
            if index == width:
                return 0 if remaining == 0 else infinity
            rows_left = width - index
            if remaining < 0 or remaining > upper * rows_left:
                return infinity

            minimum_part = (remaining + rows_left - 1) // rows_left
            maximum_part = min(upper, remaining, width)
            best = infinity
            for value in range(minimum_part, maximum_part + 1):
                tail = remaining - value
                if tail > value * (rows_left - 1):
                    continue
                candidate = (
                    weights[index] * profile[value]
                    + solve(index + 1, value, tail)
                )
                if candidate < best:
                    best = candidate
            return best

        self.width = width
        self._solve = solve

    def minimum(self, family_size: int) -> int:
        return self._solve(0, self.width, family_size)


def verify_pair(
    n: int,
    m: int,
    cap_size: int,
    first_bad_size: int,
    expected_cap_shadow: int,
    expected_first_bad_shadow: int,
) -> None:
    shadow = IndependentShadow(n, m)
    cap_value = shadow.minimum(cap_size)
    first_bad_value = shadow.minimum(first_bad_size)
    require(
        (cap_value, first_bad_value)
        == (expected_cap_shadow, expected_first_bad_shadow),
        (n, m, cap_size, first_bad_size, cap_value, first_bad_value),
    )
    print(
        f"independent_n{n}_m{m}_F({cap_size})={cap_value} "
        f"F({first_bad_size})={first_bad_value}"
    )


def main() -> int:
    verify_pair(7, 2, 3, 4, 6, 8)
    verify_pair(7, 3, 41, 42, 66, 69)
    verify_pair(7, 4, 263, 264, 494, 497)
    verify_pair(8, 2, 6, 7, 8, 9)
    verify_pair(8, 3, 112, 113, 118, 120)
    verify_pair(8, 4, 560, 561, 784, 793)

    target7 = 7**2 * comb(7, 3) ** 2 - comb(7, 4) ** 2
    one_term7 = 7**2 * comb(7, 3) - comb(7, 4)
    residual7 = -(-(target7 - 7**2 * 263) // one_term7)
    require(
        (target7, one_term7, residual7, 17 + residual7)
        == (58_800, 1_680, 28, 45),
        (target7, one_term7, residual7),
    )

    target8 = 8**2 * comb(8, 4) ** 2 - comb(8, 5) ** 2
    one_term8 = 8**2 * comb(8, 4) - comb(8, 5)
    residual8 = -(-(target8 - 8**2 * 560) // one_term8)
    require(
        (target8, one_term8, residual8, 17 + residual8)
        == (310_464, 4_424, 63, 80),
        (target8, one_term8, residual8),
    )

    print("independent_perm7_lower_bound=45")
    print("independent_perm8_lower_bound=80")
    print("GENERAL_CROSS_DEGREE_BLOCK_PROJECTION_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
