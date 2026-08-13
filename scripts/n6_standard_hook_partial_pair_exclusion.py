#!/usr/bin/env python3
"""Exact replay for the N6-109 standard-hook partial-pair exclusion."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_standard_hook_partial_pair_exclusion.json"
CELLS = tuple(
    [(row, column) for row in range(3) for column in range(6)]
    + [(3, column) for column in range(5)]
)
CELL_INDEX = {cell: index for index, cell in enumerate(CELLS)}
EDGES6 = tuple(combinations(range(6), 2))

REPRESENTATIVES = {
    "K26": {(row, column) for row in (0, 1) for column in range(6)},
    "K34_core_columns": {
        (row, column) for row in (0, 1, 2) for column in (0, 1, 2, 3)
    },
    "K34_with_sixth_column": {
        (row, column) for row in (0, 1, 2) for column in (0, 1, 2, 5)
    },
    "K34_with_fourth_row": {
        (row, column) for row in (0, 1, 3) for column in (0, 1, 2, 3)
    },
    "K43": {
        (row, column) for row in (0, 1, 2, 3) for column in (0, 1, 2)
    },
}

EXPECTED_PRODUCT_TANGENT_DIMENSIONS = {
    "K26": 2,
    "K34_core_columns": 11,
    "K34_with_sixth_column": 8,
    "K34_with_fourth_row": 7,
    "K43": 6,
}


def require(condition: bool, payload: object) -> None:
    if not condition:
        raise AssertionError(payload)


def rational_rank(rows: list[tuple[int, ...]] | list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column]), None
        )
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
                for value, pivot_value in zip(matrix[row], matrix[rank], strict=True)
            ]
        rank += 1
    return rank


def minimum_nonzero_support(rows: list[tuple[int, ...]]) -> tuple[int, int]:
    full_rank = rational_rank(rows)
    require(full_rank > 0, rows)
    for zero_count in range(len(rows), -1, -1):
        for zero_rows in combinations(range(len(rows)), zero_count):
            if rational_rank([rows[index] for index in zero_rows]) < full_rank:
                return len(rows) - zero_count, len(rows[0]) - full_rank
    raise AssertionError(rows)


def rectangle_quadrics() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    quadrics = []
    for rows in combinations(range(4), 2):
        for columns in combinations(range(6), 2):
            corners = {(row, column) for row in rows for column in columns}
            if corners <= CELL_INDEX.keys():
                first_row, second_row = rows
                first_column, second_column = columns
                quadrics.append(
                    (
                        tuple(
                            sorted(
                                (
                                    CELL_INDEX[first_row, first_column],
                                    CELL_INDEX[second_row, second_column],
                                )
                            )
                        ),
                        tuple(
                            sorted(
                                (
                                    CELL_INDEX[first_row, second_column],
                                    CELL_INDEX[second_row, first_column],
                                )
                            )
                        ),
                    )
                )
    return tuple(quadrics)


QUADRICS = rectangle_quadrics()


def quotient_monomial(
    monomial: tuple[int, int], support: frozenset[int]
) -> tuple[tuple[int, int], int] | None:
    if monomial[0] in support and monomial[1] in support:
        return None
    left, right = monomial
    left_row, left_column = CELLS[left]
    right_row, right_column = CELLS[right]
    if left_row == right_row or left_column == right_column:
        return monomial, 1
    opposite_cells = ((left_row, right_column), (right_row, left_column))
    if opposite_cells[0] not in CELL_INDEX or opposite_cells[1] not in CELL_INDEX:
        return monomial, 1
    opposite = tuple(
        sorted((CELL_INDEX[opposite_cells[0]], CELL_INDEX[opposite_cells[1]]))
    )
    if opposite[0] in support and opposite[1] in support:
        return None
    if opposite < monomial:
        return opposite, -1
    return monomial, 1


def tangent_weight(
    source: tuple[int, int], target: tuple[int, int]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (
        tuple(int(index == target[0]) - int(index == source[0]) for index in range(4)),
        tuple(int(index == target[1]) - int(index == source[1]) for index in range(6)),
    )


def coordinate_threshold_enumeration() -> dict[str, object]:
    histogram: Counter[int] = Counter()
    profiles: Counter[tuple[int, tuple[int, ...]]] = Counter()
    for support in combinations(range(len(CELLS)), 12):
        row_masks = [0] * 4
        for position in support:
            row, column = CELLS[position]
            row_masks[row] |= 1 << column
        rectangle_count = 0
        for first, second in combinations(range(4), 2):
            common = (row_masks[first] & row_masks[second]).bit_count()
            rectangle_count += common * (common - 1) // 2
        histogram[rectangle_count] += 1
        if rectangle_count >= 13:
            profile = tuple(
                sorted((mask.bit_count() for mask in row_masks), reverse=True)
            )
            profiles[rectangle_count, profile] += 1
    require(sum(profiles.values()) == 43, profiles)
    require(not any(histogram[value] for value in (13, 14, 16, 17)), histogram)
    return {
        "coordinate_twelve_plane_count": sum(histogram.values()),
        "histogram_from_ten_up": {
            str(value): histogram[value] for value in sorted(histogram) if value >= 10
        },
        "threshold_thirteen_fixed_point_count": sum(profiles.values()),
        "fixed_profiles": [
            {
                "intersection_dimension": dimension,
                "row_degree_profile": list(profile),
                "count": count,
            }
            for (dimension, profile), count in sorted(profiles.items())
        ],
        "no_coordinate_values_thirteen_fourteen_sixteen_seventeen": True,
    }


def graph_linear_expansion(
    support_cells: set[tuple[int, int]],
) -> tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    tuple[dict[tuple[int, int], tuple[int, ...]], ...],
]:
    support = frozenset(CELL_INDEX[cell] for cell in support_cells)
    outside = tuple(index for index in range(len(CELLS)) if index not in support)
    variables = tuple((source, target) for source in sorted(support) for target in outside)
    variable_index = {variable: index for index, variable in enumerate(variables)}
    quadrics = tuple(
        quadric
        for quadric in QUADRICS
        if frozenset(quadric[0] + quadric[1]) <= support
    )
    columns = []
    for quadric in quadrics:
        column: dict[tuple[int, int], list[int]] = defaultdict(
            lambda: [0] * len(variables)
        )
        for source_pair in quadric:
            first, second = source_pair
            for source, other in ((first, second), (second, first)):
                for target in outside:
                    quotient = quotient_monomial(
                        tuple(sorted((target, other))), support
                    )
                    if quotient is None:
                        continue
                    key, sign = quotient
                    column[key][variable_index[source, target]] += sign
        columns.append(
            {key: tuple(row) for key, row in column.items() if any(row)}
        )
    return variables, quadrics, tuple(columns)


def product_tangent_vectors(
    name: str, variables: tuple[tuple[int, int], ...]
) -> list[tuple[int, ...]]:
    lookup = {variable: index for index, variable in enumerate(variables)}
    support = REPRESENTATIVES[name]
    answer = []

    def add_axis(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> None:
        vector = [0] * len(variables)
        for source, target in pairs:
            vector[lookup[CELL_INDEX[source], CELL_INDEX[target]]] = 1
        answer.append(tuple(vector))

    if name == "K26":
        for source_row in (0, 1):
            add_axis([
                ((source_row, column), (2, column)) for column in range(6)
            ])
    elif name == "K34_core_columns":
        for source_row in (0, 1, 2):
            add_axis([
                ((source_row, column), (3, column)) for column in (0, 1, 2, 3)
            ])
        for source_column in (0, 1, 2, 3):
            for target_column in (4, 5):
                add_axis([
                    ((row, source_column), (row, target_column))
                    for row in (0, 1, 2)
                ])
    elif name == "K34_with_sixth_column":
        for source_column in (0, 1, 2, 5):
            for target_column in (3, 4):
                add_axis([
                    ((row, source_column), (row, target_column))
                    for row in (0, 1, 2)
                ])
    elif name == "K34_with_fourth_row":
        for source_row in (0, 1, 3):
            add_axis([
                ((source_row, column), (2, column)) for column in (0, 1, 2, 3)
            ])
        for source_column in (0, 1, 2, 3):
            add_axis([
                ((row, source_column), (row, 4)) for row in (0, 1, 3)
            ])
    elif name == "K43":
        for source_column in (0, 1, 2):
            for target_column in (3, 4):
                add_axis([
                    ((row, source_column), (row, target_column))
                    for row in (0, 1, 2, 3)
                ])
    else:
        raise AssertionError(name)
    require(len(answer) == EXPECTED_PRODUCT_TANGENT_DIMENSIONS[name], (name, answer))
    return answer


def local_leakage_certificate(
    name: str, support_cells: set[tuple[int, int]]
) -> dict[str, object]:
    variables, quadrics, columns = graph_linear_expansion(support_cells)
    coefficient_rows = [
        row for column in columns for row in column.values() if any(row)
    ]
    linear_rank = rational_rank(coefficient_rows)
    product_vectors = product_tangent_vectors(name, variables)
    require(rational_rank(product_vectors) == len(product_vectors), name)
    require(
        all(
            sum(row[index] * vector[index] for index in range(len(variables))) == 0
            for row in coefficient_rows
            for vector in product_vectors
        ),
        name,
    )
    require(linear_rank == len(variables) - len(product_vectors), name)

    groups: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = defaultdict(list)
    for variable, (source, target) in enumerate(variables):
        groups[tangent_weight(CELLS[source], CELLS[target])].append(variable)
    signatures = []
    for members in groups.values():
        rows = []
        for column in columns:
            nonzero = []
            for row in column.values():
                restriction = tuple(row[index] for index in members)
                if any(restriction):
                    nonzero.append(restriction)
            require(len(nonzero) <= 1, (name, members, nonzero))
            rows.extend(nonzero)
        if rows:
            minimum, kernel_dimension = minimum_nonzero_support(rows)
        else:
            minimum, kernel_dimension = 0, len(members)
        signatures.append((len(members), len(rows), kernel_dimension, minimum))
    require(
        sum(signature[2] for signature in signatures) == len(product_vectors),
        (name, signatures),
    )
    minimum_rank = min(signature[3] for signature in signatures if signature[3])
    allowed_loss = len(quadrics) - 13
    require(minimum_rank > allowed_loss, (name, minimum_rank, allowed_loss))
    return {
        "name": name,
        "graph_variables": len(variables),
        "base_intersection_dimension": len(quadrics),
        "allowed_leakage_at_threshold_thirteen": allowed_loss,
        "exact_QQ_linear_rank": linear_rank,
        "kernel_dimension": len(product_vectors),
        "kernel_equals_product_tangent": True,
        "minimum_nonproduct_fixed_weight_leakage_rank": minimum_rank,
        "weight_group_signature_histogram": [
            {
                "variable_count": signature[0],
                "output_weight_count": signature[1],
                "kernel_dimension": signature[2],
                "minimum_rank_outside_kernel": signature[3],
                "group_count": count,
            }
            for signature, count in sorted(Counter(signatures).items())
        ],
    }


Polynomial = dict[tuple[int, ...], int]


def add_term(polynomial: Polynomial, monomial: tuple[int, ...], coefficient: int) -> None:
    value = polynomial.get(monomial, 0) + coefficient
    if value:
        polynomial[monomial] = value
    else:
        polynomial.pop(monomial, None)


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            add_term(
                answer,
                tuple(sorted(left_monomial + right_monomial)),
                left_coefficient * right_coefficient,
            )
    return answer


def add_vector_product(
    column: dict[tuple[int, int], Polynomial],
    left_cell: int,
    left: Polynomial,
    right_cell: int,
    right: Polynomial,
    support: frozenset[int],
) -> None:
    quotient = quotient_monomial(tuple(sorted((left_cell, right_cell))), support)
    if quotient is None:
        return
    key, sign = quotient
    product = multiply_polynomials(left, right)
    polynomial = column.setdefault(key, {})
    for monomial, coefficient in product.items():
        add_term(polynomial, monomial, sign * coefficient)


def corner_defect_certificate(name: str) -> dict[str, object]:
    if name == "K34_core_columns":
        selected_rows = (0, 1, 2)
        missing_row = 3
        selected_columns = (0, 1, 2, 3)
        compatible_targets = (4,)
        incompatible_targets = (5,)
    elif name == "K34_with_fourth_row":
        selected_rows = (0, 1, 3)
        missing_row = 2
        selected_columns = (0, 1, 2, 3)
        compatible_targets = (4,)
        incompatible_targets = ()
    else:
        raise AssertionError(name)
    support_cells = REPRESENTATIVES[name]
    support = frozenset(CELL_INDEX[cell] for cell in support_cells)
    quadrics = tuple(
        quadric
        for quadric in QUADRICS
        if frozenset(quadric[0] + quadric[1]) <= support
    )
    a_variables = tuple(range(3))
    next_variable = 3
    b_variables = {}
    for target in compatible_targets + incompatible_targets:
        for column_position, source_column in enumerate(selected_columns):
            b_variables[target, source_column] = next_variable
            next_variable += 1
    defect_variables = {}
    for target in compatible_targets:
        for row_position, source_row in enumerate(selected_rows):
            for column_position, source_column in enumerate(selected_columns):
                defect_variables[target, source_row, source_column] = next_variable
                next_variable += 1

    vectors: dict[int, dict[int, Polynomial]] = {}
    for row_position, row in enumerate(selected_rows):
        for column_position, column in enumerate(selected_columns):
            source = CELL_INDEX[row, column]
            vector: dict[int, Polynomial] = {
                source: {(): 1},
                CELL_INDEX[missing_row, column]: {(a_variables[row_position],): 1},
            }
            for target in compatible_targets + incompatible_targets:
                b_variable = b_variables[target, column]
                vector[CELL_INDEX[row, target]] = {(b_variable,): 1}
                corner = (missing_row, target)
                if target in compatible_targets:
                    defect = defect_variables[target, row, column]
                    vector[CELL_INDEX[corner]] = {
                        tuple(sorted((a_variables[row_position], b_variable))): 1,
                        (defect,): 1,
                    }
                else:
                    require(corner not in CELL_INDEX, (name, corner))
            vectors[source] = vector

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
                    )
        columns.append({key: value for key, value in column.items() if value})

    all_keys = sorted(set().union(*(set(column) for column in columns)))
    defect_monomials = {(variable,) for variable in defect_variables.values()}
    incompatible_monomials = {
        tuple(sorted((a_variables[row_position], b_variables[target, column])))
        for target in incompatible_targets
        for row_position in range(3)
        for column in selected_columns
    }
    pure_defect_keys = []
    pure_incompatible_keys = []
    for key in all_keys:
        monomials = set().union(
            *(set(column.get(key, {})) for column in columns)
        )
        if monomials and monomials <= defect_monomials:
            pure_defect_keys.append(key)
        if monomials and monomials <= incompatible_monomials:
            pure_incompatible_keys.append(key)

    defect_ranks = []
    for defect in defect_variables.values():
        rows = []
        for key in pure_defect_keys:
            row = tuple(column.get(key, {}).get((defect,), 0) for column in columns)
            if any(row):
                rows.append(row)
        defect_ranks.append(rational_rank(rows))
    incompatible_ranks = []
    for target in incompatible_targets:
        for row_position, row in enumerate(selected_rows):
            for column in selected_columns:
                monomial = tuple(
                    sorted((a_variables[row_position], b_variables[target, column]))
                )
                rows = []
                for key in pure_incompatible_keys:
                    output = tuple(
                        item.get(key, {}).get(monomial, 0) for item in columns
                    )
                    if any(output):
                        rows.append(output)
                incompatible_ranks.append(rational_rank(rows))
    require(defect_ranks == [6] * len(defect_variables), (name, defect_ranks))
    require(
        incompatible_ranks == [6] * (3 * 4 * len(incompatible_targets)),
        (name, incompatible_ranks),
    )
    return {
        "name": name,
        "compatible_corner_defects": len(defect_variables),
        "pure_compatible_defect_weights": len(pure_defect_keys),
        "compatible_corner_defect_ranks": defect_ranks,
        "missing_corner_products": len(incompatible_ranks),
        "pure_missing_corner_product_weights": len(pure_incompatible_keys),
        "missing_corner_product_ranks": incompatible_ranks,
        "allowed_leakage": 5,
        "conclusion": (
            "Every compatible corner equals a tensor b, and every missing-corner "
            "product a tensor b vanishes."
        ),
    }


def matrix_multiplier_rank(matrix: list[list[int]]) -> int:
    columns = []
    for first, second in EDGES6:
        symmetric = [[0] * 6 for _ in range(6)]
        symmetric[first][second] = symmetric[second][first] = 1
        product = [
            [sum(matrix[row][k] * symmetric[k][column] for k in range(6))
             for column in range(6)]
            for row in range(6)
        ]
        columns.append(
            [product[index][index] for index in range(6)]
            + [
                product[i][j] - product[j][i]
                for i, j in EDGES6
            ]
        )
    return rational_rank([list(column) for column in zip(*columns)])


def partial_two_row_lemmas() -> dict[str, object]:
    off_diagonal_ranks = []
    for row in range(6):
        for column in range(6):
            if row == column:
                continue
            matrix = [[0] * 6 for _ in range(6)]
            matrix[row][column] = 1
            off_diagonal_ranks.append(matrix_multiplier_rank(matrix))
    require(set(off_diagonal_ranks) == {5}, off_diagonal_ranks)

    diagonal_fixed_minimum = min(
        sum(left != right for left, right in EDGES6 if values[left] != values[right])
        for values in (
            tuple(int(index in support) for index in range(6))
            for size in range(1, 6)
            for support in combinations(range(6), size)
        )
    )
    require(diagonal_fixed_minimum == 5, diagonal_fixed_minimum)

    perfect_matchings = [
        frozenset((tuple(sorted(pair)) for pair in matching))
        for matching in (
            ((a, b), (c, d), (e, f))
            for a, b in combinations(range(6), 2)
            for c, d in combinations([x for x in range(6) if x not in (a, b)], 2)
            for e, f in [tuple(x for x in range(6) if x not in (a, b, c, d))]
        )
    ]
    perfect_matchings = sorted(set(perfect_matchings), key=sorted)
    require(len(perfect_matchings) == 15, len(perfect_matchings))
    coordinate_q13 = []
    for edges in combinations(EDGES6, 13):
        edge_set = frozenset(edges)
        coordinate_q13.append(sum(matching <= edge_set for matching in perfect_matchings))
    require(min(coordinate_q13) > 0, min(coordinate_q13))

    invariant_maxima = {}
    for dimension in range(1, 6):
        maximum = 0
        for image_support in combinations(range(6), dimension):
            image = set(image_support)
            for source_support in combinations(range(6), dimension):
                source = set(source_support)
                allowed = sum(
                    (first not in source or second in image)
                    and (second not in source or first in image)
                    for first, second in EDGES6
                )
                maximum = max(maximum, allowed)
        invariant_maxima[str(dimension)] = maximum
    require(max(invariant_maxima.values()) == 12, invariant_maxima)
    return {
        "multiplier_projective_fixed_ranks": {
            "minimum_non_scalar_diagonal_rank": diagonal_fixed_minimum,
            "off_diagonal_matrix_unit_rank_set": sorted(set(off_diagonal_ranks)),
            "rank_allowed_by_a_thirteen_plane": 2,
            "conclusion": "XQ subset S0 and dim Q at least 13 force X scalar",
        },
        "invertible_member": {
            "coordinate_thirteen_planes": len(coordinate_q13),
            "perfect_matchings_of_K6": len(perfect_matchings),
            "minimum_matching_count_after_deleting_two_edges": min(coordinate_q13),
            "conclusion": "every thirteen-plane in S0 contains an invertible member",
        },
        "ratio_algebra": {
            "coordinate_invariant_pair_maxima_by_dimension": invariant_maxima,
            "maximum": max(invariant_maxima.values()),
            "required_Q_dimension": 13,
            "conclusion": "Alg(Q B0^-1)=End(k^6)",
        },
        "partial_transverse_theorem": (
            "If D subset E26 has dimension at least 13, shadow dimension 12, "
            "and full projection to two rows, then U=P2 tensor k6; for an actual "
            "complementary block pair, L=p tensor k6 and M=q tensor k6."
        ),
    }


def build_payload() -> dict[str, object]:
    coordinate = coordinate_threshold_enumeration()
    local = [
        local_leakage_certificate(name, support)
        for name, support in REPRESENTATIVES.items()
    ]
    require(
        [row["minimum_nonproduct_fixed_weight_leakage_rank"] for row in local]
        == [5, 6, 6, 6, 6],
        local,
    )
    partial = partial_two_row_lemmas()
    corner = [
        corner_defect_certificate("K34_core_columns"),
        corner_defect_certificate("K34_with_fourth_row"),
    ]
    return {
        "certificate": "N6-109",
        "status": "CERTIFIED_STANDARD_HOOK_PARTIAL_PAIR_EXCLUSION",
        "field": "algebraically closed, characteristic zero",
        "standard_hook": {
            "M": "R4 tensor C5 + R3 tensor C6",
            "dimension": 23,
            "intrinsic_quadratic_space": "K=E2 intersect Sym^2(M)",
            "dimension_of_K": 75,
        },
        "coordinate_threshold_thirteen": coordinate,
        "relative_normal_leakage_certificates": local,
        "nonlinear_product_corner_certificates": corner,
        "pure_product_globalization": {
            "statement": (
                "Every U in Gr(12,M) with dim(K intersect Sym2 U)>=13 is a "
                "product of type 2x6, 3x4, or 4x3."
            ),
            "method": "projective torus components and relative normal cones",
            "product_dimension_gate": {
                "2x6": [15],
                "3x4": [15, 18],
                "4x3": [15, 18],
            },
        },
        "partial_two_row_rigidity": partial,
        "a2_72_standard_hook_application": {
            "newly_excluded_kappa2_values": [1, 2],
            "complementary_relation_graph_connected": True,
            "K34_K43_edges_excluded_by": "N6-108",
            "K26_edge_consequence": "both endpoint factor planes are complete row slices",
            "final_contradiction": (
                "Connectivity makes all six factor planes complete row slices, so "
                "their sum has dimension divisible by 6, not 23."
            ),
        },
        "remaining_frontier": {
            "a2_72": ["kappa2=0 standard hook", "kappa2=0 biflag"],
            "higher_a2": [73, 74, 75],
        },
        "claim_boundary": (
            "This closes the a2=72, kappa2=1,2 standard-hook branches only. "
            "The kappa2=0 standard and biflag branches and all a2=73,74,75 "
            "states remain open; this is not ordinary lower 29, exact "
            "ChowRank(perm_6)=32, or a border-rank theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    if arguments.json:
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    if arguments.verify_json:
        frozen = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        require(payload == frozen, "frozen payload mismatch")
    if not arguments.json and not arguments.verify_json:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
