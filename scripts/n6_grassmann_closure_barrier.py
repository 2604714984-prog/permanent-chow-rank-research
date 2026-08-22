#!/usr/bin/env python3
"""Exact G-049 collision barrier for complementary Chow factor frames."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_grassmann_closure_barrier.json"
N = 6
V_DIM = 2 * N
SYM2_COORDINATES = list(combinations(range(V_DIM), 2)) + [
    (index, index) for index in range(V_DIM)
]
SYM2_INDEX = {pair: index for index, pair in enumerate(SYM2_COORDINATES)}


def rank_q(rows: list[list[int | Fraction]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][column]
        matrix[rank] = [entry / value for entry in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank or not matrix[index][column]:
                continue
            value = matrix[index][column]
            matrix[index] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(matrix[index], matrix[rank])
            ]
        rank += 1
    return rank


def determinant_q(rows: list[list[int | Fraction]]) -> Fraction:
    matrix = [[Fraction(value) for value in row] for row in rows]
    determinant = Fraction(1)
    for column in range(len(matrix)):
        pivot = next(
            (index for index in range(column, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant *= -1
        value = matrix[column][column]
        determinant *= value
        matrix[column] = [entry / value for entry in matrix[column]]
        for index in range(column + 1, len(matrix)):
            value = matrix[index][column]
            if not value:
                continue
            matrix[index] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(matrix[index], matrix[column])
            ]
    return determinant


def u(column: int) -> list[Fraction]:
    vector = [Fraction(0)] * V_DIM
    vector[column] = 1
    return vector


def v(column: int) -> list[Fraction]:
    vector = [Fraction(0)] * V_DIM
    vector[N + column] = 1
    return vector


def add(*vectors: list[Fraction]) -> list[Fraction]:
    return [sum(entries, Fraction(0)) for entries in zip(*vectors)]


def scale(scalar: int | Fraction, vector: list[Fraction]) -> list[Fraction]:
    return [Fraction(scalar) * entry for entry in vector]


def sym_product(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * len(SYM2_COORDINATES)
    for i, left_value in enumerate(left):
        if not left_value:
            continue
        for j, right_value in enumerate(right):
            if not right_value:
                continue
            pair = (i, j) if i <= j else (j, i)
            result[SYM2_INDEX[pair]] += left_value * right_value
    return result


def factor_plane(sign: int, t: int | Fraction) -> list[list[Fraction]]:
    return [add(v(column), scale(sign * Fraction(t), u(column))) for column in range(N)]


def full_frame(sign: int, t: int | Fraction) -> list[list[Fraction]]:
    plane = factor_plane(sign, t)
    return [sym_product(plane[c], plane[d]) for c, d in combinations(range(N), 2)]


def symmetric_square_plane(sign: int, t: int | Fraction) -> list[list[Fraction]]:
    plane = factor_plane(sign, t)
    return [
        sym_product(plane[c], plane[d])
        for c in range(N)
        for d in range(c, N)
    ]


def difference_space() -> list[list[Fraction]]:
    return [
        add(sym_product(u(c), v(d)), sym_product(u(d), v(c)))
        for c, d in combinations(range(N), 2)
    ]


def derivative_span(quadrics: list[list[Fraction]]) -> list[list[Fraction]]:
    derivatives: list[list[Fraction]] = []
    for quadric in quadrics:
        for variable in range(V_DIM):
            linear = [Fraction(0)] * V_DIM
            for coefficient, (i, j) in zip(quadric, SYM2_COORDINATES):
                if not coefficient:
                    continue
                if i == j == variable:
                    linear[variable] += 2 * coefficient
                elif i == variable:
                    linear[j] += coefficient
                elif j == variable:
                    linear[i] += coefficient
            derivatives.append(linear)
    return derivatives


def hook_support_audit() -> dict[str, object]:
    rows_four = set(range(4))
    rows_three = set(range(3))
    columns_five = set(range(5))
    row_pairs_four = set(combinations(rows_four, 2))
    row_pairs_three = set(combinations(rows_three, 2))
    column_pairs_five = set(combinations(columns_five, 2))
    column_pairs_six = set(combinations(range(6), 2))
    hook = (row_pairs_four | row_pairs_three)
    hook_support = {
        (row_pair, column_pair)
        for row_pair in row_pairs_four
        for column_pair in column_pairs_five
    } | {
        (row_pair, column_pair)
        for row_pair in row_pairs_three
        for column_pair in column_pairs_six
    }
    del hook
    d_support = {((0, 1), column_pair) for column_pair in column_pairs_six}
    hook_shadow = {
        (row, column)
        for row in rows_four
        for column in columns_five
    } | {(row, column) for row in rows_three for column in range(6)}
    d_shadow = {(row, column) for row in (0, 1) for column in range(6)}
    assert len(hook_support) == 75
    assert len(d_support) == 15 and d_support <= hook_support
    assert len(hook_shadow) == 23
    assert len(d_shadow) == 12 and d_shadow <= hook_shadow
    return {
        "standard_b50_hook_quadratic_dimension": len(hook_support),
        "fixed_D_dimension": len(d_support),
        "D_is_contained_in_hook": d_support <= hook_support,
        "standard_b50_hook_second_shadow_dimension": len(hook_shadow),
        "D_second_shadow_dimension": len(d_shadow),
        "D_shadow_is_contained_in_hook_shadow": d_shadow <= hook_shadow,
    }


def nonzero_fiber_audit(t: int) -> dict[str, object]:
    plus_plane = factor_plane(+1, t)
    minus_plane = factor_plane(-1, t)
    plus_frame = full_frame(+1, t)
    minus_frame = full_frame(-1, t)
    plus_symmetric_square = symmetric_square_plane(+1, t)
    minus_symmetric_square = symmetric_square_plane(-1, t)
    difference = difference_space()
    normalized_differences = [
        scale(Fraction(1, 2 * t), add(plus, scale(-1, minus)))
        for plus, minus in zip(plus_frame, minus_frame)
    ]
    return {
        "t": t,
        "factor_plane_ranks": [rank_q(plus_plane), rank_q(minus_plane)],
        "factor_plane_sum_rank": rank_q(plus_plane + minus_plane),
        "exterior_determinant": int(determinant_q(plus_plane + minus_plane)),
        "full_frame_ranks": [rank_q(plus_frame), rank_q(minus_frame)],
        "full_frame_sum_rank": rank_q(plus_frame + minus_frame),
        "symmetric_square_sum_rank": rank_q(
            plus_symmetric_square + minus_symmetric_square
        ),
        "D_rank": rank_q(difference),
        "D_contained_in_full_frame_sum": (
            rank_q(plus_frame + minus_frame + difference)
            == rank_q(plus_frame + minus_frame)
        ),
        "D_contained_in_symmetric_square_sum": (
            rank_q(plus_symmetric_square + minus_symmetric_square + difference)
            == rank_q(plus_symmetric_square + minus_symmetric_square)
        ),
        "normalized_section_difference_equals_fixed_D": normalized_differences
        == difference,
        "common_quotient_image_dimension": rank_q(difference + plus_frame)
        - rank_q(difference),
        "quotient_images_are_equal": (
            rank_q(difference + plus_frame + minus_frame)
            == rank_q(difference + plus_frame)
            == rank_q(difference + minus_frame)
        ),
    }


def special_fiber_audit() -> dict[str, object]:
    plus_plane = factor_plane(+1, 0)
    minus_plane = factor_plane(-1, 0)
    plus_frame = full_frame(+1, 0)
    minus_frame = full_frame(-1, 0)
    plus_symmetric_square = symmetric_square_plane(+1, 0)
    minus_symmetric_square = symmetric_square_plane(-1, 0)
    difference = difference_space()
    derivatives = derivative_span(difference)
    flat_factor_sum = [u(column) for column in range(N)] + plus_plane
    flat_full_frame_sum = plus_frame + difference
    return {
        "t": 0,
        "colliding_factor_plane_rank": rank_q(plus_plane + minus_plane),
        "fixed_D_rank": rank_q(difference),
        "fixed_D_derivative_rank": rank_q(derivatives),
        "derivative_contained_in_actual_plane_sum": (
            rank_q(plus_plane + minus_plane + derivatives)
            == rank_q(plus_plane + minus_plane)
        ),
        "colliding_full_frame_sum_rank": rank_q(plus_frame + minus_frame),
        "D_contained_in_actual_full_frame_sum": (
            rank_q(plus_frame + minus_frame + difference)
            == rank_q(plus_frame + minus_frame)
        ),
        "colliding_symmetric_square_sum_rank": rank_q(
            plus_symmetric_square + minus_symmetric_square
        ),
        "D_contained_in_actual_symmetric_square_sum": (
            rank_q(plus_symmetric_square + minus_symmetric_square + difference)
            == rank_q(plus_symmetric_square + minus_symmetric_square)
        ),
        "flat_limit_factor_sum_rank": rank_q(flat_factor_sum),
        "D_derivative_contained_in_flat_factor_sum": (
            rank_q(flat_factor_sum + derivatives) == rank_q(flat_factor_sum)
        ),
        "flat_limit_full_frame_sum_rank": rank_q(flat_full_frame_sum),
        "D_contained_in_flat_full_frame_sum": (
            rank_q(flat_full_frame_sum + difference) == rank_q(flat_full_frame_sum)
        ),
        "first_order_relative_graph_map_rank": N,
        "first_order_relative_graph_map_matrix": [
            [2 if row == column else 0 for column in range(N)] for row in range(N)
        ],
        "order_of_complementarity_determinant": N,
        "leading_complementarity_determinant_coefficient": 2**N,
    }


def build_payload() -> dict[str, object]:
    nonzero = [nonzero_fiber_audit(t) for t in (-3, -1, 1, 2)]
    for row in nonzero:
        assert row["factor_plane_ranks"] == [6, 6]
        assert row["factor_plane_sum_rank"] == 12
        assert row["exterior_determinant"] == 64 * row["t"] ** 6
        assert row["full_frame_ranks"] == [15, 15]
        assert row["full_frame_sum_rank"] == 30
        assert row["symmetric_square_sum_rank"] == 42
        assert row["D_rank"] == 15
        assert row["D_contained_in_full_frame_sum"]
        assert row["D_contained_in_symmetric_square_sum"]
        assert row["normalized_section_difference_equals_fixed_D"]
        assert row["common_quotient_image_dimension"] == 15
        assert row["quotient_images_are_equal"]
    special = special_fiber_audit()
    assert special["colliding_factor_plane_rank"] == 6
    assert special["fixed_D_rank"] == 15
    assert special["fixed_D_derivative_rank"] == 12
    assert not special["derivative_contained_in_actual_plane_sum"]
    assert special["colliding_full_frame_sum_rank"] == 15
    assert not special["D_contained_in_actual_full_frame_sum"]
    assert special["colliding_symmetric_square_sum_rank"] == 21
    assert not special["D_contained_in_actual_symmetric_square_sum"]
    assert special["flat_limit_factor_sum_rank"] == 12
    assert special["D_derivative_contained_in_flat_factor_sum"]
    assert special["flat_limit_full_frame_sum_rank"] == 30
    assert special["D_contained_in_flat_full_frame_sum"]
    return {
        "status": [
            "PURE_EXPLICIT_DEGENERATION",
            "EXACT_QQ_REPLAY",
            "GRASSMANN_INCIDENCE_ROUTE_BARRIER",
            "G-049",
        ],
        "family": {
            "factor_planes": "L_t=(v+t*u) tensor C6, M_t=(v-t*u) tensor C6",
            "fixed_section_difference": "D=(u*v+v*u) tensor S0(C6)",
            "nonzero_parameters_replayed": nonzero,
            "special_fiber": special,
        },
        "standard_b50_hook_embedding": hook_support_audit(),
        "claim_boundary": (
            "This is one exact two-frame common-quotient collision embedded in "
            "the standard b=50 quadratic hook. It proves that the raw conditions "
            "partial(D) subset L+M and D subset Sym2(L)+Sym2(M) are not closed "
            "when L and M collide. It is not a complete six-term b=50 "
            "configuration, does not satisfy all fifteen section-difference "
            "cocycles, and does not refute lower 28. The flat limit and the "
            "full-rank first-order relative graph map retain the missing data."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("nonzero plane sums", [row["factor_plane_sum_rank"] for row in payload["family"]["nonzero_parameters_replayed"]])
    print("special plane sum", payload["family"]["special_fiber"]["colliding_factor_plane_rank"])
    print("fixed D/shadow", payload["family"]["special_fiber"]["fixed_D_rank"], payload["family"]["special_fiber"]["fixed_D_derivative_rank"])
    print("hook", payload["standard_b50_hook_embedding"])


if __name__ == "__main__":
    main()
