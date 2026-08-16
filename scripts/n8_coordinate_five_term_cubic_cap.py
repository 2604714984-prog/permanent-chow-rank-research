#!/usr/bin/env python3
"""Exact coordinate five-term cubic-cap audit for ``perm_8``.

A coordinate degree-eight Chow monomial has at most eight distinct support
edges in the 8 by 8 variable matrix.  Its cubic derivative space contains a
perfect-matching monomial exactly when the matching's three edges lie in that
support graph.

The audit proves that one eight-edge bipartite graph has at most eight 3 by 3
rectangles containing at least two perfect matchings.  Since six matchings must
be covered by five support graphs, every covered permanent rectangle is
charged to a graph containing at least two of its matchings.  Hence five
coordinate Chow terms cover at most 40 permanent cubic basis vectors.

This is a torus-fixed literal-sum theorem.  It does not control nonliteral flat
limits of sums of moving derivative spaces.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable

N = 8
ALL_EDGES = tuple((row, column) for row in range(N) for column in range(N))
H5 = frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)})
H6 = frozenset({(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)})
EXPECTED_CORE_SHA256 = (
    "194ad847df5d43e122a6a702c6594648ad9f1194dd6f93ec75d47f86d7da5e89"
)

Edge = tuple[int, int]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def matching_statistics(edges: Iterable[Edge]) -> tuple[int, int, int]:
    """Return pair count, multi-rectangle count and maximum matching count."""

    support = tuple(sorted(set(edges)))
    counts: dict[
        tuple[tuple[int, ...], tuple[int, ...]],
        int,
    ] = defaultdict(int)
    for triple in combinations(support, 3):
        rows = tuple(sorted({edge[0] for edge in triple}))
        columns = tuple(sorted({edge[1] for edge in triple}))
        if len(rows) == len(columns) == 3:
            counts[(rows, columns)] += 1

    pair_count = sum(value * (value - 1) // 2 for value in counts.values())
    multi_rectangle_count = sum(value >= 2 for value in counts.values())
    maximum_matching_count = max(counts.values(), default=0)
    return pair_count, multi_rectangle_count, maximum_matching_count


def enumerate_extensions(
    base: frozenset[Edge],
    extra_edge_count: int,
) -> dict[str, object]:
    remaining = tuple(edge for edge in ALL_EDGES if edge not in base)
    pair_histogram: Counter[int] = Counter()
    rectangle_histogram: Counter[int] = Counter()
    maximum_pair_count = -1
    maximum_rectangle_count = -1
    pair_maximizers: list[tuple[Edge, ...]] = []
    rectangle_maximizers: list[tuple[Edge, ...]] = []

    for extra in combinations(remaining, extra_edge_count):
        graph = tuple(sorted(set(base) | set(extra)))
        require(len(graph) == 8, graph)
        pair_count, rectangle_count, _ = matching_statistics(graph)
        pair_histogram[pair_count] += 1
        rectangle_histogram[rectangle_count] += 1

        if pair_count > maximum_pair_count:
            maximum_pair_count = pair_count
            pair_maximizers = [graph]
        elif pair_count == maximum_pair_count:
            pair_maximizers.append(graph)

        if rectangle_count > maximum_rectangle_count:
            maximum_rectangle_count = rectangle_count
            rectangle_maximizers = [graph]
        elif rectangle_count == maximum_rectangle_count:
            rectangle_maximizers.append(graph)

    return {
        "extension_count": comb(len(remaining), extra_edge_count),
        "pair_histogram": {
            str(key): value for key, value in sorted(pair_histogram.items())
        },
        "multi_rectangle_histogram": {
            str(key): value
            for key, value in sorted(rectangle_histogram.items())
        },
        "maximum_matching_pair_count": maximum_pair_count,
        "maximum_multi_rectangle_count": maximum_rectangle_count,
        "pair_maximizer_count": len(pair_maximizers),
        "rectangle_maximizer_count": len(rectangle_maximizers),
        "example_pair_maximizer": [
            list(edge) for edge in pair_maximizers[0]
        ],
    }


def build_payload() -> dict[str, object]:
    shared = enumerate_extensions(H5, 3)
    disjoint = enumerate_extensions(H6, 2)

    require(shared["extension_count"] == 32_509, shared)
    require(disjoint["extension_count"] == 1_653, disjoint)
    require(
        shared["pair_histogram"]
        == {
            "1": 1700,
            "2": 8950,
            "3": 14420,
            "4": 6920,
            "5": 200,
            "6": 294,
            "8": 25,
        },
        shared,
    )
    require(
        disjoint["pair_histogram"]
        == {"1": 1455, "3": 30, "4": 90, "5": 75, "6": 3},
        disjoint,
    )
    require(shared["maximum_matching_pair_count"] == 8, shared)
    require(shared["maximum_multi_rectangle_count"] == 8, shared)
    require(disjoint["maximum_matching_pair_count"] == 6, disjoint)
    require(disjoint["maximum_multi_rectangle_count"] == 4, disjoint)

    core = {
        "status": [
            "N8_COORDINATE_FIVE_TERM_CAP_40",
            "EXACT_FINITE_ENUMERATION",
            "FLAT_SUM_GAP_IDENTIFIED",
        ],
        "single_graph_theorem": {
            "support_edge_cap": 8,
            "maximum_matching_pair_count": 8,
            "maximum_three_by_three_rectangles_with_at_least_two_matchings": 8,
        },
        "canonical_extension_cases": {
            "shared_edge_pair": {
                "base_type": (
                    "two matchings sharing one edge: C4 plus a disjoint edge"
                ),
                "base_edge_count": 5,
                "extension_edges": 3,
                **shared,
            },
            "disjoint_pair": {
                "base_type": "two disjoint matchings: a six-cycle",
                "base_edge_count": 6,
                "extension_edges": 2,
                **disjoint,
            },
        },
        "five_term_coordinate_consequence": {
            "coordinate_chow_terms": 5,
            "matching_count_per_permanent": 6,
            "pigeonhole_required_pair_in_one_term": True,
            "coordinate_permanent_subspace_cap": 40,
        },
        "general_target_comparison": {
            "general_recursive_block_cap": 160,
            "required_chow_cap_for_lower_80": 146,
            "coordinate_fixed_term_cap": 40,
            "minimum_nonliteral_flat_sum_directions_if_dimension_147_persists": 107,
        },
        "claim_boundary": (
            "This is a theorem for five coordinate degree-eight Chow "
            "monomials and their literal cubic derivative-space sum. Raw "
            "literal sums are not closed under Chow-term specialization, so "
            "the result does not prove the general five-term cap 146 or "
            "ChowRank(perm_8)>=80. It identifies flat-sum/valuation "
            "directions as the only remaining source of a large fixed-point "
            "intersection."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N8_COORDINATE_FIVE_TERM_CUBIC_CAP_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
