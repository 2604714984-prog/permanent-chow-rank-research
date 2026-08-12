#!/usr/bin/env python3
"""Exact audit of the fixed-six off-central C_(4,2) interface.

The script uses only integers and ``Fraction``.  It proves a ceiling, rather
than a lower-27 theorem: the quadratic image of ``perm_6-R`` is contained in
``E_2+H_2``, whose dimension is at most ``315-Shadow(b)``.  It also replays
the current high-layer lower bounds for the quotient dimension ``t_2`` and
closes the endpoint ``b=64`` exactly.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INHERITED_N6032_DATA = ROOT / "data" / "n6_lower27_hereditary_residual_audit.json"


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
        lower_cubic = generalized_binomial(lower, 3) ** 2
        upper_cubic = generalized_binomial(upper, 3) ** 2
        if not lower_cubic < dimension < upper_cubic:
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


def macaulay_successor(value: int, degree: int) -> int:
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


HIGH_LAYER_H_LOWER = {
    52: 88,
    53: 92,
    54: 96,
    55: 98,
    56: 98,
    57: 100,
    58: 110,
    59: 112,
    60: 112,
    61: 116,
    62: 118,
    63: 118,
    64: 120,
}


def h_lower(intersection: int) -> int:
    if intersection in HIGH_LAYER_H_LOWER:
        return HIGH_LAYER_H_LOWER[intersection]
    first = Fraction(120) - Fraction(2 * intersection, 3)
    first_ceiling = (first.numerator + first.denominator - 1) // first.denominator
    return max(first_ceiling, 2 * intersection - 16)


def nondecreasing_profiles(total: int, length: int, minimum: int = 0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for value in range(minimum, total + 1):
        for tail in nondecreasing_profiles(total - value, length - 1, value):
            yield (value,) + tail


def exact_t2_lower(
    intersection: int, shadow: int
) -> tuple[int, dict[str, object]]:
    """Optimize the proved defect/Macaulay/Sylvester inequalities."""

    defect_budget = 78 - shadow
    central_cap = 120 - h_lower(intersection)
    best: int | None = None
    witness: dict[str, object] | None = None

    # The omitted-factor constraints give sum(eps)-min(eps)<=D.  Therefore
    # min(eps)<=D/5 and total sum<=D+min(eps), a tiny exact enumeration.
    for minimum in range(defect_budget // 5 + 1):
        for total in range(6 * minimum, defect_budget + minimum + 1):
            for profile in nondecreasing_profiles(total, 6, minimum):
                if profile[0] != minimum:
                    continue
                if sum(profile) - minimum > defect_budget:
                    continue
                # A sextic Chow term cannot have quadratic derivative rank 12.
                if 3 in profile:
                    continue
                kappa2 = defect_budget - sum(profile) + minimum
                rho3 = min(macaulay_successor(kappa2, 2), central_cap)
                kappa4 = macaulay_successor(rho3, 3)
                quadratic_capacity = 90 - sum(profile)
                fixed_intersection_upper = 78 - (sum(profile) - minimum)
                coupled_quadratic_lower = (
                    quadratic_capacity - kappa2 - kappa4
                )
                quotient_lower = max(
                    1, coupled_quadratic_lower - fixed_intersection_upper
                )
                if best is None or quotient_lower < best:
                    best = quotient_lower
                    witness = {
                        "sorted_quadratic_defects": list(profile),
                        "quadratic_relation_cap": kappa2,
                        "central_relation_cap": rho3,
                        "quartic_relation_cap": kappa4,
                        "quadratic_capacity": quadratic_capacity,
                        "fixed_intersection_upper": fixed_intersection_upper,
                        "coupled_quadratic_lower": coupled_quadratic_lower,
                    }
    require(best is not None and witness is not None, intersection)
    return best, witness


def build_payload() -> dict[str, object]:
    inherited = json.loads(INHERITED_N6032_DATA.read_text(encoding="utf-8"))
    inherited_high_layers = {
        int(row["b"]): int(row["central_rank_lower"])
        for row in inherited["fixed_six_high_layer_table"]
    }
    require(
        inherited_high_layers == HIGH_LAYER_H_LOWER,
        ("N6-032 high-layer mismatch", inherited_high_layers, HIGH_LAYER_H_LOWER),
    )
    rows: list[dict[str, object]] = []
    for intersection in range(45, 65):
        certificate = exact_shadow_certificate(intersection)
        shadow = int(certificate["integer_shadow_lower_bound"])
        quotient_lower, witness = exact_t2_lower(intersection, shadow)
        quotient_upper = 90 - shadow

        dual_certificate = exact_shadow_certificate(400 - intersection)
        quartic_intersection_upper = 225 - int(
            dual_certificate["integer_shadow_lower_bound"]
        )
        residual_quadratic_lower = max(
            203,
            225 + quotient_lower - quartic_intersection_upper,
        )
        residual_quadratic_upper = 225 + quotient_upper
        require(residual_quadratic_upper <= 251, intersection)
        require(residual_quadratic_upper < 300, intersection)

        rows.append(
            {
                "middle_intersection_b": intersection,
                "middle_rank_h_lower": h_lower(intersection),
                "fixed_middle_shadow_lower": shadow,
                "fixed_middle_shadow_certificate": certificate,
                "fixed_quadratic_quotient_t2_lower": quotient_lower,
                "fixed_quadratic_quotient_t2_upper": quotient_upper,
                "fixed_quartic_intersection_J4_upper": quartic_intersection_upper,
                "residual_C42_rank_lower_from_current_interfaces": (
                    residual_quadratic_lower
                ),
                "residual_C42_rank_upper_from_common_sum_space": (
                    residual_quadratic_upper
                ),
                "lower_optimization_witness": witness,
            }
        )

    endpoint = rows[-1]
    require(endpoint["middle_intersection_b"] == 64, endpoint)
    require(endpoint["middle_rank_h_lower"] == 120, endpoint)
    require(endpoint["fixed_middle_shadow_lower"] == 78, endpoint)
    require(endpoint["fixed_quadratic_quotient_t2_lower"] == 12, endpoint)
    require(endpoint["fixed_quadratic_quotient_t2_upper"] == 12, endpoint)
    require(endpoint["fixed_quartic_intersection_J4_upper"] == 22, endpoint)
    require(
        endpoint["residual_C42_rank_lower_from_current_interfaces"] == 215,
        endpoint,
    )
    require(
        endpoint["residual_C42_rank_upper_from_common_sum_space"] == 237,
        endpoint,
    )
    endpoint_witness = endpoint["lower_optimization_witness"]
    endpoint_d2_lower = int(endpoint_witness["coupled_quadratic_lower"])
    endpoint_d2_upper = 90
    require(endpoint_d2_lower == endpoint_d2_upper, endpoint_witness)
    endpoint_a2_lower = int(endpoint["fixed_middle_shadow_lower"])
    endpoint_a2_upper = int(endpoint_witness["fixed_intersection_upper"])
    require(endpoint_a2_lower == endpoint_a2_upper, endpoint_witness)
    endpoint_t2 = endpoint_d2_lower - endpoint_a2_lower
    require(
        endpoint_t2
        == endpoint["fixed_quadratic_quotient_t2_lower"]
        == endpoint["fixed_quadratic_quotient_t2_upper"],
        endpoint,
    )

    return {
        "status": "EXACT_N6_FIXED_SIX_OFFCENTRAL_C42_CEILING",
        "arithmetic": "exact integers and Fraction over Q",
        "conditional_on": "the N6-032 fixed-six reduction of a hypothetical 26-term decomposition of perm_6",
        "inherited_high_layers_verified_against": str(
            INHERITED_N6032_DATA.relative_to(ROOT)
        ).replace("\\", "/"),
        "rows": rows,
        "b64_endpoint": {
            "middle_intersection_b": 64,
            "middle_rank_h": endpoint["middle_rank_h_lower"],
            "fixed_quadratic_rank_d2": endpoint_d2_lower,
            "fixed_quadratic_intersection_a2": endpoint_a2_lower,
            "fixed_quadratic_quotient_t2": endpoint_t2,
            "fixed_quartic_intersection_J4_upper": endpoint[
                "fixed_quartic_intersection_J4_upper"
            ],
            "residual_C42_rank_window": [
                endpoint["residual_C42_rank_lower_from_current_interfaces"],
                endpoint["residual_C42_rank_upper_from_common_sum_space"],
            ],
        },
        "strict_route_conclusion": (
            "For every surviving b in 45..64, rank C_(4,2)(perm_6-R) "
            "is at most 315-Shadow(b), hence at most 251 and strictly below "
            "the twenty-term cap 300.  The proposed direct rank-above-300 "
            "endpoint cannot occur."
        ),
        "claim_boundary": (
            "This is a characteristic-zero consequence and a route ceiling, "
            "not a construction of Chow terms and not a proof of lower 27."
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
    print("N6_FIXED_SIX_OFFCENTRAL_C42_CEILING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
