#!/usr/bin/env python3
"""Independent pure-Python replay of the recursive zero-seeded tower for n<=8.

This implementation imports none of the primary C++ engine, the primary
driver, PR #51 helpers or PR #80 helpers. It reconstructs colex order,
Ferrers inverse shadows, the parent direct seeds, recursive zero closure and
both baseline/seeded prefix envelopes.
"""

from __future__ import annotations

import argparse
from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


class IndependentInverseShadow:
    def __init__(self, n: int, degree: int) -> None:
        layer = tuple(sorted(combinations(range(n), degree), key=colex_rank))
        require(
            tuple(colex_rank(value) for value in layer)
            == tuple(range(len(layer))),
            (n, degree),
        )
        width = len(layer)
        lower_width = comb(n, degree - 1)
        maximum_cost = lower_width**2

        running: set[tuple[int, ...]] = set()
        profile = [0]
        weights = []
        for upper in layer:
            running.update(combinations(upper, degree - 1))
            profile.append(len(running))
            present = set(upper)
            weights.append(next(value for value in range(n) if value not in present))
        require(len(running) == lower_width, (n, degree, len(running)))
        require(sum(weights) == lower_width, (n, degree, sum(weights)))

        negative = -10**9
        costs = maximum_cost + 1
        dp = [[negative] * costs for _ in range(width + 1)]
        dp[width][0] = 0
        reachable = 0

        for weight in weights:
            if weight == 0:
                for upper, row in enumerate(dp):
                    if upper == 0:
                        continue
                    for cost in range(reachable + 1):
                        if row[cost] > negative // 2:
                            row[cost] += upper
                continue

            next_dp = [[negative] * costs for _ in range(width + 1)]
            row_costs = [weight * value for value in profile]
            for cost in range(reachable + 1):
                suffix_best = negative
                for part in range(width, -1, -1):
                    suffix_best = max(suffix_best, dp[part][cost])
                    next_cost = cost + row_costs[part]
                    if suffix_best > negative // 2 and next_cost < costs:
                        next_dp[part][next_cost] = max(
                            next_dp[part][next_cost],
                            suffix_best + part,
                        )
            dp = next_dp
            reachable = min(maximum_cost, reachable + weight * lower_width)

        gamma = []
        prefix = 0
        for cost in range(costs):
            exact = max(row[cost] for row in dp)
            prefix = max(prefix, exact)
            gamma.append(prefix)
        require(gamma[-1] == width**2, (n, degree, gamma[-1]))
        self.gamma = gamma


def strict_increment(n: int, degree: int) -> int:
    return (degree * degree - 1) // n


def parent_direct_seed(n: int, degree: int) -> int:
    value = strict_increment(n, degree)
    if degree >= 3:
        first_excess = (degree * degree + 1) // n
        if first_excess >= 2:
            value = max(value, first_excess)
    if degree == 4:
        post = (degree * degree + degree + 3) // n
        if post >= 2:
            value = max(value, post)
    if degree >= 5:
        post = (degree * degree + degree + 4) // n
        if post >= 2:
            value = max(value, post)
    return value


def zero_closure(n: int) -> list[int]:
    values = [0] * (n + 1)
    for degree in range(2, n + 1):
        values[degree] = max(
            parent_direct_seed(n, degree),
            values[degree - 1] + strict_increment(n, degree),
        )
    return values


def build_both_towers(n: int):
    maximum_terms = 2 ** (n - 1)
    baseline = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    seeded = {1: baseline[1][:]}
    base_thresholds = [n]
    seeded_thresholds = [n]
    zero = zero_closure(n)
    changed = 0
    maximum_reduction = 0

    for degree in range(2, n):
        inverse = IndependentInverseShadow(n, degree)
        one_term = comb(n, degree)
        ambient = one_term**2
        base_row = [0]
        seed_row = [0]
        base_prefix = 0
        seed_prefix = 0

        for terms in range(1, maximum_terms + 1):
            base_direct = min(
                ambient,
                terms * one_term,
                inverse.gamma[baseline[degree - 1][terms]],
            )
            if terms <= zero[degree]:
                seed_direct = 0
            else:
                seed_direct = min(
                    ambient,
                    terms * one_term,
                    inverse.gamma[seeded[degree - 1][terms]],
                )

            base_prefix = min(base_prefix, base_direct - terms * one_term)
            seed_prefix = min(seed_prefix, seed_direct - terms * one_term)
            base_value = terms * one_term + base_prefix
            seed_value = terms * one_term + seed_prefix
            require(seed_value <= base_value, (n, degree, terms))
            base_row.append(base_value)
            seed_row.append(seed_value)
            if seed_value != base_value:
                changed += 1
                maximum_reduction = max(
                    maximum_reduction,
                    base_value - seed_value,
                )

        baseline[degree] = base_row
        seeded[degree] = seed_row
        base_thresholds.append(base_row.index(ambient))
        seeded_thresholds.append(seed_row.index(ambient))

    return zero, base_thresholds, seeded_thresholds, changed, maximum_reduction


def run(maximum_n: int) -> int:
    require(3 <= maximum_n <= 8, maximum_n)
    expected_thresholds = {
        3: [3, 4],
        4: [4, 7, 8],
        5: [5, 11, 14, 15],
        6: [6, 16, 24, 26, 27],
        7: [7, 22, 39, 46, 48, 49],
        8: [8, 29, 59, 80, 87, 89, 90],
    }
    expected_zero = {
        3: [0, 1, 3],
        4: [0, 0, 2, 5],
        5: [0, 0, 2, 5, 9],
        6: [0, 0, 1, 3, 7, 12],
        7: [0, 0, 1, 3, 6, 11, 17],
        8: [0, 0, 1, 2, 5, 9, 15, 22],
    }
    expected_changes = {
        3: (0, 0),
        4: (0, 0),
        5: (2, 1),
        6: (0, 0),
        7: (1, 1),
        8: (1, 1),
    }

    total_changed = 0
    for n in range(3, maximum_n + 1):
        zero, base, seeded, changed, maximum = build_both_towers(n)
        require(base == expected_thresholds[n], (n, base))
        require(seeded == base, (n, seeded, base))
        require(zero[1:] == expected_zero[n], (n, zero))
        require((changed, maximum) == expected_changes[n], (n, changed, maximum))
        total_changed += changed

    print(f"independent_n_range=3..{maximum_n}")
    print(f"independent_changed_capacity_cells={total_changed}")
    print("independent_thresholds_unchanged=true")
    print("GENERAL_RECURSIVE_ZERO_SEEDED_TOWER_INDEPENDENT_PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-n", type=int, default=8)
    args = parser.parse_args()
    return run(args.maximum_n)


if __name__ == "__main__":
    raise SystemExit(main())
