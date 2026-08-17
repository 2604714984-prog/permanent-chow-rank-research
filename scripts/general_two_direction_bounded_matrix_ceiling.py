#!/usr/bin/env python3
"""Finite replay for bounded-size homogeneous two-direction matrix images."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def subset_masks(n: int, degree: int) -> list[int]:
    if not 0 <= degree <= n:
        return []
    return [
        sum(1 << value for value in subset)
        for subset in combinations(range(n), degree)
    ]


def power_inclusion_matrix(
    n: int,
    source_degree: int,
    power: int,
) -> list[list[int]]:
    target_degree = source_degree + power
    source = subset_masks(n, source_degree)
    target = subset_masks(n, target_degree)
    return [
        [1 if lower & ~upper == 0 else 0 for lower in source]
        for upper in target
    ]


def modular_rank(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = [[value % prime for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0

    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], prime - 2, prime)
        rows[pivot_row] = [(value * inverse) % prime for value in rows[pivot_row]]

        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def lefschetz_power_checks() -> int:
    checks = 0
    for n in range(2, 9):
        for power in range(1, n + 1):
            for target_degree in range(power, n + 1):
                source_degree = target_degree - power
                expected = min(comb(n, source_degree), comb(n, target_degree))
                rank = modular_rank(power_inclusion_matrix(n, source_degree, power))
                require(rank == expected, (n, power, target_degree, rank, expected))
                checks += 1
    require(checks == 119, checks)
    return checks


def arithmetic_ceiling_checks() -> tuple[int, dict[str, Any]]:
    checks = 0
    samples: dict[str, Any] = {}

    for n in range(2, 10):
        central = comb(n, n // 2)
        for degree_of_entries in range(1, min(4, n) + 1):
            for output_degree in range(degree_of_entries, n + 1):
                source = comb(n, output_degree - degree_of_entries)
                target = comb(n, output_degree)
                lefschetz_rank = min(source, target)

                for row_count in range(1, 5):
                    for column_count in range(1, 5):
                        for normal_rank in range(1, min(row_count, column_count) + 1):
                            denominator = normal_rank * lefschetz_rank
                            numerator = min(
                                column_count * source * source,
                                row_count * target * target,
                            )
                            exact_ceiling = ceil_div(numerator, denominator)
                            coarse_ceiling = ceil_div(
                                max(row_count, column_count) * central,
                                normal_rank,
                            )
                            require(
                                exact_ceiling <= coarse_ceiling,
                                (
                                    n,
                                    degree_of_entries,
                                    output_degree,
                                    row_count,
                                    column_count,
                                    normal_rank,
                                    exact_ceiling,
                                    coarse_ceiling,
                                ),
                            )
                            checks += 1

                            key_tuple = (
                                n,
                                degree_of_entries,
                                output_degree,
                                row_count,
                                column_count,
                                normal_rank,
                            )
                            if key_tuple in {
                                (4, 1, 2, 2, 3, 1),
                                (6, 2, 4, 4, 3, 2),
                                (8, 3, 5, 4, 4, 4),
                                (9, 4, 7, 3, 4, 2),
                            }:
                                samples["_".join(map(str, key_tuple))] = {
                                    "source_boolean": source,
                                    "target_boolean": target,
                                    "normal_rank_denominator": denominator,
                                    "permanent_numerator_cap": numerator,
                                    "exact_route_ceiling": exact_ceiling,
                                    "coarse_central_ceiling": coarse_ceiling,
                                }

    require(checks == 3_870, checks)
    return checks, samples


def matrix_size_diagnostics() -> dict[str, dict[str, int]]:
    rows = {}
    for n in range(3, 31):
        central = comb(n, n // 2)
        glynn = 2 ** (n - 1)
        rows[str(n)] = {
            "central_binomial": central,
            "glynn_scale": glynn,
            "minimum_integer_K_not_excluded": ceil_div(glynn, central),
        }
    return rows


def build_payload() -> dict[str, Any]:
    lefschetz_checks = lefschetz_power_checks()
    arithmetic_checks, samples = arithmetic_ceiling_checks()

    return {
        "status": [
            "GENERAL_BOUNDED_HOMOGENEOUS_MATRIX_CEILING",
            "GENERAL_SUB_SQRT_MATRIX_SIZE_BARRIER",
            "BOOLEAN_NORMAL_RANK_WITNESS",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "boolean_denominator": (
                "beta_Phi(n,d)>=r*min(C(n,d-delta),C(n,d)), where r is "
                "the normal rank."
            ),
            "permanent_numerator": (
                "rho_Phi(A_perm,d)<=min(q*C(n,d-delta)^2,p*C(n,d)^2)."
            ),
            "explicit_ceiling": (
                "R_(Phi,n,d)<=ceil(min(q*Hs^2,p*Ht^2)/(r*min(Hs,Ht)))."
            ),
            "bounded_size": (
                "If p,q<=K_n, then R_(Phi,n)<=K_n*C(n,floor(n/2))+1."
            ),
            "complexity_barrier": (
                "A uniform-degree homogeneous matrix-image proof of Glynn "
                "scale requires max(p,q)=Omega(sqrt(n)); K_n=o(sqrt(n)) is "
                "insufficient."
            ),
        },
        "finite_replay": {
            "lefschetz_power_rank_checks": lefschetz_checks,
            "arithmetic_route_ceiling_checks": arithmetic_checks,
            "prime": PRIME,
            "samples": samples,
            "matrix_size_diagnostics": matrix_size_diagnostics(),
        },
        "claim_boundary": (
            "This is a route ceiling for one homogeneous matrix with a common "
            "entry degree. It is not an upper bound on Chow rank and does not "
            "cover nonuniform degree shifts, joint Fitting/minor profiles, "
            "higher syzygy modules, representation-valued data, "
            "Chow-realizability defects, border rank or exact rank for n>=6. "
            "Literature novelty is not established."
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
    print("GENERAL_TWO_DIRECTION_BOUNDED_MATRIX_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
