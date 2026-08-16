#!/usr/bin/env python3
"""Independent replay of fixed-codimension tower tails.

This file imports none of the primary tail audit, the budget-maximizing shadow
DP, or any historical tower implementation.  It computes the complete minimum
shadow table by exact Ferrers family size, inverts that table, rebuilds every
tower row through n=8, and independently enumerates all bipartite graphs for
n=3,4.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def finite_layer_data(n: int, degree: int) -> tuple[list[int], list[int]]:
    layer = sorted(combinations(range(n), degree), key=colex_rank)
    require(
        [colex_rank(value) for value in layer] == list(range(len(layer))),
        (n, degree),
    )

    running: set[tuple[int, ...]] = set()
    profile = [0]
    weights = []
    for upper in layer:
        running.update(combinations(upper, degree - 1))
        profile.append(len(running))
        present = set(upper)
        weights.append(next(value for value in range(n) if value not in present))
    require(sum(weights) == comb(n, degree - 1), weights)
    return profile, weights


def direct_minimum_table(n: int, degree: int) -> list[int]:
    """Compute F_(n,d)(b) by a size-indexed Ferrers dynamic program."""

    profile, weights = finite_layer_data(n, degree)
    width = len(weights)
    upper_ambient = width**2
    infinity = 10**9

    dp = [[infinity] * (upper_ambient + 1) for _ in range(width + 1)]
    dp[width][0] = 0

    for weight in weights:
        new = [[infinity] * (upper_ambient + 1) for _ in range(width + 1)]
        for family_size in range(upper_ambient + 1):
            best_upper = infinity
            for part in range(width, -1, -1):
                if dp[part][family_size] < best_upper:
                    best_upper = dp[part][family_size]
                new_size = family_size + part
                if best_upper < infinity and new_size <= upper_ambient:
                    candidate = best_upper + weight * profile[part]
                    if candidate < new[part][new_size]:
                        new[part][new_size] = candidate
        dp = new

    minimum = [
        min(dp[part][family_size] for part in range(width + 1))
        for family_size in range(upper_ambient + 1)
    ]
    require(minimum[0] == 0, minimum[:2])
    require(
        minimum[-1] == comb(n, degree - 1) ** 2,
        (n, degree, minimum[-1]),
    )
    require(
        all(left <= right for left, right in zip(minimum, minimum[1:])),
        (n, degree),
    )
    return minimum


def inverse_table(minimum: list[int], lower_ambient: int) -> list[int]:
    result = []
    family_size = 0
    for capacity in range(lower_ambient + 1):
        while (
            family_size + 1 < len(minimum)
            and minimum[family_size + 1] <= capacity
        ):
            family_size += 1
        result.append(family_size)
    return result


def independent_tower(
    n: int,
    minima: dict[int, list[int]],
    maximum_terms: int,
) -> dict[int, list[int]]:
    gammas = {
        degree: inverse_table(
            minima[degree],
            comb(n, degree - 1) ** 2,
        )
        for degree in minima
    }

    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    for degree in range(2, n):
        one_term = comb(n, degree)
        ambient = one_term**2
        row = []
        prefix = 0
        for terms in range(maximum_terms + 1):
            direct = min(
                ambient,
                terms * one_term,
                gammas[degree][rows[degree - 1][terms]],
            )
            candidate = direct - terms * one_term
            if terms == 0 or candidate < prefix:
                prefix = candidate
            row.append(min(ambient, terms * one_term + prefix))
        rows[degree] = row
    return rows


def tail_constant(k: int) -> int:
    return max(
        0,
        *(
            comb(a, k - 1) - comb(a - 1, k) - 1
            for a in range(k, 3 * k)
        ),
    )


def ceil_div(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def c4_minimum_edge_profile(n: int) -> list[int]:
    maximum_cycles = comb(n, 2) ** 2
    exact = [10**9] * (maximum_cycles + 1)
    row_mask = (1 << n) - 1

    for graph in range(1 << (n * n)):
        neighborhoods = [
            (graph >> (row * n)) & row_mask
            for row in range(n)
        ]
        cycles = sum(
            comb((neighborhoods[left] & neighborhoods[right]).bit_count(), 2)
            for left in range(n)
            for right in range(left + 1, n)
        )
        exact[cycles] = min(exact[cycles], graph.bit_count())

    profile = [0] * (maximum_cycles + 1)
    running = 10**9
    for cycles in range(maximum_cycles, -1, -1):
        running = min(running, exact[cycles])
        profile[cycles] = running
    return profile


EXPECTED = {
    3: [3, 4],
    4: [4, 7, 8],
    5: [5, 11, 14, 15],
    6: [6, 16, 24, 26, 27],
    7: [7, 22, 39, 46, 48, 49],
    8: [8, 29, 59, 80, 87, 89, 90],
}


def main() -> int:
    require(
        [tail_constant(k) for k in range(2, 9)]
        == [1, 5, 20, 83, 362, 1572, 7513],
        "tail constants",
    )

    top_criteria = {}
    lipschitz_checks = 0
    monotonicity_checks = 0
    tail_checks = 0

    for n in range(3, 9):
        minima = {
            degree: direct_minimum_table(n, degree)
            for degree in range(2, n)
        }
        rows = independent_tower(n, minima, max(EXPECTED[n]))
        thresholds = [
            next(
                terms
                for terms, value in enumerate(rows[degree])
                if value == comb(n, degree) ** 2
            )
            for degree in range(1, n)
        ]
        require(thresholds == EXPECTED[n], (n, thresholds))

        for degree, row in rows.items():
            one_term = comb(n, degree)
            for left, right in zip(row, row[1:]):
                require(0 <= right - left <= one_term, (n, degree, left, right))
                lipschitz_checks += 1

        for left, right in zip(thresholds, thresholds[1:]):
            require(left <= right, (n, thresholds))
            monotonicity_checks += 1

        for k in range(2, n):
            if n < 2 * k:
                continue
            previous_index = n - k - 1
            next_index = n - k
            require(
                thresholds[next_index] - thresholds[previous_index]
                <= tail_constant(k),
                (n, k, thresholds),
            )
            tail_checks += 1

        previous_threshold = thresholds[-2]
        previous_degree = n - 2
        previous_ambient = comb(n, previous_degree) ** 2
        top = max(
            n,
            *(
                retained
                + ceil_div(
                    minima[2][
                        previous_ambient - rows[previous_degree][retained]
                    ],
                    n,
                )
                for retained in range(previous_threshold + 1)
            ),
        )
        require(top == thresholds[-1], (n, top, thresholds))
        top_criteria[n] = top

        if n in (3, 4):
            require(c4_minimum_edge_profile(n) == minima[2], n)

    require(lipschitz_checks == 1151, lipschitz_checks)
    require(monotonicity_checks == 21, monotonicity_checks)
    require(tail_checks == 9, tail_checks)
    require(top_criteria == {3: 4, 4: 8, 5: 15, 6: 27, 7: 49, 8: 90}, top_criteria)

    print("independent_tail_constants=1,5,20,83,362,1572,7513")
    print("independent_lipschitz_checks=1151")
    print("independent_threshold_monotonicity_checks=21")
    print("independent_tail_threshold_checks=9")
    print("independent_bipartite_graphs_enumerated=66048")
    print("independent_top_thresholds=4,8,15,27,49,90")
    print("GENERAL_TOWER_TAIL_CONSTANTS_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
