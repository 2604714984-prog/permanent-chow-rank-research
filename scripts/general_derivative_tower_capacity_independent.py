#!/usr/bin/env python3
"""Independent finite replay of the derivative-tower capacity theorem.

This implementation imports none of the primary audit or exact-shadow helper.
It reconstructs colex order, first lower shadows and first-container weights
from explicit finite sets, uses its own memoized Ferrers recurrence, and then
rebuilds the first three adjacent capacity rows for n=7 and n=8.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def colex_layer(n: int, degree: int) -> tuple[tuple[int, ...], ...]:
    layer = tuple(sorted(combinations(range(n), degree), key=colex_rank))
    require(
        tuple(colex_rank(value) for value in layer)
        == tuple(range(len(layer))),
        (n, degree),
    )
    return layer


class IndependentFerrersShadow:
    def __init__(self, n: int, degree: int) -> None:
        require(degree >= 2, (n, degree))
        lower_degree = degree - 1
        self.layer = colex_layer(n, degree)
        self.width = len(self.layer)

        running: set[tuple[int, ...]] = set()
        profile = [0]
        for upper in self.layer:
            running.update(combinations(upper, lower_degree))
            profile.append(len(running))
        self.profile = tuple(profile)

        first_container: dict[tuple[int, ...], int] = {}
        for lower in combinations(range(n), lower_degree):
            containers = [
                index
                for index, upper in enumerate(self.layer)
                if set(lower).issubset(upper)
            ]
            require(containers, (n, degree, lower))
            first_container[lower] = min(containers)

        weights = [0] * self.width
        for index in first_container.values():
            weights[index] += 1
        self.weights = tuple(weights)
        require(sum(weights) == comb(n, lower_degree), weights)

        infinity = 10**30

        @lru_cache(maxsize=None)
        def solve(index: int, upper: int, remaining: int) -> int:
            if index == self.width:
                return 0 if remaining == 0 else infinity
            rows_left = self.width - index
            if remaining < 0 or remaining > upper * rows_left:
                return infinity

            minimum_part = (remaining + rows_left - 1) // rows_left
            maximum_part = min(upper, remaining, self.width)
            best = infinity
            for part in range(minimum_part, maximum_part + 1):
                tail = remaining - part
                if tail > part * (rows_left - 1):
                    continue
                candidate = (
                    self.weights[index] * self.profile[part]
                    + solve(index + 1, part, tail)
                )
                if candidate < best:
                    best = candidate
            return best

        self._solve = solve

    def minimum(self, family_size: int) -> int:
        return self._solve(0, self.width, family_size)

    def inverse(self, threshold: int) -> int:
        full = self.width**2
        if self.minimum(full) <= threshold:
            return full
        lower = 0
        upper = full
        while lower + 1 < upper:
            midpoint = (lower + upper) // 2
            if self.minimum(midpoint) <= threshold:
                lower = midpoint
            else:
                upper = midpoint
        require(
            self.minimum(lower) <= threshold < self.minimum(upper),
            (threshold, lower, upper),
        )
        return lower


def first_three_rows(n: int) -> dict[int, list[int]]:
    maximum_terms = 5
    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }

    for degree in (2, 3):
        one_term = comb(n, degree)
        shadow = IndependentFerrersShadow(n, degree)
        rows[degree] = [0]
        for terms in range(1, maximum_terms + 1):
            candidates = [
                min(one_term**2, terms * one_term),
                shadow.inverse(rows[degree - 1][terms]),
            ]
            candidates.extend(
                (terms - retained) * one_term + rows[degree][retained]
                for retained in range(1, terms)
            )
            rows[degree].append(min(candidates))
    return rows


def outer_n7_check() -> tuple[int, int, int, int]:
    outer = IndependentFerrersShadow(7, 4)
    cap = outer.inverse(589)
    require(cap == 341, cap)
    require(outer.minimum(341) == 586, outer.minimum(341))
    require(outer.minimum(342) == 590, outer.minimum(342))

    target = 7**2 * comb(7, 3) ** 2 - comb(7, 4) ** 2
    one_term = 7**2 * comb(7, 3) - comb(7, 4)
    residual = -(-(target - 49 * cap) // one_term)
    require(
        (target, one_term, residual) == (58_800, 1_680, 26),
        (target, one_term, residual),
    )
    return cap, target, one_term, residual


def main() -> int:
    rows7 = first_three_rows(7)
    rows8 = first_three_rows(8)

    expected7 = {
        1: [0, 7, 14, 21, 28, 35],
        2: [0, 3, 22, 43, 64, 85],
        3: [0, 0, 4, 17, 40, 64],
    }
    expected8 = {
        1: [0, 8, 16, 24, 32, 40],
        2: [0, 6, 34, 62, 90, 118],
        3: [0, 0, 10, 40, 80, 112],
    }
    require(rows7 == expected7, rows7)
    require(rows8 == expected8, rows8)

    cap, target, one_term, residual = outer_n7_check()
    require(20 + residual == 46, residual)

    print(f"independent_n7_degree2_row={rows7[2]}")
    print(f"independent_n7_degree3_row={rows7[3]}")
    print(f"independent_n8_degree2_row={rows8[2]}")
    print(f"independent_n8_degree3_row={rows8[3]}")
    print(f"independent_n7_outer_cap={cap}")
    print(f"independent_n7_target={target}")
    print(f"independent_n7_one_term={one_term}")
    print("independent_perm7_lower_bound=46")
    print("GENERAL_DERIVATIVE_TOWER_CAPACITY_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
