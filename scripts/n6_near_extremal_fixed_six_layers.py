#!/usr/bin/env python3
"""Exact arithmetic reduction for the N6 fixed-six layers b=61,62,63.

The mathematical input is N6-038's omitted-factor defect inequalities,
N6-031's single-term catalectic profiles, and the extremal six-plane theorem.
This script only enumerates their exact integer consequences.  It makes no
realizability claim for any surviving integer state.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6038_DATA = ROOT / "data" / "n6_fixed_six_offcentral_c42_ceiling.json"
RANK_GAP_DATA = ROOT / "data" / "n6_single_term_middle_rank_gap.json"

LAYERS = {61: 76, 62: 77, 63: 77}
FIXED_TERMS = 6
PERM_MIDDLE_RANK = 400
RESIDUAL_TERMS = 20
TERM_MIDDLE_CAP = 20


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def central_rank_from_defect(epsilon: int) -> int:
    """Exact rank in the only near-extremal defect profiles that occur."""

    if epsilon in (0, 1):
        return 20
    if epsilon == 2:
        return 18
    raise ValueError(epsilon)


def canonical_states(intersection: int, shadow: int) -> list[dict[str, object]]:
    """Enumerate permutation classes of all proved scalar constraints."""

    defect_budget = 78 - shadow
    states: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()

    # The omitted-factor inequality forces min(epsilon)=0 and epsilon<=2 in
    # these layers, so this is already exhaustive.
    for epsilon in product(range(3), repeat=FIXED_TERMS):
        if tuple(sorted(epsilon)) != epsilon:
            continue
        if sum(epsilon) - min(epsilon) > defect_budget:
            continue

        for alpha in product(range(4), repeat=FIXED_TERMS):
            pairs = tuple(sorted(zip(epsilon, alpha)))
            if tuple(zip(epsilon, alpha)) != pairs:
                continue
            if any(
                sum(epsilon) - epsilon[index] + alpha[index] > defect_budget
                for index in range(FIXED_TERMS)
            ):
                continue

            relation_cap = (
                defect_budget
                - sum(epsilon)
                - max(alpha[index] - epsilon[index] for index in range(FIXED_TERMS))
            )
            if relation_cap < 0:
                continue

            for kappa2 in range(relation_cap + 1):
                quadratic_rank = 90 - sum(epsilon) - kappa2
                intersection_upper = 78 - (sum(epsilon) - min(epsilon))
                for a2 in range(shadow, intersection_upper + 1):
                    t2 = quadratic_rank - a2
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

                    # If kappa2=0 the middle spaces are visibly direct.  If
                    # kappa2=1, a relation component would be a cube, excluded
                    # by the exact near-extremal normal forms.  If kappa2=2,
                    # the enumeration itself forces epsilon=alpha=0; the
                    # extremal theorem makes every term squarefree and the
                    # binary-cubic lemma again makes the middle sum direct.
                    if kappa2 == 2:
                        require(all(pair == (0, 0) for pair in pairs), key)

                    middle_rank = sum(
                        central_rank_from_defect(value) for value in epsilon
                    )
                    residual_middle_lower = (
                        PERM_MIDDLE_RANK + middle_rank - 2 * intersection
                    )
                    residual_defect_relation_budget = (
                        RESIDUAL_TERMS * TERM_MIDDLE_CAP - residual_middle_lower
                    )
                    minimum_full_residual_terms = (
                        RESIDUAL_TERMS - residual_defect_relation_budget // 2
                    )
                    extremal_terms = sum(
                        value == 0 and loss == 0 for value, loss in pairs
                    )

                    states.append(
                        {
                            "epsilon_alpha_pairs": [list(pair) for pair in pairs],
                            "quadratic_relation_dimension_kappa2": kappa2,
                            "fixed_quadratic_rank_d2": quadratic_rank,
                            "fixed_quadratic_intersection_a2": a2,
                            "fixed_quadratic_quotient_t2": t2,
                            "individual_quotient_dimensions": list(
                                sorted(individual_quotients)
                            ),
                            "extremal_rectangle_term_count": extremal_terms,
                            "fixed_middle_rank_h": middle_rank,
                            "residual_middle_rank_lower": residual_middle_lower,
                            "residual_defect_plus_relation_budget": (
                                residual_defect_relation_budget
                            ),
                            "minimum_full_middle_rank_residual_terms": (
                                minimum_full_residual_terms
                            ),
                        }
                    )

    return sorted(
        states,
        key=lambda row: (
            row["epsilon_alpha_pairs"],
            row["quadratic_relation_dimension_kappa2"],
            row["fixed_quadratic_intersection_a2"],
            row["fixed_quadratic_quotient_t2"],
        ),
    )


def profile_summary(states: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[tuple[int, ...], list[dict[str, object]]] = {}
    for state in states:
        profile = tuple(pair[0] for pair in state["epsilon_alpha_pairs"])
        buckets.setdefault(profile, []).append(state)

    answer: list[dict[str, object]] = []
    for profile, rows in sorted(buckets.items()):
        answer.append(
            {
                "sorted_epsilon_profile": list(profile),
                "canonical_scalar_state_count": len(rows),
                "fixed_middle_rank_h": sorted(
                    {int(row["fixed_middle_rank_h"]) for row in rows}
                ),
                "quadratic_relation_dimensions": sorted(
                    {
                        int(row["quadratic_relation_dimension_kappa2"])
                        for row in rows
                    }
                ),
                "fixed_quadratic_intersections_a2": sorted(
                    {int(row["fixed_quadratic_intersection_a2"]) for row in rows}
                ),
                "fixed_quadratic_quotients_t2": sorted(
                    {int(row["fixed_quadratic_quotient_t2"]) for row in rows}
                ),
                "extremal_rectangle_term_count_range": [
                    min(int(row["extremal_rectangle_term_count"]) for row in rows),
                    max(int(row["extremal_rectangle_term_count"]) for row in rows),
                ],
                "residual_middle_rank_lower": min(
                    int(row["residual_middle_rank_lower"]) for row in rows
                ),
                "minimum_full_middle_rank_residual_terms": min(
                    int(row["minimum_full_middle_rank_residual_terms"])
                    for row in rows
                ),
            }
        )
    return answer


def build_payload() -> dict[str, object]:
    n6038 = json.loads(N6038_DATA.read_text(encoding="utf-8"))
    inherited = {
        int(row["middle_intersection_b"]): int(row["fixed_middle_shadow_lower"])
        for row in n6038["rows"]
        if int(row["middle_intersection_b"]) in LAYERS
    }
    require(inherited == LAYERS, ("N6-038 shadow mismatch", inherited))

    rank_gap = json.loads(RANK_GAP_DATA.read_text(encoding="utf-8"))
    require(rank_gap["excluded_middle_rank"] == 19, rank_gap)
    require(
        rank_gap["factor_span_five_support_profiles"]
        == {"1": 14, "2": 14, "3": 18, "4": 20, "5": 20},
        rank_gap,
    )

    layers: list[dict[str, object]] = []
    for intersection, shadow in LAYERS.items():
        states = canonical_states(intersection, shadow)
        summary = profile_summary(states)
        layers.append(
            {
                "middle_intersection_b": intersection,
                "shadow_lower_m_b": shadow,
                "defect_budget_D_b": 78 - shadow,
                "canonical_scalar_state_count": len(states),
                "profile_summary": summary,
                "states": states,
            }
        )

    by_b = {int(row["middle_intersection_b"]): row for row in layers}
    require(by_b[61]["canonical_scalar_state_count"] == 73, by_b[61])
    require(by_b[62]["canonical_scalar_state_count"] == 11, by_b[62])
    require(by_b[63]["canonical_scalar_state_count"] == 11, by_b[63])

    # The strict conclusions below are deliberately asserted separately from
    # the enumeration so accidental weakening changes the replay result.
    for intersection in (62, 63):
        require(
            {int(state["fixed_middle_rank_h"]) for state in by_b[intersection]["states"]}
            == {120},
            by_b[intersection],
        )
    require(
        {int(state["fixed_middle_rank_h"]) for state in by_b[61]["states"]}
        == {118, 120},
        by_b[61],
    )

    highlighted: list[dict[str, object]] = []
    for layer in layers:
        intersection = int(layer["middle_intersection_b"])
        for state in layer["states"]:
            profile = [pair[0] for pair in state["epsilon_alpha_pairs"]]
            condition = (
                (intersection in (62, 63) and profile == [0, 0, 0, 0, 0, 1])
                or (intersection == 61 and profile in ([0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 1, 1]))
                or (
                    intersection == 61
                    and profile == [0, 0, 0, 0, 0, 1]
                    and state["quadratic_relation_dimension_kappa2"] == 1
                )
            )
            if condition:
                require(state["fixed_quadratic_quotient_t2"] == 12, state)
                require(state["extremal_rectangle_term_count"] >= 4, state)
                highlighted.append(
                    {
                        "middle_intersection_b": intersection,
                        "epsilon_alpha_pairs": state["epsilon_alpha_pairs"],
                        "quadratic_relation_dimension_kappa2": state[
                            "quadratic_relation_dimension_kappa2"
                        ],
                        "common_quotient_dimension": 12,
                        "extremal_rectangle_term_count": state[
                            "extremal_rectangle_term_count"
                        ],
                    }
                )

    return {
        "status": "EXACT_NEAR_EXTREMAL_FIXED_SIX_REDUCTION",
        "arithmetic": "exact integer enumeration",
        "conditional_on": [
            "N6-038 omitted-factor and projection inequalities",
            "N6-031 single-term middle-rank profiles and missing-rank-19 theorem",
            "the extremal six-plane classification",
            "N6-025 binary-cubic and relation-factorization lemmas",
            "cubic directness implies D2(R) equals the sum of the six termwise quadratic spaces",
        ],
        "layers": layers,
        "highlighted_common_quotient_states": highlighted,
        "strict_conclusions": {
            "b62_b63_fixed_middle_rank": 120,
            "b61_fixed_middle_rank_possibilities": [118, 120],
            "b61_rank118_unique_epsilon_profile": [0, 0, 0, 0, 0, 2],
            "b61_h120_residual_middle_lower": 398,
            "b61_h118_residual_middle_lower": 396,
            "b62_residual_middle_lower": 396,
            "b63_residual_middle_lower": 394,
            "minimum_full_rank_residual_terms": {
                "b61_h120": 19,
                "b61_h118": 18,
                "b62": 18,
                "b63": 17,
            },
        },
        "claim_boundary": (
            "These are necessary characteristic-zero consequences of a hypothetical "
            "26-term decomposition.  The 73/11/11 scalar states are not asserted "
            "realizable.  Only terms with epsilon=alpha=0 are placed in the 5580 "
            "extremal support components; the near-extremal alpha=1 or 2 loci remain "
            "unclassified.  No b-layer and no hypothetical decomposition is excluded."
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
    print(rendered, end="")
    print("N6_NEAR_EXTREMAL_FIXED_SIX_LAYERS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
