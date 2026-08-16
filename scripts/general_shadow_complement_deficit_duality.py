#!/usr/bin/env python3
"""Exact shadow-complement duality and deficit transport for perm_n.

For the product layer

    U_d = C([n],d) x C([n],d),

let F_(n,d)(b) be the exact minimum simultaneous lower shadow of a b-plane in
D_d(perm_n), and let Gamma_(n,d) be its inverse capacity.  Complementing both
coordinates identifies missing lower cells with an upper shadow, yielding

    Gamma_(n,d)(A_(d-1)-z)
      = A_d - F_(n,n-d+1)(z).

The identity converts the derivative-tower recurrence into an exact recurrence
for capacity deficits.  This script reconstructs the Ferrers inverse tables
with exact integer arithmetic, verifies the duality exhaustively for n=3..8,
and checks that the deficit recurrence reproduces every tower row through its
saturation threshold.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def colex_layer(n: int, degree: int) -> tuple[tuple[int, ...], ...]:
    require(1 <= degree < n, (n, degree))
    result = tuple(sorted(combinations(range(n), degree), key=colex_rank))
    require(
        tuple(colex_rank(value) for value in result)
        == tuple(range(len(result))),
        ("noncontiguous colex ranks", n, degree),
    )
    return result


def first_shadow_profile_and_weights(
    n: int,
    degree: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    layer = colex_layer(n, degree)
    running: set[tuple[int, ...]] = set()
    profile = [0]
    weights = []
    for upper in layer:
        running.update(combinations(upper, degree - 1))
        profile.append(len(running))
        present = set(upper)
        weights.append(next(value for value in range(n) if value not in present))
    require(profile[-1] == comb(n, degree - 1), (n, degree, profile[-1]))
    require(sum(weights) == comb(n, degree - 1), (n, degree, weights))
    return tuple(profile), tuple(weights)


class ExactInverseShadow:
    """All inverse capacities Gamma_(n,d)(C) by a dual Ferrers budget DP."""

    def __init__(self, n: int, degree: int) -> None:
        self.n = n
        self.degree = degree
        self.profile, self.weights = first_shadow_profile_and_weights(n, degree)
        self.width = len(self.weights)
        self.lower_ambient = comb(n, degree - 1) ** 2
        self.upper_ambient = self.width**2
        self.gamma = self._build_gamma()
        self.minimum = self._invert_gamma()

    def _build_gamma(self) -> tuple[int, ...]:
        budget = self.lower_ambient
        width = self.width
        negative = -10**9

        # dp[u][c] is the largest partition sum after the processed rows when
        # the most recent part is u and the exact shadow cost is c.
        dp = [[negative] * (budget + 1) for _ in range(width + 1)]
        dp[width][0] = 0

        for weight in self.weights:
            new = [[negative] * (budget + 1) for _ in range(width + 1)]
            for cost in range(budget + 1):
                best_upper = negative
                for part in range(width, -1, -1):
                    if dp[part][cost] > best_upper:
                        best_upper = dp[part][cost]
                    if best_upper < 0:
                        continue
                    new_cost = cost + weight * self.profile[part]
                    if new_cost <= budget:
                        candidate = best_upper + part
                        if candidate > new[part][new_cost]:
                            new[part][new_cost] = candidate
            dp = new

        gamma = []
        running = 0
        for cost in range(budget + 1):
            exact = max(dp[part][cost] for part in range(width + 1))
            if exact > running:
                running = exact
            gamma.append(running)
        require(gamma[0] == 0, (self.n, self.degree, gamma[0]))
        require(
            gamma[-1] == self.upper_ambient,
            (self.n, self.degree, gamma[-1], self.upper_ambient),
        )
        require(
            all(left <= right for left, right in zip(gamma, gamma[1:])),
            (self.n, self.degree),
        )
        return tuple(gamma)

    def _invert_gamma(self) -> tuple[int, ...]:
        result = []
        cost = 0
        for family_size in range(self.upper_ambient + 1):
            while self.gamma[cost] < family_size:
                cost += 1
            result.append(cost)
        require(result[0] == 0, result[:2])
        require(result[-1] == self.lower_ambient, result[-2:])
        return tuple(result)


EXPECTED_THRESHOLDS: dict[str, list[int]] = {
    "3": [3, 4],
    "4": [4, 7, 8],
    "5": [5, 11, 14, 15],
    "6": [6, 16, 24, 26, 27],
    "7": [7, 22, 39, 46, 48, 49],
    "8": [8, 29, 59, 80, 87, 89, 90],
}


def direct_tower_rows(
    n: int,
    tables: dict[int, ExactInverseShadow],
    maximum_terms: int,
) -> dict[int, list[int]]:
    rows: dict[int, list[int]] = {
        1: [min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    for degree in range(2, n):
        one_term = comb(n, degree)
        ambient = one_term**2
        row = []
        prefix_defect = 0
        for terms in range(maximum_terms + 1):
            direct = min(
                ambient,
                terms * one_term,
                tables[degree].gamma[rows[degree - 1][terms]],
            )
            current_defect = direct - terms * one_term
            if terms == 0 or current_defect < prefix_defect:
                prefix_defect = current_defect
            row.append(min(ambient, terms * one_term + prefix_defect))
        rows[degree] = row
    return rows


def deficit_tower_rows(
    n: int,
    tables: dict[int, ExactInverseShadow],
    maximum_terms: int,
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    deficits: dict[int, list[int]] = {
        1: [n * n - min(n * n, terms * n) for terms in range(maximum_terms + 1)]
    }
    capacities: dict[int, list[int]] = {
        1: [n * n - value for value in deficits[1]]
    }

    for degree in range(2, n):
        one_term = comb(n, degree)
        ambient = one_term**2
        complementary_degree = n - degree + 1
        complementary_shadow = tables[complementary_degree].minimum
        row_deficits = []
        running = -10**18
        for terms in range(maximum_terms + 1):
            direct_deficit = max(
                0,
                ambient - terms * one_term,
                complementary_shadow[deficits[degree - 1][terms]],
            )
            running = max(running, direct_deficit + terms * one_term)
            row_deficits.append(max(0, running - terms * one_term))
        deficits[degree] = row_deficits
        capacities[degree] = [ambient - value for value in row_deficits]

    return capacities, deficits


def saturation_threshold(row: list[int], ambient: int) -> int:
    require(row[0] == 0, row[:2])
    require(all(left <= right for left, right in zip(row, row[1:])), row)
    return next(index for index, value in enumerate(row) if value == ambient)


def build_payload() -> dict[str, Any]:
    tables_by_n: dict[int, dict[int, ExactInverseShadow]] = {}
    duality_checks = 0
    recurrence_checks = 0
    thresholds: dict[str, list[int]] = {}

    for n in range(3, 9):
        tables = {
            degree: ExactInverseShadow(n, degree)
            for degree in range(2, n)
        }
        tables_by_n[n] = tables

        for degree in range(2, n):
            upper_ambient = comb(n, degree) ** 2
            lower_ambient = comb(n, degree - 1) ** 2
            complementary_degree = n - degree + 1
            for missing_lower in range(lower_ambient + 1):
                left = tables[degree].gamma[lower_ambient - missing_lower]
                right = (
                    upper_ambient
                    - tables[complementary_degree].minimum[missing_lower]
                )
                require(
                    left == right,
                    (n, degree, missing_lower, left, right),
                )
                duality_checks += 1

        expected = EXPECTED_THRESHOLDS[str(n)]
        maximum_terms = max(expected)
        direct = direct_tower_rows(n, tables, maximum_terms)
        transported, _ = deficit_tower_rows(n, tables, maximum_terms)
        require(direct == transported, (n, direct, transported))

        observed = []
        for degree in range(1, n):
            ambient = comb(n, degree) ** 2
            observed.append(saturation_threshold(direct[degree], ambient))
            recurrence_checks += len(direct[degree])
        require(observed == expected, (n, observed, expected))
        thresholds[str(n)] = observed

    require(duality_checks == 17_378, duality_checks)
    require(recurrence_checks == 1_178, recurrence_checks)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_SHADOW_COMPLEMENT_DUALITY_THEOREM",
            "GENERAL_DEFICIT_TRANSPORT_RECURRENCE",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "duality": (
                "Gamma_(n,d)(A_(d-1)-z)="
                "A_d-F_(n,n-d+1)(z)."
            ),
            "direct_deficit": (
                "H_(n,d)(q)=max(0,A_d-q*M_d,"
                "F_(n,n-d+1)(D_(n,d-1)(q)))."
            ),
            "transport": (
                "D_(n,d)(q)=max_(0<=t<=q)"
                "(H_(n,d)(t)-(q-t)*M_d)."
            ),
            "saturation": (
                "Q_(n,d)=min{q:D_(n,d)(q)=0}, and every Chow "
                "decomposition has at least max_d Q_(n,d) terms."
            ),
        },
        "exhaustive_replay": {
            "n_min": 3,
            "n_max": 8,
            "duality_identity_checks": duality_checks,
            "tower_deficit_entry_checks": recurrence_checks,
            "thresholds": thresholds,
        },
        "claim_boundary": (
            "The shadow-complement identity and deficit transport are exact "
            "general-n reformulations of the scalar permanent derivative "
            "tower. They reproduce the full-degree saturation thresholds "
            "through n=8 but do not improve those numerical bounds by "
            "themselves, determine an exact rank for n>=6, prove a border-rank "
            "statement, provide the asymptotic rate of the tower, or prove "
            "general Glynn optimality."
        ),
    }
    return core


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_SHADOW_COMPLEMENT_DEFICIT_DUALITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
