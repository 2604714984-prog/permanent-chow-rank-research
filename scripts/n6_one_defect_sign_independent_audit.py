#!/usr/bin/env python3
"""Independent exact-rank replay for the one-defect sign theorem.

This script does not import the primary audit.  It reconstructs the six
canonical parity fibers, computes additive-feature ranks modulo a different
prime, and supplies explicit characteristic-zero kernel spaces of the matching
codimensions:

* five position-constant relations on every parity fiber; and
* five additional row-total relations on the permutation fiber.

A modular rank of an integer matrix is a characteristic-zero lower bound.  The
explicit independent kernel vectors provide the matching upper bound, so the
reported ranks are exact over every characteristic-zero field.
"""

from __future__ import annotations

import json
from itertools import product

N = 6
BITS = 5
TARGET = (1 << BITS) - 1
PRIME = 1_000_033


def row_character(row: int) -> int:
    return 0 if row == 0 else 1 << (row - 1)


def parity(assignment: tuple[int, ...]) -> int:
    value = 0
    for row in assignment:
        value ^= row_character(row)
    return value


def fibers() -> dict[int, list[tuple[int, ...]]]:
    result = {value: [] for value in range(1 << BITS)}
    for assignment in product(range(N), repeat=N):
        result[parity(assignment)].append(assignment)
    return result


def feature_rows(assignments: list[tuple[int, ...]]) -> list[int]:
    rows: list[int] = []
    for assignment in assignments:
        bits = 0
        for position, row in enumerate(assignment):
            bits |= 1 << (N * position + row)
        rows.append(bits)
    return rows


def rank_binary_rows_mod(rows: list[int], columns: int, prime: int) -> int:
    dense = [
        [1 if (row >> column) & 1 else 0 for column in range(columns)]
        for row in rows
    ]
    rank = 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(dense)) if dense[index][column]),
            None,
        )
        if pivot is None:
            continue
        dense[rank], dense[pivot] = dense[pivot], dense[rank]
        inverse = pow(dense[rank][column], prime - 2, prime)
        dense[rank] = [value * inverse % prime for value in dense[rank]]
        for index in range(rank + 1, len(dense)):
            coefficient = dense[index][column]
            if coefficient:
                dense[index] = [
                    (dense[index][entry] - coefficient * dense[rank][entry])
                    % prime
                    for entry in range(columns)
                ]
        rank += 1
    return rank


def position_kernel_vectors() -> list[list[int]]:
    vectors: list[list[int]] = []
    for position in range(1, N):
        vector = [0] * (N * N)
        for row in range(N):
            vector[N * position + row] = 1
            vector[row] = -1
        vectors.append(vector)
    return vectors


def row_kernel_vectors() -> list[list[int]]:
    vectors: list[list[int]] = []
    for row in range(1, N):
        vector = [0] * (N * N)
        for position in range(N):
            vector[N * position + row] = 1
            vector[N * position] = -1
        vectors.append(vector)
    return vectors


def dot_feature(assignment: tuple[int, ...], vector: list[int]) -> int:
    return sum(vector[N * position + row] for position, row in enumerate(assignment))


def vector_rank_mod(vectors: list[list[int]], prime: int = PRIME) -> int:
    data = [[value % prime for value in vector] for vector in vectors]
    rank = 0
    columns = len(data[0]) if data else 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(data)) if data[index][column]),
            None,
        )
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        inverse = pow(data[rank][column], prime - 2, prime)
        data[rank] = [value * inverse % prime for value in data[rank]]
        for index in range(len(data)):
            if index == rank:
                continue
            coefficient = data[index][column]
            if coefficient:
                data[index] = [
                    (data[index][entry] - coefficient * data[rank][entry])
                    % prime
                    for entry in range(columns)
                ]
        rank += 1
        if rank == len(data):
            break
    return rank


def build_payload() -> dict[str, object]:
    all_fibers = fibers()
    position_kernels = position_kernel_vectors()
    if vector_rank_mod(position_kernels) != 5:
        raise AssertionError("position kernels are not independent")

    rows: list[dict[str, object]] = []
    expected_sizes = [2256, 1712, 1712, 1200, 1200, 720]
    expected_ranks = [31, 31, 31, 31, 31, 26]

    for weight in range(BITS + 1):
        canonical = (1 << weight) - 1 if weight else 0
        assignments = all_fibers[canonical]
        if len(assignments) != expected_sizes[weight]:
            raise AssertionError((weight, len(assignments)))
        kernels = position_kernels[:]
        if weight == BITS:
            if any(tuple(sorted(value)) != tuple(range(N)) for value in assignments):
                raise AssertionError("target fiber is not the permutation fiber")
            kernels += row_kernel_vectors()
        if any(dot_feature(value, vector) for value in assignments for vector in kernels):
            raise AssertionError((weight, "kernel vector does not vanish"))
        kernel_rank = vector_rank_mod(kernels)
        expected_kernel_rank = 10 if weight == BITS else 5
        if kernel_rank != expected_kernel_rank:
            raise AssertionError((weight, kernel_rank))
        modular_rank = rank_binary_rows_mod(feature_rows(assignments), N * N, PRIME)
        exact_upper = N * N - kernel_rank
        if modular_rank != exact_upper or modular_rank != expected_ranks[weight]:
            raise AssertionError((weight, modular_rank, exact_upper))
        rows.append(
            {
                "parity_weight": weight,
                "canonical_parity": canonical,
                "fiber_size": len(assignments),
                "modular_rank_lower_bound": modular_rank,
                "explicit_kernel_dimension": kernel_rank,
                "characteristic_zero_rank_upper_bound": exact_upper,
                "exact_characteristic_zero_rank": modular_rank,
            }
        )

    span_dimension = 31 * 31 + 26
    if span_dimension != 987:
        raise AssertionError(span_dimension)
    return {
        "status": "N6_ONE_DEFECT_SIGN_INDEPENDENT_AUDIT_PASS",
        "prime": PRIME,
        "canonical_parity_rows": rows,
        "one_defect_span_dimension": span_dimension,
        "logical_direction": (
            "modular integer-matrix rank gives a characteristic-zero lower "
            "bound; explicit independent kernel vectors give the equal upper "
            "bound"
        ),
    }


def main() -> int:
    payload = build_payload()
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("N6_ONE_DEFECT_SIGN_INDEPENDENT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
