#!/usr/bin/env python3
"""Exact arithmetic for the perm_7 rectangular half-defect barrier.

The global implication is pure linear algebra.  The required two-sided
one-term half-defect inequality remains the explicit open interface.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_rectangular_half_defect_reduction.json"


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    maximum = total if maximum is None else min(maximum, total)
    for first in range(maximum, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def bounded_subset_coefficient(profile: tuple[int, ...], degree: int) -> int:
    coefficients = [1]
    for exponent in profile:
        updated = [0] * (len(coefficients) + exponent)
        for old_degree, value in enumerate(coefficients):
            for increment in range(exponent + 1):
                updated[old_degree + increment] += value
        coefficients = updated
    return coefficients[degree]


def middle_rank_floors() -> dict[int, dict[str, object]]:
    result: dict[int, dict[str, object]] = {}
    for factor_span in range(1, 8):
        candidates = [
            (bounded_subset_coefficient(profile, 3), profile)
            for profile in partitions(7)
            if len(profile) == factor_span
        ]
        rank, profile = min(candidates)
        result[factor_span] = {
            "minimum_middle_rank": rank,
            "minimizing_partition": list(profile),
            "profile_count": len(candidates),
        }
    return result


def build_payload() -> dict[str, object]:
    q = 35
    permanent_rank = q * q
    target_terms = 64
    factor_span_total = 49
    required_total = q * target_terms - permanent_rank
    required_slope = Fraction(required_total, factor_span_total)
    assert permanent_rank == 1225
    assert required_total == 1015
    assert required_slope == Fraction(145, 7)
    floors = middle_rank_floors()
    assert [floors[i]["minimum_middle_rank"] for i in range(1, 8)] == [
        1,
        2,
        4,
        8,
        15,
        25,
        35,
    ]
    full_quotient_symbol_capacity = 2 * q
    full_quotient_required = required_slope * 7
    assert full_quotient_symbol_capacity == 70
    assert full_quotient_required == 145
    return {
        "status": "PURE_SINGLE_MIDDLE_LAYER_ROUTE_BARRIER",
        "claim_boundary": (
            "The proposed two-sided local inequality is false already for a "
            "full-factor squarefree term at quotient rank seven. This excludes "
            "the route, not Chow rank 64."
        ),
        "middle_subset_rank_q": q,
        "permanent_rectangular_catalectic_rank": permanent_rank,
        "glynn_target_terms": target_terms,
        "factor_span_total": factor_span_total,
        "required_combined_excess": required_total,
        "required_two_sided_slope": str(required_slope),
        "combined_one_direction_capacity": q,
        "full_quotient_symbol_capacity": full_quotient_symbol_capacity,
        "full_quotient_required_by_linear_slope": str(full_quotient_required),
        "full_quotient_gap": str(full_quotient_symbol_capacity - full_quotient_required),
        "slope_below_capacity": False,
        "upper_template": "h_plus+h_minus <= 35*N - 1225 - Delta",
        "target_lower_template": "h_plus+h_minus >= 1015 - Delta",
        "middle_rank_floors_by_factor_span": {
            str(key): value for key, value in floors.items()
        },
        "next_open_interface": (
            "Construct a multi-degree coupled derivative-module invariant that "
            "continues to charge terms after the 49-dimensional factor span is full."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS: perm_7 rectangular reduction payload matches")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
