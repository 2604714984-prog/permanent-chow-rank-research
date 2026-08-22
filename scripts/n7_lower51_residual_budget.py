#!/usr/bin/env python3
"""Exact arithmetic controls for the v7 residual middle budget."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def residual_cap(sum_all_middle: int, basis_middle: int) -> int:
    return sum_all_middle - 1225 - 2 * basis_middle


def build() -> dict:
    all_rank7 = residual_cap(50 * 35, 7 * 35)
    mixed_50_minimum = residual_cap(7 * 25 + 43 * 35, 7 * 25 + 35)
    mixed_49_endpoint = residual_cap(7 * 25 + 42 * 35, 7 * 25 + 35)
    assert (all_rank7, mixed_50_minimum, mixed_49_endpoint) == (35, 35, 0)

    mixed_controls = []
    for basis_cost in range(36):
        for outside_cost in range(36 - basis_cost):
            basis_middle = 210 + basis_cost
            sum_all_middle = basis_middle + 42 * 35 - outside_cost
            direct = residual_cap(sum_all_middle, basis_middle)
            budget = 35 - basis_cost - outside_cost
            assert direct == budget
            mixed_controls.append(
                {
                    "basis_cost": basis_cost,
                    "outside_cost": outside_cost,
                    "residual_cap": direct,
                }
            )
    assert len(mixed_controls) == 666
    return {
        "schema_version": 1,
        "all_rank7_50_residual_cap": all_rank7,
        "mixed_50_minimum_profile_residual_cap": mixed_50_minimum,
        "mixed_49_endpoint_residual_cap": mixed_49_endpoint,
        "mixed_budget_pairs_checked": len(mixed_controls),
        "mixed_controls": mixed_controls,
        "claim_boundary": (
            "These are dimension caps. They do not classify residual "
            "multiplication or assert that the cap is attained."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    print(json.dumps({k: payload[k] for k in payload if k != "mixed_controls"}, indent=2, sort_keys=True))
    print("N7_LOWER51_RESIDUAL_BUDGET_PASS")


if __name__ == "__main__":
    main()
