#!/usr/bin/env python3
"""Exact fixed-six integer frontier for a hypothetical 28-term decomposition.

This is the N6-074 arithmetic certificate.  It deliberately records the
open 75-shadow plateau at b=47,48,49; N6-072 applies only after the N6-064
fifty-plane flag-hook theorem and therefore does not remove those layers.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHADOW_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"
DEFAULT_JSON = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"

TOTAL_TERMS = 28
FIXED_TERMS = 6
RESIDUAL_TERMS = 22
PERMANENT_MIDDLE_RANK = 400
TERM_MIDDLE_CAP = 20
TERM_QUADRATIC_CAP = 15
E2_DIMENSION = 225
SIX_TERM_PROJECTION_CAP = 78


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def load_shadow_module():
    spec = importlib.util.spec_from_file_location("n6_shadow_n6074", SHADOW_SCRIPT)
    require(spec is not None and spec.loader is not None, SHADOW_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def macaulay_successor_degree_two(value: int) -> int:
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def individual_middle_lower(epsilon: int) -> int | None:
    dimension = TERM_QUADRATIC_CAP - epsilon
    if dimension in (15, 14):
        return 20
    if dimension == 13:
        return 18
    if dimension == 12:
        return None
    if dimension == 11:
        return 14
    if 0 <= dimension <= 10:
        return 0
    raise ValueError(epsilon)


def selection_lower(maximum_rank: int, b: int) -> int:
    """The N=28 fixed-six lower bound after eliminating z."""

    return ceiling(Fraction(4000 - 118 * maximum_rank - 10 * b, 17))


def residual_upper(maximum_rank: int, b: int) -> int:
    return 2 * b + RESIDUAL_TERMS * maximum_rank - PERMANENT_MIDDLE_RANK


def scalar_state_count(b: int, shadow: int) -> int:
    """Count symmetric (epsilon,kappa_2) states after the scalar bounds."""

    defect = SIX_TERM_PROJECTION_CAP - shadow
    lower = selection_lower(20, b)
    upper = residual_upper(20, b)
    count = 0
    for epsilon in combinations_with_replacement(range(16), FIXED_TERMS):
        omitted = sum(epsilon) - min(epsilon)
        if omitted > defect:
            continue
        middle = [individual_middle_lower(value) for value in epsilon]
        if any(value is None for value in middle):
            continue
        for kappa2 in range(defect - omitted + 1):
            profile_lower = sum(int(value) for value in middle) - 2 * macaulay_successor_degree_two(kappa2)
            if max(lower, profile_lower) <= upper:
                count += 1
    return count


def build_payload() -> dict[str, object]:
    shadow_module = load_shadow_module()

    @lru_cache(maxsize=None)
    def shadow(dimension: int) -> int:
        return int(shadow_module.minimum_ferrers_shadow(dimension)[0])

    low_rank_rows = []
    for rank, projection_cap in ((16, 58), (17, 58), (18, 68)):
        scalar_min = next(
            b
            for b in range(401)
            if selection_lower(rank, b) <= residual_upper(rank, b)
        )
        # The product-shadow minimum is monotone.  Stop at its first strict
        # excess instead of evaluating all 401 possible dimensions.
        shadow_max = next(
            b for b in range(401) if shadow(b) > projection_cap
        ) - 1
        require(scalar_min > shadow_max, (rank, scalar_min, shadow_max))
        low_rank_rows.append(
            {
                "maximum_middle_rank_r": rank,
                "scalar_feasibility_forces_b_at_least": scalar_min,
                "quadratic_projection_cap": projection_cap,
                "product_shadow_allows_b_at_most": shadow_max,
                "excluded": True,
            }
        )

    rank_twenty_rows = []
    for b in range(22, 53):
        exact_shadow = shadow(b)
        rank_twenty_rows.append(
            {
                "b": b,
                "selection_middle_rank_lower": selection_lower(20, b),
                "residual_middle_rank_upper": residual_upper(20, b),
                "exact_product_shadow_minimum": exact_shadow,
                "scalar_state_count": scalar_state_count(b, exact_shadow),
            }
        )
    require(rank_twenty_rows[0]["selection_middle_rank_lower"] == 84, rank_twenty_rows[0])
    require(rank_twenty_rows[0]["residual_middle_rank_upper"] == 84, rank_twenty_rows[0])

    literal_six_rows = []
    for b in range(22, 34):
        x_floor = 80 - b
        exact_shadow = shadow(x_floor)
        row: dict[str, object] = {
            "b": b,
            "literal_six_intersection_floor": x_floor,
            "exact_product_shadow_at_floor": exact_shadow,
            "six_term_projection_cap": SIX_TERM_PROJECTION_CAP,
        }
        if b <= 27:
            require(exact_shadow > SIX_TERM_PROJECTION_CAP, row)
            row["outcome"] = "excluded_by_strict_product_shadow"
        elif b in (28, 29):
            require(exact_shadow == SIX_TERM_PROJECTION_CAP, row)
            row["outcome"] = "excluded_by_defect_zero_common_W12_and_N6-044"
        elif b == 30:
            require((x_floor, exact_shadow) == (50, 75), row)
            row["outcome"] = "excluded_by_local_x_51_52_W12_or_local_x_50_N6-064_N6-072"
        elif b == 31:
            require((x_floor, exact_shadow) == (49, 75), row)
            row["outcome"] = "open_49_plane_75_shadow_plateau"
        else:
            require((b, x_floor, exact_shadow) in ((32, 48, 75), (33, 47, 75)), row)
            row["outcome"] = "open_75_shadow_plateau"
        literal_six_rows.append(row)

    q_frontier_rows = []
    for b in range(28, 47):
        candidates = []
        for q in range(1, 16):
            x_floor = 20 * q - 40 - b
            if x_floor <= 0:
                continue
            exact_shadow = shadow(x_floor)
            cap = 15 * q - 12
            candidates.append((cap - exact_shadow, -q, x_floor, exact_shadow, cap))
        defect, negative_q, x_floor, exact_shadow, cap = min(candidates)
        q = -negative_q
        q_frontier_rows.append(
            {
                "b": b,
                "best_q_before_ambient_cap_saturation": q,
                "literal_q_intersection_floor": x_floor,
                "exact_product_shadow_at_floor": exact_shadow,
                "q_term_projection_cap": cap,
                "nonnegative_shadow_defect": defect,
                "strict_shadow_contradiction": defect < 0,
            }
        )
    require(not any(row["strict_shadow_contradiction"] for row in q_frontier_rows), q_frontier_rows)

    high_layers = [
        {
            "b": b,
            "scalar_state_count": next(row["scalar_state_count"] for row in rank_twenty_rows if row["b"] == b),
            "status_after_existing_term_caps": (
                "one_all_alpha_three_state_remains_open"
                if b in (47, 48, 49)
                else "excluded_by_N6-064_and_N6-072"
                if b == 50
                else "excluded_by_defect_zero_t12_prolongation_cap"
            ),
        }
        for b in range(47, 53)
    ]

    return {
        "status": [
            "PURE_FIXED_SIX_REDUCTION",
            "EXACT_INTEGER_REPLAY",
            "LOWER_29_ARITHMETIC_FRONTIER",
            "N6-074",
        ],
        "hypothesis": {
            "ordinary_chow_decomposition_terms": TOTAL_TERMS,
            "fixed_terms": FIXED_TERMS,
            "residual_terms": RESIDUAL_TERMS,
            "base_field": "algebraically closed of characteristic zero",
        },
        "formulas": {
            "selection_lower": "ceil((4000-118*r-10*b)/17)",
            "residual_upper": "2*b+22*r-400",
            "literal_q_intersection_floor": "20*q-40-b",
            "q_projection_cap_before_ambient_saturation": "15*q-12",
        },
        "low_maximum_rank_branches": low_rank_rows,
        "rank_19_excluded_by": "N6-031",
        "maximum_middle_rank_forced": 20,
        "rank_twenty_scalar_window": [22, 52],
        "rank_twenty_rows": rank_twenty_rows,
        "literal_six_frontier": literal_six_rows,
        "strict_shadow_excluded_b": list(range(22, 28)),
        "proved_local_endpoint_exclusions": {
            "28": "x=52, defect zero, common W12, literal directness, N6-044",
            "29": "x=51 or 52, defect zero, common W12, literal directness, N6-044",
            "30": "x=51 or 52 as above; x=50 uses N6-064 and N6-072",
        },
        "q_frontier_before_ambient_cap_saturation": q_frontier_rows,
        "high_layers": high_layers,
        "excluded_b_after_current_proved_interfaces": list(range(22, 31)) + [50, 51, 52],
        "open_b_after_current_proved_interfaces": list(range(31, 50)),
        "next_geometric_frontiers": [
            "b=31: a hereditary 49-plane, 75-shadow common-W15 obstruction",
            "b=32,33: the 48- and 47-plane portions of the same 75-shadow plateau",
            "b=34,35: the q=7 floors 66 and 65 have shadow 87 against cap 93",
        ],
        "claim_boundary": (
            "This freezes the integer consequences and already proved local endpoint interfaces. "
            "It does not exclude b=31,...,49 or prove ChowRank(perm_6)>=29. In particular, "
            "N6-072 depends on the N6-064 fifty-plane flag-hook theorem and does not exclude "
            "the all-alpha-three b=47,48,49 layers. No 47-, 48-, or 49-plane equality "
            "classification is inferred from the product-shadow numbers alone."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print("low_r_excluded=16,17,18; r19=N6-031; r20_b=22..52")
    print("strict_shadow_excluded_b=22..27")
    print("proved_endpoint_excluded_b=28,29,30,50,51,52")
    print("open_b=31..49")
    print("N6_LOWER29_FIXED_SIX_ARITHMETIC_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
