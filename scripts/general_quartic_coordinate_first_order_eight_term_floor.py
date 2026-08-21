#!/usr/bin/env python3
"""Arithmetic replay for the coordinate first-order eight-term floor."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TARGET_MATCHINGS = 24
LOCAL_BUDGET = 6
REQUIRED_GLOBAL_BUDGET = 2 * TARGET_MATCHINGS


def payload() -> dict[str, object]:
    floor = (REQUIRED_GLOBAL_BUDGET + LOCAL_BUDGET - 1) // LOCAL_BUDGET
    return {
        "schema": "general_quartic_coordinate_first_order_eight_term_floor/v1",
        "target_matching_count": TARGET_MATCHINGS,
        "minimum_required_global_budget": REQUIRED_GLOBAL_BUDGET,
        "maximum_local_budget": LOCAL_BUDGET,
        "minimum_component_count": floor,
        "q6_margin": REQUIRED_GLOBAL_BUDGET - 6 * LOCAL_BUDGET,
        "q7_margin": REQUIRED_GLOBAL_BUDGET - 7 * LOCAL_BUDGET,
        "conclusion": {
            "coordinate_regular_first_order_q_le_7": "IMPOSSIBLE",
            "coordinate_regular_first_order_q8_existence": "OPEN",
            "mu_6_4_exact_value": "OPEN_IN_[6,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = payload()
    assert result["minimum_component_count"] == 8
    assert result["q6_margin"] == 12
    assert result["q7_margin"] == 6
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print("GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_FLOOR_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
