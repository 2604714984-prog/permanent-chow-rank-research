#!/usr/bin/env python3
"""Exact scalar-state frontier for the fixed-six layer b=60 (N6-050)."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6047_DATA = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"
N6048_DATA = ROOT / "data" / "n6_alpha1_prolongation_closure.json"
N6049_DATA = ROOT / "data" / "n6_alpha2_prolongation_exclusion.json"

FIXED_TERMS = 6
PERMANENT_QUADRATIC_DIMENSION = 225
PERMANENT_CUBIC_DIMENSION = 400
INTERSECTION_B = 60
SHADOW_LOWER = 75
DEFECT_BUDGET = 3


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def central_rank(epsilon: int) -> int:
    if epsilon in (0, 1):
        return 20
    if epsilon == 2:
        return 18
    raise ValueError(epsilon)


def canonical_states() -> list[dict[str, object]]:
    """Enumerate every permutation class allowed by the proved scalar bounds."""

    states: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()

    # The omitted-factor inequality forces min(epsilon)=0 and every other
    # epsilon<=3.  Epsilon=3 would be the impossible quadratic dimension 12.
    for epsilon in product(range(3), repeat=FIXED_TERMS):
        if tuple(sorted(epsilon)) != epsilon:
            continue
        omitted_defect = sum(epsilon) - min(epsilon)
        if omitted_defect > DEFECT_BUDGET:
            continue

        for alpha in product(range(4), repeat=FIXED_TERMS):
            pairs = tuple(sorted(zip(epsilon, alpha)))
            if tuple(zip(epsilon, alpha)) != pairs:
                continue
            if any(
                sum(epsilon) - epsilon[index] + alpha[index]
                > DEFECT_BUDGET
                for index in range(FIXED_TERMS)
            ):
                continue

            relation_cap = (
                DEFECT_BUDGET
                - sum(epsilon)
                - max(
                    alpha[index] - epsilon[index]
                    for index in range(FIXED_TERMS)
                )
            )
            if relation_cap < 0:
                continue

            for kappa2 in range(relation_cap + 1):
                d2 = 90 - sum(epsilon) - kappa2
                a2_upper = 78 - omitted_defect
                for a2 in range(SHADOW_LOWER, a2_upper + 1):
                    t2 = d2 - a2
                    individual_quotients = tuple(
                        12 - epsilon[index] + alpha[index]
                        for index in range(FIXED_TERMS)
                    )
                    if t2 < max(individual_quotients):
                        continue

                    key = (pairs, kappa2, a2, t2)
                    if key in seen:
                        continue
                    seen.add(key)

                    middle_sum = sum(central_rank(value) for value in epsilon)
                    if kappa2 <= 2:
                        h_lower = middle_sum
                        h_upper = middle_sum
                        h_exact: int | None = middle_sum
                        cubic_relation_cap = 0
                    else:
                        # The enumeration forces the unique kappa2=3 state.
                        # Macaulay gives rho3<=3^{<2>}=4 and block Sylvester
                        # gives h>=120-2*rho3=112.  No exact h is claimed.
                        require(
                            kappa2 == 3
                            and all(pair == (0, 0) for pair in pairs),
                            key,
                        )
                        cubic_relation_cap = 4
                        h_lower = middle_sum - 2 * cubic_relation_cap
                        h_upper = middle_sum
                        h_exact = None

                    states.append(
                        {
                            "epsilon_alpha_pairs": [list(pair) for pair in pairs],
                            "quadratic_relation_dimension_kappa2": kappa2,
                            "cubic_relation_dimension_upper_rho3": (
                                cubic_relation_cap
                            ),
                            "fixed_quadratic_rank_d2": d2,
                            "fixed_quadratic_intersection_a2": a2,
                            "fixed_quadratic_quotient_t2": t2,
                            "individual_quotient_dimensions": list(
                                sorted(individual_quotients)
                            ),
                            "individual_middle_rank_sum": middle_sum,
                            "fixed_middle_rank_h_exact": h_exact,
                            "fixed_middle_rank_h_lower": h_lower,
                            "fixed_middle_rank_h_upper": h_upper,
                            "extremal_term_count": sum(
                                pair == (0, 0) for pair in pairs
                            ),
                            "alpha_one_term_count": sum(
                                pair == (0, 1) for pair in pairs
                            ),
                            "alpha_two_term_count": sum(
                                pair == (0, 2) for pair in pairs
                            ),
                        }
                    )

    states.sort(
        key=lambda row: (
            row["epsilon_alpha_pairs"],
            row["quadratic_relation_dimension_kappa2"],
            row["fixed_quadratic_intersection_a2"],
            row["fixed_quadratic_quotient_t2"],
        )
    )
    for index, state in enumerate(states):
        state["state_id"] = f"b60_state_{index:03d}"
    return states


def frozen_caps() -> dict[str, int]:
    n6047 = json.loads(N6047_DATA.read_text(encoding="utf-8"))
    n6048 = json.loads(N6048_DATA.read_text(encoding="utf-8"))
    n6049 = json.loads(N6049_DATA.read_text(encoding="utf-8"))
    base_caps = {
        key: int(value)
        for key, value in n6047["fixed_point_cap_audit"][
            "characteristic_zero_prolongation_upper_caps"
        ].items()
    }
    require(base_caps == {"12": 436, "13": 440, "14": 448}, base_caps)
    require(
        {
            key: int(value)
            for key, value in n6048["pure_alpha1_prolongation_caps"].items()
        }
        == {"13": 440, "14": 448},
        n6048["pure_alpha1_prolongation_caps"],
    )
    alpha2_cap = int(n6049["one_rectangle_universal_prolongation_cap"])
    require(alpha2_cap == 453, alpha2_cap)
    return {
        "extremal_t12": base_caps["12"],
        "extremal_t13": base_caps["13"],
        "extremal_t14": base_caps["14"],
        "alpha1_t13": base_caps["13"],
        "alpha1_t14": base_caps["14"],
        "alpha2_t14": alpha2_cap,
    }


def prune(states: list[dict[str, object]], caps: dict[str, int]) -> None:
    for state in states:
        t2 = int(state["fixed_quadratic_quotient_t2"])
        h_lower = int(state["fixed_middle_rank_h_lower"])
        required = PERMANENT_CUBIC_DIMENSION + h_lower - INTERSECTION_B
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

        if reason is None:
            state["excluded_by_existing_cap"] = False
            state["exclusion_reason"] = None
            state["required_prolongation_dimension_lower"] = required
            state["applicable_prolongation_upper_cap"] = None
        else:
            require(cap is not None and required > cap, (state, required, cap))
            state["excluded_by_existing_cap"] = True
            state["exclusion_reason"] = reason
            state["required_prolongation_dimension_lower"] = required
            state["applicable_prolongation_upper_cap"] = cap


def build_payload() -> dict[str, object]:
    states = canonical_states()
    caps = frozen_caps()
    prune(states, caps)

    epsilon_profiles = Counter(
        tuple(pair[0] for pair in state["epsilon_alpha_pairs"])
        for state in states
    )
    kappa_histogram = Counter(
        int(state["quadratic_relation_dimension_kappa2"])
        for state in states
    )
    t2_histogram = Counter(
        int(state["fixed_quadratic_quotient_t2"]) for state in states
    )
    exclusion_histogram = Counter(
        state["exclusion_reason"] or "remaining_t15_frontier"
        for state in states
    )
    remaining = [state for state in states if not state["excluded_by_existing_cap"]]
    exceptional = [
        state
        for state in states
        if int(state["quadratic_relation_dimension_kappa2"]) == 3
    ]

    require(len(states) == 367, len(states))
    require(kappa_histogram == {0: 294, 1: 62, 2: 10, 3: 1}, kappa_histogram)
    require(t2_histogram == {12: 32, 13: 111, 14: 140, 15: 84}, t2_histogram)
    require(
        exclusion_histogram
        == {
            "N6-047 universal extremal-term cap": 226,
            "N6-048 universal alpha-one-term cap": 51,
            "N6-049 universal alpha-two-term cap": 6,
            "remaining_t15_frontier": 84,
        },
        exclusion_histogram,
    )
    require(len(exceptional) == 1, exceptional)
    require(
        exceptional[0]["state_id"] == "b60_state_009"
        and exceptional[0]["fixed_middle_rank_h_exact"] is None
        and exceptional[0]["fixed_middle_rank_h_lower"] == 112
        and exceptional[0]["fixed_middle_rank_h_upper"] == 120,
        exceptional,
    )
    require(
        all(
            state["fixed_quadratic_quotient_t2"] == 15
            and state["quadratic_relation_dimension_kappa2"] == 0
            and state["fixed_quadratic_rank_d2"] == 90
            and state["fixed_quadratic_intersection_a2"] == 75
            and state["fixed_middle_rank_h_exact"] == 120
            and all(pair[0] == 0 for pair in state["epsilon_alpha_pairs"])
            for state in remaining
        ),
        remaining,
    )

    return {
        "status": "N6_050_B60_SCALAR_FRONTIER",
        "arithmetic": "exact integer exhaustive enumeration and cap comparison",
        "layer_parameters": {
            "middle_intersection_b": INTERSECTION_B,
            "quadratic_shadow_lower_m_b": SHADOW_LOWER,
            "defect_budget_D_b": DEFECT_BUDGET,
        },
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
            "All 283 b=60 canonical states with t2 at most fourteen are "
            "excluded by the N6-047, N6-048, and universal N6-049 term caps. "
            "Exactly 84 t2=15 states remain."
        ),
        "claim_boundary": (
            "This is a complete scalar necessary-state enumeration, not a "
            "geometric realizability classification. It does not exclude the "
            "84 t2=15 states, a hypothetical twenty-six-term decomposition, "
            "prove ChowRank(perm_6)>=27, or make a border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"canonical_states={payload['canonical_state_count']}")
    print(f"remaining_t15_states={payload['remaining_state_count']}")
    print("N6_B60_SCALAR_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
