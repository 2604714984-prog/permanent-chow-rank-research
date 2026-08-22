#!/usr/bin/env python3
"""Exact replay for local six-block rigidity of the seven-block Glynn witness."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence

ORDER = 4
REFERENCE = (1, 1, 1, 1)
SIGNS = tuple((1,) + tail for tail in product((1, -1), repeat=3))
RETAINED = tuple(value for value in SIGNS if value != REFERENCE)
PRIMES = (1_000_003, 1_000_033)
EXPECTED_CORE = "7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710"

Vector = tuple[int, ...]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def character(value: Sequence[int]) -> int:
    result = 1
    for entry in value:
        result *= int(entry)
    return result


def sign_bits(value: Sequence[int]) -> int:
    result = 0
    for index, entry in enumerate(value[1:]):
        if entry == -1:
            result |= 1 << index
    return result


def tensor4(a: Sequence[int], b: Sequence[int], c: Sequence[int], d: Sequence[int]) -> Vector:
    return tuple(
        int(a[i]) * int(b[j]) * int(c[k]) * int(d[l])
        for i in range(ORDER)
        for j in range(ORDER)
        for k in range(ORDER)
        for l in range(ORDER)
    )


def add_vectors(*terms: tuple[int, Sequence[int]]) -> Vector:
    result = [0] * (ORDER**4)
    for scalar, vector in terms:
        for index, entry in enumerate(vector):
            result[index] += int(scalar) * int(entry)
    return tuple(result)


def atom(value: Sequence[int]) -> Vector:
    diagonal = tensor4(value, value, value, value)
    reference_tail = tensor4(value, value, REFERENCE, REFERENCE)
    return add_vectors((character(value), diagonal), (-character(value), reference_tail))


def basis_vector(index: int) -> tuple[int, ...]:
    return tuple(1 if position == index else 0 for position in range(ORDER))


def projected_tangent_generators(value: Sequence[int]) -> tuple[Vector, ...]:
    """Complete (1,1,1,1)-column multidegree tangent projection.

    Four source directions, eight shared-column factor directions, and sixteen
    tail-factor directions remain after the multidegree projection.
    """

    v = tuple(int(entry) for entry in value)
    w = REFERENCE
    chi = character(v)
    result: list[Vector] = []

    for left_tail in (v, w):
        for right_tail in (v, w):
            result.append(
                tuple(
                    chi * entry
                    for entry in tensor4(v, v, left_tail, right_tail)
                )
            )

    for row in range(ORDER):
        u = basis_vector(row)
        result.append(
            add_vectors(
                (chi, tensor4(u, v, v, v)),
                (-chi, tensor4(u, v, w, w)),
            )
        )
        result.append(
            add_vectors(
                (chi, tensor4(v, u, v, v)),
                (-chi, tensor4(v, u, w, w)),
            )
        )

    for row in range(ORDER):
        u = basis_vector(row)
        result.append(tuple(chi * entry for entry in tensor4(v, v, u, v)))
        result.append(tuple(chi * entry for entry in tensor4(v, v, v, u)))
        result.append(tuple(-chi * entry for entry in tensor4(v, v, u, w)))
        result.append(tuple(-chi * entry for entry in tensor4(v, v, w, u)))

    require(len(result) == 28, len(result))
    return tuple(result)


def sparse_modular_rank(vectors: Iterable[Sequence[int]], prime: int) -> int:
    basis: dict[int, dict[int, int]] = {}
    for vector in vectors:
        current = {
            index: int(entry) % prime
            for index, entry in enumerate(vector)
            if int(entry) % prime
        }
        while current:
            pivot = max(current)
            known = basis.get(pivot)
            if known is None:
                inverse = pow(current[pivot], prime - 2, prime)
                current = {
                    index: coefficient * inverse % prime
                    for index, coefficient in current.items()
                    if coefficient * inverse % prime
                }
                basis[pivot] = current
                break
            factor = current[pivot]
            for index, coefficient in known.items():
                updated = (current.get(index, 0) - factor * coefficient) % prime
                if updated:
                    current[index] = updated
                elif index in current:
                    del current[index]
    return len(basis)


def rational_rank(rows: Sequence[Sequence[int]]) -> int:
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    if not matrix:
        return 0
    rank = 0
    width = len(matrix[0])
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [entry / scale for entry in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                left - factor * right
                for left, right in zip(matrix[row], matrix[rank], strict=True)
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def mode_rank(vector: Sequence[int], mode: int) -> int:
    rows = [[0] * (ORDER**3) for _ in range(ORDER)]
    for i in range(ORDER):
        for j in range(ORDER):
            for k in range(ORDER):
                for l in range(ORDER):
                    indices = (i, j, k, l)
                    row = indices[mode]
                    remaining = tuple(
                        indices[position]
                        for position in range(4)
                        if position != mode
                    )
                    column = (
                        remaining[0] * ORDER * ORDER
                        + remaining[1] * ORDER
                        + remaining[2]
                    )
                    flat = ((i * ORDER + j) * ORDER + k) * ORDER + l
                    rows[row][column] = int(vector[flat])
    return rational_rank(rows)


def build_core() -> dict[str, object]:
    atoms = {value: atom(value) for value in RETAINED}
    tangents = {
        value: projected_tangent_generators(value) for value in RETAINED
    }

    individual_ranks = {
        str(sign_bits(value)): [
            sparse_modular_rank(tangents[value], prime) for prime in PRIMES
        ]
        for value in RETAINED
    }
    require(
        all(ranks == [18, 18] for ranks in individual_ranks.values()),
        individual_ranks,
    )

    pair_profiles = []
    for left, right in combinations(RETAINED, 2):
        combined = add_vectors((1, atoms[left]), (1, atoms[right]))
        profile = tuple(mode_rank(combined, mode) for mode in range(4))
        require(profile == (2, 2, 3, 3), (left, right, profile))
        pair_profiles.append(
            {
                "left": sign_bits(left),
                "right": sign_bits(right),
                "mode_ranks": list(profile),
                "essential_dimension": sum(profile),
            }
        )

    deletion_checks = []
    for missing in RETAINED:
        columns = [
            generator
            for value in RETAINED
            if value != missing
            for generator in tangents[value]
        ]
        ranks = [sparse_modular_rank(columns, prime) for prime in PRIMES]
        augmented = [
            sparse_modular_rank(columns + [atoms[missing]], prime)
            for prime in PRIMES
        ]
        require(ranks == [108, 108], (missing, ranks))
        require(augmented == [109, 109], (missing, augmented))
        deletion_checks.append(
            {
                "missing_sign_bits": sign_bits(missing),
                "missing_hamming_weight": sign_bits(missing).bit_count(),
                "six_projected_tangent_rank": ranks,
                "augmented_with_missing_summand_rank": augmented,
            }
        )

    all_seven_rank = [
        sparse_modular_rank(
            [
                generator
                for value in RETAINED
                for generator in tangents[value]
            ],
            prime,
        )
        for prime in PRIMES
    ]
    require(all_seven_rank == [123, 123], all_seven_rank)

    return {
        "schema": "general_seven_block_glynn_local_rigidity/v1",
        "classification": "STRICT_LOCAL_ROUTE_BARRIER",
        "field": "characteristic_zero",
        "standard_witness": {
            "sign_vectors": len(SIGNS),
            "retained_summands": len(RETAINED),
            "reference_sign_bits": sign_bits(REFERENCE),
            "shared_columns": [1, 2],
            "tail_columns": [3, 4],
            "inherited_witness_core": "045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e",
        },
        "direct_pair_merge": {
            "pairs_checked": len(pair_profiles),
            "uniform_mode_rank_profile": [2, 2, 3, 3],
            "uniform_essential_dimension": 10,
            "degree_six_chow_derivative_essential_cap": 6,
            "direct_pair_merge_possible": False,
            "checks": pair_profiles,
        },
        "projected_tangent": {
            "column_multidegree": [1, 1, 1, 1],
            "ambient_dimension": ORDER**4,
            "raw_projected_generators_per_block": 28,
            "exact_tangent_dimension_per_block": 18,
            "analytic_six_block_rank_upper_bound": 108,
            "modular_primes": list(PRIMES),
            "individual_rank_checks": individual_ranks,
            "deletion_checks": deletion_checks,
            "all_seven_projected_tangent_rank": all_seven_rank,
        },
        "conclusion": {
            "direct_merge_of_two_standard_summands": "IMPOSSIBLE",
            "first_order_absorption_of_deleted_summand_by_other_six": "IMPOSSIBLE",
            "standard_seven_block_witness_locally_six_irreducible": True,
        },
        "claim_boundary": {
            "global_six_block_literal_sum": "OPEN",
            "remote_or_singular_six_block_witness": "NOT_EXCLUDED",
            "higher_order_coalescence": "NOT_EXCLUDED",
            "mu_6_4": "OPEN_IN_[6,7]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--print-core-only", action="store_true")
    arguments = parser.parse_args()

    core = build_core()
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    require(digest == EXPECTED_CORE, digest)
    payload = dict(core)
    payload["core_sha256"] = digest
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.print_core_only:
        print(digest)
    else:
        print("GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_PASS")
        print(digest)


if __name__ == "__main__":
    main()
