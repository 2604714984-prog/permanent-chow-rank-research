#!/usr/bin/env python3
"""Audit the equivariant-K0 full-orbit barrier.

The proof shows that full-group orbit completion turns every term algebra into
the regular representation tensored with its graded vector space. Since every
permanent apolar degree is multiplicity-free under S_n x S_n, any nonnegative
exact-additive graded isotype scalar has route ceiling one.

This script replays the finite representation and arithmetic interfaces with
exact integers only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import Any, Iterable


EXPECTED_CORE_SHA256 = (
    "e6ac3ce63910c27ef4a89856487caefdf66c7a133c706cd3e6bd5c3d31d17357"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def integer_partitions(n: int, maximum: int | None = None) -> Iterable[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    upper = n if maximum is None else min(n, maximum)
    for first in range(upper, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def hook_dimension(partition: tuple[int, ...]) -> int:
    n = sum(partition)
    hook_product = 1
    for row, width in enumerate(partition):
        for column in range(width):
            below = sum(
                1
                for later in range(row + 1, len(partition))
                if partition[later] > column
            )
            hook_product *= width - column + below
    return factorial(n) // hook_product


def two_row_dimensions(n: int, degree: int) -> list[int]:
    boundary = min(degree, n - degree)
    return [
        comb(n, index) - (comb(n, index - 1) if index else 0)
        for index in range(boundary + 1)
    ]


def build_payload() -> dict[str, Any]:
    regular_partition_cells = 0
    regular_dimension_checks = 0

    for n in range(1, 11):
        partitions = list(integer_partitions(n))
        dimensions = [hook_dimension(partition) for partition in partitions]
        require(sum(value * value for value in dimensions) == factorial(n), n)
        regular_partition_cells += len(partitions)
        regular_dimension_checks += 1

    two_row_dimension_checks = 0
    degree_isotype_cells = 0
    weighted_degree_checks = 0
    exhaustive_supports = 0
    finite_block_checks = 0
    ungraded_isotype_checks = 0
    diagnostics: dict[str, list[list[int]]] = {}

    for n in range(2, 41):
        block_numerator = 0
        block_denominator = 0
        local_diagnostics: list[list[int]] = []

        for degree in range(n + 1):
            dimensions = two_row_dimensions(n, degree)
            level = comb(n, degree)
            require(sum(dimensions) == level, (n, degree, dimensions))

            for index, dimension in enumerate(dimensions):
                partition = (n,) if index == 0 else (n - index, index)
                require(dimension == hook_dimension(partition), (n, degree, index))
                two_row_dimension_checks += 1

            isotype_dimensions = [
                left * right
                for left in dimensions
                for right in dimensions
            ]
            require(sum(isotype_dimensions) == level * level, (n, degree))
            degree_isotype_cells += len(isotype_dimensions)

            weight_rows: list[list[int]] = [
                [1] * len(isotype_dimensions),
                [(index + 1) % 5 for index in range(len(isotype_dimensions))],
                [
                    ((index + 3) * 2_654_435_761 + 31 * n + 17 * degree) % 13
                    for index in range(len(isotype_dimensions))
                ],
            ]
            for index in range(len(isotype_dimensions)):
                singleton = [0] * len(isotype_dimensions)
                singleton[index] = 1
                weight_rows.append(singleton)

            best = Fraction(0)
            for weights in weight_rows:
                orbit_weight = sum(
                    weight * dimension
                    for weight, dimension in zip(weights, isotype_dimensions)
                )
                if orbit_weight == 0:
                    continue
                permanent_weight = sum(weights)
                ratio = Fraction(permanent_weight, level * orbit_weight)
                require(ratio <= 1, (n, degree, weights, ratio))
                best = max(best, ratio)
                weighted_degree_checks += 1

            block_numerator += len(isotype_dimensions)
            block_denominator += level * sum(isotype_dimensions)

            if n <= 12:
                local_diagnostics.append(
                    [
                        degree,
                        level,
                        len(isotype_dimensions),
                        best.numerator,
                        best.denominator,
                    ]
                )

            if n <= 7:
                for mask in range(1, 1 << len(isotype_dimensions)):
                    permanent_weight = mask.bit_count()
                    orbit_weight = sum(
                        isotype_dimensions[index]
                        for index in range(len(isotype_dimensions))
                        if (mask >> index) & 1
                    )
                    require(
                        Fraction(permanent_weight, level * orbit_weight) <= 1,
                        (n, degree, mask),
                    )
                    exhaustive_supports += 1

        require(Fraction(block_numerator, block_denominator) <= 1, n)
        finite_block_checks += 1

        dimensions = two_row_dimensions(n, n // 2)
        for left_index, left in enumerate(dimensions):
            for right_index, right in enumerate(dimensions):
                multiplicity = n - 2 * max(left_index, right_index) + 1
                require(multiplicity >= 1, (n, left_index, right_index))
                orbit_multiplicity = (2**n) * left * right
                require(Fraction(multiplicity, orbit_multiplicity) <= 1, n)
                ungraded_isotype_checks += 1

        if n <= 12:
            diagnostics[str(n)] = local_diagnostics

    core: dict[str, Any] = {
        "status": [
            "GENERAL_EQUIVARIANT_GRADED_K0_CLASSIFICATION",
            "GENERAL_APOLAR_ORBIT_SUBQUOTIENT",
            "ORBIT_SYMMETRIZED_ISOTYPE_BARRIER",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "equivariant_K0": (
                "Exact-additive scalars on finite-length graded "
                "G-equivariant k[s,t]-modules are nonnegative weighted "
                "graded isotype multiplicities."
            ),
            "orbit_subquotient": (
                "For G-invariant f=sum_i T_i, A_f is a G-equivariant "
                "subquotient of direct_sum_(i,g) A_(gT_i)."
            ),
            "regular_orbit": (
                "For each term T, direct_sum_g A_(gT) is isomorphic to "
                "k[G] tensor A_T, with G regular on the first factor."
            ),
            "permanent_multiplicity": (
                "Each degree of A_(perm_n) is multiplicity-free under "
                "S_n x S_n."
            ),
            "route_ceiling": (
                "Every full-orbit exact-additive isotype scalar gives a "
                "rank-ratio lower bound at most one."
            ),
        },
        "exact_replay": {
            "regular_partition_cells": regular_partition_cells,
            "regular_dimension_checks": regular_dimension_checks,
            "two_row_dimension_checks": two_row_dimension_checks,
            "degree_isotype_cells": degree_isotype_cells,
            "weighted_degree_checks": weighted_degree_checks,
            "exhaustive_isotype_supports": exhaustive_supports,
            "finite_block_checks": finite_block_checks,
            "ungraded_isotype_checks": ungraded_isotype_checks,
            "diagnostics": diagnostics,
        },
        "claim_boundary": (
            "The theorem closes exact-additive representation scalars only "
            "after the legal full-group orbit symmetrization of arbitrary "
            "Chow terms. It does not close a more efficient termwise "
            "equivariant envelope, fixed linear maps already treated by "
            "matching-orbit theorems, minimal syzygy functors which are not "
            "exact-additive, nonlinear determinantal data, valuative "
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
    print("GENERAL_EQUIVARIANT_K0_ORBIT_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
