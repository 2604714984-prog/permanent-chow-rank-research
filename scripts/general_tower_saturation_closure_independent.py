#!/usr/bin/env python3
"""Independent replay of the n=7 tower saturation closure.

This file imports none of the primary saturation, bootstrap, tower or exact
shadow modules. It reconstructs colex order, first shadows, Ferrers minima,
all derivative-tower rows through degree five and 48 terms, then checks the
direct saturation lower bound and the named Koszul bootstrap closure.
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


class IndependentFirstShadow:
    def __init__(self, n: int, degree: int) -> None:
        layer = tuple(sorted(combinations(range(n), degree), key=colex_rank))
        require(
            tuple(colex_rank(value) for value in layer)
            == tuple(range(len(layer))),
            (n, degree),
        )
        self.width = len(layer)

        running: set[tuple[int, ...]] = set()
        profile = [0]
        for upper in layer:
            running.update(combinations(upper, degree - 1))
            profile.append(len(running))
        self.profile = tuple(profile)

        weights = []
        for upper in layer:
            present = set(upper)
            least_missing = next(
                value for value in range(n) if value not in present
            )
            weights.append(least_missing)
        self.weights = tuple(weights)
        require(sum(weights) == comb(n, degree - 1), weights)

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


def tower_rows(n: int, maximum_degree: int, maximum_terms: int) -> dict[int, list[int]]:
    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    shadows: dict[int, IndependentFirstShadow] = {}
    for degree in range(2, maximum_degree + 1):
        one_term = comb(n, degree)
        ambient = one_term**2
        shadows[degree] = IndependentFirstShadow(n, degree)
        rows[degree] = [0]
        for terms in range(1, maximum_terms + 1):
            candidates = [
                min(ambient, terms * one_term),
                shadows[degree].inverse(rows[degree - 1][terms]),
            ]
            candidates.extend(
                (terms - retained) * one_term + rows[degree][retained]
                for retained in range(1, terms)
            )
            rows[degree].append(min(candidates))
    return rows


def first_koszul(n: int, output_degree: int) -> tuple[int, int, int]:
    target = (
        n * n * comb(n, output_degree) ** 2
        - comb(n, output_degree + 1) ** 2
    )
    one_term = (
        n * n * comb(n, output_degree)
        - comb(n, output_degree + 1)
    )
    return target, one_term, -(-target // one_term)


def koszul_step(n: int, rows: dict[int, list[int]], lower_bound: int) -> int:
    best = lower_bound
    for output_degree in range(2, n - 1):
        complement = n - output_degree
        target, one_term, _ = first_koszul(n, output_degree)
        for fixed_terms in range(1, lower_bound + 1):
            numerator = target - n * n * rows[complement][fixed_terms]
            residual = 0 if numerator <= 0 else -(-numerator // one_term)
            best = max(best, fixed_terms + residual)
    return best


def saturation_threshold(row: list[int], ambient: int) -> int:
    require(all(a <= b <= ambient for a, b in zip(row, row[1:])), row)
    return next(index for index, value in enumerate(row) if value == ambient)


def main() -> int:
    n = 7
    rows = tower_rows(n, 5, 48)
    thresholds = {
        degree: saturation_threshold(row, comb(n, degree) ** 2)
        for degree, row in rows.items()
    }
    direct = max(thresholds.values())

    require(rows[5][46:49] == [405, 426, 441], rows[5][44:49])
    require(thresholds[5] == 48, thresholds)
    require(direct == 48, (direct, thresholds))

    base = max(first_koszul(n, degree)[2] for degree in range(2, n - 1))
    require(base == 36, base)
    koszul_36 = koszul_step(n, rows, 36)
    koszul_48 = koszul_step(n, rows, 48)
    require((koszul_36, koszul_48) == (46, 48), (koszul_36, koszul_48))

    enhanced_36 = max(base, direct, koszul_36)
    enhanced_48 = max(enhanced_36, direct, koszul_48)
    require((enhanced_36, enhanced_48) == (48, 48), (
        enhanced_36,
        enhanced_48,
    ))

    print(f"independent_tower_thresholds={thresholds}")
    print("independent_B_7_5_46=405")
    print("independent_B_7_5_47=426")
    print("independent_B_7_5_48=441")
    print("independent_perm7_lower_bound=48")
    print("independent_n7_scalar_tower_closure=48")
    print("GENERAL_TOWER_SATURATION_CLOSURE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
