#!/usr/bin/env python3
"""Exact audit for the average-six-subset lower bound for ``perm_6``.

The mathematical proof selects six terms by submodular averaging.  The only
finite interface checked here is the already established fixed-six central
pruning at intersection dimensions 54 through 64, plus the shadow cutoff at
65.  All arithmetic is over the integers and ``Fraction``.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb, factorial
from pathlib import Path


TOTAL_TERMS = 25
FIXED_TERMS = 6
PERM_CENTRAL_RANK = 400
TERM_CENTRAL_CAP = 20
FIXED_QUADRATIC_PROJECTION_CAP = 78


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def generalized_binomial(value: Fraction, degree: int) -> Fraction:
    result = Fraction(1)
    for index in range(degree):
        result *= value - index
    return result / factorial(degree)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def exact_shadow_certificate(dimension: int) -> dict[str, object]:
    """Certify the integer Bukh-shadow endpoint using rational separators."""

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


def macaulay_first_prolongation(value: int) -> int:
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def colored_partition_cap(total: int, colors: int) -> int:
    best = 0

    def visit(remaining: int, slots: int, lower: int, subtotal: int) -> None:
        nonlocal best
        if slots == 1:
            if remaining >= lower:
                best = max(
                    best,
                    subtotal + macaulay_first_prolongation(remaining),
                )
            return
        for value in range(lower, remaining + 1):
            visit(
                remaining - value,
                slots - 1,
                value,
                subtotal + macaulay_first_prolongation(value),
            )

    visit(total, colors, 0, 0)
    return best


def central_profile_lower(epsilon: int) -> int | None:
    quadratic_dimension = 15 - epsilon
    if quadratic_dimension in (15, 14):
        return 20
    if quadratic_dimension == 13:
        return 18
    if quadratic_dimension == 12:
        return None
    if quadratic_dimension == 11:
        return 14
    return 0


def central_layer(dimension: int) -> dict[str, object]:
    shadow = exact_shadow_certificate(dimension)
    shadow_lower = int(shadow["integer_shadow_lower_bound"])
    budget = FIXED_QUADRATIC_PROJECTION_CAP - shadow_lower
    require(0 <= budget <= 9, (dimension, budget))

    best: int | None = None
    minimizers: list[list[int]] = []
    feasible_profiles = 0
    for epsilon in combinations_with_replacement(range(16), FIXED_TERMS):
        if sum(epsilon) - min(epsilon) > budget:
            continue
        lowers = [central_profile_lower(value) for value in epsilon]
        if any(value is None for value in lowers):
            continue
        feasible_profiles += 1
        relation = budget - sum(epsilon) + min(epsilon)
        central_sum = sum(int(value) for value in lowers)
        lower = central_sum - 2 * macaulay_first_prolongation(relation)
        if best is None or lower < best:
            best = lower
            minimizers = [list(epsilon)]
        elif lower == best:
            minimizers.append(list(epsilon))

    require(best is not None, ("no feasible profile", dimension))
    residual_upper = min(120, 2 * dimension - 20)
    require(best > residual_upper, (dimension, best, residual_upper))
    return {
        "b": dimension,
        "shadow_lower_bound": shadow_lower,
        "shadow_lower_separator": shadow["lower_separator"],
        "shadow_upper_separator": shadow["upper_separator"],
        "quadratic_relation_budget": budget,
        "feasible_symmetric_profile_count": feasible_profiles,
        "central_rank_lower_bound": best,
        "residual_central_rank_upper_bound": residual_upper,
        "strict_margin": best - residual_upper,
        "minimizer_profiles": minimizers,
    }


def build_payload() -> dict[str, object]:
    for value in range(10):
        require(
            colored_partition_cap(value, FIXED_TERMS)
            == macaulay_first_prolongation(value),
            ("colored Macaulay interface", value),
        )

    layers = [central_layer(dimension) for dimension in range(54, 65)]
    cutoff = exact_shadow_certificate(65)
    require(
        cutoff["integer_shadow_lower_bound"]
        > FIXED_QUADRATIC_PROJECTION_CAP,
        cutoff,
    )

    # Fix a term of largest rank r.  Conditional submodular averaging over
    # six-subsets containing it gives
    # r + (5/24)(2D-R-r) >= r + (5/24)(800-24r) >= 260/3.
    conditional_average_floor = min(
        Fraction(largest_rank)
        + Fraction(FIXED_TERMS - 1, TOTAL_TERMS - 1)
        * (
            2 * (PERM_CENTRAL_RANK + largest_rank)
            - TOTAL_TERMS * largest_rank
            - largest_rank
        )
        for largest_rank in range(TERM_CENTRAL_CAP + 1)
    )
    require(conditional_average_floor == Fraction(260, 3), conditional_average_floor)
    selected_six_lower = (
        conditional_average_floor.numerator
        + conditional_average_floor.denominator
        - 1
    ) // conditional_average_floor.denominator
    require(selected_six_lower == 87, selected_six_lower)

    forced_intersection = (selected_six_lower + 20 + 1) // 2
    require(forced_intersection == 54, forced_intersection)

    return {
        "status": "EXACT_N6_LOWER26_AVERAGE_SUBSET_CERTIFICATE",
        "hypothetical_total_terms": TOTAL_TERMS,
        "selected_term_count": FIXED_TERMS,
        "conditional_six_subset_average_floor": str(conditional_average_floor),
        "selected_six_central_rank_lower_bound": selected_six_lower,
        "residual_forced_intersection_lower_bound": forced_intersection,
        "fixed_six_central_exclusion_layers": layers,
        "shadow_cutoff": {
            "first_excluded_b": 65,
            "shadow_lower_bound": cutoff["integer_shadow_lower_bound"],
            "quadratic_projection_cap": FIXED_QUADRATIC_PROJECTION_CAP,
            "lower_separator": cutoff["lower_separator"],
            "upper_separator": cutoff["upper_separator"],
        },
        "conclusion": {
            "ordinary_chow_rank_lower_bound": 26,
            "glynn_upper_bound": 32,
            "ordinary_chow_rank_interval": [26, 32],
        },
        "claim_boundary": (
            "The certificate proves an ordinary Chow-rank lower bound in "
            "characteristic zero. It does not prove border Chow rank at least 26 "
            "and does not determine the exact ordinary rank."
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
    print("N6_LOWER26_AVERAGE_SUBSET_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
