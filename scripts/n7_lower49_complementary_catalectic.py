#!/usr/bin/env python3
"""Exact recursive-shadow certificate for ChowRank(perm_7) >= 49."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / "scripts" / "n7_lower47_dual_koszul_shadow_tower.py"
SPEC = importlib.util.spec_from_file_location("n7_lower47_dual_koszul_shadow_tower", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BASE)

N = 7


def build_payload() -> dict[str, object]:
    sections, argmins, _ = BASE.recursive_section_caps()
    r6_table = BASE.BASE.exact_shadow_table(6)
    r6_witness = (7, 7, 7, 3, 3, 3, 3)
    selected_scan = []
    for selected in range(1, 47):
        degree_six_cap = sections[6][selected]
        residual_catalectic_rank = N * N - degree_six_cap
        remaining = max(0, math.ceil(residual_catalectic_rank / N))
        selected_scan.append(
            {
                "selected_terms": selected,
                "degree_six_intersection_cap": degree_six_cap,
                "residual_catalectic_rank_lower_bound": residual_catalectic_rank,
                "remaining_terms_lower_bound": remaining,
                "total_terms_lower_bound": selected + remaining,
            }
        )
    best_total = max(row["total_terms_lower_bound"] for row in selected_scan)
    maximizers = [row for row in selected_scan if row["total_terms_lower_bound"] == best_total]
    chosen = selected_scan[45]
    degree_six_argmin = argmins[6][46]
    assert degree_six_argmin is not None
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_49",
        "n": N,
        "prerequisite": "N7-007 proves ChowRank(perm_7) >= 46",
        "degree_five_section_cap_for_46_terms": sections[5][46],
        "degree_six_section": {
            "input_shadow_budget": degree_six_argmin["shadow_budget"],
            "capacity": sections[6][46],
            "witness_partition": list(r6_witness),
            "witness_area": sum(r6_witness),
            "witness_shadow": BASE.BASE.ferrers_shadow(r6_witness, r6_table),
            "next_area": 34,
            "next_area_minimum_shadow": 411,
        },
        "selected_term_scan": selected_scan,
        "chosen_route": chosen,
        "best_total_lower_bound": best_total,
        "maximizers": maximizers,
        "theorem": "ChowRank(perm_7) >= 49 over characteristic zero",
        "current_ordinary_interval": [49, 64],
        "claim_boundary": [
            "This proves ordinary Chow rank only, not border rank.",
            "It does not prove ChowRank(perm_7)=64.",
            "The last step uses the raw C_(6,1) catalectic, not an invalid K_1 prolongation identity.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    assert payload["degree_five_section_cap_for_46_terms"] == 405
    degree_six = payload["degree_six_section"]
    assert degree_six == {
        "input_shadow_budget": 405,
        "capacity": 33,
        "witness_partition": [7, 7, 7, 3, 3, 3, 3],
        "witness_area": 33,
        "witness_shadow": 405,
        "next_area": 34,
        "next_area_minimum_shadow": 411,
    }
    assert payload["chosen_route"] == {
        "selected_terms": 46,
        "degree_six_intersection_cap": 33,
        "residual_catalectic_rank_lower_bound": 16,
        "remaining_terms_lower_bound": 3,
        "total_terms_lower_bound": 49,
    }
    assert payload["best_total_lower_bound"] == 49
    assert payload["maximizers"] == [payload["chosen_route"]]


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
