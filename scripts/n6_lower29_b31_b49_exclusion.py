#!/usr/bin/env python3
"""Exact application audit excluding the N=28 fixed-six layers b=31 and b=49.

N6-075 recomputes the endpoint arithmetic and freezes the geometric interfaces
N6-059, N6-069, N6-072, N6-073, and N6-074 without re-running their proofs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b31_b49_exclusion.json"
N6074_SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6073_DATA = ROOT / "data" / "n6_product_shadow_b49_equality_locus.json"
N6047_DATA = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"
N6051_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
N6052_DATA = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"
N6049_DATA = ROOT / "data" / "n6_alpha2_prolongation_exclusion.json"
N6031_DATA = ROOT / "data" / "n6_single_term_middle_rank_gap.json"


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_n6074_module():
    spec = importlib.util.spec_from_file_location("n6074_for_n6075", N6074_SCRIPT)
    require(spec is not None and spec.loader is not None, N6074_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frozen_caps() -> dict[str, int]:
    n6047 = json.loads(N6047_DATA.read_text(encoding="utf-8"))
    n6051 = json.loads(N6051_DATA.read_text(encoding="utf-8"))
    n6052 = json.loads(N6052_DATA.read_text(encoding="utf-8"))
    n6049 = json.loads(N6049_DATA.read_text(encoding="utf-8"))
    base = {
        int(key): int(value)
        for key, value in n6047["fixed_point_cap_audit"][
            "characteristic_zero_prolongation_upper_caps"
        ].items()
    }
    require(base == {12: 436, 13: 440, 14: 448}, base)
    require(int(n6049["one_rectangle_universal_prolongation_cap"]) == 453, n6049)
    require(int(n6051["characteristic_zero_prolongation_upper_cap_t15"]) == 458, n6051)
    require(int(n6052["universal_alpha2_t15_prolongation_upper_cap"]) == 458, n6052)
    return {"12": 436, "13": 440, "14": 453, "15": 458}


def b49_scalar_states(n6074, caps: dict[str, int]) -> dict[str, object]:
    b = 49
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
            possible_all_alpha_three = epsilon == (0,) * 6 and kappa2 == 0
            if possible_all_alpha_three:
                cap = caps["15"]
                require(required > cap, (required, cap))
                excluded_by_cap = False
                route = "requires_t15_alpha_subcase_split"
            else:
                require(0 in epsilon and 12 <= t2_upper <= 14, (epsilon, kappa2, t2_upper))
                cap = caps[str(t2_upper)]
                excluded_by_cap = required > cap
                require(excluded_by_cap, (epsilon, kappa2, required, cap))
                route = "contains_epsilon_zero_term_with_alpha_at_most_two"
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
                    "excluded_by_existing_cap": excluded_by_cap,
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
        "cap_excluded_state_count": len(states) - len(survivors),
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
        },
        "states": states,
    }


def alpha_three_forcing(required: int, caps: dict[str, int]) -> dict[str, object]:
    """Replay the defect-at-most-three route, without assuming shadow equality."""

    quadratic_projection_cap = 78
    product_shadow_floor = 75
    defect_upper = quadratic_projection_cap - product_shadow_floor
    epsilon_types = [
        epsilon
        for epsilon in combinations_with_replacement(range(16), 6)
        if sum(epsilon) - min(epsilon) <= defect_upper
    ]
    require(all(min(epsilon) == 0 for epsilon in epsilon_types), epsilon_types)
    require(required > caps["15"], (required, caps["15"]))

    # An epsilon-zero term with alpha<=2 is excluded by the t2<=15 cap.
    # Thus alpha=3 and q_i=12-epsilon_i+alpha_i=15.  Since
    # t2<=d2-a2<=90-75=15, equality forces d2=90, a2=75, t2=15,
    # epsilon=(0^6), and kappa2=0.  The same cap then forces alpha=3
    # for each of the other five terms.
    quotient_image_from_epsilon_zero_alpha_three = 12 - 0 + 3
    t2_upper = 90 - product_shadow_floor
    require(quotient_image_from_epsilon_zero_alpha_three == t2_upper == 15, t2_upper)
    return {
        "product_shadow_lower": product_shadow_floor,
        "quadratic_projection_cap": quadratic_projection_cap,
        "omitted_defect_upper": defect_upper,
        "omitted_defect_epsilon_type_count": len(epsilon_types),
        "every_omitted_defect_epsilon_type_contains_epsilon_zero": True,
        "required_prolongation_lower": required,
        "alpha_at_most_two_cap": caps["15"],
        "strict_cap_gap": required - caps["15"],
        "forced_quadratic_state": {
            "epsilon": [0] * 6,
            "alpha": [3] * 6,
            "kappa2": 0,
            "d2": 90,
            "a2": 75,
            "t2": 15,
            "common_quotient_dimension": 15,
            "six_quadratic_spaces_literal_direct": True,
        },
    }


def b31_hereditary_arithmetic(n6074, caps: dict[str, int]) -> dict[str, object]:
    """The two-level hereditary chain needed before the 49-plane theorem."""

    b = 31
    dim_s_floor = 400 - b
    term_middle_cap = 20
    n6031 = json.loads(N6031_DATA.read_text(encoding="utf-8"))
    require(int(n6031["excluded_middle_rank"]) == 19, n6031)
    next_nonfull_middle_rank = int(n6031["excluded_middle_rank"]) - 1
    sixteen_term_cap = 16 * term_middle_cap
    shadow_module = n6074.load_shadow_module()
    shadow = lambda dimension: int(shadow_module.minimum_ferrers_shadow(dimension)[0])
    shadow_values = {dimension: shadow(dimension) for dimension in range(49, 54)}
    require(shadow_values == {49: 75, 50: 75, 51: 78, 52: 78, 53: 81}, shadow_values)

    # Stage 1.  For six A, use f_A=dim(S intersect L_A),
    # x_A=dim(E3 intersect L_A), and ell_A=dim L_A.  The shadow/cap bound
    # gives x_A<=52.  Applying S -> L_all/L_C to a complementary six-set C
    # gives ell_B>=369-f_C>=317 for every sixteen-set B.  Enlarging A to B
    # then gives ell_A>=317-10*20=117.
    x_upper_initial = max(d for d, value in shadow_values.items() if value <= 78)
    ell16_floor_initial = dim_s_floor - x_upper_initial
    ell6_floor_initial = ell16_floor_initial - 10 * term_middle_cap
    require((x_upper_initial, ell16_floor_initial, ell6_floor_initial) == (52, 317, 117), (x_upper_initial, ell16_floor_initial, ell6_floor_initial))

    # Stage 2.  At x=51,52 the exact shadow reaches the full projection cap,
    # so the defect-zero common-W12 interface has prolongation cap 436.
    w12_exclusions = []
    for x in (51, 52):
        required = 400 + ell6_floor_initial - x
        require(shadow_values[x] == 78 and required > caps["12"], (x, required))
        w12_exclusions.append(
            {
                "x": x,
                "literal_middle_dimension_floor": ell6_floor_initial,
                "exact_product_shadow": shadow_values[x],
                "required_prolongation_lower": required,
                "common_W12_cap": caps["12"],
                "strict_gap": required - caps["12"],
            }
        )
    x_upper_after_w12 = 50

    # Stage 3.  If some f_A=50, then all f_C<=x_C<=50.  Hence every
    # sixteen-set has ell_B>=319.  The rank-19 gap forces every U_j to have
    # rank 20, and enlarging A to a sixteen-set gives ell_A>=119.  Since
    # f_A<=x_A<=50, X=S intersect L_A is the whole 50-plane E3 intersect L_A.
    f50_ell16_floor = dim_s_floor - x_upper_after_w12
    nonfull_sixteen_cap = 15 * term_middle_cap + next_nonfull_middle_rank
    require(f50_ell16_floor > nonfull_sixteen_cap, (f50_ell16_floor, nonfull_sixteen_cap))
    f50_ell6_floor = f50_ell16_floor - 10 * term_middle_cap
    f50_required = 400 + f50_ell6_floor - 50
    require((f50_ell16_floor, nonfull_sixteen_cap, f50_ell6_floor, f50_required) == (319, 318, 119, 469), f50_required)
    f50_profile = alpha_three_forcing(f50_required, caps)

    # Stage 4.  Excluding f=50 leaves 49<=f_A<=49.  The exact sequence for
    # S -> L_all/L_A then forces dim S=369 and ell_B=320 for every sixteen-set.
    f_floor_from_complement_capacity = dim_s_floor - sixteen_term_cap
    require(f_floor_from_complement_capacity == 49, f_floor_from_complement_capacity)
    forced_dim_s = f_floor_from_complement_capacity + sixteen_term_cap
    forced_ell16 = forced_dim_s - f_floor_from_complement_capacity
    forced_ell6 = 6 * term_middle_cap
    require((forced_dim_s, forced_ell16, forced_ell6) == (369, 320, 120), (forced_dim_s, forced_ell16, forced_ell6))

    # Stage 5.  Now f_A=49 and ell_A=120, while 49<=x_A<=50.  A remaining
    # x=50 has required prolongation 470 and is excluded through N6-064.
    x50_required = 400 + forced_ell6 - 50
    require(x50_required == 470, x50_required)
    x50_profile = alpha_three_forcing(x50_required, caps)

    # Hence x=49.  Only now do we obtain the exact 75-shadow/common-W15
    # 49-plane to which N6-073 applies.
    x49_required = 400 + forced_ell6 - 49
    require(x49_required == 471, x49_required)
    x49_profile = alpha_three_forcing(x49_required, caps)
    return {
        "notation": {
            "U_i": "D3(T_i)",
            "L_A": "sum of U_i for i in A",
            "ell_A": "dim L_A",
            "S": "E3 intersect the coupled residual middle space",
            "f_A": "dim(S intersect L_A)",
            "x_A": "dim(E3 intersect L_A)",
        },
        "stage1_initial_bounds": {
            "global_residual_permanent_intersection_floor": dim_s_floor,
            "shadow_values_49_through_53": {str(key): value for key, value in shadow_values.items()},
            "six_term_quadratic_projection_cap": 78,
            "initial_x_A_upper": x_upper_initial,
            "initial_sixteen_term_literal_floor": ell16_floor_initial,
            "initial_six_term_literal_floor": ell6_floor_initial,
        },
        "stage2_exclude_x_51_52": {
            "cases": w12_exclusions,
            "x_A_upper_after_stage": x_upper_after_w12,
            "interface": "defect-zero common-W12 and N6-044",
        },
        "stage3_exclude_some_f_50": {
            "hypothesis": "some f_A=50",
            "every_f_C_upper": x_upper_after_w12,
            "sixteen_term_literal_floor": f50_ell16_floor,
            "N6_031_nonfull_sixteen_term_cap": nonfull_sixteen_cap,
            "every_individual_middle_rank_forced": term_middle_cap,
            "six_term_literal_floor": f50_ell6_floor,
            "forced_x_A": 50,
            "profile": f50_profile,
            "quadratic_directness_then_forces_literal_middle_dimension": 120,
            "contradiction_interface": "N6-064 then N6-069/N6-061/N6-059/N6-072",
        },
        "stage4_all_f_49_and_literal_directness": {
            "f_A_floor_from_sixteen_term_capacity": f_floor_from_complement_capacity,
            "f_A_dimension": 49,
            "global_residual_permanent_intersection_dimension": forced_dim_s,
            "every_sixteen_term_literal_dimension": forced_ell16,
            "every_sixteen_term_family_literal_direct": True,
            "every_six_term_literal_dimension": forced_ell6,
        },
        "stage5_exclude_x_50_then_force_x_49": {
            "x_A_options_before_exclusion": [49, 50],
            "x_50_required_prolongation": x50_required,
            "x_50_profile": x50_profile,
            "x_50_contradiction_interface": "N6-064 then N6-069/N6-061/N6-059/N6-072",
            "forced_x_A": 49,
            "x_49_required_prolongation": x49_required,
            "x_49_profile": x49_profile,
            "x_49_contradiction_interface": "N6-073 then N6-069/N6-061/N6-059/N6-072",
        },
    }


def build_payload() -> dict[str, object]:
    n6074 = load_n6074_module()
    n6074_frozen = json.loads(N6074_DATA.read_text(encoding="utf-8"))
    require(n6074.build_payload() == n6074_frozen, N6074_DATA)
    require(n6074_frozen["open_b_after_current_proved_interfaces"] == list(range(31, 50)), n6074_frozen)

    n6073 = json.loads(N6073_DATA.read_text(encoding="utf-8"))
    globalization = n6073["projective_globalization"]
    require(globalization["every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"], globalization)
    require(globalization["first_shadow_equals_the_parent_first_shadow"], globalization)
    require(globalization["second_shadow_dimension"] == 23, globalization)
    require(globalization["second_shadow_is_a_projective_flag_hook"], globalization)

    caps = frozen_caps()
    b31 = b31_hereditary_arithmetic(n6074, caps)
    b49 = b49_scalar_states(n6074, caps)
    return {
        "status": [
            "PURE_ENDPOINT_APPLICATION",
            "EXACT_INTEGER_PROFILE_REPLAY",
            "B31_AND_B49_EXCLUDED",
            "N6-075",
        ],
        "hypothesis": "the N6-074 fixed-six reduction of a hypothetical minimum 28-term ordinary Chow decomposition of perm_6",
        "frozen_prolongation_caps": caps,
        "b31_hereditary_endpoint": b31,
        "b49_fixed_six_endpoint": b49,
        "shared_geometric_route": [
            "the 49-plane X has first shadow K of dimension 75",
            "N6-073 extends X to an N6-064 fifty-plane and makes the second shadow of K a genuine 23-dimensional flag hook",
            "common W15 and literal quadratic directness make the five section-difference spaces span K",
            "the 15-plane product-shadow bound makes every pair of factor six-planes transverse and identifies the first shadow of K with their sum",
            "the pure N6-069 block proof re-applies to a transverse pair; the common-quotient domain argument of N6-061 then propagates separation to all six frames",
            "N6-059 would then bound the local permanent cubic intersection by 40, contradicting 49, so every row and column block is singular",
            "N6-072 excludes six actual all-singular frames over a genuine flag hook",
        ],
        "n6073_interface": globalization,
        "excluded_here": [31, 49],
        "frontier_before": list(range(31, 50)),
        "frontier_after": list(range(32, 49)),
        "strict_conclusion": (
            "The N6-073 forty-nine-plane extension theorem applies both to the hereditary local b=31 endpoint and to the original fixed-six b=49 endpoint. "
            "After the common-W15, directness, transversality, block-rigidity, and all-singular hook interfaces are reconnected, both layers are impossible."
        ),
        "claim_boundary": (
            "This excludes only b=31 and b=49 inside the N6-074 ordinary-rank reduction. The current fixed-six frontier is b=32,...,48. "
            "N6-073 does not classify 47- or 48-dimensional shadow-75 planes, so it does not exclude b=32 or b=48 without a new extension theorem. "
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
    if args.json is not None:
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(payload == expected, args.verify_json)
    print("excluded_here=31,49")
    print("frontier_after=32..48")
    print("N6_LOWER29_B31_B49_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
