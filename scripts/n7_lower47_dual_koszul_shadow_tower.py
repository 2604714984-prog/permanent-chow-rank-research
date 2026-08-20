#!/usr/bin/env python3
"""Exact recursive-shadow certificate for ChowRank(perm_7) >= 47."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts" / "n7_lower46_recursive_shadow_tower.py"
SPEC = importlib.util.spec_from_file_location("n7_lower46_recursive_shadow_tower", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BASE)

N = 7
VARIABLES = N * N
MAX_SELECTED = 46


def recursive_section_caps() -> tuple[dict[int, list[int]], dict[int, list[dict[str, int] | None]], dict[int, int]]:
    product_caps: dict[int, list[int]] = {}
    peak_states: dict[int, int] = {}
    for degree in range(2, 7):
        table = BASE.exact_shadow_table(degree)
        product_caps[degree], peak_states[degree] = BASE.ferrers_caps(
            table, math.comb(N, degree - 1) ** 2
        )

    sections: dict[int, list[int]] = {
        1: [0] + [min(VARIABLES, N * terms) for terms in range(1, MAX_SELECTED + 1)]
    }
    argmins: dict[int, list[dict[str, int] | None]] = {1: [None] * (MAX_SELECTED + 1)}
    for degree in range(2, 7):
        term_cap = math.comb(N, degree)
        maximum_budget = math.comb(N, degree - 1) ** 2
        sections[degree] = [0]
        argmins[degree] = [None]
        for terms in range(1, MAX_SELECTED + 1):
            choices = []
            for local_terms in range(1, terms + 1):
                shadow_budget = min(sections[degree - 1][local_terms], maximum_budget)
                local_cap = product_caps[degree][shadow_budget]
                aggregate_cap = (terms - local_terms) * term_cap + local_cap
                choices.append((aggregate_cap, local_terms, shadow_budget, local_cap))
            aggregate_cap, local_terms, shadow_budget, local_cap = min(choices)
            sections[degree].append(aggregate_cap)
            argmins[degree].append(
                {
                    "terms": terms,
                    "local_terms": local_terms,
                    "shadow_budget": shadow_budget,
                    "local_section_cap": local_cap,
                    "aggregate_section_cap": aggregate_cap,
                }
            )
    return sections, argmins, peak_states


def build_payload() -> dict[str, object]:
    sections, argmins, peak_states = recursive_section_caps()
    trace = []
    degree, terms = 5, 46
    while degree >= 2:
        row = argmins[degree][terms]
        assert row is not None
        trace.append({"degree": degree, **row})
        terms = row["local_terms"]
        degree -= 1

    dual_koszul_scan = []
    for koszul_degree in range(2, 7):
        dual_degree = N - koszul_degree
        permanent_rank = (
            VARIABLES * math.comb(N, koszul_degree) ** 2
            - math.comb(N, koszul_degree + 1) ** 2
        )
        term_cap = (
            VARIABLES * math.comb(N, koszul_degree)
            - math.comb(N, koszul_degree + 1)
        )
        best_total = -1
        best_rows = []
        for selected in range(1, MAX_SELECTED + 1):
            dual_intersection_cap = sections[dual_degree][selected]
            residual_rank = permanent_rank - VARIABLES * dual_intersection_cap
            remaining = max(0, math.ceil(residual_rank / term_cap))
            total = selected + remaining
            row = {
                "selected_terms": selected,
                "dual_intersection_cap": dual_intersection_cap,
                "residual_rank_lower_bound": residual_rank,
                "remaining_terms_lower_bound": remaining,
                "total_terms_lower_bound": total,
            }
            if total > best_total:
                best_total = total
                best_rows = [row]
            elif total == best_total:
                best_rows.append(row)
        dual_koszul_scan.append(
            {
                "koszul_degree": koszul_degree,
                "dual_catalectic_degree": dual_degree,
                "permanent_koszul_rank": permanent_rank,
                "one_term_koszul_cap": term_cap,
                "best_total_lower_bound": best_total,
                "maximizers": best_rows,
            }
        )

    chosen = next(
        row
        for row in dual_koszul_scan[0]["maximizers"]
        if row["selected_terms"] == 46
    )
    r5_table = BASE.exact_shadow_table(5)
    r5_witness = (21,) + (15,) * 20
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_47",
        "n": N,
        "prerequisite": "N7-007 proves ChowRank(perm_7) >= 46",
        "recursive_degree_five_trace": trace,
        "degree_five_section_cap_for_46_terms": sections[5][46],
        "degree_five_critical_shadow": {
            "budget": 1_111,
            "capacity": 321,
            "witness_partition": list(r5_witness),
            "witness_area": sum(r5_witness),
            "witness_shadow": BASE.ferrers_shadow(r5_witness, r5_table),
            "next_area": 322,
            "next_area_minimum_shadow": 1_113,
        },
        "correct_dual_koszul_scan": dual_koszul_scan,
        "chosen_koszul_degree_two_route": chosen,
        "strict_nonzero_residual_gap": chosen["residual_rank_lower_bound"],
        "dp_peak_states": {str(key): value for key, value in peak_states.items()},
        "theorem": "ChowRank(perm_7) >= 47 over characteristic zero",
        "current_ordinary_interval": [47, 64],
        "claim_boundary": [
            "This proves ordinary Chow rank only, not border rank.",
            "It does not prove ChowRank(perm_7)=64.",
            "For K_m the double-quotient loss is the degree-(7-m) catalectic intersection, not the degree-(m+1) prolongation intersection.",
            "The scan starts at m=2: for m=1, E_1^(1)=Sym^2(V), not E_2, so the required prolongation identity is unavailable.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    assert payload["degree_five_section_cap_for_46_terms"] == 405
    assert payload["recursive_degree_five_trace"] == [
        {"degree": 5, "terms": 46, "local_terms": 42, "shadow_budget": 1111, "local_section_cap": 321, "aggregate_section_cap": 405},
        {"degree": 4, "terms": 42, "local_terms": 20, "shadow_budget": 589, "local_section_cap": 341, "aggregate_section_cap": 1111},
        {"degree": 3, "terms": 20, "local_terms": 5, "shadow_budget": 85, "local_section_cap": 64, "aggregate_section_cap": 589},
        {"degree": 2, "terms": 5, "local_terms": 2, "shadow_budget": 14, "local_section_cap": 22, "aggregate_section_cap": 85},
    ]
    critical = payload["degree_five_critical_shadow"]
    assert critical["capacity"] == 321
    assert critical["witness_area"] == 321
    assert critical["witness_shadow"] == 1_105
    assert critical["next_area_minimum_shadow"] == 1_113
    chosen = payload["chosen_koszul_degree_two_route"]
    assert chosen == {
        "selected_terms": 46,
        "dual_intersection_cap": 405,
        "residual_rank_lower_bound": 539,
        "remaining_terms_lower_bound": 1,
        "total_terms_lower_bound": 47,
    }
    assert [row["best_total_lower_bound"] for row in payload["correct_dual_koszul_scan"]] == [47, 46, 46, 46, 46]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    validate(payload)
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS frozen payload")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
