#!/usr/bin/env python3
"""Exact endpoint application excluding the N=28 layers b=33 and b=47."""

from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6074_SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6075_SCRIPT = ROOT / "scripts" / "n6_lower29_b31_b49_exclusion.py"
N6075_DATA = ROOT / "data" / "n6_lower29_b31_b49_exclusion.json"
N6078_DATA = ROOT / "data" / "n6_product_shadow_b47_equality_locus.json"
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


def fixed_six_states(b: int, n6074, caps: dict[str, int]) -> dict[str, object]:
    shadow = 75
    defect = 3
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
            if max(n6074.selection_lower(20, b), h_lower) > n6074.residual_upper(20, b):
                continue
            d2 = 90 - sum(epsilon) - kappa2
            t2_upper = d2 - shadow
            required = 400 + h_lower - b
            all_three = epsilon == (0,) * 6 and kappa2 == 0
            cap = caps[str(t2_upper)]
            excluded = not all_three and required > cap
            if not all_three:
                require(0 in epsilon and excluded, (epsilon, kappa2, required, cap))
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
                    "excluded_by_existing_cap": excluded,
                }
            )
    require(len(states) == 13, states)
    survivors = [row for row in states if not row["excluded_by_existing_cap"]]
    require(len(survivors) == 1 and survivors[0]["epsilon"] == [0] * 6 and survivors[0]["kappa2"] == 0, survivors)
    survivor = survivors[0]
    return {
        "exact_shadow": shadow,
        "defect_budget": defect,
        "scalar_state_count": len(states),
        "cap_excluded_state_count": len(states) - 1,
        "unique_pre_geometry_state": {
            **survivor,
            "alpha": [3] * 6,
            "alpha_at_most_two_subcase_cap": caps["15"],
            "alpha_at_most_two_subcase_strict_gap": survivor["required_prolongation_lower"] - caps["15"],
            "a2": 75,
            "t2": 15,
            "h": 120,
            "six_middle_images_literal_direct": True,
        },
        "states": states,
    }


def b33_hereditary(n6074, n6075, caps: dict[str, int]) -> dict[str, object]:
    dim_s = 367
    shadow_module = n6074.load_shadow_module()
    shadow = lambda dimension: int(shadow_module.minimum_ferrers_shadow(dimension)[0])
    shadow_values = {dimension: shadow(dimension) for dimension in range(47, 54)}
    require(shadow_values == {47: 75, 48: 75, 49: 75, 50: 75, 51: 78, 52: 78, 53: 81}, shadow_values)

    initial_ell16 = dim_s - 52
    initial_ell6 = initial_ell16 - 200
    require((initial_ell16, initial_ell6) == (315, 115), (initial_ell16, initial_ell6))
    defect_zero = []
    for x in (51, 52):
        required = 400 + initial_ell6 - x
        require(required > caps["12"], required)
        defect_zero.append({"x": x, "required": required, "cap": caps["12"], "gap": required - caps["12"]})

    stages = []
    for f, allowed_x, routes in (
        (50, (50,), ("N6-064",)),
        (49, (50, 49), ("N6-064", "N6-073_then_N6-064")),
        (48, (50, 49, 48), ("N6-064", "N6-073_then_N6-064", "N6-076_then_N6-064")),
    ):
        ell16 = dim_s - f
        ell6 = ell16 - 200
        cases = []
        for x, route in zip(allowed_x, routes):
            required = 400 + ell6 - x
            cases.append({"x": x, "required_prolongation_lower": required, "profile": n6075.alpha_three_forcing(required, caps), "extension_route": route})
        stages.append({"assumed_f_A": f, "sixteen_term_literal_floor": ell16, "six_term_literal_floor": ell6, "cases": cases})

    # At f=48 the sixteen-set floor is 319, so the rank-19 gap forces all
    # individual U_i to have rank twenty before the local profile is used.
    n6031 = json.loads(N6031_DATA.read_text(encoding="utf-8"))
    require(int(n6031["excluded_middle_rank"]) == 19, n6031)
    require(stages[-1]["sixteen_term_literal_floor"] == 319 > 318, stages[-1])
    stages[-1]["all_individual_middle_ranks_are_twenty"] = True

    f_floor = dim_s - 320
    require(f_floor == 47, f_floor)
    final_cases = []
    for x, route in (
        (50, "N6-064"),
        (49, "N6-073_then_N6-064"),
        (48, "N6-076_then_N6-064"),
        (47, "N6-078_then_N6-064"),
    ):
        required = 400 + 120 - x
        final_cases.append({"x": x, "required_prolongation": required, "profile": n6075.alpha_three_forcing(required, caps), "extension_route": route})
    return {
        "global_residual_permanent_intersection_floor": dim_s,
        "shadow_values": {str(key): value for key, value in shadow_values.items()},
        "initial_bounds": {
            "x_A_upper": 52,
            "sixteen_term_literal_floor": initial_ell16,
            "six_term_literal_floor": initial_ell6,
            "defect_zero_cases": defect_zero,
        },
        "successive_excluded_f_levels": stages,
        "forced_directness": {
            "f_A_dimension": f_floor,
            "global_residual_permanent_intersection_dimension": dim_s,
            "every_sixteen_term_literal_dimension": 320,
            "every_sixteen_term_family_literal_direct": True,
            "every_six_term_literal_dimension": 120,
        },
        "final_x_cases": final_cases,
        "last_case_uses_N6-078": True,
    }


def build_payload() -> dict[str, object]:
    n6074 = load_module(N6074_SCRIPT, "n6074_for_n6079")
    n6075 = load_module(N6075_SCRIPT, "n6075_for_n6079")
    require(n6074.build_payload() == json.loads(N6074_DATA.read_text(encoding="utf-8")), N6074_DATA)
    require(n6075.build_payload() == json.loads(N6075_DATA.read_text(encoding="utf-8")), N6075_DATA)
    caps = n6075.frozen_caps()
    n6078 = json.loads(N6078_DATA.read_text(encoding="utf-8"))["projective_globalization"]
    n6076 = json.loads(N6076_DATA.read_text(encoding="utf-8"))["projective_globalization"]
    n6073 = json.loads(N6073_DATA.read_text(encoding="utf-8"))["projective_globalization"]
    require(n6078["every_47_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"], n6078)
    return {
        "status": "N6_079_LOWER29_B33_B47_EXCLUSION",
        "hypothesis": "N=28 ordinary Chow decomposition after the N6-074 fixed-six reduction",
        "frozen_prolongation_caps": caps,
        "b33_hereditary_endpoint": b33_hereditary(n6074, n6075, caps),
        "b47_fixed_six_endpoint": fixed_six_states(47, n6074, caps),
        "extension_interfaces": {"N6-073": n6073, "N6-076": n6076, "N6-078": n6078},
        "shared_geometric_route": [
            "N6-078/N6-076/N6-073 extends the 47/48/49-plane to an N6-064 parent with the same K75",
            "N6-064 makes the second shadow a genuine 23-dimensional flag hook",
            "15-plane product-shadow equality makes all six factor spans six-dimensional and pairwise transverse",
            "N6-069 and N6-061/N6-059 exclude an invertible row or column block",
            "N6-072 excludes the remaining all-singular hook",
        ],
        "frontier_before": list(range(33, 48)),
        "excluded_here": [33, 47],
        "frontier_after": list(range(34, 47)),
        "strict_conclusion": "The ordinary lower-29 fixed-six frontier is reduced to b=34,...,46.",
        "claim_boundary": (
            "This excludes only b=33 and b=47 inside the N6-074 reduction. "
            "At b=34 the best q=7 shortening has dimension 66 and shadow 87 "
            "against projection cap 93; the defect-six layer is not classified. "
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
    print("excluded_here=33,47")
    print("frontier_after=34..46")
    print("N6_LOWER29_B33_B47_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
