#!/usr/bin/env python3
"""Exclude the defect-six b=34 layers x=67,68 (N6-099)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x67_68_exclusion.json"
N6080_SCRIPT = ROOT / "scripts" / "n6_lower29_q7_defect_six_frontier.py"
N6051_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
N6052_DATA = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"
N6095_DATA = ROOT / "data" / "n6_global_t16_prolongation_cap.json"
N6096_DATA = ROOT / "data" / "n6_alpha2_t16_prolongation_cap.json"
N6076_DATA = ROOT / "data" / "n6_product_shadow_b48_equality_locus.json"
N6078_DATA = ROOT / "data" / "n6_product_shadow_b47_equality_locus.json"
SHADOW_SCRIPT = ROOT / "scripts" / "n6_product_shadow_b53_64_exclusion.py"


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
    n6080 = load_module(N6080_SCRIPT, "n6080_for_n6099")
    shadow = load_module(SHADOW_SCRIPT, "n6056_for_n6099")
    n6051 = json.loads(N6051_DATA.read_text(encoding="utf-8"))
    n6052 = json.loads(N6052_DATA.read_text(encoding="utf-8"))
    n6095 = json.loads(N6095_DATA.read_text(encoding="utf-8"))
    n6096 = json.loads(N6096_DATA.read_text(encoding="utf-8"))
    n6076 = json.loads(N6076_DATA.read_text(encoding="utf-8"))
    n6078 = json.loads(N6078_DATA.read_text(encoding="utf-8"))
    require(n6051["characteristic_zero_prolongation_upper_cap_t15"] == 458, n6051)
    require(n6052["universal_alpha2_t15_prolongation_upper_cap"] == 458, n6052)
    require(n6095["characteristic_zero_prolongation_upper_cap_t16"] == 462, n6095)
    require(n6096["universal_alpha2_t16_prolongation_upper_cap"] == 464, n6096)
    require(n6080.cap_for_t_upper(14) == 453, n6080.cap_for_t_upper(14))
    require(
        n6076["projective_globalization"][
            "every_48_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"
        ],
        n6076,
    )
    require(
        n6078["projective_globalization"][
            "every_47_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"
        ],
        n6078,
    )

    envelope = n6080.build_payload()["relation_envelope"]
    rows = envelope["states"]
    open_rows = [row for row in rows if not row["excluded"]]
    require((len(rows), len(open_rows)) == (56, 13), (len(rows), len(open_rows)))
    t15_t16 = [row for row in open_rows if int(row["t2_upper"]) <= 16]
    high_t = [row for row in open_rows if int(row["t2_upper"]) >= 17]
    require((len(t15_t16), len(high_t)) == (10, 3), (t15_t16, high_t))
    require(
        {
            (tuple(row["epsilon"]), int(row["kappa2"]), int(row["t2_upper"]))
            for row in high_t
        }
        == {
            ((0,) * 7, 0, 18),
            ((0,) * 7, 1, 17),
            ((0,) * 6 + (1,), 0, 17),
        },
        high_t,
    )
    require(
        all(row["cubic_relations_forced_zero_by_no_pure_cube"] for row in high_t),
        high_t,
    )

    layers = []
    for dimension, extension_name in ((68, "N6_076"), (67, "N6_078")):
        shortening_dimension = dimension - 20
        shadow_minimum, minimizer_count, witness, _ = shadow.minimum_ferrers_shadow(
            shortening_dimension
        )
        require(
            (shortening_dimension, shadow_minimum) in {(48, 75), (47, 75)},
            (shortening_dimension, shadow_minimum),
        )
        required_by_state = {
            str(index): 400 + int(row["h_lower"]) - dimension
            for index, row in enumerate(open_rows)
        }
        require(
            all(
                required_by_state[str(index)]
                > (458 if int(row["t2_upper"]) == 15 else 464)
                for index, row in enumerate(open_rows)
                if int(row["t2_upper"]) <= 16
            ),
            required_by_state,
        )
        layers.append(
            {
                "central_dimension": dimension,
                "six_term_shortening_dimension": shortening_dimension,
                "product_shadow_minimum": shadow_minimum,
                "product_shadow_minimizer_count": minimizer_count,
                "product_shadow_first_minimizer": list(witness),
                "defect_six_relation_state_count": len(rows),
                "old_cap_excluded_count": len(rows) - len(open_rows),
                "pre_new_argument_state_count": len(open_rows),
                "t15_t16_state_count": len(t15_t16),
                "high_t_state_count": len(high_t),
                "required_prolongation_lower_by_open_state": required_by_state,
                "same_shadow_extension_interface": extension_name,
                "excluded": True,
            }
        )

    return {
        "status": [
            "PURE_B34_DEFECT_SIX_X67_X68_EXCLUSION",
            "EXACT_RELATION_ENVELOPE_REPLAY",
            "N6-099",
        ],
        "input_after_N6_098": "every residual seven-set has x_A<=68",
        "relation_envelope": {
            "state_count": len(rows),
            "old_cap_excluded_count": len(rows) - len(open_rows),
            "open_state_count_before_new_argument": len(open_rows),
            "t15_t16_states": len(t15_t16),
            "t17_t18_states": len(high_t),
        },
        "low_t_argument": {
            "t15_alpha_zero_or_one_cap_from_N6_051": 458,
            "t15_alpha_two_cap_from_N6_052": 458,
            "t16_alpha_zero_or_one_cap_from_N6_095": 462,
            "t16_alpha_two_cap_from_N6_096": 464,
            "strict_caps_force_every_epsilon_zero_term_to_have_alpha_three": True,
            "every_six_term_deletion_retains_a_full_fifteen_dimensional_quotient_image": True,
            "six_term_permanent_relation_dimension_is_at_most_75": True,
        },
        "quotient_deletion_loss_lemma": {
            "statement": (
                "For subspaces Q_1,...,Q_7 with total span dimension t, put "
                "delta_j=t-dim(sum_{i not equal j}Q_i). Then sum_j delta_j<=t."
            ),
            "dual_proof": (
                "The dual spaces supported only on color j are linearly direct: "
                "restricting a relation among them to Q_j kills every other summand."
            ),
        },
        "high_t_arguments": {
            "all_three_high_t_states_have_seven_literal_direct_twenty_dimensional_cubic_spaces": True,
            "direct_t17_t18": (
                "Some deletion has loss at most floor(t/7)<=2, hence the retained "
                "quotient span has dimension at least 15."
            ),
            "one_relation_t17": (
                "If every deletion had relation dimension at least 76, active "
                "relation colors would have loss at least 3 and inactive colors "
                "loss at least 4; support size at least 2 gives total loss at "
                "least 21>17."
            ),
            "one_defective_t17": (
                "Failure for the defective deletion costs at least 3 and failure "
                "for each of six full deletions costs at least 4, totaling at "
                "least 27>17."
            ),
            "therefore_some_six_term_permanent_relation_dimension_is_at_most_75": True,
            "dimension_89_equality_fallback": (
                "If the retained quadratic sum has dimension 89 and permanent "
                "relation dimension 75, its quotient has dimension 14. The six "
                "cubic spaces are literal direct of dimension 120; m_53=81>75 "
                "bounds their permanent intersection by 52, so the required "
                "prolongation is at least 468, contradicting the t14 cap 453."
            ),
            "dimension_90_equality_alpha_fallback": (
                "If the retained quadratic sum has dimension 90 and quotient "
                "dimension 15 but some full term has alpha at most 2, quadratic "
                "directness makes the six cubic spaces direct of dimension 120. "
                "Again their permanent intersection is at most 52, so 468 "
                "contradicts the t15 cap 458."
            ),
        },
        "layer_exclusions": layers,
        "equality_route": {
            "a_47_or_48_plane_with_shadow_at_most_75_has_shadow_exactly_75": True,
            "a_dimension_89_quadratic_equality_sum_is_excluded_by_the_t14_cap": True,
            "a_dimension_90_t15_equality_with_alpha_at_most_two_is_excluded_by_the_t15_cap": True,
            "the_remaining_equality_case_has_six_full_alpha_three_terms_and_common_W15": True,
            "N6_076_or_N6_078_extends_it_to_a_50_plane_with_the_same_shadow": True,
            "the_selected_six_terms_then_are_full_literal_direct_and_share_W15": True,
            "N6_064_gives_a_genuine_23_dimensional_flag_hook": True,
            "N6_069_and_N6_072_exclude_the_actual_six_frame_endpoint": True,
        },
        "updated_residual_seven_set_upper": 66,
        "strict_conclusion": (
            "All thirteen defect-six states at x_A=67,68 are excluded by the "
            "termwise t15/t16 caps or the quotient deletion-loss lemma, followed "
            "by N6-076/N6-078 and flag-hook actual-frame rigidity. Hence every "
            "actual b=34 survivor has x_A<=66 for every residual seven-set."
        ),
        "claim_boundary": (
            "This excludes only x_A=67,68 after N6-098. The x_A<=66 layers "
            "and global b=34 remain open. It does not prove ordinary lower29 "
            "and makes no border-rank claim."
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
    print("excluded_dimensions=67,68")
    print("updated_residual_seven_set_upper=66")
    print("N6_LOWER29_B34_X67_68_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
