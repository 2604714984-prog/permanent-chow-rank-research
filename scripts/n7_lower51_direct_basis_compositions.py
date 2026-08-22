#!/usr/bin/env python3
"""Enumerate every scalar direct-basis rank composition for perm7 v7."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path


AMBIENT_DIMENSION = 49
BUDGET = 35
FULL_INCREMENT_FLOOR = (26, 17, 9, 3, 0, 0, 0)


def subset_floor_ok(counts: tuple[int, ...]) -> bool:
    ranks = tuple(rank for rank, count in enumerate(counts, 1) for _ in range(count))
    if len(ranks) >= 2 and sum(ranks[:2]) < 5:
        return False
    if len(ranks) >= 3 and sum(ranks[:3]) < 12:
        return False
    return True


def enumerate_recursive() -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []

    def visit(rank: int, dimension_left: int, counts: tuple[int, ...]) -> None:
        if rank == 7:
            if dimension_left % 7:
                return
            candidate = (*counts, dimension_left // 7)
            cost = sum(a * b for a, b in zip(candidate, FULL_INCREMENT_FLOOR))
            if cost <= BUDGET and subset_floor_ok(candidate):
                rows.append(candidate)
            return
        for count in range(dimension_left // rank + 1):
            visit(rank + 1, dimension_left - rank * count, (*counts, count))

    visit(1, AMBIENT_DIMENSION, ())
    return tuple(rows)


@lru_cache(maxsize=None)
def enumerate_dp(rank: int, dimension: int, budget: int) -> tuple[tuple[int, ...], ...]:
    """Independent coefficient recursion, before the subset-floor filter."""
    if rank == 8:
        return ((),) if dimension == 0 else ()
    rows = []
    cost = FULL_INCREMENT_FLOOR[rank - 1]
    maximum = dimension // rank
    if cost:
        maximum = min(maximum, budget // cost)
    for count in range(maximum + 1):
        for tail in enumerate_dp(rank + 1, dimension - rank * count, budget - cost * count):
            rows.append((count, *tail))
    return tuple(rows)


def build() -> dict:
    recursive = enumerate_recursive()
    independent = tuple(
        row
        for row in enumerate_dp(1, AMBIENT_DIMENSION, BUDGET)
        if subset_floor_ok(row)
    )
    assert recursive == independent
    rows = []
    for counts in recursive:
        ranks = [rank for rank, count in enumerate(counts, 1) for _ in range(count)]
        surplus_floor = sum(
            a * b for a, b in zip(counts, FULL_INCREMENT_FLOOR)
        )
        rows.append(
            {
                "counts_rank_1_through_7": list(counts),
                "basis_labels": len(ranks),
                "full_increment_surplus_floor": surplus_floor,
                "maximum_residual_middle_cap": BUDGET - surplus_floor,
                "contains_rank_at_most_5": any(counts[:5]),
            }
        )
    assert len(rows) == 69
    assert sum(row["contains_rank_at_most_5"] for row in rows) == 67
    return {
        "schema_version": 1,
        "ambient_dimension": AMBIENT_DIMENSION,
        "budget": BUDGET,
        "full_increment_surplus_floor_rank_1_through_7": list(FULL_INCREMENT_FLOOR),
        "surviving_compositions": len(rows),
        "low_rank_compositions": sum(row["contains_rank_at_most_5"] for row in rows),
        "rows": rows,
        "claim": (
            "These are exactly the direct-sum rank-count vectors passing the "
            "dimension equation, universal full-increment floors, and pair/triple "
            "subset-span floors."
        ),
        "claim_boundary": (
            "They are necessary scalar basis types, not represented 50-plane "
            "packets or Chow identities; rank-six support costs can refine them."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    print(
        json.dumps(
            {
                "surviving_compositions": payload["surviving_compositions"],
                "low_rank_compositions": payload["low_rank_compositions"],
            },
            sort_keys=True,
        )
    )
    print("N7_LOWER51_DIRECT_BASIS_COMPOSITIONS_PASS")


if __name__ == "__main__":
    main()
