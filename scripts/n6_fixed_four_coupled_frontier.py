#!/usr/bin/env python3
"""Exact arithmetic audit of the realizability-aware ``n=6`` fixed-four frontier.

Assume hypothetically that ``perm_6`` has a 23-term Chow decomposition and
fix four terms with sum ``R``. The proof notes establish:

* the raw projection-shadow frontier has ``20<=b<=27`` and 36 states;
* for ``20<=b<=27``, the quadratic derivative shadow is at least ``b+21``;
* the individual quadratic-space defects satisfy the budget ``27-b``;
* common-quotient rigidity excludes every state with ``b=27``;
* the current frontier therefore has ``20<=b<=26`` and 28 states;
* the top layer ``b=26`` has exactly 24 labelled defect patterns;
* three states are already excluded by the residual rank budget;
* ten states can be excluded by relative-prolongation caps 23 or 59; and
* fifteen states require structural exclusion or a stronger invariant.

This script checks only the exact arithmetic and state partitions. It does not
replace the projection, Bukh-shadow, common-quotient, or catalectic arguments
in the proof notes.
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
SHADOW_SEPARATORS: dict[int, Fraction] = {
    20: Fraction(41, 10),
    21: Fraction(103, 25),
    22: Fraction(207, 50),
    23: Fraction(104, 25),
    24: Fraction(209, 50),
    25: Fraction(21, 5),
    26: Fraction(211, 50),
    27: Fraction(106, 25),
}


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


def exact_shadow_lower_table() -> dict[str, dict[str, object]]:
    table: dict[str, dict[str, object]] = {}
    for dimension, separator in SHADOW_SEPARATORS.items():
        cubic_size = generalized_binomial(separator, 3) ** 2
        quadratic_shadow = generalized_binomial(separator, 2) ** 2
        target_shadow = dimension + 20

        if not cubic_size < dimension:
            raise AssertionError((dimension, cubic_size))
        if not quadratic_shadow > target_shadow:
            raise AssertionError((dimension, quadratic_shadow))

        table[str(dimension)] = {
            "separator": str(separator),
            "binom_separator_3_squared": str(cubic_size),
            "binom_separator_2_squared": str(quadratic_shadow),
            "integer_shadow_lower_bound": dimension + 21,
            "per_omitted_factor_defect_budget": 27 - dimension,
        }
    return table


def build_b26_defect_patterns() -> list[dict[str, object]]:
    """Enumerate every labelled solution of the ``b=26`` defect inequalities."""

    patterns: list[dict[str, object]] = []

    # Family A: one epsilon_i=1; only alpha_i may be zero or one.
    for index in range(FIXED_TERMS):
        for alpha_value in (0, 1):
            epsilon = [0] * FIXED_TERMS
            alpha = [0] * FIXED_TERMS
            epsilon[index] = 1
            alpha[index] = alpha_value
            patterns.append(
                {
                    "family": "one_quadratic_dimension_defect",
                    "epsilon": epsilon,
                    "alpha": alpha,
                }
            )

    # Family B: every epsilon is zero and the four alpha bits are arbitrary.
    for mask in range(1 << FIXED_TERMS):
        alpha = [
            (mask >> index) & 1
            for index in range(FIXED_TERMS)
        ]
        patterns.append(
            {
                "family": "maximal_quadratic_dimensions",
                "epsilon": [0] * FIXED_TERMS,
                "alpha": alpha,
            }
        )

    for pattern in patterns:
        epsilon = pattern["epsilon"]
        alpha = pattern["alpha"]
        if not isinstance(epsilon, list) or not isinstance(alpha, list):
            raise AssertionError(pattern)
        for omitted in range(FIXED_TERMS):
            left = sum(
                int(epsilon[index])
                for index in range(FIXED_TERMS)
                if index != omitted
            ) + int(alpha[omitted])
            if left > 1:
                raise AssertionError((pattern, omitted, left))

    if len(patterns) != 24:
        raise AssertionError(len(patterns))
    family_histogram = Counter(str(pattern["family"]) for pattern in patterns)
    if dict(family_histogram) != {
        "one_quadratic_dimension_defect": 8,
        "maximal_quadratic_dimensions": 16,
    }:
        raise AssertionError(family_histogram)
    return patterns


def build_raw_states() -> list[dict[str, object]]:
    states: list[dict[str, object]] = []

    for intersection_dimension in range(20, 28):
        shadow_lower = intersection_dimension + 21
        defect_budget = 27 - intersection_dimension
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
                    "quadratic_shadow_lower_bound": shadow_lower,
                    "per_omitted_factor_defect_budget": defect_budget,
                    "minimum_quotient_gain_for_strict_koszul_budget": required_gain,
                    "maximum_possible_quotient_gain": maximum_gain,
                    "relative_prolongation_cap_sufficient_for_closure": prolongation_cap,
                    "route": route,
                }
            )

    if len(states) != 36:
        raise AssertionError(len(states))
    return states


def histogram(states: list[dict[str, object]]) -> dict[str, int]:
    return dict(sorted(Counter(row["route"] for row in states).items()))


def prolongation_histogram(states: list[dict[str, object]]) -> dict[str, int]:
    counts = Counter(
        row["relative_prolongation_cap_sufficient_for_closure"]
        for row in states
        if row["relative_prolongation_cap_sufficient_for_closure"] is not None
    )
    return {str(key): value for key, value in sorted(counts.items())}


def build_payload() -> dict[str, object]:
    projection_cap = (
        (FIXED_TERMS - 1) * PER_TERM_QUADRATIC_CAP
        + PER_TERM_QUADRATIC_INTERSECTION_CAP
    )
    if projection_cap != 48:
        raise AssertionError(projection_cap)

    shadow_table = exact_shadow_lower_table()
    defect_patterns = build_b26_defect_patterns()
    raw_states = build_raw_states()
    excluded_states = [
        row for row in raw_states if row["central_intersection_b"] == 27
    ]
    states = [
        row for row in raw_states if row["central_intersection_b"] <= 26
    ]

    raw_histogram = histogram(raw_states)
    expected_raw_histogram = {
        "rank_budget_already_strict": 3,
        "relative_prolongation_cap_can_close": 12,
        "structural_exclusion_or_stronger_invariant_required": 21,
    }
    if raw_histogram != expected_raw_histogram:
        raise AssertionError(raw_histogram)
    if prolongation_histogram(raw_states) != {"23": 6, "59": 6}:
        raise AssertionError(prolongation_histogram(raw_states))

    surviving_histogram = histogram(states)
    expected_surviving_histogram = {
        "rank_budget_already_strict": 3,
        "relative_prolongation_cap_can_close": 10,
        "structural_exclusion_or_stronger_invariant_required": 15,
    }
    if surviving_histogram != expected_surviving_histogram:
        raise AssertionError(surviving_histogram)
    if prolongation_histogram(states) != {"23": 5, "59": 5}:
        raise AssertionError(prolongation_histogram(states))
    if len(excluded_states) != 8 or len(states) != 28:
        raise AssertionError((len(excluded_states), len(states)))

    maximum_remaining_requirement = max(
        row["minimum_quotient_gain_for_strict_koszul_budget"]
        for row in states
    )
    if maximum_remaining_requirement != 157:
        raise AssertionError(maximum_remaining_requirement)

    defect_family_histogram = dict(
        sorted(Counter(str(row["family"]) for row in defect_patterns).items())
    )

    return {
        "status": "EXACT_INTEGER_FRONTIER_WITH_B27_EXCLUSION_REPLAYED",
        "hypothesis": "a 23-term Chow decomposition of perm_6",
        "fixed_terms": FIXED_TERMS,
        "residual_terms": RESIDUAL_TERMS,
        "residual_koszul_cap": RESIDUAL_KOSZUL_CAP,
        "residual_central_catalectic_cap": RESIDUAL_CENTRAL_CAP,
        "quadratic_intersection_projection_cap": projection_cap,
        "bukh_separator_certificate": bukh_separator_certificate(),
        "exact_shadow_lower_table": shadow_table,
        "raw_projection_frontier": {
            "central_intersection_range": [20, 27],
            "state_count": len(raw_states),
            "route_histogram": raw_histogram,
            "relative_prolongation_cap_histogram": prolongation_histogram(
                raw_states
            ),
        },
        "common_quotient_b27_exclusion": {
            "excluded_central_intersection": 27,
            "excluded_state_count": len(excluded_states),
            "individual_quadratic_dimensions": [15, 15, 15, 15],
            "individual_intersection_dimensions": [3, 3, 3, 3],
            "common_quotient_dimension": 12,
            "forced_quadratic_sum_dimension": 60,
            "forced_central_catalectic_rank": 80,
            "residual_inequality_upper_bound_on_central_rank": 34,
            "contradiction": "80>34",
        },
        "b26_defect_patterns": {
            "pattern_count": len(defect_patterns),
            "family_histogram": defect_family_histogram,
            "patterns": defect_patterns,
        },
        "central_intersection_range": [20, 26],
        "state_count": len(states),
        "route_histogram": surviving_histogram,
        "relative_prolongation_cap_histogram": prolongation_histogram(states),
        "maximum_remaining_gain_requirement": maximum_remaining_requirement,
        "states": states,
        "excluded_b27_states": excluded_states,
        "claim_boundary": (
            "The audit replays the 28-state frontier and 24 b=26 defect "
            "patterns after the proved b=27 common-quotient exclusion. It "
            "does not exclude the 15 remaining structural states or "
            "establish the p<=23 and p<=59 caps."
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
