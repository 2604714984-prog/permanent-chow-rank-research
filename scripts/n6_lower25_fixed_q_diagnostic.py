#!/usr/bin/env python3
"""Exact fixed-q route diagnostic for a hypothetical 24-term decomposition.

The current theorem excludes 23 terms and proves ChowRank(perm_6)>=24.
This script asks whether the same fixed-term arithmetic gives a compact
route to excluding 24 terms. It tests q=4,5,6 fixed terms using:

* exact rational Bukh-shadow separators;
* the symmetric middle-catalectic residual inequality;
* componentwise Macaulay prolongation when it can exclude states;
* the quotient-Koszul gain budget.

The output is a route diagnostic only. It does not prove a lower bound of
25 and deliberately leaves broad structural state sets unresolved.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

TOTAL_TERMS = 24
PERMANENT_CENTRAL_RANK = 400
PERMANENT_KOSZUL_RANK = 14_175
PER_TERM_CENTRAL_CAP = 20
PER_TERM_KOSZUL_CAP = 705
PER_TERM_QUADRATIC_CAP = 15
PER_TERM_INTERSECTION_CAP = 3
AMBIENT_VARIABLES = 36
FIXED_TERM_COUNTS = (4, 5, 6)

CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION: dict[int, int | None] = {
    15: 20,
    14: 20,
    13: 18,
    12: None,
    11: 14,
    10: 0,
}

# Each pair (x,m) exactly certifies
# binom(x,3)^2 < b and binom(x,2)^2 > m-1,
# hence every b-dimensional central space has quadratic shadow at least m.
SHADOW_CERTIFICATES: dict[int, tuple[Fraction, int]] = {
    1: (Fraction(3, 1), 9),
    2: (Fraction(16, 5), 13),
    3: (Fraction(10, 3), 16),
    4: (Fraction(24, 7), 18),
    5: (Fraction(7, 2), 20),
    6: (Fraction(25, 7), 22),
    7: (Fraction(51, 14), 24),
    8: (Fraction(48, 13), 25),
    9: (Fraction(56, 15), 27),
    10: (Fraction(91, 24), 29),
    11: (Fraction(65, 17), 30),
    12: (Fraction(27, 7), 31),
    13: (Fraction(82, 21), 33),
    14: (Fraction(55, 14), 34),
    15: (Fraction(83, 21), 35),
    16: (Fraction(167, 42), 36),
    17: (Fraction(145, 36), 38),
    18: (Fraction(77, 19), 39),
    19: (Fraction(53, 13), 40),
    20: (Fraction(41, 10), 41),
    21: (Fraction(33, 8), 42),
    22: (Fraction(29, 7), 43),
    23: (Fraction(25, 6), 44),
    24: (Fraction(46, 11), 45),
    25: (Fraction(21, 5), 46),
    26: (Fraction(38, 9), 47),
    27: (Fraction(17, 4), 48),
    28: (Fraction(64, 15), 49),
    29: (Fraction(30, 7), 50),
    30: (Fraction(43, 10), 51),
    31: (Fraction(69, 16), 52),
    32: (Fraction(13, 3), 53),
    33: (Fraction(74, 17), 54),
    34: (Fraction(83, 19), 55),
    35: (Fraction(57, 13), 56),
    36: (Fraction(317, 72), 57),
    37: (Fraction(53, 12), 57),
    38: (Fraction(31, 7), 58),
    39: (Fraction(40, 9), 59),
    40: (Fraction(49, 11), 60),
    41: (Fraction(76, 17), 61),
    42: (Fraction(139, 31), 62),
    43: (Fraction(139, 31), 62),
    44: (Fraction(9, 2), 63),
    45: (Fraction(95, 21), 64),
    46: (Fraction(68, 15), 65),
    47: (Fraction(141, 31), 66),
    48: (Fraction(41, 9), 66),
    49: (Fraction(32, 7), 67),
    50: (Fraction(87, 19), 68),
    51: (Fraction(124, 27), 69),
    52: (Fraction(23, 5), 69),
    53: (Fraction(60, 13), 70),
    54: (Fraction(37, 8), 71),
    55: (Fraction(51, 11), 72),
    56: (Fraction(51, 11), 72),
    57: (Fraction(93, 20), 73),
    58: (Fraction(14, 3), 74),
    59: (Fraction(276, 59), 75),
    60: (Fraction(75, 16), 75),
    61: (Fraction(61, 13), 76),
    62: (Fraction(80, 17), 77),
    63: (Fraction(33, 7), 77),
    64: (Fraction(85, 18), 78),
    65: (Fraction(71, 15), 79),
}


def generalized_binomial(value: Fraction, order: int) -> Fraction:
    result = Fraction(1)
    for index in range(order):
        result *= value - index
    return result / factorial(order)


def verify_shadow_certificates() -> dict[str, dict[str, object]]:
    table: dict[str, dict[str, object]] = {}
    previous = 0
    for dimension, (separator, shadow_lower) in SHADOW_CERTIFICATES.items():
        cubic_size = generalized_binomial(separator, 3) ** 2
        quadratic_size = generalized_binomial(separator, 2) ** 2
        if not cubic_size <= dimension:
            raise AssertionError((dimension, separator, cubic_size))
        if not quadratic_size > shadow_lower - 1:
            raise AssertionError((dimension, separator, quadratic_size))
        if shadow_lower < previous:
            raise AssertionError((dimension, shadow_lower, previous))
        previous = shadow_lower
        table[str(dimension)] = {
            "separator": str(separator),
            "binom_separator_3_squared": str(cubic_size),
            "binom_separator_2_squared": str(quadratic_size),
            "integer_shadow_lower_bound": shadow_lower,
        }
    return table


def macaulay_successor_degree_two(value: int) -> int:
    if value < 0:
        raise ValueError(value)
    if value == 0:
        return 0

    remaining = value
    upper = 10**9
    expansion: list[tuple[int, int]] = []
    for degree in (2, 1):
        index = degree - 1
        while index + 1 < upper and comb(index + 1, degree) <= remaining:
            index += 1
        expansion.append((index, degree))
        remaining -= comb(index, degree)
        upper = index

    if remaining != 0:
        raise AssertionError((value, expansion, remaining))
    return sum(
        comb(index + 1, degree + 1)
        for index, degree in expansion
    )


def central_rank_lower(quadratic_dimension: int) -> int | None:
    if quadratic_dimension in CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION:
        return CENTRAL_RANK_LOWER_BY_QUADRATIC_DIMENSION[
            quadratic_dimension
        ]
    if quadratic_dimension <= 10:
        return 0
    raise AssertionError(quadratic_dimension)


def projection_cap(fixed_terms: int) -> int:
    return (
        (fixed_terms - 1) * PER_TERM_QUADRATIC_CAP
        + PER_TERM_INTERSECTION_CAP
    )


def central_intersection_lower(fixed_terms: int) -> int:
    return max(
        0,
        PERMANENT_CENTRAL_RANK
        - (TOTAL_TERMS - fixed_terms) * PER_TERM_CENTRAL_CAP
    )


def central_intersection_upper(fixed_terms: int) -> int:
    cap = projection_cap(fixed_terms)
    start = max(20, central_intersection_lower(fixed_terms))
    for dimension in range(start, max(SHADOW_CERTIFICATES) + 1):
        if SHADOW_CERTIFICATES[dimension][1] > cap:
            return dimension - 1
    raise AssertionError(("shadow table too short", fixed_terms, cap))


def shadow_lower(dimension: int) -> int:
    if dimension == 0:
        return 0
    return SHADOW_CERTIFICATES[dimension][1]


def feasible_epsilon_profiles(
    fixed_terms: int,
    defect_budget: int,
) -> list[tuple[int, ...]]:
    maximum_total = (
        fixed_terms * defect_budget // (fixed_terms - 1)
    )
    profiles: list[tuple[int, ...]] = []

    def rec(prefix: tuple[int, ...], total: int) -> None:
        if len(prefix) == fixed_terms:
            if all(total - value <= defect_budget for value in prefix):
                profiles.append(prefix)
            return
        remaining_capacity = maximum_total - total
        for value in range(min(PER_TERM_QUADRATIC_CAP, remaining_capacity) + 1):
            rec(prefix + (value,), total + value)

    rec((), 0)
    return profiles


def component_central_lower_bound(
    fixed_terms: int,
    intersection_dimension: int,
    quadratic_shadow_lower: int,
) -> dict[str, object]:
    cap = projection_cap(fixed_terms)
    defect_budget = cap - quadratic_shadow_lower
    if defect_budget < 0:
        raise AssertionError(
            (fixed_terms, intersection_dimension, defect_budget)
        )

    all_zero_relation_cap = defect_budget
    all_zero_lower = max(
        0,
        fixed_terms * PER_TERM_CENTRAL_CAP
        - 2
        * (fixed_terms - 1)
        * macaulay_successor_degree_two(all_zero_relation_cap),
    )

    # The all-zero profile is feasible. If even its lower bound is not
    # above b, component arithmetic cannot universally exclude the lowest
    # h=b state. Returning zero is conservative and avoids a broad,
    # logically irrelevant enumeration.
    if all_zero_lower <= intersection_dimension:
        return {
            "certified_lower_bound": 0,
            "exact_profile_optimization_performed": False,
            "all_zero_profile_lower_bound": all_zero_lower,
            "defect_budget": defect_budget,
            "reason": (
                "The feasible all-zero profile already has lower bound "
                "at most b, so component arithmetic cannot exclude every "
                "state in this layer."
            ),
        }

    minimum: int | None = None
    minimizers: list[tuple[int, ...]] = []
    retained_profiles = 0
    impossible_dimension_twelve_profiles = 0

    for epsilon in feasible_epsilon_profiles(
        fixed_terms,
        defect_budget,
    ):
        quadratic_dimensions = [
            PER_TERM_QUADRATIC_CAP - value for value in epsilon
        ]
        if 12 in quadratic_dimensions:
            impossible_dimension_twelve_profiles += 1
            continue

        # For fixed epsilon, alpha=0 maximizes the quadratic relation cap
        # and therefore minimizes the certified central-rank lower bound.
        relation_cap = (
            sum(quadratic_dimensions)
            - quadratic_shadow_lower
            - max(12 - value for value in epsilon)
        )
        if relation_cap < 0:
            continue

        individual_lowers: list[int] = []
        for dimension in quadratic_dimensions:
            lower = central_rank_lower(dimension)
            if lower is None:
                raise AssertionError(dimension)
            individual_lowers.append(lower)

        relation_dimension_cap = (
            (fixed_terms - 1)
            * macaulay_successor_degree_two(relation_cap)
        )
        lower = max(
            0,
            sum(individual_lowers) - 2 * relation_dimension_cap,
        )
        retained_profiles += 1
        if minimum is None or lower < minimum:
            minimum = lower
            minimizers = [epsilon]
        elif lower == minimum:
            minimizers.append(epsilon)

    if minimum is None:
        raise AssertionError(
            (fixed_terms, intersection_dimension, defect_budget)
        )
    if minimizers != [(0,) * fixed_terms]:
        raise AssertionError(
            (fixed_terms, intersection_dimension, minimum, minimizers)
        )

    return {
        "certified_lower_bound": minimum,
        "exact_profile_optimization_performed": True,
        "all_zero_profile_lower_bound": all_zero_lower,
        "defect_budget": defect_budget,
        "retained_epsilon_profile_count": retained_profiles,
        "impossible_dimension_twelve_epsilon_profile_count": (
            impossible_dimension_twelve_profiles
        ),
        "unique_worst_epsilon_profile": list(minimizers[0]),
    }


def build_fixed_q_payload(fixed_terms: int) -> dict[str, object]:
    if fixed_terms not in FIXED_TERM_COUNTS:
        raise ValueError(fixed_terms)

    residual_terms = TOTAL_TERMS - fixed_terms
    b_min = central_intersection_lower(fixed_terms)
    b_max = central_intersection_upper(fixed_terms)
    cap = projection_cap(fixed_terms)

    layers: list[dict[str, object]] = []
    states: list[dict[str, object]] = []

    for b in range(b_min, b_max + 1):
        shadow = shadow_lower(b)
        component = component_central_lower_bound(
            fixed_terms,
            b,
            shadow,
        )
        central_lower = int(component["certified_lower_bound"])
        central_upper = 2 * b + 80 - 20 * fixed_terms
        d_max = min(
            fixed_terms * PER_TERM_CENTRAL_CAP - b,
            b + 80 - 20 * fixed_terms,
        )
        if d_max < 0:
            raise AssertionError((fixed_terms, b, d_max))

        layers.append(
            {
                "b": b,
                "quadratic_shadow_lower_bound": shadow,
                "projection_cap": cap,
                "central_rank_upper_from_residual": central_upper,
                "component_central_rank_lower": central_lower,
                "component_diagnostic": component,
                "d_range": [0, d_max],
            }
        )

        required_gain = (
            residual_terms * PER_TERM_KOSZUL_CAP
            + 1
            - (PERMANENT_KOSZUL_RANK - AMBIENT_VARIABLES * b)
        )

        for d in range(d_max + 1):
            h = b + d
            if h < central_lower:
                route = "component_central_rank_exclusion"
                prolongation_cap = None
            elif required_gain <= 0:
                route = "quotient_koszul_already_strict"
                prolongation_cap = None
            elif AMBIENT_VARIABLES * d < required_gain:
                route = "structural_exclusion_or_stronger_invariant_required"
                prolongation_cap = None
            else:
                route = "relative_prolongation_cap_can_close"
                prolongation_cap = (
                    AMBIENT_VARIABLES * d - required_gain
                )

            states.append(
                {
                    "b": b,
                    "d": d,
                    "h": h,
                    "minimum_quotient_gain_for_strict_koszul_budget": (
                        required_gain
                    ),
                    "maximum_possible_quotient_gain": (
                        AMBIENT_VARIABLES * d
                    ),
                    "relative_prolongation_cap_sufficient_for_closure": (
                        prolongation_cap
                    ),
                    "route": route,
                }
            )

    route_counts = Counter(row["route"] for row in states)
    surviving = [
        row
        for row in states
        if row["route"] != "component_central_rank_exclusion"
    ]
    p_caps = Counter(
        int(row["relative_prolongation_cap_sufficient_for_closure"])
        for row in surviving
        if row[
            "relative_prolongation_cap_sufficient_for_closure"
        ]
        is not None
    )
    structural = [
        row
        for row in surviving
        if row["route"]
        == "structural_exclusion_or_stronger_invariant_required"
    ]

    return {
        "fixed_terms": fixed_terms,
        "residual_terms": residual_terms,
        "projection_cap": cap,
        "central_intersection_range": [b_min, b_max],
        "state_count_before_component_exclusions": len(states),
        "route_counts": dict(sorted(route_counts.items())),
        "surviving_state_count": len(surviving),
        "surviving_b_range": [
            min(int(row["b"]) for row in surviving),
            max(int(row["b"]) for row in surviving),
        ],
        "relative_prolongation_cap_histogram": {
            str(key): value for key, value in sorted(p_caps.items())
        },
        "maximum_required_quotient_gain_among_survivors": max(
            int(row["minimum_quotient_gain_for_strict_koszul_budget"])
            for row in surviving
        ),
        "maximum_structural_gain_deficit": max(
            int(row["minimum_quotient_gain_for_strict_koszul_budget"])
            - int(row["maximum_possible_quotient_gain"])
            for row in structural
        ),
        "layers": layers,
        "states": states,
    }


def build_payload() -> dict[str, object]:
    shadow_table = verify_shadow_certificates()
    macaulay = {
        str(value): macaulay_successor_degree_two(value)
        for value in range(0, 23)
    }
    fixed_q = [
        build_fixed_q_payload(fixed_terms)
        for fixed_terms in FIXED_TERM_COUNTS
    ]

    expected_summary = {
        4: {
            "range": [0, 27],
            "states": 406,
            "survivors": 260,
            "routes": {
                "component_central_rank_exclusion": 146,
                "quotient_koszul_already_strict": 6,
                "relative_prolongation_cap_can_close": 60,
                "structural_exclusion_or_stronger_invariant_required": 194,
            },
            "p_caps": {"2": 20, "38": 20, "74": 20},
        },
        5: {
            "range": [20, 44],
            "states": 325,
            "survivors": 184,
            "routes": {
                "component_central_rank_exclusion": 141,
                "quotient_koszul_already_strict": 3,
                "relative_prolongation_cap_can_close": 34,
                "structural_exclusion_or_stronger_invariant_required": 147,
            },
            "p_caps": {"23": 17, "59": 17},
        },
        6: {
            "range": [40, 64],
            "states": 325,
            "survivors": 179,
            "routes": {
                "component_central_rank_exclusion": 146,
                "quotient_koszul_already_strict": 3,
                "relative_prolongation_cap_can_close": 35,
                "structural_exclusion_or_stronger_invariant_required": 141,
            },
            "p_caps": {"8": 17, "44": 18},
        },
    }

    for route in fixed_q:
        q = int(route["fixed_terms"])
        expected = expected_summary[q]
        observed = {
            "range": route["central_intersection_range"],
            "states": route["state_count_before_component_exclusions"],
            "survivors": route["surviving_state_count"],
            "routes": route["route_counts"],
            "p_caps": route["relative_prolongation_cap_histogram"],
        }
        if observed != expected:
            raise AssertionError((q, observed, expected))

    best_by_survivor_count = min(
        fixed_q,
        key=lambda row: int(row["surviving_state_count"]),
    )
    if int(best_by_survivor_count["fixed_terms"]) != 6:
        raise AssertionError(best_by_survivor_count)

    return {
        "status": "EXACT_LOWER25_FIXED_Q_ROUTE_DIAGNOSTIC_REPLAYED",
        "target": (
            "Test fixed-term arithmetic under a hypothetical 24-term "
            "decomposition of perm_6."
        ),
        "shadow_certificates": shadow_table,
        "macaulay_degree_two_successors": macaulay,
        "fixed_q_diagnostics": fixed_q,
        "route_selection": {
            "fewest_surviving_states_fixed_terms": 6,
            "fewest_surviving_states": 179,
            "fewest_structural_states": 141,
            "assessment": (
                "No tested fixed-term count produces a compact proof "
                "frontier. q=6 is numerically smallest, but it still leaves "
                "179 states, including 141 structural states, and its "
                "relative-prolongation caps 8 and 44 are tighter than the "
                "q=5 caps 23 and 59."
            ),
        },
        "conclusion": (
            "The lower-24 component-prolongation proof does not extend "
            "mechanically to a lower bound of 25. No fixed-q route is "
            "promoted beyond ROUTE_DIAGNOSTIC."
        ),
        "claim_boundary": (
            "This output does not exclude a 24-term decomposition, does "
            "not prove ChowRank(perm_6)>=25, and does not select q=6 as a "
            "proof program without an additional structural invariant."
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

    compact = {
        "status": payload["status"],
        "route_selection": payload["route_selection"],
        "conclusion": payload["conclusion"],
        "claim_boundary": payload["claim_boundary"],
    }
    print(json.dumps(compact, indent=2, sort_keys=True))
    print("N6_LOWER25_FIXED_Q_DIAGNOSTIC_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
