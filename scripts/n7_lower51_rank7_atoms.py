#!/usr/bin/env python3
"""Freeze the exact rank-seven v7 atoms already justified at the handoff."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path


SURPLUS_BY_INCREMENT = (0, 22, 29, 26, 17, 14, 7, 0)
BOOLEAN_RANKS_BY_SUPPORT = {
    1: (20, 15),
    2: (20, 15),
    3: (26, 19),
    4: (26, 19),
    5: (30, 21),
    6: (30, 21),
    7: (35, 21),
}


def build() -> dict:
    support_rows = []
    for support, (degree4_rank, degree3_rank) in BOOLEAN_RANKS_BY_SUPPORT.items():
        surplus_floor = degree4_rank + max(0, degree3_rank - 3) - 10
        support_rows.append(
            {
                "support_size": support,
                "degree4_rank": degree4_rank,
                "degree3_rank": degree3_rank,
                "quadratic_intersection_loss_cap": 3,
                "rank_one_surplus_floor": surplus_floor,
            }
        )

    eight_positive_profiles = [
        profile
        for profile in combinations_with_replacement(range(1, 8), 8)
        if sum(profile) == 49
        and sum(SURPLUS_BY_INCREMENT[d] for d in profile) <= 35
    ]
    assert eight_positive_profiles == [(1, 6, 7, 7, 7, 7, 7, 7)]
    deficiency_costs = [
        Fraction(SURPLUS_BY_INCREMENT[d], 7 - d) for d in range(1, 7)
    ]
    assert min(deficiency_costs) == Fraction(11, 3)
    assert 14 * min(deficiency_costs) > 35

    return {
        "schema_version": 1,
        "claim": (
            "Exact accepted rank-seven local atoms for the N=50 defect program: "
            "the all-increment surplus row, rank-one support floors, and the unique "
            "eight-positive-increment profile under budget 35."
        ),
        "claim_boundary": (
            "This is not the complete all-rank local atom catalog and does not "
            "classify rank-six or lower-rank mixtures."
        ),
        "surplus_by_increment_0_through_7": list(SURPLUS_BY_INCREMENT),
        "rank_one_support_rows": support_rows,
        "unique_eight_positive_profile": list(eight_positive_profiles[0]),
        "nine_or_more_positive_increments_excluded_by_deficiency_cost": True,
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
    print(rendered, end="")
    print("N7_LOWER51_RANK7_ATOMS_PASS")


if __name__ == "__main__":
    main()
