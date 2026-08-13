#!/usr/bin/env python3
"""Exclude the b=34 residual seven-set layers x=69,70,71 (N6-098)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x69_71_exclusion.json"
SHADOW_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"
N6081_SCRIPT = ROOT / "scripts" / "n6_lower29_b34_first_shortening.py"
N6093_DATA = ROOT / "data" / "n6_lower29_b34_x72_frontier.json"
N6096_DATA = ROOT / "data" / "n6_alpha2_t16_prolongation_cap.json"
N6064_DATA = ROOT / "data" / "n6_product_shadow_b50_equality_locus.json"
N6073_DATA = ROOT / "data" / "n6_product_shadow_b49_equality_locus.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_payload() -> dict[str, object]:
    n6081 = load_module(N6081_SCRIPT, "n6081_for_n6098")
    n6074 = load_module(n6081.N6074_SCRIPT, "n6074_for_n6098")
    n6080 = load_module(n6081.N6080_SCRIPT, "n6080_for_n6098")
    shadow = load_module(SHADOW_SCRIPT, "n6056_for_n6098")
    frontier = json.loads(N6093_DATA.read_text(encoding="utf-8"))
    alpha2 = json.loads(N6096_DATA.read_text(encoding="utf-8"))
    n6064 = json.loads(N6064_DATA.read_text(encoding="utf-8"))
    n6073 = json.loads(N6073_DATA.read_text(encoding="utf-8"))

    require(frontier["open_packet_count"] == 3, frontier)
    packet_names = [
        row["actual_refinement"]["name"]
        for row in frontier["open_actual_packets"]
    ]
    require(
        packet_names
        == [
            "direct_t16_packet",
            "one_quadratic_relation_common_W15_packet",
            "one_defective_term_t15_packet",
        ],
        packet_names,
    )
    require(
        alpha2["universal_alpha2_t16_prolongation_upper_cap"] == 464,
        alpha2,
    )
    require(
        n6064["second_product_shadow"][
            "boundary_second_shadows_remain_genuine_flag_hooks"
        ],
        n6064,
    )
    require(
        n6073["projective_globalization"][
            "every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"
        ]
        and n6073["projective_globalization"]["second_shadow_dimension"] == 23,
        n6073,
    )

    scalar_rows = n6081.local_state_rows(n6074, n6080, 89)
    expected_open = {
        ((0,) * 7, 0, 105, 16),
        ((0,) * 7, 1, 104, 15),
        ((0,) * 6 + (1,), 0, 104, 15),
    }
    layers = []
    for dimension in (71, 70, 69):
        open_rows = []
        for row in scalar_rows:
            required = int(row["required_prolongation_lower"]) + (80 - dimension)
            cap = row["existing_cap"]
            if cap is None or required <= int(cap):
                open_rows.append(row)
        require(
            {
                (
                    tuple(row["epsilon"]),
                    int(row["kappa2"]),
                    int(row["d2"]),
                    int(row["t2_upper"]),
                )
                for row in open_rows
            }
            == expected_open,
            (dimension, open_rows),
        )

        shortening_dimension = dimension - 20
        shadow_minimum, minimizer_count, witness, _ = shadow.minimum_ferrers_shadow(
            shortening_dimension
        )
        require(
            (shortening_dimension, shadow_minimum)
            in {(51, 78), (50, 75), (49, 75)},
            (shortening_dimension, shadow_minimum),
        )
        relation_cap = 6 * 15 - 15
        require(relation_cap == 75, relation_cap)
        if shortening_dimension == 51:
            route = "strict_product_shadow_78_greater_than_quadratic_relation_cap_75"
        elif shortening_dimension == 50:
            route = "N6_064_flag_hook_then_N6_069_and_N6_072"
        else:
            route = "N6_073_same_shadow_extension_then_N6_069_and_N6_072"
        layers.append(
            {
                "central_dimension": dimension,
                "scalar_state_count": len(scalar_rows),
                "existing_cap_excluded_count": len(scalar_rows) - len(open_rows),
                "remaining_packet_count_before_shortening": len(open_rows),
                "remaining_packets": packet_names,
                "direct_packet_alpha_at_most_two_cap": 464,
                "direct_packet_required_prolongation_lower": 540 - dimension,
                "direct_packet_survivor_forces_all_alpha_three": True,
                "one_relation_packet_omit_a_nonzero_relation_component": True,
                "one_defective_packet_omit_the_defective_term": True,
                "selected_six_quadratic_spaces_literal_direct": True,
                "selected_six_quadratic_dimension": 90,
                "selected_six_quotient_sum_dimension_floor": 15,
                "selected_six_permanent_relation_cap": relation_cap,
                "six_term_shortening_dimension": shortening_dimension,
                "product_shadow_minimum": shadow_minimum,
                "product_shadow_minimizer_count": minimizer_count,
                "product_shadow_first_minimizer": list(witness),
                "exclusion_route": route,
                "excluded": True,
            }
        )

    return {
        "status": [
            "PURE_B34_SEVEN_SET_X69_TO_X71_EXCLUSION",
            "EXACT_RELATION_STATE_AND_PRODUCT_SHADOW_REPLAY",
            "N6-098",
        ],
        "input_after_N6_097": "every residual seven-set has x_A<=71",
        "layer_exclusions": layers,
        "common_equality_consequence": {
            "at_shortening_dimensions_49_or_50_the_first_shadow_is_75": True,
            "the_selected_six_quotient_images_then_equal_one_common_W15": True,
            "the_five_anchored_section_differences_span_the_75_plane": True,
            "their_pair_shadows_force_transverse_six_dimensional_factor_spans": True,
            "N6_064_or_N6_073_makes_the_second_shadow_a_genuine_flag_hook": True,
            "an_invertible_row_or_column_block_is_excluded_by_N6_069_and_N6_059": True,
            "the_remaining_all_singular_branch_is_excluded_by_N6_072": True,
        },
        "updated_residual_seven_set_upper": 68,
        "strict_conclusion": (
            "The exact three-packet arithmetic persists at x_A=69,70,71. "
            "Six-term shortening and the N6-064/N6-073 flag-hook interfaces "
            "exclude all three layers. Hence every actual b=34 survivor has "
            "x_A<=68 for every residual seven-set."
        ),
        "claim_boundary": (
            "This excludes only x_A=69,70,71 after N6-097. The x_A<=68 "
            "layers and global b=34 remain open. It does not prove ordinary "
            "lower29 and makes no border-rank claim."
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
        require(
            payload == json.loads(args.verify_json.read_text(encoding="utf-8")),
            args.verify_json,
        )
    print("excluded_dimensions=69,70,71")
    print("updated_residual_seven_set_upper=68")
    print("N6_LOWER29_B34_X69_71_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
