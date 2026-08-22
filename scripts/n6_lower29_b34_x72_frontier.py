#!/usr/bin/env python3
"""Exact defect-four scalar frontier at the b=34, x=72 layer."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x72_frontier.json"
N6081_SCRIPT = ROOT / "scripts" / "n6_lower29_b34_first_shortening.py"
N6091_DATA = ROOT / "data" / "n6_lower29_b34_x73_76_exclusion.json"
N6092_DATA = ROOT / "data" / "n6_product_shadow_b72_equality_locus.json"


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
    n6081 = load_module(N6081_SCRIPT, "n6081_for_n6093")
    n6074 = load_module(n6081.N6074_SCRIPT, "n6074_for_n6093")
    n6080 = load_module(n6081.N6080_SCRIPT, "n6080_for_n6093")
    n6091 = json.loads(N6091_DATA.read_text(encoding="utf-8"))
    n6092 = json.loads(N6092_DATA.read_text(encoding="utf-8"))
    require("x_A<=72 and f_A<=72" in n6091["strict_conclusion"], n6091)
    require(
        n6092["projective_globalization"][
            "every_72_to_89_point_lies_in_a_partitioned_80_to_90_product_parent"
        ],
        n6092,
    )
    rows = n6081.local_state_rows(n6074, n6080, 89)
    for row in rows:
        row["required_prolongation_lower_at_x72"] = int(row["required_prolongation_lower"]) + 8
        row["excluded_at_x72_by_existing_cap"] = (
            row["existing_cap"] is not None
            and row["required_prolongation_lower_at_x72"] > row["existing_cap"]
        )
    excluded = [row for row in rows if row["excluded_at_x72_by_existing_cap"]]
    open_rows = [row for row in rows if not row["excluded_at_x72_by_existing_cap"]]
    require((len(rows), len(excluded), len(open_rows)) == (21, 18, 3), open_rows)
    expected = {
        ((0,) * 7, 0, 105, 16),
        ((0,) * 7, 1, 104, 15),
        ((0,) * 6 + (1,), 0, 104, 15),
    }
    require(
        {
            (tuple(row["epsilon"]), int(row["kappa2"]), int(row["d2"]), int(row["t2_upper"]))
            for row in open_rows
        }
        == expected,
        open_rows,
    )
    open_packets = []
    for row in open_rows:
        epsilon = tuple(row["epsilon"])
        kappa2 = int(row["kappa2"])
        if epsilon == (0,) * 7 and kappa2 == 0:
            refinement = {
                "name": "direct_t16_packet",
                "seven_quadratic_spaces_literal_direct": True,
                "literal_middle_dimension": 140,
                "required_prolongation_lower": 468,
                "quotient_sum_dimension_upper": 16,
                "existing_t15_cap_does_not_apply_without_first_forcing_t2_at_most_15": True,
            }
        elif epsilon == (0,) * 7 and kappa2 == 1:
            refinement = {
                "name": "one_quadratic_relation_common_W15_packet",
                "quadratic_sum_dimension": 104,
                "quadratic_relation_dimension": 1,
                "required_prolongation_lower": 466,
                "epsilon_zero_alpha_at_most_two_subcases_excluded_by_cap_458": True,
                "forced_alpha": [3] * 7,
                "forced_t2": 15,
                "forced_a2": 89,
                "all_seven_quotient_images_equal_one_common_W15": True,
            }
        else:
            refinement = {
                "name": "one_defective_term_t15_packet",
                "epsilon": list(epsilon),
                "quadratic_sum_dimension": 104,
                "required_prolongation_lower": 468,
                "six_epsilon_zero_terms_forced_alpha_three": True,
                "positive_epsilon_term_alpha_floor": 2,
                "positive_epsilon_term_quotient_dimension_options": [13, 14, 15],
                "forced_t2": 15,
            }
        open_packets.append({"state": row, "actual_refinement": refinement})

    return {
        "status": [
            "EXACT_B34_X72_DEFECT_FOUR_SCALAR_FRONTIER",
            "THREE_ACTUAL_PACKETS_REMAIN_OPEN",
            "N6-093",
        ],
        "input_after_n6091": "every residual seven-set has x_A<=72 and f_A<=72",
        "x72_geometry_from_n6092": {
            "first_shadow_dimension": 89,
            "second_shadow_dimension": 24,
            "lies_in_partitioned_80_to_90_product_parent": True,
            "missing_quadratic_hyperplane_direction_is_boolean_not_assumed_to_transport_actual_frames": True,
        },
        "scalar_state_count": len(rows),
        "existing_cap_excluded_count": len(excluded),
        "open_packet_count": len(open_packets),
        "all_states": rows,
        "open_actual_packets": open_packets,
        "strict_conclusion": (
            "The x_A=72 layer is reduced to three displayed actual packets; it is not excluded."
        ),
        "next_target": (
            "Use the product second shadow and the missing-quadratic-cell geometry to exclude, "
            "first, the one-relation common-W15 packet, then the one-defective-term and t16 packets."
        ),
        "claim_boundary": (
            "This is a scalar and equality-locus frontier, not an exclusion of x_A=72 or global "
            "b=34. It does not prove ChowRank(perm_6)>=29 and makes no border-rank claim."
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
    print("x72_states=21 excluded=18 open=3")
    print("open_packets=direct_t16,one_relation_common_W15,one_defective_term_t15")
    print("N6_LOWER29_B34_X72_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
