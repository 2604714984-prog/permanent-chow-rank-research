#!/usr/bin/env python3
"""Exact certificates for the twelve-dimensional 2x6 pair theorem (N6-111)."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_26_twelve_pair_rigidity.json"
EDGES = list(combinations(range(6), 2))


def rational_rank(rows: list[list[int | Fraction]]) -> int:
    basis: dict[int, dict[int, Fraction]] = {}
    for source in rows:
        row = {
            index: Fraction(value)
            for index, value in enumerate(source)
            if value
        }
        while row:
            pivot = min(row)
            coefficient = row[pivot]
            if pivot not in basis:
                basis[pivot] = {
                    index: value / coefficient for index, value in row.items()
                }
                break
            old = basis[pivot]
            for index, value in old.items():
                new = row.get(index, 0) - coefficient * value
                if new:
                    row[index] = new
                elif index in row:
                    del row[index]
    return len(basis)


def flatten(matrix: list[list[Fraction | int]]) -> list[Fraction | int]:
    return [entry for row in matrix for entry in row]


def multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(6)) for j in range(6)]
        for i in range(6)
    ]


def matrix_multiplier_rank(matrix: list[list[int]]) -> int:
    columns = []
    for first, second in EDGES:
        symmetric = [[0] * 6 for _ in range(6)]
        symmetric[first][second] = symmetric[second][first] = 1
        product = [
            [
                sum(matrix[row][index] * symmetric[index][column] for index in range(6))
                for column in range(6)
            ]
            for row in range(6)
        ]
        columns.append(
            [product[index][index] for index in range(6)]
            + [product[i][j] - product[j][i] for i, j in EDGES]
        )
    return rational_rank([list(column) for column in zip(*columns)])


def perfect_matchings() -> list[frozenset[tuple[int, int]]]:
    def recurse(vertices: frozenset[int]):
        if not vertices:
            return [frozenset()]
        first = min(vertices)
        rows = []
        for second in vertices - {first}:
            edge = tuple(sorted((first, second)))
            for tail in recurse(vertices - {first, second}):
                rows.append(tail | {edge})
        return rows

    return sorted(set(recurse(frozenset(range(6)))), key=sorted)


def rank_three_invariant_locus() -> dict[str, object]:
    maxima: dict[str, int] = {}
    equality_pairs = []
    for dimension in range(1, 6):
        maximum = 0
        for image_tuple in combinations(range(6), dimension):
            image = set(image_tuple)
            for source_tuple in combinations(range(6), dimension):
                source = set(source_tuple)
                allowed = sum(
                    (first not in source or second in image)
                    and (second not in source or first in image)
                    for first, second in EDGES
                )
                maximum = max(maximum, allowed)
                if dimension == 3 and allowed == 12:
                    equality_pairs.append(
                        {
                            "image": list(image_tuple),
                            "source": list(source_tuple),
                            "intersection_dimension": len(image & source),
                        }
                    )
        maxima[str(dimension)] = maximum

    # At H=<e0,e1,e2>, Z=<e3,e4,e5>, write H and Z as graphs A and T.
    # For a cross block C, the first variation in Hom(Z,V/H) is C^T T-A C.
    # Rank <=3 requires its diagonal and skew parts to vanish for every C.
    rows: list[list[int]] = []
    for c_row in range(3):
        for c_col in range(3):
            for diagonal in range(3):
                row = [0] * 18
                if c_col == diagonal:
                    row[9 + c_row * 3 + diagonal] += 1
                    row[diagonal * 3 + c_row] -= 1
                rows.append(row)
            for first, second in combinations(range(3), 2):
                row = [0] * 18

                # (C^T T-A C)_{first,second}
                if c_col == first:
                    row[9 + c_row * 3 + second] += 1
                    row[second * 3 + c_row] += 1
                if c_col == second:
                    row[first * 3 + c_row] -= 1
                    row[9 + c_row * 3 + first] -= 1
                rows.append(row)

    tangent_rank = rational_rank(rows)
    return {
        "coordinate_maxima_by_dimension": maxima,
        "rank_three_coordinate_equality_pair_count": len(equality_pairs),
        "all_rank_three_fixed_pairs_are_complementary": all(
            row["intersection_dimension"] == 0 for row in equality_pairs
        ),
        "rank_three_fixed_pairs": equality_pairs,
        "tangent_equation_count": len(rows),
        "tangent_variable_count": 18,
        "tangent_rank_over_Q": tangent_rank,
        "tangent_nullity": 18 - tangent_rank,
    }


def parabolic_algebra_certificate() -> dict[str, object]:
    # H={0,1,2}, Z={3,4,5}; Q consists of all zero-diagonal edges except
    # the three edges internal to Z. B0 is the cross perfect matching.
    q_edges = [edge for edge in EDGES if not set(edge) <= {3, 4, 5}]
    b0 = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for left, right in ((0, 3), (1, 4), (2, 5)):
        b0[left][right] = b0[right][left] = Fraction(1)
    b0_inverse = b0  # the cross-matching matrix is an involution

    generators = []
    for left, right in q_edges:
        matrix = [[Fraction(0) for _ in range(6)] for _ in range(6)]
        matrix[left][right] = matrix[right][left] = Fraction(1)
        generators.append(multiply(matrix, b0_inverse))

    basis: list[list[list[Fraction]]] = []

    def add(matrix: list[list[Fraction]]) -> bool:
        old_rank = rational_rank([flatten(item) for item in basis])
        new_rank = rational_rank([flatten(item) for item in basis] + [flatten(matrix)])
        if new_rank > old_rank:
            basis.append(matrix)
            return True
        return False

    identity = [[Fraction(int(i == j)) for j in range(6)] for i in range(6)]
    add(identity)
    for generator in generators:
        add(generator)
    changed = True
    rounds = 0
    while changed:
        rounds += 1
        changed = False
        old_basis = list(basis)
        for left in old_basis:
            for right in generators:
                changed = add(multiply(left, right)) or changed

    lower_left_zero = all(
        all(matrix[row][column] == 0 for row in range(3, 6) for column in range(3))
        for matrix in basis
    )
    return {
        "coordinate_Q_dimension": len(q_edges),
        "chosen_B0_is_cross_perfect_matching": True,
        "closure_round_count": rounds,
        "generated_algebra_dimension": len(basis),
        "full_three_by_three_block_upper_parabolic_dimension": 27,
        "every_generated_basis_matrix_has_zero_lower_left_block": lower_left_zero,
    }


def build_payload() -> dict[str, object]:
    off_diagonal_ranks = []
    for row in range(6):
        for column in range(6):
            if row == column:
                continue
            matrix = [[0] * 6 for _ in range(6)]
            matrix[row][column] = 1
            off_diagonal_ranks.append(matrix_multiplier_rank(matrix))
    diagonal_minimum = min(
        sum(values[left] != values[right] for left, right in EDGES)
        for size in range(1, 6)
        for support in combinations(range(6), size)
        for values in [tuple(int(index in support) for index in range(6))]
    )

    matchings = perfect_matchings()
    matching_counts = [
        sum(matching <= set(edges) for matching in matchings)
        for edges in combinations(EDGES, 12)
    ]
    invariant = rank_three_invariant_locus()
    parabolic = parabolic_algebra_certificate()

    assert set(off_diagonal_ranks) == {5}
    assert diagonal_minimum == 5
    assert len(matchings) == 15 and len(matching_counts) == 455
    assert min(matching_counts) == 6
    assert invariant["coordinate_maxima_by_dimension"] == {
        "1": 11,
        "2": 10,
        "3": 12,
        "4": 10,
        "5": 11,
    }
    assert invariant["rank_three_coordinate_equality_pair_count"] == 20
    assert invariant["tangent_rank_over_Q"] == 18
    assert parabolic["generated_algebra_dimension"] == 27
    assert parabolic["every_generated_basis_matrix_has_zero_lower_left_block"]

    return {
        "status": [
            "PURE_CHARACTERISTIC_ZERO_PRODUCT_26_TWELVE_PAIR_RIGIDITY",
            "PURE_REDUCED_RANK_THREE_INVARIANT_LOCUS",
            "EXACT_QQ_MULTIPLIER_TANGENT_AND_ALGEBRA_REPLAY",
            "N6-111",
        ],
        "twelve_plane_multiplier": {
            "rank_allowed_by_codimension_three": 3,
            "minimum_non_scalar_diagonal_rank": diagonal_minimum,
            "off_diagonal_matrix_unit_rank_set": sorted(set(off_diagonal_ranks)),
            "conclusion": "XQ subset S0 and dim Q at least 12 force X scalar",
        },
        "invertible_member": {
            "coordinate_twelve_plane_count": len(matching_counts),
            "perfect_matching_count": len(matchings),
            "minimum_surviving_matchings_after_deleting_three_edges": min(
                matching_counts
            ),
            "conclusion": "every twelve-plane in S0 contains an invertible member",
        },
        "proper_invariant_space_locus": invariant,
        "exceptional_ratio_algebra": parabolic,
        "pure_module_classification": {
            "parabolic_module": "V=H3 extended by Z3",
            "six_dimensional_submodules_of_k2_tensor_V": [
                "k2 tensor H3",
                "p tensor V for a line p in k2",
            ],
            "only_complementary_six_submodule_pairs": "p tensor V and q tensor V",
        },
        "theorem": (
            "If D is a twelve-plane in the full 2x6 permanent rectangle space, "
            "has twelve-dimensional shadow, and is block diagonal for an actual "
            "complementary pair L,M, then L=p tensor k6 and M=q tensor k6."
        ),
        "claim_boundary": (
            "This lowers the N6-109 partial 2x6 threshold from thirteen to twelve. "
            "It does not classify every twelve-plane in a standard or biflag "
            "23-plane, exclude the full kappa2=0 six-color layer, prove ordinary "
            "lower 29, determine ChowRank(perm_6)=32, or prove a border-rank bound."
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
                "invariant_fixed_points": payload["proper_invariant_space_locus"][
                    "rank_three_coordinate_equality_pair_count"
                ],
                "invariant_tangent_nullity": payload[
                    "proper_invariant_space_locus"
                ]["tangent_nullity"],
                "ratio_algebra_dimension": payload["exceptional_ratio_algebra"][
                    "generated_algebra_dimension"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
