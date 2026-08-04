#!/usr/bin/env python3
"""Exact arithmetic audit of the realizability-aware ``n=6`` fixed-four frontier.

Assume hypothetically that ``perm_6`` has a 23-term Chow decomposition and
fix four terms with sum ``R``. The mathematical note
``docs/n6_fixed_four_coupled_frontier.md`` proves:

* the central intersection ``b`` is at most 27, improving the raw Bukh cap 40;
* the central catalectic quotient dimension ``d`` satisfies
  ``20 <= b <= 27`` and ``0 <= d <= b-20``;
* exactly 36 integer states remain;
* three states are already excluded by the residual rank budget;
* twelve states can be excluded by relative-prolongation caps 23 or 59; and
* twenty-one states require structural exclusion or a stronger invariant.

This script checks only the exact arithmetic and state partition. It does not
replace the torus-degeneration, projection, multidimensional-shadow, or
coupling arguments in the proof note.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import factorial
from pathlib import Path

PERMANENT_KOSZUL_RANK = 14_175
PER_TERM_KOSZUL_CAP = 705
PER_TERM_CENTRAL_CAP = 20
PER_TERM_QUADRATIC_CAP = 15
PER_TERM_QUADRATIC_INTERSECTION_CAP = 3
FIXED_TERMS = 4
RESIDUAL_TERMS = 19
RESIDUAL_KOSZUL_CAP = RESIDUAL_TERMS * PER_TERM_KOSZUL_CAP
RESIDUAL_CENTRAL_CAP = RESIDUAL_TERMS * PER_TERM_CENTRAL_CAP
AMBIENT_VARIABLES = 36
BUKH_SEPARATOR = Fraction(427, 100)


def generalized_binomial(value: Fraction, order: int) -> Fraction:
    result = Fraction(1)
    for index in range(order):
        result *= value - index
    return result / factorial(order)


def bukh_separator_certificate() -> dict[str, object]:
    cubic_size = generalized_binomial(BUKH_SEPARATOR, 3) ** 2
    quadratic_shadow = generalized_binomial(BUKH_SEPARATOR, 2) ** 2

    if not cubic_size < 28:
        raise AssertionError(cubic_size)
    if not quadratic_shadow > 48:
        raise AssertionError(quadratic_shadow)

    return {
        "separator": str(BUKH_SEPARATOR),
        "binom_separator_3_squared": str(cubic_size),
        "binom_separator_3_squared_is_less_than_28": True,
        "binom_separator_2_squared": str(quadratic_shadow),
        "binom_separator_2_squared_is_greater_than_48": True,
        "conclusion": (
            "A subspace of D_3(perm_6) with first-derivative shadow at most "
            "48 has dimension at most 27."
        ),
    }


def build_states() -> list[dict[str, object]]:
    states: list[dict[str, object]] = []

    for intersection_dimension in range(20, 28):
        for quotient_dimension in range(
            0,
            intersection_dimension - 20 + 1,
        ):
            central_rank = intersection_dimension + quotient_dimension
            required_gain = max(
                0,
                RESIDUAL_KOSZUL_CAP
                + 1
                - (
                    PERMANENT_KOSZUL_RANK
                    - AMBIENT_VARIABLES * intersection_dimension
                ),
            )
            maximum_gain = AMBIENT_VARIABLES * quotient_dimension

            if required_gain == 0:
                route = "rank_budget_already_strict"
                prolongation_cap = None
            elif maximum_gain < required_gain:
                route = "structural_exclusion_or_stronger_invariant_required"
                prolongation_cap = None
            else:
                route = "relative_prolongation_cap_can_close"
                prolongation_cap = maximum_gain - required_gain
                if prolongation_cap not in {23, 59}:
                    raise AssertionError(prolongation_cap)

            states.append(
                {
                    "central_intersection_b": intersection_dimension,
                    "central_quotient_dimension_d": quotient_dimension,
                    "central_rank_h": central_rank,
                    "central_rank_upper_from_residual": (
                        2 * intersection_dimension - 20
                    ),
                    "minimum_quotient_gain_for_strict_koszul_budget": required_gain,
                    "maximum_possible_quotient_gain": maximum_gain,
                    "relative_prolongation_cap_sufficient_for_closure": prolongation_cap,
                    "route": route,
                }
            )

    if len(states) != 36:
        raise AssertionError(len(states))
    return states


def build_payload() -> dict[str, object]:
    projection_cap = (
        (FIXED_TERMS - 1) * PER_TERM_QUADRATIC_CAP
        + PER_TERM_QUADRATIC_INTERSECTION_CAP
    )
    if projection_cap != 48:
        raise AssertionError(projection_cap)

    states = build_states()
    route_histogram = Counter(row["route"] for row in states)
    expected_histogram = {
        "rank_budget_already_strict": 3,
        "relative_prolongation_cap_can_close": 12,
        "structural_exclusion_or_stronger_invariant_required": 21,
    }
    if dict(route_histogram) != expected_histogram:
        raise AssertionError(route_histogram)

    p_cap_histogram = Counter(
        row["relative_prolongation_cap_sufficient_for_closure"]
        for row in states
        if row["relative_prolongation_cap_sufficient_for_closure"] is not None
    )
    if dict(p_cap_histogram) != {23: 6, 59: 6}:
        raise AssertionError(p_cap_histogram)

    return {
        "status": "EXACT_INTEGER_FRONTIER_REPLAYED",
        "hypothesis": "a 23-term Chow decomposition of perm_6",
        "fixed_terms": FIXED_TERMS,
        "residual_terms": RESIDUAL_TERMS,
        "residual_koszul_cap": RESIDUAL_KOSZUL_CAP,
        "residual_central_catalectic_cap": RESIDUAL_CENTRAL_CAP,
        "quadratic_intersection_projection_cap": projection_cap,
        "bukh_separator_certificate": bukh_separator_certificate(),
        "central_intersection_range": [20, 27],
        "state_count": len(states),
        "route_histogram": dict(sorted(route_histogram.items())),
        "relative_prolongation_cap_histogram": {
            str(key): value for key, value in sorted(p_cap_histogram.items())
        },
        "states": states,
        "claim_boundary": (
            "The audit proves the numerical frontier only. It does not exclude "
            "the 21 structural states or establish the p<=23 and p<=59 caps."
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
    print("N6_FIXED_FOUR_COUPLED_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
