#!/usr/bin/env python3
"""Intrinsic and coordinate product-shadow interfaces for a biflag (N6-105)."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_biflag_internal_product_shadow.json"


def canonical_biflag_cells() -> tuple[tuple[int, int], ...]:
    """Cells of R4 x C5 union R5 x C3 in the standard coordinates."""

    return tuple(
        (row, column)
        for row in range(5)
        for column in range(5)
        if row < 4 or column < 3
    )


def rectangle_supports(cells: tuple[tuple[int, int], ...]) -> tuple[frozenset[int], ...]:
    index = {cell: position for position, cell in enumerate(cells)}
    rectangles = []
    for rows in combinations(range(6), 2):
        for columns in combinations(range(6), 2):
            corners = {(row, column) for row in rows for column in columns}
            if corners <= index.keys():
                rectangles.append(frozenset(index[cell] for cell in corners))
    return tuple(rectangles)


def rectangle_quadrics(cells: tuple[tuple[int, int], ...]) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    index = {cell: position for position, cell in enumerate(cells)}
    quadrics = []
    for rows in combinations(range(6), 2):
        for columns in combinations(range(6), 2):
            corners = {(row, column) for row in rows for column in columns}
            if corners <= index.keys():
                left, right = rows
                first, second = columns
                quadrics.append(
                    (
                        tuple(sorted((index[left, first], index[right, second]))),
                        tuple(sorted((index[left, second], index[right, first]))),
                    )
                )
    return tuple(quadrics)


def rational_rank(rows: list[tuple[int, ...]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    column_count = len(matrix[0])
    for column in range(column_count):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                value - scale * pivot_value
                for value, pivot_value in zip(matrix[row], matrix[rank])
            ]
        rank += 1
    return rank


def minimum_nonzero_support(rows: list[tuple[int, ...]]) -> tuple[int, int]:
    """Minimum Hamming weight of A*x outside ker(A), over characteristic zero."""

    full_rank = rational_rank(rows)
    assert full_rank > 0
    for zero_count in range(len(rows), -1, -1):
        for zero_rows in combinations(range(len(rows)), zero_count):
            if rational_rank([rows[index] for index in zero_rows]) < full_rank:
                return len(rows) - zero_count, len(rows[0]) - full_rank
    raise AssertionError(rows)


def tangent_weight(source: tuple[int, int], target: tuple[int, int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    source_row, source_column = source
    target_row, target_column = target
    row_weight = tuple(
        int(index == target_row) - int(index == source_row) for index in range(6)
    )
    column_weight = tuple(
        int(index == target_column) - int(index == source_column) for index in range(6)
    )
    return row_weight, column_weight


def quotient_monomial(
    monomial: tuple[int, int],
    support: frozenset[int],
    cells: tuple[tuple[int, int], ...],
    index: dict[tuple[int, int], int],
) -> tuple[tuple[int, int], int] | None:
    if monomial[0] in support and monomial[1] in support:
        return None
    left, right = monomial
    left_row, left_column = cells[left]
    right_row, right_column = cells[right]
    if left_row == right_row or left_column == right_column:
        return monomial, 1
    opposite_cells = ((left_row, right_column), (right_row, left_column))
    if opposite_cells[0] not in index or opposite_cells[1] not in index:
        return monomial, 1
    opposite = tuple(sorted((index[opposite_cells[0]], index[opposite_cells[1]])))
    if opposite[0] in support and opposite[1] in support:
        return None
    if opposite < monomial:
        return opposite, -1
    return monomial, 1


def first_leakage_certificate(name: str, support_cells: set[tuple[int, int]]) -> dict[str, object]:
    cells = canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    support = frozenset(index[cell] for cell in support_cells)
    outside = tuple(position for position in range(len(cells)) if position not in support)
    quadrics = tuple(
        quadric
        for quadric in rectangle_quadrics(cells)
        if frozenset(quadric[0] + quadric[1]) <= support
    )
    assert len(support) == 12 and len(quadrics) == 18

    variables = tuple((source, target) for source in sorted(support) for target in outside)
    weight_groups: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = {}
    for variable, (source, target) in enumerate(variables):
        weight_groups.setdefault(tangent_weight(cells[source], cells[target]), []).append(variable)

    group_rows = []
    for members in weight_groups.values():
        rows = []
        for first, second in quadrics:
            quotient_class = None
            coefficients = [0] * len(members)
            for local, variable in enumerate(members):
                source, target = variables[variable]
                containing = first if source in first else second if source in second else None
                if containing is None:
                    continue
                other = containing[0] if containing[1] == source else containing[1]
                monomial = tuple(sorted((target, other)))
                quotient = quotient_monomial(monomial, support, cells, index)
                if quotient is None:
                    continue
                key, sign = quotient
                if quotient_class is None:
                    quotient_class = key
                else:
                    assert quotient_class == key
                coefficients[local] += sign
            if any(coefficients):
                rows.append(tuple(coefficients))
        minimum, kernel_dimension = minimum_nonzero_support(rows)
        group_rows.append(
            {
                "variable_count": len(members),
                "independent_output_weight_count": len(rows),
                "kernel_dimension": kernel_dimension,
                "minimum_rank_outside_kernel": minimum,
            }
        )

    kernel_dimension = sum(row["kernel_dimension"] for row in group_rows)
    signature_histogram = Counter(
        (
            row["variable_count"],
            row["independent_output_weight_count"],
            row["kernel_dimension"],
            row["minimum_rank_outside_kernel"],
        )
        for row in group_rows
    )
    assert len(variables) == 132
    assert min(row["minimum_rank_outside_kernel"] for row in group_rows) == 6
    return {
        "name": name,
        "tangent_variable_count": len(variables),
        "supported_rectangle_dimension": len(quadrics),
        "first_leakage_kernel_dimension": kernel_dimension,
        "minimum_rank_outside_kernel": 6,
        "weight_group_signature_histogram": [
            {
                "variable_count": signature[0],
                "independent_output_weight_count": signature[1],
                "kernel_dimension": signature[2],
                "minimum_rank_outside_kernel": signature[3],
                "group_count": count,
            }
            for signature, count in sorted(signature_histogram.items())
        ],
    }


def coordinate_orbit_representatives() -> tuple[tuple[str, set[tuple[int, int]]], ...]:
    return (
        ("3x4_missing_core_column", {(row, column) for row in (0, 1, 2) for column in (1, 2, 3, 4)}),
        ("3x4_missing_wing_column", {(row, column) for row in (0, 1, 2) for column in (0, 1, 2, 4)}),
        ("4x3_core", {(row, column) for row in (0, 1, 2, 3) for column in (0, 1, 2)}),
        ("4x3_two_core_columns", {(row, column) for row in (0, 1, 2, 3) for column in (0, 1, 3)}),
        ("4x3_one_core_column", {(row, column) for row in (0, 1, 2, 3) for column in (0, 3, 4)}),
        ("4x3_tail_row", {(row, column) for row in (0, 1, 2, 4) for column in (0, 1, 2)}),
    )


def intersection_dimension(mask: int) -> int:
    """Number of permanent rectangles supported by a 12-cell subset."""

    row_masks = [
        mask & 0b11111,
        (mask >> 5) & 0b11111,
        (mask >> 10) & 0b11111,
        (mask >> 15) & 0b11111,
        (mask >> 20) & 0b00111,
    ]
    return sum(
        comb((row_masks[left] & row_masks[right]).bit_count(), 2)
        for left, right in combinations(range(5), 2)
    )


def support_profile(mask: int, cells: tuple[tuple[int, int], ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rows = [0] * 6
    columns = [0] * 6
    for position, (row, column) in enumerate(cells):
        if mask >> position & 1:
            rows[row] += 1
            columns[column] += 1
    return tuple(sorted(rows, reverse=True)), tuple(sorted(columns, reverse=True))


def product_shape(mask: int, cells: tuple[tuple[int, int], ...]) -> tuple[int, int] | None:
    support = {cell for position, cell in enumerate(cells) if mask >> position & 1}
    rows = {row for row, _ in support}
    columns = {column for _, column in support}
    if len(rows) * len(columns) != len(support):
        return None
    if support != {(row, column) for row in rows for column in columns}:
        return None
    return len(rows), len(columns)


def enumerate_coordinate_twelve_planes() -> dict[str, object]:
    cells = canonical_biflag_cells()
    dimension_histogram: Counter[int] = Counter()
    survivor_profiles: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
    survivor_shapes: Counter[tuple[int, int] | None] = Counter()
    survivor_dimensions: Counter[int] = Counter()
    survivor_masks = []

    for subset in combinations(range(len(cells)), 12):
        mask = sum(1 << position for position in subset)
        dimension = intersection_dimension(mask)
        dimension_histogram[dimension] += 1
        if dimension >= 15:
            survivor_masks.append(mask)
            survivor_dimensions[dimension] += 1
            survivor_profiles[support_profile(mask, cells)] += 1
            survivor_shapes[product_shape(mask, cells)] += 1

    expected_profiles = {
        ((4, 4, 4, 0, 0, 0), (3, 3, 3, 3, 0, 0)): 20,
        ((3, 3, 3, 3, 0, 0), (4, 4, 4, 0, 0, 0)): 14,
    }
    assert len(cells) == 23
    assert len(rectangle_supports(cells)) == 72
    assert sum(dimension_histogram.values()) == comb(23, 12) == 1_352_078
    assert dict(survivor_dimensions) == {18: 34}
    assert dict(survivor_profiles) == expected_profiles
    assert dict(survivor_shapes) == {(3, 4): 20, (4, 3): 14}
    assert all(intersection_dimension(mask) == 18 for mask in survivor_masks)

    return {
        "ambient_cell_count": len(cells),
        "biflag_rectangle_count": len(rectangle_supports(cells)),
        "enumerated_twelve_cell_support_count": sum(dimension_histogram.values()),
        "intersection_dimension_histogram": {
            str(key): value for key, value in sorted(dimension_histogram.items())
        },
        "supports_with_intersection_dimension_at_least_15": len(survivor_masks),
        "survivor_intersection_dimension_histogram": {
            str(key): value for key, value in sorted(survivor_dimensions.items())
        },
        "survivor_product_shape_counts": {
            f"{rows}x{columns}": count
            for (rows, columns), count in sorted(
                (item for item in survivor_shapes.items() if item[0] is not None)
            )
        },
        "survivor_degree_profiles": [
            {
                "row_degrees": list(row_profile),
                "column_degrees": list(column_profile),
                "count": count,
            }
            for (row_profile, column_profile), count in sorted(survivor_profiles.items())
        ],
        "every_survivor_is_a_complete_product_support": None not in survivor_shapes,
        "every_survivor_has_intersection_dimension_18": set(survivor_dimensions) == {18},
    }


def build_payload() -> dict[str, object]:
    coordinate = enumerate_coordinate_twelve_planes()
    tangent_rows = [
        first_leakage_certificate(name, support)
        for name, support in coordinate_orbit_representatives()
    ]
    assert [row["first_leakage_kernel_dimension"] for row in tangent_rows] == [7, 7, 10, 6, 6, 4]
    return {
        "status": [
            "PURE_BIFLAG_INTRINSIC_72_SPACE",
            "PURE_CORE_CHART_PRODUCT_RIGIDITY",
            "EXACT_COMPLETE_COORDINATE_12_SUPPORT_ENUMERATION",
            "EXACT_QQ_SIX_ORBIT_FIRST_LEAKAGE_GAP",
            "N6-105",
        ],
        "intrinsic_biflag_space": {
            "shape": "M=R4 tensor C5 + R5 tensor C3",
            "coordinate_rectangle_count": 72,
            "torus_specialization_upper_bound": 72,
            "critical_containment_dimension": 72,
            "conclusion": "K=E2 intersect Sym^2(M)",
        },
        "coordinate_enumeration": coordinate,
        "coordinate_first_leakage": {
            "stabilizer_orbit_count": len(tangent_rows),
            "orbit_certificates": tangent_rows,
            "kernel_dimensions": [
                row["first_leakage_kernel_dimension"] for row in tangent_rows
            ],
            "minimum_rank_outside_every_kernel": 6,
            "rank_allowed_by_retaining_a_15_plane_inside_an_18_plane": 3,
            "conclusion": (
                "Every first-order direction of the rank-at-least-15 locus lies in "
                "the factor-deformation kernel at each coordinate fixed point."
            ),
        },
        "core_chart": {
            "core": "Z=A4 tensor C3",
            "wing": "A4 tensor (C5/C3)",
            "tail": "(R5/R4) tensor C3",
            "graph_kernel_normal_form": "T=a tensor I_C3 + I_A4 tensor b",
            "mixed_graph_intersection_upper_bound": 12,
            "required_intersection_dimension": 15,
            "conclusion": (
                "If the projection U to the twelve-dimensional core is an isomorphism, "
                "then U is a product A4' tensor C3 or A4 tensor B3."
            ),
            "actual_pair_consequence": (
                "N6-068 excludes an actual complementary pair throughout this open chart."
            ),
        },
        "next_geometric_interface": (
            "Outside the now-excluded core-projection-isomorphism chart, determine whether "
            "every noncoordinate twelve-plane U in M with "
            "dim(E2 intersect Sym^2(U)) at least 15 is a tensor product A3 tensor B4 "
            "or A4 tensor B3. N6-068 excludes an actual complementary pair once this "
            "product conclusion is known."
        ),
        "claim_boundary": (
            "The intrinsic equality K=E2 intersect Sym^2(M) is a pure characteristic-zero "
            "statement. The 34-support classification is a complete coordinate enumeration "
            "only. It does not classify noncoordinate twelve-planes, exclude the biflag "
            "branch, prove ordinary lower 29, or make a border-rank claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen JSON does not match exact replay")
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
