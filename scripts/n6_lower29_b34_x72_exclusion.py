#!/usr/bin/env python3
"""Exclude all three actual packets at the b=34, x=72 layer (N6-097)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x72_exclusion.json"
SHADOW_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"
N6093_DATA = ROOT / "data" / "n6_lower29_b34_x72_frontier.json"
N6094_DATA = ROOT / "data" / "n6_b34_x72_one_relation_exclusion.json"
N6096_DATA = ROOT / "data" / "n6_alpha2_t16_prolongation_cap.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_shadow_module():
    spec = importlib.util.spec_from_file_location("n6056_for_n6097", SHADOW_SCRIPT)
    require(spec is not None and spec.loader is not None, SHADOW_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def packet_by_name(frontier: dict[str, object], name: str) -> dict[str, object]:
    return next(
        packet
        for packet in frontier["open_actual_packets"]
        if packet["actual_refinement"]["name"] == name
    )


def build_payload() -> dict[str, object]:
    frontier = json.loads(N6093_DATA.read_text(encoding="utf-8"))
    relation = json.loads(N6094_DATA.read_text(encoding="utf-8"))
    alpha2_cap = json.loads(N6096_DATA.read_text(encoding="utf-8"))
    shadow = load_shadow_module()
    m52, minimizers, witness, _ = shadow.minimum_ferrers_shadow(52)
    require(m52 == 78, (m52, minimizers, witness))
    require(frontier["open_packet_count"] == 3, frontier)
    require(relation["actual_packet_excluded"], relation)

    direct = packet_by_name(frontier, "direct_t16_packet")
    defective = packet_by_name(frontier, "one_defective_term_t15_packet")
    direct_state = direct["state"]
    defective_state = defective["state"]
    require(
        direct_state["epsilon"] == [0] * 7
        and direct_state["kappa2"] == 0
        and direct_state["conservative_h_lower"] == 140,
        direct_state,
    )
    require(
        defective_state["epsilon"] == [0] * 6 + [1]
        and defective_state["kappa2"] == 0
        and defective_state["conservative_h_lower"] == 140,
        defective_state,
    )

    cap = int(alpha2_cap["universal_alpha2_t16_prolongation_upper_cap"])
    required = int(direct["actual_refinement"]["required_prolongation_lower"])
    require((cap, required, required - cap) == (464, 468, 4), (cap, required))

    total_cubic_dimension = 140
    omitted_term_cubic_capacity = 20
    six_term_shortening_floor = 72 - omitted_term_cubic_capacity
    require(six_term_shortening_floor == 52, six_term_shortening_floor)

    direct_all_alpha_three_quotient_floor = 15
    direct_six_quadratic_dimension = 6 * 15
    direct_relation_cap = (
        direct_six_quadratic_dimension
        - direct_all_alpha_three_quotient_floor
    )
    defective_common_quotient_dimension = 15
    defective_relation_dimension = 6 * 15 - defective_common_quotient_dimension
    require((direct_relation_cap, defective_relation_dimension) == (75, 75), (
        direct_relation_cap,
        defective_relation_dimension,
    ))
    require(m52 > direct_relation_cap, (m52, direct_relation_cap))

    return {
        "status": [
            "PURE_SIX_TERM_SHORTENING_EXCLUSION",
            "EXACT_T16_CAP_INTERFACE",
            "B34_X72_EXCLUDED",
            "N6-097",
        ],
        "input_frontier_packet_count": 3,
        "one_relation_packet_excluded_by_N6_094": True,
        "direct_packet": {
            "alpha_at_most_two_prolongation_cap_from_N6_096": cap,
            "required_prolongation_lower": required,
            "strict_cap_gap": required - cap,
            "remaining_case_after_cap": "all seven alpha values equal three",
            "six_selected_cubic_sum_dimension": 120,
            "x72_shortening_floor_after_omitting_one_term": (
                six_term_shortening_floor
            ),
            "six_selected_quadratic_sum_dimension": (
                direct_six_quadratic_dimension
            ),
            "six_selected_quotient_sum_dimension_floor": (
                direct_all_alpha_three_quotient_floor
            ),
            "six_selected_permanent_quadratic_intersection_cap": (
                direct_relation_cap
            ),
            "product_shadow_lower_m52": m52,
            "excluded": True,
        },
        "one_defective_packet": {
            "seven_cubic_spaces_literal_direct_dimension": (
                total_cubic_dimension
            ),
            "x72_shortening_floor_after_omitting_defective_term": (
                six_term_shortening_floor
            ),
            "six_full_quadratic_spaces_literal_direct_dimension": 90,
            "six_full_terms_common_quotient_dimension": (
                defective_common_quotient_dimension
            ),
            "six_full_permanent_quadratic_relation_dimension": (
                defective_relation_dimension
            ),
            "product_shadow_lower_m52": m52,
            "excluded": True,
        },
        "product_shadow_certificate": {
            "input_dimension": 52,
            "minimum": m52,
            "minimizing_ferrers_partition_count": minimizers,
            "first_minimizer": list(witness),
        },
        "x72_actual_layer_excluded": True,
        "updated_residual_seven_set_upper": 71,
        "strict_conclusion": (
            "N6-094 excludes the one-relation packet. N6-096 plus six-term "
            "shortening excludes the direct packet, and the same shortening "
            "excludes the one-defective packet. Hence an actual b=34 "
            "configuration has x_A<=71 for every residual seven-set."
        ),
        "claim_boundary": (
            "This excludes only the x_A=72 layer. Global b=34 and the "
            "remaining x_A<=71 layers are open. It does not prove ordinary "
            "lower29 or any border-rank bound."
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
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print("x72_packets=3 excluded=3")
    print("updated_residual_seven_set_upper=71")
    print("N6_LOWER29_B34_X72_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
