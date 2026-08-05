#!/usr/bin/env python3
"""Exact audit for the ``n=6`` one-defect Glynn sign family.

The family consists of normalized column-oriented sign products in which five
columns use one sign vector and at most one column uses a second sign vector.
The companion proof shows that every such expression of ``perm_6`` needs at
least 32 nonzero summands; Glynn supplies 32. The script replays the finite
interfaces of that proof with integer arithmetic:

* the 32 normalized sign vectors span the six-dimensional row space;
* the 32 parity fibers of ``{0,...,5}^6`` and their additive-feature ranks;
* exact integer minors for the six Hamming-weight representatives;
* the resulting one-defect span dimension 987; and
* the 32-term Glynn coefficient identity on all ``6^6`` assignments.

No finite-field equality is promoted without an integer upper/lower argument.
The modular elimination only selects candidate minors; Bareiss determinants
certify them over ``Z`` and characteristic zero.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from typing import Iterable

N = 6
BITS = N - 1
GROUP_SIZE = 1 << BITS
TARGET_PARITY = GROUP_SIZE - 1
PRIME = 1_000_003

Assignment = tuple[int, ...]


def character(left: int, right: int) -> int:
    return -1 if (left & right).bit_count() & 1 else 1


def sign_vector(label: int) -> tuple[int, ...]:
    return (1,) + tuple(
        -1 if (label >> (row - 1)) & 1 else 1
        for row in range(1, N)
    )


def row_character(row: int) -> int:
    return 0 if row == 0 else 1 << (row - 1)


def assignment_parity(assignment: Assignment) -> int:
    parity = 0
    for row in assignment:
        parity ^= row_character(row)
    return parity


def all_parity_fibers() -> dict[int, list[Assignment]]:
    fibers: dict[int, list[Assignment]] = defaultdict(list)
    for assignment in product(range(N), repeat=N):
        fibers[assignment_parity(assignment)].append(assignment)
    if sum(map(len, fibers.values())) != N**N:
        raise AssertionError("parity fibers do not partition the ambient basis")
    return dict(fibers)


def additive_feature_row(assignment: Assignment) -> list[int]:
    row = [0] * (N * N)
    for position, value in enumerate(assignment):
        row[N * position + value] = 1
    return row


def additive_feature_matrix(assignments: Iterable[Assignment]) -> list[list[int]]:
    return [additive_feature_row(assignment) for assignment in assignments]


def pivot_minor_mod(
    matrix: list[list[int]],
    prime: int = PRIME,
) -> tuple[int, list[int], list[int]]:
    if not matrix:
        return 0, [], []
    data = [[value % prime for value in row] for row in matrix]
    row_ids = list(range(len(data)))
    columns = len(data[0])
    rank = 0
    pivot_rows: list[int] = []
    pivot_columns: list[int] = []

    for column in range(columns):
        pivot = next(
            (
                row
                for row in range(rank, len(data))
                if data[row][column] % prime
            ),
            None,
        )
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        row_ids[rank], row_ids[pivot] = row_ids[pivot], row_ids[rank]
        inverse = pow(data[rank][column], prime - 2, prime)
        data[rank] = [value * inverse % prime for value in data[rank]]
        for row in range(rank + 1, len(data)):
            coefficient = data[row][column]
            if not coefficient:
                continue
            data[row] = [
                (data[row][index] - coefficient * data[rank][index]) % prime
                for index in range(columns)
            ]
        pivot_rows.append(row_ids[rank])
        pivot_columns.append(column)
        rank += 1
        if rank == columns:
            break
    return rank, pivot_rows, pivot_columns


def bareiss_determinant(matrix: list[list[int]]) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    data = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next(
            (row for row in range(column, size) if data[row][column] != 0),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            sign = -sign
        pivot_value = data[column][column]
        for row in range(column + 1, size):
            for index in range(column + 1, size):
                numerator = (
                    data[row][index] * pivot_value
                    - data[row][column] * data[column][index]
                )
                if numerator % previous:
                    raise AssertionError("Bareiss division was not exact")
                data[row][index] = numerator // previous
            data[row][column] = 0
        previous = pivot_value
    return sign * data[size - 1][size - 1]


def certified_rank(matrix: list[list[int]]) -> dict[str, object]:
    rank, row_ids, column_ids = pivot_minor_mod(matrix)
    minor = [
        [matrix[row][column] for column in column_ids]
        for row in row_ids
    ]
    determinant = bareiss_determinant(minor)
    if determinant == 0:
        raise AssertionError("selected integer minor is singular")
    return {
        "rank_lower_bound": rank,
        "minor_order": rank,
        "minor_determinant": determinant,
        "pivot_rows": row_ids,
        "pivot_columns": column_ids,
    }


def sign_span_certificate() -> dict[str, object]:
    matrix = [list(sign_vector(label)) for label in range(GROUP_SIZE)]
    certificate = certified_rank(matrix)
    if certificate["rank_lower_bound"] != N:
        raise AssertionError(certificate)
    if certificate["minor_determinant"] != -32:
        raise AssertionError(certificate)
    return certificate


def parity_fiber_certificate() -> dict[str, object]:
    fibers = all_parity_fibers()
    size_by_weight: dict[str, int] = {}
    canonical_rows: list[dict[str, object]] = []
    expected = {
        0: (2256, 31, -32),
        1: (1712, 31, 32),
        2: (1712, 31, -32),
        3: (1200, 31, -32),
        4: (1200, 31, -32),
        5: (720, 26, 1),
    }

    for weight in range(BITS + 1):
        canonical = (1 << weight) - 1 if weight else 0
        assignments = fibers[canonical]
        matrix = additive_feature_matrix(assignments)
        certificate = certified_rank(matrix)
        expected_size, expected_rank, expected_determinant = expected[weight]
        observed = (
            len(assignments),
            int(certificate["rank_lower_bound"]),
            int(certificate["minor_determinant"]),
        )
        if observed != (expected_size, expected_rank, expected_determinant):
            raise AssertionError((weight, observed))
        size_by_weight[str(weight)] = len(assignments)
        canonical_rows.append(
            {
                "parity_weight": weight,
                "canonical_parity": canonical,
                "fiber_size": len(assignments),
                **certificate,
            }
        )

    rank_histogram: Counter[int] = Counter()
    for parity, assignments in fibers.items():
        weight = parity.bit_count()
        if len(assignments) != expected[weight][0]:
            raise AssertionError((parity, len(assignments), expected[weight][0]))
        rank_histogram[expected[weight][1]] += 1

    target_assignments = fibers[TARGET_PARITY]
    if len(target_assignments) != 720:
        raise AssertionError(len(target_assignments))
    if any(tuple(sorted(assignment)) != tuple(range(N)) for assignment in target_assignments):
        raise AssertionError("target parity fiber contains a non-permutation")

    span_dimension = sum(
        count * rank for rank, count in rank_histogram.items()
    )
    if rank_histogram != Counter({31: 31, 26: 1}):
        raise AssertionError(rank_histogram)
    if span_dimension != 987:
        raise AssertionError(span_dimension)

    return {
        "fiber_size_by_parity_weight": size_by_weight,
        "canonical_integer_minor_certificates": canonical_rows,
        "feature_rank_histogram": {
            str(rank): count for rank, count in sorted(rank_histogram.items())
        },
        "target_parity": TARGET_PARITY,
        "target_fiber_size": len(target_assignments),
        "target_fiber_is_exactly_the_permutation_support": True,
        "one_defect_span_dimension": span_dimension,
    }


def coefficient_identity_certificate() -> dict[str, object]:
    vectors = [sign_vector(label) for label in range(GROUP_SIZE)]
    nonzero_count = 0
    zero_count = 0
    for assignment in product(range(N), repeat=N):
        numerator = 0
        for label, vector in enumerate(vectors):
            coefficient = character(TARGET_PARITY, label)
            for row in assignment:
                coefficient *= vector[row]
            numerator += coefficient
        is_permutation = tuple(sorted(assignment)) == tuple(range(N))
        expected = GROUP_SIZE if is_permutation else 0
        if numerator != expected:
            raise AssertionError((assignment, numerator, expected))
        if numerator:
            nonzero_count += 1
        else:
            zero_count += 1
    if nonzero_count != 720 or zero_count != N**N - 720:
        raise AssertionError((nonzero_count, zero_count))
    return {
        "coefficient_denominator": GROUP_SIZE,
        "nonzero_target_coefficients": nonzero_count,
        "zero_non_target_coefficients": zero_count,
        "identity_verified_on_all_assignments": N**N,
    }


def one_defect_character_identity_certificate() -> dict[str, object]:
    checks = 0
    for base in range(GROUP_SIZE):
        for defect in range(GROUP_SIZE):
            for parity in range(GROUP_SIZE):
                for row in range(N):
                    left = (
                        character(base, parity ^ row_character(row))
                        * sign_vector(base ^ defect)[row]
                    )
                    right = character(base, parity) * sign_vector(defect)[row]
                    if left != right:
                        raise AssertionError((base, defect, parity, row))
                    checks += 1
    return {
        "checks": checks,
        "identity": (
            "chi_base(parity+e_row)*s_(base+defect)(row)="
            "chi_base(parity)*s_defect(row)"
        ),
    }


def build_payload() -> dict[str, object]:
    sign_certificate = sign_span_certificate()
    fibers = parity_fiber_certificate()
    glynn = coefficient_identity_certificate()
    character_identity = one_defect_character_identity_certificate()

    unique_terms = GROUP_SIZE + N * GROUP_SIZE * (GROUP_SIZE - 1)
    indexed_terms = N * GROUP_SIZE * GROUP_SIZE
    if unique_terms != 5_984 or indexed_terms != 6_144:
        raise AssertionError((unique_terms, indexed_terms))

    return {
        "status": "N6_ONE_DEFECT_SIGN_FAMILY_EXACT_32",
        "field": "characteristic zero",
        "normalization": (
            "Each column sign vector has row-zero coefficient +1. "
            "A nonuniform term has five copies of one sign vector and one "
            "copy of a second sign vector."
        ),
        "family": {
            "normalized_sign_vector_count": GROUP_SIZE,
            "indexed_term_count_with_uniform_duplicates": indexed_terms,
            "unique_term_count": unique_terms,
            "sign_span_certificate": sign_certificate,
        },
        "one_defect_character_identity": character_identity,
        "parity_fiber_certificate": fibers,
        "glynn_upper_bound_certificate": glynn,
        "restricted_support_theorem": {
            "lower_bound": GROUP_SIZE,
            "upper_bound": GROUP_SIZE,
            "exact_minimum_nonzero_summands": GROUP_SIZE,
            "proof_role_of_computation": (
                "The five non-target additive-kernel ranks are certified by "
                "31-by-31 integer minors. The target parity fiber is the 720 "
                "permutation support. Fourier inversion and the two-case "
                "support argument are mathematical steps in the companion note."
            ),
        },
        "route_decision": {
            "one_defect_sign_decomposition_with_at_most_25_terms": "impossible",
            "one_defect_sign_decomposition_with_at_most_31_terms": "impossible",
            "minimum_inside_restricted_family": 32,
            "general_chow_rank_changed": False,
            "full_column_sign_family": "open",
            "row_homogeneous_tensor_rank": "open",
        },
        "claim_boundary": (
            "This is an exact theorem only for the normalized one-defect sign "
            "family. It is not a lower bound for arbitrary column-sign, "
            "row-homogeneous, tensor-rank, or unrestricted Chow decompositions."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_ONE_DEFECT_SIGN_RIGIDITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
