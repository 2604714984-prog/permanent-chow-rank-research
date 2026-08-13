#!/usr/bin/env python3
"""Exact small regression for N6-070 column-separated rigidity."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


N = 6
DEFAULT_JSON = Path("data/n6_column_separated_common_quotient_rigidity.json")


def exact_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
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


def rho_matrix() -> list[list[int]]:
    """Matrix of tensor -> (diagonal, antisymmetric part)."""

    rows: list[list[int]] = []
    for index in range(N):
        row = [0] * (N * N)
        row[index * N + index] = 1
        rows.append(row)
    for left, right in combinations(range(N), 2):
        row = [0] * (N * N)
        row[left * N + right] = 1
        row[right * N + left] = -1
        rows.append(row)
    return rows


def s0_rows() -> list[list[int]]:
    rows = []
    for left, right in combinations(range(N), 2):
        row = [0] * (N * N)
        row[left * N + right] = 1
        row[right * N + left] = 1
        rows.append(row)
    return rows


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector, strict=True)) for row in matrix]


def tensor(left: tuple[int, ...], right: tuple[int, ...]) -> list[int]:
    return [left[i] * right[j] for i in range(N) for j in range(N)]


def wedge(left: tuple[int, ...], right: tuple[int, ...]) -> list[int]:
    return [
        left[i] * right[j] - left[j] * right[i]
        for i, j in combinations(range(N), 2)
    ]


def tau(left: tuple[int, ...], right: tuple[int, ...]) -> list[int]:
    return [left[i] * right[i] for i in range(N)] + wedge(left, right)


def binary_pair_audit() -> dict[str, int]:
    vectors = [
        values
        for values in product((0, 1), repeat=N)
        if any(values)
    ]
    dependent = 0
    independent = 0
    for left in vectors:
        for right in vectors:
            tau_value = tau(left, right)
            if not any(tau_value):
                raise AssertionError((left, right))
            wedge_zero = not any(wedge(left, right))
            rank_one = exact_rank([list(left), list(right)]) == 1
            if wedge_zero != rank_one:
                raise AssertionError((left, right, wedge_zero, rank_one))
            if rank_one:
                dependent += 1
            else:
                independent += 1
    return {
        "nonzero_binary_vectors": len(vectors),
        "ordered_pairs": len(vectors) ** 2,
        "dependent_pairs": dependent,
        "independent_pairs": independent,
    }


def proportional(left: list[int], right: list[int]) -> bool:
    return exact_rank([left, right]) <= 1


def false_positive_regression() -> dict[str, object]:
    """A pair that passes its diagonal check but fails the full tau check."""

    p0 = (1, 1, 1, 0, 0, 0)
    p1 = (1, 0, 0, 1, 1, 0)
    q0 = (1, 2, 3, 0, 0, 0)
    q1 = (1, 0, 0, 2, 4, 0)
    diagonal_p = tau(p0, p1)[:N]
    diagonal_q = tau(q0, q1)[:N]
    wedge_p = wedge(p0, p1)
    wedge_q = wedge(q0, q1)
    payload = {
        "diagonal_p": diagonal_p,
        "diagonal_q": diagonal_q,
        "diagonal_proportional": proportional(diagonal_p, diagonal_q),
        "wedge_01_p": wedge_p[0],
        "wedge_01_q": wedge_q[0],
        "full_tau_proportional": proportional(tau(p0, p1), tau(q0, q1)),
    }
    if payload != {
        "diagonal_p": [1, 0, 0, 0, 0, 0],
        "diagonal_q": [1, 0, 0, 0, 0, 0],
        "diagonal_proportional": True,
        "wedge_01_p": -1,
        "wedge_01_q": -2,
        "full_tau_proportional": False,
    }:
        raise AssertionError(payload)
    return payload


def add(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(vector[index] for vector in vectors) for index in range(N))


def scale(value: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value * entry for entry in vector)


def branch_regression() -> dict[str, object]:
    basis = [tuple(int(i == j) for i in range(N)) for j in range(N)]
    e0, e1, e2 = basis[:3]

    rank_three_union = exact_rank([list(e0), list(e1), list(e2)])
    rank_three_plane_intersection = 2 + 2 - rank_three_union

    p_rank_two = [e0, e1, e0, e1, add(e0, e1), add(e0, scale(-1, e1))]
    q_rank_two = [
        e1,
        scale(-1, e0),
        e1,
        scale(-1, e0),
        add(scale(-1, e0), e1),
        add(e0, e1),
    ]
    for left, right in zip(p_rank_two, q_rank_two, strict=True):
        if exact_rank([list(left), list(right)]) != 2:
            raise AssertionError((left, right))
    for first, second in combinations(range(N), 2):
        p_pair_rank = exact_rank(
            [list(p_rank_two[first]), list(p_rank_two[second])]
        )
        q_pair_rank = exact_rank(
            [list(q_rank_two[first]), list(q_rank_two[second])]
        )
        if p_pair_rank != q_pair_rank:
            raise AssertionError((first, second, p_pair_rank, q_pair_rank))
        if p_pair_rank == 2:
            union_rank = exact_rank(
                [
                    list(p_rank_two[first]),
                    list(p_rank_two[second]),
                    list(q_rank_two[first]),
                    list(q_rank_two[second]),
                ]
            )
            if union_rank != 2:
                raise AssertionError((first, second, union_rank))

    p_rank_one = [e0] * N
    q_rank_one = [e1] * N
    rank_one_union = exact_rank([list(p_rank_one[0]), list(q_rank_one[0])])

    return {
        "rank_three_pair_plane_intersection_dimension": (
            rank_three_plane_intersection
        ),
        "rank_two_p_family_rank": exact_rank([list(v) for v in p_rank_two]),
        "rank_two_q_family_rank": exact_rank([list(v) for v in q_rank_two]),
        "rank_two_each_coordinate_pair_rank": [
            exact_rank([list(left), list(right)])
            for left, right in zip(p_rank_two, q_rank_two, strict=True)
        ],
        "rank_one_p_family_rank": exact_rank([list(v) for v in p_rank_one]),
        "rank_one_q_family_rank": exact_rank([list(v) for v in q_rank_one]),
        "rank_one_combined_plane_rank": rank_one_union,
    }


def build_payload() -> dict[str, object]:
    rho = rho_matrix()
    s0 = s0_rows()
    rho_rank = exact_rank(rho)
    s0_rank = exact_rank(s0)
    s0_in_kernel = all(not any(matrix_vector(rho, row)) for row in s0)
    binary = binary_pair_audit()
    false_positive = false_positive_regression()
    branches = branch_regression()

    if (rho_rank, N * N - rho_rank, s0_rank, s0_in_kernel) != (
        21,
        15,
        15,
        True,
    ):
        raise AssertionError((rho_rank, s0_rank, s0_in_kernel))
    if binary != {
        "nonzero_binary_vectors": 63,
        "ordered_pairs": 3969,
        "dependent_pairs": 63,
        "independent_pairs": 3906,
    }:
        raise AssertionError(binary)
    if branches != {
        "rank_three_pair_plane_intersection_dimension": 1,
        "rank_two_p_family_rank": 2,
        "rank_two_q_family_rank": 2,
        "rank_two_each_coordinate_pair_rank": [2] * N,
        "rank_one_p_family_rank": 1,
        "rank_one_q_family_rank": 1,
        "rank_one_combined_plane_rank": 2,
    }:
        raise AssertionError(branches)

    return {
        "status": [
            "PURE_COLUMN_SEPARATED_COMMON_QUOTIENT_RIGIDITY",
            "EXACT_QQ_BLOCK_REGRESSION",
            "B50_COMMON_SEPARATION_EXCLUDED",
            "N6-070",
        ],
        "arithmetic": "exact integers and rational elimination; no floating point",
        "regression": {
            "rho_shape": [21, 36],
            "rho_rank": rho_rank,
            "rho_kernel_dimension": N * N - rho_rank,
            "S0_basis_rank": s0_rank,
            "S0_basis_annihilated_by_rho": s0_in_kernel,
            "binary_pair_audit": binary,
            "diagonal_only_false_positive": false_positive,
            "rank_branch_regression": branches,
        },
        "pure_theorem": {
            "common_column_separation_and_common_W_force_P2_tensor_C6": True,
            "transpose_for_common_row_separation": True,
            "b50_pair_triggers_N6_061": True,
            "b50_endpoint_excluded_by_N6_059": True,
        },
        "strict_conclusion": (
            "Two complementary actual frames separated by the same coordinate "
            "columns and sharing one quotient have joint span P2 tensor C6. "
            "At the b=50 endpoint N6-061 and N6-059 exclude such a pair."
        ),
        "claim_boundary": (
            "Common column or row separation is an assumption, not a conclusion "
            "for an arbitrary common-W15 pair. The all-singular nonseparated "
            "layer remains open. The finite replay does not replace the pure "
            "proof, prove ChowRank(perm_6)>=28, or make a border-rank claim."
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
    print("rho_rank=21 kernel_dimension=15")
    print("binary_ordered_pairs=3969")
    print("N6_COLUMN_SEPARATED_COMMON_QUOTIENT_RIGIDITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
