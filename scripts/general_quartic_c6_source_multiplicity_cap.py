#!/usr/bin/env python3
"""Exact enumeration of source multiplicities in all quartic C6 frames."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from pathlib import Path

ROWS = tuple(range(4))
COLUMNS = tuple(range(4))


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frames() -> tuple[frozenset[tuple[int, int]], ...]:
    result = set()
    for row_set in combinations(ROWS, 3):
        for column_set in combinations(COLUMNS, 3):
            for permutation in permutations(column_set):
                missing = {(row_set[index], permutation[index]) for index in range(3)}
                support = frozenset(
                    (row, column)
                    for row in row_set
                    for column in column_set
                    if (row, column) not in missing
                )
                require(len(support) == 6, support)
                result.add(support)
    require(len(result) == 96, len(result))
    return tuple(sorted(result, key=lambda value: tuple(sorted(value))))


def source_shape(source: frozenset[tuple[int, int]]) -> str:
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
    for row, column in source:
        left = ("r", row)
        right = ("c", column)
        adjacency[left].add(right)
        adjacency[right].add(left)

    seen = set()
    component_edges = []
    for start in adjacency:
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        degree_sum = 0
        while queue:
            vertex = queue.popleft()
            degree_sum += len(adjacency[vertex])
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        component_edges.append(degree_sum // 2)

    component_edges.sort(reverse=True)
    if component_edges == [4]:
        return "P5"
    if component_edges == [3, 1]:
        return "P4_DISJOINT_P2"
    if component_edges == [2, 2]:
        return "P3_DISJOINT_P3"
    raise RuntimeError((source, component_edges))


def payload() -> dict[str, object]:
    all_frames = frames()
    source_owners: dict[frozenset[tuple[int, int]], int] = Counter()
    incidence_by_shape = Counter()

    for support in all_frames:
        local_shapes = Counter()
        for values in combinations(sorted(support), 4):
            source = frozenset(values)
            shape = source_shape(source)
            local_shapes[shape] += 1
            incidence_by_shape[shape] += 1
            source_owners[source] += 1
        require(
            local_shapes
            == Counter({"P5": 6, "P4_DISJOINT_P2": 6, "P3_DISJOINT_P3": 3}),
            (support, local_shapes),
        )

    multiplicity_distribution = Counter(source_owners.values())
    require(multiplicity_distribution == Counter({1: 576, 2: 432}), multiplicity_distribution)
    require(max(source_owners.values()) == 2, max(source_owners.values()))
    require(len(source_owners) == 1008, len(source_owners))
    require(sum(source_owners.values()) == 1440, sum(source_owners.values()))

    distinct_by_shape = Counter()
    multiplicities_by_shape: dict[str, set[int]] = defaultdict(set)
    for source, multiplicity in source_owners.items():
        shape = source_shape(source)
        distinct_by_shape[shape] += 1
        multiplicities_by_shape[shape].add(multiplicity)

    require(
        distinct_by_shape
        == Counter({"P5": 288, "P4_DISJOINT_P2": 576, "P3_DISJOINT_P3": 144}),
        distinct_by_shape,
    )
    require(multiplicities_by_shape["P5"] == {2}, multiplicities_by_shape)
    require(multiplicities_by_shape["P4_DISJOINT_P2"] == {1}, multiplicities_by_shape)
    require(multiplicities_by_shape["P3_DISJOINT_P3"] == {2}, multiplicities_by_shape)

    return {
        "schema": "general_quartic_c6_source_multiplicity_cap/v1",
        "labeled_c6_frames": len(all_frames),
        "sources_per_frame": 15,
        "source_incidences": sum(source_owners.values()),
        "distinct_sources": len(source_owners),
        "source_multiplicity_distribution": {"1": 576, "2": 432},
        "maximum_distinct_frame_multiplicity": 2,
        "shape_table": {
            "P5": {"per_frame": 6, "extension_count": 2, "distinct_sources": 288},
            "P4_DISJOINT_P2": {"per_frame": 6, "extension_count": 1, "distinct_sources": 576},
            "P3_DISJOINT_P3": {"per_frame": 3, "extension_count": 2, "distinct_sources": 144},
        },
        "conclusion": {
            "triple_source_across_distinct_c6_frames": "IMPOSSIBLE",
            "triple_source_requires_repeated_frame_copy": True,
            "general_second_order_lift": "OPEN",
            "mu_6_4_exact_value": "OPEN_IN_[6,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print("GENERAL_QUARTIC_C6_SOURCE_MULTIPLICITY_CAP_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
