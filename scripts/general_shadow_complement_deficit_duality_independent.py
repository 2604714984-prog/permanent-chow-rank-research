#!/usr/bin/env python3
"""Independent replay of shadow-complement and deficit duality.

This implementation imports none of the primary audit or historical shadow
modules.  Unlike the primary budget-maximization DP, it computes the complete
minimum-shadow function directly: the state is indexed by the exact Ferrers
family size and stores the minimum objective.  It then inverts that table,
checks complement duality, and reconstructs both forms of the derivative-tower
recurrence through n=8.
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
    """Compute F_(n,d)(b) directly by a size-indexed Ferrers DP."""

    profile, weights = finite_layer_data(n, degree)
    width = len(weights)
    upper_ambient = width**2
    infinity = 10**9

    # dp[u][b] is the minimum objective after the processed rows when the
    # latest partition part is u and the exact family size is b.
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
    gamma = []
    family_size = 0
    for capacity in range(lower_ambient + 1):
        while (
            family_size + 1 < len(minimum)
            and minimum[family_size + 1] <= capacity
        ):
            family_size += 1
        gamma.append(family_size)
    return gamma


EXPECTED_THRESHOLDS = {
    "3": [3, 4],
    "4": [4, 7, 8],
    "5": [5, 11, 14, 15],
    "6": [6, 16, 24, 26, 27],
    "7": [7, 22, 39, 46, 48, 49],
    "8": [8, 29, 59, 80, 87, 89, 90],
}


def direct_rows(
    n: int,
    minima: dict[int, list[int]],
    gammas: dict[int, list[int]],
    maximum_terms: int,
) -> dict[int, list[int]]:
    del minima
    rows = {1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]}
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


def transported_rows(
    n: int,
    minima: dict[int, list[int]],
    maximum_terms: int,
) -> dict[int, list[int]]:
    deficits = {
        1: [n * n - min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    capacities = {1: [n * n - value for value in deficits[1]]}
    for degree in range(2, n):
        one_term = comb(n, degree)
        ambient = one_term**2
        complementary_degree = n - degree + 1
        running = -10**18
        row_deficits = []
        for terms in range(maximum_terms + 1):
            direct_deficit = max(
                0,
                ambient - terms * one_term,
                minima[complementary_degree][deficits[degree - 1][terms]],
            )
            running = max(running, direct_deficit + terms * one_term)
            row_deficits.append(max(0, running - terms * one_term))
        deficits[degree] = row_deficits
        capacities[degree] = [ambient - value for value in row_deficits]
    return capacities


def main() -> int:
    duality_checks = 0
    recurrence_checks = 0

    for n in range(3, 9):
        minima = {
            degree: direct_minimum_table(n, degree)
            for degree in range(2, n)
        }
        gammas = {
            degree: inverse_table(
                minima[degree],
                comb(n, degree - 1) ** 2,
            )
            for degree in range(2, n)
        }

        for degree in range(2, n):
            lower_ambient = comb(n, degree - 1) ** 2
            upper_ambient = comb(n, degree) ** 2
            complementary_degree = n - degree + 1
            for missing_lower in range(lower_ambient + 1):
                require(
                    gammas[degree][lower_ambient - missing_lower]
                    == upper_ambient - minima[complementary_degree][missing_lower],
                    (n, degree, missing_lower),
                )
                duality_checks += 1

        maximum_terms = max(EXPECTED_THRESHOLDS[str(n)])
        direct = direct_rows(n, minima, gammas, maximum_terms)
        transported = transported_rows(n, minima, maximum_terms)
        require(direct == transported, n)

        observed = []
        for degree in range(1, n):
            ambient = comb(n, degree) ** 2
            observed.append(next(q for q, value in enumerate(direct[degree]) if value == ambient))
            recurrence_checks += len(direct[degree])
        require(observed == EXPECTED_THRESHOLDS[str(n)], (n, observed))

    require(duality_checks == 17_378, duality_checks)
    require(recurrence_checks == 1_178, recurrence_checks)
    print("independent_duality_identity_checks=17378")
    print("independent_tower_deficit_entry_checks=1178")
    print("independent_threshold_n7=7,22,39,46,48,49")
    print("independent_threshold_n8=8,29,59,80,87,89,90")
    print("GENERAL_SHADOW_COMPLEMENT_DEFICIT_DUALITY_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
