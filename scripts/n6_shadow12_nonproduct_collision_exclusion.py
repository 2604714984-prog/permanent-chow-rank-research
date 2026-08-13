#!/usr/bin/env python3
"""Exact fixed-endpoint certificate for the nonproduct 12-shadow pair locus.

The expensive part enumerates all coordinate twelve-planes in the two
twenty-three-cell N6-101 hooks.  It is intentionally kept behind the explicit
``--json`` / ``--verify-json`` commands; ordinary regression tests inspect the
frozen payload and replay one local Jacobian only.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_shadow12_nonproduct_collision_exclusion.json"
VERTICES = tuple(range(6))
PAIRS = tuple(combinations(VERTICES, 2))
TRIPLES = tuple(combinations(VERTICES, 3))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
TRIPLE_INDEX = {triple: index for index, triple in enumerate(TRIPLES)}


def lower_pairs(triple: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(PAIR_INDEX[pair] for pair in combinations(triple, 2))


def product_shadow(
    support: set[tuple[int, int]] | frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row_pair, column_pair)
        for row_triple, column_triple in support
        for row_pair in lower_pairs(TRIPLES[row_triple])
        for column_pair in lower_pairs(TRIPLES[column_triple])
    )


def canonical_cubic_support(kind: str) -> frozenset[tuple[int, int]]:
    if kind == "standard":
        row_three = (0, 1, 2)
        row_four = (0, 1, 2, 3)
        column_four = (0, 1, 2, 3)
        column_five = (0, 1, 2, 3, 4)
        row_base = {TRIPLE_INDEX[row] for row in combinations(row_four, 3)}
        column_ten = {
            TRIPLE_INDEX[column] for column in combinations(column_five, 3)
        }
        column_sixteen = {
            index
            for index, column in enumerate(TRIPLES)
            if len(set(column) & set(column_four)) >= 2
        }
        distinguished = TRIPLE_INDEX[row_three]
        return frozenset(
            {(row, column) for row in row_base for column in column_ten}
            | {(distinguished, column) for column in column_sixteen}
        )
    if kind == "biflag":
        row_four = (0, 1, 2, 3)
        row_five = (0, 1, 2, 3, 4)
        column_three = (0, 1, 2)
        column_five = (0, 1, 2, 3, 4)
        row_four_cubics = {
            TRIPLE_INDEX[row] for row in combinations(row_four, 3)
        }
        row_five_cubics = {
            TRIPLE_INDEX[row] for row in combinations(row_five, 3)
        }
        column_five_cubics = {
            TRIPLE_INDEX[column] for column in combinations(column_five, 3)
        }
        distinguished = TRIPLE_INDEX[column_three]
        return frozenset(
            {
                (row, column)
                for row in row_four_cubics
                for column in column_five_cubics
            }
            | {(row, distinguished) for row in row_five_cubics}
        )
    raise ValueError(kind)


def hook_data(kind: str) -> tuple[tuple[tuple[int, int], ...], tuple[int, ...]]:
    quadratic = product_shadow(canonical_cubic_support(kind))
    cells = tuple(
        sorted(
            {
                (row, column)
                for row_pair, column_pair in quadratic
                for row in PAIRS[row_pair]
                for column in PAIRS[column_pair]
            }
        )
    )
    cell_index = {cell: index for index, cell in enumerate(cells)}
    rectangle_masks = []
    for row_pair, column_pair in sorted(quadratic):
        rectangle_masks.append(
            sum(
                1 << cell_index[row, column]
                for row in PAIRS[row_pair]
                for column in PAIRS[column_pair]
            )
        )
    assert len(canonical_cubic_support(kind)) == 46
    assert len(quadratic) == 72
    assert len(cells) == 23
    return cells, tuple(rectangle_masks)


def edge_masks(
    support_mask: int,
    cells: tuple[tuple[int, int], ...],
    rectangle_masks: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[tuple[tuple[int, int], tuple[int, int]], ...]]:
    chosen = tuple(index for index in range(23) if support_mask >> index & 1)
    local = {global_index: local_index for local_index, global_index in enumerate(chosen)}
    adjacency = [0] * 12
    quadrics = []
    for rectangle in rectangle_masks:
        if rectangle & support_mask != rectangle:
            continue
        corners = [index for index in chosen if rectangle >> index & 1]
        by_cell = {cells[index]: local[index] for index in corners}
        rows = sorted({cells[index][0] for index in corners})
        columns = sorted({cells[index][1] for index in corners})
        edges = (
            (
                by_cell[rows[0], columns[0]],
                by_cell[rows[1], columns[1]],
            ),
            (
                by_cell[rows[0], columns[1]],
                by_cell[rows[1], columns[0]],
            ),
        )
        quadrics.append(edges)
        for left, right in edges:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    return tuple(adjacency), tuple(quadrics)


SIX_MASKS = tuple(sum(1 << index for index in subset) for subset in combinations(range(12), 6))


def coordinate_crossfree_pairs(adjacency: tuple[int, ...]) -> tuple[int, int | None, bool]:
    full = (1 << 12) - 1
    count = 0
    unique_left = None
    unique_diagonal = False
    for left in SIX_MASKS:
        forbidden = 0
        cursor = left
        while cursor:
            bit = cursor & -cursor
            forbidden |= adjacency[bit.bit_length() - 1]
            cursor -= bit
        allowed = full ^ forbidden
        size = allowed.bit_count()
        if size < 6:
            continue
        count += comb(size, 6)
        if count == 1 and size == 6:
            unique_left = left
            unique_diagonal = left == allowed
        else:
            unique_left = None
            unique_diagonal = False
    return count, unique_left, unique_diagonal


def gf2_rank(rows: list[int], column_count: int) -> int:
    pivots = [0] * column_count
    rank = 0
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivots[pivot]:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                rank += 1
                break
    return rank


def pair_jacobian_rank(
    quadrics: tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    plane_mask: int,
) -> int:
    plane = tuple(index for index in range(12) if plane_mask >> index & 1)
    outside = tuple(index for index in range(12) if not (plane_mask >> index & 1))
    outside_index = {vertex: index for index, vertex in enumerate(outside)}
    rows: list[int] = []
    for edges in quadrics:
        local_adjacency = [None] * 12
        for left, right in edges:
            local_adjacency[left] = right
            local_adjacency[right] = left
        for left_index, left_source in enumerate(plane):
            for right_index, right_source in enumerate(plane):
                row = 0
                target = local_adjacency[right_source]
                if target in outside_index:
                    row |= 1 << (left_index * 6 + outside_index[target])
                target = local_adjacency[left_source]
                if target in outside_index:
                    row |= 1 << (36 + right_index * 6 + outside_index[target])
                if row:
                    rows.append(row)
    return gf2_rank(rows, 72)


def rectangle_shape(mask: int, cells: tuple[tuple[int, int], ...]) -> str:
    chosen = {cells[index] for index in range(23) if mask >> index & 1}
    rows = sorted({row for row, _ in chosen})
    columns = sorted({column for _, column in chosen})
    if chosen == {(row, column) for row in rows for column in columns}:
        return f"{len(rows)}x{len(columns)}"
    return "nonproduct"


def hook_certificate(kind: str) -> dict[str, object]:
    cells, rectangle_masks = hook_data(kind)
    intersection_histogram: Counter[int] = Counter()
    shape_histogram: Counter[str] = Counter()
    e12_crossfree_histogram: Counter[int] = Counter()
    rank_histogram: Counter[int] = Counter()
    e12_diagonal_count = 0
    e12_no_pair_count = 0
    complementary_partition_count = 0
    representative = None

    for subset in combinations(range(23), 12):
        support_mask = sum(1 << index for index in subset)
        dimension = sum(
            rectangle & support_mask == rectangle for rectangle in rectangle_masks
        )
        if dimension < 12:
            continue
        intersection_histogram[dimension] += 1
        shape_histogram[rectangle_shape(support_mask, cells)] += 1
        adjacency, quadrics = edge_masks(support_mask, cells, rectangle_masks)
        for left in SIX_MASKS:
            right = ((1 << 12) - 1) ^ left
            if all(not (adjacency[index] & right) for index in range(12) if left >> index & 1):
                complementary_partition_count += 1
        if dimension != 12:
            continue
        pair_count, plane, diagonal = coordinate_crossfree_pairs(adjacency)
        e12_crossfree_histogram[pair_count] += 1
        if pair_count == 0:
            e12_no_pair_count += 1
            continue
        assert pair_count == 1 and plane is not None and diagonal
        e12_diagonal_count += 1
        rank_histogram[pair_jacobian_rank(quadrics, plane)] += 1
        if representative is None:
            chosen = tuple(index for index in range(23) if support_mask >> index & 1)
            local_cells = tuple(cells[index] for index in chosen)
            representative = {
                "U_cells": [list(cell) for cell in local_cells],
                "P_equals_Q_cells": [
                    list(local_cells[index])
                    for index in range(12)
                    if plane >> index & 1
                ],
            }

    assert complementary_partition_count == 0
    assert set(e12_crossfree_histogram) <= {0, 1}
    assert rank_histogram == Counter({72: e12_diagonal_count})
    assert representative is not None
    return {
        "hook": kind,
        "quadratic_dimension": len(rectangle_masks),
        "linear_hook_dimension": len(cells),
        "intersection_dimension_histogram_for_at_least_twelve": {
            str(key): value for key, value in sorted(intersection_histogram.items())
        },
        "coordinate_twelve_plane_shape_histogram_for_at_least_twelve": {
            key: value for key, value in sorted(shape_histogram.items())
        },
        "e12_coordinate_crossfree_ordered_pair_count_histogram": {
            str(key): value for key, value in sorted(e12_crossfree_histogram.items())
        },
        "e12_unique_diagonal_fixed_endpoint_count": e12_diagonal_count,
        "e12_no_fixed_pair_count": e12_no_pair_count,
        "coordinate_complementary_partition_count": complementary_partition_count,
        "pair_variable_jacobian_size": [12 * 6 * 6, 2 * 6 * 6],
        "pair_variable_jacobian_rank_over_F2_histogram": {
            str(key): value for key, value in sorted(rank_histogram.items())
        },
        "fixed_endpoint_representative": representative,
        "rank_over_Q_is_72_at_every_fixed_endpoint": True,
    }


def build_payload() -> dict[str, object]:
    hooks = [hook_certificate("standard"), hook_certificate("biflag")]
    return {
        "status": "EXACT_PROJECTIVE_NONPRODUCT_E12_PAIR_COMPONENT_EXCLUSION",
        "arithmetic": {
            "coordinate_twelve_subsets_per_hook": comb(23, 12),
            "rank_field": "F_2",
            "full_column_rank_over_F2_implies_full_rank_over_Q": True,
        },
        "hooks": hooks,
        "formal_argument": {
            "crossfree_equations_are_invariant_under_swapping_P_and_Q": True,
            "full_pair_variable_jacobian_gives_formal_relative_uniqueness": True,
            "formal_relative_uniqueness_and_swap_force_P_equals_Q": True,
            "projective_torus_components_contain_coordinate_fixed_points": True,
            "every_component_with_an_e12_fixed_point_is_diagonal": True,
            "an_actual_complementary_pair_cannot_lie_on_the_diagonal": True,
        },
        "conclusion": {
            "all_nonproduct_e12_fixed_endpoint_components_are_excluded": True,
            "remaining_fixed_endpoints_have_product_twelve_cell_support": True,
            "standard_remaining_product_support_count": 43,
            "biflag_remaining_product_support_count": 34,
        },
        "boundary": (
            "This excludes only pair-incidence components whose torus-fixed endpoint has "
            "quadratic intersection dimension exactly twelve. The product endpoints with "
            "intersection dimensions fourteen, fifteen, or eighteen remain separate inputs. "
            "It does not by itself exclude the kappa2=0 six-color branches, prove ordinary "
            "lower 29, determine exact Chow rank 32, or prove a border-rank bound."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    if args.json or args.verify_json:
        payload = build_payload()
        if args.json:
            args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        if args.verify_json:
            frozen = json.loads(args.verify_json.read_text())
            if frozen != payload:
                raise SystemExit("frozen JSON does not match regenerated certificate")
    else:
        frozen = json.loads(DEFAULT_JSON.read_text())
        print(frozen["status"])
        for hook in frozen["hooks"]:
            print(
                hook["hook"],
                hook["e12_unique_diagonal_fixed_endpoint_count"],
                hook["pair_variable_jacobian_rank_over_F2_histogram"],
            )


if __name__ == "__main__":
    main()
