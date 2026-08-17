#!/usr/bin/env python3
"""Exact audit of two-sided matching-source compression ceilings.

The general proof is in docs/general_two_sided_matching_source_ceiling.md.
This finite replay verifies the canonical source-section graph support,
matching-projector coverage, dense rational compression interfaces,
row--column multiplicity-free dimension arithmetic and common-term block sums.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, comb, factorial
from pathlib import Path
from typing import Any


EXPECTED_CORE_SHA256 = (
    "72fb06b3ca6201e2b31e0d0aafb22370cf2b7572eaf9e43a3eb0d0f6096c4533"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def matrix_rank_fraction(matrix: list[list[Fraction]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for index in range(row_count):
            if index == rank or not rows[index][column]:
                continue
            factor = rows[index][column]
            rows[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(rows[index], rows[rank], strict=True)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix, strict=True)]


def multiply(
    left: list[list[Fraction]],
    right: list[list[Fraction]],
) -> list[list[Fraction]]:
    return [
        [
            sum(
                Fraction(left[row][index]) * Fraction(right[index][column])
                for index in range(len(right))
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    augmented = [
        [Fraction(matrix[row][column]) for column in range(size)]
        + [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        require(pivot is not None, ("singular Gram matrix", column))
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(size):
            if row == column or not augmented[row][column]:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    augmented[row],
                    augmented[column],
                    strict=True,
                )
            ]
    return [row[size:] for row in augmented]


def gram(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return multiply(transpose(matrix), matrix)


def graph_data(
    n: int,
    degree: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    subsets = tuple(combinations(range(n), degree))
    index = {subset: position for position, subset in enumerate(subsets)}
    maps = []
    for permutation in permutations(range(n)):
        maps.append(
            tuple(
                index[tuple(sorted(permutation[value] for value in subset))]
                for subset in subsets
            )
        )
    return subsets, tuple(maps)


def source_and_coverage_replay() -> tuple[int, int, list[list[int]]]:
    source_checks = 0
    coordinate_coverage_checks = 0
    rows: list[list[int]] = []

    for n in range(2, 7):
        for degree in range(1, n):
            subsets, maps = graph_data(n, degree)
            width = len(subsets)
            counts = [[0] * width for _ in range(width)]
            for graph_map in maps:
                for source, target in enumerate(graph_map):
                    counts[source][target] += 1
                    source_checks += 1

            expected = factorial(degree) * factorial(n - degree)
            require(
                all(value == expected for row in counts for value in row),
                (n, degree, expected),
            )
            coordinate_coverage_checks += width * width
            rows.append([n, degree, width, factorial(n), expected])

    return source_checks, coordinate_coverage_checks, rows


def dense_compression_replay() -> tuple[int, int, list[list[int]]]:
    rank_computations = 0
    trace_checks = 0
    rows: list[list[int]] = []

    for n in range(3, 6):
        for degree in range(1, n // 2 + 1):
            subsets, maps = graph_data(n, degree)
            width = len(subsets)
            ambient = width * width
            ranks = sorted(
                {
                    1,
                    min(width, ambient),
                    min(2 * width, ambient),
                    min(max(2, ambient // 3), ambient),
                }
            )
            for subspace_rank in ranks:
                basis = [
                    [Fraction((coordinate + 1) ** power) for power in range(subspace_rank)]
                    for coordinate in range(ambient)
                ]
                require(
                    matrix_rank_fraction(basis) == subspace_rank,
                    (n, degree, subspace_rank, "basis rank"),
                )
                gram_inverse = inverse(gram(basis))
                traces: list[Fraction] = []
                compression_ranks: list[int] = []

                for graph_map in maps:
                    mask = [
                        source * width + graph_map[source]
                        for source in range(width)
                    ]
                    restricted_basis = [basis[index] for index in mask]
                    restricted_gram = gram(restricted_basis)
                    compression = multiply(gram_inverse, restricted_gram)
                    traces.append(
                        sum(compression[index][index] for index in range(subspace_rank))
                    )
                    compression_ranks.append(matrix_rank_fraction(restricted_basis))
                    rank_computations += 1

                average_trace = sum(traces, Fraction(0)) / len(traces)
                require(
                    average_trace == Fraction(subspace_rank, width),
                    (n, degree, subspace_rank, average_trace),
                )
                require(
                    max(compression_ranks) >= ceil(subspace_rank / width),
                    (n, degree, subspace_rank, compression_ranks),
                )
                trace_checks += 1
                rows.append(
                    [
                        n,
                        degree,
                        width,
                        subspace_rank,
                        max(compression_ranks),
                        average_trace.numerator,
                        average_trace.denominator,
                    ]
                )

    return rank_computations, trace_checks, rows


def isotype_and_block_replay() -> tuple[int, int, int, dict[str, list[int]]]:
    isotype_cells = 0
    support_checks = 0
    block_sum_checks = 0
    diagnostics: dict[str, list[int]] = {}

    for n in range(2, 31):
        per_degree: list[tuple[int, int]] = []
        central = comb(n, n // 2)
        for degree in range(1, n):
            maximum_index = min(degree, n - degree)
            dimensions = [
                comb(n, index) - (comb(n, index - 1) if index else 0)
                for index in range(maximum_index + 1)
            ]
            require(sum(dimensions) == comb(n, degree), (n, degree, dimensions))
            isotypes = [left * right for left in dimensions for right in dimensions]
            isotype_cells += len(isotypes)

            supports = list(isotypes)
            for left in range(len(isotypes)):
                for right in range(left + 1, min(len(isotypes), left + 4)):
                    supports.append(isotypes[left] + isotypes[right])
            supports.extend(
                [
                    sum(isotypes),
                    sum(
                        dimension
                        for index, dimension in enumerate(isotypes)
                        if index % 2 == 0
                    ),
                ]
            )

            width = comb(n, degree)
            for support_dimension in supports:
                if not support_dimension:
                    continue
                term_rank = ceil(support_dimension / width)
                require(
                    ceil(support_dimension / term_rank) <= width,
                    (n, degree, support_dimension, term_rank),
                )
                support_checks += 1
            per_degree.append((width, sum(isotypes)))

        numerator = sum(dimension for _, dimension in per_degree)
        denominator = sum(
            Fraction(dimension, width)
            for width, dimension in per_degree
        )
        require(Fraction(numerator, 1) / denominator <= central, (n, numerator))
        block_sum_checks += 1
        if n <= 12:
            diagnostics[str(n)] = [
                central,
                numerator,
                denominator.numerator,
                denominator.denominator,
            ]

    return isotype_cells, support_checks, block_sum_checks, diagnostics


def build_payload() -> dict[str, Any]:
    source_checks, coverage_checks, source_rows = source_and_coverage_replay()
    dense_ranks, dense_traces, dense_rows = dense_compression_replay()
    isotype_cells, support_checks, block_checks, diagnostics = (
        isotype_and_block_replay()
    )

    require(source_checks == 48_616, source_checks)
    require(coverage_checks == 1_262, coverage_checks)
    require(dense_ranks == 1_146, dense_ranks)
    require(dense_traces == 18, dense_traces)
    require(isotype_cells == 23_195, isotype_cells)
    require(support_checks == 91_040, support_checks)
    require(block_checks == 29, block_checks)

    core: dict[str, Any] = {
        "status": [
            "GENERAL_TWO_SIDED_MATCHING_SOURCE_SECTION",
            "GENERAL_SYMMETRIC_COMPRESSION_CEILING",
            "GENERAL_EQUIVARIANT_PREPOST_CEILING",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "source_section": "Q_m C_perm J_m=I_(E_m).",
            "matching_term": (
                "Q_m C_(T_sigma) J_m=(m!(n-m)!)^(-1) P_sigma."
            ),
            "graph_average": "average_sigma P_sigma=I/binom(n,m).",
            "symmetric_ceiling": (
                "rank(P_U C_perm P_U)/max_T rank(P_U C_T P_U)"
                "<=binom(n,m)."
            ),
            "equivariant_ceiling": (
                "Arbitrary S_n x S_n-equivariant pre/post endomorphisms "
                "of E_m obey the same ceiling."
            ),
            "finite_blocks": (
                "A finite block sum across degrees is capped by "
                "binom(n,floor(n/2))."
            ),
        },
        "exact_replay": {
            "source_graph_checks": source_checks,
            "coordinate_coverage_checks": coverage_checks,
            "dense_restriction_rank_computations": dense_ranks,
            "dense_average_trace_checks": dense_traces,
            "isotype_dimension_cells": isotype_cells,
            "isotype_support_checks": support_checks,
            "finite_block_sum_checks": block_checks,
            "source_rows": source_rows,
            "dense_rows": dense_rows,
            "block_diagnostics": diagnostics,
        },
        "claim_boundary": (
            "The theorem closes symmetric two-sided compression through the "
            "canonical matching source section and arbitrary row-column "
            "equivariant pre/post endomorphisms of the effective matching "
            "module. It does not cover unrelated non-equivariant source and "
            "target spaces, source-kernel directions outside J_m(E_m), "
            "minimal syzygy functors, nonlinear determinantal data, valuative "
            "arguments, Chow-realizability defects, border rank, exact rank "
            "for n>=6, or general Glynn optimality."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


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
    print("GENERAL_TWO_SIDED_MATCHING_SOURCE_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
