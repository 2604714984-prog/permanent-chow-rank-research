#!/usr/bin/env python3
"""Exact local diagnostic for the 12 -> 11 small-hook pair incidence.

This is intentionally a local research script.  It separates the derivative
incidence from the cross-free pair equations and reports the torus-weight
blocks of their Zariski tangent spaces over QQ.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

from sympy import SparseMatrix


ROWS = range(6)
COLS = range(6)
CELLS = [(row, col) for row in ROWS for col in COLS]
CELL_INDEX = {cell: index for index, cell in enumerate(CELLS)}
PAIRS = list(combinations(range(6), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_shadow11_pair_incidence_exclusion.json"


def cell_weight(cell: tuple[int, int]) -> tuple[int, ...]:
    row, col = cell
    weight = [0] * 12
    weight[row] = 1
    weight[6 + col] = 1
    return tuple(weight)


def add_weight(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def subtract_weight(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(left, right))


def poly_add(
    left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int]
) -> dict[tuple[int, ...], int]:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def poly_multiply(
    left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int]
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def boolean_replace(
    vector: dict[tuple[int, int], dict[tuple[int, ...], int]],
    axis: str,
    old: int,
    new: int,
    variable: int,
    degree: int,
    scalar: int = 1,
) -> dict[tuple[int, int], dict[tuple[int, ...], int]]:
    subsets = PAIRS if degree == 2 else [(index,) for index in range(6)]
    subset_index = {subset: index for index, subset in enumerate(subsets)}
    result = {key: dict(polynomial) for key, polynomial in vector.items()}
    for (row_index, col_index), polynomial in list(vector.items()):
        chosen = list(subsets[row_index] if axis == "row" else subsets[col_index])
        if old not in chosen or new in chosen:
            continue
        chosen[chosen.index(old)] = new
        replacement = subset_index[tuple(sorted(chosen))]
        key = (
            (replacement, col_index)
            if axis == "row"
            else (row_index, replacement)
        )
        shifted = {
            tuple(sorted(monomial + (variable,))): scalar * coefficient
            for monomial, coefficient in polynomial.items()
        }
        result[key] = poly_add(result.get(key, {}), shifted)
    return {key: polynomial for key, polynomial in result.items() if polynomial}


def transformed_basis(
    base: set[tuple[int, int]],
    row_sources: tuple[int, int, int],
    column_sources: tuple[int, int],
    degree: int,
) -> list[dict[tuple[int, int], dict[tuple[int, ...], int]]]:
    vectors = []
    moves = [
        *(('row', source, target) for source, target in zip(row_sources, (3, 4, 5))),
        *(('column', source, target) for source, target in zip(column_sources, (4, 5))),
    ]
    for key in sorted(base):
        vector = {key: {(): 1}}
        for variable, (axis, old, new) in enumerate(moves):
            vector = boolean_replace(vector, axis, old, new, variable, degree)
        vectors.append(vector)
    return vectors


def product_shadow(support: set[tuple[int, int]]) -> set[tuple[int, int]]:
    return {
        (row_vertex, col_vertex)
        for row_pair_index, col_pair_index in support
        for row_vertex in PAIRS[row_pair_index]
        for col_vertex in PAIRS[col_pair_index]
    }


def equality_support_classification() -> dict[str, object]:
    ordered_pairs = sorted(PAIRS, key=lambda pair: sum(1 << value for value in pair))
    seen: set[int] = set()
    one_factor_sizes = [0]
    weights = []
    for pair in ordered_pairs:
        new_vertices = set(pair) - seen
        weights.append(len(new_vertices))
        seen.update(pair)
        one_factor_sizes.append(len(seen))

    @lru_cache(maxsize=None)
    def solve(index: int, previous: int, remaining: int):
        if index == 15:
            return (0, ((),)) if remaining == 0 else (10**9, ())
        best = 10**9
        witnesses: list[tuple[int, ...]] = []
        for value in range(min(previous, remaining), -1, -1):
            if remaining - value > value * (14 - index):
                continue
            tail_value, tails = solve(index + 1, value, remaining - value)
            candidate = weights[index] * one_factor_sizes[value] + tail_value
            if candidate < best:
                best = candidate
                witnesses = [(value,) + tail for tail in tails]
            elif candidate == best:
                witnesses.extend((value,) + tail for tail in tails)
        return best, tuple(witnesses)

    minimum, profiles = solve(0, 15, 12)

    small_family_rows = []
    for size, shadow_size in ((1, 2), (3, 3), (6, 4)):
        families = [
            family
            for family in combinations(PAIRS, size)
            if len(set().union(*map(set, family))) == shadow_size
        ]
        small_family_rows.append(
            {
                "size": size,
                "vertex_shadow": shadow_size,
                "family_count": len(families),
            }
        )

    row_oriented: set[frozenset[tuple[int, int]]] = set()
    for row_three in combinations(range(6), 3):
        row_edges = list(combinations(row_three, 2))
        for long_row_edge in row_edges:
            for col_four in combinations(range(6), 4):
                for col_three in combinations(col_four, 3):
                    long_columns = list(combinations(col_four, 2))
                    short_columns = list(combinations(col_three, 2))
                    support = {
                        (PAIR_INDEX[tuple(sorted(long_row_edge))], PAIR_INDEX[col_edge])
                        for col_edge in long_columns
                    }
                    support.update(
                        (PAIR_INDEX[row_edge], PAIR_INDEX[col_edge])
                        for row_edge in row_edges
                        if row_edge != long_row_edge
                        for col_edge in short_columns
                    )
                    row_oriented.add(frozenset(support))

    transpose_oriented = {
        frozenset((col, row) for row, col in support) for support in row_oriented
    }
    all_supports = row_oriented | transpose_oriented
    shadow_histogram: dict[int, int] = defaultdict(int)
    for support in all_supports:
        shadow_histogram[len(product_shadow(set(support)))] += 1

    return {
        "minimum": minimum,
        "minimizing_ferrers_profiles": [list(profile) for profile in profiles],
        "small_one_factor_equalities": small_family_rows,
        "row_oriented_count": len(row_oriented),
        "transpose_oriented_count": len(transpose_oriented),
        "overlap_count": len(row_oriented & transpose_oriented),
        "total_coordinate_support_count": len(all_supports),
        "coordinate_shadow_histogram": {
            str(key): value for key, value in sorted(shadow_histogram.items())
        },
    }


def build_problem() -> dict[str, object]:
    quadrics: list[set[tuple[int, int]]] = []
    quadric_weights: list[tuple[int, ...]] = []
    monomial_to_quadric: dict[tuple[int, int], int] = {}
    for first_row, second_row in combinations(ROWS, 2):
        for first_col, second_col in combinations(COLS, 2):
            monomials = {
                tuple(
                    sorted(
                        (
                            CELL_INDEX[(first_row, first_col)],
                            CELL_INDEX[(second_row, second_col)],
                        )
                    )
                ),
                tuple(
                    sorted(
                        (
                            CELL_INDEX[(first_row, second_col)],
                            CELL_INDEX[(second_row, first_col)],
                        )
                    )
                ),
            }
            quadric_index = len(quadrics)
            quadrics.append(monomials)
            quadric_weights.append(
                add_weight(
                    cell_weight((first_row, first_col)),
                    cell_weight((second_row, second_col)),
                )
            )
            for monomial in monomials:
                monomial_to_quadric[monomial] = quadric_index

    hook_cells = [
        *(CELL_INDEX[(row, col)] for row in (0, 1) for col in range(4)),
        *(CELL_INDEX[(2, col)] for col in range(3)),
    ]
    hook_set = set(hook_cells)
    outside_cells = [index for index in range(36) if index not in hook_set]
    base_quadrics = [
        index
        for index, monomials in enumerate(quadrics)
        if all(left in hook_set and right in hook_set for left, right in monomials)
    ]
    base_quadric_set = set(base_quadrics)
    outside_quadrics = [index for index in range(225) if index not in base_quadric_set]

    annihilator = [
        CELL_INDEX[cell]
        for cell in ((0, 3), (1, 3), (2, 0), (2, 1), (2, 2))
    ]
    annihilator_set = set(annihilator)
    annihilator_complement = [cell for cell in hook_cells if cell not in annihilator_set]

    return {
        "quadrics": quadrics,
        "quadric_weights": quadric_weights,
        "monomial_to_quadric": monomial_to_quadric,
        "hook_cells": hook_cells,
        "outside_cells": outside_cells,
        "base_quadrics": base_quadrics,
        "outside_quadrics": outside_quadrics,
        "annihilator": annihilator,
        "annihilator_complement": annihilator_complement,
    }


def coordinate_pair_scan(problem: dict[str, object]) -> dict[str, object]:
    quadrics = problem["quadrics"]
    hook_cells = problem["hook_cells"]
    base_quadrics = problem["base_quadrics"]
    local_index = {ambient: index for index, ambient in enumerate(hook_cells)}
    local_monomials = [
        tuple(sorted((local_index[left], local_index[right])))
        for quadric in base_quadrics
        for left, right in quadrics[quadric]
    ]

    def cross_free(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
        left_set = set(left)
        right_set = set(right)
        return not any(
            (first in left_set and second in right_set)
            or (second in left_set and first in right_set)
            for first, second in local_monomials
        )

    five_planes = list(combinations(range(11), 5))
    five_pairs = [
        (left, right)
        for left in five_planes
        for right in five_planes
        if cross_free(left, right)
    ]
    six_planes = list(combinations(range(11), 6))
    five_six_pair_count = sum(
        cross_free(left, right) for left in five_planes for right in six_planes
    )
    six_five_pair_count = sum(
        cross_free(left, right) for left in six_planes for right in five_planes
    )
    six_pair_count = sum(
        cross_free(left, right) for left in six_planes for right in six_planes
    )
    return {
        "coordinate_five_plane_count": len(five_planes),
        "ordered_five_pair_count": len(five_planes) ** 2,
        "cross_free_five_pairs": [
            {
                "left": [list(CELLS[hook_cells[index]]) for index in left],
                "right": [list(CELLS[hook_cells[index]]) for index in right],
                "intersection_dimension": len(set(left) & set(right)),
            }
            for left, right in five_pairs
        ],
        "coordinate_six_plane_count": len(six_planes),
        "cross_free_five_six_pair_count": five_six_pair_count,
        "cross_free_six_five_pair_count": six_five_pair_count,
        "ordered_six_pair_count": len(six_planes) ** 2,
        "cross_free_six_pair_count": six_pair_count,
    }


def branch_replay(problem: dict[str, object]) -> dict[str, object]:
    hook_cells = problem["hook_cells"]
    base_quadrics = problem["base_quadrics"]
    base_d = {(quadric // 15, quadric % 15) for quadric in base_quadrics}
    base_u = {CELLS[cell] for cell in hook_cells}
    base_u_keys = {(row, col) for row, col in base_u}
    annihilator_cells = {
        CELLS[cell]
        for cell in problem["annihilator"]
    }

    def pull_back(
        vector: dict[tuple[int, int], dict[tuple[int, ...], int]],
        row_sources: tuple[int, int, int],
        column_sources: tuple[int, int],
        degree: int,
    ) -> dict[tuple[int, int], dict[tuple[int, ...], int]]:
        moves = [
            *(('row', source, target) for source, target in zip(row_sources, (3, 4, 5))),
            *(('column', source, target) for source, target in zip(column_sources, (4, 5))),
        ]
        for variable, (axis, old, new) in reversed(list(enumerate(moves))):
            vector = boolean_replace(
                vector, axis, old, new, variable, degree, scalar=-1
            )
        return vector

    branch_count = 0
    derivative_failures = 0
    cross_free_failures = 0
    jacobian_failures = 0
    for row_sources in product(range(3), repeat=3):
        for column_sources in product(range(4), repeat=2):
            branch_count += 1
            quadratic_vectors = transformed_basis(
                base_d, row_sources, column_sources, degree=2
            )
            linear_vectors = transformed_basis(
                base_u_keys, row_sources, column_sources, degree=1
            )
            linear_by_source = {
                source: vector
                for source, vector in zip(sorted(base_u_keys), linear_vectors)
            }

            derivative_ok = True
            for quadratic_vector in quadratic_vectors:
                for row in range(6):
                    for col in range(6):
                        derivative: dict[
                            tuple[int, int], dict[tuple[int, ...], int]
                        ] = {}
                        for (row_pair_index, col_pair_index), polynomial in quadratic_vector.items():
                            row_pair = PAIRS[row_pair_index]
                            col_pair = PAIRS[col_pair_index]
                            if row in row_pair and col in col_pair:
                                key = (
                                    next(value for value in row_pair if value != row),
                                    next(value for value in col_pair if value != col),
                                )
                                derivative[key] = poly_add(
                                    derivative.get(key, {}), polynomial
                                )
                        restored = pull_back(
                            derivative, row_sources, column_sources, degree=1
                        )
                        if any(key not in base_u_keys for key in restored):
                            derivative_ok = False
            derivative_failures += int(not derivative_ok)

            cross_free_ok = True
            for quadratic_vector in quadratic_vectors:
                for left_source in annihilator_cells:
                    for right_source in annihilator_cells:
                        value: dict[tuple[int, ...], int] = {}
                        left_vector = linear_by_source[left_source]
                        right_vector = linear_by_source[right_source]
                        for (row_pair_index, col_pair_index), coefficient in quadratic_vector.items():
                            row_pair = PAIRS[row_pair_index]
                            col_pair = PAIRS[col_pair_index]
                            opposite_monomials = (
                                ((row_pair[0], col_pair[0]), (row_pair[1], col_pair[1])),
                                ((row_pair[0], col_pair[1]), (row_pair[1], col_pair[0])),
                            )
                            for first_cell, second_cell in opposite_monomials:
                                first_left = left_vector.get(first_cell, {})
                                second_right = right_vector.get(second_cell, {})
                                second_left = left_vector.get(second_cell, {})
                                first_right = right_vector.get(first_cell, {})
                                term = poly_add(
                                    poly_multiply(first_left, second_right),
                                    poly_multiply(second_left, first_right),
                                )
                                scaled = poly_multiply(term, coefficient)
                                value = poly_add(value, scaled)
                        if value:
                            cross_free_ok = False
            cross_free_failures += int(not cross_free_ok)

            desired_moves = [
                *(('row', source, target) for source, target in zip(row_sources, (3, 4, 5))),
                *(('column', source, target) for source, target in zip(column_sources, (4, 5))),
            ]
            jacobian = []
            for axis, old, new in desired_moves:
                source = (old, 0) if axis == "row" else (0, old)
                target = (new, source[1]) if axis == "row" else (source[0], new)
                polynomial = linear_by_source[source].get(target, {})
                jacobian.append([polynomial.get((variable,), 0) for variable in range(5)])
            jacobian_failures += int(
                jacobian != [[int(i == j) for j in range(5)] for i in range(5)]
            )

    return {
        "branch_count": branch_count,
        "derivative_containment_failures": derivative_failures,
        "diagonal_cross_free_failures": cross_free_failures,
        "selected_jacobian_failures": jacobian_failures,
    }


def analyse() -> dict[str, object]:
    problem = build_problem()
    quadrics = problem["quadrics"]
    quadric_weights = problem["quadric_weights"]
    monomial_to_quadric = problem["monomial_to_quadric"]
    hook_cells = problem["hook_cells"]
    outside_cells = problem["outside_cells"]
    base_quadrics = problem["base_quadrics"]
    outside_quadrics = problem["outside_quadrics"]
    annihilator = problem["annihilator"]
    annihilator_complement = problem["annihilator_complement"]
    outside_quadric_set = set(outside_quadrics)

    variables: list[tuple[object, ...]] = []
    variable_weight: dict[tuple[object, ...], tuple[int, ...]] = {}

    def add_variable(key: tuple[object, ...], weight: tuple[int, ...]) -> None:
        variables.append(key)
        variable_weight[key] = weight

    for source in base_quadrics:
        for target in outside_quadrics:
            add_variable(
                ("eta", source, target),
                subtract_weight(quadric_weights[target], quadric_weights[source]),
            )
    for source in hook_cells:
        for target in outside_cells:
            add_variable(
                ("u", source, target),
                subtract_weight(cell_weight(CELLS[target]), cell_weight(CELLS[source])),
            )
    for tag in ("P", "Q"):
        for source in annihilator:
            for target in annihilator_complement:
                add_variable(
                    (tag, source, target),
                    subtract_weight(cell_weight(CELLS[source]), cell_weight(CELLS[target])),
                )

    variables_by_weight: dict[tuple[int, ...], list[tuple[object, ...]]] = defaultdict(list)
    for variable in variables:
        variables_by_weight[variable_weight[variable]].append(variable)

    RowRecord = tuple[tuple[object, ...], dict[tuple[object, ...], int]]
    derivative_rows: dict[tuple[int, ...], list[RowRecord]] = defaultdict(list)
    cross_rows: dict[tuple[int, ...], list[RowRecord]] = defaultdict(list)

    def quadric_coefficient(quadric: int, left: int, right: int) -> int:
        return int(tuple(sorted((left, right))) in quadrics[quadric])

    def append_row(
        destination: dict[tuple[int, ...], list[RowRecord]],
        label: tuple[object, ...],
        row: dict[tuple[object, ...], int],
        expected_weight: tuple[int, ...],
    ) -> None:
        row = {variable: coefficient for variable, coefficient in row.items() if coefficient}
        if row:
            weights = {variable_weight[variable] for variable in row}
            if weights != {expected_weight}:
                raise RuntimeError(
                    f"wrong torus weight in row {label}: {weights} != {expected_weight}"
                )
        destination[expected_weight].append((label, row))

    for source_quadric in base_quadrics:
        for outside_cell in outside_cells:
            for derivative_cell in range(36):
                row: dict[tuple[object, ...], int] = {}
                target_quadric = None
                if outside_cell != derivative_cell:
                    target_quadric = monomial_to_quadric.get(
                        tuple(sorted((outside_cell, derivative_cell)))
                    )
                if target_quadric in outside_quadric_set:
                    row[("eta", source_quadric, target_quadric)] = 1
                for hook_cell in hook_cells:
                    if quadric_coefficient(source_quadric, hook_cell, derivative_cell):
                        row[("u", hook_cell, outside_cell)] = -1
                append_row(
                    derivative_rows,
                    ("derivative", source_quadric, outside_cell, derivative_cell),
                    row,
                    subtract_weight(
                        add_weight(
                            cell_weight(CELLS[outside_cell]),
                            cell_weight(CELLS[derivative_cell]),
                        ),
                        quadric_weights[source_quadric],
                    ),
                )

    for source_quadric in base_quadrics:
        for left in annihilator:
            for right in annihilator:
                row = {}
                target_quadric = None
                if left != right:
                    target_quadric = monomial_to_quadric.get(tuple(sorted((left, right))))
                if target_quadric in outside_quadric_set:
                    row[("eta", source_quadric, target_quadric)] = 1
                for target in annihilator_complement:
                    if quadric_coefficient(source_quadric, target, right):
                        row[("P", left, target)] = 1
                    if quadric_coefficient(source_quadric, left, target):
                        row[("Q", right, target)] = 1
                append_row(
                    cross_rows,
                    ("cross", source_quadric, left, right),
                    row,
                    subtract_weight(
                        add_weight(cell_weight(CELLS[left]), cell_weight(CELLS[right])),
                        quadric_weights[source_quadric],
                    ),
                )

    block_records: list[dict[str, object]] = []
    tangent_directions: list[dict[str, object]] = []
    totals = {
        "derivative_nullity": 0,
        "full_nullity": 0,
        "separation_image_dimension": 0,
        "diagonal_pair_image_dimension": 0,
    }

    for weight, block_variables in variables_by_weight.items():
        local_index = {variable: index for index, variable in enumerate(block_variables)}

        def matrix_from_rows(rows: list[RowRecord]) -> SparseMatrix:
            entries = {
                (row_index, local_index[variable]): coefficient
                for row_index, (_, row) in enumerate(rows)
                for variable, coefficient in row.items()
            }
            return SparseMatrix(len(rows), len(block_variables), entries)

        derivative_matrix = matrix_from_rows(derivative_rows.get(weight, []))
        full_matrix = matrix_from_rows(
            derivative_rows.get(weight, []) + cross_rows.get(weight, [])
        )
        derivative_rank = derivative_matrix.rank()
        full_rank = full_matrix.rank()
        derivative_nullity = len(block_variables) - derivative_rank
        full_nullity = len(block_variables) - full_rank

        difference_rows: list[RowRecord] = []
        diagonal_rows: list[RowRecord] = []
        for source in annihilator:
            for target in annihilator_complement:
                left = ("P", source, target)
                right = ("Q", source, target)
                if left in local_index and right in local_index:
                    difference_rows.append((("difference", source, target), {left: 1, right: -1}))
                    diagonal_rows.append((("diagonal", source, target), {left: 1, right: 1}))

        def kernel_image_dimension(rows: list[RowRecord]) -> int:
            if not rows:
                return 0
            probe = matrix_from_rows(rows)
            return full_matrix.col_join(probe).rank() - full_rank

        separation_dimension = kernel_image_dimension(difference_rows)
        diagonal_dimension = kernel_image_dimension(diagonal_rows)

        if full_nullity:
            if full_nullity != 1:
                raise RuntimeError(f"unexpected full nullity {full_nullity} at weight {weight}")
            null_vector = full_matrix.nullspace()[0]
            vector = {
                variable: null_vector[index]
                for index, variable in enumerate(block_variables)
                if null_vector[index]
            }
            nonzero_u = [variable for variable in vector if variable[0] == "u"]
            if not nonzero_u:
                raise RuntimeError(f"surviving tangent without a hook motion at weight {weight}")
            pivot = nonzero_u[0]
            scale = vector[pivot]
            vector = {variable: coefficient / scale for variable, coefficient in vector.items()}
            source_cell = CELLS[pivot[1]]
            target_cell = CELLS[pivot[2]]
            if source_cell[1] == target_cell[1]:
                move = ("row", source_cell[0], target_cell[0])
            elif source_cell[0] == target_cell[0]:
                move = ("column", source_cell[1], target_cell[1])
            else:
                raise RuntimeError(f"non-axis hook motion: {source_cell} -> {target_cell}")
            tangent_directions.append(
                {"weight": weight, "move": move, "vector": vector}
            )
        totals["derivative_nullity"] += derivative_nullity
        totals["full_nullity"] += full_nullity
        totals["separation_image_dimension"] += separation_dimension
        totals["diagonal_pair_image_dimension"] += diagonal_dimension

        if derivative_nullity or full_nullity:
            block_records.append(
                {
                    "weight": weight,
                    "variables": len(block_variables),
                    "derivative_rank": derivative_rank,
                    "derivative_nullity": derivative_nullity,
                    "full_rank": full_rank,
                    "full_nullity": full_nullity,
                    "separation_dimension": separation_dimension,
                    "diagonal_dimension": diagonal_dimension,
                    "variable_types": dict(
                        (tag, sum(variable[0] == tag for variable in block_variables))
                        for tag in ("eta", "u", "P", "Q")
                    ),
                }
            )

    tangent_directions.sort(key=lambda record: record["move"])

    quadratic_columns: dict[
        tuple[int, ...],
        list[tuple[tuple[int, int], dict[tuple[object, ...], object]]],
    ] = defaultdict(list)

    def accumulate_derivative_quadratic(
        output: dict[tuple[object, ...], object],
        u_vector: dict[tuple[object, ...], object],
        eta_vector: dict[tuple[object, ...], object],
    ) -> None:
        for u_variable, u_coefficient in u_vector.items():
            if u_variable[0] != "u":
                continue
            _, source_cell, outside_cell = u_variable
            for eta_variable, eta_coefficient in eta_vector.items():
                if eta_variable[0] != "eta":
                    continue
                _, source_quadric, target_quadric = eta_variable
                for left, right in quadrics[target_quadric]:
                    if left == source_cell:
                        derivative_cell = right
                    elif right == source_cell:
                        derivative_cell = left
                    else:
                        continue
                    label = (
                        "derivative",
                        source_quadric,
                        outside_cell,
                        derivative_cell,
                    )
                    output[label] = (
                        output.get(label, 0) - u_coefficient * eta_coefficient
                    )

    for first_index, first_direction in enumerate(tangent_directions):
        for second_index in range(first_index, len(tangent_directions)):
            second_direction = tangent_directions[second_index]
            quadratic: dict[tuple[object, ...], object] = {}
            accumulate_derivative_quadratic(
                quadratic,
                first_direction["vector"],
                second_direction["vector"],
            )
            if first_index != second_index:
                accumulate_derivative_quadratic(
                    quadratic,
                    second_direction["vector"],
                    first_direction["vector"],
                )
            quadratic = {label: coefficient for label, coefficient in quadratic.items() if coefficient}
            weight = add_weight(first_direction["weight"], second_direction["weight"])
            quadratic_columns[weight].append(
                ((first_index, second_index), quadratic)
            )

    quadratic_rank = 0
    obstructed_pairs: set[tuple[int, int]] = set()
    quadratic_weight_records: list[dict[str, object]] = []
    for weight, columns in quadratic_columns.items():
        block_variables = variables_by_weight.get(weight, [])
        local_index = {variable: index for index, variable in enumerate(block_variables)}
        records = derivative_rows.get(weight, []) + cross_rows.get(weight, [])
        row_index = {label: index for index, (label, _) in enumerate(records)}
        linear_entries = {
            (record_index, local_index[variable]): coefficient
            for record_index, (_, row) in enumerate(records)
            for variable, coefficient in row.items()
        }
        linear_matrix = SparseMatrix(
            len(records), len(block_variables), linear_entries
        )
        linear_rank = linear_matrix.rank()
        quadratic_entries = {
            (row_index[label], column_index): coefficient
            for column_index, (_, column) in enumerate(columns)
            for label, coefficient in column.items()
        }
        quadratic_matrix = SparseMatrix(
            len(records), len(columns), quadratic_entries
        )
        augmented_rank = linear_matrix.row_join(quadratic_matrix).rank()
        weight_obstruction_rank = augmented_rank - linear_rank
        quadratic_rank += weight_obstruction_rank
        individually_obstructed: list[tuple[int, int]] = []
        for column_index, (pair, _) in enumerate(columns):
            single_rank = linear_matrix.row_join(
                quadratic_matrix[:, column_index]
            ).rank()
            if single_rank > linear_rank:
                individually_obstructed.append(pair)
                obstructed_pairs.add(pair)
        if weight_obstruction_rank:
            quadratic_weight_records.append(
                {
                    "weight": weight,
                    "monomial_count": len(columns),
                    "obstruction_rank": weight_obstruction_rank,
                    "individually_obstructed": individually_obstructed,
                }
            )

    expected_forbidden = {
        (first_index, second_index)
        for first_index in range(len(tangent_directions))
        for second_index in range(first_index + 1, len(tangent_directions))
        if tangent_directions[first_index]["move"][0]
        == tangent_directions[second_index]["move"][0]
        and tangent_directions[first_index]["move"][2]
        == tangent_directions[second_index]["move"][2]
    }

    quadratic_summary = {
        "monomial_count": sum(len(columns) for columns in quadratic_columns.values()),
        "obstruction_rank": quadratic_rank,
        "individually_obstructed_count": len(obstructed_pairs),
        "expected_forbidden_count": len(expected_forbidden),
        "missing_expected": sorted(expected_forbidden - obstructed_pairs),
        "unexpected_obstructed": sorted(obstructed_pairs - expected_forbidden),
        "weight_records": quadratic_weight_records,
    }

    return {
        "ambient_dimension": 36,
        "hook_dimension": len(hook_cells),
        "quadratic_dimension": len(base_quadrics),
        "annihilator_dimension": len(annihilator),
        "variable_count": len(variables),
        "weight_group_count": len(variables_by_weight),
        **totals,
        "nonzero_blocks": block_records,
        "tangent_directions": tangent_directions,
        "quadratic_summary": quadratic_summary,
        "equality_support_classification": equality_support_classification(),
        "coordinate_pair_scan": coordinate_pair_scan(problem),
        "branch_replay": branch_replay(problem),
    }


def build_payload() -> dict[str, object]:
    result = analyse()
    quadratic = result["quadratic_summary"]
    moves = [record["move"] for record in result["tangent_directions"]]
    move_groups: dict[str, int] = defaultdict(int)
    for axis, _, target in moves:
        move_groups[f"{axis}_target_{target}"] += 1
    coordinate_scan = result["coordinate_pair_scan"]
    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_SHADOW11_ACTUAL_PAIR_EXCLUSION",
            "PURE_PROJECTIVE_EQUALITY_LOCUS_GLOBALIZATION",
            "EXACT_QQ_LINEAR_AND_QUADRATIC_ELIMINATION",
            "EXACT_SYMBOLIC_432_BRANCH_REPLAY",
            "N6-110",
        ],
        "equality_support_classification": result[
            "equality_support_classification"
        ],
        "standard_fixed_point": {
            "ambient_dimension": result["ambient_dimension"],
            "hook_dimension": result["hook_dimension"],
            "quadratic_dimension": result["quadratic_dimension"],
            "annihilator_dimension": result["annihilator_dimension"],
        },
        "coordinate_cross_free_scan": {
            "coordinate_five_plane_count": coordinate_scan[
                "coordinate_five_plane_count"
            ],
            "ordered_five_pair_count": coordinate_scan["ordered_five_pair_count"],
            "cross_free_five_pair_count": len(
                coordinate_scan["cross_free_five_pairs"]
            ),
            "cross_free_five_pairs": coordinate_scan["cross_free_five_pairs"],
            "coordinate_six_plane_count": coordinate_scan[
                "coordinate_six_plane_count"
            ],
            "ordered_six_pair_count": coordinate_scan["ordered_six_pair_count"],
            "cross_free_five_six_pair_count": coordinate_scan[
                "cross_free_five_six_pair_count"
            ],
            "cross_free_six_five_pair_count": coordinate_scan[
                "cross_free_six_five_pair_count"
            ],
            "cross_free_six_pair_count": coordinate_scan[
                "cross_free_six_pair_count"
            ],
        },
        "linear_incidence": {
            "variable_count": result["variable_count"],
            "torus_weight_group_count": result["weight_group_count"],
            "derivative_incidence_nullity": result["derivative_nullity"],
            "full_pair_incidence_nullity": result["full_nullity"],
            "pair_separation_image_dimension": result[
                "separation_image_dimension"
            ],
            "pair_diagonal_image_dimension": result[
                "diagonal_pair_image_dimension"
            ],
            "free_move_groups": dict(sorted(move_groups.items())),
            "free_move_count": len(moves),
        },
        "quadratic_initial_ideal": {
            "quadratic_monomial_count": quadratic["monomial_count"],
            "obstruction_rank": quadratic["obstruction_rank"],
            "individually_obstructed_count": quadratic[
                "individually_obstructed_count"
            ],
            "expected_same_target_generator_count": quadratic[
                "expected_forbidden_count"
            ],
            "missing_expected_generators": quadratic["missing_expected"],
            "unexpected_obstructed_monomials": quadratic[
                "unexpected_obstructed"
            ],
            "radical_facets": 3**3 * 4**2,
            "facet_dimension": 5,
        },
        "symbolic_branches": result["branch_replay"],
        "pure_theorem": (
            "If D is a twelve-plane in the permanent rectangle space E2 and "
            "D is an actual section-difference space for two six-planes, then "
            "dim(partial D)=12 and the two factor six-planes are transverse."
        ),
        "kappa_zero_consequence": (
            "At the a2=72,kappa2=0 critical six-term layer, every pair quotient "
            "intersection has dimension at least twelve; any twelve-dimensional "
            "subspace of its section difference has full twelve-dimensional "
            "shadow. Hence all six factor planes are pairwise transverse and "
            "their sum equals the N6-101 23-plane."
        ),
        "claim_boundary": (
            "The theorem closes the shadow-eleven pair collision and strengthens "
            "the kappa2=0 geometry. It does not yet exclude the resulting standard "
            "or biflag six-color configurations, prove ordinary lower 29, determine "
            "ChowRank(perm_6)=32, or prove a border-rank statement."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify_json:
        if args.verify_json.read_text(encoding="utf-8") != encoded:
            raise SystemExit("frozen JSON does not match exact replay")
        print("PASS")
        return
    destination = args.json or DEFAULT_JSON
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(encoded, encoding="utf-8")
    print(
        json.dumps(
            {
                "fixed_supports": payload["equality_support_classification"][
                    "total_coordinate_support_count"
                ],
                "full_nullity": payload["linear_incidence"][
                    "full_pair_incidence_nullity"
                ],
                "quadratic_rank": payload["quadratic_initial_ideal"][
                    "obstruction_rank"
                ],
                "branches": payload["symbolic_branches"]["branch_count"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
