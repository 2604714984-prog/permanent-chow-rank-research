#!/usr/bin/env python3
"""Exact small replay for N6-071 row-block compression ranks."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path


N = 6
EDGES = list(combinations(range(N), 2))
SYM5 = list(combinations_with_replacement(range(5), 2))


def exact_rank(matrix: list[list[Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next(
            (row for row in range(answer, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        value = work[answer][column]
        work[answer] = [entry / value for entry in work[answer]]
        for row in range(answer + 1, len(work)):
            scale = work[row][column]
            if scale:
                work[row] = [
                    entry - scale * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[answer], strict=True)
                ]
        answer += 1
    return answer


def quotient_matrix(kernel: list[int]) -> list[list[Fraction]]:
    """A 5-by-6 quotient map with the displayed kernel vector."""

    if kernel[-1] == 0:
        raise ValueError("the replay places a nonzero kernel coordinate last")
    matrix = [[Fraction(0) for _ in range(N)] for _ in range(5)]
    for index in range(5):
        matrix[index][index] = 1
        matrix[index][5] = -Fraction(kernel[index], kernel[5])
    return matrix


def transpose(matrix):
    return [list(column) for column in zip(*matrix, strict=True)]


def matmul(left, right):
    return [
        [
            sum(left[row][middle] * right[middle][column]
                for middle in range(len(right)))
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def edge_tensor(edge):
    matrix = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    left, right = edge
    matrix[left][right] = matrix[right][left] = 1
    return matrix


def compression_matrix(quotient):
    columns = []
    for edge in EDGES:
        compressed = matmul(matmul(quotient, edge_tensor(edge)), transpose(quotient))
        columns.append([compressed[i][j] for i, j in SYM5])
    return transpose(columns)


def rank_profile() -> list[dict[str, object]]:
    rows = []
    for zero_count in range(6):
        kernel = [0] * zero_count + [1] * (N - zero_count)
        quotient = quotient_matrix(kernel)
        compression_rank = exact_rank(compression_matrix(quotient))
        expected = 15 - zero_count
        if exact_rank(quotient) != 5 or compression_rank != expected:
            raise AssertionError((zero_count, compression_rank, expected))
        rows.append(
            {
                "kernel_zero_count": zero_count,
                "kernel_representative": kernel,
                "row_block_rank": 5,
                "exact_compression_rank": compression_rank,
                "formula_rank": expected,
            }
        )
    return rows


def build_payload() -> dict[str, object]:
    return {
        "status": [
            "PURE_SIX_COLOR_ROW_RANK_SYNCHRONIZATION",
            "EXACT_QQ_RANK_FORMULA_REGRESSION",
            "N6-071",
        ],
        "rank_five_kernel_support_replay": rank_profile(),
        "pure_conclusion": (
            "For each ambient row r, the six maps mu_(i,r) factor as "
            "theta_r composed with the six isomorphisms S0->W. Therefore their "
            "ranks and images are common. In the all-singular layer, one rank-five "
            "block with full-support kernel forces all six blocks in that row to "
            "have rank five, full-support kernels, and one common five-dimensional "
            "image plane. The transposed statement holds for ambient columns."
        ),
        "directness_reformulation": (
            "With section lifts s_i:W->F_i and delta_i=s_i-s_1, literal "
            "directness of the six F_i is equivalent to injectivity of "
            "Delta=(delta_2,...,delta_6):W^5->E2; its image is K75."
        ),
        "claim_boundary": (
            "Every same-row projection annihilates E2, so it also annihilates "
            "all delta_i. Thus six-color directness supplies no additional "
            "single-row equation capable of removing the local rank-five "
            "Cremona freedom in G-050. The theorem does not exclude the "
            "all-singular layer or the b=50 endpoint, prove lower 28, or make a "
            "border-rank claim. A further argument must combine distinct-row or "
            "distinct-column blocks using the full permanent quotient, or use "
            "the global K75 shadow geometry."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError(arguments.verify_json)
    print(rendered, end="")


if __name__ == "__main__":
    main()
