#!/usr/bin/env python3
"""Exact small regression for N6-069 common-row-block rigidity."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


N = 6
DEFAULT_JSON = Path("data/n6_common_row_block_rigidity.json")


def exact_rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
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


def s0_basis() -> list[list[list[int]]]:
    basis = []
    for left, right in combinations(range(N), 2):
        matrix = [[0] * N for _ in range(N)]
        matrix[left][right] = 1
        matrix[right][left] = 1
        basis.append(matrix)
    return basis


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [
            sum(left[row][index] * right[index][column] for index in range(N))
            for column in range(N)
        ]
        for row in range(N)
    ]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(column) for column in zip(*matrix, strict=True)]


def linear_system(kind: str) -> list[list[int]]:
    """Equations on a 6 by 6 unknown matrix for the three proof lemmas."""

    rows: list[list[int]] = []
    for z in s0_basis():
        if kind in {"commutant", "anti_commutant"}:
            sign = -1 if kind == "commutant" else 1
            for output_row in range(N):
                for output_column in range(N):
                    equation = [0] * (N * N)
                    for index in range(N):
                        equation[output_row * N + index] += z[index][output_column]
                        equation[output_column * N + index] += (
                            sign * z[output_row][index]
                        )
                    rows.append(equation)
        elif kind == "left_multiplier":
            for output_row in range(N):
                equation = [0] * (N * N)
                for index in range(N):
                    equation[output_row * N + index] += z[index][output_row]
                rows.append(equation)
            for output_row, output_column in combinations(range(N), 2):
                equation = [0] * (N * N)
                for index in range(N):
                    equation[output_row * N + index] += z[index][output_column]
                    equation[output_column * N + index] -= z[index][output_row]
                rows.append(equation)
        else:
            raise ValueError(kind)
    return rows


def monomial_normalizer_sample() -> dict[str, object]:
    permutation = [2, 0, 5, 1, 4, 3]
    scales = [1, -2, 3, -4, 5, -6]
    matrix = [[0] * N for _ in range(N)]
    for column, row in enumerate(permutation):
        matrix[row][column] = scales[column]

    images = []
    for z in s0_basis():
        image = multiply(multiply(matrix, z), transpose(matrix))
        if any(image[index][index] for index in range(N)):
            raise AssertionError("monomial congruence created a diagonal entry")
        if image != transpose(image):
            raise AssertionError("monomial congruence broke symmetry")
        images.append(
            [image[left][right] for left, right in combinations(range(N), 2)]
        )

    return {
        "permutation": permutation,
        "scales": scales,
        "image_rank": exact_rank(images),
        "preserves_S0": exact_rank(images) == len(s0_basis()),
    }


def build_payload() -> dict[str, object]:
    ranks = {
        "TZ_equals_ZT_transpose": exact_rank(linear_system("commutant")),
        "RZ_plus_ZR_transpose": exact_rank(linear_system("anti_commutant")),
        "CZ_in_S0": exact_rank(linear_system("left_multiplier")),
    }
    sample = monomial_normalizer_sample()
    if ranks != {
        "TZ_equals_ZT_transpose": 35,
        "RZ_plus_ZR_transpose": 36,
        "CZ_in_S0": 35,
    }:
        raise AssertionError(ranks)
    if sample["image_rank"] != 15 or not sample["preserves_S0"]:
        raise AssertionError(sample)

    return {
        "status": [
            "PURE_COMMON_ROW_BLOCK_RIGIDITY",
            "EXACT_QQ_LINEAR_ALGEBRA_REGRESSION",
            "B50_INVERTIBLE_BLOCK_EXCLUDED",
            "N6-069",
        ],
        "arithmetic": "exact integers and rational elimination; no floating point",
        "regression": {
            "dimension_S0": 15,
            "unknown_matrix_dimension": 36,
            "linear_system_ranks": ranks,
            "linear_system_nullities": {
                "TZ_equals_ZT_transpose": 1,
                "RZ_plus_ZR_transpose": 0,
                "CZ_in_S0": 1,
            },
            "monomial_normalizer_sample": sample,
        },
        "pure_theorem": {
            "one_invertible_row_block_forces_both_blocks_invertible": True,
            "actual_pair_forced_to_common_coordinate_column_separation": True,
            "transpose_forces_common_coordinate_row_separation": True,
            "b50_propagates_by_N6_061_and_is_excluded_by_N6_059": True,
            "survivor_all_row_and_column_blocks_singular": True,
        },
        "strict_conclusion": (
            "At the b=50 common-W15 endpoint, any actual pair with one "
            "invertible row or column block is forced into common coordinate "
            "separation; propagation and N6-059 exclude that endpoint branch."
        ),
        "claim_boundary": (
            "The all-row-block-singular and all-column-block-singular layer "
            "remains open. The replay checks only three elementary matrix "
            "lemmas and one monomial sample; the arbitrary theorem is pure. "
            "This does not prove ChowRank(perm_6)>=28 and makes no border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise AssertionError(args.verify_json)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print("linear_system_ranks=35,36,35")
    print("monomial_normalizer_image_rank=15")
    print("N6_COMMON_ROW_BLOCK_RIGIDITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

