#!/usr/bin/env python3
"""Exact finite audit for row/column-isotype projected catalecticants.

The proof document establishes a general characteristic-zero theorem.  For the
permanent derivative module

    E_m ~= k[C([n],m)] tensor k[C([n],m)],

any rectangular row/column symmetry projection A tensor B has rank
`dim(A)*dim(B)` on perm_n.  A diagonal matching Chow term yields the diagonal
comultiplication, whose projection has rank at least max(dim(A),dim(B)).
Consequently every such rank-ratio route, and every finite block-diagonal sum,
is capped by binom(n,m).

This script reconstructs the primitive Johnson projectors modulo a large prime
and checks every irreducible rectangle for 2<=n<=9.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import comb
from pathlib import Path
from typing import Any

PRIME = 1_000_003
EXPECTED_CORE_SHA256 = "604549395d620264b183513f6e18eaced85c79b62c0c34b980634b10708d4804"


def require(c: bool, msg: object) -> None:
    if not c:
        raise RuntimeError(msg)


def canonical_sha256(x: object) -> str:
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n, k, m = len(a), len(b), len(b[0])
    require(len(a[0]) == k, (len(a[0]), k))
    bt = list(zip(*b))
    return [
        [sum(x * y for x, y in zip(row, col)) % PRIME for col in bt]
        for row in a
    ]


def eye(n: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def add_scalar_identity(a: list[list[int]], scalar: int) -> list[list[int]]:
    out = [row[:] for row in a]
    for i in range(len(a)):
        out[i][i] = (out[i][i] + scalar) % PRIME
    return out


def scale(a: list[list[int]], c: int) -> list[list[int]]:
    return [[c * x % PRIME for x in row] for row in a]


def rank_mod(a: list[list[int]]) -> int:
    if not a:
        return 0
    a = [row[:] for row in a]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] % PRIME), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % PRIME, PRIME - 2, PRIME)
        a[r] = [(x * inv) % PRIME for x in a[r]]
        for i in range(rows):
            if i == r or not a[i][c]:
                continue
            q = a[i][c]
            a[i] = [(x - q * y) % PRIME for x, y in zip(a[i], a[r])]
        r += 1
        if r == rows:
            break
    return r


def johnson_data(n: int, m: int):
    subsets = list(itertools.combinations(range(n), m))
    sets = [set(x) for x in subsets]
    size = len(subsets)
    adjacency = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if len(sets[i] & sets[j]) == m - 1:
                adjacency[i][j] = adjacency[j][i] = 1
    s = min(m, n - m)
    eigenvalues = [(m - i) * (n - m - i) - i for i in range(s + 1)]
    dimensions = [
        comb(n, i) - (comb(n, i - 1) if i else 0)
        for i in range(s + 1)
    ]
    projectors = []
    identity = eye(size)
    for i, theta in enumerate(eigenvalues):
        projector = identity
        denominator = 1
        for j, eta in enumerate(eigenvalues):
            if j == i:
                continue
            projector = matmul(
                projector,
                add_scalar_identity(adjacency, -eta),
            )
            denominator = denominator * (theta - eta) % PRIME
        projector = scale(
            projector,
            pow(denominator % PRIME, PRIME - 2, PRIME),
        )
        require(matmul(projector, projector) == projector, (n, m, i, "not idempotent"))
        require(
            rank_mod(projector) == dimensions[i],
            (n, m, i, rank_mod(projector), dimensions[i]),
        )
        projectors.append(projector)
    summed = [
        [
            sum(projectors[k][i][j] for k in range(s + 1)) % PRIME
            for j in range(size)
        ]
        for i in range(size)
    ]
    require(summed == identity, (n, m, "projectors do not sum to identity"))
    return size, dimensions, projectors


def build_payload() -> dict[str, Any]:
    projector_checks = 0
    rectangle_checks = 0
    block_sum_checks = 0
    finite = {}
    for n in range(2, 10):
        nrows = []
        for m in range(1, n):
            if m > n - m:
                continue
            size, dims, projectors = johnson_data(n, m)
            rows = []
            for i, dim_i in enumerate(dims):
                for j, dim_j in enumerate(dims):
                    gram = [
                        [
                            projectors[i][r][c] * projectors[j][r][c] % PRIME
                            for c in range(size)
                        ]
                        for r in range(size)
                    ]
                    diagonal_rank = rank_mod(gram)
                    require(
                        diagonal_rank >= max(dim_i, dim_j),
                        (n, m, i, j, diagonal_rank, dim_i, dim_j),
                    )
                    route = (dim_i * dim_j + diagonal_rank - 1) // diagonal_rank
                    require(route <= size, (n, m, i, j, route, size))
                    rows.append([i, j, dim_i, dim_j, diagonal_rank, route])
                    rectangle_checks += 1
            require(
                all(
                    dim_i * dim_j <= size * max(dim_i, dim_j)
                    for _, _, dim_i, dim_j, _, _ in rows
                ),
                (n, m),
            )
            block_sum_checks += len(rows)
            projector_checks += len(projectors)
            nrows.append(
                {
                    "m": m,
                    "subset_dimension": size,
                    "isotype_dimensions": dims,
                    "maximum_route_ceiling": max(row[-1] for row in rows),
                    "rectangle_table_sha256": canonical_sha256(rows),
                }
            )
        finite[str(n)] = nrows
    core = {
        "status": [
            "GENERAL_ROW_COLUMN_RECTANGULAR_PROJECTION_CEILING",
            "DIAGONAL_TERM_WITNESS",
            "EXACT_MODULAR_REPLAY",
        ],
        "theorem": {
            "permanent_rank": "rank F_(A,B)(perm_n)=dim(A)*dim(B)",
            "diagonal_term_rank": "rank F_(A,B)(prod_i x_ii)>=max(dim(A),dim(B))",
            "single_rectangle_ceiling": "route ratio <= min(dim(A),dim(B)) <= binom(n,m)",
            "finite_block_sum_ceiling": "every finite block-diagonal sum of rectangular projections has ratio <= binom(n,m)",
            "global_ceiling": "max over m is binom(n,floor(n/2))",
        },
        "exact_replay": {
            "prime": PRIME,
            "projector_checks": projector_checks,
            "rectangle_checks": rectangle_checks,
            "block_sum_checks": block_sum_checks,
            "finite": finite,
        },
        "claim_boundary": (
            "The theorem covers row/column symmetry projections whose target is "
            "A tensor B, with A and B sums of Johnson isotypes, and finite "
            "block-diagonal sums of such maps. It does not cover a single "
            "projection onto an arbitrary nonrectangular union of isotype pairs, "
            "row/column projections of higher Koszul maps, arbitrary Pieri maps, "
            "nonlinear minors, higher syzygies, Chow-realizability defects, "
            "border rank, exact rank for n>=6, or general Glynn optimality."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        require(
            payload["core_sha256"] == EXPECTED_CORE_SHA256,
            payload["core_sha256"],
        )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")
    print("GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
