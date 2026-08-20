#!/usr/bin/env python3
"""Exact finite certificate for ChowRank(perm_7) >= 45."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N = 7
TERM_CUBIC_CAP = 35
TERM_QUADRATIC_CAP = 21
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


def exact_shadow_table(uniformity: int) -> tuple[int, ...]:
    ordered = sorted(
        itertools.combinations(range(1, N + 1), uniformity), key=colex_key
    )
    return tuple(
        len(lower_shadow(set(ordered[:size]))) for size in range(len(ordered) + 1)
    )


def ferrers_shadow(partition: tuple[int, ...], table: tuple[int, ...]) -> int:
    width = len(table) - 1
    if len(partition) != width:
        raise ValueError(f"expected {width} rows")
    if any(partition[index] < partition[index + 1] for index in range(width - 1)):
        raise ValueError("partition must be nonincreasing")
    return sum(
        (table[row] - table[row - 1]) * table[partition[row - 1]]
        for row in range(1, width + 1)
    )


def ferrers_caps(table: tuple[int, ...], maximum_budget: int) -> tuple[list[int], int]:
    width = len(table) - 1
    states: dict[tuple[int, int], int] = {(width, 0): 0}
    peak_states = 1
    for row in range(1, width + 1):
        delta = table[row] - table[row - 1]
        following: dict[tuple[int, int], int] = {}
        for (previous, cost), area in states.items():
            for length in range(previous + 1):
                new_cost = cost + delta * table[length]
                if new_cost > maximum_budget:
                    continue
                key = (length, new_cost)
                following[key] = max(following.get(key, -1), area + length)
        states = following
        peak_states = max(peak_states, len(states))
    exact = [-1] * (maximum_budget + 1)
    for (_, cost), area in states.items():
        exact[cost] = max(exact[cost], area)
    caps: list[int] = []
    running = 0
    for area in exact:
        running = max(running, area)
        caps.append(running)
    return caps, peak_states


def build_payload() -> dict[str, object]:
    r3_table = exact_shadow_table(3)
    r4_table = exact_shadow_table(4)
    r3_caps, r3_peak = ferrers_caps(r3_table, math.comb(N, 2) ** 2)
    r4_caps, r4_peak = ferrers_caps(r4_table, math.comb(N, 3) ** 2)

    local_k_caps = {1: 0}
    for local_terms in range(2, 36):
        budget = min(local_terms * TERM_QUADRATIC_CAP, math.comb(N, 2) ** 2)
        local_k_caps[local_terms] = r3_caps[budget]

    route_scan = []
    for selected in range(1, 36):
        for local_terms in range(1, selected + 1):
            cubic_budget = (
                (selected - local_terms) * TERM_CUBIC_CAP
                + local_k_caps[local_terms]
            )
            intersection_cap = r4_caps[min(cubic_budget, math.comb(N, 3) ** 2)]
            residual = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * intersection_cap
            remaining = max(0, (residual + TERM_KOSZUL_CAP - 1) // TERM_KOSZUL_CAP)
            route_scan.append(
                {
                    "selected_terms": selected,
                    "local_terms": local_terms,
                    "cubic_shadow_budget": cubic_budget,
                    "degree_four_intersection_cap": intersection_cap,
                    "remaining_terms_lower_bound": remaining,
                    "total_terms_lower_bound": selected + remaining,
                }
            )

    best_total = max(row["total_terms_lower_bound"] for row in route_scan)
    maximizers = [
        row for row in route_scan if row["total_terms_lower_bound"] == best_total
    ]
    chosen = next(
        row
        for row in route_scan
        if row["selected_terms"] == 19 and row["local_terms"] == 4
    )
    local_witness = (16,) * 4 + (0,) * 31
    global_witness = (35,) * 5 + (19,) * 4 + (15,) * 6 + (0,) * 20
    residual_rank = (
        PERMANENT_KOSZUL_RANK
        - PROLONGATION_MULTIPLIER * chosen["degree_four_intersection_cap"]
    )
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_45",
        "n": N,
        "local_four_term_shadow": {
            "uniformity": 3,
            "budget": 84,
            "capacity": local_k_caps[4],
            "witness_partition": list(local_witness),
            "witness_area": sum(local_witness),
            "witness_shadow": ferrers_shadow(local_witness, r3_table),
            "peak_dp_states": r3_peak,
        },
        "nineteen_term_cubic_intersection_cap": 15 * TERM_CUBIC_CAP + local_k_caps[4],
        "degree_four_shadow": {
            "uniformity": 4,
            "budget": 589,
            "capacity": chosen["degree_four_intersection_cap"],
            "witness_partition": list(global_witness),
            "witness_area": sum(global_witness),
            "witness_shadow": ferrers_shadow(global_witness, r4_table),
            "peak_dp_states": r4_peak,
        },
        "chosen_route": chosen,
        "koszul_residual_rank_lower_bound": residual_rank,
        "twenty_five_term_koszul_capacity": 25 * TERM_KOSZUL_CAP,
        "full_local_selected_route_scan": route_scan,
        "best_total_lower_bound_in_this_route": best_total,
        "maximizers": maximizers,
        "theorem": "ChowRank(perm_7) >= 45 over characteristic zero",
        "current_ordinary_interval": [45, 64],
        "claim_boundary": [
            "This proves ordinary Chow rank only, not border rank.",
            "It does not prove ChowRank(perm_7)=64.",
            "The route scan uses only universal local shadow caps and the complementary Koszul residual.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    local = payload["local_four_term_shadow"]
    global_shadow = payload["degree_four_shadow"]
    chosen = payload["chosen_route"]
    assert local["capacity"] == 64
    assert local["witness_area"] == 64
    assert local["witness_shadow"] == 84
    assert payload["nineteen_term_cubic_intersection_cap"] == 589
    assert global_shadow["capacity"] == 341
    assert global_shadow["witness_area"] == 341
    assert global_shadow["witness_shadow"] == 586
    assert chosen == {
        "selected_terms": 19,
        "local_terms": 4,
        "cubic_shadow_budget": 589,
        "degree_four_intersection_cap": 341,
        "remaining_terms_lower_bound": 26,
        "total_terms_lower_bound": 45,
    }
    assert payload["koszul_residual_rank_lower_bound"] == 42_091
    assert payload["twenty_five_term_koszul_capacity"] == 42_000
    assert payload["best_total_lower_bound_in_this_route"] == 45
    assert payload["maximizers"] == [chosen]


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
