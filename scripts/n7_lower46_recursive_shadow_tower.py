#!/usr/bin/env python3
"""Exact finite certificate for ChowRank(perm_7) >= 46."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N = 7
TERM_LINEAR_CAP = 7
TERM_QUADRATIC_CAP = 21
TERM_CUBIC_CAP = 35
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
    tables = {degree: exact_shadow_table(degree) for degree in (2, 3, 4)}
    caps_and_peaks = {
        degree: ferrers_caps(tables[degree], math.comb(N, degree - 1) ** 2)
        for degree in (2, 3, 4)
    }
    caps = {degree: value[0] for degree, value in caps_and_peaks.items()}

    quadratic_packet_rows = []
    for terms in range(1, 36):
        choices = []
        for inner_terms in range(1, terms + 1):
            direct_budget = min(
                inner_terms * TERM_LINEAR_CAP, math.comb(N, 1) ** 2
            )
            direct_cap = caps[2][direct_budget]
            aggregate_budget = (terms - inner_terms) * TERM_QUADRATIC_CAP + direct_cap
            choices.append((aggregate_budget, inner_terms, direct_cap, direct_budget))
        budget, inner_terms, direct_cap, direct_budget = min(choices)
        quadratic_packet_rows.append(
            {
                "quadratic_terms": terms,
                "inner_linear_terms": inner_terms,
                "inner_linear_shadow_budget": direct_budget,
                "inner_quadratic_section_cap": direct_cap,
                "quadratic_section_cap": budget,
                "cubic_section_cap": caps[3][min(budget, math.comb(N, 2) ** 2)],
            }
        )

    route_rows = []
    for selected in range(1, 36):
        choices = []
        for packet in quadratic_packet_rows[:selected]:
            local_terms = packet["quadratic_terms"]
            cubic_budget = (
                (selected - local_terms) * TERM_CUBIC_CAP
                + packet["cubic_section_cap"]
            )
            choices.append((cubic_budget, packet))
        cubic_budget, packet = min(choices, key=lambda item: (item[0], item[1]["quadratic_terms"]))
        degree_four_cap = caps[4][min(cubic_budget, math.comb(N, 3) ** 2)]
        residual = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * degree_four_cap
        remaining = max(0, math.ceil(residual / TERM_KOSZUL_CAP))
        route_rows.append(
            {
                "selected_terms": selected,
                "local_cubic_terms": packet["quadratic_terms"],
                "inner_quadratic_terms": packet["inner_linear_terms"],
                "cubic_shadow_budget": cubic_budget,
                "degree_four_intersection_cap": degree_four_cap,
                "remaining_terms_lower_bound": remaining,
                "total_terms_lower_bound": selected + remaining,
            }
        )

    triple_scan_histogram: Counter[int] = Counter()
    triple_scan_maximizers = []
    triple_scan_count = 0
    triple_scan_best = 0
    for selected in range(1, 36):
        for local_terms in range(1, selected + 1):
            for inner_terms in range(1, local_terms + 1):
                direct_budget = min(inner_terms * TERM_LINEAR_CAP, math.comb(N, 1) ** 2)
                direct_cap = caps[2][direct_budget]
                quadratic_budget = (local_terms - inner_terms) * TERM_QUADRATIC_CAP + direct_cap
                cubic_cap = caps[3][min(quadratic_budget, math.comb(N, 2) ** 2)]
                cubic_budget = (selected - local_terms) * TERM_CUBIC_CAP + cubic_cap
                degree_four_cap = caps[4][min(cubic_budget, math.comb(N, 3) ** 2)]
                residual = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * degree_four_cap
                remaining = max(0, math.ceil(residual / TERM_KOSZUL_CAP))
                total = selected + remaining
                triple_scan_count += 1
                triple_scan_histogram[total] += 1
                row = {
                    "selected_terms": selected,
                    "local_cubic_terms": local_terms,
                    "inner_quadratic_terms": inner_terms,
                    "total_terms_lower_bound": total,
                }
                if total > triple_scan_best:
                    triple_scan_best = total
                    triple_scan_maximizers = [row]
                elif total == triple_scan_best:
                    triple_scan_maximizers.append(row)

    chosen = route_rows[19]
    best_total = max(row["total_terms_lower_bound"] for row in route_rows)
    maximizers = [row for row in route_rows if row["total_terms_lower_bound"] == best_total]
    r2_witness = (3,) * 6 + (1,) * 4 + (0,) * 11
    r3_witness = (4,) * 16 + (0,) * 19
    r4_witness = (15,) * 15 + (9,) * 4 + (5,) * 16
    residual_rank = PERMANENT_KOSZUL_RANK - PROLONGATION_MULTIPLIER * chosen["degree_four_intersection_cap"]
    return {
        "schema_version": 1,
        "status": "PURE_EXACT_ORDINARY_LOWER_46",
        "n": N,
        "recursive_shadow_tower": {
            "two_term_quadratic_section": {
                "linear_shadow_budget": 14,
                "capacity": caps[2][14],
                "witness_partition": list(r2_witness),
                "witness_area": sum(r2_witness),
                "witness_shadow": ferrers_shadow(r2_witness, tables[2]),
            },
            "five_term_quadratic_section_cap": quadratic_packet_rows[4]["quadratic_section_cap"],
            "five_term_cubic_section": {
                "quadratic_shadow_budget": quadratic_packet_rows[4]["quadratic_section_cap"],
                "capacity": quadratic_packet_rows[4]["cubic_section_cap"],
                "witness_partition": list(r3_witness),
                "witness_area": sum(r3_witness),
                "witness_shadow": ferrers_shadow(r3_witness, tables[3]),
            },
            "twenty_term_cubic_section_cap": chosen["cubic_shadow_budget"],
            "twenty_term_degree_four_section": {
                "cubic_shadow_budget": chosen["cubic_shadow_budget"],
                "capacity": chosen["degree_four_intersection_cap"],
                "witness_partition": list(r4_witness),
                "witness_area": sum(r4_witness),
                "witness_shadow": ferrers_shadow(r4_witness, tables[4]),
            },
        },
        "quadratic_packet_rows": quadratic_packet_rows,
        "selected_term_frontier": route_rows,
        "full_recursive_scan": {
            "triple_count": triple_scan_count,
            "total_bound_histogram": {
                str(key): triple_scan_histogram[key]
                for key in sorted(triple_scan_histogram)
            },
            "best_total_lower_bound": triple_scan_best,
            "maximizers": triple_scan_maximizers,
        },
        "chosen_route": chosen,
        "koszul_residual_rank_lower_bound": residual_rank,
        "twenty_five_term_koszul_capacity": 25 * TERM_KOSZUL_CAP,
        "best_total_lower_bound_in_this_route": best_total,
        "maximizers": maximizers,
        "dp_peak_states": {str(degree): caps_and_peaks[degree][1] for degree in (2, 3, 4)},
        "theorem": "ChowRank(perm_7) >= 46 over characteristic zero",
        "current_ordinary_interval": [46, 64],
        "claim_boundary": [
            "This proves ordinary Chow rank only, not border rank.",
            "It does not prove ChowRank(perm_7)=64.",
            "The recursive route uses only universal shadow caps, quotient packing, and the complementary Koszul residual.",
        ],
    }


def validate(payload: dict[str, object]) -> None:
    tower = payload["recursive_shadow_tower"]
    chosen = payload["chosen_route"]
    assert tower["two_term_quadratic_section"]["capacity"] == 22
    assert tower["two_term_quadratic_section"]["witness_shadow"] == 14
    assert tower["five_term_quadratic_section_cap"] == 85
    assert tower["five_term_cubic_section"]["capacity"] == 64
    assert tower["five_term_cubic_section"]["witness_shadow"] == 84
    assert tower["twenty_term_cubic_section_cap"] == 589
    assert tower["twenty_term_degree_four_section"]["capacity"] == 341
    assert chosen == {
        "selected_terms": 20,
        "local_cubic_terms": 5,
        "inner_quadratic_terms": 2,
        "cubic_shadow_budget": 589,
        "degree_four_intersection_cap": 341,
        "remaining_terms_lower_bound": 26,
        "total_terms_lower_bound": 46,
    }
    assert payload["koszul_residual_rank_lower_bound"] == 42_091
    assert payload["twenty_five_term_koszul_capacity"] == 42_000
    assert payload["best_total_lower_bound_in_this_route"] == 46
    assert payload["maximizers"] == [chosen]
    assert payload["full_recursive_scan"]["triple_count"] == 7_770
    assert payload["full_recursive_scan"]["best_total_lower_bound"] == 46
    assert payload["full_recursive_scan"]["maximizers"] == [
        {
            "selected_terms": 20,
            "local_cubic_terms": 5,
            "inner_quadratic_terms": 2,
            "total_terms_lower_bound": 46,
        }
    ]


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
