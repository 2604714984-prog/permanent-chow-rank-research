#!/usr/bin/env python3
"""Exact fixed-q diagnostic for a hypothetical 24-term decomposition of perm_6.

The script rebuilds the arithmetic for q=4,5,6 fixed terms. It certifies
Bukh-shadow lower bounds with exact rational brackets, enumerates every
central state, applies the already-proved scalar component-prolongation
bound, and records the remaining quotient-Koszul route.

This is a route diagnostic only. It does not prove ChowRank(perm_6)>=25.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb, factorial
from pathlib import Path

TOTAL_TERMS = 24
PERMANENT_CENTRAL_DIMENSION = 400
PERMANENT_KOSZUL_RANK = 14_175
PER_TERM_CENTRAL_CAP = 20
PER_TERM_KOSZUL_CAP = 705
PER_TERM_QUADRATIC_CAP = 15
PER_TERM_INTERSECTION_CAP = 3
AMBIENT_VARIABLES = 36
FIXED_TERM_CHOICES = (4, 5, 6)

CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION: dict[int, int | None] = {
    15: 20,
    14: 20,
    13: 18,
    12: None,
    11: 14,
    10: 0,
}


def canonical_sha256(value: object) -> str:
    text = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(text).hexdigest()


def generalized_binomial(value: Fraction, order: int) -> Fraction:
    result = Fraction(1)
    for index in range(order):
        result *= value - index
    return result / factorial(order)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def certify_shadow_lower(dimension: int) -> dict[str, object]:
    """Certify ceil(binomial(x,2)^2) where binomial(x,3)^2=dimension."""

    if dimension < 0:
        raise ValueError(dimension)
    if dimension == 0:
        return {
            "dimension": 0,
            "integer_shadow_lower_bound": 0,
            "lower_separator": "0",
            "upper_separator": "0",
            "exact_root": True,
        }

    for integer_root in range(3, 20):
        x = Fraction(integer_root)
        if generalized_binomial(x, 3) ** 2 == dimension:
            shadow = generalized_binomial(x, 2) ** 2
            if shadow.denominator != 1:
                raise AssertionError(shadow)
            return {
                "dimension": dimension,
                "integer_shadow_lower_bound": int(shadow),
                "lower_separator": str(x),
                "upper_separator": str(x),
                "exact_root": True,
            }

    for denominator in (
        10,
        100,
        1_000,
        10_000,
        100_000,
        1_000_000,
    ):
        low = 3 * denominator
        high = 10 * denominator
        while low + 1 < high:
            middle = (low + high) // 2
            x = Fraction(middle, denominator)
            if generalized_binomial(x, 3) ** 2 < dimension:
                low = middle
            else:
                high = middle

        lower = Fraction(low, denominator)
        upper = Fraction(high, denominator)
        lower_cubic = generalized_binomial(lower, 3) ** 2
        upper_cubic = generalized_binomial(upper, 3) ** 2
        if not lower_cubic < dimension < upper_cubic:
            continue

        lower_shadow = generalized_binomial(lower, 2) ** 2
        upper_shadow = generalized_binomial(upper, 2) ** 2
        if floor_fraction(lower_shadow) != floor_fraction(upper_shadow):
            continue

        integer_lower = floor_fraction(lower_shadow) + 1
        if not lower_shadow > integer_lower - 1:
            raise AssertionError((dimension, lower_shadow))
        if not upper_shadow < integer_lower:
            raise AssertionError((dimension, upper_shadow))
        return {
            "dimension": dimension,
            "integer_shadow_lower_bound": integer_lower,
            "lower_separator": str(lower),
            "upper_separator": str(upper),
            "exact_root": False,
        }

    raise AssertionError(f"no exact rational shadow bracket for {dimension}")


def shadow_certificates(maximum_dimension: int = 65) -> list[dict[str, object]]:
    certificates = [
        certify_shadow_lower(dimension)
        for dimension in range(maximum_dimension + 1)
    ]
    lowers = [
        int(row["integer_shadow_lower_bound"])
        for row in certificates
    ]
    if lowers != sorted(lowers):
        raise AssertionError(lowers)
    return certificates


def macaulay_successor_degree_two(value: int) -> int:
    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0

    remaining = value
    upper = 10**9
    answer = 0
    for degree in (2, 1):
        index = degree - 1
        while (
            index + 1 < upper
            and comb(index + 1, degree) <= remaining
        ):
            index += 1
        remaining -= comb(index, degree)
        answer += comb(index + 1, degree + 1)
        upper = index

    if remaining != 0:
        raise AssertionError((value, remaining))
    return answer


def projection_cap(fixed_terms: int) -> int:
    return (
        (fixed_terms - 1) * PER_TERM_QUADRATIC_CAP
        + PER_TERM_INTERSECTION_CAP
    )


def central_intersection_lower(fixed_terms: int) -> int:
    residual_terms = TOTAL_TERMS - fixed_terms
    return max(
        0,
        PERMANENT_CENTRAL_DIMENSION
        - residual_terms * PER_TERM_CENTRAL_CAP,
    )


def central_intersection_upper(
    fixed_terms: int,
    shadows: dict[int, int],
) -> int:
    cap = projection_cap(fixed_terms)
    start = central_intersection_lower(fixed_terms)
    for dimension in range(start, max(shadows) + 1):
        if shadows[dimension] > cap:
            return dimension - 1
    raise AssertionError((fixed_terms, cap))


def initial_states(
    fixed_terms: int,
    upper: int,
) -> list[dict[str, int]]:
    residual_terms = TOTAL_TERMS - fixed_terms
    residual_central_cap = residual_terms * PER_TERM_CENTRAL_CAP
    states: list[dict[str, int]] = []

    for b in range(central_intersection_lower(fixed_terms), upper + 1):
        maximum_d = min(
            fixed_terms * PER_TERM_CENTRAL_CAP - b,
            residual_central_cap
            - PERMANENT_CENTRAL_DIMENSION
            + b,
        )
        if maximum_d < 0:
            continue
        for d in range(maximum_d + 1):
            states.append(
                {
                    "b": b,
                    "d": d,
                    "h": b + d,
                }
            )
    return states


def central_rank_lower(quadratic_dimension: int) -> int | None:
    if quadratic_dimension in CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION:
        return CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION[
            quadratic_dimension
        ]
    if quadratic_dimension < 10:
        return 0
    raise ValueError(quadratic_dimension)


def scalar_component_bound(
    fixed_terms: int,
    b: int,
    shadow_lower: int,
) -> dict[str, object]:
    defect_budget = projection_cap(fixed_terms) - shadow_lower
    if defect_budget < 0:
        raise AssertionError((fixed_terms, b, defect_budget))

    all_zero_relation_cap = defect_budget
    all_zero_relation_dimension_cap = (
        (fixed_terms - 1)
        * macaulay_successor_degree_two(all_zero_relation_cap)
    )
    all_zero_central_lower = max(
        0,
        fixed_terms * PER_TERM_CENTRAL_CAP
        - 2 * all_zero_relation_dimension_cap,
    )

    if all_zero_central_lower <= b:
        return {
            "b": b,
            "shadow_lower_bound": shadow_lower,
            "defect_budget": defect_budget,
            "minimum_central_rank_lower_bound": 0,
            "minimizing_epsilon_profiles": [],
            "reason": (
                "The all-zero defect profile is not strict; the existing "
                "componentwise scalar bound cannot universally exclude "
                "this central layer."
            ),
        }

    best: int | None = None
    minimizers: list[list[int]] = []
    profile_count = 0

    for epsilon in combinations_with_replacement(
        range(PER_TERM_QUADRATIC_CAP + 1),
        fixed_terms,
    ):
        if 3 in epsilon:
            continue

        minimum_alpha = [
            max(0, value - 12)
            for value in epsilon
        ]
        if any(
            sum(epsilon)
            - epsilon[omitted]
            + minimum_alpha[omitted]
            > defect_budget
            for omitted in range(fixed_terms)
        ):
            continue

        quadratic_dimensions = [
            PER_TERM_QUADRATIC_CAP - value
            for value in epsilon
        ]
        quotient_dimensions = [
            max(12 - value, 0)
            for value in epsilon
        ]
        relation_cap = (
            sum(quadratic_dimensions)
            - shadow_lower
            - max(quotient_dimensions)
        )
        if relation_cap < 0:
            continue

        individual_lowers: list[int] = []
        profile_impossible = False
        for dimension in quadratic_dimensions:
            lower = central_rank_lower(dimension)
            if lower is None:
                profile_impossible = True
                break
            individual_lowers.append(lower)
        if profile_impossible:
            continue

        relation_dimension_cap = (
            (fixed_terms - 1)
            * macaulay_successor_degree_two(relation_cap)
        )
        central_lower = max(
            0,
            sum(individual_lowers)
            - 2 * relation_dimension_cap,
        )
        profile_count += 1

        if best is None or central_lower < best:
            best = central_lower
            minimizers = [list(epsilon)]
        elif central_lower == best:
            minimizers.append(list(epsilon))

    if best is None:
        raise AssertionError((fixed_terms, b, defect_budget))
    if minimizers != [[0] * fixed_terms]:
        raise AssertionError((fixed_terms, b, best, minimizers))

    return {
        "b": b,
        "shadow_lower_bound": shadow_lower,
        "defect_budget": defect_budget,
        "profile_count": profile_count,
        "minimum_central_rank_lower_bound": best,
        "minimizing_epsilon_profiles": minimizers,
        "reason": "Exact symmetric epsilon-profile optimization.",
    }


def route_for_state(
    fixed_terms: int,
    state: dict[str, int],
) -> dict[str, object]:
    b = state["b"]
    d = state["d"]
    residual_terms = TOTAL_TERMS - fixed_terms
    residual_koszul_cap = residual_terms * PER_TERM_KOSZUL_CAP
    base_residual_lower = PERMANENT_KOSZUL_RANK - AMBIENT_VARIABLES * b
    required_gain = max(
        0,
        residual_koszul_cap + 1 - base_residual_lower,
    )
    maximum_gain = AMBIENT_VARIABLES * d

    if required_gain == 0:
        route = "quotient_budget_already_strict"
        prolongation_cap = None
    elif maximum_gain < required_gain:
        route = "structural_exclusion_or_stronger_invariant_required"
        prolongation_cap = None
    else:
        route = "relative_prolongation_cap_can_close"
        prolongation_cap = maximum_gain - required_gain

    return {
        **state,
        "minimum_quotient_gain_for_strict_koszul_budget": required_gain,
        "maximum_possible_quotient_gain": maximum_gain,
        "sufficient_relative_prolongation_cap": prolongation_cap,
        "route": route,
    }


def fixed_q_payload(
    fixed_terms: int,
    shadows: dict[int, int],
) -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]]]:
    upper = central_intersection_upper(fixed_terms, shadows)
    states = initial_states(fixed_terms, upper)

    layer_cache: dict[int, dict[str, object]] = {}
    for b in sorted({row["b"] for row in states}):
        layer_cache[b] = scalar_component_bound(
            fixed_terms,
            b,
            shadows[b],
        )

    surviving: list[dict[str, object]] = []
    for state in states:
        lower = int(
            layer_cache[state["b"]][
                "minimum_central_rank_lower_bound"
            ]
        )
        if lower > state["h"]:
            continue
        surviving.append(
            {
                **route_for_state(fixed_terms, state),
                "component_central_rank_lower_bound": lower,
            }
        )

    route_histogram = Counter(str(row["route"]) for row in surviving)
    prolongation_histogram = Counter(
        int(row["sufficient_relative_prolongation_cap"])
        for row in surviving
        if row["sufficient_relative_prolongation_cap"] is not None
    )
    unresolved = [
        row
        for row in surviving
        if row["route"] != "quotient_budget_already_strict"
    ]

    summary = {
        "fixed_terms": fixed_terms,
        "central_projection_cap": projection_cap(fixed_terms),
        "central_intersection_range": [
            central_intersection_lower(fixed_terms),
            upper,
        ],
        "initial_state_count": len(states),
        "component_excluded_state_count": len(states) - len(surviving),
        "state_count_after_component_pruning": len(surviving),
        "unresolved_state_count": len(unresolved),
        "unresolved_b_range": (
            [
                min(int(row["b"]) for row in unresolved),
                max(int(row["b"]) for row in unresolved),
            ]
            if unresolved
            else None
        ),
        "route_histogram_after_component_pruning": dict(
            sorted(route_histogram.items())
        ),
        "prolongation_cap_histogram": {
            str(key): value
            for key, value in sorted(prolongation_histogram.items())
        },
        "maximum_required_quotient_gain_after_component_pruning": max(
            int(
                row[
                    "minimum_quotient_gain_for_strict_koszul_budget"
                ]
            )
            for row in surviving
        ),
        "maximum_structural_gain_deficit": max(
            (
                int(
                    row[
                        "minimum_quotient_gain_for_strict_koszul_budget"
                    ]
                )
                - int(row["maximum_possible_quotient_gain"])
                for row in surviving
                if row["route"]
                == "structural_exclusion_or_stronger_invariant_required"
            ),
            default=0,
        ),
    }
    return summary, list(layer_cache.values()), surviving


def build_payload() -> dict[str, object]:
    certificates = shadow_certificates()
    shadows = {
        int(row["dimension"]): int(
            row["integer_shadow_lower_bound"]
        )
        for row in certificates
    }

    summaries: list[dict[str, object]] = []
    full_layers: dict[str, list[dict[str, object]]] = {}
    full_states: dict[str, list[dict[str, object]]] = {}

    for fixed_terms in FIXED_TERM_CHOICES:
        summary, layers, states = fixed_q_payload(
            fixed_terms,
            shadows,
        )
        summaries.append(summary)
        full_layers[str(fixed_terms)] = layers
        full_states[str(fixed_terms)] = states

    expected = {
        4: (406, 146, 260, 254, 6, 60, 194),
        5: (325, 141, 184, 181, 3, 34, 147),
        6: (325, 146, 179, 176, 3, 35, 141),
    }
    for summary in summaries:
        fixed_terms = int(summary["fixed_terms"])
        routes = summary[
            "route_histogram_after_component_pruning"
        ]
        observed = (
            int(summary["initial_state_count"]),
            int(summary["component_excluded_state_count"]),
            int(summary["state_count_after_component_pruning"]),
            int(summary["unresolved_state_count"]),
            int(routes["quotient_budget_already_strict"]),
            int(routes["relative_prolongation_cap_can_close"]),
            int(
                routes[
                    "structural_exclusion_or_stronger_invariant_required"
                ]
            ),
        )
        if observed != expected[fixed_terms]:
            raise AssertionError((fixed_terms, observed))

    return {
        "status": "EXACT_LOWER25_FIXED_Q_ROUTE_DIAGNOSTIC_REPLAYED",
        "fixed_q_results": summaries,
        "route_selection": {
            "numerically_smallest_fixed_terms": 6,
            "fewest_unresolved_states": 176,
            "selected_for_proof": None,
            "verdict": "NO_COMPACT_FIXED_Q_FRONTIER",
        },
        "shadow_certificate_sha256": canonical_sha256(certificates),
        "layer_diagnostics_sha256": canonical_sha256(full_layers),
        "surviving_states_sha256": canonical_sha256(full_states),
        "claim_boundary": (
            "This is a route diagnostic under a hypothetical 24-term "
            "decomposition. It does not prove ChowRank(perm_6)>=25, "
            "does not prove any displayed relative-prolongation cap, "
            "and does not change the certified interval 24..32."
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
    print("N6_LOWER25_FIXED_Q_DIAGNOSTIC_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
