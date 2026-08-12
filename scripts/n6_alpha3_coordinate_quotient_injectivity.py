#!/usr/bin/env python3
"""Exact regression for coordinate alpha-three quotient injectivity.

The proof is combinatorial and appears in the companion note.  This script
independently enumerates every six-cell support in a 6 by 6 grid, retains the
rectangle-free supports, and checks that their fifteen-axis quotient
signatures are all distinct.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path


N = 6
CELL_COUNT = N * N


def pair_rank(first: int, second: int) -> int:
    """Rank ``first < second`` among the fifteen two-subsets of six."""

    return first * 5 - first * (first - 1) // 2 + second - first - 1


def quotient_axis(left: int, right: int) -> int:
    row0, column0 = divmod(left, N)
    row1, column1 = divmod(right, N)
    if row0 == row1:
        column0, column1 = sorted((column0, column1))
        return row0 * 15 + pair_rank(column0, column1)
    if column0 == column1:
        row0, row1 = sorted((row0, row1))
        return 90 + column0 * 15 + pair_rank(row0, row1)
    row0, row1 = sorted((row0, row1))
    column0, column1 = sorted((column0, column1))
    return 180 + pair_rank(row0, row1) * 15 + pair_rank(column0, column1)


def is_rectangle_free(support: tuple[int, ...]) -> bool:
    row_masks = [0] * N
    for cell in support:
        row, column = divmod(cell, N)
        row_masks[row] |= 1 << column
    return all(
        (row_masks[first] & row_masks[second]).bit_count() <= 1
        for first in range(N)
        for second in range(first)
    )


def signature(support: tuple[int, ...]) -> int:
    answer = 0
    for left, right in combinations(support, 2):
        answer |= 1 << quotient_axis(left, right)
    if answer.bit_count() != 15:
        raise AssertionError((support, answer.bit_count()))
    return answer


def audit() -> dict[str, object]:
    signatures: set[int] = set()
    rectangle_free_count = 0
    collision_witness = None
    for support in combinations(range(CELL_COUNT), 6):
        if not is_rectangle_free(support):
            continue
        rectangle_free_count += 1
        value = signature(support)
        if value in signatures:
            collision_witness = list(support)
            break
        signatures.add(value)

    if collision_witness is not None:
        raise AssertionError(collision_witness)
    if rectangle_free_count != 1_837_392:
        raise AssertionError(rectangle_free_count)
    if len(signatures) != rectangle_free_count:
        raise AssertionError((len(signatures), rectangle_free_count))

    return {
        "status": "EXACT_N6_ALPHA3_COORDINATE_QUOTIENT_INJECTIVITY",
        "arithmetic": "integer exhaustive regression plus a pure recovery theorem",
        "all_coordinate_six_cell_supports": comb(CELL_COUNT, 6),
        "rectangle_free_coordinate_supports": rectangle_free_count,
        "distinct_quotient_signatures": len(signatures),
        "signature_axis_universe_dimension": 405,
        "axes_per_signature": 15,
        "collision_count": 0,
        "strict_conclusion": (
            "The quotient signature map is injective on all coordinate "
            "six-cell supports with no rectangle."
        ),
        "claim_boundary": (
            "This is a coordinate theorem. It does not prove injectivity on "
            "noncoordinate alpha-three Chow frames or exclude the coupled "
            "six-term b=60 incidence."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = audit()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(f"rectangle_free_supports={payload['rectangle_free_coordinate_supports']}")
    print(f"distinct_signatures={payload['distinct_quotient_signatures']}")
    print("N6_ALPHA3_COORDINATE_QUOTIENT_INJECTIVITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
