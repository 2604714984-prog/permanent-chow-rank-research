#!/usr/bin/env python3
"""Exact replay for the N6-108 partial 3x4 product-pair exclusion."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, permutations
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_34_partial_pair_exclusion.json"
PRIME = 1_000_003
ROW_EDGES = tuple(combinations(range(3), 2))
COLUMN_EDGES = tuple(combinations(range(4), 2))
COORDINATES = tuple(range(12))
SIX_SUPPORTS = tuple(combinations(COORDINATES, 6))

REPRESENTATIVES = {
    "K23_diagonal": ((0, 1, 2, 4, 5, 6), (0, 1, 2, 4, 5, 6)),
    "K32_diagonal": ((0, 1, 4, 5, 8, 9), (0, 1, 4, 5, 8, 9)),
    "row_42_diagonal": ((0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)),
    "row_33_intersection_4": ((0, 1, 2, 4, 5, 7), (0, 1, 3, 4, 5, 6)),
}

RANK_FIVE_TANGENTS = {
    "row_42_diagonal": (
        (("L", 7, 3, -1), ("M", 6, 2, 1)),
        (("L", 7, 2, -1), ("M", 7, 2, 1)),
        (("L", 6, 3, -1), ("M", 6, 3, 1)),
        (("L", 6, 2, -1), ("M", 7, 3, 1)),
        (("L", 6, 4, 1), ("M", 6, 4, 1)),
        (("L", 7, 4, 1), ("M", 7, 4, 1)),
        (("L", 6, 5, 1), ("M", 6, 5, 1)),
        (("L", 7, 5, 1), ("M", 7, 5, 1)),
    ),
    "row_33_intersection_4": (
        (("L", 6, 4, 1), ("M", 2, 0, 1)),
        (("L", 6, 5, 1), ("M", 2, 1, 1)),
        (("L", 6, 7, -1), ("M", 2, 3, 1)),
        (("L", 6, 2, -1), ("M", 7, 3, 1)),
        (("L", 3, 0, 1), ("M", 7, 4, 1)),
        (("L", 3, 1, 1), ("M", 7, 5, 1)),
        (("L", 3, 7, -1), ("M", 2, 6, 1)),
        (("L", 3, 2, -1), ("M", 7, 6, 1)),
    ),
}


def signed_mod(value: int) -> int:
    value %= PRIME
    return value if value <= PRIME // 2 else value - PRIME


def rank_mod(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    work = [[entry % PRIME for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, PRIME)
        work[row] = [(entry * inverse) % PRIME for entry in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            coefficient = work[index][column]
            work[index] = [
                (left - coefficient * right) % PRIME
                for left, right in zip(work[index], work[row], strict=True)
            ]
        row += 1
        if row == len(work):
            break
    return row


def integer_nullspace(matrix: list[list[int]]) -> list[list[int]]:
    answer = []
    for vector in sp.Matrix(matrix).nullspace():
        denominator = 1
        for entry in vector:
            denominator = denominator * entry.q // gcd(denominator, entry.q)
        scaled = [int(entry * denominator) for entry in vector]
        divisor = 0
        for entry in scaled:
            divisor = gcd(divisor, abs(entry))
        answer.append([entry // max(divisor, 1) for entry in scaled])
    return answer


def unit(index: int) -> list[int]:
    return [int(coordinate == index) for coordinate in COORDINATES]


def beta(left: list[int], right: list[int]) -> list[int]:
    return [
        left[4 * i + c] * right[4 * j + d]
        + left[4 * i + d] * right[4 * j + c]
        + left[4 * j + c] * right[4 * i + d]
        + left[4 * j + d] * right[4 * i + c]
        for i, j in ROW_EDGES
        for c, d in COLUMN_EDGES
    ]


def cross_matrix(left: tuple[int, ...], right: tuple[int, ...]) -> list[list[int]]:
    return [beta(unit(i), unit(j)) for i in left for j in right]


def coordinate_cross_support(
    left: tuple[int, ...], right: tuple[int, ...]
) -> frozenset[tuple[tuple[int, int], tuple[int, int]]]:
    support = set()
    for first in left:
        for second in right:
            row_pair = tuple(sorted((first // 4, second // 4)))
            column_pair = tuple(sorted((first % 4, second % 4)))
            if row_pair[0] != row_pair[1] and column_pair[0] != column_pair[1]:
                support.add((row_pair, column_pair))
    return frozenset(support)


def transform_support(
    support: tuple[int, ...], row_permutation: tuple[int, ...],
    column_permutation: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        sorted(row_permutation[index // 4] * 4 + column_permutation[index % 4]
               for index in support)
    )


def orbit(pair: tuple[tuple[int, ...], tuple[int, ...]]) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    answer = set()
    for row_permutation in permutations(range(3)):
        for column_permutation in permutations(range(4)):
            transformed = (
                transform_support(pair[0], row_permutation, column_permutation),
                transform_support(pair[1], row_permutation, column_permutation),
            )
            answer.add(transformed)
            answer.add((transformed[1], transformed[0]))
    return answer


def coordinate_classification() -> dict[str, object]:
    small_pairs = {}
    for left in SIX_SUPPORTS:
        for right in SIX_SUPPORTS:
            dimension = len(coordinate_cross_support(left, right))
            if dimension <= 5:
                small_pairs[(left, right)] = dimension
    orbits = {name: orbit(pair) for name, pair in REPRESENTATIVES.items()}
    union = set().union(*orbits.values())
    assert union == set(small_pairs)
    assert sum(map(len, orbits.values())) == len(union)
    distribution: dict[str, int] = {}
    for dimension in small_pairs.values():
        distribution[str(dimension)] = distribution.get(str(dimension), 0) + 1
    return {
        "ordered_coordinate_pair_count": len(SIX_SUPPORTS) ** 2,
        "cross_dimension_at_most_five_count": len(small_pairs),
        "dimension_distribution": distribution,
        "orbits": {
            name: {
                "representative": [list(pair[0]), list(pair[1])],
                "orbit_size": len(orbits[name]),
                "cross_dimension": small_pairs[pair],
                "intersection_dimension": len(set(pair[0]) & set(pair[1])),
                "common_two_row_ambient": name != "K32_diagonal",
            }
            for name, pair in REPRESENTATIVES.items()
        },
        "orbit_union_is_complete_and_disjoint": True,
    }


def graph_derivatives(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[list[tuple[str, int, int]], list[list[list[int]]]]:
    variables = []
    derivatives = []
    for side, support, other in (("L", left, right), ("M", right, left)):
        targets = [index for index in COORDINATES if index not in support]
        for basis_index, source in enumerate(support):
            for target in targets:
                matrix = []
                for i in range(6):
                    for j in range(6):
                        if side == "L" and i == basis_index:
                            matrix.append(beta(unit(target), unit(right[j])))
                        elif side == "M" and j == basis_index:
                            matrix.append(beta(unit(left[i]), unit(target)))
                        else:
                            matrix.append([0] * 18)
                variables.append((side, target, source))
                derivatives.append(matrix)
    return variables, derivatives


def tangent_equations(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[list[tuple[str, int, int]], list[list[int]], list[list[list[int]]]]:
    base = cross_matrix(left, right)
    right_kernel = integer_nullspace(base)
    left_kernel = integer_nullspace([list(column) for column in zip(*base)])
    variables, derivatives = graph_derivatives(left, right)
    equations = []
    for left_vector in left_kernel:
        for right_vector in right_kernel:
            equations.append([
                sum(
                    left_vector[i] * derivative[i][j] * right_vector[j]
                    for i in range(36)
                    for j in range(18)
                )
                for derivative in derivatives
            ])
    return variables, equations, derivatives


def sparse_direction(
    variables: list[tuple[str, int, int]], entries: tuple[tuple[str, int, int, int], ...]
) -> list[int]:
    lookup = {variable: index for index, variable in enumerate(variables)}
    vector = [0] * len(variables)
    for side, target, source, coefficient in entries:
        vector[lookup[(side, target, source)]] = coefficient
    return vector


def rank_five_certificate(name: str) -> dict[str, object]:
    left, right = REPRESENTATIVES[name]
    variables, equations, _ = tangent_equations(left, right)
    directions = [
        sparse_direction(variables, entries) for entries in RANK_FIVE_TANGENTS[name]
    ]
    assert all(
        sum(row[index] * direction[index] for index in range(72)) == 0
        for row in equations
        for direction in directions
    )
    assert rank_mod(directions) == 8
    assert all(
        variables[index][1] < 8
        for direction in directions
        for index, coefficient in enumerate(direction)
        if coefficient
    )
    modular_rank = rank_mod(equations)
    assert modular_rank == 64
    normal_columns = [
        index for index, (_, target, _) in enumerate(variables) if target >= 8
    ]
    normal_rank = rank_mod([
        [row[index] for index in normal_columns] for row in equations
    ])
    assert len(normal_columns) == normal_rank == 48
    return {
        "base_cross_rank": 5,
        "equation_matrix_shape": [len(equations), len(equations[0])],
        "modular_rank_lower_bound": modular_rank,
        "explicit_integer_kernel_dimension": len(directions),
        "exact_QQ_rank": 64,
        "exact_QQ_nullity": 8,
        "normal_graph_variables": len(normal_columns),
        "exact_normal_linear_rank": normal_rank,
        "all_tangent_directions_stay_in_common_two_row_ambient": True,
    }


def add_polynomial(
    target: dict[tuple[int, int, int], int],
    first: list[tuple[int, int]], second: list[tuple[int, int]],
    third: list[tuple[int, int]], sign: int
) -> None:
    for i, a in first:
        for j, b in second:
            for k, c in third:
                monomial = tuple(sorted((i, j, k)))
                target[monomial] = target.get(monomial, 0) + sign * a * b * c


def cubic_minor_rows(
    matrices: list[list[list[int]]]
) -> tuple[list[tuple[int, ...]], list[tuple[int, int, int]]]:
    variable_count = len(matrices)
    monomials = list(combinations(range(variable_count), 3))
    monomials += [
        (i, i, j) for i in range(variable_count) for j in range(variable_count)
        if i != j
    ]
    monomials += [(i, i, i) for i in range(variable_count)]
    monomials = sorted(set(tuple(sorted(item)) for item in monomials))
    monomial_index = {monomial: index for index, monomial in enumerate(monomials)}
    forms = [
        [
            [
                (variable, matrices[variable][row][column])
                for variable in range(variable_count)
                if matrices[variable][row][column]
            ]
            for column in range(15)
        ]
        for row in range(33)
    ]
    rows = set()
    signs = (1, -1, -1, 1, 1, -1)
    permutations_three = tuple(permutations(range(3)))
    for row_indices in combinations(range(33), 3):
        possible_columns = [
            column for column in range(15)
            if any(forms[row][column] for row in row_indices)
        ]
        for column_indices in combinations(possible_columns, 3):
            polynomial: dict[tuple[int, int, int], int] = {}
            for sign, permutation in zip(signs, permutations_three, strict=True):
                factors = [
                    forms[row_indices[index]][column_indices[permutation[index]]]
                    for index in range(3)
                ]
                if all(factors):
                    add_polynomial(polynomial, *factors, sign)
            row = [0] * len(monomials)
            for monomial, coefficient in polynomial.items():
                row[monomial_index[monomial]] = coefficient
            if any(row):
                divisor = 0
                for coefficient in row:
                    divisor = gcd(divisor, abs(coefficient))
                row = [coefficient // max(divisor, 1) for coefficient in row]
                if next(coefficient for coefficient in row if coefficient) < 0:
                    row = [-coefficient for coefficient in row]
                rows.add(tuple(row))
    return sorted(rows), monomials


def leading_normal_matrices(
    left: tuple[int, ...], right: tuple[int, ...],
    variable_indices: list[int], derivatives: list[list[list[int]]]
) -> list[list[list[int]]]:
    base = cross_matrix(left, right)
    right_kernel = integer_nullspace(base)
    left_kernel = integer_nullspace([list(column) for column in zip(*base)])
    answer = []
    for variable in variable_indices:
        derivative = derivatives[variable]
        answer.append([
            [
                sum(
                    left_kernel[row][i] * derivative[i][j] * right_kernel[column][j]
                    for i in range(36)
                    for j in range(18)
                )
                for column in range(15)
            ]
            for row in range(33)
        ])
    return answer


def rank_three_certificate(name: str) -> dict[str, object]:
    left, right = REPRESENTATIVES[name]
    variables, _, derivatives = tangent_equations(left, right)
    grouped: dict[tuple[int, int], list[int]] = {}
    for index, (_, target, source) in enumerate(variables):
        weight = (target // 4 - source // 4, target % 4 - source % 4)
        grouped.setdefault(weight, []).append(index)
    if name == "K23_diagonal":
        grouped = {
            weight: indices for weight, indices in grouped.items()
            if any(variables[index][1] >= 8 for index in indices)
        }
    table = []
    for weight in sorted(grouped):
        indices = grouped[weight]
        matrices = leading_normal_matrices(left, right, indices, derivatives)
        rows, monomials = cubic_minor_rows(matrices)
        modular_rank = rank_mod([list(row) for row in rows])
        internal_positions = {
            position for position, index in enumerate(indices)
            if name == "K23_diagonal" and variables[index][1] < 8
        }
        internal_variables = len(internal_positions)
        internal_columns = [
            column for column, monomial in enumerate(monomials)
            if all(variable in internal_positions for variable in monomial)
        ]
        internal_matrix = [
            [row[column] for column in internal_columns] for row in rows
        ]
        exact_internal_rank = int(sp.Matrix(internal_matrix).rank()) if internal_columns else 0
        normal_monomials = len(monomials) - len(internal_columns)
        assert modular_rank == normal_monomials + exact_internal_rank, (
            name,
            weight,
            len(indices),
            internal_variables,
            len(monomials),
            modular_rank,
            exact_internal_rank,
            normal_monomials,
        )
        table.append({
            "weight": list(weight),
            "variables": len(indices),
            "internal_variables": internal_variables,
            "cubic_monomials": len(monomials),
            "unique_nonzero_minor_rows": len(rows),
            "modular_total_rank": modular_rank,
            "exact_QQ_internal_projection_rank": exact_internal_rank,
            "normal_monomials": normal_monomials,
            "all_normal_cubic_monomials_in_exact_initial_ideal": True,
        })
    return {
        "base_cross_rank": 3,
        "weight_group_count": len(table),
        "groups": table,
        "relative_projectivized_normal_cone_has_no_fixed_point": True,
    }


def build_payload() -> dict[str, object]:
    coordinate = coordinate_classification()
    rank_five = {
        name: rank_five_certificate(name)
        for name in ("row_42_diagonal", "row_33_intersection_4")
    }
    rank_three = {
        name: rank_three_certificate(name)
        for name in ("K23_diagonal", "K32_diagonal")
    }
    return {
        "certificate": "N6-108",
        "status": "CERTIFIED_CHARACTERISTIC_ZERO_PRODUCT_34_PARTIAL_PAIR_EXCLUSION",
        "field": "characteristic zero",
        "prime_used_for_nonzero_minor_lower_bounds": PRIME,
        "coordinate_fixed_pair_classification": coordinate,
        "rank_five_linear_normal_certificates": rank_five,
        "rank_three_cubic_normal_cone_certificates": rank_three,
        "pure_theorem": {
            "ambient": "V=k^3 tensor k^4",
            "quadratic_space": "E34=S0(k^3) tensor S0(k^4), dimension 18",
            "statement": "complementary six-planes L,M have beta_E34(L,M) dimension at least 6",
            "globalization": "projective torus components plus relative normal cones",
        },
        "partial_pair_corollary": {
            "q6": "cross-free D dimension at least 13 would force full E34 cross rank at most 5",
            "q5": "cross-free D dimension at least 13 has rank at most 2 in its 15-space; adding the three missing E34 directions gives rank at most 5",
            "transpose": True,
            "excluded_dimensions": [13, 14, 15],
        },
        "application": {
            "a2": 72,
            "newly_closed_biflag_kappa2_values": [1, 2],
            "closed_biflag_kappa2_values_after_N6_107_and_N6_108": [1, 2, 3],
            "remaining_a2_72_branches": [
                "standard hook and biflag at kappa2=0",
                "standard hook at kappa2=1,2",
            ],
        },
        "claim_boundary": (
            "This excludes the biflag product alternatives only for kappa2=1,2 "
            "(with kappa2=3 already excluded by N6-107). The kappa2=0 standard "
            "and biflag branches and standard-hook kappa2=1,2 branches remain "
            "open; this is not a proof of ordinary lower 29, exact "
            "ChowRank(perm_6)=32, or a border-rank statement."
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
