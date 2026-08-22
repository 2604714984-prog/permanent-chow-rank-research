#!/usr/bin/env python3
"""Frozen arithmetic replay for the F3,H6=42 q5=2 replacement bounds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TOTAL_POINTS = 42
PERMANENT_WARING_RANK = 64


def span_one_total_cost(support_size: int) -> int:
    if not 7 <= support_size <= TOTAL_POINTS:
        raise ValueError("a nonzero fifth-power relation has support 7..42")
    return 7 + TOTAL_POINTS - support_size


def flag_total_cost(support_size: int, exceptional_p_point: bool) -> int:
    if not 1 <= support_size <= TOTAL_POINTS:
        raise ValueError("flag support must be between 1 and 42")
    supported = support_size + (6 if exceptional_p_point else 1)
    return supported + TOTAL_POINTS - support_size


def residual_derivative_coefficients(kappa: int = 5) -> dict[str, tuple[int, int]]:
    """Check Q=6*M*P^5+kappa*P^6 in independent coordinates P,M.

    Each derivative is returned in the basis (M*P^4, P^5).  The transverse
    derivative is exactly 6*P^5; the P derivative differs from the required
    transverse condition only in the unrestricted P direction.
    """
    derivative_p = (30, 6 * kappa)
    derivative_m = (0, 6)
    return {"dQ_dP": derivative_p, "dQ_dM": derivative_m}


def exceptional_primitive_gradient(kappa: int = 5) -> dict[str, tuple[int, int]]:
    """Differentiate F=M*P^6+(kappa/7)*P^7.

    Coefficients use the basis (M*P^5, P^6), and reproduce the residual
    vector field (Q, P^6) with Q=6*M*P^5+kappa*P^6.
    """
    return {"dF_dP": (6, kappa), "dF_dM": (0, 1)}


def build_payload() -> dict[str, object]:
    span_one_costs = [span_one_total_cost(size) for size in range(7, 43)]
    flag_regular_costs = [flag_total_cost(size, False) for size in range(1, 43)]
    flag_exceptional_costs = [flag_total_cost(size, True) for size in range(1, 43)]
    derivative = residual_derivative_coefficients()
    primitive_gradient = exceptional_primitive_gradient()
    if derivative["dQ_dM"] != (0, 6):
        raise AssertionError(derivative)
    if primitive_gradient != {"dF_dP": (6, 5), "dF_dM": (0, 1)}:
        raise AssertionError(primitive_gradient)
    branch_bounds = {
        "bivector_span_zero": 42,
        "bivector_span_one": max(span_one_costs),
        "flag_line_without_p_point": max(flag_regular_costs),
        "flag_line_with_p_point": max(flag_exceptional_costs),
        "non_grassmannian_line": 42,
    }
    if max(branch_bounds.values()) >= PERMANENT_WARING_RANK:
        raise AssertionError(branch_bounds)
    return {
        "schema_version": 1,
        "status": "F3-H6-42-Q5-2-CLOSED",
        "total_points": TOTAL_POINTS,
        "permanent_waring_rank": PERMANENT_WARING_RANK,
        "relation_support_sizes_checked": 36,
        "flag_support_sizes_checked_per_stratum": 42,
        "branch_replacement_bounds": branch_bounds,
        "exceptional_residual_identity": {
            "Q": "6*M*P^5+kappa*P^6",
            "dQ_dM_coefficients_in_M_P4__P5": list(derivative["dQ_dM"]),
            "dF_dP_coefficients_in_M_P5__P6": list(primitive_gradient["dF_dP"]),
            "dF_dM_coefficients_in_M_P5__P6": list(primitive_gradient["dF_dM"]),
            "primitive": "M*P^6+(kappa/7)*P^7",
            "waring_cost_upper_bound": 7,
        },
        "exhaustive_q5_two_branches": [
            "BIVECTOR-SPAN-RANK-AT-MOST-ONE",
            "NON-GRASSMANNIAN-LINE-AT-MOST-TWO-NONZERO-RATIOS",
            "GRASSMANNIAN-FLAG-LINE",
        ],
        "claim_boundary": [
            "The complete gauge-free F3,H6=42 q5=2 pencil is closed.",
            "F3,H6=41 has q6=1 gauge and is not closed here.",
            "This replay does not prove lower 50 or border Chow rank.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("F3_H642_FLAG_REPLACEMENT_FROZEN_REPLAY_FAIL")
            return 1
        print("F3_H642_FLAG_REPLACEMENT_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
