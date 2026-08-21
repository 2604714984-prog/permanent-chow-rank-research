#!/usr/bin/env python3
"""Exact support and orbit replay for the coordinate second-order envelope."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from pathlib import Path

ORDER = 4
CELLS = tuple(range(ORDER * ORDER))
MATCHINGS = tuple(
    frozenset(row * ORDER + permutation[row] for row in range(ORDER))
    for permutation in permutations(range(ORDER))
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def envelope_two(support: frozenset[int]) -> frozenset[int]:
    return frozenset(
        index
        for index, matching in enumerate(MATCHINGS)
        if len(matching & support) >= 2
    )


def row_column_degrees(support: frozenset[int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rows = [0] * ORDER
    columns = [0] * ORDER
    for cell in support:
        rows[cell // ORDER] += 1
        columns[cell % ORDER] += 1
    return tuple(sorted(rows, reverse=True)), tuple(sorted(columns, reverse=True))


def canonical_support(support: frozenset[int]) -> tuple[int, ...]:
    return min(
        tuple(
            sorted(
                row_permutation[cell // ORDER] * ORDER
                + column_permutation[cell % ORDER]
                for cell in support
            )
        )
        for row_permutation in permutations(range(ORDER))
        for column_permutation in permutations(range(ORDER))
    )


def partial_matching_counts(support: frozenset[int]) -> tuple[int, int, int]:
    r2 = sum(
        1
        for subset in combinations(support, 2)
        if len({cell // ORDER for cell in subset}) == 2
        and len({cell % ORDER for cell in subset}) == 2
    )
    r3 = sum(
        1
        for subset in combinations(support, 3)
        if len({cell // ORDER for cell in subset}) == 3
        and len({cell % ORDER for cell in subset}) == 3
    )
    r4 = sum(1 for matching in MATCHINGS if matching <= support)
    return r2, r3, r4


def explicit_six_cover() -> tuple[list[frozenset[int]], frozenset[int]]:
    frames = []
    for missing in permutations(range(3)):
        support = frozenset(
            row * ORDER + column
            for row in range(3)
            for column in range(3)
            if column != missing[row]
        )
        require(len(support) == 6, support)
        require(len(envelope_two(support)) == 14, support)
        frames.append(support)
    union = frozenset().union(*(envelope_two(support) for support in frames))
    require(len(union) == 24, union)
    return frames, union


def payload() -> dict[str, object]:
    checked = 0
    maximum = -1
    equality_supports: list[frozenset[int]] = []

    for size in range(7):
        for values in combinations(CELLS, size):
            support = frozenset(values)
            checked += 1
            envelope_size = len(envelope_two(support))
            r2, r3, r4 = partial_matching_counts(support)
            require(envelope_size == 2 * r2 - 2 * r3 + 3 * r4, support)
            if envelope_size > maximum:
                maximum = envelope_size
                equality_supports = [support]
            elif envelope_size == maximum:
                equality_supports.append(support)

    require(checked == 14893, checked)
    require(maximum == 14, maximum)
    require(len(equality_supports) == 96, len(equality_supports))
    require(
        all(
            len(support) == 6
            and row_column_degrees(support)
            == ((2, 2, 2, 0), (2, 2, 2, 0))
            and partial_matching_counts(support) == (9, 2, 0)
            for support in equality_supports
        ),
        equality_supports,
    )
    require(
        len({canonical_support(support) for support in equality_supports}) == 1,
        equality_supports,
    )
    frames, union = explicit_six_cover()

    return {
        "schema": "general_quartic_coordinate_second_order_envelope/v1",
        "supports_checked": checked,
        "maximum_second_order_envelope": maximum,
        "equality_supports": len(equality_supports),
        "equality_row_column_orbits": 1,
        "equality_graph": "C6_EQUALS_K33_MINUS_PERFECT_MATCHING",
        "equality_partial_matching_counts": {"r2": 9, "r3": 2, "r4": 0},
        "explicit_cover_frame_count": len(frames),
        "explicit_cover_union": len(union),
        "claim_boundary": {
            "raw_second_order_support_route": "INSUFFICIENT",
            "second_order_six_block_witness": False,
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
    print("GENERAL_QUARTIC_COORDINATE_SECOND_ORDER_ENVELOPE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
