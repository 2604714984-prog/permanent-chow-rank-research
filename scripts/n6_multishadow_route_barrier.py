#!/usr/bin/env python3
"""Exact route barrier for the current ``n=6`` one-step multishadow theorem.

The script optimizes the proved one-step Bukh-shadow/Koszul formula over every
admissible output degree ``m=2,3,4`` and every attainable integer fixed-term
count. All comparisons use ``Fraction`` arithmetic. It also checks an explicit
central coordinate family of size 40 and shadow size 60, showing that the
``q=4`` Bukh cap is sharp as a universal shadow statement.

This is a method-boundary certificate. It does not upper-bound Chow rank and it
does not rule out stronger arguments that use Chow realizability, a positive
quotient Koszul gain, or a different invariant.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path

N = 6


def generalized_binomial(x: Fraction, r: int) -> Fraction:
    x = Fraction(x)
    out = Fraction(1)
    for i in range(r):
        out *= x - i
    return out / factorial(r)


def ceil_fraction(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)


def threshold_interval(
    output_degree: int,
    fixed_terms: int,
    iterations: int = 256,
) -> tuple[Fraction, Fraction]:
    complementary_degree = N - output_degree
    target = fixed_terms * comb(N, complementary_degree - 1)
    lower = Fraction(complementary_degree)
    upper = Fraction(N)

    if generalized_binomial(lower, complementary_degree - 1) ** 2 >= target:
        return lower, lower

    for _ in range(iterations):
        midpoint = (lower + upper) / 2
        if generalized_binomial(midpoint, complementary_degree - 1) ** 2 >= target:
            upper = midpoint
        else:
            lower = midpoint
    return lower, upper


def minimum_intersection_cap(
    output_degree: int,
    fixed_terms: int,
) -> tuple[int, Fraction, Fraction]:
    complementary_degree = N - output_degree
    lower, upper = threshold_interval(output_degree, fixed_terms)
    target = fixed_terms * comb(N, complementary_degree - 1)

    assert generalized_binomial(lower, complementary_degree - 1) ** 2 <= target
    assert generalized_binomial(upper, complementary_degree - 1) ** 2 >= target

    lower_value = generalized_binomial(lower, complementary_degree) ** 2
    upper_value = generalized_binomial(upper, complementary_degree) ** 2
    lower_floor = lower_value.numerator // lower_value.denominator
    upper_floor = upper_value.numerator // upper_value.denominator

    exact_threshold = (
        generalized_binomial(upper, complementary_degree - 1) ** 2 == target
    )
    if not exact_threshold:
        assert lower_floor == upper_floor, (
            output_degree,
            fixed_terms,
            lower_floor,
            upper_floor,
        )
    else:
        # At a closed threshold the admissible point is ``upper`` itself. The
        # floor may jump there, as happens at the integer witnesses 5 and 6.
        assert upper_value.denominator == 1 or upper_floor - lower_floor in (0, 1)

    return upper_floor, lower, upper


def route_rows(output_degree: int) -> list[dict[str, object]]:
    complementary_degree = N - output_degree
    derivative_dimension = comb(N, output_degree)
    target_rank = (
        N * N * derivative_dimension**2
        - comb(N, output_degree + 1) ** 2
    )
    term_cap = (
        N * N * derivative_dimension
        - comb(N, output_degree + 1)
    )

    rows: list[dict[str, object]] = []
    for fixed_terms in range(1, comb(N, complementary_degree - 1) + 1):
        intersection_cap, lower, upper = minimum_intersection_cap(
            output_degree,
            fixed_terms,
        )
        residual_rank = target_rank - N * N * intersection_cap
        residual_terms = max(
            0,
            ceil_fraction(Fraction(residual_rank, term_cap)),
        )
        rows.append(
            {
                "output_degree": output_degree,
                "complementary_degree": complementary_degree,
                "fixed_terms": fixed_terms,
                "minimum_bukh_intersection_cap": intersection_cap,
                "residual_rank_floor": residual_rank,
                "residual_terms": residual_terms,
                "total_lower_bound_from_route": fixed_terms + residual_terms,
                "threshold_lower": str(lower),
                "threshold_upper": str(upper),
            }
        )
    return rows


def sharp_q4_family() -> dict[str, int]:
    left = list(combinations(range(5), 3))
    right = list(combinations(range(4), 3))
    left_shadow = {
        pair
        for triple in left
        for pair in combinations(triple, 2)
    }
    right_shadow = {
        pair
        for triple in right
        for pair in combinations(triple, 2)
    }
    family_size = len(left) * len(right)
    shadow_size = len(left_shadow) * len(right_shadow)
    assert (family_size, shadow_size) == (40, 60)
    return {
        "left_family_size": len(left),
        "right_family_size": len(right),
        "family_size": family_size,
        "left_shadow_size": len(left_shadow),
        "right_shadow_size": len(right_shadow),
        "simultaneous_shadow_size": shadow_size,
    }


def build_payload() -> dict[str, object]:
    rows = [
        row
        for output_degree in (2, 3, 4)
        for row in route_rows(output_degree)
    ]
    maximum = max(int(row["total_lower_bound_from_route"]) for row in rows)
    maximizers = [
        {
            "output_degree": row["output_degree"],
            "fixed_terms": row["fixed_terms"],
            "minimum_bukh_intersection_cap": row[
                "minimum_bukh_intersection_cap"
            ],
            "residual_terms": row["residual_terms"],
        }
        for row in rows
        if row["total_lower_bound_from_route"] == maximum
    ]

    assert maximum == 23
    assert maximizers == [
        {
            "output_degree": 3,
            "fixed_terms": 4,
            "minimum_bukh_intersection_cap": 40,
            "residual_terms": 19,
        },
        {
            "output_degree": 3,
            "fixed_terms": 5,
            "minimum_bukh_intersection_cap": 60,
            "residual_terms": 18,
        },
    ]

    return {
        "status": "COMPUTATION_REPLAYED",
        "scope": "optimization of the proved n=6 one-step multishadow formula",
        "maximum_certified_lower_bound_within_route": maximum,
        "maximizers": maximizers,
        "sharp_q4_coordinate_family": sharp_q4_family(),
        "rows": rows,
        "claim_boundary": (
            "The current one-step multishadow formula cannot exceed 23. "
            "A stronger Chow-rank result requires realizability information, "
            "a positive quotient Koszul gain, or a different invariant."
        ),
    }


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
    print("N6_MULTISHADOW_ROUTE_BARRIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
