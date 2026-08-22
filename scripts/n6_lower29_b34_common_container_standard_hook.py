#!/usr/bin/env python3
"""Exact finite interfaces for the b=34 common-container reduction (N6-103)."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_lower29_b34_common_container_standard_hook.json"
N6102_JSON = ROOT / "data" / "n6_lower29_b34_critical_six_scalar_frontier.json"


def colex_subsets(size: int) -> list[tuple[int, ...]]:
    return sorted(combinations(range(6), size), key=lambda s: sum(1 << x for x in s))


def quadratic_product_shadow_minimum(total: int) -> int:
    edges = colex_subsets(2)
    seen: set[int] = set()
    one_factor_shadow = [0]
    first_weights: list[int] = []
    for edge in edges:
        new = set(edge) - seen
        first_weights.append(len(new))
        seen.update(edge)
        one_factor_shadow.append(len(seen))

    @lru_cache(maxsize=None)
    def solve(index: int, previous: int, remaining: int) -> int:
        if index == 15:
            return 0 if remaining == 0 else 10**9
        best = 10**9
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (14 - index):
                continue
            best = min(
                best,
                first_weights[index] * one_factor_shadow[value]
                + solve(index + 1, value, remaining - value),
            )
        return best

    return solve(0, 15, total)


EDGES = list(combinations(range(6), 2))
TRIANGLES = list(combinations(range(6), 3))


def component_count(mask: int, complement: bool = False) -> int:
    parent = list(range(6))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index, (left, right) in enumerate(EDGES):
        selected = bool(mask & (1 << index))
        if complement:
            selected = not selected
        if selected:
            a, b = find(left), find(right)
            if a != b:
                parent[a] = b
    return len({find(x) for x in range(6)})


def relation_graph_rows() -> list[dict[str, int | bool]]:
    rows = []
    for kappa in range(4):
        admissible = [
            mask
            for mask in range(1 << len(EDGES))
            if 6 - component_count(mask) <= kappa
        ]
        connected_complements = sum(
            component_count(mask, complement=True) == 1 for mask in admissible
        )
        rows.append(
            {
                "kappa": kappa,
                "admissible_intersection_graph_count": len(admissible),
                "connected_complement_count": connected_complements,
                "every_complement_connected": connected_complements == len(admissible),
            }
        )
    return rows


ONE_FACTOR_CUBIC_SHADOW = (0, 3, 5, 6, 6, 8, 9)


def separated_block_bound(kappa: int) -> tuple[int, list[int]]:
    best = -1
    witness: list[int] = []

    def maximum_cubic_dimension(cap: int) -> int:
        return max(
            size for size, shadow in enumerate(ONE_FACTOR_CUBIC_SHADOW) if shadow <= cap
        )

    def search(index: int, remaining: int, deficits: list[int]) -> None:
        nonlocal best, witness
        if index == len(EDGES):
            if remaining:
                return
            total = 0
            for triangle in TRIANGLES:
                caps = []
                for edge in combinations(triangle, 2):
                    caps.append(5 - deficits[EDGES.index(edge)])
                total += maximum_cubic_dimension(min(caps))
            if total > best:
                best = total
                witness = deficits[:]
            return
        for value in range(remaining + 1):
            search(index + 1, remaining - value, deficits + [value])

    search(0, kappa, [])
    return best, witness


def build_payload() -> dict[str, object]:
    n6102 = json.loads(N6102_JSON.read_text(encoding="utf-8"))
    scalar_rows = n6102["critical_six_scalar_states"]
    a72_rows = [row for row in scalar_rows if row["a2"] == 72]
    assert [(row["kappa2"], row["t2"]) for row in a72_rows] == [
        (0, 18),
        (1, 17),
        (2, 16),
        (3, 15),
    ]

    shadow_rows = {
        str(size): quadratic_product_shadow_minimum(size) for size in range(12, 16)
    }
    graph_rows = relation_graph_rows()
    assert all(row["every_complement_connected"] for row in graph_rows)

    separated_rows = []
    for kappa in range(4):
        bound, witness = separated_block_bound(kappa)
        separated_rows.append(
            {
                "kappa": kappa,
                "maximum_separated_central_dimension": bound,
                "deficit_witness_on_fifteen_column_pairs": witness,
            }
        )
    assert [row["maximum_separated_central_dimension"] for row in separated_rows] == [
        40,
        36,
        36,
        33,
    ]

    return {
        "status": [
            "PURE_COMMON_A2_CONTAINER_REDUCTION",
            "PURE_A72_KAPPA3_STANDARD_HOOK_EXCLUSION",
            "EXACT_FINITE_GRAPH_AND_SHADOW_REPLAY",
            "N6-103",
        ],
        "global_zero_terms": {
            "minimum_epsilon_zero_terms": 19,
            "minimum_external_epsilon_zero_terms": 13,
            "critical_six_size": 6,
            "critical_middle_intersection_dimension": 46,
            "common_container_statement": (
                "For every epsilon-zero term j, U_j is contained in E3+L_C and "
                "F_j is contained in A2=E2+sum_{i in C}F_i."
            ),
            "common_container_dimension": "225+t2, hence at most 243",
            "external_term_directness": (
                "Every external epsilon-zero F_j is disjoint from the sum of the "
                "critical six F_i; hence it is disjoint from every critical F_i."
            ),
            "external_critical_pair_shadow": 12,
            "all_nineteen_alpha": 3,
            "prolongation_lower_bound": 474,
            "alpha_at_most_two_prolongation_cap": 458,
            "all_nineteen_row_and_column_blocks_forced_singular": True,
        },
        "quadratic_product_shadow_minima": shadow_rows,
        "a2_72_rows": a72_rows,
        "relation_intersection_graph": graph_rows,
        "separated_common_W15_bounds": separated_rows,
        "excluded_branch": {
            "a2": 72,
            "kappa2": 3,
            "t2": 15,
            "second_shadow_geometry": "standard flag hook or its transpose",
            "reason": (
                "The zero-intersection graph is connected, so the six factor planes span "
                "the hook. An invertible block forces common separation and the exact "
                "separated bound 33<46; otherwise the directness-free core of N6-072 "
                "excludes the all-singular standard hook."
            ),
        },
        "open_boundary": [
            "the biflag rectangle hook at (a2,kappa2,t2)=(72,3,15)",
            "both N6-101 geometries at the other three a2=72 states",
            "all a2=73,74,75 states",
            "ordinary lower 29 and border rank",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen JSON does not match exact replay")
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
