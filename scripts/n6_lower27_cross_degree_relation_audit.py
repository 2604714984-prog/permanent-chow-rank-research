#!/usr/bin/env python3
"""Exact arithmetic audit for the N6-037 cross-degree interfaces.

The mathematical statements are proved in
``docs/n6_lower27_cross_degree_relation_frontier.md``.  This script replays
the Macaulay successors, the Bukh-shadow integer endpoints, the fixed-six
dual-intersection table, and one aggregate integer state showing that the
current scalar inequalities do not yet exclude a hypothetical 26-term
decomposition.  The aggregate state is not a polynomial or Chow
decomposition.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def macaulay_successor(value: int, degree: int) -> int:
    """Return the exact degree-``degree`` Macaulay successor."""

    require(value >= 0 and degree >= 1, (value, degree))
    if value == 0:
        return 0
    remaining = value
    upper_bound: int | None = None
    expansion: list[tuple[int, int]] = []
    for lower in range(degree, 0, -1):
        if upper_bound is None:
            upper = lower
            while comb(upper + 1, lower) <= remaining:
                upper += 1
        else:
            upper = upper_bound - 1
            while upper >= lower and comb(upper, lower) > remaining:
                upper -= 1
        if upper >= lower and comb(upper, lower) <= remaining:
            expansion.append((upper, lower))
            remaining -= comb(upper, lower)
            upper_bound = upper
        else:
            upper_bound = upper
    require(remaining == 0, (value, degree, expansion, remaining))
    return sum(comb(upper + 1, lower + 1) for upper, lower in expansion)


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    result = Fraction(1)
    for index in range(degree):
        result *= value - index
    return result / factorial(degree)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def exact_shadow_certificate(dimension: int) -> dict[str, object]:
    """Certify the integer two-dimensional 3-to-2 Bukh shadow endpoint."""

    require(dimension > 0, dimension)
    for denominator in (10, 100, 1_000, 10_000, 100_000, 1_000_000):
        low = 2 * denominator
        high = 12 * denominator
        while low + 1 < high:
            middle = (low + high) // 2
            value = Fraction(middle, denominator)
            if generalized_binomial(value, 3) ** 2 < dimension:
                low = middle
            else:
                high = middle
        lower = Fraction(low, denominator)
        upper = Fraction(high, denominator)
        if not (
            generalized_binomial(lower, 3) ** 2
            < dimension
            < generalized_binomial(upper, 3) ** 2
        ):
            continue
        lower_shadow = generalized_binomial(lower, 2) ** 2
        upper_shadow = generalized_binomial(upper, 2) ** 2
        if floor_fraction(lower_shadow) != floor_fraction(upper_shadow):
            continue
        integer_lower = floor_fraction(lower_shadow) + 1
        if lower_shadow > integer_lower - 1 and upper_shadow < integer_lower:
            return {
                "dimension": dimension,
                "integer_shadow_lower_bound": integer_lower,
                "lower_separator": str(lower),
                "upper_separator": str(upper),
            }
    raise RuntimeError(("no exact shadow certificate", dimension))


def consistent_scalar_state() -> dict[str, object]:
    """Build and verify a nongeometric aggregate integer feasibility point."""

    fixed = {
        "middle_rank_h": 120,
        "middle_intersection_b": 64,
        "quadratic_rank": 90,
        "quadratic_intersection_a2": 78,
        "quartic_intersection_c4": 22,
    }
    residual = {
        "sum_individual_middle_ranks_C3": 400,
        "ordinary_middle_relation_dimension_rho3": 4,
        "middle_pairing_radical_dimension_delta3": 4,
        "coupled_middle_rank_g3": 392,
        "literal_middle_sum_dimension": 396,
        "coupled_middle_quotient_mod_E3": 56,
        "literal_middle_quotient_mod_E3": 60,
        "coupled_middle_intersection_with_E3": 336,
        "literal_middle_intersection_with_E3": 336,
        "colored_middle_quotient_relations": 340,
        "sum_individual_quadratic_ranks_C2": 300,
        "ordinary_quadratic_relation_dimension_kappa2": 75,
        "ordinary_quartic_relation_dimension_kappa4": 5,
        "literal_quadratic_sum_dimension": 225,
        "literal_quadratic_intersection_with_E2": 203,
        "colored_quadratic_quotient_relations": 278,
        "coupled_quadratic_rank": 220,
        "coupled_quadratic_intersection_with_E2": 203,
    }

    require(
        fixed["middle_rank_h"]
        >= 120 - Fraction(2 * fixed["middle_intersection_b"], 3),
        fixed,
    )
    require(fixed["middle_rank_h"] >= 2 * fixed["middle_intersection_b"] - 16, fixed)
    require(fixed["middle_rank_h"] <= 2 * fixed["middle_intersection_b"], fixed)
    require(45 <= fixed["middle_intersection_b"] <= 64, fixed)
    require(fixed["middle_rank_h"] - fixed["middle_intersection_b"] == 56, fixed)
    require(fixed["quadratic_rank"] - fixed["quadratic_intersection_a2"] == 12, fixed)
    require(fixed["quadratic_rank"] - fixed["quadratic_intersection_a2"] >= 1, fixed)
    require(fixed["quartic_intersection_c4"] <= 22, fixed)

    require(
        residual["coupled_middle_rank_g3"]
        == residual["sum_individual_middle_ranks_C3"]
        - residual["ordinary_middle_relation_dimension_rho3"]
        - residual["middle_pairing_radical_dimension_delta3"],
        residual,
    )
    require(
        residual["literal_middle_sum_dimension"]
        == residual["sum_individual_middle_ranks_C3"]
        - residual["ordinary_middle_relation_dimension_rho3"],
        residual,
    )
    require(
        residual["colored_middle_quotient_relations"]
        == residual["sum_individual_middle_ranks_C3"]
        - residual["literal_middle_quotient_mod_E3"],
        residual,
    )
    require(
        residual["coupled_middle_intersection_with_E3"]
        == residual["coupled_middle_rank_g3"]
        - residual["coupled_middle_quotient_mod_E3"],
        residual,
    )
    require(
        residual["literal_middle_intersection_with_E3"]
        == residual["literal_middle_sum_dimension"]
        - residual["literal_middle_quotient_mod_E3"],
        residual,
    )
    require(residual["coupled_middle_rank_g3"] >= 384, residual)
    require(
        residual["ordinary_middle_relation_dimension_rho3"]
        + residual["middle_pairing_radical_dimension_delta3"]
        <= 16,
        residual,
    )
    require(
        residual["ordinary_quartic_relation_dimension_kappa4"]
        <= macaulay_successor(
            residual["ordinary_middle_relation_dimension_rho3"], 3
        ),
        residual,
    )
    require(
        residual["literal_quadratic_sum_dimension"]
        == residual["sum_individual_quadratic_ranks_C2"]
        - residual["ordinary_quadratic_relation_dimension_kappa2"],
        residual,
    )
    require(
        residual["colored_quadratic_quotient_relations"]
        == residual["sum_individual_quadratic_ranks_C2"]
        - (
            residual["literal_quadratic_sum_dimension"]
            - residual["literal_quadratic_intersection_with_E2"]
        ),
        residual,
    )
    require(
        residual["colored_middle_quotient_relations"]
        <= macaulay_successor(
            residual["colored_quadratic_quotient_relations"], 2
        ),
        residual,
    )
    require(
        residual["coupled_quadratic_rank"]
        >= residual["sum_individual_quadratic_ranks_C2"]
        - residual["ordinary_quadratic_relation_dimension_kappa2"]
        - residual["ordinary_quartic_relation_dimension_kappa4"],
        residual,
    )
    require(
        residual["coupled_quadratic_rank"]
        >= 225
        + fixed["quadratic_rank"]
        - fixed["quadratic_intersection_a2"]
        - fixed["quartic_intersection_c4"],
        (fixed, residual),
    )
    require(
        residual["coupled_quadratic_intersection_with_E2"] >= 203,
        residual,
    )
    return {
        "classification": "AGGREGATE_INTEGER_DIAGNOSTIC_ONLY",
        "fixed_six": fixed,
        "twenty_term_residual": residual,
        "warning": (
            "This is not a family of Chow terms, a polynomial, or a geometric "
            "counterexample. It only shows simultaneous feasibility of the "
            "listed scalar rank, relation, shadow, and double-quotient bounds."
        ),
    }


def build_payload() -> dict[str, object]:
    shadow_336 = exact_shadow_certificate(336)
    require(shadow_336["integer_shadow_lower_bound"] == 203, shadow_336)

    fixed_six_table: list[dict[str, object]] = []
    for intersection in range(45, 65):
        annihilator_dimension = 400 - intersection
        certificate = exact_shadow_certificate(annihilator_dimension)
        shadow = int(certificate["integer_shadow_lower_bound"])
        fixed_six_table.append(
            {
                "middle_intersection_b": intersection,
                "dual_middle_annihilator_dimension": annihilator_dimension,
                "dual_quadratic_shadow_lower": shadow,
                "quartic_intersection_upper": 225 - shadow,
                "lower_separator": certificate["lower_separator"],
                "upper_separator": certificate["upper_separator"],
            }
        )

    minimum_k2_for_320 = next(
        value for value in range(321) if macaulay_successor(value, 2) >= 320
    )
    require(minimum_k2_for_320 == 74, minimum_k2_for_320)
    require(macaulay_successor(73, 2) == 314, "73 successor")
    require(macaulay_successor(74, 2) == 322, "74 successor")
    require(macaulay_successor(16, 3) == 25, "16 successor")

    return {
        "status": "EXACT_N6_LOWER27_CROSS_DEGREE_RELATION_FRONTIER",
        "arithmetic": "exact integers and Fraction over Q",
        "conditional_on": "a hypothetical 26-term Chow decomposition of perm_6",
        "twenty_term_residual": {
            "middle_rank_lower": 384,
            "sum_individual_middle_ranks_upper": 400,
            "ordinary_middle_relation_plus_radical_upper": 16,
            "ordinary_quartic_relation_upper": 25,
            "colored_middle_quotient_relation_lower": 320,
            "colored_quadratic_relation_lower_from_macaulay_only": 74,
            "colored_quadratic_relation_lower_from_shadow": 203,
            "middle_to_quadratic_shadow_certificate": shadow_336,
        },
        "macaulay_endpoint_checks": {
            "16_degree_3_successor": macaulay_successor(16, 3),
            "73_degree_2_successor": macaulay_successor(73, 2),
            "74_degree_2_successor": macaulay_successor(74, 2),
            "least_k_with_k_degree_2_successor_at_least_320": minimum_k2_for_320,
        },
        "fixed_six_dual_quartic_intersection_table": fixed_six_table,
        "scalar_nonclosure_witness": consistent_scalar_state(),
        "claim_boundary": (
            "The relation, shadow, and dual-intersection statements are exact "
            "characteristic-zero consequences. The integer state is diagnostic "
            "only. Nothing here excludes a 26-term decomposition, proves "
            "ChowRank(perm_6)>=27, or makes a border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("N6_LOWER27_CROSS_DEGREE_RELATION_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
