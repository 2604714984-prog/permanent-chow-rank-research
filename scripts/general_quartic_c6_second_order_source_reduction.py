#!/usr/bin/env python3
"""Exact replay of the canonical six-C6 source and collision reduction."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

ORDER = 4
SMALL = 3
SMALL_PERMUTATIONS = tuple(permutations(range(SMALL)))
FULL_PERMUTATIONS = tuple(permutations(range(ORDER)))


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frame(mu: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, column)
        for row in range(SMALL)
        for column in range(SMALL)
        if column != mu[row]
    )


def cross(row: int, column: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        [(row, other) for other in range(SMALL) if other != column]
        + [(other, column) for other in range(SMALL) if other != row]
    )


def parity(mu: tuple[int, ...]) -> int:
    inversions = sum(
        mu[left] > mu[right]
        for left in range(SMALL)
        for right in range(left + 1, SMALL)
    )
    return inversions % 2


def full_matching(permutation: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset((row, permutation[row]) for row in range(ORDER))


def payload() -> dict[str, object]:
    frames = {mu: frame(mu) for mu in SMALL_PERMUTATIONS}
    require(all(len(value) == 6 for value in frames.values()), frames)

    source_occurrences: dict[frozenset[tuple[int, int]], list[tuple[int, ...]]] = defaultdict(list)
    for mu, support in frames.items():
        for source in combinations(sorted(support), 4):
            source_occurrences[frozenset(source)].append(mu)

    multiplicities = Counter(len(owners) for owners in source_occurrences.values())
    require(multiplicities == Counter({1: 72, 2: 9}), multiplicities)
    require(len(source_occurrences) == 81, len(source_occurrences))
    require(sum(len(owners) for owners in source_occurrences.values()) == 90, source_occurrences)

    shared_labels: dict[tuple[int, int], tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for source, owners in source_occurrences.items():
        if len(owners) != 2:
            continue
        common_cells = set((row, owners[0][row]) for row in range(SMALL)) & set(
            (row, owners[1][row]) for row in range(SMALL)
        )
        require(len(common_cells) == 1, (source, owners, common_cells))
        label = next(iter(common_cells))
        require(source == cross(*label), (source, owners, label, cross(*label)))
        require(parity(owners[0]) != parity(owners[1]), owners)
        shared_labels[label] = tuple(sorted(owners))

    require(len(shared_labels) == 9, shared_labels)
    require(set(shared_labels) == {(row, column) for row in range(3) for column in range(3)}, shared_labels)

    for mu in SMALL_PERMUTATIONS:
        incident = {(row, mu[row]) for row in range(SMALL)}
        require(all(mu in shared_labels[label] for label in incident), (mu, incident))

    gamma_edges: list[tuple[tuple[int, int], tuple[int, int]]] = []
    common_tangent_channels: dict[str, int] = {}
    cells = tuple((row, column) for row in range(3) for column in range(3))
    for left, right in combinations(cells, 2):
        intersection = cross(*left) & cross(*right)
        expected = 1 if left[0] == right[0] or left[1] == right[1] else 2
        require(len(intersection) == expected, (left, right, intersection))
        if expected == 2:
            gamma_edges.append((left, right))
            left_private = cross(*left) - intersection
            right_private = cross(*right) - intersection
            channels = len(left_private) * len(right_private)
            require(channels == 4, (left, right, channels))
            common_tangent_channels[f"{left}-{right}"] = channels

    require(len(gamma_edges) == 18, len(gamma_edges))
    degrees = Counter(vertex for edge in gamma_edges for vertex in edge)
    require(set(degrees.values()) == {4}, degrees)

    cross_targets: dict[frozenset[tuple[int, int]], tuple[tuple[int, int], tuple[int, int]]] = {}
    fixed_targets = []
    for permutation in FULL_PERMUTATIONS:
        target = full_matching(permutation)
        if (3, 3) in target:
            fixed_targets.append(target)
            continue
        internal = frozenset((row, column) for row, column in target if row < 3 and column < 3)
        require(len(internal) == 2, (permutation, internal))
        containing = [cell for cell in cells if internal <= cross(*cell)]
        require(len(containing) == 2, (permutation, internal, containing))
        require(containing[0][0] != containing[1][0] and containing[0][1] != containing[1][1], containing)
        cross_targets[target] = tuple(sorted(containing))

    require(len(cross_targets) == 18, len(cross_targets))
    require(set(cross_targets.values()) == {tuple(sorted(edge)) for edge in gamma_edges}, cross_targets)
    require(len(fixed_targets) == 6, len(fixed_targets))

    fixed_mode_counts = []
    for target in fixed_targets:
        restriction = target - {(3, 3)}
        counts = [len(restriction & cross(*cell)) for cell in cells]
        require(Counter(counts) == Counter({2: 6, 0: 3}), (target, counts))
        fixed_mode_counts.append(sum(count == 2 for count in counts))

    return {
        "schema": "general_quartic_c6_second_order_source_reduction/v1",
        "frame_count": 6,
        "sources_per_frame": 15,
        "source_coordinates": 90,
        "distinct_source_monomials": 81,
        "source_multiplicity_distribution": {"1": 72, "2": 9},
        "order_zero_kernel_dimension": 9,
        "order_zero_kernel_basis": "NINE_PAIRWISE_CROSS_DIFFERENCES",
        "frame_graph": "K3,3_ON_EVEN_AND_ODD_S3_PERMUTATIONS",
        "source_mode_count": 9,
        "source_collision_graph": {
            "vertices": 9,
            "degree": 4,
            "edges": 18,
            "common_tangent_channels_per_edge": 4,
        },
        "cross_boundary_target_count": 18,
        "cross_boundary_target_edge_bijection": True,
        "fixed_33_target_count": 6,
        "source_modes_per_fixed_33_target": sorted(set(fixed_mode_counts)),
        "claim_boundary": {
            "coefficient_system_reduced": True,
            "second_order_lift_decided": False,
            "mu_6_4_exact_value": "OPEN_IN_[6,8]",
            "new_unrestricted_chow_rank_bound": False,
            "new_border_rank_bound": False,
            "literature_novelty": "NOT_ESTABLISHED",
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
    print("GENERAL_QUARTIC_C6_SECOND_ORDER_SOURCE_REDUCTION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
