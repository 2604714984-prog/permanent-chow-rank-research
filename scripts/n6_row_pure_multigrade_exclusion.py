#!/usr/bin/env python3
"""Exact integer replay for the conditional N6-067 exclusion."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_row_pure_multigrade_exclusion.json"


def build_payload() -> dict[str, object]:
    rows = [
        {
            "row_support_dimension_r": r,
            "squarefree_row_cap": comb(r, 2),
            "row_pure_shadow_dimension": 6 * r,
            "can_contain_a_five_plane_Q": comb(r, 2) >= 5,
        }
        for r in range(1, 7)
    ]
    possible = [row for row in rows if row["can_contain_a_five_plane_Q"]]
    minimum_r = min(row["row_support_dimension_r"] for row in possible)
    minimum_shadow = min(
        row["row_pure_shadow_dimension"] for row in possible
    )
    assert minimum_r == 4
    assert minimum_shadow == 24
    assert [row["squarefree_row_cap"] for row in rows] == [0, 1, 3, 6, 10, 15]
    assert [row["row_pure_shadow_dimension"] for row in rows] == [
        6,
        12,
        18,
        24,
        30,
        36,
    ]

    return {
        "status": [
            "PURE_CONDITIONAL_ROW_PURE_MULTIGRADE_EXCLUSION",
            "EXACT_INTEGER_REPLAY",
            "N6-067",
        ],
        "hypothesis": {
            "flat_limit": "K0=Q tensor S0(C) is contained in E2",
            "row_factor_dimension": 5,
            "shared_column_frame_dimension": 15,
            "valuation_scope": (
                "Arbitrary valuation levels and rooted-tree shape are allowed "
                "only when the saturated seventy-five-plane has the stated "
                "row-pure tensor form."
            ),
        },
        "dimension_rows": rows,
        "minimum_row_support_dimension": minimum_r,
        "minimum_row_pure_shadow_dimension": minimum_shadow,
        "b50_equality_shadow_dimension": 23,
        "shadow_gap": minimum_shadow - 23,
        "strict_conclusion": (
            "A seventy-five-dimensional row-pure multigrade limit with five-"
            "dimensional row factor has derivative shadow at least twenty-four "
            "and cannot be the twenty-three-shadow b=50 equality limit."
        ),
        "claim_boundary": (
            "The result requires K0=Q tensor S0(C). It does not cover partial-"
            "rank Smith packets, column jets, different column frames across "
            "nodes, End(S0(C))-valued quotient gauges, arbitrary collision "
            "trees, the full b=50 endpoint, or lower twenty-eight."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("minimum_row_support", payload["minimum_row_support_dimension"])
    print("minimum_shadow", payload["minimum_row_pure_shadow_dimension"])
    print("b50_shadow", payload["b50_equality_shadow_dimension"])


if __name__ == "__main__":
    main()
