#!/usr/bin/env python3
"""Exact finite audit of the matching-orbit postprocessing ceiling.

For the m-subset permutation module M, every permutation-matching Chow term
restricts a fixed linear postprocessing map A on M tensor M tensor H to one
graph subspace. Averaging the graph-subspace projectors over S_n x S_n gives
I/dim(M). The proof document turns this into a general rank lower bound.

This script exhausts the graph orbits for n<=5 and checks deterministic linear
maps over a prime field. The finite computation is a replay of the interface,
not the proof of the general theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations, permutations
from math import comb
from pathlib import Path
from typing import Any

PRIME = 1_000_003
EXPECTED_CORE_SHA256 = "7d1c559339080ccd46cc5bf1ee881ec6bbb1e1f816eb40119fe037804eb1846d"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    rows = [[x % prime for x in row] for row in matrix]
    if not rows:
        return 0
    r = 0
    nrows, ncols = len(rows), len(rows[0])
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c], prime - 2, prime)
        rows[r] = [(v * inv) % prime for v in rows[r]]
        for i in range(nrows):
            if i != r and rows[i][c]:
                a = rows[i][c]
                rows[i] = [(x - a*y) % prime for x, y in zip(rows[i], rows[r], strict=True)]
        r += 1
        if r == nrows:
            break
    return r


def action_tables(n: int, m: int):
    subsets = tuple(combinations(range(n), m))
    index = {s: i for i, s in enumerate(subsets)}
    perms = tuple(permutations(range(n)))
    actions = []
    for p in perms:
        actions.append(tuple(index[tuple(sorted(p[i] for i in s))] for s in subsets))
    return subsets, perms, tuple(actions)


def graph_columns(left: tuple[int, ...], right: tuple[int, ...], M: int, h: int) -> list[int]:
    return [((left[s] * M + right[s]) * h + u) for s in range(M) for u in range(h)]


def deterministic_matrix(rows: int, columns: int, seed: int) -> list[list[int]]:
    return [
        [
            ((i + 1) * (j + 3) + seed * (i*i + 3*j*j + 5*i*j + 7)) % PRIME
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def restrict_columns(matrix: list[list[int]], columns: list[int]) -> list[list[int]]:
    return [[row[j] for j in columns] for row in matrix]


def build_payload() -> dict[str, Any]:
    coverage_checks = 0
    map_checks = 0
    rank_bound_checks = 0
    block_sum_checks = 0
    rows_out: dict[str, Any] = {}

    for n in range(3, 6):
        n_rows = []
        for m in range(1, n//2 + 1):
            subsets, perms, actions = action_tables(n, m)
            M = len(subsets)
            group_size = len(perms)
            counts = [[0]*M for _ in range(M)]
            for left in actions:
                for right in actions:
                    for s in range(M):
                        counts[left[s]][right[s]] += 1
            expected = group_size * group_size // M
            require(all(v == expected for row in counts for v in row), (n, m, expected))
            coverage_checks += M*M

            instances = []
            for h in (1, 2):
                domain = M*M*h
                for seed in (1, 2, 5):
                    target = min(domain, M*h + seed + 2)
                    matrix = deterministic_matrix(target, domain, seed + 11*n + 3*m + h)
                    full_rank = rank_mod(matrix)
                    best = 0
                    total_rank = 0
                    for left in actions:
                        for right in actions:
                            r = rank_mod(restrict_columns(matrix, graph_columns(left, right, M, h)))
                            best = max(best, r)
                            total_rank += r
                            map_checks += 1
                    require(M * best >= full_rank, (n, m, h, seed, full_rank, best))
                    require(total_rank * M >= full_rank * group_size * group_size, (n, m, h, seed, "average"))
                    rank_bound_checks += 2
                    instances.append({
                        "auxiliary_dimension": h,
                        "seed": seed,
                        "full_rank": full_rank,
                        "maximum_matching_restriction_rank": best,
                    })
            n_rows.append({
                "degree": m,
                "subset_module_dimension": M,
                "group_size": group_size,
                "coverage_multiplicity": expected,
                "map_instances": instances,
            })
        rows_out[str(n)] = n_rows

    for n in range(4, 6):
        degree_data = []
        all_actions = []
        for m in range(1, n//2 + 1):
            _, perms, actions = action_tables(n, m)
            M = comb(n, m)
            matrix = deterministic_matrix(M+3, M*M, 101+n+7*m)
            degree_data.append((M, matrix, rank_mod(matrix)))
            all_actions.append(actions)
        group_size = len(perms)
        best_sum = 0
        for a in range(group_size):
            for b in range(group_size):
                value = 0
                for (M, matrix, _), actions in zip(degree_data, all_actions, strict=True):
                    value += rank_mod(restrict_columns(matrix, graph_columns(actions[a], actions[b], M, 1)))
                best_sum = max(best_sum, value)
        numerator = sum(r for _, _, r in degree_data)
        denominator_floor = sum(r/M for M, _, r in degree_data)
        require(best_sum + 1e-12 >= denominator_floor, (n, best_sum, denominator_floor))
        require(numerator <= max(M for M, _, _ in degree_data) * best_sum, (n, numerator, best_sum))
        block_sum_checks += 2

    core = {
        "status": [
            "GENERAL_MATCHING_ORBIT_POSTPROCESSING_CEILING",
            "ARBITRARY_FIXED_LINEAR_POSTPROCESSING",
            "MATCHING_PROJECTED_KOSZUL_MAPS_CLOSED",
            "FINITE_BLOCK_SUMS_CLOSED",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "graph_restriction": (
                "For a transitive G-set X, any A:k^(XxX) tensor H -> Y has "
                "max_(g,h) rank A|_(graph(g,h) tensor H) >= rank(A)/|X|."
            ),
            "permanent_application": (
                "Every fixed linear postprocessing of the canonical matching-projected "
                "degree-m catalecticant has Chow rank-ratio ceiling binom(n,m)."
            ),
            "block_sum": (
                "Every finite block-diagonal sum across degrees has ceiling "
                "binom(n,floor(n/2))."
            ),
        },
        "exact_replay": {
            "prime": PRIME,
            "n_min": 3,
            "n_max": 5,
            "coverage_checks": coverage_checks,
            "restricted_map_rank_checks": map_checks,
            "rank_bound_checks": rank_bound_checks,
            "block_sum_checks": block_sum_checks,
            "rows": rows_out,
        },
        "claim_boundary": (
            "This closes fixed linear postprocessing after the canonical matching "
            "projection, including target/source projections and standard Koszul or "
            "Young differentials applied after the projected derivative image. It is "
            "not an upper bound on actual Chow rank and does not cover preprocessing "
            "on the differential-operator source before the catalecticant, nonlinear "
            "minors, term-dependent maps, minimal syzygy functors, valuative arguments, "
            "Chow-realizability defects, border rank, exact rank for n>=6, or general "
            "Glynn optimality. Literature novelty is not established."
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
    print("GENERAL_MATCHING_ORBIT_POSTPROCESSING_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
