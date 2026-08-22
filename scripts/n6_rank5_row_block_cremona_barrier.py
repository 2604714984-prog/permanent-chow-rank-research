#!/usr/bin/env python3
"""Exact rational replay for the G-050 rank-five row-block barrier."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path


N = 6
EDGES = list(combinations(range(N), 2))
SYM5 = list(combinations_with_replacement(range(5), 2))


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix):
    return [list(column) for column in zip(*matrix, strict=True)]


def determinant(matrix) -> Fraction:
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = Fraction(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column])
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        value = work[column][column]
        answer *= value
        work[column] = [entry / value for entry in work[column]]
        for row in range(column + 1, len(work)):
            scale = work[row][column]
            if scale:
                work[row] = [
                    entry - scale * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[column], strict=True)
                ]
    return answer


def inverse(matrix):
    size = len(matrix)
    work = [
        [Fraction(value) for value in row]
        + [Fraction(int(i == j)) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    entry - scale * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[column], strict=True)
                ]
    return [row[size:] for row in work]


def rank(matrix) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = 0
    for column in range(len(work[0])):
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


def compression(kernel):
    """A rank-five 6-by-6 matrix with the displayed full-support kernel."""

    matrix = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for index in range(5):
        matrix[index][index] = 1
        matrix[index][5] = -Fraction(kernel[index], kernel[5])
    return matrix


def edge_tensor(edge):
    matrix = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    i, j = edge
    matrix[i][j] = matrix[j][i] = 1
    return matrix


def mu_matrix(compression_matrix):
    columns = []
    for edge in EDGES:
        image = matmul(
            matmul(compression_matrix, edge_tensor(edge)),
            transpose(compression_matrix),
        )
        columns.append([image[i][j] for i, j in SYM5])
    return transpose(columns)


def rendered_fraction(value: Fraction):
    return value.numerator if value.denominator == 1 else str(value)


def edge_image(matrix, edge):
    column = EDGES.index(edge)
    return [
        {"edge": list(target), "coefficient": rendered_fraction(matrix[row][column])}
        for row, target in enumerate(EDGES)
        if matrix[row][column]
    ]


def linear_combination(coefficients, matrices):
    return [
        [
            sum(coefficient * matrix[i][j]
                for coefficient, matrix in zip(coefficients, matrices, strict=True))
            for j in range(N)
        ]
        for i in range(N)
    ]


def anchor_row_system(compression_a, compression_b, phi):
    """Full diagonal-plus-wedge equations for one further row-block pair.

    The 72 variables are the row-major entries of ``C`` followed by those of
    ``D``.  For every edge tensor ``Z``, the matrix

        A Z C^T - B phi(Z) D^T

    must have zero diagonal and be symmetric.  Thus there are
    15 * (6 + 15) = 315 scalar equations.
    """

    edge_tensors = [edge_tensor(edge) for edge in EDGES]
    rows = []
    for source_column, z_matrix in enumerate(edge_tensors):
        phi_z = linear_combination(
            [phi[target_column][source_column] for target_column in range(15)],
            edge_tensors,
        )
        az = matmul(compression_a, z_matrix)
        bphi_z = matmul(compression_b, phi_z)

        for i in range(N):
            equation = [Fraction(0) for _ in range(72)]
            for column in range(N):
                equation[N * i + column] = az[i][column]
                equation[36 + N * i + column] = -bphi_z[i][column]
            rows.append(equation)

        for i, j in combinations(range(N), 2):
            equation = [Fraction(0) for _ in range(72)]
            for column in range(N):
                equation[N * j + column] += az[i][column]
                equation[N * i + column] -= az[j][column]
                equation[36 + N * j + column] -= bphi_z[i][column]
                equation[36 + N * i + column] += bphi_z[j][column]
            rows.append(equation)
    return rows


def factorized_kernel_basis(compression_a, compression_b):
    """Columns encoding (C,D)=(T A,T B), for T in Mat_{6 by 5}."""

    columns = []
    for target_row in range(N):
        for source_row in range(5):
            vector = [Fraction(0) for _ in range(72)]
            for column in range(N):
                vector[N * target_row + column] = compression_a[source_row][column]
                vector[36 + N * target_row + column] = compression_b[source_row][column]
            columns.append(vector)
    return transpose(columns)


def build_payload() -> dict[str, object]:
    kernel_a = [1, 1, 1, 1, 1, 1]
    kernel_b = [1, 2, 3, 4, 5, 6]
    compression_a = compression(kernel_a)
    compression_b = compression(kernel_b)
    mu_a = mu_matrix(compression_a)
    mu_b = mu_matrix(compression_b)
    determinant_a = determinant(mu_a)
    determinant_b = determinant(mu_b)
    phi = matmul(inverse(mu_b), mu_a)
    cross_row_system = anchor_row_system(compression_a, compression_b, phi)
    factorized_kernel = factorized_kernel_basis(compression_a, compression_b)
    system_rank = rank(cross_row_system)
    kernel_basis_rank = rank(factorized_kernel)
    kernel_residual_rank = rank(matmul(cross_row_system, factorized_kernel))
    expected_edge_image = [
        {"edge": [0, 1], "coefficient": 1},
        {"edge": [0, 2], "coefficient": 2},
        {"edge": [0, 3], "coefficient": 3},
        {"edge": [0, 4], "coefficient": 4},
        {"edge": [0, 5], "coefficient": 6},
    ]
    if rank(compression_a) != 5 or rank(compression_b) != 5:
        raise AssertionError("compression rank")
    if (determinant_a, determinant_b) != (Fraction(-32), Fraction(-40, 81)):
        raise AssertionError((determinant_a, determinant_b))
    if edge_image(phi, (0, 5)) != expected_edge_image:
        raise AssertionError(edge_image(phi, (0, 5)))
    fixed_edges = [edge for edge in EDGES if edge[1] < 5]
    if any(edge_image(phi, edge) != [{"edge": list(edge), "coefficient": 1}]
           for edge in fixed_edges):
        raise AssertionError("unexpected fixed edge")
    if (len(cross_row_system), len(cross_row_system[0])) != (315, 72):
        raise AssertionError("cross-row system shape")
    if (system_rank, kernel_basis_rank, kernel_residual_rank) != (42, 30, 0):
        raise AssertionError(
            (system_rank, kernel_basis_rank, kernel_residual_rank)
        )
    return {
        "status": [
            "PURE_RANK5_FULL_SUPPORT_COMMON_IMAGE_LEMMA",
            "EXACT_QQ_LOCAL_CREMONA_BARRIER",
            "EXACT_QQ_EXPLICIT_CROSS_ROW_NONEXTENSION",
            "G-050",
        ],
        "pure_lemma": {
            "kernel_formula": (
                "ker(mu_A)={a*b^T+b*a^T : b_i=0 whenever a_i!=0}"
            ),
            "rank_formula": "rank(mu_A)=15-number_of_zero_coordinates(a)",
            "full_support_conclusion": (
                "If A and B are singular row blocks, rank(A)=5, ker(A) has "
                "full coordinate support, and A Z A^T=B phi(Z) B^T for every "
                "Z in S0 with phi invertible, then rank(B)=5, ker(B) has full "
                "coordinate support, and im(A)=im(B)."
            ),
        },
        "exact_local_barrier": {
            "kernel_a": kernel_a,
            "kernel_b": kernel_b,
            "compression_a": [
                [rendered_fraction(value) for value in row] for row in compression_a
            ],
            "compression_b": [
                [rendered_fraction(value) for value in row] for row in compression_b
            ],
            "rank_a": 5,
            "rank_b": 5,
            "determinant_mu_a": rendered_fraction(determinant_a),
            "determinant_mu_b": rendered_fraction(determinant_b),
            "phi_definition": "phi=mu_B^{-1} mu_A",
            "fixed_edge_count": len(fixed_edges),
            "phi_F05": edge_image(phi, (0, 5)),
            "not_monomial_congruence_reason": (
                "A congruence preserving S0 is monomial and therefore sends "
                "each edge line to one edge line, whereas phi(F05) has five "
                "nonzero edge components."
            ),
            "full_cross_row_extension": {
                "system_definition": (
                    "For one further row-block pair (C,D), impose zero diagonal "
                    "and zero skew part on A Z C^T-B phi(Z) D^T for all 15 edge "
                    "basis tensors Z."
                ),
                "system_shape": [315, 72],
                "system_rank_over_Q": system_rank,
                "system_nullity": 72 - system_rank,
                "displayed_kernel_basis": "(C,D)=(T A,T B), T in Mat_{6 by 5}",
                "displayed_kernel_rank_over_Q": kernel_basis_rank,
                "system_times_displayed_kernel_rank_over_Q": kernel_residual_rank,
                "strict_conclusion": (
                    "For this explicit A, B, and phi, every further row block "
                    "factors as (C,D)=(T A,T B). Stacking all six row blocks "
                    "therefore gives rank(X)<=5 and rank(Y)<=5, so this local "
                    "Cremona identity cannot extend to an actual injective pair."
                ),
            },
        },
        "claim_boundary": (
            "The nonextension certificate is specific to the displayed rational "
            "A, B, and phi; it is not a theorem for every rank-five full-support "
            "anchor. It excludes this local Cremona identity from an actual "
            "common-W15 pair, but does not exclude the general all-singular "
            "rank-five layer or the b=50 endpoint, prove ChowRank(perm_6)>=28, "
            "or make a border-rank claim. The certificate retains both diagonal "
            "and wedge axes and does not contradict N6-069."
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
