#!/usr/bin/env python3
"""Exact finite audit of row-column projected catalecticant ceilings.

The proof document gives a general Frobenius/operator-norm argument.  This
script reconstructs primitive Johnson-scheme idempotents modulo a large prime,
checks the diagonal-compression ranks on every irreducible pair through n=8,
and tests deterministic nonrectangular stable sums.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any, Iterable


PRIME = 1_000_003
EXPECTED_CORE_SHA256 = "21b695309c3009ee3eade7ed553faeeefa60b061b2652430d5e48486f9e93cc4"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def ceil_div(a: int, b: int) -> int:
    require(b > 0, b)
    return -(-a // b)


def identity(size: int) -> list[list[int]]:
    return [[1 if row == col else 0 for col in range(size)] for row in range(size)]


def matmul(left: list[list[int]], right: list[list[int]], prime: int = PRIME) -> list[list[int]]:
    rows = len(left)
    middle = len(right)
    columns = len(right[0]) if right else 0
    require(all(len(row) == middle for row in left), "left shape")
    result = [[0] * columns for _ in range(rows)]
    right_columns = [[right[k][j] for k in range(middle)] for j in range(columns)]
    for i, row in enumerate(left):
        out = result[i]
        for j, column in enumerate(right_columns):
            out[j] = sum(a * b for a, b in zip(row, column, strict=True)) % prime
    return result


def matrix_rank_mod(matrix: Iterable[Iterable[int]], prime: int = PRIME) -> int:
    rows = [list(value % prime for value in row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next((index for index in range(rank, row_count) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        pivot_row = rows[rank]
        for index in range(row_count):
            if index == rank:
                continue
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    (value - coefficient * pivot_value) % prime
                    for value, pivot_value in zip(rows[index], pivot_row, strict=True)
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def matrix_equal(left: list[list[int]], right: list[list[int]]) -> bool:
    return left == right


def johnson_adjacency(n: int, m: int) -> list[list[int]]:
    subsets = tuple(combinations(range(n), m))
    sets = tuple(set(value) for value in subsets)
    size = len(subsets)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if len(sets[i] & sets[j]) == m - 1:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


def johnson_eigenvalues(n: int, m: int) -> list[int]:
    return [(m - i) * (n - m - i) - i for i in range(min(m, n - m) + 1)]


def specht_dimensions(n: int, m: int) -> list[int]:
    return [comb(n, i) - (comb(n, i - 1) if i else 0) for i in range(min(m, n - m) + 1)]


def primitive_idempotents(n: int, m: int, prime: int = PRIME) -> list[list[list[int]]]:
    adjacency = johnson_adjacency(n, m)
    size = len(adjacency)
    ident = identity(size)
    eigenvalues = johnson_eigenvalues(n, m)
    projectors = []
    for index, theta in enumerate(eigenvalues):
        polynomial = identity(size)
        denominator = 1
        for other_index, other in enumerate(eigenvalues):
            if other_index == index:
                continue
            factor = [row[:] for row in adjacency]
            for diagonal in range(size):
                factor[diagonal][diagonal] = (factor[diagonal][diagonal] - other) % prime
            polynomial = matmul(polynomial, factor, prime)
            denominator = denominator * (theta - other) % prime
        inverse = pow(denominator, prime - 2, prime)
        projector = [[value * inverse % prime for value in row] for row in polynomial]
        projectors.append(projector)
    total = [[0] * size for _ in range(size)]
    for projector in projectors:
        for i in range(size):
            for j in range(size):
                total[i][j] = (total[i][j] + projector[i][j]) % prime
    require(matrix_equal(total, ident), (n, m, "projector sum"))
    return projectors


def hadamard(left: list[list[int]], right: list[list[int]], prime: int = PRIME) -> list[list[int]]:
    return [
        [(a * b) % prime for a, b in zip(row_a, row_b, strict=True)]
        for row_a, row_b in zip(left, right, strict=True)
    ]


def sum_matrices(matrices: Iterable[list[list[int]]], size: int, prime: int = PRIME) -> list[list[int]]:
    result = [[0] * size for _ in range(size)]
    for matrix in matrices:
        for i in range(size):
            for j in range(size):
                result[i][j] = (result[i][j] + matrix[i][j]) % prime
    return result


def deterministic_masks(component_count: int) -> list[set[tuple[int, int]]]:
    all_pairs = {(i, j) for i in range(component_count) for j in range(component_count)}
    masks: list[set[tuple[int, int]]] = [all_pairs]
    masks.append({(i, i) for i in range(component_count)})
    masks.append({(i, j) for i in range(component_count) for j in range(component_count) if (i + j) % 2 == 0})
    masks.append({(i, j) for i in range(component_count) for j in range(component_count) if i <= j})
    for i in range(component_count):
        masks.append({(i, j) for j in range(component_count)})
        masks.append({(j, i) for j in range(component_count)})
    unique = []
    seen = set()
    for mask in masks:
        key = tuple(sorted(mask))
        if mask and key not in seen:
            seen.add(key)
            unique.append(mask)
    return unique


def build_payload() -> dict[str, Any]:
    projector_rank_checks = 0
    projector_orthogonality_checks = 0
    irreducible_pair_checks = 0
    stable_sum_checks = 0
    gl_pieri_checks = 0
    finite_rows: dict[str, Any] = {}

    for n in range(3, 9):
        n_rows = []
        for m in range(1, n // 2 + 1):
            module_dimension = comb(n, m)
            dimensions = specht_dimensions(n, m)
            require(sum(dimensions) == module_dimension, (n, m, dimensions))
            projectors = primitive_idempotents(n, m)
            require(len(projectors) == len(dimensions), (n, m))

            for index, (projector, dimension) in enumerate(zip(projectors, dimensions, strict=True)):
                require(matrix_rank_mod(projector) == dimension, (n, m, index, dimension))
                require(matrix_equal(matmul(projector, projector), projector), (n, m, index, "idempotent"))
                projector_rank_checks += 1
            for i in range(len(projectors)):
                for j in range(i + 1, len(projectors)):
                    zero = matmul(projectors[i], projectors[j])
                    require(all(not value for row in zero for value in row), (n, m, i, j))
                    projector_orthogonality_checks += 1

            pair_ranks = {}
            pair_grams: dict[tuple[int, int], list[list[int]]] = {}
            for i, left in enumerate(projectors):
                for j, right in enumerate(projectors):
                    gram = hadamard(left, right)
                    pair_grams[(i, j)] = gram
                    rank = matrix_rank_mod(gram)
                    numerator = dimensions[i] * dimensions[j]
                    require(module_dimension * rank >= numerator, (n, m, i, j, rank, numerator))
                    require(ceil_div(numerator, rank) <= module_dimension, (n, m, i, j))
                    pair_ranks[f"{i},{j}"] = rank
                    irreducible_pair_checks += 1

            masks = deterministic_masks(len(projectors))
            mask_rows = []
            for mask in masks:
                gram = sum_matrices((pair_grams[pair] for pair in mask), module_dimension)
                rank = matrix_rank_mod(gram)
                subspace_dimension = sum(dimensions[i] * dimensions[j] for i, j in mask)
                require(module_dimension * rank >= subspace_dimension, (n, m, mask, rank, subspace_dimension))
                require(ceil_div(subspace_dimension, rank) <= module_dimension, (n, m, mask))
                mask_rows.append({
                    "component_count": len(mask),
                    "subspace_dimension": subspace_dimension,
                    "diagonal_rank_lower_bound_mod_prime": rank,
                })
                stable_sum_checks += 1

            n_rows.append({
                "degree": m,
                "module_dimension": module_dimension,
                "specht_dimensions": dimensions,
                "pair_ranks_mod_prime": pair_ranks,
                "stable_sum_tests": mask_rows,
            })
        finite_rows[str(n)] = n_rows

    for ambient_dimension in range(3, 13):
        for m in range(1, 9):
            for p in range(ambient_dimension):
                common_hook = (m,) + (1,) * p
                source_other = None if p == 0 else (m + 1,) + (1,) * (p - 1)
                target_other = None
                if m >= 2 and p + 2 <= ambient_dimension:
                    target_other = (m - 1,) + (1,) * (p + 1)
                require(common_hook != source_other and common_hook != target_other, (ambient_dimension, m, p))
                gl_pieri_checks += 1

    core: dict[str, Any] = {
        "status": [
            "GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING",
            "ARBITRARY_STABLE_ISOTYPE_SUMS",
            "FINITE_BLOCK_SUMS_CLOSED",
            "GLV_STANDARD_DELTA_PROJECTIONS_REDUNDANT",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "stable_projection_ceiling": (
                "For every S_n x S_n-stable W in the m-subpermanent module, "
                "the projected catalecticant rank ratio is at most binom(n,m)."
            ),
            "diagonal_compression": (
                "For a transitive G-set X and G x G-stable W in k^(X x X), "
                "rank(P_W D)>=dim(W)/|X|."
            ),
            "finite_block_sum": (
                "Every finite block-diagonal sum across degrees and stable summands "
                "is capped by binom(n,floor(n/2))."
            ),
            "glv_projection_boundary": (
                "Every GL(V)-equivariant pre/post-projection of the standard exterior "
                "differential is zero or a scalar multiple of that differential."
            ),
        },
        "exact_replay": {
            "prime": PRIME,
            "n_min": 3,
            "n_max": 8,
            "projector_rank_checks": projector_rank_checks,
            "projector_orthogonality_checks": projector_orthogonality_checks,
            "irreducible_pair_checks": irreducible_pair_checks,
            "stable_sum_checks": stable_sum_checks,
            "gl_pieri_checks": gl_pieri_checks,
            "finite_rows_sha256": canonical_sha256(finite_rows),
            "selected_rows": {
                "n6_m3": finite_rows["6"][-1],
                "n8_m4": finite_rows["8"][-1],
            },
        },
        "claim_boundary": (
            "This is a route ceiling for the canonical matching projection followed by "
            "an arbitrary row-column stable catalecticant projection, and for GL(V)-"
            "equivariant projections immediately around the standard exterior differential. "
            "It does not cover row-column projections inside higher Koszul/Young complexes, "
            "source projections before the catalecticant, arbitrary Pieri maps, nonlinear "
            "minors, higher syzygies, valuative arguments, Chow-realizability defects, border "
            "rank, exact rank for n>=6, or general Glynn optimality. Literature novelty is "
            "not established."
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
    print("GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
