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
from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path


N = 6
CELL_COUNT = N * N
PAIRS = tuple(combinations(range(N), 2))


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


def recover_signature(value: int) -> tuple[int, ...]:
    """Recover the six-cell support without retaining earlier signatures."""

    active_rows: set[int] = set()
    active_columns: set[int] = set()
    recovered: set[int] = set()
    disjoint_by_rows: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)

    remaining = value
    while remaining:
        lowest = remaining & -remaining
        axis = lowest.bit_length() - 1
        remaining ^= lowest
        if axis < 90:
            row, pair_index = divmod(axis, 15)
            column0, column1 = PAIRS[pair_index]
            active_rows.add(row)
            active_columns.update((column0, column1))
            recovered.update((row * N + column0, row * N + column1))
        elif axis < 180:
            column, pair_index = divmod(axis - 90, 15)
            row0, row1 = PAIRS[pair_index]
            active_rows.update((row0, row1))
            active_columns.add(column)
            recovered.update((row0 * N + column, row1 * N + column))
        else:
            row_pair_index, column_pair_index = divmod(axis - 180, 15)
            row_pair = PAIRS[row_pair_index]
            column_pair = PAIRS[column_pair_index]
            active_rows.update(row_pair)
            active_columns.update(column_pair)
            disjoint_by_rows[row_pair].add(column_pair)

    recovered_rows = {cell // N for cell in recovered}
    recovered_columns = {cell % N for cell in recovered}
    missing_rows = sorted(active_rows - recovered_rows)
    missing_columns = sorted(active_columns - recovered_columns)
    if len(missing_rows) != len(missing_columns):
        raise AssertionError((missing_rows, missing_columns))

    missing_count = len(missing_rows)
    if missing_count == 1:
        recovered.add(missing_rows[0] * N + missing_columns[0])
    elif missing_count >= 3:
        for index, row in enumerate(missing_rows):
            other0 = missing_rows[(index + 1) % missing_count]
            other1 = missing_rows[(index + 2) % missing_count]
            pair0 = tuple(sorted((row, other0)))
            pair1 = tuple(sorted((row, other1)))
            columns0 = next(iter(disjoint_by_rows[pair0]))
            columns1 = next(iter(disjoint_by_rows[pair1]))
            common = set(columns0) & set(columns1)
            if len(common) != 1:
                raise AssertionError((row, columns0, columns1))
            recovered.add(row * N + common.pop())
    elif missing_count == 2:
        recovered_neighbors: dict[int, set[int]] = defaultdict(set)
        for cell in recovered:
            recovered_neighbors[cell // N].add(cell % N)
        anchor_row, anchor_columns = next(iter(recovered_neighbors.items()))
        for row in missing_rows:
            row_pair = tuple(sorted((anchor_row, row)))
            observed = disjoint_by_rows[row_pair]
            candidates = [
                column
                for column in missing_columns
                if {
                    tuple(sorted((column, anchor_column)))
                    for anchor_column in anchor_columns
                }
                == observed
            ]
            if len(candidates) != 1:
                raise AssertionError((row, observed, candidates))
            recovered.add(row * N + candidates[0])

    answer = tuple(sorted(recovered))
    if len(answer) != 6 or signature(answer) != value:
        raise AssertionError((answer, value))
    return answer


def audit() -> dict[str, object]:
    rectangle_free_count = 0
    for support in combinations(range(CELL_COUNT), 6):
        if not is_rectangle_free(support):
            continue
        rectangle_free_count += 1
        value = signature(support)
        recovered = recover_signature(value)
        if recovered != support:
            raise AssertionError((support, recovered))

    if rectangle_free_count != 1_837_392:
        raise AssertionError(rectangle_free_count)

    return {
        "status": "EXACT_N6_ALPHA3_COORDINATE_QUOTIENT_INJECTIVITY",
        "arithmetic": "integer exhaustive regression plus a pure recovery theorem",
        "all_coordinate_six_cell_supports": comb(CELL_COUNT, 6),
        "rectangle_free_coordinate_supports": rectangle_free_count,
        "distinct_quotient_signatures": rectangle_free_count,
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
