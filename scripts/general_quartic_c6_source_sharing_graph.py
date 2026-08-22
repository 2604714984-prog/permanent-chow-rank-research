#!/usr/bin/env python3
"""Exact source-sharing graph replay for quartic C6 equality frames."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

ORDER = 4


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frames() -> tuple[frozenset[int], ...]:
    result = []
    for rows in combinations(range(ORDER), 3):
        for columns in combinations(range(ORDER), 3):
            for removed_columns in permutations(columns):
                removed = {(rows[i], removed_columns[i]) for i in range(3)}
                support = frozenset(
                    row * ORDER + column
                    for row in rows
                    for column in columns
                    if (row, column) not in removed
                )
                result.append(support)
    require(len(result) == 96 and len(set(result)) == 96, len(result))
    return tuple(result)


def omitted_pair(frame: frozenset[int]) -> tuple[int, int]:
    rows = {cell // ORDER for cell in frame}
    columns = {cell % ORDER for cell in frame}
    return (
        next(iter(set(range(ORDER)) - rows)),
        next(iter(set(range(ORDER)) - columns)),
    )


def row_column_maps() -> tuple[tuple[int, ...], ...]:
    result = []
    for row_perm in permutations(range(ORDER)):
        for column_perm in permutations(range(ORDER)):
            result.append(
                tuple(
                    row_perm[cell // ORDER] * ORDER + column_perm[cell % ORDER]
                    for cell in range(ORDER * ORDER)
                )
            )
    return tuple(result)


def canonical_six_set(
    six_set: frozenset[int],
    all_frames: tuple[frozenset[int], ...],
    index: dict[tuple[int, ...], int],
    maps: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    candidates = []
    for mapping in maps:
        moved = []
        for frame_index in six_set:
            transformed = tuple(sorted(mapping[cell] for cell in all_frames[frame_index]))
            moved.append(index[transformed])
        candidates.append(tuple(sorted(moved)))
    return min(candidates)


def payload() -> dict[str, object]:
    all_frames = frames()
    frame_index = {tuple(sorted(frame)): i for i, frame in enumerate(all_frames)}

    source_frames: dict[frozenset[int], list[int]] = defaultdict(list)
    for i, frame in enumerate(all_frames):
        for source in combinations(frame, 4):
            source_frames[frozenset(source)].append(i)

    multiplicities = Counter(len(indices) for indices in source_frames.values())
    require(multiplicities == Counter({1: 576, 2: 432}), multiplicities)

    adjacency = [set() for _ in all_frames]
    edges = []
    intersection_histogram: Counter[int] = Counter()
    for left, right in combinations(range(len(all_frames)), 2):
        intersection = all_frames[left] & all_frames[right]
        intersection_histogram[len(intersection)] += 1
        if len(intersection) == 4:
            require(len(source_frames[frozenset(intersection)]) == 2, (left, right))
            adjacency[left].add(right)
            adjacency[right].add(left)
            edges.append((left, right))

    require(len(edges) == 432, len(edges))
    require(all(len(neighbors) == 9 for neighbors in adjacency), [len(x) for x in adjacency])

    triangle_count = 0
    for a in range(len(all_frames)):
        for b in adjacency[a]:
            if b <= a:
                continue
            triangle_count += len(adjacency[a] & adjacency[b])
    triangle_count //= 3
    require(triangle_count == 0, triangle_count)

    k33_sets: set[frozenset[int]] = set()
    for left in combinations(range(len(all_frames)), 3):
        if any(b in adjacency[a] for a, b in combinations(left, 2)):
            continue
        common = adjacency[left[0]] & adjacency[left[1]] & adjacency[left[2]]
        if len(common) == 3:
            six_set = frozenset(set(left) | common)
            edge_count = sum(
                b in adjacency[a]
                for a, b in combinations(sorted(six_set), 2)
            )
            if edge_count == 9:
                k33_sets.add(six_set)

    require(len(k33_sets) == 112, len(k33_sets))

    maps = row_column_maps()
    orbit_counts: Counter[tuple[int, ...]] = Counter(
        canonical_six_set(six_set, all_frames, frame_index, maps)
        for six_set in k33_sets
    )
    require(len(orbit_counts) == 3, orbit_counts)
    require(sorted(orbit_counts.values()) == [16, 48, 48], orbit_counts)

    orbit_profiles = []
    for representative, orbit_size in sorted(orbit_counts.items()):
        omissions = [omitted_pair(all_frames[i]) for i in representative]
        omitted_rows = Counter(row for row, _ in omissions)
        omitted_columns = Counter(column for _, column in omissions)
        orbit_profiles.append(
            {
                "representative": list(representative),
                "orbit_size": orbit_size,
                "omitted_row_multiplicities": sorted(omitted_rows.values(), reverse=True),
                "omitted_column_multiplicities": sorted(omitted_columns.values(), reverse=True),
            }
        )

    require(
        sorted(
            (
                tuple(profile["omitted_row_multiplicities"]),
                tuple(profile["omitted_column_multiplicities"]),
            )
            for profile in orbit_profiles
        )
        == sorted(
            [
                ((6,), (6,)),
                ((2, 2, 2), (6,)),
                ((6,), (2, 2, 2)),
            ]
        ),
        orbit_profiles,
    )

    return {
        "schema": "general_quartic_c6_source_sharing_graph/v1",
        "frame_count": len(all_frames),
        "source_count": len(source_frames),
        "source_multiplicity_histogram": dict(sorted(multiplicities.items())),
        "frame_pair_intersection_histogram": dict(sorted(intersection_histogram.items())),
        "source_sharing_edges": len(edges),
        "source_sharing_degree": 9,
        "triangle_count": triangle_count,
        "six_frame_kernel_dimension_upper_bound": 9,
        "six_frame_equality_graph": "K3,3",
        "labeled_k33_six_sets": len(k33_sets),
        "row_column_orbits": len(orbit_counts),
        "orbit_sizes": sorted(orbit_counts.values()),
        "orbit_profiles": orbit_profiles,
        "claim_boundary": {
            "distinct_c6_order_zero_common_source_kernel": "DIMENSION_AT_MOST_9",
            "canonical_fixed_3x3_orbit": "ALREADY_CLOSED_BY_PAIR_CANCELLATION",
            "two_noncanonical_maximal_orbits": "OPEN",
            "general_six_block_zero_theorem": False,
            "mu_6_4": "OPEN_IN_[6,7]",
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
    print("GENERAL_QUARTIC_C6_SOURCE_SHARING_GRAPH_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
