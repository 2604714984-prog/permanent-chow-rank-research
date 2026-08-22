#!/usr/bin/env python3
"""Exact endpoint application excluding the N=28 layers b=32 and b=48."""

from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b32_b48_exclusion.json"
N6074_SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6075_SCRIPT = ROOT / "scripts" / "n6_lower29_b31_b49_exclusion.py"
N6075_DATA = ROOT / "data" / "n6_lower29_b31_b49_exclusion.json"
N6076_DATA = ROOT / "data" / "n6_product_shadow_b48_equality_locus.json"
N6073_DATA = ROOT / "data" / "n6_product_shadow_b49_equality_locus.json"
N6031_DATA = ROOT / "data" / "n6_single_term_middle_rank_gap.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def b48_scalar_states(n6074, caps: dict[str, int]) -> dict[str, object]:
    b = 48
    shadow = 75
    defect = 78 - shadow
    selection = n6074.selection_lower(20, b)
    residual = n6074.residual_upper(20, b)
    states = []
    for epsilon in combinations_with_replacement(range(16), 6):
        omitted = sum(epsilon) - min(epsilon)
        if omitted > defect:
            continue
        middle = [n6074.individual_middle_lower(value) for value in epsilon]
        if any(value is None for value in middle):
            continue
        for kappa2 in range(defect - omitted + 1):
            h_lower = sum(int(value) for value in middle) - 2 * n6074.macaulay_successor_degree_two(kappa2)
            if max(selection, h_lower) > residual:
                continue
            d2 = 90 - sum(epsilon) - kappa2
            t2_upper = d2 - shadow
            required = 400 + h_lower - b
            all_alpha_three_candidate = epsilon == (0,) * 6 and kappa2 == 0
            cap = caps[str(t2_upper)]
            if all_alpha_three_candidate:
                require(t2_upper == 15 and required > cap, (required, cap))
                excluded = False
                route = "t15_cap_excludes_only_the_alpha_at_most_two_subcase"
            else:
                require(0 in epsilon and 12 <= t2_upper <= 14, (epsilon, kappa2, t2_upper))
                excluded = required > cap
                require(excluded, (epsilon, kappa2, required, cap))
                route = "epsilon_zero_alpha_at_most_two_term_cap"
            states.append(
                {
                    "epsilon": list(epsilon),
                    "kappa2": kappa2,
                    "h_lower": h_lower,
                    "d2": d2,
                    "a2_lower": shadow,
                    "t2_upper": t2_upper,
                    "required_prolongation_lower": required,
                    "applicable_cap": cap,
                    "cap_route": route,
                    "excluded_by_existing_cap": excluded,
                }
            )
    require(len(states) == 13, states)
    survivors = [state for state in states if not state["excluded_by_existing_cap"]]
    require(len(survivors) == 1, survivors)
    survivor = survivors[0]
    require(survivor["epsilon"] == [0] * 6 and survivor["kappa2"] == 0, survivor)
    return {
        "exact_shadow": shadow,
        "defect_budget": defect,
        "selection_middle_lower": selection,
        "residual_middle_upper": residual,
        "scalar_state_count": len(states),
        "cap_excluded_state_count": len(states) - 1,
        "unique_pre_geometry_state": {
            **survivor,
            "alpha": [3] * 6,
            "alpha_at_most_two_subcase_cap": caps["15"],
            "alpha_at_most_two_subcase_strict_gap": survivor[
                "required_prolongation_lower"
            ]
            - caps["15"],
            "a2": 75,
            "t2": 15,
            "h": 120,
            "six_middle_images_literal_direct": True,
        },
        "states": states,
    }


def b32_hereditary_arithmetic(n6074, n6075, caps: dict[str, int]) -> dict[str, object]:
    b = 32
    dim_s_floor = 400 - b
    term_cap = 20
    complement_capacity = 16 * term_cap
    n6031 = json.loads(N6031_DATA.read_text(encoding="utf-8"))
    require(int(n6031["excluded_middle_rank"]) == 19, n6031)
    nonfull_rank_cap = 18
    shadow_module = n6074.load_shadow_module()
    shadow = lambda dimension: int(shadow_module.minimum_ferrers_shadow(dimension)[0])
    shadow_values = {dimension: shadow(dimension) for dimension in range(48, 54)}
    require(shadow_values == {48: 75, 49: 75, 50: 75, 51: 78, 52: 78, 53: 81}, shadow_values)

    # Initial shortening: x_A<=52, ell_16>=316, ell_6>=116.
    x_upper_initial = max(d for d, value in shadow_values.items() if value <= 78)
    ell16_initial = dim_s_floor - x_upper_initial
    ell6_initial = ell16_initial - 10 * term_cap
    require((x_upper_initial, ell16_initial, ell6_initial) == (52, 316, 116), (x_upper_initial, ell16_initial, ell6_initial))
    defect_zero_cases = []
    for x in (51, 52):
        required = 400 + ell6_initial - x
        require(shadow_values[x] == 78 and required > caps["12"], (x, required))
        defect_zero_cases.append(
            {
                "x": x,
                "required_prolongation_lower": required,
                "common_W12_cap": caps["12"],
                "strict_gap": required - caps["12"],
            }
        )

    # If f_A=50 then X=S intersect L_A is the actual 50-plane.  Complementary
    # shortening gives ell_A>=118; the alpha-three profile then makes the six
    # F_i, hence the six U_i, literal direct, and N6-064/N6-072 applies.
    f50_ell16 = dim_s_floor - 50
    f50_ell6 = f50_ell16 - 10 * term_cap
    f50_required = 400 + f50_ell6 - 50
    require((f50_ell16, f50_ell6, f50_required) == (318, 118, 468), f50_required)
    f50_profile = n6075.alpha_three_forcing(f50_required, caps)

    # Once all f<=49, ell_16>=319.  The rank-19 gap forces all individual
    # U_i to have rank 20 and ell_A>=119.  Both possible x values are excluded:
    # x=50 by N6-064 and x=49 by N6-073.
    f49_ell16 = dim_s_floor - 49
    nonfull_sixteen_cap = 15 * term_cap + nonfull_rank_cap
    require(f49_ell16 > nonfull_sixteen_cap, (f49_ell16, nonfull_sixteen_cap))
    f49_ell6 = f49_ell16 - 10 * term_cap
    f49_cases = []
    for x, extension in ((50, "N6-064"), (49, "N6-073_then_N6-064")):
        required = 400 + f49_ell6 - x
        f49_cases.append(
            {
                "x": x,
                "six_term_literal_floor": f49_ell6,
                "required_prolongation_lower": required,
                "profile": n6075.alpha_three_forcing(required, caps),
                "extension_route": extension,
            }
        )

    # Therefore every f_A=48.  Equality in the shortening sequence gives
    # dim S=368 and every complementary sixteen-set literal direct, hence
    # every six-set literal direct with ell_A=120.  Exclude x=50,49,48 in turn.
    f_floor = dim_s_floor - complement_capacity
    require(f_floor == 48, f_floor)
    final_cases = []
    for x, extension in (
        (50, "N6-064"),
        (49, "N6-073_then_N6-064"),
        (48, "N6-076_then_N6-064"),
    ):
        required = 400 + 120 - x
        final_cases.append(
            {
                "x": x,
                "exact_product_shadow": shadow_values[x],
                "required_prolongation": required,
                "profile": n6075.alpha_three_forcing(required, caps),
                "extension_route": extension,
            }
        )
    return {
        "global_residual_permanent_intersection_floor": dim_s_floor,
        "shadow_values": {str(key): value for key, value in shadow_values.items()},
        "stage1_initial_bounds": {
            "initial_x_A_upper": x_upper_initial,
            "initial_sixteen_term_literal_floor": ell16_initial,
            "initial_six_term_literal_floor": ell6_initial,
            "defect_zero_cases": defect_zero_cases,
            "x_A_upper_after_stage": 50,
        },
        "stage2_exclude_some_f_50": {
            "sixteen_term_literal_floor": f50_ell16,
            "six_term_literal_floor": f50_ell6,
            "required_prolongation_lower": f50_required,
            "profile": f50_profile,
            "excluded_by": "N6-064/N6-069/N6-072",
        },
        "stage3_exclude_some_f_49": {
            "sixteen_term_literal_floor": f49_ell16,
            "nonfull_sixteen_term_cap": nonfull_sixteen_cap,
            "all_individual_middle_ranks_are_twenty": True,
            "cases": f49_cases,
        },
        "stage4_all_f_48_and_literal_directness": {
            "f_A_dimension": f_floor,
            "global_residual_permanent_intersection_dimension": dim_s_floor,
            "every_sixteen_term_literal_dimension": complement_capacity,
            "every_sixteen_term_family_literal_direct": True,
            "every_six_term_literal_dimension": 120,
            "literal_and_coupled_six_term_middle_spaces_agree": True,
        },
        "stage5_exclude_x_50_49_48": {
            "cases": final_cases,
            "last_case_uses_N6-076": True,
        },
    }


def build_payload() -> dict[str, object]:
    n6074 = load_module(N6074_SCRIPT, "n6074_for_n6077")
    n6075 = load_module(N6075_SCRIPT, "n6075_for_n6077")
    require(n6074.build_payload() == json.loads(N6074_DATA.read_text(encoding="utf-8")), N6074_DATA)
    require(n6075.build_payload() == json.loads(N6075_DATA.read_text(encoding="utf-8")), N6075_DATA)
    caps = n6075.frozen_caps()
    n6076 = json.loads(N6076_DATA.read_text(encoding="utf-8"))
    n6073 = json.loads(N6073_DATA.read_text(encoding="utf-8"))
    extension48 = n6076["projective_globalization"]
    extension49 = n6073["projective_globalization"]
    require(extension48["every_48_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"], extension48)
    require(extension49["every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"], extension49)
    b32 = b32_hereditary_arithmetic(n6074, n6075, caps)
    b48 = b48_scalar_states(n6074, caps)
    return {
        "status": "N6_077_LOWER29_B32_B48_EXCLUSION",
        "hypothesis": "N=28 ordinary Chow decomposition after the N6-074 fixed-six reduction",
        "frozen_prolongation_caps": caps,
        "b32_hereditary_endpoint": b32,
        "b48_fixed_six_endpoint": b48,
        "n6076_interface": extension48,
        "n6073_interface": extension49,
        "shared_geometric_route": [
            "N6-076 or N6-073 extends the 48- or 49-plane to an N6-064 50-plane with the same K75",
            "N6-064 makes the second shadow a genuine 23-dimensional flag hook",
            "15-plane product-shadow equality makes all six factor spans six-dimensional and pairwise transverse",
            "N6-069 and N6-061/N6-059 exclude any invertible row or column block",
            "N6-072 excludes the remaining all-singular six-frame hook",
        ],
        "frontier_before": list(range(32, 49)),
        "excluded_here": [32, 48],
        "frontier_after": list(range(33, 48)),
        "strict_conclusion": "The ordinary lower-29 fixed-six frontier is reduced to b=33,...,47.",
        "claim_boundary": (
            "This excludes only b=32 and b=48 inside the N6-074 reduction. "
            "The dimension-47 shadow-75 plateau at b=33 and b=47 remains open. "
            "This does not prove ChowRank(perm_6)>=29 and makes no border-rank claim."
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
    print("excluded_here=32,48")
    print("frontier_after=33..47")
    print("N6_LOWER29_B32_B48_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
