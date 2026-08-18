#!/usr/bin/env python3
"""Exact finite replay for the principal two-direction ideal barrier.

For the Boolean algebra B_n, multiplication by

    L^p,  L=z_1+...+z_n,

between degrees d-p and d is, up to the nonzero scalar p!, the subset
inclusion matrix.  The proof document shows by an sl_2 argument that its
characteristic-zero rank is

    min(binom(n,d-p), binom(n,d)).

This script independently verifies the explicit finite interface modulo a
large prime and freezes the source/target route ceiling for the permanent
Hilbert function.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any


PRIME = 1_000_003
FROZEN = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "general_two_direction_principal_ideal_barrier.json"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subset_masks(n: int, size: int) -> list[int]:
    return [
        sum(1 << value for value in subset)
        for subset in combinations(range(n), size)
    ]


def modular_rank(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    pivot_row = 0

    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % prime, prime - 2, prime)
        rows[pivot_row] = [(value * inverse) % prime for value in rows[pivot_row]]

        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column] % prime
            if factor:
                rows[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[row], rows[pivot_row])
                ]

        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def inclusion_matrix(n: int, source_degree: int, target_degree: int) -> list[list[int]]:
    require(0 <= source_degree <= target_degree <= n, (n, source_degree, target_degree))
    sources = subset_masks(n, source_degree)
    targets = subset_masks(n, target_degree)
    return [
        [1 if source & ~target == 0 else 0 for source in sources]
        for target in targets
    ]


def build_payload() -> dict[str, Any]:
    cells = 0
    rows: dict[str, dict[str, int]] = {}

    for n in range(2, 9):
        central = comb(n, n // 2)
        row: dict[str, int] = {}
        for p in range(1, n + 1):
            for degree in range(p, n + 1):
                source_degree = degree - p
                expected = min(comb(n, source_degree), comb(n, degree))
                rank = modular_rank(inclusion_matrix(n, source_degree, degree))
                require(rank == expected, (n, p, degree, rank, expected))

                permanent_cap = min(
                    comb(n, source_degree) ** 2,
                    comb(n, degree) ** 2,
                )
                require(permanent_cap == expected**2, (n, p, degree))
                require(expected <= central, (n, p, degree, expected, central))
                row[f"p{p}_d{degree}"] = expected
                cells += 1
        rows[str(n)] = row

    require(cells == 119, cells)

    return {
        "status": [
            "GENERAL_TWO_DIRECTION_PRINCIPAL_IDEAL_BARRIER",
            "EXACT_BOOLEAN_ENVELOPE",
            "CENTRAL_BINOMIAL_ROUTE_CEILING",
            "EXACT_FINITE_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "boolean_envelope": (
                "beta_pr(n,p,d)=min(binom(n,d-p),binom(n,d))."
            ),
            "permanent_cap": (
                "rank(g:A_perm[d-p]->A_perm[d])<=beta_pr(n,p,d)^2."
            ),
            "route_ceiling": (
                "Every principal homogeneous ideal profile proves at most "
                "the central binomial coefficient binom(n,floor(n/2)) terms."
            ),
            "first_open_interface": (
                "At least two genuinely active minimal generators are "
                "required to exceed the principal barrier."
            ),
        },
        "finite_replay": {
            "n_min": 2,
            "n_max": 8,
            "principal_profile_cells": cells,
            "prime": PRIME,
            "boolean_envelopes": rows,
        },
        "claim_boundary": (
            "This is a ceiling for principal homogeneous ideals in a selected "
            "differential two-plane, not an upper bound on Chow rank. It gives "
            "no new finite-n rank lower bound and does not close nonprincipal "
            "ideals, relation modules, representation-valued invariants, "
            "valuative methods, border rank or Chow-realizability defects. "
            "Literature novelty is not established."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_TWO_DIRECTION_PRINCIPAL_IDEAL_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
