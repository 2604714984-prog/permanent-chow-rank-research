#!/usr/bin/env python3
"""Exact small regression for the pure N6-061 transverse-pair theorem."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


N = 6
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_two_row_transverse_rigidity.json"


Matrix = list[list[Fraction]]


def zero_matrix() -> Matrix:
    return [[Fraction(0) for _ in range(N)] for _ in range(N)]


def identity_matrix() -> Matrix:
    answer = zero_matrix()
    for index in range(N):
        answer[index][index] = Fraction(1)
    return answer


def edge_matrix(i: int, j: int) -> Matrix:
    answer = zero_matrix()
    answer[i][j] = answer[j][i] = Fraction(1)
    return answer


def s0_basis() -> list[Matrix]:
    return [edge_matrix(i, j) for i, j in combinations(range(N), 2)]


def flatten(matrix: Matrix) -> list[Fraction]:
    return [entry for row in matrix for entry in row]


def transpose(matrix: Matrix) -> Matrix:
    return [[matrix[j][i] for j in range(N)] for i in range(N)]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(N)), Fraction(0))
            for j in range(N)
        ]
        for i in range(N)
    ]


def exact_rank(rows: list[list[Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            coefficient = work[row][column]
            work[row] = [
                value - coefficient * pivot_value
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def inverse(matrix: Matrix) -> Matrix:
    work = [row[:] + identity for row, identity in zip(matrix, identity_matrix())]
    rank = 0
    for column in range(N):
        pivot = next((row for row in range(rank, N) if work[row][column]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(N):
            if row == rank or not work[row][column]:
                continue
            coefficient = work[row][column]
            work[row] = [
                value - coefficient * pivot_value
                for value, pivot_value in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
    return [row[N:] for row in work]


def determinant(matrix: Matrix) -> Fraction:
    work = [row[:] for row in matrix]
    answer = Fraction(1)
    for column in range(N):
        pivot = next((row for row in range(column, N) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        scale = work[column][column]
        answer *= scale
        for row in range(column + 1, N):
            if not work[row][column]:
                continue
            coefficient = work[row][column] / scale
            for entry in range(column, N):
                work[row][entry] -= coefficient * work[column][entry]
    return answer


def scalar_multiplier_constraint_rank() -> int:
    """Rank of the equations XB symmetric zero-diagonal for every B in S0."""

    equations: list[list[Fraction]] = []
    for basis_matrix in s0_basis():
        # Diagonal equations for XB.
        for i in range(N):
            row = [Fraction(0) for _ in range(N * N)]
            for k in range(N):
                row[i * N + k] += basis_matrix[k][i]
            equations.append(row)
        # Symmetry equations (XB)_ij-(XB)_ji.
        for i, j in combinations(range(N), 2):
            row = [Fraction(0) for _ in range(N * N)]
            for k in range(N):
                row[i * N + k] += basis_matrix[k][j]
                row[j * N + k] -= basis_matrix[k][i]
            equations.append(row)
    return exact_rank(equations)


def s0_action_rank(support_size: int) -> int:
    z = [Fraction(int(index < support_size)) for index in range(N)]
    images = []
    for basis_matrix in s0_basis():
        images.append(
            [
                sum(
                    (basis_matrix[i][j] * z[j] for j in range(N)), Fraction(0)
                )
                for i in range(N)
            ]
        )
    return exact_rank(images)


def matching_matrix() -> Matrix:
    answer = zero_matrix()
    for i, j in ((0, 1), (2, 3), (4, 5)):
        answer[i][j] = answer[j][i] = Fraction(1)
    return answer


def dense_matrix() -> Matrix:
    answer = zero_matrix()
    for i, j in combinations(range(N), 2):
        answer[i][j] = answer[j][i] = Fraction(1)
    return answer


def algebra_dimension(b0: Matrix) -> int:
    inverse_b0 = inverse(b0)
    generators = [multiply(basis_matrix, inverse_b0) for basis_matrix in s0_basis()]
    basis = [identity_matrix()]
    basis_rank = 1
    cursor = 0
    while cursor < len(basis):
        left = basis[cursor]
        cursor += 1
        for generator in generators:
            product = multiply(left, generator)
            candidate_rows = [flatten(matrix) for matrix in basis] + [flatten(product)]
            candidate_rank = exact_rank(candidate_rows)
            if candidate_rank > basis_rank:
                basis.append(product)
                basis_rank = candidate_rank
                if basis_rank == N * N:
                    return basis_rank
    return basis_rank


def disjoint_nonempty_column_supports() -> dict[str, object]:
    """Enumerate labelled pairwise-disjoint supports on six columns.

    Assign each column to one of six factors or leave it unused.  Requiring
    every factor to occur is equivalent to six nonempty pairwise-disjoint
    support sets.
    """

    valid = 0
    profiles: set[tuple[int, ...]] = set()
    for assignment in product(range(N + 1), repeat=N):
        sizes = tuple(assignment.count(factor) for factor in range(N))
        if all(sizes):
            valid += 1
            profiles.add(tuple(sorted(sizes)))
    return {
        "labelled_assignments": valid,
        "support_size_profiles": [list(profile) for profile in sorted(profiles)],
    }


def build_payload() -> dict[str, object]:
    constraint_rank = scalar_multiplier_constraint_rank()
    action_ranks = [s0_action_rank(size) for size in range(1, N + 1)]
    samples = {
        "perfect_matching": matching_matrix(),
        "dense_off_diagonal": dense_matrix(),
    }
    sample_data = {}
    for name, matrix in samples.items():
        sample_data[name] = {
            "determinant": int(determinant(matrix)),
            "generated_algebra_dimension": algebra_dimension(matrix),
        }
    support_data = disjoint_nonempty_column_supports()

    assert constraint_rank == 35
    assert action_ranks == [5, 5, 6, 6, 6, 6]
    assert all(item["determinant"] != 0 for item in sample_data.values())
    assert all(
        item["generated_algebra_dimension"] == 36 for item in sample_data.values()
    )
    assert support_data == {
        "labelled_assignments": 720,
        "support_size_profiles": [[1, 1, 1, 1, 1, 1]],
    }

    return {
        "status": [
            "PURE_TRANSVERSE_PAIR_RIGIDITY_THEOREM",
            "EXACT_QQ_LINEAR_ALGEBRA_REGRESSION",
            "B50_TRANSVERSE_PAIR_EXCLUDED",
            "N6-061",
        ],
        "arithmetic": "exact integers and fractions; no floating point",
        "regression": {
            "dimension_S0": 15,
            "scalar_multiplier_equation_rank": constraint_rank,
            "scalar_multiplier_solution_dimension": 36 - constraint_rank,
            "S0_action_rank_by_support_size_1_through_6": action_ranks,
            "sample_invertible_B0_checks": sample_data,
            "six_disjoint_nonempty_column_supports": support_data,
        },
        "pure_theorem": {
            "shadow_dimension": 12,
            "section_difference_dimension": 15,
            "full_row_pair_projection_implies_tensor_plane": True,
            "actual_pair_implies_common_column_separation": True,
            "full_column_pair_projection_implies_tensor_plane": True,
            "actual_pair_implies_common_row_separation": True,
            "b50_one_transverse_pair_propagates_to_all_six_terms": True,
            "b50_one_transverse_pair_excluded_by_N6_059": True,
            "arbitrary_invertible_B0_algebra": "proved by direct irreducibility plus Burnside",
        },
        "strict_conclusion": (
            "An actual fifteen-dimensional Chow section-difference pair whose "
            "twelve-dimensional shadow projects isomorphically to two complete "
            "rows is column-separated; the transposed statement gives row "
            "separation for projection to two complete columns. At the b=50 "
            "endpoint, one transverse pair propagates separation to all six "
            "terms and N6-059 excludes the configuration."
        ),
        "claim_boundary": (
            "The theorem excludes only actual pairs having a full-rank projection "
            "to some complete row pair or complete column pair. At the b=50 "
            "endpoint one such pair propagates separation to all six terms and "
            "is excluded using N6-059. The closed locus where every projection "
            "of every term pair is singular remains open. It does not prove "
            "ChowRank(perm_6)>=28 or make "
            "a border-rank claim. The two B0 calculations are regression samples; "
            "the arbitrary-B0 statement is proved purely, not by enumeration."
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
    print("scalar_multiplier_solution_dimension=1")
    print("sample_generated_algebra_dimensions=36,36")
    print("N6_TWO_ROW_TRANSVERSE_RIGIDITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
