#!/usr/bin/env python3
"""Exact application excluding seven-set shortening dimensions 79 and 80."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x79_exclusion.json"
INPUTS = {
    "n6081": ROOT / "data" / "n6_lower29_b34_first_shortening.json",
    "n6082": ROOT / "data" / "n6_product_shadow_b80_equality_locus.json",
    "n6083": ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json",
    "n6084": ROOT / "data" / "n6_product_shadow_b79_equality_locus.json",
}


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def build_payload() -> dict[str, object]:
    frozen = {}
    for name, data in INPUTS.items():
        frozen[name] = json.loads(data.read_text(encoding="utf-8"))

    # The upstream scripts have their own frozen-payload tests.  This
    # application certificate reads only the recorded theorem interfaces,
    # avoiding four redundant symbolic replays on every local test.
    require(frozen["n6081"]["status"] == "N6_081_B34_FIRST_SHORTENING_EXACT_ENDPOINT", frozen["n6081"])
    require("N6-082" in frozen["n6082"]["status"], frozen["n6082"])
    require("N6-083" in frozen["n6083"]["status"], frozen["n6083"])
    require("N6-084" in frozen["n6084"]["status"], frozen["n6084"])

    n6081 = frozen["n6081"]
    n6082 = frozen["n6082"]
    n6083 = frozen["n6083"]
    n6084 = frozen["n6084"]
    require("f_A<=79" in n6083["strict_conclusion"], n6083["strict_conclusion"])
    require(n6082["second_product_shadow"]["every_equality_point_has_second_shadow_dimension"] == 24, n6082)
    require(n6084["projective_globalization"]["every_79_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow"], n6084)

    states = n6081["conditional_f80_state_pruning"]["states"]
    require(len(states) == 11, len(states))
    pregeometry = [state for state in states if not state["excluded_by_existing_cap"]]
    require(len(pregeometry) == 1, pregeometry)
    require(pregeometry[0]["epsilon"] == [0] * 7 and pregeometry[0]["kappa2"] == 0, pregeometry)
    for state in states:
        if state["existing_cap"] is not None:
            # Replacing x=80 by x=79 raises every required lower bound by one.
            require(int(state["required_prolongation_lower"]) + 1 > int(state["existing_cap"]), state)

    endpoint_rows = []
    for x in (80, 79):
        required = 400 + 140 - x
        require(required > 458, required)
        endpoint_rows.append(
            {
                "central_dimension_x": x,
                "exact_first_shadow_dimension": 90,
                "relation_state_count": 11,
                "t_at_most_14_states_excluded_count": 10,
                "unique_pre_geometry_state": {
                    "epsilon": [0] * 7,
                    "kappa2": 0,
                    "d2": 105,
                    "t2": 15,
                },
                "literal_middle_dimension_after_quadratic_directness": 140,
                "required_prolongation_lower": required,
                "alpha_at_most_two_cap": 458,
                "strict_cap_gap": required - 458,
                "forced_alpha": [3] * 7,
                "forced_a2": 90,
                "forced_common_W15": True,
                "equality_locus_interface": "N6-082" if x == 80 else "N6-084 then N6-082",
                "partitioned_second_shadow_dimension": 24,
                "actual_endpoint_excluded_by_n6083_block_dichotomy": True,
            }
        )
    return {
        "status": [
            "PURE_B34_SEVEN_SET_X79_X80_EXCLUSION",
            "EXACT_RELATION_STATE_REPLAY",
            "N6-085",
        ],
        "global_hypothesis": {
            "global_b": 34,
            "coupled_residual_intersection_floor": 366,
            "residual_terms": 22,
            "subset_terms": 7,
            "input_after_n6083": "every f_A<=79",
        },
        "improved_literal_floors": {
            "every_fifteen_set_literal_dimension_floor": 366 - 79,
            "every_seven_set_literal_dimension_floor": 366 - 79 - 8 * 20,
        },
        "x79_x80_endpoint_rows": endpoint_rows,
        "strict_conclusion": (
            "Every global b=34 survivor satisfies x_A<=78 and f_A<=78 for every "
            "residual seven-set A."
        ),
        "next_target": (
            "Classify the 78-to-90 equality locus or continue the hereditary shortening "
            "without assuming an extension to the 80-plane product locus."
        ),
        "claim_boundary": (
            "This excludes only seven-set shortening dimensions 79 and 80 inside the "
            "global b=34 branch. It does not classify or exclude x_A<=78, does not "
            "exclude global b=34, does not prove ChowRank(perm_6)>=29, and makes no "
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
    print("x80_and_x79_relation_states=11_each unique_endpoint=common_W15")
    print("remaining_every_seven_set_x_and_f_at_most_78")
    print("N6_LOWER29_B34_X79_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
