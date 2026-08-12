#!/usr/bin/env python3
"""Exact G-048 barrier to a dimension-only hook-to-transversality argument."""

from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_hook_plane_projection_barrier.json"
SEED = 62064
HOOK_COORDINATES = [
    (row, column) for row in range(3) for column in range(6)
] + [(3, column) for column in range(5)]


def rank_q(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][column]
        matrix[rank] = [entry / value for entry in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank or not matrix[index][column]:
                continue
            value = matrix[index][column]
            matrix[index] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(matrix[index], matrix[rank])
            ]
        rank += 1
    return rank


def witness_planes() -> list[list[list[int]]]:
    rng = random.Random(SEED)
    kernel_coordinates = [
        [index for index, (row, _) in enumerate(HOOK_COORDINATES) if row in omitted]
        for omitted in ({2, 3}, {1, 3}, {0, 3})
    ]

    def random_vector(allowed: list[int]) -> list[int]:
        vector = [0] * len(HOOK_COORDINATES)
        for index in allowed:
            vector[index] = rng.randint(-5, 5)
        if not any(vector):
            vector[allowed[0]] = 1
        return vector

    planes = []
    for _ in range(6):
        planes.append(
            [random_vector(kernel) for kernel in kernel_coordinates]
            + [random_vector(list(range(23))) for _ in range(3)]
        )
    return planes


def build_payload() -> dict[str, object]:
    planes = witness_planes()
    plane_ranks = [rank_q(plane) for plane in planes]
    pair_ranks = [rank_q(planes[i] + planes[j]) for i, j in combinations(range(6), 2)]
    total_rank = rank_q(sum(planes, []))
    projection_rows = []
    for i, j in combinations(range(6), 2):
        for row_pair in ((0, 1), (0, 2), (1, 2)):
            columns = [
                index
                for index, (row, _) in enumerate(HOOK_COORDINATES)
                if row in row_pair
            ]
            projection_rows.append(
                {
                    "plane_pair": [i, j],
                    "row_pair": list(row_pair),
                    "exact_QQ_projection_rank": rank_q(
                        [[vector[index] for index in columns] for vector in planes[i] + planes[j]]
                    ),
                    "full_rank_twelve": False,
                }
            )
    assert plane_ranks == [6] * 6
    assert pair_ranks == [12] * 15
    assert total_rank == 23
    assert len(projection_rows) == 45
    assert {row["exact_QQ_projection_rank"] for row in projection_rows} == {10}
    return {
        "status": ["EXACT_QQ_COUNTEREXAMPLE", "PURE_DIMENSION_ROUTE_BARRIER", "G-048"],
        "ambient_hook_coordinates": [list(coordinate) for coordinate in HOOK_COORDINATES],
        "ambient_hook_dimension": 23,
        "seed": SEED,
        "six_plane_integer_bases": planes,
        "individual_plane_ranks": plane_ranks,
        "pair_sum_ranks": pair_ranks,
        "total_span_rank": total_rank,
        "potentially_full_two_row_projection_audit": projection_rows,
        "claim_boundary": (
            "This is an abstract Grassmann arrangement inside the standard "
            "twenty-three-dimensional hook. It has no section-difference "
            "spaces, E2 containment, common quotient, cocycle, or Chow-frame "
            "realizability. It only disproves a dimension-only implication "
            "from hook containment and pairwise transversality to N6-061."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("individual", payload["individual_plane_ranks"])
    print("pair_ranks", sorted(set(payload["pair_sum_ranks"])))
    print("total", payload["total_span_rank"])
    print(
        "projection_ranks",
        sorted({row["exact_QQ_projection_rank"] for row in payload["potentially_full_two_row_projection_audit"]}),
    )


if __name__ == "__main__":
    main()
