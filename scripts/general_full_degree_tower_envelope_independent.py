#!/usr/bin/env python3
"""Independent pure-Python replay of full-degree tower saturation for n<=8.

This file imports none of the primary audit, the C++ engine, the canonical
exact-shadow implementation, or the previous tower scripts.  It reconstructs
colex order, one-dimensional lower shadows, first-container weights, the dual
Ferrers budget dynamic program, and the prefix min-plus tower envelope.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


class IndependentInverseShadow:
    def __init__(self, n: int, degree: int) -> None:
        layer = tuple(
            sorted(combinations(range(n), degree), key=colex_rank)
        )
        require(
            tuple(colex_rank(value) for value in layer)
            == tuple(range(len(layer))),
            (n, degree),
        )
        self.width = len(layer)
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
        dp = [[negative] * costs for _ in range(self.width + 1)]
        dp[self.width][0] = 0

        for weight in weights:
            if weight == 0:
                for upper, row in enumerate(dp):
                    if upper == 0:
                        continue
                    for cost, value in enumerate(row):
                        if value > negative // 2:
                            row[cost] = value + upper
                continue

            next_dp = [[negative] * costs for _ in range(self.width + 1)]
            row_costs = [weight * value for value in profile]
            for cost in range(costs):
                suffix_best = negative
                for part in range(self.width, -1, -1):
                    suffix_best = max(suffix_best, dp[part][cost])
                    next_cost = cost + row_costs[part]
                    if suffix_best > negative // 2 and next_cost < costs:
                        next_dp[part][next_cost] = max(
                            next_dp[part][next_cost],
                            suffix_best + part,
                        )
            dp = next_dp

        gamma = []
        prefix = 0
        for cost in range(costs):
            exact = max(row[cost] for row in dp)
            prefix = max(prefix, exact)
            gamma.append(prefix)
        require(gamma[-1] == self.width**2, (n, degree, gamma[-1]))
        self.gamma = gamma


def independent_tower(n: int) -> tuple[dict[int, list[int]], list[int]]:
    maximum_terms = 2 ** (n - 1)
    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    thresholds = [n]

    for degree in range(2, n):
        inverse = IndependentInverseShadow(n, degree)
        one_term = comb(n, degree)
        ambient = one_term**2
        row = [0]
        prefix_envelope = 0
        for terms in range(1, maximum_terms + 1):
            direct = min(
                ambient,
                terms * one_term,
                inverse.gamma[rows[degree - 1][terms]],
            )
            prefix_envelope = min(
                prefix_envelope,
                direct - terms * one_term,
            )
            row.append(terms * one_term + prefix_envelope)
        rows[degree] = row
        thresholds.append(row.index(ambient))
    return rows, thresholds


def main() -> int:
    expected = {
        3: [3, 4],
        4: [4, 7, 8],
        5: [5, 11, 14, 15],
        6: [6, 16, 24, 26, 27],
        7: [7, 22, 39, 46, 48, 49],
        8: [8, 29, 59, 80, 87, 89, 90],
    }
    observed = {}
    for n in range(3, 9):
        rows, thresholds = independent_tower(n)
        require(thresholds == expected[n], (n, thresholds))
        observed[n] = thresholds

        # Explicit new full-degree boundaries.
        if n == 7:
            require((rows[6][48], rows[6][49]) == (44, 49), rows[6][46:50])
        if n == 8:
            require((rows[7][89], rows[7][90]) == (60, 64), rows[7][87:91])

    print(f"independent_thresholds={observed}")
    print("independent_perm7_lower_bound=49")
    print("independent_perm8_lower_bound=90")
    print("GENERAL_FULL_DEGREE_TOWER_ENVELOPE_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
