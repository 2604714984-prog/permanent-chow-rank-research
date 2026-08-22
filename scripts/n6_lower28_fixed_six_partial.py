#!/usr/bin/env python3
"""Exact integer interfaces for the partial lower-28 fixed-six route (N6-058)."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower28_fixed_six_partial.json"
TOTAL_TERMS = 27
FIXED_TERMS = 6
RESIDUAL_TERMS = 21
PERMANENT_MIDDLE_RANK = 400
TERM_MIDDLE_CAP = 20
TERM_QUADRATIC_CAP = 15
FIXED_SIX_PROJECTION_CAP = 78
N6047_DATA = ROOT / "data" / "n6_global_quotient_prolongation_caps.json"
N6051_DATA = ROOT / "data" / "n6_global_t15_prolongation_cap.json"
N6052_DATA = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"
N6049_DATA = ROOT / "data" / "n6_alpha2_prolongation_exclusion.json"


def ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def colex_subsets(size: int) -> list[tuple[int, ...]]:
    return sorted(combinations(range(6), size), key=lambda s: sum(1 << x for x in s))


def product_shadow_data() -> tuple[list[int], list[int]]:
    seen: set[tuple[int, int]] = set()
    k = [0]
    weights = []
    for triple in colex_subsets(3):
        pairs = set(combinations(triple, 2))
        weights.append(len(pairs - seen))
        seen.update(pairs)
        k.append(len(seen))
    assert (len(k), len(weights), len(seen)) == (21, 20, 15)
    return k, weights


def product_shadow_minimum(total: int) -> int:
    k, weights = product_shadow_data()

    @lru_cache(maxsize=None)
    def dp(index: int, previous: int, remaining: int) -> int:
        if index == 20:
            return 0 if remaining == 0 else 10**9
        best = 10**9
        for value in range(min(previous, remaining) + 1):
            if remaining - value > value * (19 - index):
                continue
            best = min(
                best,
                weights[index] * k[value]
                + dp(index + 1, value, remaining - value),
            )
        return best

    return dp(0, 20, total)


def macaulay_successor_degree_two(value: int) -> int:
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    assert 0 <= remainder < largest
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def individual_middle_lower(epsilon: int) -> int | None:
    quadratic_dimension = TERM_QUADRATIC_CAP - epsilon
    if quadratic_dimension in (15, 14):
        return 20
    if quadratic_dimension == 13:
        return 18
    if quadratic_dimension == 12:
        return None
    if quadratic_dimension == 11:
        return 14
    if 0 <= quadratic_dimension <= 10:
        return 0
    raise ValueError(epsilon)


def profile_lower(b: int, shadow: int) -> dict[str, object]:
    defect_budget = FIXED_SIX_PROJECTION_CAP - shadow
    feasible = []
    impossible = 0
    total_admissible = 0
    for epsilon in combinations_with_replacement(range(16), FIXED_TERMS):
        omitted_defect = sum(epsilon) - min(epsilon)
        if omitted_defect > defect_budget:
            continue
        total_admissible += 1
        individual = [individual_middle_lower(value) for value in epsilon]
        if any(value is None for value in individual):
            impossible += 1
            continue
        quadratic_relation_cap = defect_budget - omitted_defect
        cubic_relation_cap = macaulay_successor_degree_two(quadratic_relation_cap)
        middle_lower = sum(int(value) for value in individual) - 2 * cubic_relation_cap
        feasible.append(
            (
                middle_lower,
                epsilon,
                quadratic_relation_cap,
                cubic_relation_cap,
            )
        )
    minimum = min(row[0] for row in feasible)
    minimizers = [row for row in feasible if row[0] == minimum]
    return {
        "defect_budget": defect_budget,
        "admissible_symmetric_epsilon_type_count": total_admissible,
        "feasible_symmetric_epsilon_type_count": len(feasible),
        "impossible_quadratic_rank_twelve_type_count": impossible,
        "profile_middle_rank_lower": minimum,
        "profile_minimizer_count": len(minimizers),
        "first_profile_minimizer": {
            "epsilon": list(minimizers[0][1]),
            "quadratic_relation_cap": minimizers[0][2],
            "cubic_relation_cap": minimizers[0][3],
        },
    }


def low_maximum_rank_branches() -> list[dict[str, object]]:
    branches = []
    for maximum_rank, maximum_z, quadratic_cap in ((16, 16, 11), (17, 29, 11), (18, 43, 13)):
        maximum_tau = TOTAL_TERMS * maximum_rank - PERMANENT_MIDDLE_RANK - 2 * maximum_z
        average_lower = ceiling(
            Fraction(
                maximum_rank * 26
                + 5 * (PERMANENT_MIDDLE_RANK - maximum_tau - maximum_rank),
                26,
            )
        )
        intersection_lower = average_lower - maximum_z
        shadow = product_shadow_minimum(intersection_lower)
        projection_cap = 5 * quadratic_cap + 3
        assert shadow > projection_cap
        branches.append(
            {
                "maximum_individual_middle_rank": maximum_rank,
                "global_extra_span_z_upper": maximum_z,
                "pairing_rank_tau_upper_at_z_upper": maximum_tau,
                "selected_six_middle_rank_lower": average_lower,
                "selected_six_intersection_b_lower": intersection_lower,
                "individual_quadratic_rank_cap": quadratic_cap,
                "fixed_six_quadratic_projection_cap": projection_cap,
                "exact_product_shadow_at_b_lower": shadow,
                "contradiction": "product shadow exceeds fixed-six projection cap",
            }
        )
    return branches


def frozen_prolongation_caps() -> dict[str, int]:
    n6047 = json.loads(N6047_DATA.read_text(encoding="utf-8"))
    n6051 = json.loads(N6051_DATA.read_text(encoding="utf-8"))
    n6052 = json.loads(N6052_DATA.read_text(encoding="utf-8"))
    n6049 = json.loads(N6049_DATA.read_text(encoding="utf-8"))
    base = {
        str(key): int(value)
        for key, value in n6047["fixed_point_cap_audit"][
            "characteristic_zero_prolongation_upper_caps"
        ].items()
    }
    assert base == {"12": 436, "13": 440, "14": 448}
    assert int(n6051["characteristic_zero_prolongation_upper_cap_t15"]) == 458
    assert int(n6052["one_rectangle_prolongation_upper_cap_t15"]) == 458
    assert int(n6049["one_rectangle_universal_prolongation_cap"]) == 453
    # At t=14 an alpha-two term needs 453 rather than the 448 extremal/alpha-one
    # cap, so use the largest applicable cap in the coarse case split.
    return {"12": 436, "13": 440, "14": 453, "15": 458}


def high_layer_pruning(rows: list[dict[str, object]]) -> dict[str, object]:
    """Exact scalar consequences for b=47,...,52.

    The geometric term caps are inherited; this function checks only the
    finite dimension arithmetic that places each non-alpha-three state in
    one of those proved caps.
    """

    caps = frozen_prolongation_caps()
    details = []
    for row in rows:
        b = int(row["b"])
        if b not in range(47, 53):
            continue
        shadow = int(row["exact_product_shadow_minimum"])
        upper_h = 2 * b + 20
        if b in (51, 52):
            # D=0 forces epsilon=alpha=kappa=0, hence d2=90,a2=78,t2=12,h=120.
            state = {
                "epsilon_alpha_pairs": [[0, 0]] * 6,
                "kappa2": 0,
                "d2": 90,
                "a2": 78,
                "t2": 12,
                "h_lower": 120,
                "required_prolongation_lower": 400 + 120 - b,
                "applicable_cap": caps["12"],
                "excluded": 400 + 120 - b > caps["12"],
            }
            assert state["excluded"]
            details.append({"b": b, "scalar_case_count": 1, "excluded_case_count": 1, "cases": [state]})
            continue

        defect_budget = 78 - shadow
        cases = []
        # It is enough to enumerate epsilon profiles and the actual kappa.
        # For each, d2 is exact and a2>=shadow; alpha restrictions then place
        # every state except the displayed b=50 all-alpha-three endpoint under
        # a frozen cap.
        for epsilon in combinations_with_replacement(range(3), 6):
            omitted = sum(epsilon) - min(epsilon)
            if omitted > defect_budget:
                continue
            cvalues = [individual_middle_lower(value) for value in epsilon]
            if any(value is None for value in cvalues):
                continue
            for kappa in range(defect_budget - omitted + 1):
                h_lower = sum(int(value) for value in cvalues) - 2 * macaulay_successor_degree_two(kappa)
                if h_lower > upper_h:
                    continue
                d2 = 90 - sum(epsilon) - kappa
                t2_upper = d2 - shadow
                required = 400 + h_lower - b
                if b == 47:
                    # Feasibility leaves epsilon=0,kappa=3. Then t2=12 and
                    # q_i>=12 forces every alpha_i=0.
                    assert epsilon == (0,) * 6 and kappa == 3 and t2_upper == 12
                    cap = caps["12"]
                    kind = "all extremal"
                    excluded = required > cap
                elif b == 48:
                    # Every feasible state has t2<=13. Any epsilon-zero term
                    # has alpha<=1, hence an extremal or alpha-one term.
                    assert t2_upper <= 13 and 0 in epsilon
                    cap = caps[str(t2_upper)]
                    kind = "extremal or alpha one"
                    excluded = required > cap
                elif b == 49:
                    # Every feasible state has t2<=14. An epsilon-zero term has
                    # alpha<=2, hence falls under extremal/alpha-one/alpha-two.
                    assert t2_upper <= 14 and 0 in epsilon
                    cap = caps[str(t2_upper)]
                    kind = "extremal, alpha one, or alpha two"
                    excluded = required > cap
                else:
                    assert b == 50 and t2_upper <= 15 and 0 in epsilon
                    if epsilon == (0,) * 6 and kappa == 0 and t2_upper == 15:
                        cap = None
                        kind = "possible all alpha three endpoint"
                        excluded = False
                    else:
                        cap = caps[str(t2_upper)]
                        kind = "contains an alpha zero, one, or two term"
                        excluded = required > cap
                assert excluded or (b == 50 and kind == "possible all alpha three endpoint")
                cases.append(
                    {
                        "epsilon": list(epsilon),
                        "kappa2": kappa,
                        "d2": d2,
                        "a2_lower": shadow,
                        "t2_upper": t2_upper,
                        "h_lower": h_lower,
                        "term_cap_kind": kind,
                        "required_prolongation_lower": required,
                        "applicable_cap": cap,
                        "excluded": excluded,
                    }
                )
        details.append(
            {
                "b": b,
                "scalar_case_count": len(cases),
                "excluded_case_count": sum(bool(case["excluded"]) for case in cases),
                "cases": cases,
            }
        )
    remaining = [
        (layer["b"], case)
        for layer in details
        for case in layer["cases"]
        if not case["excluded"]
    ]
    assert len(remaining) == 1 and remaining[0][0] == 50
    survivor = remaining[0][1]
    assert survivor["epsilon"] == [0] * 6 and survivor["kappa2"] == 0
    return {
        "frozen_caps": caps,
        "layers": details,
        "remaining_b50_scalar_endpoint": {
            **survivor,
            "alpha": [3] * 6,
            "a2": 75,
            "t2": 15,
            "h": 120,
        },
    }


def build_payload() -> dict[str, object]:
    branches = low_maximum_rank_branches()
    rows = []
    for b in range(34, 53):
        shadow = product_shadow_minimum(b)
        profile = profile_lower(b, shadow)
        selection_lower = ceiling(Fraction(860 - 5 * b, 8))
        combined_lower = max(selection_lower, int(profile["profile_middle_rank_lower"]))
        residual_upper = 2 * b + 20
        rows.append(
            {
                "b": b,
                "exact_product_shadow_minimum": shadow,
                **profile,
                "selection_middle_rank_lower": selection_lower,
                "combined_middle_rank_lower": combined_lower,
                "twenty_one_term_residual_middle_rank_upper_for_h": residual_upper,
                "gap_lower_minus_upper": combined_lower - residual_upper,
            }
        )
    assert rows[0]["combined_middle_rank_lower"] == 87
    assert rows[0]["twenty_one_term_residual_middle_rank_upper_for_h"] == 88
    assert max(row["gap_lower_minus_upper"] for row in rows) == -1
    high_pruning = high_layer_pruning(rows)
    b34 = {
        "intersection_b": 34,
        "selected_six_middle_rank_integer_window": [87, 88],
        "residual_middle_rank_lower_if_h87": 419,
        "residual_middle_rank_lower_if_h88": 420,
        "sum_of_21_individual_middle_ranks": 420,
        "all_21_individual_middle_ranks_forced": 20,
        "h87_relation_pairing_loss_rho_plus_delta_upper": 1,
        "h88_residual_middle_rank_exact": 420,
        "h88_relation_dimension_rho": 0,
        "h88_pairing_radical_delta": 0,
    }
    return {
        "status": [
            "PURE_SYMBOLIC_REDUCTION",
            "EXACT_INTEGER_STATE_REPLAY",
            "LOWER_28_FIXED_SIX_PARTIAL",
            "N6-058",
        ],
        "hypothesis": "a hypothetical minimum 27-term Chow decomposition of perm_6",
        "global_exact_identity": "R=400+2z+tau with z>=r and R<=27r",
        "conditional_average": "h>=ceil(r+5*(400-tau-r)/26)",
        "low_maximum_rank_branches_excluded": branches,
        "maximum_individual_middle_rank_forced": 20,
        "rank_19_excluded_by": "N6-031",
        "rank_20_selection_consequence": "h>=ceil((860-5b)/8)",
        "residual_capacity_consequence": "h<=2b+20",
        "intersection_window_after_product_shadow": [34, 52],
        "remaining_integer_rows": rows,
        "high_layer_prolongation_pruning": high_pruning,
        "remaining_intersection_layers_after_existing_caps": list(range(34, 47)) + [50],
        "closest_endpoint_b34": b34,
        "strict_conclusion": (
            "The reused fixed-six, average-subset, product-shadow, and scalar "
            "profile interfaces do not prove lower 28. The product shadow first "
            "reduces to b=34,...,52; existing term prolongation caps then exclude "
            "b=47,48,49,51,52 and all b=50 scalar states except the all-alpha-three "
            "endpoint. At b=34, h is 87 or 88 and every residual term has "
            "middle rank 20; the residual relation-pairing loss is at most one, "
            "and at h=88 the 21 individual middle images are direct."
        ),
        "claim_boundary": (
            "This is a necessary-state reduction under a hypothetical 27-term "
            "ordinary Chow decomposition. It does not exclude any of the "
            "remaining b=34,...,46 layers or the all-alpha-three b=50 endpoint, "
            "prove ChowRank(perm_6)>=28, determine "
            "the exact ordinary rank, or make a border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(args.verify_json)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print("remaining_b=34..46,50")
    print("b34_h=87..88")
    print("N6_LOWER28_FIXED_SIX_PARTIAL_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
