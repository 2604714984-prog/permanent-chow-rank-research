#!/usr/bin/env python3
"""Exact finite replay for the N6-062A coordinate equality theorem."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_coordinate_product_shadow_b50_equality.json"
VERTICES = tuple(range(6))
TRIPLES = tuple(combinations(VERTICES, 3))
PAIRS = tuple(combinations(VERTICES, 2))


def lower_shadow(family: tuple[tuple[int, ...], ...], size: int) -> set[tuple[int, ...]]:
    return {
        face
        for member in family
        for face in combinations(member, size)
    }


def colex_subsets(size: int) -> list[tuple[int, ...]]:
    return sorted(combinations(VERTICES, size), key=lambda s: sum(1 << x for x in s))


def one_factor_data() -> tuple[list[int], list[int]]:
    seen: set[tuple[int, ...]] = set()
    shadow_sizes = [0]
    weights = []
    for triple in colex_subsets(3):
        new = set(combinations(triple, 2)) - seen
        weights.append(len(new))
        seen.update(new)
        shadow_sizes.append(len(seen))
    return shadow_sizes, weights


def minimum_ferrers_partitions(total: int) -> tuple[int, list[tuple[int, ...]]]:
    shadow_sizes, weights = one_factor_data()
    infinity = 10**9

    @lru_cache(maxsize=None)
    def solve(index: int, previous: int, remaining: int) -> int:
        if index == 20:
            return 0 if remaining == 0 else infinity
        return min(
            (
                weights[index] * shadow_sizes[value]
                + solve(index + 1, value, remaining - value)
                for value in range(min(previous, remaining), -1, -1)
                if remaining - value <= value * (19 - index)
            ),
            default=infinity,
        )

    minimum = solve(0, 20, total)
    witnesses: list[tuple[int, ...]] = []

    def collect(index: int, previous: int, remaining: int, prefix: tuple[int, ...]):
        if index == 20:
            if remaining == 0:
                witnesses.append(prefix)
            return
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (19 - index):
                continue
            if (
                weights[index] * shadow_sizes[value]
                + solve(index + 1, value, remaining - value)
                == solve(index, previous, remaining)
            ):
                collect(index + 1, value, remaining - value, prefix + (value,))

    collect(0, 20, total, ())
    return minimum, witnesses


def small_equality_families(size: int, shadow_size: int) -> list[tuple[tuple[int, ...], ...]]:
    return [
        family
        for family in combinations(TRIPLES, size)
        if len(lower_shadow(family, 2)) == shadow_size
    ]


def is_complete_triple_clique(family: tuple[tuple[int, ...], ...], vertex_count: int) -> bool:
    vertices = set().union(*(set(member) for member in family))
    return len(vertices) == vertex_count and set(family) == set(combinations(vertices, 3))


def hook_support(transpose: bool = False) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    row_four = {0, 1, 2, 3}
    row_three = {0, 1, 2}
    column_five = {0, 1, 2, 3, 4}
    support = {
        (row, column)
        for row in TRIPLES
        for column in TRIPLES
        if (set(row) <= row_four and set(column) <= column_five)
        or set(row) <= row_three
    }
    return {(column, row) for row, column in support} if transpose else support


def product_shadow(support, output_size: int):
    return {
        (row_face, column_face)
        for row, column in support
        for row_face in combinations(row, output_size)
        for column_face in combinations(column, output_size)
    }


def build_payload() -> dict[str, object]:
    minimum, ferrers = minimum_ferrers_partitions(50)
    degree_profiles = sorted(ferrers)
    four_families = small_equality_families(4, 6)
    ten_families = small_equality_families(10, 10)
    assert minimum == 75
    assert len(ferrers) == 2
    assert set(degree_profiles) == set(ferrers)
    assert len(four_families) == 15
    assert all(is_complete_triple_clique(family, 4) for family in four_families)
    assert len(ten_families) == 6
    assert all(is_complete_triple_clique(family, 5) for family in ten_families)

    hook_rows = []
    for transpose in (False, True):
        support = hook_support(transpose)
        first_shadow = product_shadow(support, 2)
        second_shadow = product_shadow(first_shadow, 1)
        assert (len(support), len(first_shadow), len(second_shadow)) == (50, 75, 23)
        hook_rows.append(
            {
                "orientation": "transpose" if transpose else "row_hook",
                "support_size": len(support),
                "first_product_shadow_size": len(first_shadow),
                "second_product_shadow_size": len(second_shadow),
            }
        )

    return {
        "status": [
            "PURE_COORDINATE_PRODUCT_SHADOW_EQUALITY_THEOREM",
            "EXACT_SMALL_KRUSKAL_KATONA_REPLAY",
            "N6-062A",
        ],
        "b": 50,
        "minimum_first_product_shadow": minimum,
        "minimizing_ferrers_partitions": [list(row) for row in ferrers],
        "original_row_degree_profiles_preserved_by_double_compression": [
            list(row) for row in degree_profiles
        ],
        "small_equality_replay": {
            "four_triples_shadow_six_family_count": len(four_families),
            "all_four_triple_families_are_complete_on_four_vertices": True,
            "ten_triples_shadow_ten_family_count": len(ten_families),
            "all_ten_triple_families_are_complete_on_five_vertices": True,
        },
        "coordinate_equality_types_up_to_row_column_permutations": [
            "row_hook",
            "transpose_hook",
        ],
        "hook_replays": hook_rows,
        "claim_boundary": (
            "This classifies coordinate fifty-supports with product lower shadow "
            "seventy-five. It does not classify noncoordinate subspaces, the "
            "rank-at-most-seventy-five determinantal scheme, or unrestricted "
            "Chow decompositions."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
