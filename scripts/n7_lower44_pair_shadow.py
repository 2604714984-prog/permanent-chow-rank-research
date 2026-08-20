#!/usr/bin/env python3
"""Exact pair-shadow certificate for ChowRank(perm_7) >= 44."""

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


def ferrers_cap(table: tuple[int, ...], budget: int) -> tuple[int, int]:
    """Maximize area under an exact simultaneous-shadow budget."""

    width = len(table) - 1
    states: dict[tuple[int, int], int] = {(width, 0): 0}
    peak_states = 1
    for row in range(1, width + 1):
        delta = table[row] - table[row - 1]
        following: dict[tuple[int, int], int] = {}
        for (previous, cost), area in states.items():
            for length in range(previous + 1):
                new_cost = cost + delta * table[length]
                if new_cost > budget:
                    continue
                key = (length, new_cost)
                following[key] = max(following.get(key, -1), area + length)
        states = following
        peak_states = max(peak_states, len(states))
    return max(states.values()), peak_states


def ferrers_caps(table: tuple[int, ...], maximum_budget: int) -> tuple[list[int], int]:
    """Return the maximum area for every budget through maximum_budget."""

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
    pair_cap, pair_peak = ferrers_cap(r3_table, 2 * TERM_QUADRATIC_CAP)
    maximum_route_budget = 35 * 35 - 53
    r4_caps, global_peak = ferrers_caps(r4_table, maximum_route_budget)
    global_cap = r4_caps[577]
    pair_witness = (4, 4, 4, 4, 1) + (0,) * 30
    global_witness = (35,) * 5 + (22,) + (15,) * 9 + (0,) * 20
    residual = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * global_cap
    remaining = (residual + TERM_KOSZUL_CAP - 1) // TERM_KOSZUL_CAP
    q_scan = []
    for selected in range(2, 36):
        budget = TERM_CUBIC_CAP * (selected - 2) + pair_cap
        intersection_cap = r4_caps[budget]
        residual_rank = (
            PERMANENT_KOSZUL_RANK
            - PROLONGATION_MULTIPLIER * intersection_cap
        )
        remaining_terms = max(
            0, (residual_rank + TERM_KOSZUL_CAP - 1) // TERM_KOSZUL_CAP
        )
        q_scan.append(
            {
                "selected_terms": selected,
                "shadow_budget": budget,
                "intersection_cap": intersection_cap,
                "remaining_terms_lower_bound": remaining_terms,
                "total_terms_lower_bound": selected + remaining_terms,
            }
        )
    route_best = max(row["total_terms_lower_bound"] for row in q_scan)
    route_maximizers = [
        row["selected_terms"]
        for row in q_scan
        if row["total_terms_lower_bound"] == route_best
    ]
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_44",
        "n": N,
        "pair_shadow": {
            "uniformity": 3,
            "shadow_table": list(r3_table),
            "budget": 42,
            "capacity": pair_cap,
            "peak_dp_states": pair_peak,
            "witness_partition": list(pair_witness),
            "witness_area": sum(pair_witness),
            "witness_shadow": ferrers_shadow(pair_witness, r3_table),
        },
        "eighteen_term_intersection_cap": 16 * TERM_CUBIC_CAP + pair_cap,
        "degree_four_shadow": {
            "uniformity": 4,
            "shadow_table": list(r4_table),
            "budget": 577,
            "capacity": global_cap,
            "peak_dp_states": global_peak,
            "witness_partition": list(global_witness),
            "witness_area": sum(global_witness),
            "witness_shadow": ferrers_shadow(global_witness, r4_table),
        },
        "all_selected_q_pair_route": q_scan,
        "best_total_lower_bound_in_pair_route": route_best,
        "maximizing_selected_q": route_maximizers,
        "koszul": {
            "permanent_rank": PERMANENT_KOSZUL_RANK,
            "prolongation_multiplier": PROLONGATION_MULTIPLIER,
            "single_term_cap": TERM_KOSZUL_CAP,
            "residual_rank_lower_bound": residual,
            "twenty_five_term_capacity": 25 * TERM_KOSZUL_CAP,
            "remaining_terms_lower_bound": remaining,
            "selected_terms": 18,
            "total_terms_lower_bound": 18 + remaining,
        },
        "theorem": "ChowRank(perm_7) >= 44 over characteristic zero",
        "current_ordinary_interval": [44, 64],
        "claim_boundary": [
            "This is an ordinary Chow-rank theorem, not a border-rank theorem.",
            "It does not prove ChowRank(perm_7)=64.",
            "The finite certificates concern simultaneous product shadows only.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    pair = payload["pair_shadow"]
    degree_four = payload["degree_four_shadow"]
    koszul = payload["koszul"]
    assert pair["capacity"] == 17
    assert pair["witness_area"] == 17
    assert pair["witness_shadow"] == 42
    assert payload["eighteen_term_intersection_cap"] == 577
    assert degree_four["capacity"] == 332
    assert degree_four["witness_area"] == 332
    assert degree_four["witness_shadow"] == 577
    assert koszul["residual_rank_lower_bound"] == 42_532
    assert koszul["twenty_five_term_capacity"] == 42_000
    assert koszul["remaining_terms_lower_bound"] == 26
    assert koszul["total_terms_lower_bound"] == 44
    assert payload["best_total_lower_bound_in_pair_route"] == 44
    assert payload["maximizing_selected_q"] == [17, 18, 27]


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
