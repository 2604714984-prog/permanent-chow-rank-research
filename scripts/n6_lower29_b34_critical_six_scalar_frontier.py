#!/usr/bin/env python3
"""Exact all-zero critical-six scalar frontier after N6-101 (N6-102)."""

from __future__ import annotations

import argparse
import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_critical_six_scalar_frontier.json"
N6080_DATA = ROOT / "data" / "n6_lower29_q7_defect_six_frontier.json"
N6100_DATA = ROOT / "data" / "n6_lower29_b34_x66_global_frontier.json"
N6101_DATA = ROOT / "data" / "n6_product_shadow_b46_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def global_epsilon_profiles(open_types: set[tuple[int, ...]]) -> list[tuple[int, ...]]:
    profiles = []
    for count_two in range(23):
        for count_one in range(23 - count_two):
            count_zero = 22 - count_one - count_two
            valid = True
            for take_two in range(min(count_two, 7) + 1):
                for take_one in range(min(count_one, 7 - take_two) + 1):
                    take_zero = 7 - take_two - take_one
                    if take_zero < 0 or take_zero > count_zero:
                        continue
                    row = (0,) * take_zero + (1,) * take_one + (2,) * take_two
                    if row not in open_types:
                        valid = False
            if valid:
                profiles.append((0,) * count_zero + (1,) * count_one + (2,) * count_two)
    return profiles


def critical_rows() -> list[dict[str, object]]:
    rows = []
    for kappa2 in range(4):
        d2 = 90 - kappa2
        for a2 in range(72, 76):
            t2 = d2 - a2
            if t2 < 15:
                continue
            rows.append(
                {
                    "kappa2": kappa2,
                    "d2": d2,
                    "a2": a2,
                    "t2": t2,
                    "all_six_alpha_equal_three_forced_by_existing_caps": t2 <= 16,
                    "common_W15_forced": t2 == 15,
                    "N6_101_second_shadow_classification_applies": a2 == 72,
                }
            )
    return rows


def build_payload() -> dict[str, object]:
    n6080 = json.loads(N6080_DATA.read_text(encoding="utf-8"))
    n6100 = json.loads(N6100_DATA.read_text(encoding="utf-8"))
    n6101 = json.loads(N6101_DATA.read_text(encoding="utf-8"))
    open_types = {
        tuple(row["epsilon"])
        for row in n6080["relation_envelope"]["states"]
        if not row["excluded"]
    }
    require(len(open_types) == 6, open_types)
    profiles = global_epsilon_profiles(open_types)
    expected = {
        (0,) * 22,
        (0,) * 21 + (1,),
        (0,) * 21 + (2,),
        (0,) * 20 + (1, 1),
        (0,) * 20 + (1, 2),
        (0,) * 19 + (1, 1, 1),
    }
    require(set(profiles) == expected, profiles)
    require(all(profile.count(0) >= 19 for profile in profiles), profiles)
    require(
        n6100["critical_six_shortening"]["therefore_selected_six_intersection_dimension"] == 46,
        n6100,
    )
    require(
        n6101["projective_globalization"][
            "every_46_plane_with_first_shadow_72_has_second_shadow_dimension"
        ]
        == 23,
        n6101,
    )
    rows = critical_rows()
    require(len(rows) == 10, rows)
    require(
        {(row["kappa2"], row["a2"], row["t2"]) for row in rows}
        == {
            (0, 72, 18), (0, 73, 17), (0, 74, 16), (0, 75, 15),
            (1, 72, 17), (1, 73, 16), (1, 74, 15),
            (2, 72, 16), (2, 73, 15),
            (3, 72, 15),
        },
        rows,
    )
    require(sum(row["N6_101_second_shadow_classification_applies"] for row in rows) == 4, rows)
    return {
        "status": [
            "PURE_GLOBAL_EPSILON_ZERO_CRITICAL_SIX_REDUCTION",
            "EXACT_TEN_STATE_SCALAR_FRONTIER",
            "N6-102",
        ],
        "global_epsilon_profiles": {
            "allowed_profile_count": len(profiles),
            "profiles": [list(profile) for profile in profiles],
            "every_profile_has_at_least_nineteen_epsilon_zero_terms": True,
            "therefore_an_all_epsilon_zero_residual_seven_set_exists": True,
        },
        "all_zero_seven_set": {
            "N6_080_relation_dimension_kappa7_range": [0, 3],
            "N6_099_selects_an_all_zero_six_subset_with_quadratic_permanent_relation_dimension_at_most": 75,
            "N6_100_forces_its_central_intersection_dimension": 46,
            "all_six_cubic_images_are_literal_direct_of_total_dimension": 120,
            "required_actual_term_prolongation_lower": 474,
        },
        "critical_six_scalar_states": rows,
        "state_summary": {
            "state_count": len(rows),
            "t2_histogram": {
                str(value): sum(row["t2"] == value for row in rows)
                for value in (15, 16, 17, 18)
            },
            "a2_histogram": {
                str(value): sum(row["a2"] == value for row in rows)
                for value in (72, 73, 74, 75)
            },
            "t2_at_most_16_forces_all_six_alpha_three_by_caps_at_most_464": True,
            "t2_equal_15_forces_one_common_W15": True,
            "a2_equal_72_states_are_classified_by_N6_101": 4,
        },
        "strict_conclusion": (
            "The critical six-set may be chosen with epsilon=0 on every term. "
            "Only ten (kappa2,a2,t2) scalar states remain.  The four a2=72 "
            "states have 23-dimensional second shadow of standard-flag or "
            "biflag-rectangle type by N6-101; the a2=73,74,75 states and the "
            "actual six-color realizability of the a2=72 states remain open."
        ),
        "next_target": (
            "Use the actual six Chow spaces and their quotient subspaces to "
            "exclude the ten critical states, treating standard and biflag "
            "23-dimensional second-shadow geometries separately."
        ),
        "claim_boundary": (
            "This is an exact scalar and geometric reduction, not an exclusion "
            "of b=34. N6-101 does not by itself exclude a critical six-color "
            "realization, and this certificate does not prove ordinary lower29, "
            "the exact rank, or a border-rank statement."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        require(payload == json.loads(args.verify_json.read_text(encoding="utf-8")), args.verify_json)
    print("global_epsilon_profiles=6 minimum_zero_terms=19")
    print("critical_all_zero_six_scalar_states=10")
    print("N6_LOWER29_B34_CRITICAL_SIX_SCALAR_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
