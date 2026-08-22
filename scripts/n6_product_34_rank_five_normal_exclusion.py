#!/usr/bin/env python3
"""Exact N6-114 exclusion of the rank-five 3 x 4 product strata.

The only enumerations are projective coefficient scans in torus weight spaces
of dimension at most eight.  They are streamed and retain no growing state.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_34_rank_five_normal_exclusion.json"
BASE_PATH = ROOT / "scripts" / "n6_product_34_partial_pair_exclusion.py"
FIXED_PATH = ROOT / "scripts" / "n6_product_34_rank_six_fixed_reduction.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


BASE = load_module("n6_product_34_partial", BASE_PATH)
FIXED = load_module("n6_product_34_fixed", FIXED_PATH)
PRIME = BASE.PRIME


def torus_weight(variable: tuple[str, int, int]) -> tuple[int, ...]:
    _, target, source = variable
    answer = [0] * 7
    answer[target // 4] += 1
    answer[source // 4] -= 1
    answer[3 + target % 4] += 1
    answer[3 + source % 4] -= 1
    return tuple(answer)


def all_exact_leading_matrices(
    name: str,
) -> tuple[list[tuple[str, int, int]], dict[int, list[list[int]]]]:
    left, right = BASE.REPRESENTATIVES[name]
    variables, _, derivatives = BASE.tangent_equations(left, right)
    base = BASE.cross_matrix(left, right)
    right_kernel = BASE.integer_nullspace(base)
    left_kernel = BASE.integer_nullspace([list(column) for column in zip(*base)])
    matrices = {}
    for index, variable in enumerate(variables):
        if variable[1] < 8:
            continue
        derivative = derivatives[index]
        matrices[index] = (
            [
                [
                    sum(
                        left_kernel[row][i]
                        * derivative[i][j]
                        * right_kernel[column][j]
                        for i in range(36)
                        for j in range(18)
                    )
                    for column in range(len(right_kernel))
                ]
                for row in range(len(left_kernel))
            ]
        )
    return variables, matrices


def add_fraction_row(
    row: list[int], basis: list[tuple[int, list[Fraction]]]
) -> None:
    reduced = [Fraction(entry) for entry in row]
    for pivot, current in basis:
        if reduced[pivot]:
            coefficient = reduced[pivot]
            reduced = [
                left - coefficient * right
                for left, right in zip(reduced, current, strict=True)
            ]
    pivot = next((index for index, entry in enumerate(reduced) if entry), None)
    if pivot is None:
        return
    coefficient = reduced[pivot]
    reduced = [entry / coefficient for entry in reduced]
    updated = []
    for old_pivot, current in basis:
        if current[pivot]:
            coefficient = current[pivot]
            current = [
                left - coefficient * right
                for left, right in zip(current, reduced, strict=True)
            ]
        updated.append((old_pivot, current))
    updated.append((pivot, reduced))
    updated.sort()
    basis[:] = updated


def quadratic_minor_span(
    matrices: list[list[list[int]]],
) -> list[list[int]]:
    dimension = len(matrices)
    monomials = [(i, j) for i in range(dimension) for j in range(i, dimension)]
    position = {monomial: index for index, monomial in enumerate(monomials)}
    basis: list[tuple[int, list[Fraction]]] = []
    rows = len(matrices[0])
    columns = len(matrices[0][0])
    for row1 in range(rows):
        for row2 in range(row1 + 1, rows):
            for column1 in range(columns):
                for column2 in range(column1 + 1, columns):
                    answer = [0] * len(monomials)
                    for sign, first, second in (
                        (1, (row1, column1), (row2, column2)),
                        (-1, (row1, column2), (row2, column1)),
                    ):
                        for i in range(dimension):
                            left = matrices[i][first[0]][first[1]]
                            if not left:
                                continue
                            for j in range(dimension):
                                right = matrices[j][second[0]][second[1]]
                                if right:
                                    answer[position[tuple(sorted((i, j)))]] += (
                                        sign * left * right
                                    )
                    if any(answer):
                        add_fraction_row(answer, basis)
    assert all(entry.denominator == 1 for _, row in basis for entry in row)
    return [[int(entry) for entry in row] for _, row in basis]


def square_monomials_in_span(equations: list[list[int]], dimension: int) -> list[bool]:
    monomials = [(i, j) for i in range(dimension) for j in range(i, dimension)]
    answer = []
    for index in range(dimension):
        basis = [
            (
                next(position for position, entry in enumerate(row) if entry),
                [Fraction(entry) for entry in row],
            )
            for row in equations
        ]
        old_dimension = len(basis)
        add_fraction_row(
            [int(monomial == (index, index)) for monomial in monomials], basis
        )
        answer.append(len(basis) == old_dimension)
    return answer


ROW42_WEIGHT = (0, -1, 1, 0, 0, 0, 0)
ROW33_WEIGHTS = ((-1, 0, 1, 0, 0, 0, 0), (0, -1, 1, 0, 0, 0, 0))


def expected_rank_one_rref(dimension: int) -> list[list[int]]:
    monomial_count = dimension * (dimension + 1) // 2
    if dimension == 4:
        trailing_positions = [9, 8, 9, 8, 9, 8, 9, 9]
        signs = [-1] * 8
    else:
        assert dimension == 6
        trailing_positions = [20] * 20
        signs = [
            -1, -1, -1, 1, 1, 1, -1, -1, 1, 1,
            1, -1, 1, 1, 1, -1, -1, -1, -1, -1,
        ]
    answer = []
    for pivot, (trailing, sign) in enumerate(zip(trailing_positions, signs)):
        row = [0] * monomial_count
        row[pivot] = 1
        row[trailing] = sign
        answer.append(row)
    return answer


def normal_weight_certificate(name: str) -> dict[str, object]:
    left, right = BASE.REPRESENTATIVES[name]
    variables, all_matrices = all_exact_leading_matrices(name)
    groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for index, variable in enumerate(variables):
        if variable[1] >= 8:
            groups[torus_weight(variable)].append(index)

    dimension_histogram: Counter[int] = Counter()
    excluded_by_square_certificate = 0
    surviving = []
    for weight, indices in sorted(groups.items()):
        group_variables = [variables[index] for index in indices]
        matrices = [all_matrices[index] for index in indices]
        dimension_histogram[len(indices)] += 1
        equations = quadratic_minor_span(matrices)
        square_membership = square_monomials_in_span(equations, len(indices))
        if all(square_membership):
            excluded_by_square_certificate += 1
            continue
        surviving.append(
            {
                "weight": list(weight),
                "variables": [list(variable) for variable in group_variables],
                "dimension": len(indices),
                "exact_quadratic_span_rank": len(equations),
                "exact_quadratic_rref": equations,
                "square_monomials_in_quadratic_span": square_membership,
            }
        )

    if name == "row_42_diagonal":
        assert len(surviving) == 1
        assert tuple(surviving[0]["weight"]) == ROW42_WEIGHT
        assert surviving[0]["dimension"] == 4
        assert surviving[0]["exact_quadratic_span_rank"] == 8
        assert surviving[0]["exact_quadratic_rref"] == expected_rank_one_rref(4)
        fixed_points = [[1, 1, 1, 1], [1, -1, 1, -1]]
    else:
        assert len(surviving) == 2
        assert {tuple(row["weight"]) for row in surviving} == set(ROW33_WEIGHTS)
        assert all(row["dimension"] == 6 for row in surviving)
        assert all(row["exact_quadratic_span_rank"] == 20 for row in surviving)
        assert all(
            row["exact_quadratic_rref"] == expected_rank_one_rref(6)
            for row in surviving
        )
        fixed_points = [[1, 1, 1, -1, -1, -1]] * 2

    return {
        "normal_weight_group_count": len(groups),
        "dimension_histogram": {str(k): v for k, v in sorted(dimension_histogram.items())},
        "groups_excluded_because_all_variable_squares_lie_in_the_exact_minor_span": (
            excluded_by_square_certificate
        ),
        "surviving_weight_groups": surviving,
        "characteristic_zero_fixed_points": fixed_points,
        "fixed_points_are_reduced_by_the_displayed_affine_chart_equations": True,
    }


def plane_columns(
    support: tuple[int, ...], moves: list[tuple[int, int, int]]
) -> list[list[int]]:
    columns = []
    for source in support:
        vector = [0] * 12
        vector[source] = 1
        for target, current_source, coefficient in moves:
            if source == current_source:
                vector[target] += coefficient
        columns.append(vector)
    return columns


def modular_nullspace(matrix: list[list[int]]) -> list[list[int]]:
    work = [[entry % PRIME for entry in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    row = 0
    pivots = []
    for column in range(columns):
        pivot = next(
            (index for index in range(row, rows) if work[index][column]), None
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, PRIME)
        work[row] = [(entry * inverse) % PRIME for entry in work[row]]
        for index in range(rows):
            if index != row and work[index][column]:
                coefficient = work[index][column]
                work[index] = [
                    (left - coefficient * right) % PRIME
                    for left, right in zip(work[index], work[row], strict=True)
                ]
        pivots.append(column)
        row += 1
        if row == rows:
            break
    free = [column for column in range(columns) if column not in pivots]
    answer = []
    for column in free:
        vector = [0] * columns
        vector[column] = 1
        for index, pivot in enumerate(pivots):
            vector[pivot] = -work[index][column] % PRIME
        answer.append(vector)
    return answer


def graph_data(
    left_support: tuple[int, ...],
    right_support: tuple[int, ...],
    left_moves: list[tuple[int, int, int]],
    right_moves: list[tuple[int, int, int]],
):
    left = plane_columns(left_support, left_moves)
    right = plane_columns(right_support, right_moves)
    base = [BASE.beta(left[i], right[j]) for i in range(6) for j in range(6)]
    right_kernel = BASE.integer_nullspace(base)
    left_kernel = BASE.integer_nullspace([list(column) for column in zip(*base)])
    assert len(right_kernel) == 12 and len(left_kernel) == 30
    variables = []
    derivatives = []
    for side, support, other in (
        ("L", left_support, right),
        ("M", right_support, left),
    ):
        for basis_index, source in enumerate(support):
            for target in range(12):
                if target in support:
                    continue
                rows = []
                for i in range(6):
                    for j in range(6):
                        if side == "L" and i == basis_index:
                            rows.append(BASE.beta(BASE.unit(target), other[j]))
                        elif side == "M" and j == basis_index:
                            rows.append(BASE.beta(other[i], BASE.unit(target)))
                        else:
                            rows.append([0] * 18)
                variables.append((side, target, source))
                derivatives.append(rows)
    equations = [
        [
            sum(
                left_vector[i] * derivative[i][j] * right_vector[j]
                for i in range(36)
                for j in range(18)
            )
            for derivative in derivatives
        ]
        for left_vector in left_kernel
        for right_vector in right_kernel
    ]
    return left, right, base, variables, derivatives, equations


def direction_vector(
    variables: list[tuple[str, int, int]],
    entries: list[tuple[str, int, int, int]],
) -> list[int]:
    lookup = {variable: index for index, variable in enumerate(variables)}
    answer = [0] * len(variables)
    for side, target, source, coefficient in entries:
        answer[lookup[side, target, source]] = coefficient
    return answer


def local_quadratic_certificate(
    left_support: tuple[int, ...],
    right_support: tuple[int, ...],
    left_moves: list[tuple[int, int, int]],
    right_moves: list[tuple[int, int, int]],
    directions: list[list[tuple[str, int, int, int]]],
) -> dict[str, object]:
    _, _, base, variables, derivatives, equations = graph_data(
        left_support, right_support, left_moves, right_moves
    )
    vectors = [direction_vector(variables, entries) for entries in directions]
    assert all(
        sum(row[index] * vector[index] for index in range(72)) == 0
        for row in equations
        for vector in vectors
    )
    assert BASE.rank_mod(vectors) == len(vectors)
    linear_rank = BASE.rank_mod(equations)
    assert linear_rank == 72 - len(vectors)

    matrix = np.array(base, dtype=np.int64) % PRIME
    _, pivot_columns = FIXED.modular_rref(matrix)
    _, pivot_rows = FIXED.modular_rref(matrix.T)
    pivot_columns = pivot_columns[:6]
    pivot_rows = pivot_rows[:6]
    other_rows = [index for index in range(36) if index not in pivot_rows]
    other_columns = [index for index in range(18) if index not in pivot_columns]
    pivot = matrix[np.ix_(pivot_rows, pivot_columns)]
    pivot_inverse = FIXED.modular_inverse(pivot)
    upper_right = matrix[np.ix_(pivot_rows, other_columns)]
    lower_left = matrix[np.ix_(other_rows, pivot_columns)]
    left_transform = np.zeros((36, 36), dtype=np.int64)
    left_transform[:6, pivot_rows] = pivot_inverse
    left_transform[6:, other_rows] = np.eye(30, dtype=np.int64)
    left_transform[6:, pivot_rows] = -lower_left @ pivot_inverse % PRIME
    right_transform = np.zeros((18, 18), dtype=np.int64)
    right_transform[np.ix_(pivot_columns, range(6))] = np.eye(6, dtype=np.int64)
    right_transform[np.ix_(other_columns, range(6, 18))] = np.eye(
        12, dtype=np.int64
    )
    right_transform[np.ix_(pivot_columns, range(6, 18))] = (
        -pivot_inverse @ upper_right % PRIME
    )

    def transform(current: np.ndarray) -> np.ndarray:
        return left_transform @ current @ right_transform % PRIME

    transformed_derivatives = [
        transform(np.array(derivative, dtype=np.int64) % PRIME)
        for derivative in derivatives
    ]
    linear = np.array(
        [current[6:, 6:].reshape(-1) for current in transformed_derivatives],
        dtype=np.int64,
    ).T % PRIME
    assert BASE.rank_mod(linear.tolist()) == linear_rank
    transformed_directions = [
        sum(
            (
                int(coefficient) * current
                for coefficient, current in zip(vector, transformed_derivatives)
            ),
            start=np.zeros((36, 18), dtype=np.int64),
        )
        % PRIME
        for vector in vectors
    ]

    def delta(
        vector: list[int], side: str, support: tuple[int, ...]
    ) -> np.ndarray:
        answer = np.zeros((12, 6), dtype=np.int64)
        for coefficient, (current_side, target, source) in zip(vector, variables):
            if current_side == side and coefficient:
                answer[target, support.index(source)] += coefficient
        return answer % PRIME

    left_deltas = [delta(vector, "L", left_support) for vector in vectors]
    right_deltas = [delta(vector, "M", right_support) for vector in vectors]

    def second(first: int, second_index: int) -> np.ndarray:
        return np.array(
            [
                BASE.beta(
                    left_deltas[first][:, i].tolist(),
                    right_deltas[second_index][:, j].tolist(),
                )
                for i in range(6)
                for j in range(6)
            ],
            dtype=np.int64,
        ) % PRIME

    monomials = []
    quadratic_columns = []
    for first in range(len(vectors)):
        for second_index in range(first, len(vectors)):
            current = second(first, second_index)
            if first != second_index:
                current = (current + second(second_index, first)) % PRIME
            lower = transform(current)[6:, 6:]
            lower -= (
                transformed_directions[first][6:, :6]
                @ transformed_directions[second_index][:6, 6:]
            )
            if first != second_index:
                lower -= (
                    transformed_directions[second_index][6:, :6]
                    @ transformed_directions[first][:6, 6:]
                )
            monomials.append((first, second_index))
            quadratic_columns.append(lower.reshape(-1) % PRIME)

    augmented = np.column_stack([linear, *quadratic_columns])
    augmented_difference = BASE.rank_mod(augmented.tolist()) - linear_rank
    individual_differences = {}
    for monomial, column in zip(monomials, quadratic_columns):
        individual_differences[str(monomial)] = (
            BASE.rank_mod(np.column_stack([linear, column]).tolist()) - linear_rank
        )
    assert augmented_difference == 1
    assert individual_differences[str((1, 2))] == 1
    assert sum(individual_differences.values()) == 1
    return {
        "linear_equation_shape": [len(equations), 72],
        "exact_QQ_linear_rank": linear_rank,
        "exact_tangent_dimension": len(vectors),
        "quadratic_monomials": [list(monomial) for monomial in monomials],
        "quadratic_cokernel_rank": augmented_difference,
        "individual_augmented_rank_differences": individual_differences,
        "unique_forbidden_monomial": [1, 2],
        "completed_local_ideal": "(x1*x2) after linear elimination",
    }


def one_dimensional_local_certificate(
    support: tuple[int, ...],
    moves: list[tuple[int, int, int]],
    direction: list[tuple[str, int, int, int]],
) -> dict[str, object]:
    _, _, _, variables, _, equations = graph_data(support, support, moves, moves)
    vector = direction_vector(variables, direction)
    assert all(
        sum(row[index] * vector[index] for index in range(72)) == 0
        for row in equations
    )
    assert BASE.rank_mod(equations) == 71
    return {
        "linear_equation_shape": [len(equations), 72],
        "exact_QQ_linear_rank": 71,
        "exact_tangent_dimension": 1,
        "completed_local_ring": "k[[s]]",
    }


ROW42_SUPPORT = BASE.REPRESENTATIVES["row_42_diagonal"][0]
ROW42_PLUS_MOVES = [(8, 4, 1), (9, 5, 1)]
ROW42_SCALE = [
    ("L", 8, 4, 1), ("L", 9, 5, 1),
    ("M", 8, 4, 1), ("M", 9, 5, 1),
]
ROW42_FIRST = [
    ("L", 8, 0, 1), ("L", 9, 1, 1), ("L", 6, 2, -1),
    ("L", 11, 3, 1), ("M", 8, 0, -1), ("M", 9, 1, -1),
    ("M", 10, 2, -1), ("M", 7, 3, 1),
]
ROW42_SECOND = [
    ("L", 8, 0, -1), ("L", 9, 1, -1), ("L", 10, 2, -1),
    ("L", 7, 3, 1), ("M", 8, 0, 1), ("M", 9, 1, 1),
    ("M", 6, 2, -1), ("M", 11, 3, 1),
]

ROW33_LEFT, ROW33_RIGHT = BASE.REPRESENTATIVES["row_33_intersection_4"]
ROW33_A_LEFT = [(8, 0, 1), (9, 1, 1), (10, 2, 1)]
ROW33_A_RIGHT = [(8, 0, -1), (9, 1, -1), (11, 3, -1)]
ROW33_SCALE = [
    ("L", 8, 0, 1), ("L", 9, 1, 1), ("L", 10, 2, 1),
    ("M", 8, 0, -1), ("M", 9, 1, -1), ("M", 11, 3, -1),
]
ROW33_EXTRA = [
    ("L", 8, 4, 1), ("L", 9, 5, 1), ("L", 3, 7, -1),
    ("M", 8, 4, 1), ("M", 9, 5, 1), ("M", 2, 6, 1),
]
ROW33_OTHER = [
    ("L", 8, 4, 1), ("L", 9, 5, 1), ("L", 11, 7, 1),
    ("M", 8, 4, -1), ("M", 9, 5, -1), ("M", 10, 6, -1),
]


def symbolic_family_ranks() -> dict[str, dict[str, int]]:
    s, c, a, b = sp.symbols("s c a b", nonzero=True)

    def vector(source: int, terms: list[tuple[int, sp.Expr]]) -> list[sp.Expr]:
        answer = [sp.Integer(0)] * 12
        answer[source] = 1
        for target, coefficient in terms:
            answer[target] += coefficient
        return answer

    def matrix(columns: list[list[sp.Expr]]) -> sp.Matrix:
        return sp.Matrix(12, 6, lambda i, j: columns[j][i])

    def ranks(left: sp.Matrix, right: sp.Matrix) -> dict[str, int]:
        cross_columns = [
            BASE.beta(list(left[:, i]), list(right[:, j]))
            for i in range(6)
            for j in range(6)
        ]
        cross = sp.Matrix(18, 36, lambda i, j: cross_columns[j][i])
        return {
            "generic_sum_rank": left.row_join(right).rank(),
            "generic_cross_rank": cross.rank(),
        }

    row42_minus = matrix(
        [
            vector(0, []), vector(1, []), vector(2, []), vector(3, []),
            vector(4, [(8, s)]), vector(5, [(9, -s)]),
        ]
    )
    row42_first_left = matrix(
        [
            vector(0, [(8, c * s)]), vector(1, [(9, c * s)]),
            vector(2, [(6, -c)]), vector(3, [(11, c * s)]),
            vector(4, [(8, s)]), vector(5, [(9, s)]),
        ]
    )
    row42_first_right = matrix(
        [
            vector(0, [(8, -c * s)]), vector(1, [(9, -c * s)]),
            vector(2, [(10, -c * s)]), vector(3, [(7, c)]),
            vector(4, [(8, s)]), vector(5, [(9, s)]),
        ]
    )
    row33_pencil_left = matrix(
        [
            vector(0, [(8, a)]), vector(1, [(9, a)]),
            vector(2, [(10, a)]), vector(4, [(8, b)]),
            vector(5, [(9, b)]), vector(7, [(11, b)]),
        ]
    )
    row33_pencil_right = matrix(
        [
            vector(0, [(8, -a)]), vector(1, [(9, -a)]),
            vector(3, [(11, -a)]), vector(4, [(8, -b)]),
            vector(5, [(9, -b)]), vector(6, [(10, -b)]),
        ]
    )
    row33_extra_left = matrix(
        [
            vector(0, [(8, a)]), vector(1, [(9, a)]),
            vector(2, [(10, a)]), vector(4, [(8, a * c)]),
            vector(5, [(9, a * c)]), vector(7, [(3, -c)]),
        ]
    )
    row33_extra_right = matrix(
        [
            vector(0, [(8, -a)]), vector(1, [(9, -a)]),
            vector(3, [(11, -a)]), vector(4, [(8, a * c)]),
            vector(5, [(9, a * c)]), vector(6, [(2, c)]),
        ]
    )
    answer = {
        "row42_reduced_point_curve": ranks(row42_minus, row42_minus),
        "row42_node_branch": ranks(row42_first_left, row42_first_right),
        "row33_projective_pencil": ranks(row33_pencil_left, row33_pencil_right),
        "row33_endpoint_extra_branch": ranks(row33_extra_left, row33_extra_right),
    }
    assert answer == {
        "row42_reduced_point_curve": {"generic_sum_rank": 6, "generic_cross_rank": 6},
        "row42_node_branch": {"generic_sum_rank": 10, "generic_cross_rank": 6},
        "row33_projective_pencil": {"generic_sum_rank": 10, "generic_cross_rank": 6},
        "row33_endpoint_extra_branch": {"generic_sum_rank": 10, "generic_cross_rank": 6},
    }
    return answer


def build_payload() -> dict[str, object]:
    row42_weights = normal_weight_certificate("row_42_diagonal")
    row33_weights = normal_weight_certificate("row_33_intersection_4")
    row42_plus = local_quadratic_certificate(
        ROW42_SUPPORT,
        ROW42_SUPPORT,
        ROW42_PLUS_MOVES,
        ROW42_PLUS_MOVES,
        [ROW42_SCALE, ROW42_FIRST, ROW42_SECOND],
    )
    row42_minus = one_dimensional_local_certificate(
        ROW42_SUPPORT,
        [(8, 4, 1), (9, 5, -1)],
        [
            ("L", 8, 4, -1), ("L", 9, 5, 1),
            ("M", 8, 4, -1), ("M", 9, 5, 1),
        ],
    )
    row33_endpoint = local_quadratic_certificate(
        ROW33_LEFT,
        ROW33_RIGHT,
        ROW33_A_LEFT,
        ROW33_A_RIGHT,
        [ROW33_SCALE, ROW33_EXTRA, ROW33_OTHER],
    )
    return {
        "certificate": "N6-114",
        "status": "CERTIFIED_CHARACTERISTIC_ZERO_PRODUCT_34_RANK_FIVE_EXCLUSION",
        "field": "characteristic zero",
        "bounded_replay": {
            "largest_weight_dimension": 8,
            "streaming_minor_elimination": True,
            "maximum_retained_quadratic_rows": 36,
            "unbounded_collections": False,
        },
        "rank_five_fixed_orbits": {
            "row_42_diagonal": row42_weights,
            "row_33_intersection_4": row33_weights,
        },
        "finite_exceptional_local_models": {
            "row_42_reduced_point": row42_minus,
            "row_42_node": row42_plus,
            "row_33_endpoint_node": row33_endpoint,
            "second_row_33_endpoint_follows_by_row_swap_and_L_M_swap": True,
        },
        "exact_symbolic_branch_ranks": symbolic_family_ranks(),
        "pure_formal_conclusion": {
            "normal_homogeneity": (
                "the third-row normal block is linear because E34 contains no "
                "same-row quadrics; row scaling identifies the strict-transform "
                "normal chart with the displayed finite representatives"
            ),
            "row_42": (
                "one fixed point is a smooth noncomplementary curve; the other "
                "has completed ideal (x1*x2), and both smooth branches "
                "have sum rank at most ten"
            ),
            "row_33": (
                "each endpoint has completed ideal (x1*x2); its pencil "
                "branch and extra branch both have sum rank ten"
            ),
            "globalization": (
                "every component of the projectivized relative normal cone has "
                "a torus fixed point, and every completed branch at such a point "
                "is noncomplementary"
            ),
            "statement": (
                "no complementary component of rank beta_E34 at most six can "
                "specialize to either rank-five coordinate orbit"
            ),
            "transpose": True,
        },
        "application": {
            "N6_113_remaining_fixed_ranks_before": [3, 5],
            "remaining_fixed_ranks_after_N6_114": [3],
            "next_open_stratum": "rank-three K23/K32 normal cones for rank at most six",
        },
        "claim_boundary": (
            "This closes only the rank-five fixed strata in the 3x4/4x3 "
            "twelve-plane product equality case. Rank-three fixed strata remain "
            "open, so this does not yet close kappa2=0, prove ordinary lower 29, "
            "prove exact unrestricted rank 32, or prove a border-rank statement."
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
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
    if not arguments.json and not arguments.verify_json:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
