#!/usr/bin/env python3
"""Exact scalar-state frontier for the fixed-six layer b=59 (N6-054)."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6038_DATA = ROOT / "data" / "n6_fixed_six_offcentral_c42_ceiling.json"
N6050_SCRIPT = ROOT / "scripts" / "n6_b60_scalar_frontier.py"
N6051_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
N6052_DATA = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"
PERMANENT_CUBIC_DIMENSION = 400
INTERSECTION_B = 59
EXPECTED_SHADOW = 75
EXPECTED_DEFECT_BUDGET = 3


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inherited_layer() -> dict[str, int]:
    payload = json.loads(N6038_DATA.read_text(encoding="utf-8"))
    row = next(
        item for item in payload["rows"]
        if int(item["middle_intersection_b"]) == INTERSECTION_B
    )
    shadow = int(row["fixed_middle_shadow_lower"])
    defect = 78 - shadow
    require((shadow, defect) == (EXPECTED_SHADOW, EXPECTED_DEFECT_BUDGET), row)
    return {
        "middle_intersection_b": INTERSECTION_B,
        "quadratic_shadow_lower_m_b": shadow,
        "defect_budget_D_b": defect,
    }


def canonical_states() -> list[dict[str, object]]:
    """Replay the D=3 scalar enumeration and relabel it for b=59."""

    layer = inherited_layer()
    n6050 = load_module(N6050_SCRIPT, "n6054_n6050")
    require(
        int(n6050.DEFECT_BUDGET) == layer["defect_budget_D_b"]
        and int(n6050.SHADOW_LOWER) == layer["quadratic_shadow_lower_m_b"],
        layer,
    )
    states = copy.deepcopy(n6050.canonical_states())
    for index, state in enumerate(states):
        state["state_id"] = f"b59_state_{index:03d}"
        state.pop("excluded_by_existing_cap", None)
        state.pop("exclusion_reason", None)
        state.pop("required_prolongation_dimension_lower", None)
        state.pop("applicable_prolongation_upper_cap", None)
    return states


def frozen_caps() -> dict[str, int]:
    n6050 = load_module(N6050_SCRIPT, "n6054_caps")
    caps = n6050.frozen_caps()
    n6051 = json.loads(N6051_DATA.read_text(encoding="utf-8"))
    n6052 = json.loads(N6052_DATA.read_text(encoding="utf-8"))
    caps.update(
        {
            "extremal_t15": int(
                n6051["characteristic_zero_prolongation_upper_cap_t15"]
            ),
            "alpha1_t15": int(
                n6051["characteristic_zero_prolongation_upper_cap_t15"]
            ),
            "alpha2_t15": int(
                n6052["universal_alpha2_t15_prolongation_upper_cap"]
            ),
        }
    )
    require(
        caps
        == {
            "extremal_t12": 436,
            "extremal_t13": 440,
            "extremal_t14": 448,
            "alpha1_t13": 440,
            "alpha1_t14": 448,
            "alpha2_t14": 453,
            "extremal_t15": 458,
            "alpha1_t15": 458,
            "alpha2_t15": 458,
        },
        caps,
    )
    return caps


def prune(states: list[dict[str, object]], caps: dict[str, int]) -> None:
    for state in states:
        t2 = int(state["fixed_quadratic_quotient_t2"])
        required = (
            PERMANENT_CUBIC_DIMENSION
            + int(state["fixed_middle_rank_h_lower"])
            - INTERSECTION_B
        )
        reason: str | None = None
        cap: int | None = None
        if int(state["extremal_term_count"]) and t2 in (12, 13, 14):
            reason = "N6-047 universal extremal-term cap"
            cap = caps[f"extremal_t{t2}"]
        elif int(state["alpha_one_term_count"]) and t2 in (13, 14):
            reason = "N6-048 universal alpha-one-term cap"
            cap = caps[f"alpha1_t{t2}"]
        elif int(state["alpha_two_term_count"]) and t2 == 14:
            reason = "N6-049 universal alpha-two-term cap"
            cap = caps["alpha2_t14"]
        elif int(state["extremal_term_count"]) and t2 == 15:
            reason = "N6-051 universal extremal-term t15 cap"
            cap = caps["extremal_t15"]
        elif int(state["alpha_one_term_count"]) and t2 == 15:
            reason = "N6-051 universal alpha-one-term t15 cap"
            cap = caps["alpha1_t15"]
        elif int(state["alpha_two_term_count"]) and t2 == 15:
            reason = "N6-052 universal alpha-two-term t15 cap"
            cap = caps["alpha2_t15"]

        state["required_prolongation_dimension_lower"] = required
        state["excluded_by_existing_cap"] = reason is not None
        state["exclusion_reason"] = reason
        state["applicable_prolongation_upper_cap"] = cap
        if reason is not None:
            require(cap is not None and required > cap, (state, required, cap))


def build_payload() -> dict[str, object]:
    layer = inherited_layer()
    states = canonical_states()
    caps = frozen_caps()
    prune(states, caps)
    epsilon_profiles = Counter(
        tuple(pair[0] for pair in state["epsilon_alpha_pairs"])
        for state in states
    )
    kappa_histogram = Counter(
        int(state["quadratic_relation_dimension_kappa2"]) for state in states
    )
    t2_histogram = Counter(
        int(state["fixed_quadratic_quotient_t2"]) for state in states
    )
    exclusion_histogram = Counter(
        state["exclusion_reason"] or "remaining_all_alpha_three"
        for state in states
    )
    exceptional = [
        state for state in states
        if int(state["quadratic_relation_dimension_kappa2"]) == 3
    ]
    remaining = [state for state in states if not state["excluded_by_existing_cap"]]

    expected_exclusions = {
        "N6-047 universal extremal-term cap": 226,
        "N6-048 universal alpha-one-term cap": 51,
        "N6-049 universal alpha-two-term cap": 6,
        "N6-051 universal alpha-one-term t15 cap": 21,
        "N6-051 universal extremal-term t15 cap": 56,
        "N6-052 universal alpha-two-term t15 cap": 6,
        "remaining_all_alpha_three": 1,
    }
    require(len(states) == 367, len(states))
    require(kappa_histogram == {0: 294, 1: 62, 2: 10, 3: 1}, kappa_histogram)
    require(t2_histogram == {12: 32, 13: 111, 14: 140, 15: 84}, t2_histogram)
    require(exclusion_histogram == expected_exclusions, exclusion_histogram)
    require(
        len(exceptional) == 1
        and exceptional[0]["state_id"] == "b59_state_009"
        and exceptional[0]["fixed_middle_rank_h_exact"] is None
        and exceptional[0]["fixed_middle_rank_h_lower"] == 112
        and exceptional[0]["fixed_middle_rank_h_upper"] == 120
        and exceptional[0]["required_prolongation_dimension_lower"] == 453,
        exceptional,
    )
    require(
        len(remaining) == 1
        and remaining[0]["state_id"] == "b59_state_366"
        and remaining[0]["epsilon_alpha_pairs"] == [[0, 3]] * 6
        and remaining[0]["fixed_middle_rank_h_exact"] == 120
        and remaining[0]["required_prolongation_dimension_lower"] == 461,
        remaining,
    )
    return {
        "status": "N6_054_B59_SCALAR_FRONTIER",
        "arithmetic": "exact integer exhaustive enumeration and frozen-cap comparison",
        "layer_parameters": layer,
        "prolongation_caps_used": caps,
        "canonical_state_count": len(states),
        "epsilon_profile_histogram": {
            ",".join(map(str, key)): value
            for key, value in sorted(epsilon_profiles.items())
        },
        "quadratic_relation_dimension_histogram": {
            str(key): kappa_histogram[key] for key in sorted(kappa_histogram)
        },
        "global_quotient_dimension_histogram": {
            str(key): t2_histogram[key] for key in sorted(t2_histogram)
        },
        "exclusion_histogram": dict(sorted(exclusion_histogram.items())),
        "unique_kappa3_state_id": exceptional[0]["state_id"],
        "unique_kappa3_middle_rank_window": [112, 120],
        "remaining_state_count": len(remaining),
        "remaining_state_ids": [state["state_id"] for state in remaining],
        "states": states,
        "strict_conclusion": (
            "Exactly 366 of the 367 b=59 scalar necessary states are excluded "
            "by N6-047 through N6-052. The sole remaining state is the "
            "all-alpha-three t2=15 state and requires prolongation dimension 461."
        ),
        "claim_boundary": (
            "This is a complete scalar necessary-state enumeration, not a "
            "geometric realizability classification. It does not exclude the "
            "all-alpha-three state, the b=59 layer, a hypothetical twenty-six-term "
            "decomposition, prove ChowRank(perm_6)>=27, or make a border-rank claim."
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
    print(f"canonical_states={payload['canonical_state_count']}")
    print(f"remaining_states={payload['remaining_state_count']}")
    print("N6_B59_SCALAR_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
