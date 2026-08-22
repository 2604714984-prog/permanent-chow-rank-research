#!/usr/bin/env python3
"""Exact local q=7 defect-six frontier for the N=28 program.

N6-080 adds the elementary actual-term constraint

    epsilon > 0  ==>  alpha >= 2

to the q=7, 66-to-87 shortening envelope.  It then applies only the already
proved t<=15 individual-term prolongation caps.  The result is a local state
pruning certificate, not an exclusion of the global b=34 layer.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N6074_SCRIPT = ROOT / "scripts" / "n6_lower29_fixed_six_arithmetic.py"
N6074_DATA = ROOT / "data" / "n6_lower29_fixed_six_arithmetic.json"
N6043_DATA = ROOT / "data" / "n6_near_extremal_six_plane_frontier.json"
DEFAULT_JSON = ROOT / "data" / "n6_lower29_q7_defect_six_frontier.json"

FIXED_TERMS = 7
LOCAL_CENTRAL_DIMENSION = 66
PRODUCT_SHADOW_LOWER = 87
QUADRATIC_PROJECTION_CAP = 93
DEFECT = QUADRATIC_PROJECTION_CAP - PRODUCT_SHADOW_LOWER


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def alpha_floor(epsilon: int) -> int:
    """Pure actual-term consequence of N6-043."""

    return 0 if epsilon == 0 else 2


def raw_epsilon_types() -> list[tuple[int, ...]]:
    return [
        row
        for row in combinations_with_replacement(range(16), FIXED_TERMS)
        if sum(row) - min(row) <= DEFECT
    ]


def term_feasible(row: tuple[int, ...], n6074) -> bool:
    if any(n6074.individual_middle_lower(value) is None for value in row):
        return False
    return all(
        sum(row) - row[index] + alpha_floor(row[index]) <= DEFECT
        for index in range(FIXED_TERMS)
    )


def cap_for_t_upper(t_upper: int) -> int | None:
    # These are the largest applicable already-proved caps up to the displayed
    # quotient dimension.  At t<=14 an epsilon-zero term cannot have alpha=3.
    return {12: 436, 13: 440, 14: 453}.get(t_upper)


def state_rows(n6074, feasible: list[tuple[int, ...]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for epsilon in feasible:
        relation_cap = DEFECT - sum(epsilon) + min(epsilon)
        require(relation_cap >= 0, epsilon)
        individual = [n6074.individual_middle_lower(value) for value in epsilon]
        require(all(value is not None for value in individual), epsilon)
        for kappa2 in range(relation_cap + 1):
            d2 = 15 * FIXED_TERMS - sum(epsilon) - kappa2
            t2_upper = d2 - PRODUCT_SHADOW_LOWER
            conservative_h_lower = sum(int(value) for value in individual) - 2 * n6074.macaulay_successor_degree_two(kappa2)
            # In every open profile the individual quadratic dimensions are
            # 13, 14, or 15.  Their cubic normal forms contain no nonzero pure
            # cube.  If kappa2<=1, relation factorization therefore forces the
            # cubic spaces to be literal-direct.
            pure_cube_relation_excluded = kappa2 <= 1 and max(epsilon) <= 2
            h_lower = (
                sum(int(value) for value in individual)
                if pure_cube_relation_excluded
                else conservative_h_lower
            )
            required = 400 + h_lower - LOCAL_CENTRAL_DIMENSION
            cap = cap_for_t_upper(t2_upper)
            excluded = cap is not None and required > cap
            if t2_upper <= 14:
                require(0 in epsilon and excluded, (epsilon, kappa2, t2_upper, required, cap))
                route = "excluded_by_existing_actual_term_prolongation_cap"
            elif t2_upper == 15:
                route = "open_only_if_every_epsilon_zero_term_has_alpha_three"
            else:
                require(t2_upper in (16, 17, 18), t2_upper)
                route = "open_quotient_dimension_above_existing_term_caps"
            rows.append(
                {
                    "epsilon": list(epsilon),
                    "kappa2": kappa2,
                    "d2": d2,
                    "a2_lower": PRODUCT_SHADOW_LOWER,
                    "t2_upper": t2_upper,
                    "conservative_h_lower": conservative_h_lower,
                    "h_lower": h_lower,
                    "cubic_relations_forced_zero_by_no_pure_cube": pure_cube_relation_excluded,
                    "required_prolongation_lower_if_b_local_is_66": required,
                    "existing_cap": cap,
                    "excluded": excluded,
                    "route": route,
                }
            )
    return rows


def histogram(values) -> dict[str, int]:
    return {str(key): value for key, value in sorted(Counter(values).items())}


def build_payload() -> dict[str, object]:
    n6074 = load_module(N6074_SCRIPT, "n6074_for_n6080")
    require(n6074.build_payload() == json.loads(N6074_DATA.read_text(encoding="utf-8")), N6074_DATA)
    n6043 = json.loads(N6043_DATA.read_text(encoding="utf-8"))
    require(n6043["coordinate_fixed_supports"]["five_edge_maximum_rectangle_count"] == 1, n6043)
    require("dim L at most five" in n6043["proved_geometric_consequence"], n6043["proved_geometric_consequence"])

    shadow_module = n6074.load_shadow_module()
    shadow_at_66 = int(shadow_module.minimum_ferrers_shadow(66)[0])
    require(shadow_at_66 == PRODUCT_SHADOW_LOWER, shadow_at_66)

    raw = raw_epsilon_types()
    dimension_gap = [row for row in raw if any(n6074.individual_middle_lower(value) is None for value in row)]
    after_gap = [row for row in raw if row not in dimension_gap]
    feasible = [row for row in after_gap if term_feasible(row, n6074)]
    alpha_floor_excluded = [row for row in after_gap if row not in feasible]
    rows = state_rows(n6074, feasible)
    excluded = [row for row in rows if row["excluded"]]
    open_rows = [row for row in rows if not row["excluded"]]

    require((len(raw), len(dimension_gap), len(alpha_floor_excluded), len(feasible)) == (31, 7, 6, 18), (raw, dimension_gap, alpha_floor_excluded, feasible))
    require((len(rows), len(excluded), len(open_rows)) == (56, 43, 13), (len(rows), len(excluded), len(open_rows)))
    require(histogram(row["t2_upper"] for row in rows) == {"12": 18, "13": 15, "14": 10, "15": 6, "16": 4, "17": 2, "18": 1}, rows)
    require(histogram(row["t2_upper"] for row in open_rows) == {"15": 6, "16": 4, "17": 2, "18": 1}, open_rows)
    require(sum(row["cubic_relations_forced_zero_by_no_pure_cube"] for row in open_rows) == 10, open_rows)

    return {
        "status": "N6_080_Q7_DEFECT_SIX_LOCAL_FRONTIER",
        "local_hypothesis": {
            "fixed_terms": FIXED_TERMS,
            "local_central_intersection_dimension": LOCAL_CENTRAL_DIMENSION,
            "exact_product_shadow_lower": PRODUCT_SHADOW_LOWER,
            "quadratic_projection_cap": QUADRATIC_PROJECTION_CAP,
            "defect_budget": DEFECT,
        },
        "pure_actual_term_lemma": {
            "statement": "epsilon>0 forces factor-span dimension at most five, hence alpha>=2 by N6-043",
            "reason": [
                "six factors spanning six dimensions are independent and have quadratic derivative dimension 15",
                "therefore epsilon>0 forces the factor span to have dimension at most five",
                "N6-043 gives dim(E2 intersect Sym2 L)<=1 for such a span",
                "D2(T) is contained in Sym2 L, so 3-alpha=dim(E2 intersect D2(T))<=1",
            ],
        },
        "epsilon_type_pruning": {
            "raw_symmetric_type_count": len(raw),
            "quadratic_dimension_twelve_gap_excluded_count": len(dimension_gap),
            "quadratic_dimension_twelve_gap_excluded": [list(row) for row in dimension_gap],
            "positive_epsilon_alpha_floor_excluded_count": len(alpha_floor_excluded),
            "positive_epsilon_alpha_floor_excluded": [list(row) for row in alpha_floor_excluded],
            "feasible_symmetric_type_count": len(feasible),
            "feasible_symmetric_types": [list(row) for row in feasible],
        },
        "relation_envelope": {
            "state_count": len(rows),
            "t2_upper_histogram": histogram(row["t2_upper"] for row in rows),
            "existing_cap_excluded_count": len(excluded),
            "open_state_count": len(open_rows),
            "open_t2_upper_histogram": histogram(row["t2_upper"] for row in open_rows),
            "open_t15_state_count": sum(row["t2_upper"] == 15 for row in open_rows),
            "open_t16_to_t18_state_count": sum(row["t2_upper"] >= 16 for row in open_rows),
            "open_states_with_cubic_directness_forced_by_kappa_at_most_one": sum(
                row["cubic_relations_forced_zero_by_no_pure_cube"] for row in open_rows
            ),
            "states": rows,
        },
        "strict_local_conclusion": (
            "The termwise alpha floor and the existing t<=14 prolongation caps remove "
            "43 of 56 q=7 defect-six relation-envelope states.  Exactly 13 envelope "
            "states remain: six at t2_upper=15 and seven at t2_upper=16,17,18."
        ),
        "next_geometric_targets": [
            "classify the t2=15 packets in which every epsilon-zero term has alpha=3",
            "prove new actual-term or coupled caps for quotient dimensions 16,17,18",
            "separately justify that a global b=34 survivor reaches the local b_local=66 equality packet",
        ],
        "claim_boundary": (
            "This is a local exact state pruning conditional on a seven-term coupled packet "
            "with central intersection 66.  It does not force such a packet from global b=34, "
            "does not exclude b=34, does not prove ChowRank(perm_6)>=29, and makes no "
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
    print("epsilon_types=31 -> 18")
    print("relation_states=56 excluded=43 open=13")
    print("N6_LOWER29_Q7_DEFECT_SIX_FRONTIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
