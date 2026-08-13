#!/usr/bin/env python3
"""Exact first shortening of the N=28, b=34 residual layer.

N6-081 proves a strict alternative.  Either every residual seven-set has
coupled shortening dimension at most 79, or one seven-set is forced into the
unique scalar 80-to-90 endpoint with seven literal-direct quadratic spaces
and a common 15-dimensional quotient.  This does not exclude b=34.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_first_shortening.json"
N6074_SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6080_SCRIPT = ROOT / "scripts" / "n6_lower29_q7_defect_six_frontier.py"
N6080_DATA = ROOT / "data" / "n6_lower29_q7_defect_six_frontier.json"

RESIDUAL_TERMS = 22
SUBSET_TERMS = 7
COMPLEMENT_TERMS = RESIDUAL_TERMS - SUBSET_TERMS
GLOBAL_B = 34
COUPLED_INTERSECTION_FLOOR = 400 - GLOBAL_B
TERM_MIDDLE_CAP = 20
QUADRATIC_PROJECTION_CAP = 15 * (SUBSET_TERMS - 1) + 3


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cap_for_t_upper(t_upper: int) -> int | None:
    return {12: 436, 13: 440, 14: 453}.get(t_upper)


def local_state_rows(n6074, n6080, shadow_at_80: int) -> list[dict[str, object]]:
    defect = QUADRATIC_PROJECTION_CAP - shadow_at_80
    rows: list[dict[str, object]] = []
    for epsilon in combinations_with_replacement(range(16), SUBSET_TERMS):
        if sum(epsilon) - min(epsilon) > defect:
            continue
        middle = [n6074.individual_middle_lower(value) for value in epsilon]
        if any(value is None for value in middle):
            continue
        if any(
            sum(epsilon) - epsilon[index] + n6080.alpha_floor(epsilon[index]) > defect
            for index in range(SUBSET_TERMS)
        ):
            continue
        relation_cap = defect - sum(epsilon) + min(epsilon)
        for kappa2 in range(relation_cap + 1):
            d2 = 15 * SUBSET_TERMS - sum(epsilon) - kappa2
            t2_upper = d2 - shadow_at_80
            conservative_h_lower = sum(int(value) for value in middle) - 2 * n6074.macaulay_successor_degree_two(kappa2)
            required = 400 + conservative_h_lower - 80
            cap = cap_for_t_upper(t2_upper)
            excluded = cap is not None and required > cap
            rows.append(
                {
                    "epsilon": list(epsilon),
                    "kappa2": kappa2,
                    "d2": d2,
                    "a2_lower": shadow_at_80,
                    "t2_upper": t2_upper,
                    "conservative_h_lower": conservative_h_lower,
                    "required_prolongation_lower": required,
                    "existing_cap": cap,
                    "excluded_by_existing_cap": excluded,
                }
            )
    return rows


def build_payload() -> dict[str, object]:
    n6074 = load_module(N6074_SCRIPT, "n6074_for_n6081")
    n6080 = load_module(N6080_SCRIPT, "n6080_for_n6081")
    require(n6074.build_payload() == json.loads(N6074_DATA.read_text(encoding="utf-8")), N6074_DATA)
    require(n6080.build_payload() == json.loads(N6080_DATA.read_text(encoding="utf-8")), N6080_DATA)

    shadow_module = n6074.load_shadow_module()
    shadow_table = {
        dimension: int(shadow_module.minimum_ferrers_shadow(dimension)[0])
        for dimension in range(66, 82)
    }
    require(
        shadow_table
        == {
            66: 87,
            67: 87,
            68: 87,
            69: 89,
            70: 89,
            71: 89,
            72: 89,
            73: 90,
            74: 90,
            75: 90,
            76: 90,
            77: 90,
            78: 90,
            79: 90,
            80: 90,
            81: 96,
        },
        shadow_table,
    )
    require(shadow_table[80] <= QUADRATIC_PROJECTION_CAP < shadow_table[81], shadow_table)

    seven_shortening_upper = 80
    fifteen_literal_floor = COUPLED_INTERSECTION_FLOOR - seven_shortening_upper
    seven_literal_floor = fifteen_literal_floor - 8 * TERM_MIDDLE_CAP
    require((fifteen_literal_floor, seven_literal_floor) == (286, 126), (fifteen_literal_floor, seven_literal_floor))

    rows = local_state_rows(n6074, n6080, shadow_table[80])
    excluded = [row for row in rows if row["excluded_by_existing_cap"]]
    open_rows = [row for row in rows if not row["excluded_by_existing_cap"]]
    require((len(rows), len(excluded), len(open_rows)) == (11, 10, 1), rows)
    endpoint = open_rows[0]
    require(endpoint["epsilon"] == [0] * 7 and endpoint["kappa2"] == 0, endpoint)
    require((endpoint["d2"], endpoint["t2_upper"]) == (105, 15), endpoint)

    # With epsilon=0 and kappa2=0 the seven F_i are literal direct.  Taking
    # derivatives shows the seven U_i are literal direct too, so ell_A=140.
    # The t=15 cap then excludes every alpha_i<=2 subcase.
    literal_middle_dimension = SUBSET_TERMS * TERM_MIDDLE_CAP
    endpoint_required = 400 + literal_middle_dimension - 80
    alpha_at_most_two_cap = 458
    require((literal_middle_dimension, endpoint_required) == (140, 460), endpoint_required)
    require(endpoint_required > alpha_at_most_two_cap, endpoint_required)
    quotient_dimension_each = 12 - 0 + 3
    require(quotient_dimension_each == endpoint["t2_upper"], quotient_dimension_each)
    forced_a2 = int(endpoint["d2"]) - int(endpoint["t2_upper"])
    require(forced_a2 == shadow_table[80] == 90, forced_a2)

    return {
        "status": "N6_081_B34_FIRST_SHORTENING_EXACT_ENDPOINT",
        "global_hypothesis": {
            "total_terms": 28,
            "fixed_terms": 6,
            "residual_terms": RESIDUAL_TERMS,
            "global_b": GLOBAL_B,
            "coupled_residual_intersection_floor": COUPLED_INTERSECTION_FLOOR,
        },
        "seven_set_shortening": {
            "quadratic_projection_cap": QUADRATIC_PROJECTION_CAP,
            "exact_product_shadow_table_66_to_81": {str(key): value for key, value in shadow_table.items()},
            "universal_x_A_upper": seven_shortening_upper,
            "every_f_A_upper": seven_shortening_upper,
            "every_fifteen_set_literal_dimension_floor": fifteen_literal_floor,
            "every_seven_set_literal_dimension_floor": seven_literal_floor,
        },
        "conditional_f80_state_pruning": {
            "hypothesis": "some residual seven-set A has f_A=80",
            "forced_x_A": 80,
            "exact_product_shadow": shadow_table[80],
            "defect_budget": QUADRATIC_PROJECTION_CAP - shadow_table[80],
            "state_count": len(rows),
            "existing_cap_excluded_count": len(excluded),
            "pre_geometry_survivor_count": len(open_rows),
            "states": rows,
        },
        "unique_endpoint": {
            "epsilon": [0] * 7,
            "alpha": [3] * 7,
            "kappa2": 0,
            "d2": 105,
            "a2": forced_a2,
            "t2": 15,
            "seven_quadratic_spaces_literal_direct": True,
            "seven_middle_spaces_literal_direct": True,
            "literal_middle_dimension": literal_middle_dimension,
            "required_prolongation_lower": endpoint_required,
            "alpha_at_most_two_cap": alpha_at_most_two_cap,
            "strict_cap_gap": endpoint_required - alpha_at_most_two_cap,
            "all_quotient_images_equal_one_common_W15": True,
            "central_space_dimension": 80,
            "central_first_shadow_dimension": 90,
            "six_anchor_differences_span_the_90_plane": True,
        },
        "strict_conclusion": (
            "Any global b=34 survivor either has f_A<=79 for every residual seven-set A, "
            "or contains the displayed exact 80-to-90 common-W15 seven-frame endpoint."
        ),
        "next_geometric_target": (
            "Classify or exclude the actual seven-frame 80-to-90 endpoint; separately, "
            "continue shortening the branch in which every seven-set has f_A<=79."
        ),
        "claim_boundary": (
            "This certificate does not exclude either branch of the alternative, does not "
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
    print("seven_set_x_upper=80 literal_floor=126")
    print("f80_states=11 excluded=10 survivor=1")
    print("N6_LOWER29_B34_FIRST_SHORTENING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
