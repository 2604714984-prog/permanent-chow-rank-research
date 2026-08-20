#!/usr/bin/env python3
"""Exact finite certificate for the ordinary lower bound 43 for perm_7.

The only enumeration is a bounded dynamic program on the 35 by 35 Ferrers
diagram supplied by the two-dimensional Kruskal--Katona compression theorem.
No family of subsets is materialized.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_lower43_bivariate_shadow.json"
N = 7
UNIFORMITY = 4
WIDTH = math.comb(N, UNIFORMITY)
TERM_CUBIC_CAP = math.comb(N, 3)
PERMANENT_KOSZUL_RANK = 58_800
PROLONGATION_MULTIPLIER = 49
TERM_KOSZUL_CAP = 1_680


def colex_key(subset: tuple[int, ...]) -> int:
    return sum(math.comb(value - 1, index) for index, value in enumerate(subset, 1))


def lower_shadow(family: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    return {
        member[:index] + member[index + 1 :]
        for member in family
        for index in range(len(member))
    }


def exact_shadow_table() -> tuple[int, ...]:
    ordered = sorted(
        itertools.combinations(range(1, N + 1), UNIFORMITY), key=colex_key
    )
    return tuple(
        len(lower_shadow(set(ordered[:size]))) for size in range(WIDTH + 1)
    )


def ferrers_shadow_size(partition: tuple[int, ...], table: tuple[int, ...]) -> int:
    if len(partition) != WIDTH:
        raise ValueError(f"expected {WIDTH} rows")
    if any(partition[index] < partition[index + 1] for index in range(WIDTH - 1)):
        raise ValueError("partition must be nonincreasing")
    return sum(
        (table[row] - table[row - 1]) * table[partition[row - 1]]
        for row in range(1, WIDTH + 1)
    )


def cap_table(table: tuple[int, ...], maximum_budget: int) -> tuple[list[int], int]:
    """Return the maximum Ferrers area for every budget up to maximum_budget."""

    states: dict[tuple[int, int], int] = {(WIDTH, 0): 0}
    peak_states = 1
    for row in range(1, WIDTH + 1):
        delta = table[row] - table[row - 1]
        following: dict[tuple[int, int], int] = {}
        for (previous, cost), area in states.items():
            for length in range(previous + 1):
                new_cost = cost + delta * table[length]
                if new_cost > maximum_budget:
                    continue
                key = (length, new_cost)
                new_area = area + length
                if new_area > following.get(key, -1):
                    following[key] = new_area
        states = following
        peak_states = max(peak_states, len(states))

    exact_cost_best = [-1] * (maximum_budget + 1)
    for (_, cost), area in states.items():
        exact_cost_best[cost] = max(exact_cost_best[cost], area)
    caps: list[int] = []
    running = 0
    for area in exact_cost_best:
        running = max(running, area)
        caps.append(running)
    return caps, peak_states


def q_row(q: int, caps: list[int]) -> dict[str, int]:
    budget = (q - 1) * TERM_CUBIC_CAP
    cap = caps[budget]
    residual = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * cap
    remaining = max(0, (residual + TERM_KOSZUL_CAP - 1) // TERM_KOSZUL_CAP)
    return {
        "selected_terms": q,
        "shadow_budget": budget,
        "intersection_cap": cap,
        "residual_koszul_rank_lower_bound": residual,
        "remaining_terms_lower_bound": remaining,
        "total_terms_lower_bound": q + remaining,
    }


def build_payload() -> dict[str, object]:
    table = exact_shadow_table()
    maximum_budget = (35 - 1) * TERM_CUBIC_CAP
    caps, peak_states = cap_table(table, maximum_budget)
    q_scan = [q_row(q, caps) for q in range(1, 36)]
    chosen = q_scan[13]
    witness = (28,) + (15,) * 14 + (0,) * 20
    best_total = max(row["total_terms_lower_bound"] for row in q_scan)
    maximizing_q = [
        row["selected_terms"]
        for row in q_scan
        if row["total_terms_lower_bound"] == best_total
    ]
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_43",
        "n": N,
        "uniformity": UNIFORMITY,
        "one_dimensional_shadow_table": list(table),
        "dp": {
            "maximum_budget": maximum_budget,
            "peak_state_count": peak_states,
            "streaming": True,
        },
        "selected_q_certificate": chosen,
        "sharp_witness": {
            "partition": list(witness),
            "area": sum(witness),
            "shadow_size": ferrers_shadow_size(witness, table),
        },
        "all_q_scan": q_scan,
        "best_total_lower_bound_in_this_method": best_total,
        "maximizing_selected_q": maximizing_q,
        "theorem": "ChowRank(perm_7) >= 43 over characteristic zero",
        "current_ordinary_interval": [43, 64],
        "claim_boundary": [
            "This proves an ordinary Chow-rank lower bound, not border rank.",
            "It does not prove ChowRank(perm_7)=64.",
            "The q-scan optimizes only this quotient-packing and bivariate-shadow route.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    chosen = payload["selected_q_certificate"]
    witness = payload["sharp_witness"]
    assert chosen == {
        "selected_terms": 14,
        "shadow_budget": 455,
        "intersection_cap": 238,
        "residual_koszul_rank_lower_bound": 47_138,
        "remaining_terms_lower_bound": 29,
        "total_terms_lower_bound": 43,
    }
    assert witness["area"] == 238
    assert witness["shadow_size"] == 452
    assert payload["best_total_lower_bound_in_this_method"] == 43
    assert 14 in payload["maximizing_selected_q"]


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
