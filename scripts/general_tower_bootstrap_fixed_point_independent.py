#!/usr/bin/env python3
"""Independent replay of the n=7 derivative-tower bootstrap closure.

This file imports none of the primary bootstrap or exact-shadow modules. It
reconstructs colex order, first shadows, first-container weights, the Ferrers
recurrence, every capacity row through degree five, and every Koszul bootstrap
candidate through the fixed point 47.
"""

from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from itertools import combinations
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


class IndependentFirstShadow:
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
    lower_bound = -(-target // one_term)
    return target, one_term, lower_bound


def scan(n: int, rows: dict[int, list[int]], lower_bound: int) -> list[list[int]]:
    result = []
    for output_degree in range(2, n - 1):
        complementary_degree = n - output_degree
        target, one_term, _ = first_koszul(n, output_degree)
        for fixed_terms in range(1, lower_bound + 1):
            cap = rows[complementary_degree][fixed_terms]
            numerator = target - n * n * cap
            residual = 0 if numerator <= 0 else -(-numerator // one_term)
            result.append(
                [
                    lower_bound,
                    output_degree,
                    complementary_degree,
                    fixed_terms,
                    cap,
                    target,
                    one_term,
                    numerator,
                    residual,
                    fixed_terms + residual,
                ]
            )
    return result


def step(n: int, rows: dict[int, list[int]], lower_bound: int) -> tuple[int, int, str]:
    table = scan(n, rows, lower_bound)
    output = max([lower_bound, *(row[-1] for row in table)])
    count = sum(row[-1] == output for row in table)
    return output, count, canonical_sha256(table)


def main() -> int:
    n = 7
    rows = tower_rows(n, 5, 47)
    expected_row_hashes = {
        1: "dd5c90d63280597099bbb44281011baf7a91e9866c3c1dadca75e11015ea7c2c",
        2: "5ae812113ab22d0a274717e849d58476eb312acfca3e308b4de459178d5e215a",
        3: "35f9e59f67db39e8994bb7e898af46bc1ace17c3df22f6cc442bf3505c1be208",
        4: "d074d44521a93a74bfe346bdcb8bc3aced8a6925ca49f21471257f74f59a25c6",
        5: "c6780cc7fa8b07dc8bba5823429303decde202833bff56788566dbe8527146be",
    }
    require(
        {degree: canonical_sha256(row) for degree, row in rows.items()}
        == expected_row_hashes,
        rows,
    )
    require(
        (rows[4][20], rows[5][36], rows[5][39], rows[5][46], rows[5][47])
        == (341, 233, 267, 405, 426),
        rows[5],
    )

    base = max(first_koszul(n, degree)[2] for degree in range(2, n - 1))
    require(base == 36, base)
    step_36 = step(n, rows, 36)
    step_46 = step(n, rows, 46)
    step_47 = step(n, rows, 47)
    require(
        step_36
        == (
            46,
            4,
            "202033c70b741647b7c768932b2a5ea30a8aae6ab492144661a9d025ad1b9b19",
        ),
        step_36,
    )
    require(
        step_46
        == (
            47,
            8,
            "99e34ee704bf1db03d9e5071f6789827788152dc02a6209d82d30a30cbacbb96",
        ),
        step_46,
    )
    require(
        step_47
        == (
            47,
            12,
            "b2ee29697a66edea251fbd7e1461e0c4109cf2311dbf546c1db24477387dfa8e",
        ),
        step_47,
    )

    target, one_term, _ = first_koszul(7, 2)
    numerator = target - 49 * rows[5][46]
    require((target, one_term, numerator) == (20_384, 994, 539), (
        target,
        one_term,
        numerator,
    ))

    print("independent_n7_bootstrap_sequence=36,46,47,47")
    print("independent_B_7_5_46=405")
    print("independent_B_7_5_47=426")
    print("independent_perm7_lower_bound=47")
    print("independent_n7_scalar_tower_fixed_point=47")
    print("GENERAL_TOWER_BOOTSTRAP_FIXED_POINT_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
