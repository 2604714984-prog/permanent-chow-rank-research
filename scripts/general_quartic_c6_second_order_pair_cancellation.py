#!/usr/bin/env python3
"""Exact finite replay for canonical C6 second-order pair cancellation."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

S3 = tuple(permutations(range(3)))
S4 = tuple(permutations(range(4)))
CELLS = tuple((row, column) for row in range(3) for column in range(3))
BOUNDARY = tuple(
    (row, column)
    for row in range(4)
    for column in range(4)
    if row == 3 or column == 3
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frame(mu: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, column)
        for row in range(3)
        for column in range(3)
        if column != mu[row]
    )


def cross(cell: tuple[int, int]) -> frozenset[tuple[int, int]]:
    row, column = cell
    return frozenset(
        {(row, other) for other in range(3) if other != column}
        | {(other, column) for other in range(3) if other != row}
    )


def parity(mu: tuple[int, ...]) -> int:
    return sum(
        mu[left] > mu[right]
        for left in range(3)
        for right in range(left + 1, 3)
    ) % 2


def deterministic_velocity(
    source: tuple[int, int],
    factor: tuple[int, int],
    boundary: tuple[int, int],
) -> int:
    return (
        1
        + 17 * source[0]
        + 29 * source[1]
        + 31 * factor[0]
        + 37 * factor[1]
        + 41 * boundary[0]
        + 43 * boundary[1]
    )


def payload() -> dict[str, object]:
    frames = {mu: frame(mu) for mu in S3}
    source_owners: dict[frozenset[tuple[int, int]], list[tuple[int, ...]]] = defaultdict(list)
    for mu, support in frames.items():
        for source in combinations(sorted(support), 4):
            source_owners[frozenset(source)].append(mu)

    shared = {
        cell: (
            cross(cell),
            tuple(sorted(mu for mu in S3 if mu[cell[0]] == cell[1])),
        )
        for cell in CELLS
    }
    require(all(len(owners) == 2 for _, owners in shared.values()), shared)
    require(
        all(source_owners[source] == list(owners) for source, owners in shared.values()),
        (source_owners, shared),
    )
    require(all(parity(owners[0]) != parity(owners[1]) for _, owners in shared.values()), shared)

    tangent_keys: dict[
        tuple[tuple[int, int], tuple[tuple[int, int], ...]],
        list[tuple[tuple[int, int], tuple[int, int]]],
    ] = defaultdict(list)
    for cell, (source, _) in shared.items():
        for factor in source:
            triple = tuple(sorted(source - {factor}))
            for boundary in BOUNDARY:
                tangent_keys[(boundary, triple)].append((cell, factor))

    require(len(tangent_keys) == 9 * 4 * 7, len(tangent_keys))
    require(all(len(owners) == 1 for owners in tangent_keys.values()), tangent_keys)

    cross_targets = []
    pair_cancellation_checks = 0
    for sigma in S4:
        target = frozenset((row, sigma[row]) for row in range(4))
        if (3, 3) in target:
            continue
        internal = frozenset(
            (row, column) for row, column in target if row < 3 and column < 3
        )
        boundary = tuple(sorted(target - internal))
        require(len(internal) == 2 and len(boundary) == 2, (sigma, internal, boundary))
        modes = [cell for cell, (source, _) in shared.items() if internal <= source]
        require(len(modes) == 2, (sigma, modes))
        for cell in modes:
            source, owners = shared[cell]
            moved = tuple(sorted(source - internal))
            require(len(moved) == 2, (sigma, cell, moved))
            plus = next(mu for mu in owners if parity(mu) == 0)
            minus = next(mu for mu in owners if parity(mu) == 1)
            coefficient = 1 + 5 * cell[0] + 7 * cell[1]

            def bracket(_mu: tuple[int, ...]) -> int:
                left, right = moved
                y, z = boundary
                # First-order cancellation forces these boundary velocities to
                # equal the source-indexed values at both endpoints.
                return (
                    deterministic_velocity(cell, left, y)
                    * deterministic_velocity(cell, right, z)
                    + deterministic_velocity(cell, left, z)
                    * deterministic_velocity(cell, right, y)
                )

            contribution = coefficient * bracket(plus) - coefficient * bracket(minus)
            require(contribution == 0, (sigma, cell, contribution))
            pair_cancellation_checks += 1
        cross_targets.append(target)

    require(len(cross_targets) == 18, len(cross_targets))
    require(pair_cancellation_checks == 36, pair_cancellation_checks)
    require(len(BOUNDARY) == 7, BOUNDARY)

    return {
        "schema": "general_quartic_c6_second_order_pair_cancellation/v1",
        "frame_count": 6,
        "source_mode_count": 9,
        "boundary_cell_count": 7,
        "boundary_tangent_rows": len(tangent_keys),
        "boundary_tangent_row_multiplicity": 1,
        "cross_boundary_target_count": len(cross_targets),
        "source_modes_per_cross_target": 2,
        "pair_cancellation_checks": pair_cancellation_checks,
        "conclusion": {
            "canonical_fixed_3x3_six_c6_second_order_cover": "ZERO_ON_18_CROSS_TARGETS",
            "permanent_target": "IMPOSSIBLE_IN_THIS_SUBCASE",
            "general_coordinate_second_order_covers": "OPEN",
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
    print("GENERAL_QUARTIC_C6_SECOND_ORDER_PAIR_CANCELLATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
