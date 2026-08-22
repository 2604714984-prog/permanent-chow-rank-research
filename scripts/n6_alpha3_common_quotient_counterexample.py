#!/usr/bin/env python3
"""Exact G-043 common-W15 alpha-three counterexample.

Six actual Chow terms have pairwise-disjoint quadratic derivative spaces and
one common fifteen-dimensional quotient.  Their quadratic scalar data are
exactly the residual all-alpha-three data, but their cubic permanent
intersection is zero rather than sixty.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path


N = 6


def exact_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    column_count = len(work[0]) if work else 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(rank + 1, len(work)):
            coefficient = work[row][column]
            if not coefficient:
                continue
            work[row] = [
                value - coefficient * pivot_value
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def sign_rows() -> list[list[int]]:
    """All plus, followed by the five single-coordinate flips."""

    rows = [[1] * N]
    for index in range(1, N):
        row = [1] * N
        row[index] = -1
        rows.append(row)
    return rows


def symmetric_power_rows(rows: list[list[int]], degree: int) -> list[list[int]]:
    monomials = list(combinations_with_replacement(range(N), degree))
    return [
        [
            product(row[index] for index in monomial)
            for monomial in monomials
        ]
        for row in rows
    ]


def product(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def repeated_cubic_projection(rows: list[list[int]]) -> list[list[int]]:
    """Use the coefficients of e_0^3 and e_0^2 e_r, r=1,...,5."""

    return [[1] + [row[index] for index in range(1, N)] for row in rows]


def audit() -> dict[str, object]:
    rows = sign_rows()
    sign_rank = exact_rank(rows)
    square_rows = symmetric_power_rows(rows, 2)
    cube_rows = symmetric_power_rows(rows, 3)
    square_rank = exact_rank(square_rows)
    cube_rank = exact_rank(cube_rows)
    repeated_rank = exact_rank(repeated_cubic_projection(rows))
    determinant = (-2) ** 5
    if (sign_rank, square_rank, cube_rank, repeated_rank) != (6, 6, 6, 6):
        raise AssertionError((sign_rank, square_rank, cube_rank, repeated_rank))

    column_pair_count = len(list(combinations(range(N), 2)))
    column_triple_count = len(list(combinations(range(N), 3)))
    individual_quadratic_dimension = column_pair_count
    individual_cubic_dimension = column_triple_count
    quadratic_sum_dimension = column_pair_count * square_rank
    common_quotient_dimension = column_pair_count
    quadratic_permanent_intersection = (
        quadratic_sum_dimension - common_quotient_dimension
    )
    cubic_sum_dimension = column_triple_count * cube_rank
    cubic_permanent_intersection = column_triple_count * (6 - repeated_rank)

    if (
        individual_quadratic_dimension,
        individual_cubic_dimension,
        quadratic_sum_dimension,
        common_quotient_dimension,
        quadratic_permanent_intersection,
        cubic_sum_dimension,
        cubic_permanent_intersection,
    ) != (15, 20, 90, 15, 75, 120, 0):
        raise AssertionError("unexpected derivative dimensions")

    return {
        "status": "EXACT_N6_ALPHA3_COMMON_QUOTIENT_COUNTEREXAMPLE",
        "arithmetic": "pure coefficient formulas plus exact integer/QQ ranks",
        "construction": {
            "linear_forms": (
                "ell_(i,c)=sum_(r=0)^5 sigma_(i,r) x_(r,c), "
                "T_i=product_(c=0)^5 ell_(i,c)"
            ),
            "sign_rows": rows,
            "selected_sign_minor_determinant": determinant,
            "exact_QQ_sign_rank": sign_rank,
            "exact_QQ_square_rank": square_rank,
            "exact_QQ_cube_rank": cube_rank,
            "exact_QQ_repeated_cubic_projection_rank": repeated_rank,
        },
        "individual_term_data": {
            "quadratic_derivative_dimension": individual_quadratic_dimension,
            "cubic_derivative_dimension": individual_cubic_dimension,
            "permanent_quadratic_intersection_dimension": 0,
            "epsilon_alpha": [0, 3],
        },
        "coupled_quadratic_data": {
            "six_F_literal_direct": True,
            "d2": quadratic_sum_dimension,
            "common_quotient_W_dimension": common_quotient_dimension,
            "a2": quadratic_permanent_intersection,
            "t2": common_quotient_dimension,
            "pairwise_F_intersection_dimension": 0,
        },
        "coupled_cubic_data": {
            "h": cubic_sum_dimension,
            "b": cubic_permanent_intersection,
            "required_b_in_residual_state": 60,
        },
        "strict_conclusion": (
            "The assertion that two actual epsilon-zero alpha-three Chow "
            "spaces with the same W15 must intersect is false, even for six "
            "literal-direct spaces. Pure quadratic common-quotient geometry "
            "cannot exclude the residual state."
        ),
        "claim_boundary": (
            "The constructed six-term family has b=0, not b=60. It does not "
            "realize the residual fixed-six state, refute its exclusion, or "
            "change the Chow-rank lower bound. It isolates the remaining "
            "obstruction as cubic coupling."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = audit()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(f"quadratic_data={payload['coupled_quadratic_data']}")
    print(f"cubic_data={payload['coupled_cubic_data']}")
    print("N6_ALPHA3_COMMON_QUOTIENT_COUNTEREXAMPLE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
