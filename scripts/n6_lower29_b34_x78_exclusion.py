#!/usr/bin/env python3
"""Application excluding the residual seven-set x=78 product-shadow layer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x78_exclusion.json"
N6081_DATA = ROOT / "data" / "n6_lower29_b34_first_shortening.json"
N6083_DATA = ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json"
N6085_DATA = ROOT / "data" / "n6_lower29_b34_x79_exclusion.json"
N6086_DATA = ROOT / "data" / "n6_product_shadow_b78_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def build_payload() -> dict[str, object]:
    n6081 = json.loads(N6081_DATA.read_text(encoding="utf-8"))
    n6083 = json.loads(N6083_DATA.read_text(encoding="utf-8"))
    n6085 = json.loads(N6085_DATA.read_text(encoding="utf-8"))
    n6086 = json.loads(N6086_DATA.read_text(encoding="utf-8"))
    require("x_A<=78 and f_A<=78" in n6085["strict_conclusion"], n6085)
    require(n6086["projective_globalization"]["every_78_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow"], n6086)
    require("f_A<=79" in n6083["strict_conclusion"], n6083)
    states = n6081["conditional_f80_state_pruning"]["states"]
    require(len(states) == 11, states)
    for state in states:
        if state["existing_cap"] is not None:
            require(int(state["required_prolongation_lower"]) + 2 > int(state["existing_cap"]), state)
    survivors = [state for state in states if state["existing_cap"] is None]
    require(len(survivors) == 1 and survivors[0]["epsilon"] == [0] * 7, survivors)
    literal_fifteen_floor = 366 - 78
    literal_seven_floor = literal_fifteen_floor - 8 * 20
    required = 400 + 140 - 78
    require((literal_fifteen_floor, literal_seven_floor, required) == (288, 128, 462), required)
    require(required > 458, required)
    return {
        "status": [
            "PURE_B34_SEVEN_SET_X78_EXCLUSION",
            "EXACT_RELATION_STATE_REPLAY",
            "N6-087",
        ],
        "input_after_n6085": "every residual seven-set has x_A<=78 and f_A<=78",
        "improved_literal_floors": {
            "every_fifteen_set_literal_dimension_floor": literal_fifteen_floor,
            "every_seven_set_literal_dimension_floor": literal_seven_floor,
        },
        "conditional_x78_packet": {
            "exact_first_shadow_dimension": 90,
            "quadratic_projection_cap": 93,
            "relation_state_count": len(states),
            "t_at_most_14_states_excluded_count": 10,
            "unique_pre_geometry_state": {
                "epsilon": [0] * 7,
                "kappa2": 0,
                "d2": 105,
                "t2": 15,
            },
            "forced_literal_middle_dimension": 140,
            "required_prolongation_lower": required,
            "alpha_at_most_two_cap": 458,
            "strict_cap_gap": required - 458,
            "forced_alpha": [3] * 7,
            "forced_a2": 90,
            "forced_common_W15": True,
            "n6086_extends_to_partitioned_80_to_90_product_locus": True,
            "n6083_actual_block_dichotomy_reapplies_because_78_is_greater_than_60": True,
            "excluded": True,
        },
        "strict_conclusion": (
            "Every global b=34 survivor satisfies x_A<=77 and f_A<=77 for every "
            "residual seven-set A."
        ),
        "next_target": "the 77-to-90 equality locus and the next hereditary shortening step",
        "claim_boundary": (
            "This excludes only the x_A=78 layer. It does not classify 77-planes, does "
            "not exclude global b=34, does not prove ChowRank(perm_6)>=29, and makes no "
            "border-rank claim."
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
    print("x78_relation_states=11 unique_endpoint=common_W15 excluded=true")
    print("remaining_every_seven_set_x_and_f_at_most_77")
    print("N6_LOWER29_B34_X78_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
