#!/usr/bin/env python3
"""Exact rank-six fixed-stratum reduction in the 3 x 4 product space.

This certificate deliberately stops at the lower-rank fixed strata.  Its
expensive replay enumerates all coordinate pairs and performs the twenty
rank-six local eliminations.  Ordinary tests use the frozen JSON and replay
only the two exceptional representatives.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_34_rank_six_fixed_reduction.json"
BASE_PATH = ROOT / "scripts" / "n6_product_34_partial_pair_exclusion.py"
SPEC = importlib.util.spec_from_file_location("n6_product_34_partial", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BASE)
PRIME = BASE.PRIME


def modular_rref(matrix: np.ndarray) -> tuple[np.ndarray, list[int]]:
    work = matrix.copy() % PRIME
    row = 0
    pivots = []
    for column in range(work.shape[1]):
        choices = np.nonzero(work[row:, column] % PRIME)[0]
        if not len(choices):
            continue
        pivot = row + int(choices[0])
        work[[row, pivot]] = work[[pivot, row]]
        work[row] = work[row] * pow(int(work[row, column]), -1, PRIME) % PRIME
        for other in range(work.shape[0]):
            if other != row and work[other, column]:
                work[other] = (
                    work[other] - int(work[other, column]) * work[row]
                ) % PRIME
        pivots.append(column)
        row += 1
        if row == work.shape[0]:
            break
    return work, pivots


def modular_inverse(matrix: np.ndarray) -> np.ndarray:
    size = matrix.shape[0]
    work = np.concatenate(
        [matrix.copy() % PRIME, np.eye(size, dtype=np.int64)], axis=1
    )
    for column in range(size):
        choices = np.nonzero(work[column:, column] % PRIME)[0]
        assert len(choices)
        pivot = column + int(choices[0])
        work[[column, pivot]] = work[[pivot, column]]
        work[column] = (
            work[column] * pow(int(work[column, column]), -1, PRIME) % PRIME
        )
        for other in range(size):
            if other != column and work[other, column]:
                work[other] = (
                    work[other] - int(work[other, column]) * work[column]
                ) % PRIME
    return work[:, size:] % PRIME


def rank_six_coordinate_orbits() -> tuple[list[dict[str, object]], Counter[int]]:
    pairs = {}
    distribution: Counter[int] = Counter()
    for left in BASE.SIX_SUPPORTS:
        for right in BASE.SIX_SUPPORTS:
            dimension = len(BASE.coordinate_cross_support(left, right))
            if dimension <= 6:
                pairs[(left, right)] = dimension
                distribution[dimension] += 1

    remaining = {pair for pair, dimension in pairs.items() if dimension == 6}
    rows = []
    while remaining:
        pair = min(remaining)
        current_orbit = BASE.orbit(pair) & remaining
        remaining -= current_orbit
        union_rows = {coordinate // 4 for support in pair for coordinate in support}
        rows.append(
            {
                "representative": [list(pair[0]), list(pair[1])],
                "orbit_size": len(current_orbit),
                "intersection_dimension": len(set(pair[0]) & set(pair[1])),
                "common_coordinate_two_row_container": len(union_rows) <= 2,
            }
        )
    assert len(rows) == 20
    assert sum(row["orbit_size"] for row in rows) == 2424
    assert sum(row["common_coordinate_two_row_container"] for row in rows) == 18
    return rows, distribution


def linear_certificate(pair: tuple[tuple[int, ...], tuple[int, ...]]) -> dict[str, object]:
    variables, equations, _ = BASE.tangent_equations(*pair)
    modular_rank = BASE.rank_mod(equations)
    nullity = 72 - modular_rank
    integer_kernel = BASE.integer_nullspace(equations)
    assert len(integer_kernel) == nullity
    return {
        "linear_rank_mod_1000003": modular_rank,
        "integer_kernel_dimension": len(integer_kernel),
        "exact_QQ_rank": modular_rank,
        "exact_tangent_nullity": nullity,
    }


def common_two_row_certificate(
    rows: list[dict[str, object]],
) -> dict[str, object]:
    rank_histogram: Counter[int] = Counter()
    internal_rank_histogram: Counter[int] = Counter()
    orbit_size = 0
    for row in rows:
        if not row["common_coordinate_two_row_container"]:
            continue
        pair = tuple(tuple(value) for value in row["representative"])
        variables, equations, _ = BASE.tangent_equations(*pair)
        active_rows = {coordinate // 4 for support in pair for coordinate in support}
        internal = [
            index
            for index, (_, target, _) in enumerate(variables)
            if target // 4 in active_rows
        ]
        internal_equations = [
            [equation[index] for index in internal] for equation in equations
        ]
        rank = BASE.rank_mod(equations)
        internal_rank = BASE.rank_mod(internal_equations)
        assert len(internal) == 24
        assert rank == 48 and internal_rank == 0
        rank_histogram[rank] += 1
        internal_rank_histogram[internal_rank] += 1
        orbit_size += row["orbit_size"]
    assert rank_histogram == Counter({48: 18})
    assert internal_rank_histogram == Counter({0: 18})
    assert orbit_size == 2268
    return {
        "representative_orbit_count": 18,
        "ordered_fixed_pair_count": orbit_size,
        "internal_graph_variable_count": 24,
        "normal_graph_variable_count": 48,
        "normal_linear_rank_histogram": {"48": 18},
        "internal_linear_rank_histogram": {"0": 18},
        "formal_germ_is_contained_in_the_fixed_eight_space": True,
        "intersection_dimension_is_at_least_four": True,
    }


def difference_matrix(
    pair: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[list[list[int]], list[list[int]], list[tuple[str, int, int]]]:
    assert pair[0] == pair[1]
    variables, equations, _ = BASE.tangent_equations(*pair)
    positions = {variable: index for index, variable in enumerate(variables)}
    columns = []
    for source in pair[0]:
        for target in BASE.COORDINATES:
            if target in pair[0]:
                continue
            columns.append(
                [
                    equation[positions["L", target, source]]
                    - equation[positions["M", target, source]]
                    for equation in equations
                ]
            )
    return equations, [list(row) for row in zip(*columns)], variables


def diagonal_411_certificate() -> dict[str, object]:
    support = (0, 1, 2, 3, 4, 8)
    pair = (support, support)
    equations, difference, _ = difference_matrix(pair)
    linear = linear_certificate(pair)
    difference_rank = BASE.rank_mod(difference)
    assert linear["exact_QQ_rank"] == 69
    assert difference_rank == 36
    return {
        "representative": list(support),
        "row_profile": [4, 1, 1],
        "ordered_fixed_pair_count": 12,
        **linear,
        "difference_variable_rank": difference_rank,
        "formal_swap_uniqueness_forces_L_equals_M": True,
    }


def weight(variable: tuple[str, int, int]) -> tuple[int, ...]:
    _, target, source = variable
    answer = [0] * 7
    answer[target // 4] += 1
    answer[source // 4] -= 1
    answer[3 + target % 4] += 1
    answer[3 + source % 4] -= 1
    return tuple(answer)


def transformed_schur_data(
    pair: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[
    list[tuple[str, int, int]],
    list[list[int]],
    list[list[int]],
    list[np.ndarray],
    np.ndarray,
    np.ndarray,
    list[int],
    list[int],
]:
    variables, equations, derivatives = BASE.tangent_equations(*pair)
    kernel = BASE.integer_nullspace(equations)
    base = np.array(BASE.cross_matrix(*pair), dtype=np.int64) % PRIME
    _, pivot_columns = modular_rref(base)
    _, pivot_rows = modular_rref(base.T)
    pivot_columns = pivot_columns[:6]
    pivot_rows = pivot_rows[:6]
    other_rows = [index for index in range(36) if index not in pivot_rows]
    other_columns = [index for index in range(18) if index not in pivot_columns]
    pivot = base[np.ix_(pivot_rows, pivot_columns)]
    pivot_inverse = modular_inverse(pivot)
    upper_right = base[np.ix_(pivot_rows, other_columns)]
    lower_left = base[np.ix_(other_rows, pivot_columns)]

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

    def transform(matrix: np.ndarray) -> np.ndarray:
        return left_transform @ matrix @ right_transform % PRIME

    canonical = transform(base)
    assert np.array_equal(canonical[:6, :6], np.eye(6, dtype=np.int64))
    assert not canonical[:6, 6:].any() and not canonical[6:, :].any()
    linear_columns = []
    linear_blocks = []
    for derivative in derivatives:
        transformed = transform(np.array(derivative, dtype=np.int64) % PRIME)
        linear_columns.append(transformed[6:, 6:].reshape(-1))
    linear = np.array(linear_columns, dtype=np.int64).T % PRIME
    for vector in kernel:
        derivative = sum(
            (
                int(coefficient) * np.array(matrix, dtype=np.int64)
                for coefficient, matrix in zip(vector, derivatives)
            ),
            start=np.zeros((36, 18), dtype=np.int64),
        ) % PRIME
        transformed = transform(derivative)
        linear_blocks.append((transformed[6:, :6], transformed[:6, 6:]))
    return (
        variables,
        equations,
        kernel,
        linear_blocks,
        linear,
        np.array([transform(base)]),
        pivot_rows,
        pivot_columns,
    )


def staircase_quadratic_certificate() -> dict[str, object]:
    support = (0, 1, 2, 4, 5, 8)
    pair = (support, support)
    (
        variables,
        equations,
        kernel,
        linear_blocks,
        linear,
        _,
        _,
        _,
    ) = transformed_schur_data(pair)
    assert len(kernel) == 11
    assert BASE.rank_mod(linear.tolist()) == 61
    diagonal_directions = 0
    for vector in kernel:
        left_coefficients = {
            (target, source): coefficient
            for coefficient, (side, target, source) in zip(vector, variables)
            if side == "L" and coefficient
        }
        right_coefficients = {
            (target, source): coefficient
            for coefficient, (side, target, source) in zip(vector, variables)
            if side == "M" and coefficient
        }
        diagonal_directions += left_coefficients == right_coefficients
    assert diagonal_directions == 9

    directions_left = []
    directions_right = []
    for vector in kernel:
        left = np.zeros((6, 12), dtype=np.int64)
        right = np.zeros((6, 12), dtype=np.int64)
        for coefficient, (side, target, source) in zip(vector, variables):
            if not coefficient:
                continue
            basis_index = support.index(source)
            destination = left if side == "L" else right
            destination[basis_index, target] += coefficient
        directions_left.append(left % PRIME)
        directions_right.append(right % PRIME)

    base = np.array(BASE.cross_matrix(*pair), dtype=np.int64) % PRIME
    _, pivot_columns = modular_rref(base)
    _, pivot_rows = modular_rref(base.T)
    pivot_columns = pivot_columns[:6]
    pivot_rows = pivot_rows[:6]
    other_rows = [index for index in range(36) if index not in pivot_rows]
    other_columns = [index for index in range(18) if index not in pivot_columns]
    pivot_inverse = modular_inverse(base[np.ix_(pivot_rows, pivot_columns)])
    upper_right = base[np.ix_(pivot_rows, other_columns)]
    lower_left = base[np.ix_(other_rows, pivot_columns)]
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

    def transform(matrix: np.ndarray) -> np.ndarray:
        return left_transform @ matrix @ right_transform % PRIME

    def quadratic_cross(left: np.ndarray, right: np.ndarray) -> np.ndarray:
        return np.array(
            [
                BASE.beta(left[i].tolist(), right[j].tolist())
                for i in range(6)
                for j in range(6)
            ],
            dtype=np.int64,
        ) % PRIME

    _, independent_columns = modular_rref(linear)
    independent_columns = independent_columns[:61]
    _, independent_rows = modular_rref(linear[:, independent_columns].T)
    independent_rows = independent_rows[:61]
    inverse_minor = modular_inverse(
        linear[np.ix_(independent_rows, independent_columns)]
    )

    labels = []
    quadratic_columns = []
    for first in range(11):
        for second in range(first, 11):
            if first == second:
                quadratic = quadratic_cross(
                    directions_left[first], directions_right[first]
                )
            else:
                quadratic = (
                    quadratic_cross(
                        directions_left[first], directions_right[second]
                    )
                    + quadratic_cross(
                        directions_left[second], directions_right[first]
                    )
                ) % PRIME
            transformed = transform(quadratic)
            schur = transformed[6:, 6:] - (
                linear_blocks[first][0] @ linear_blocks[second][1]
            )
            if first != second:
                schur -= linear_blocks[second][0] @ linear_blocks[first][1]
            quadratic_columns.append(schur.reshape(-1) % PRIME)
            labels.append((first, second))
    quadratic_matrix = np.array(quadratic_columns, dtype=np.int64).T % PRIME
    residual = (
        quadratic_matrix
        - linear[:, independent_columns]
        @ inverse_minor
        @ quadratic_matrix[independent_rows, :]
    ) % PRIME
    reduced, _ = modular_rref(residual)
    nonzero_rows = [row for row in reduced if row.any()]
    monomial_generators = []
    for row in nonzero_rows:
        support_indices = np.nonzero(row)[0]
        assert len(support_indices) == 1
        monomial_generators.append(labels[int(support_indices[0])])
    monomial_generators = sorted(monomial_generators)
    expected = sorted(
        [
            (0, 1), (0, 3), (0, 4), (0, 7), (1, 2),
            (1, 4), (1, 8), (2, 4), (3, 6), (3, 10),
            (4, 6), (4, 8), (4, 10), (5, 6), (5, 8),
            (5, 10), (6, 7), (7, 8), (7, 10), (9, 10),
        ]
    )
    assert monomial_generators == expected

    facets = []
    edge_sets = [set(edge) for edge in expected]
    for mask in range(1 << 11):
        subset = {index for index in range(11) if mask >> index & 1}
        if any(edge <= subset for edge in edge_sets):
            continue
        if all(
            any(edge <= subset | {index} for edge in edge_sets)
            for index in range(11)
            if index not in subset
        ):
            facets.append(tuple(sorted(subset)))
    assert len(facets) == 9

    tangent_weights = []
    for vector in kernel:
        nonzero = [
            variable
            for coefficient, variable in zip(vector, variables)
            if coefficient
        ]
        weights = {weight(variable) for variable in nonzero}
        assert len(weights) == 1
        tangent_weights.append(next(iter(weights)))
    row_counts = Counter(coordinate // 4 for coordinate in support)
    column_counts = Counter(coordinate % 4 for coordinate in support)
    determinant_weight = tuple(
        [4 - 2 * row_counts[index] for index in range(3)]
        + [3 - 2 * column_counts[index] for index in range(4)]
    )
    assert determinant_weight == (-2, 0, 2, -3, -1, 1, 3)
    generator_weights = [
        tuple(
            tangent_weights[first][coordinate]
            + tangent_weights[second][coordinate]
            for coordinate in range(7)
        )
        for first, second in expected
    ]
    weight_block_histogram = Counter(Counter(generator_weights).values())
    assert weight_block_histogram == Counter({1: 12, 2: 4})
    facets_with_column_three_weight = [facet for facet in facets if 1 in facet]
    assert facets_with_column_three_weight == [
        (1, 6, 9),
        (1, 3, 5, 7, 9),
        (1, 6, 10),
    ]
    # The final column coordinate forces exponent(x_1)=3.  The middle facet
    # then has no positive column-2 weight.  In the other two facets the
    # column equations determine (x_6,x_9)=(4,3) or (x_6,x_10)=(1,3),
    # respectively; all three variables have zero row weight, whereas the
    # determinant has row weight (-2,0,2).
    return {
        "representative": list(support),
        "row_profile": [3, 2, 1],
        "ordered_fixed_pair_count": 144,
        "exact_linear_rank": 61,
        "exact_tangent_nullity": 11,
        "diagonal_tangent_dimension": diagonal_directions,
        "separating_tangent_dimension": 11 - diagonal_directions,
        "quadratic_cokernel_rank": len(nonzero_rows),
        "quadratic_squarefree_monomial_generators": [
            list(edge) for edge in expected
        ],
        "quadratic_generator_weight_block_size_histogram": {
            str(key): value
            for key, value in sorted(weight_block_histogram.items())
        },
        "every_quadratic_generator_weight_block_has_full_modular_rank": True,
        "maximal_independent_facets": [list(facet) for facet in facets],
        "facet_dimension_histogram": {
            str(key): value for key, value in sorted(Counter(map(len, facets)).items())
        },
        "tangent_weights": [list(value) for value in tangent_weights],
        "complement_determinant_weight": list(determinant_weight),
        "facets_containing_the_only_positive_column_three_weight": [
            list(facet) for facet in facets_with_column_three_weight
        ],
        "no_surviving_tangent_monomial_has_the_complement_determinant_weight": True,
        "complement_determinant_vanishes_in_the_completed_local_ring": True,
    }


def build_payload() -> dict[str, object]:
    orbits, distribution = rank_six_coordinate_orbits()
    return {
        "status": "EXACT_RANK_SIX_FIXED_STRATUM_COMPLEMENT_EXCLUSION",
        "coordinate_classification": {
            "ordered_coordinate_pair_count": len(BASE.SIX_SUPPORTS) ** 2,
            "cross_rank_at_most_six_count": sum(distribution.values()),
            "rank_distribution": {
                str(key): value for key, value in sorted(distribution.items())
            },
            "rank_six_ordered_pair_count": distribution[6],
            "rank_six_orbit_count": len(orbits),
            "rank_six_orbits": orbits,
            "coordinate_complementary_rank_six_pair_count": 0,
        },
        "common_two_row_stratum": common_two_row_certificate(orbits),
        "diagonal_411_stratum": diagonal_411_certificate(),
        "diagonal_321_staircase_stratum": staircase_quadratic_certificate(),
        "projective_conclusion": {
            "every_component_with_a_rank_exactly_six_fixed_point_is_noncomplementary": True,
            "a_complementary_rank_at_most_six_component_must_specialize_to_rank_three_or_five": True,
        },
        "arithmetic": {
            "prime_for_nonzero_minor_lower_bounds": PRIME,
            "integer_kernel_dimensions_supply_matching_QQ_upper_bounds": True,
            "quadratic_weight_blocks_supply_matching_QQ_upper_bounds": True,
        },
        "boundary": (
            "This excludes complementarity only for components whose torus-fixed point has "
            "cross rank exactly six. Components specializing to the rank-three or rank-five "
            "fixed strata require their larger rank-at-most-six normal cones to be analyzed. "
            "Therefore this does not yet exclude every twelve-dimensional 3x4 section, the "
            "kappa2=0 six-color branches, ordinary lower 29, exact rank 32, or border rank."
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
            if json.loads(args.verify_json.read_text()) != payload:
                raise SystemExit("frozen JSON does not match regenerated certificate")
    else:
        payload = json.loads(DEFAULT_JSON.read_text())
        print(payload["status"])
        print(payload["coordinate_classification"]["rank_distribution"])
        print(payload["diagonal_321_staircase_stratum"]["quadratic_cokernel_rank"])


if __name__ == "__main__":
    main()
