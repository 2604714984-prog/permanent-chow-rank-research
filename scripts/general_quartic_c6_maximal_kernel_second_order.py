#!/usr/bin/env python3
"""Exact second-order exclusion for noncanonical maximal C6 source kernels."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path

ORDER = 4
MATCHINGS = tuple(
    frozenset(row * ORDER + permutation[row] for row in range(ORDER))
    for permutation in permutations(range(ORDER))
)
NONCANONICAL_REPRESENTATIVES = (
    (0, 1, 6, 7, 12, 13),
    (0, 1, 24, 25, 48, 49),
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def frames() -> tuple[frozenset[int], ...]:
    result = []
    for rows in combinations(range(ORDER), 3):
        for columns in combinations(range(ORDER), 3):
            for removed_columns in permutations(columns):
                removed = {(rows[i], removed_columns[i]) for i in range(3)}
                result.append(
                    frozenset(
                        row * ORDER + column
                        for row in rows
                        for column in columns
                        if (row, column) not in removed
                    )
                )
    require(len(result) == 96 and len(set(result)) == 96, len(result))
    return tuple(result)


def one_factor_envelope(frame: frozenset[int]) -> frozenset[int]:
    return frozenset(
        index
        for index, matching in enumerate(MATCHINGS)
        if len(frame & matching) >= 3
    )


def representative_payload(
    representative: tuple[int, ...],
    all_frames: tuple[frozenset[int], ...],
) -> dict[str, object]:
    selected = [all_frames[index] for index in representative]
    shared_sources = []
    for left, right in combinations(range(6), 2):
        intersection = selected[left] & selected[right]
        if len(intersection) == 4:
            shared_sources.append(frozenset(intersection))

    require(len(shared_sources) == 9, len(shared_sources))
    require(len(set(shared_sources)) == 9, shared_sources)

    envelope_union = frozenset().union(
        *(one_factor_envelope(frame) for frame in selected)
    )
    outside_targets = sorted(set(range(len(MATCHINGS))) - set(envelope_union))
    require(len(envelope_union) == 12, len(envelope_union))
    require(len(outside_targets) == 12, outside_targets)

    overlap_histogram: Counter[int] = Counter()
    for source in shared_sources:
        for target_index in outside_targets:
            overlap_histogram[len(source & MATCHINGS[target_index])] += 1

    require(max(overlap_histogram) == 1, overlap_histogram)
    require(overlap_histogram == Counter({0: 60, 1: 48}), overlap_histogram)

    return {
        "representative": list(representative),
        "shared_sources": len(shared_sources),
        "one_factor_envelope_union": len(envelope_union),
        "outside_target_count": len(outside_targets),
        "active_source_outside_target_overlap_histogram": dict(
            sorted(overlap_histogram.items())
        ),
        "maximum_active_source_outside_target_overlap": max(overlap_histogram),
        "second_order_outside_targets": "ZERO",
    }


def payload() -> dict[str, object]:
    all_frames = frames()
    representatives = [
        representative_payload(representative, all_frames)
        for representative in NONCANONICAL_REPRESENTATIVES
    ]
    return {
        "schema": "general_quartic_c6_maximal_kernel_second_order/v1",
        "noncanonical_row_column_orbits": 2,
        "representatives": representatives,
        "transposition_pair": True,
        "canonical_maximal_orbit": "CLOSED_BY_EXISTING_PAIR_CANCELLATION",
        "all_distinct_c6_maximal_kernel_orbits": "SECOND_ORDER_CLOSED",
        "claim_boundary": {
            "distinct_c6_kernel_dimension_9": "ZERO_AT_SECOND_ORDER_FOR_PERM4",
            "lower_kernel_dimension_c6_states": "OPEN",
            "repeated_c6_frames": "OPEN",
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
    print("GENERAL_QUARTIC_C6_MAXIMAL_KERNEL_SECOND_ORDER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
