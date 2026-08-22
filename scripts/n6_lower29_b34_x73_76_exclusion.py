#!/usr/bin/env python3
"""Exclude the complete residual seven-set x=73--76 plateau at b=34."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x73_76_exclusion.json"
N6081_DATA = ROOT / "data" / "n6_lower29_b34_first_shortening.json"
N6083_DATA = ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json"
N6089_DATA = ROOT / "data" / "n6_lower29_b34_x77_exclusion.json"
N6090_DATA = ROOT / "data" / "n6_product_shadow_b73_76_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def build_payload() -> dict[str, object]:
    n6081 = json.loads(N6081_DATA.read_text(encoding="utf-8"))
    n6083 = json.loads(N6083_DATA.read_text(encoding="utf-8"))
    n6089 = json.loads(N6089_DATA.read_text(encoding="utf-8"))
    n6090 = json.loads(N6090_DATA.read_text(encoding="utf-8"))
    require("x_A<=76 and f_A<=76" in n6089["strict_conclusion"], n6089)
    require(
        n6090["projective_globalization"][
            "every_73_to_76_plane_with_first_shadow_90_extends_to_an_80_plane_with_the_same_shadow"
        ],
        n6090,
    )
    require("f_A<=79" in n6083["strict_conclusion"], n6083)
    states = n6081["conditional_f80_state_pruning"]["states"]
    require(len(states) == 11, states)
    survivors = [state for state in states if state["existing_cap"] is None]
    require(
        len(survivors) == 1
        and survivors[0]["epsilon"] == [0] * 7
        and survivors[0]["kappa2"] == 0,
        survivors,
    )
    rows = []
    for dimension in range(76, 72, -1):
        delta = 80 - dimension
        for state in states:
            if state["existing_cap"] is not None:
                require(
                    int(state["required_prolongation_lower"]) + delta
                    > int(state["existing_cap"]),
                    (dimension, state),
                )
        fifteen_floor = 366 - dimension
        seven_floor = fifteen_floor - 8 * 20
        required = 400 + 140 - dimension
        require(required > 458, (dimension, required))
        rows.append(
            {
                "dimension": dimension,
                "exact_first_shadow_dimension": 90,
                "relation_state_count": len(states),
                "t_at_most_14_states_excluded_count": 10,
                "fifteen_set_literal_dimension_floor": fifteen_floor,
                "seven_set_literal_dimension_floor": seven_floor,
                "required_prolongation_lower": required,
                "alpha_at_most_two_cap": 458,
                "strict_cap_gap": required - 458,
                "unique_pre_geometry_state": {
                    "epsilon": [0] * 7,
                    "kappa2": 0,
                    "d2": 105,
                    "t2": 15,
                },
                "forced_literal_middle_dimension": 140,
                "forced_alpha": [3] * 7,
                "forced_a2": 90,
                "forced_common_W15": True,
                "n6090_extends_to_partitioned_80_to_90_product_locus": True,
                "n6083_actual_block_dichotomy_reapplies_because_dimension_is_greater_than_60": True,
                "excluded": True,
            }
        )
    return {
        "status": [
            "PURE_B34_SEVEN_SET_X73_TO_X76_EXCLUSION",
            "EXACT_RELATION_STATE_REPLAY",
            "N6-091",
        ],
        "input_after_n6089": "every residual seven-set has x_A<=76 and f_A<=76",
        "descending_plateau_exclusions": rows,
        "strict_conclusion": (
            "Every global b=34 survivor satisfies x_A<=72 and f_A<=72 for "
            "every residual seven-set A."
        ),
        "next_target": (
            "the dimension-72 first-product-shadow-89 locus and its defect-four actual packet"
        ),
        "claim_boundary": (
            "This excludes only the x_A=73 through 76 plateau. It does not classify the new "
            "72-to-89 equality locus, does not exclude global b=34, does not prove "
            "ChowRank(perm_6)>=29, and makes no border-rank claim."
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
    print("excluded_dimensions=73,74,75,76 unique_endpoint=common_W15")
    print("remaining_every_seven_set_x_and_f_at_most_72")
    print("N6_LOWER29_B34_X73_76_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
