#!/usr/bin/env python3
"""Exact invalid-monomial tail ranks for two permutation types in perm7."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_equality_packet_crossdegree_search as base  # noqa: E402
import n7_mixed_glynn_four_permutation_character_dp as four_type  # noqa: E402
import n7_mixed_glynn_graph_search as graph  # noqa: E402
import n7_mixed_glynn_permutation_character_dp as character  # noqa: E402


PERMUTATIONS = character.PERMUTATIONS
IDENTITY = character.IDENTITY
TAILS = tuple(graph.tail_dictionary(0))
CANDIDATE_COUNT = 719 * 5


def invalid_parities(permutations: tuple[tuple[int, ...], ...]) -> set[int]:
    valid = {(0, 0)}
    invalid: set[int] = set()
    for permutation in permutations:
        labels = (0, *(1 << permutation[index] for index in range(6)))
        next_invalid = {value ^ label for value in invalid for label in labels}
        next_valid = set()
        for value, used_columns in valid:
            for column, label in enumerate(labels):
                image = value ^ label
                if (used_columns >> column) & 1:
                    next_invalid.add(image)
                else:
                    next_valid.add((image, used_columns | (1 << column)))
        valid, invalid = next_valid, next_invalid
    return invalid


def tail_character_mask(tail: tuple[int, ...]) -> int:
    return sum((value < 0) << index for index, value in enumerate(tail))


def tail_feature_row(parity: int) -> list[int]:
    return [
        (-1 if (tail_character_mask(tail) & parity).bit_count() & 1 else 1)
        % base.PRIME
        for tail in TAILS
    ]


def modular_rank(rows: list[list[int]]) -> int:
    pivots: dict[int, list[int]] = {}
    for raw_row in rows:
        row = [value % base.PRIME for value in raw_row]
        while True:
            column = next((index for index, value in enumerate(row) if value), None)
            if column is None:
                break
            if column not in pivots:
                inverse = pow(row[column], base.PRIME - 2, base.PRIME)
                pivots[column] = [value * inverse % base.PRIME for value in row]
                break
            multiple = row[column]
            row = [
                (value - multiple * pivot) % base.PRIME
                for value, pivot in zip(row, pivots[column])
            ]
    return len(pivots)


def modular_nullspace_basis(rows: list[list[int]], column_count: int) -> list[list[int]]:
    matrix = [[value % base.PRIME for value in row] for row in rows]
    pivot_columns = []
    pivot_row = 0
    for column in range(column_count):
        selected = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], base.PRIME - 2, base.PRIME)
        matrix[pivot_row] = [
            value * inverse % base.PRIME for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row != pivot_row and matrix[row][column]:
                multiple = matrix[row][column]
                matrix[row] = [
                    (value - multiple * pivot) % base.PRIME
                    for value, pivot in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
    free_columns = [
        column for column in range(column_count) if column not in pivot_columns
    ]
    basis = []
    for free in free_columns:
        vector = [0] * column_count
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -matrix[row][free] % base.PRIME
        basis.append(vector)
    return basis


def invalid_tail_rank(permutations: tuple[tuple[int, ...], ...]) -> int:
    return modular_rank(
        [tail_feature_row(parity) for parity in invalid_parities(permutations)]
    )


def build_payload() -> dict[str, object]:
    character_masks = [tail_character_mask(tail) for tail in TAILS]
    if len(set(character_masks)) != 42:
        raise AssertionError("the tail dictionary must give 42 distinct characters")
    full_character_rank = modular_rank(
        [tail_feature_row(parity) for parity in range(64)]
    )
    identity_invalid_rows = [
        tail_feature_row(parity)
        for parity in invalid_parities((IDENTITY,) * 6)
    ]
    identity_rank = modular_rank(identity_invalid_rows)
    identity_kernel = modular_nullspace_basis(identity_invalid_rows, len(TAILS))
    if len(identity_kernel) != 1:
        raise AssertionError(len(identity_kernel))
    target_parities = [63, *(63 ^ (1 << column) for column in range(6))]
    identity_target_profile = [
        sum(value * coefficient for value, coefficient in zip(tail_feature_row(parity), identity_kernel[0]))
        % base.PRIME
        for parity in target_parities
    ]
    identity_target_support = [
        column for column, value in enumerate(identity_target_profile) if value
    ]
    if len(identity_target_support) < 2:
        raise AssertionError(identity_target_profile)

    rank_histogram: Counter[int] = Counter()
    cycle_histogram: dict[tuple[int, ...], Counter[int]] = defaultdict(Counter)
    started = time.perf_counter()
    for permutation in PERMUTATIONS[1:]:
        kind = four_type.cycle_type(permutation)
        for identity_count in range(1, 6):
            packet = (IDENTITY,) * identity_count + (permutation,) * (
                6 - identity_count
            )
            rank = invalid_tail_rank(packet)
            rank_histogram[rank] += 1
            cycle_histogram[kind][rank] += 1

    if sum(rank_histogram.values()) != CANDIDATE_COUNT:
        raise AssertionError(rank_histogram)
    return {
        "schema_version": 1,
        "status": "EXHAUSTIVE_TWO_PERMUTATION_INVALID_TAIL_RANK",
        "field": f"F_{base.PRIME}",
        "tail_count": len(TAILS),
        "distinct_tail_character_count": len(set(character_masks)),
        "tail_character_masks": character_masks,
        "full_walsh_feature_rank": full_character_rank,
        "identity_packet_invalid_tail_rank": identity_rank,
        "identity_kernel_dimension": len(identity_kernel),
        "identity_kernel_target_parities": target_parities,
        "identity_kernel_target_profile": identity_target_profile,
        "identity_kernel_target_support": identity_target_support,
        "candidate_formula": "(6! - 1) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "invalid_tail_rank_histogram": dict(sorted(rank_histogram.items())),
        "cycle_type_rank_histogram": {
            "+".join(map(str, kind)): dict(sorted(histogram.items()))
            for kind, histogram in sorted(cycle_histogram.items())
        },
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "A common coordinate permutation normalizes one underlying permutation type to the identity.",
            "Every nonidentity relative permutation and all five positive multiplicity splits are exhausted.",
            "The 42 tails are distinct Walsh characters; global tail negation is already a complementary Walsh character because nonzero-count parity equals XOR Hamming-weight parity.",
            "Arbitrary diagonal signs only rescale monomial columns by nonzero scalars, so they do not change the invalid-feature row rank.",
            "Rank 42 on invalid monomials forces zero local permanent-target intersection for every packet with exactly two underlying permutation types.",
            "This does not cover general GL(6) graph transforms, arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
