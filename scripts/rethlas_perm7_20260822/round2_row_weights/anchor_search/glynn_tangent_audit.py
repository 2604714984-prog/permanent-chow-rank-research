#!/usr/bin/env python3
r"""Exact small-n audit of row-weight cancellation at the Glynn packet.

For each n, the 2^(n-1) Glynn tensors are v_epsilon^{\otimes n}, where
epsilon_0=1.  We form an independent basis of each affine Segre tangent
space, split tensor coordinates into permutations and non-permutations, and
compute exact rational ranks.  No finite-field inference is used.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path


def glynn_signs(n: int):
    for tail in itertools.product((-1, 1), repeat=n - 1):
        yield (1,) + tail


def tensor_entries(vectors):
    """Return coordinates of v_0 tensor ... tensor v_(n-1)."""
    n = len(vectors)
    for idx in itertools.product(range(n), repeat=n):
        value = 1
        for mode, row in enumerate(idx):
            value *= vectors[mode][row]
        yield idx, value


def tangent_columns(n: int):
    """Independent columns for the direct sum of Glynn Segre tangents.

    Since every sign vector v has v[0]=1, {v,e_1,...,e_(n-1)} is a basis.
    A tangent basis is v^tensor n and, for each mode, the tensors obtained by
    replacing v in that mode by e_i (1 <= i < n).
    """
    columns = []
    labels = []
    for eps in glynn_signs(n):
        base_vectors = [eps] * n
        columns.append(dict(tensor_entries(base_vectors)))
        labels.append((eps, "scale", -1, -1))
        for mode in range(n):
            for row in range(1, n):
                unit = tuple(int(i == row) for i in range(n))
                vectors = list(base_vectors)
                vectors[mode] = unit
                columns.append(dict(tensor_entries(vectors)))
                labels.append((eps, "vary", mode, row))
    return columns, labels


def echelon_over_q(columns, rows):
    """Exact sparse integer echelon form over Q."""
    # Row dictionaries are much sparser than the rectangular dense matrix.
    matrix = []
    for row in rows:
        sparse = {j: column.get(row, 0) for j, column in enumerate(columns)
                  if column.get(row, 0)}
        matrix.append(sparse)

    rank = 0
    pivot_columns = []
    ncols = len(columns)
    for col in range(ncols):
        candidates = [i for i in range(rank, len(matrix)) if col in matrix[i]]
        if not candidates:
            continue
        pivot_index = min(candidates, key=lambda i: abs(matrix[i][col]))
        matrix[rank], matrix[pivot_index] = matrix[pivot_index], matrix[rank]
        pivot_row = matrix[rank]
        pivot = pivot_row[col]
        for i in range(rank + 1, len(matrix)):
            row = matrix[i]
            coefficient = row.get(col, 0)
            if not coefficient:
                continue
            keys = set(row) | set(pivot_row)
            new_row = {
                j: pivot * row.get(j, 0) - coefficient * pivot_row.get(j, 0)
                for j in keys if j > col
            }
            new_row = {j: value for j, value in new_row.items() if value}
            if new_row:
                divisor = 0
                for value in new_row.values():
                    divisor = math.gcd(divisor, abs(value))
                if divisor > 1:
                    new_row = {j: value // divisor for j, value in new_row.items()}
                first = min(new_row)
                if new_row[first] < 0:
                    new_row = {j: -value for j, value in new_row.items()}
            matrix[i] = new_row
        rank += 1
        pivot_columns.append(col)
        if rank == len(matrix):
            break
    return matrix[:rank], pivot_columns


def rank_over_q(columns, rows):
    return len(echelon_over_q(columns, rows)[1])


def rank_mod_prime(columns, rows, prime):
    """Independent modular row elimination used only as a replay check."""
    matrix = []
    for coordinate in rows:
        row = {
            j: column.get(coordinate, 0) % prime
            for j, column in enumerate(columns)
            if column.get(coordinate, 0) % prime
        }
        matrix.append(row)
    rank = 0
    for col in range(len(columns)):
        pivot_index = next(
            (i for i in range(rank, len(matrix)) if matrix[i].get(col, 0)),
            None,
        )
        if pivot_index is None:
            continue
        matrix[rank], matrix[pivot_index] = matrix[pivot_index], matrix[rank]
        pivot_row = matrix[rank]
        inverse = pow(pivot_row[col], -1, prime)
        pivot_row = {j: value * inverse % prime for j, value in pivot_row.items()}
        matrix[rank] = pivot_row
        for i in range(rank + 1, len(matrix)):
            coefficient = matrix[i].get(col, 0)
            if not coefficient:
                continue
            keys = set(matrix[i]) | set(pivot_row)
            matrix[i] = {
                j: (matrix[i].get(j, 0) - coefficient * pivot_row.get(j, 0)) % prime
                for j in keys if j > col
            }
            matrix[i] = {j: value for j, value in matrix[i].items() if value}
        rank += 1
        if rank == len(matrix):
            break
    return rank


def primitive_integer_vector(vector):
    denominator = 1
    for value in vector:
        denominator = math.lcm(denominator, value.denominator)
    integers = [value.numerator * (denominator // value.denominator)
                for value in vector]
    divisor = 0
    for value in integers:
        divisor = math.gcd(divisor, abs(value))
    if divisor:
        integers = [value // divisor for value in integers]
    for value in integers:
        if value:
            if value < 0:
                integers = [-entry for entry in integers]
            break
    return integers


def nullspace_over_q(columns, rows):
    echelon, pivots = echelon_over_q(columns, rows)
    free = [j for j in range(len(columns)) if j not in set(pivots)]
    basis = []
    for free_col in free:
        vector = [Fraction(0) for _ in columns]
        vector[free_col] = Fraction(1)
        for row, pivot_col in zip(reversed(echelon), reversed(pivots)):
            tail = sum(Fraction(value) * vector[j]
                       for j, value in row.items() if j > pivot_col)
            vector[pivot_col] = -tail / row[pivot_col]
        basis.append(primitive_integer_vector(vector))
    return basis


def audit(n: int):
    all_rows = list(itertools.product(range(n), repeat=n))
    perm_rows = [row for row in all_rows if len(set(row)) == n]
    off_rows = [row for row in all_rows if len(set(row)) < n]
    columns, labels = tangent_columns(n)
    rank_full = rank_over_q(columns, all_rows)
    rank_off = rank_over_q(columns, off_rows)
    rank_target = rank_over_q(columns, perm_rows)
    modular_replays = {}
    for prime in (1000003, 1000033):
        replay = {
            "full": rank_mod_prime(columns, all_rows, prime),
            "off": rank_mod_prime(columns, off_rows, prime),
            "target": rank_mod_prime(columns, perm_rows, prime),
        }
        assert replay == {
            "full": rank_full,
            "off": rank_off,
            "target": rank_target,
        }
        modular_replays[str(prime)] = replay
    domain_dim = len(columns)
    target_motion = rank_full - rank_off
    nullspace = nullspace_over_q(columns, all_rows)

    expected_target_motion = (n - 1) ** 2 + 1
    expected_term_tangent = n * (n - 1) + 1
    assert domain_dim == (2 ** (n - 1)) * expected_term_tangent
    assert len(perm_rows) == math.factorial(n)
    assert rank_target == expected_target_motion
    assert target_motion == expected_target_motion
    assert len(nullspace) == domain_dim - rank_full

    compact_relations = []
    for relation in nullspace:
        compact_relations.append([
            {
                "coefficient": coefficient,
                "epsilon": list(labels[j][0]),
                "kind": labels[j][1],
                "mode": labels[j][2],
                "row": labels[j][3],
            }
            for j, coefficient in enumerate(relation) if coefficient
        ])

    return {
        "n": n,
        "terms": 2 ** (n - 1),
        "ambient_dimension": n**n,
        "permutation_coordinate_dimension": math.factorial(n),
        "offweight_coordinate_dimension": n**n - math.factorial(n),
        "one_term_tangent_dimension": expected_term_tangent,
        "direct_sum_tangent_dimension": domain_dim,
        "rank_full_jacobian": rank_full,
        "rank_offweight_jacobian": rank_off,
        "rank_target_restriction": rank_target,
        "kernel_full_jacobian_dimension": domain_dim - rank_full,
        "kernel_offweight_jacobian_dimension": domain_dim - rank_off,
        "compatible_target_motion_dimension": target_motion,
        "expected_coordinate_torus_motion_dimension": expected_target_motion,
        "full_zero_tangent_relations": compact_relations,
        "independent_modular_replays": modular_replays,
        "checks": {
            "target_motion_equals_full_minus_off_rank": True,
            "target_motion_is_exactly_coordinate_torus_tangent": True,
            "all_ranks_over_Q": True,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=4)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if not 2 <= args.max_n <= 5:
        raise SystemExit("exact audit supports 2 <= max-n <= 5")
    payload = [audit(n) for n in range(2, args.max_n + 1)]
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("GLYNN_TANGENT_AUDIT_PASS")


if __name__ == "__main__":
    main()
