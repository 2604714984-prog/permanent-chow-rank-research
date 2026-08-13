#!/usr/bin/env python3
"""Exact graph-chart reduction at the biflag 3 x 4 endpoints (N6-106)."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_biflag_three_by_four_chart.json"

Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]


def canonical_biflag_cells() -> tuple[tuple[int, int], ...]:
    return tuple(
        (row, column)
        for row in range(5)
        for column in range(5)
        if row < 4 or column < 3
    )


def rectangle_quadrics(
    cells: tuple[tuple[int, int], ...],
) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
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
    for column in range(len(matrix[0])):
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


def tangent_weight(
    source: tuple[int, int], target: tuple[int, int]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    source_row, source_column = source
    target_row, target_column = target
    return (
        tuple(int(index == target_row) - int(index == source_row) for index in range(6)),
        tuple(
            int(index == target_column) - int(index == source_column)
            for index in range(6)
        ),
    )


def quotient_monomial(
    monomial: tuple[int, int],
    support: frozenset[int],
    cells: tuple[tuple[int, int], ...],
    index: dict[tuple[int, int], int],
) -> tuple[tuple[int, int], int] | None:
    """Reduce modulo Sym^2(U0) and the 54 outside permanent rectangles."""

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


def add_polynomial_term(polynomial: Polynomial, monomial: Monomial, coefficient: int) -> None:
    value = polynomial.get(monomial, 0) + coefficient
    if value:
        polynomial[monomial] = value
    else:
        polynomial.pop(monomial, None)


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            add_polynomial_term(
                answer,
                tuple(sorted(left_monomial + right_monomial)),
                left_coefficient * right_coefficient,
            )
    return answer


def graph_linear_expansion(
    support_cells: set[tuple[int, int]],
) -> tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    tuple[dict[tuple[int, int], Polynomial], ...],
]:
    """Expand the 18 base rectangles in all 132 affine graph variables."""

    cells = canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    support = frozenset(index[cell] for cell in support_cells)
    outside = tuple(position for position in range(len(cells)) if position not in support)
    variables = tuple((source, target) for source in sorted(support) for target in outside)
    variable_index = {variable: position for position, variable in enumerate(variables)}
    quadrics = tuple(
        quadric
        for quadric in rectangle_quadrics(cells)
        if frozenset(quadric[0] + quadric[1]) <= support
    )
    assert len(support) == 12 and len(outside) == 11
    assert len(variables) == 132 and len(quadrics) == 18

    columns = []
    for quadric in quadrics:
        column: dict[tuple[int, int], Polynomial] = defaultdict(dict)
        for source_pair in quadric:
            first, second = source_pair
            for source, other in ((first, second), (second, first)):
                for target in outside:
                    quotient = quotient_monomial(
                        tuple(sorted((target, other))), support, cells, index
                    )
                    if quotient is None:
                        continue
                    key, sign = quotient
                    add_polynomial_term(
                        column[key], (variable_index[source, target],), sign
                    )
            for first_target in outside:
                for second_target in outside:
                    quotient = quotient_monomial(
                        tuple(sorted((first_target, second_target))),
                        support,
                        cells,
                        index,
                    )
                    if quotient is None:
                        continue
                    key, sign = quotient
                    add_polynomial_term(
                        column[key],
                        tuple(
                            sorted(
                                (
                                    variable_index[first, first_target],
                                    variable_index[second, second_target],
                                )
                            )
                        ),
                        sign,
                    )
        columns.append({key: value for key, value in column.items() if value})
    return variables, quadrics, tuple(columns)


def expected_kernel_vectors(
    support_cells: set[tuple[int, int]],
    variables: tuple[tuple[int, int], ...],
    include_tail: bool,
) -> list[tuple[int, ...]]:
    cells = canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    variable_index = {variable: position for position, variable in enumerate(variables)}
    selected_rows = sorted({row for row, _ in support_cells})
    selected_columns = sorted({column for _, column in support_cells})
    missing_row = next(row for row in range(4) if row not in selected_rows)
    missing_column = next(column for column in range(5) if column not in selected_columns)
    answer = []

    for row in selected_rows:
        vector = [0] * len(variables)
        for column in selected_columns:
            vector[variable_index[index[row, column], index[missing_row, column]]] = 1
        answer.append(tuple(vector))
    for column in selected_columns:
        vector = [0] * len(variables)
        for row in selected_rows:
            vector[variable_index[index[row, column], index[row, missing_column]]] = 1
        answer.append(tuple(vector))
    for row in selected_rows:
        for column in selected_columns:
            vector = [0] * len(variables)
            vector[
                variable_index[index[row, column], index[missing_row, missing_column]]
            ] = 1
            answer.append(tuple(vector))
    if include_tail:
        tail_target = index[4, missing_column]
        for row in selected_rows:
            for column in selected_columns:
                vector = [0] * len(variables)
                vector[variable_index[index[row, column], tail_target]] = 1
                answer.append(tuple(vector))
    assert len(answer) == 19 + 12 * int(include_tail)
    return answer


def linear_only_certificate(
    name: str, support_cells: set[tuple[int, int]]
) -> dict[str, object]:
    cells = canonical_biflag_cells()
    variables, quadrics, columns = graph_linear_expansion(support_cells)
    all_keys = set().union(*(set(column) for column in columns))
    quadratic_keys = {
        key
        for column in columns
        for key, polynomial in column.items()
        if any(len(monomial) == 2 for monomial in polynomial)
    }
    linear_only_keys = all_keys - quadratic_keys

    selected_columns = sorted({column for _, column in support_cells})
    missing_column = next(column for column in range(5) if column not in selected_columns)
    index = {cell: position for position, cell in enumerate(cells)}
    tail_target = index.get((4, missing_column))
    tail_variables = {
        variable
        for variable, (_, target) in enumerate(variables)
        if tail_target is not None and target == tail_target
    }
    tail_touched_keys = {
        key
        for key in linear_only_keys
        if any(
            column.get(key, {}).get((variable,), 0)
            for column in columns
            for variable in tail_variables
        )
    }
    effective_keys = linear_only_keys - tail_touched_keys

    coefficient_rows = []
    for column in columns:
        for key in sorted(effective_keys):
            polynomial = column.get(key, {})
            row = tuple(polynomial.get((variable,), 0) for variable in range(len(variables)))
            if any(row):
                coefficient_rows.append(row)
    linear_rank = rational_rank(coefficient_rows)
    expected = expected_kernel_vectors(support_cells, variables, tail_target is not None)
    assert rational_rank(expected) == len(expected)
    assert all(
        sum(row[index] * vector[index] for index in range(len(variables))) == 0
        for row in coefficient_rows
        for vector in expected
    )
    assert linear_rank == len(variables) - len(expected)

    weight_groups: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = defaultdict(list)
    for variable, (source, target) in enumerate(variables):
        weight_groups[tangent_weight(cells[source], cells[target])].append(variable)

    signatures = []
    for members in weight_groups.values():
        rows = []
        for column in columns:
            nonzero_rows = []
            for key in effective_keys:
                polynomial = column.get(key, {})
                row = tuple(polynomial.get((variable,), 0) for variable in members)
                if any(row):
                    nonzero_rows.append(row)
            assert len(nonzero_rows) <= 1
            if nonzero_rows:
                rows.append(nonzero_rows[0])
        if rows:
            minimum, kernel_dimension = minimum_nonzero_support(rows)
        else:
            minimum, kernel_dimension = 0, len(members)
        signatures.append((len(members), len(rows), kernel_dimension, minimum))

    assert sum(signature[2] for signature in signatures) == len(expected)
    minimum_rank = min(signature[3] for signature in signatures if signature[3])
    return {
        "name": name,
        "graph_variable_count": len(variables),
        "base_rectangle_dimension": len(quadrics),
        "linear_only_quotient_weight_count": len(linear_only_keys),
        "discarded_tail_touched_weight_count": len(tail_touched_keys),
        "effective_linear_quotient_weight_count": len(effective_keys),
        "linear_equation_rank_over_Q": linear_rank,
        "kernel_dimension": len(variables) - linear_rank,
        "expected_normal_form_dimension": len(expected),
        "tail_parameter_count": len(tail_variables),
        "minimum_rank_outside_kernel": minimum_rank,
        "weight_group_signature_histogram": [
            {
                "variable_count": signature[0],
                "independent_output_weight_count": signature[1],
                "kernel_dimension": signature[2],
                "minimum_rank_outside_kernel": signature[3],
                "group_count": count,
            }
            for signature, count in sorted(Counter(signatures).items())
        ],
    }


def add_vector_product(
    column: dict[tuple[int, int], Polynomial],
    left_cell: int,
    left: Polynomial,
    right_cell: int,
    right: Polynomial,
    support: frozenset[int],
    cells: tuple[tuple[int, int], ...],
    index: dict[tuple[int, int], int],
) -> None:
    quotient = quotient_monomial(
        tuple(sorted((left_cell, right_cell))), support, cells, index
    )
    if quotient is None:
        return
    key, sign = quotient
    product = multiply_polynomials(left, right)
    polynomial = column.setdefault(key, {})
    for monomial, coefficient in product.items():
        add_polynomial_term(polynomial, monomial, sign * coefficient)


def corner_defect_certificate(
    name: str, support_cells: set[tuple[int, int]]
) -> dict[str, object]:
    cells = canonical_biflag_cells()
    index = {cell: position for position, cell in enumerate(cells)}
    support = frozenset(index[cell] for cell in support_cells)
    selected_rows = sorted({row for row, _ in support_cells})
    selected_columns = sorted({column for _, column in support_cells})
    missing_row = next(row for row in range(4) if row not in selected_rows)
    missing_column = next(column for column in range(5) if column not in selected_columns)
    quadrics = tuple(
        quadric
        for quadric in rectangle_quadrics(cells)
        if frozenset(quadric[0] + quadric[1]) <= support
    )

    # Variable order: a_0,...,a_2,b_0,...,b_3,d_00,...,d_23,
    # followed, when present, by twelve tail variables.
    a_variables = tuple(range(3))
    b_variables = tuple(range(3, 7))
    d_variables = tuple(range(7, 19))
    tail_target = index.get((4, missing_column))
    tail_variables = tuple(range(19, 31)) if tail_target is not None else ()

    vectors: dict[int, dict[int, Polynomial]] = {}
    for row_position, row in enumerate(selected_rows):
        for column_position, column in enumerate(selected_columns):
            source = index[row, column]
            vectors[source] = {
                source: {(): 1},
                index[missing_row, column]: {(a_variables[row_position],): 1},
                index[row, missing_column]: {(b_variables[column_position],): 1},
                index[missing_row, missing_column]: {
                    tuple(sorted((a_variables[row_position], b_variables[column_position]))): 1,
                    (d_variables[4 * row_position + column_position],): 1,
                },
            }
            if tail_target is not None:
                vectors[source][tail_target] = {
                    (tail_variables[4 * row_position + column_position],): 1
                }

    columns = []
    for quadric in quadrics:
        column: dict[tuple[int, int], Polynomial] = {}
        for source_pair in quadric:
            first, second = source_pair
            for first_cell, first_polynomial in vectors[first].items():
                for second_cell, second_polynomial in vectors[second].items():
                    add_vector_product(
                        column,
                        first_cell,
                        first_polynomial,
                        second_cell,
                        second_polynomial,
                        support,
                        cells,
                        index,
                    )
        columns.append({key: polynomial for key, polynomial in column.items() if polynomial})

    all_keys = set().union(*(set(column) for column in columns))
    pure_defect_keys = []
    pure_tail_keys = []
    for key in sorted(all_keys):
        polynomials = [column.get(key, {}) for column in columns]
        monomials = set().union(*(set(polynomial) for polynomial in polynomials))
        if monomials and all(
            len(monomial) == 1 and monomial[0] in d_variables for monomial in monomials
        ):
            pure_defect_keys.append(key)
        if monomials and tail_variables and all(
            len(monomial) == 1 and monomial[0] in tail_variables
            for monomial in monomials
        ):
            pure_tail_keys.append(key)

    coordinate_ranks = []
    for defect in d_variables:
        matrix = []
        for key in pure_defect_keys:
            matrix.append(
                tuple(column.get(key, {}).get((defect,), 0) for column in columns)
            )
        coordinate_ranks.append(rational_rank(matrix))
    assert len(pure_defect_keys) == 12
    assert coordinate_ranks == [6] * 12
    tail_coordinate_ranks = []
    for tail in tail_variables:
        matrix = []
        for key in pure_tail_keys:
            matrix.append(
                tuple(column.get(key, {}).get((tail,), 0) for column in columns)
            )
        tail_coordinate_ranks.append(rational_rank(matrix))
    if tail_variables:
        assert len(pure_tail_keys) == 12
        assert tail_coordinate_ranks == [6] * 12
    else:
        assert not pure_tail_keys and not tail_coordinate_ranks
    return {
        "name": name,
        "factor_parameter_count": 7,
        "corner_parameter_count": 12,
        "tail_parameter_count": len(tail_variables),
        "pure_tail_quotient_weight_count": len(pure_tail_keys),
        "coordinate_tail_ranks_over_Q": tail_coordinate_ranks,
        "pure_corner_defect_quotient_weight_count": len(pure_defect_keys),
        "coordinate_corner_defect_ranks_over_Q": coordinate_ranks,
        "minimum_fixed_weight_rank": min(coordinate_ranks),
        "rank_allowed_by_a_thirteen_plane": 5,
        "conclusion": (
            "Every rank-at-most-five leakage point has zero tail parameters and "
            "gamma=a tensor b."
        ),
    }


def orbit_representatives() -> tuple[tuple[str, set[tuple[int, int]]], ...]:
    return (
        (
            "3x4_missing_core_column",
            {(row, column) for row in (0, 1, 2) for column in (1, 2, 3, 4)},
        ),
        (
            "3x4_missing_wing_column",
            {(row, column) for row in (0, 1, 2) for column in (0, 1, 2, 4)},
        ),
    )


def build_payload() -> dict[str, object]:
    linear = [linear_only_certificate(name, support) for name, support in orbit_representatives()]
    corner = [corner_defect_certificate(name, support) for name, support in orbit_representatives()]
    by_name = {row["name"]: row for row in linear}
    assert by_name["3x4_missing_wing_column"]["minimum_rank_outside_kernel"] == 6
    assert by_name["3x4_missing_core_column"]["minimum_rank_outside_kernel"] == 6
    assert by_name["3x4_missing_core_column"]["tail_parameter_count"] == 12
    assert by_name["3x4_missing_wing_column"]["tail_parameter_count"] == 0
    return {
        "status": [
            "EXACT_QQ_BIFLAG_3X4_GRAPH_REDUCTION",
            "PURE_3X4_THRESHOLD13_PRODUCT_DIMENSION_GATE",
            "CERTIFIED_BIFLAG_3X4_ACTUAL_PAIR_EXCLUDED",
            "N6-106",
        ],
        "ambient": {
            "biflag": "M=R4 tensor C5 + R5 tensor C3",
            "intrinsic_quadratic_space": "K=E2 intersect Sym^2(M)",
            "dimension_of_K": 72,
            "coordinate_3x4_orbit_count": 2,
        },
        "linear_only_graph_reduction": {
            "orbit_certificates": linear,
            "kernel_normal_form": (
                "row factor a tensor I_B, column factor I_A tensor b, an arbitrary "
                "twelve-coordinate corner gamma, and on the missing-core-column orbit "
                "twelve additional tail coordinates"
            ),
            "rank_allowed_by_retaining_13_of_18_rectangles": 5,
        },
        "tail_and_corner_defect_reduction": {
            "orbit_certificates": corner,
            "defect": "d=gamma-a tensor b",
            "minimum_fixed_weight_rank": 6,
            "conclusion": (
                "On both 3x4 charts, all tail parameters and d vanish, so the twelve-plane "
                "is an exact tensor product A3' tensor B4'."
            ),
        },
        "product_dimension_gate": {
            "row_parameter_support_at_most_one": {
                "row_quadratic_dimension": 3,
                "column_quadratic_dimension": [5, 6],
                "intersection_dimensions": [15, 18],
            },
            "row_parameter_support_at_least_two": {
                "row_quadratic_dimension": 2,
                "column_quadratic_dimension": [5, 6],
                "intersection_dimensions": [10, 12],
            },
            "conclusion": (
                "Intersection dimension at least 13 holds exactly when the missing-row "
                "functional uses at most one selected coordinate."
            ),
        },
        "actual_pair_consequence": (
            "Every graph-chart U with intersection dimension at least 13 is a product. "
            "N6-068 excludes an actual complementary Chow pair when its full "
            "fifteen-dimensional section-difference space is present."
        ),
        "remaining_geometric_interface": (
            "The four 4x3 endpoint orbits remain, although the core orbit was excluded "
            "purely in N6-105."
        ),
        "claim_boundary": (
            "The linear calculations are deterministic characteristic-zero certificates "
            "over Q, and the final product dimension gate is pure. This note does not "
            "exclude every 4x3 endpoint, the full biflag branch, prove ordinary lower 29, "
            "determine exact Chow rank 32, or make a border-rank claim."
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
