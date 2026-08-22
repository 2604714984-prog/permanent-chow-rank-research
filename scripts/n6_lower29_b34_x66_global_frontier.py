#!/usr/bin/env python3
"""Connect the global b=34 branch to the hereditary x=66 frontier (N6-100)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_x66_global_frontier.json"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6080_DATA = ROOT / "data" / "n6_lower29_q7_defect_six_frontier.json"
N6099_SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x67_68_exclusion.py"
N6099_DATA = ROOT / "data" / "n6_lower29_b34_x67_68_exclusion.json"
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
    n6074 = json.loads(N6074_DATA.read_text(encoding="utf-8"))
    n6080 = json.loads(N6080_DATA.read_text(encoding="utf-8"))
    n6099_module = load_module(N6099_SCRIPT, "n6099_for_n6100")
    n6099 = n6099_module.build_payload()
    shadow = load_module(SHADOW_SCRIPT, "n6056_for_n6100")
    require(n6099 == json.loads(N6099_DATA.read_text(encoding="utf-8")), N6099_DATA)

    q7 = next(
        row
        for row in n6074["q_frontier_before_ambient_cap_saturation"]
        if row["b"] == 34
    )
    require(
        (
            q7["best_q_before_ambient_cap_saturation"],
            q7["literal_q_intersection_floor"],
            q7["exact_product_shadow_at_floor"],
        )
        == (7, 66, 87),
        q7,
    )
    require(n6099["updated_residual_seven_set_upper"] == 66, n6099)
    relation = n6080["relation_envelope"]
    require(
        (relation["state_count"], relation["existing_cap_excluded_count"], relation["open_state_count"])
        == (56, 43, 13),
        relation,
    )
    m46, count46, witness46, _ = shadow.minimum_ferrers_shadow(46)
    m47, _, _, _ = shadow.minimum_ferrers_shadow(47)
    m53, _, _, _ = shadow.minimum_ferrers_shadow(53)
    require((m46, m47, m53) == (72, 75, 81), (m46, m47, m53))

    total_central_floor = 400 - 34
    seven_lower = total_central_floor - 15 * 20
    require((total_central_floor, seven_lower) == (366, 66), None)
    fifteen_literal_cap = 15 * 20
    seven_literal_dimension = 7 * 20
    six_literal_dimension = 6 * 20
    critical_six_lower = total_central_floor - 16 * 20
    require(
        (fifteen_literal_cap, seven_literal_dimension, six_literal_dimension, critical_six_lower)
        == (300, 140, 120, 46),
        None,
    )

    return {
        "status": [
            "PURE_GLOBAL_B34_TO_HEREDITARY_X66_REDUCTION",
            "EXACT_FIXED_SIX_AND_RELATION_ENVELOPE_REPLAY",
            "N6-100",
        ],
        "global_hypothesis": {
            "ordinary_terms": 28,
            "fixed_terms": 6,
            "residual_terms": 22,
            "global_b": 34,
            "central_space_dimension_floor": total_central_floor,
        },
        "hereditary_seven_set_equality": {
            "N6_074_lower_for_every_residual_seven_set": seven_lower,
            "N6_099_upper_for_every_residual_seven_set": 66,
            "therefore_every_literal_seven_set_intersection_dimension": 66,
            "therefore_every_coupled_seven_set_intersection_dimension": 66,
            "global_central_space_dimension": 366,
            "every_fifteen_term_literal_sum_dimension": fifteen_literal_cap,
            "every_at_most_fifteen_term_family_is_literal_direct": True,
            "every_term_cubic_dimension": 20,
            "every_seven_term_literal_and_coupled_sum_dimension": seven_literal_dimension,
        },
        "forced_local_frontier": {
            "every_seven_set_first_shadow_lower": 87,
            "quadratic_projection_cap": 93,
            "defect": 6,
            "N6_080_relation_state_count": relation["state_count"],
            "N6_080_old_cap_excluded_count": relation["existing_cap_excluded_count"],
            "open_exact_state_count": relation["open_state_count"],
            "every_seven_set_lies_in_one_of_the_thirteen_states": True,
        },
        "critical_six_shortening": {
            "for_every_seven_set_N6_099_selects_a_six_subset_with_quadratic_permanent_relation_dimension_at_most": 75,
            "six_literal_cubic_sum_dimension": six_literal_dimension,
            "central_intersection_lower_from_sixteen_term_complement_capacity": critical_six_lower,
            "dimension_at_least_47_is_excluded_by_N6_078_or_the_t14_fallback": True,
            "therefore_selected_six_intersection_dimension": 46,
            "selected_six_product_shadow_dimension_range": [m46, 75],
            "complementary_sixteen_term_literal_sum_dimension": 320,
            "complementary_sixteen_terms_are_literal_direct": True,
            "product_shadow_m46": m46,
            "product_shadow_minimizer_count": count46,
            "product_shadow_first_minimizer": list(witness46),
            "product_shadow_m47": m47,
            "product_shadow_m53": m53,
        },
        "strict_conclusion": (
            "A hypothetical ordinary 28-term decomposition in the b=34 branch "
            "forces every residual seven-set into the exact x=66, first-shadow-at-"
            "least-87 N6-080 frontier. Every such seven-set contains a six-set "
            "whose central intersection is exactly 46, whose product shadow has "
            "dimension 72 through 75, and whose sixteen-term complement is literal "
            "direct. This is now the first unresolved b=34 layer."
        ),
        "next_target": (
            "Use actual Chow common-section and coproduct structure to exclude the "
            "critical six-term 46-plane packets with quadratic shadow 72 through 75."
        ),
        "claim_boundary": (
            "This is a strict global reduction, not an exclusion of b=34. It does "
            "not classify arbitrary 46-planes, prove ordinary lower29, determine "
            "the exact rank, or make a border-rank claim."
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
    print("global_b34_every_seven_set_x=66")
    print("critical_six_set_x=46 shadow=72..75")
    print("N6_LOWER29_B34_X66_GLOBAL_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
