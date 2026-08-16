#!/usr/bin/env python3
"""Exact replay for same-factor-span Chow derivative overlaps.

The theorem-facing proof is in docs/general_same_span_chow_overlap.md.
This script uses exact Fraction elimination to verify the sharp quadratic
bound, its explicit equality constructions, the distinction between primal
and dual shared directions, and the Kruskal--Katona higher-degree corollary.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path
from typing import Iterable


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rank_fraction(matrix: list[list[int | Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [[Fraction(value) for value in row] for row in matrix]
    width = len(rows[0])
    require(all(len(row) == width for row in rows), "ragged matrix")
    rank = 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][column]
        rows[rank] = [entry / value for entry in rows[rank]]
        for index in range(len(rows)):
            if index == rank:
                continue
            coefficient = rows[index][column]
            if coefficient:
                rows[index] = [
                    left - coefficient * right
                    for left, right in zip(rows[index], rows[rank], strict=True)
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def matrix_multiply(
    left: list[list[int]],
    right: list[list[int]],
) -> list[list[int]]:
    require(left and right, "empty matrix")
    require(len(left[0]) == len(right), (len(left[0]), len(right)))
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(column) for column in zip(*matrix, strict=True)]


def identity(size: int) -> list[list[int]]:
    return [
        [int(row == column) for column in range(size)]
        for row in range(size)
    ]


def block_diagonal(blocks: Iterable[list[list[int]]]) -> list[list[int]]:
    values = list(blocks)
    size = sum(len(block) for block in values)
    result = [[0] * size for _ in range(size)]
    offset = 0
    for block in values:
        require(block and all(len(row) == len(block) for row in block), block)
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                result[offset + i][offset + j] = value
        offset += len(block)
    return result


HADAMARD_2 = [[1, 1], [1, -1]]
ORTHOGONAL_3 = [
    [1, 1, 1],
    [1, -1, 0],
    [1, 1, -2],
]


def sharp_transition(n: int, dual_shared: int) -> list[list[int]]:
    """Transition matrix attaining the quadratic bound."""
    require(2 <= n and 0 <= dual_shared <= n, (n, dual_shared))
    remainder = n - dual_shared
    if remainder == 0:
        return identity(n)
    if remainder == 1:
        matrix = identity(n)
        matrix[0][-1] = 1
        return matrix

    blocks: list[list[list[int]]] = [
        [[1]] for _ in range(dual_shared)
    ]
    if remainder % 2 == 0:
        blocks.extend(HADAMARD_2 for _ in range(remainder // 2))
    else:
        require(remainder >= 3, remainder)
        blocks.extend(HADAMARD_2 for _ in range((remainder - 3) // 2))
        blocks.append(ORTHOGONAL_3)
    return block_diagonal(blocks)


def one_sparse_column_count(matrix: list[list[int]]) -> int:
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "not square")
    return sum(
        sum(int(matrix[row][column] != 0) for row in range(size)) == 1
        for column in range(size)
    )


def off_diagonal_square_constraint(
    transition: list[list[int]],
) -> list[list[int]]:
    """Matrix for d -> offdiag(A diag(d) A^T)."""
    size = len(transition)
    require(all(len(row) == size for row in transition), "not square")
    return [
        [
            transition[left][column] * transition[right][column]
            for column in range(size)
        ]
        for left, right in combinations(range(size), 2)
    ]


def common_diagonal_dimension(transition: list[list[int]]) -> int:
    size = len(transition)
    return size - rank_fraction(off_diagonal_square_constraint(transition))


def common_quadratic_dimension(transition: list[list[int]]) -> int:
    size = len(transition)
    constraint_rank = rank_fraction(
        off_diagonal_square_constraint(transition)
    )
    return comb(size, 2) - constraint_rank


def quadratic_bound(n: int, dual_shared: int) -> int:
    return comb(n, 2) - ceil((n - dual_shared) / 2)


def colex_rank(subset: tuple[int, ...]) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def colex_subsets(n: int, m: int) -> tuple[tuple[int, ...], ...]:
    layer = tuple(sorted(combinations(range(n), m), key=colex_rank))
    require(
        tuple(colex_rank(value) for value in layer)
        == tuple(range(len(layer))),
        (n, m),
    )
    return layer


def degree_two_shadow_profile(n: int, m: int) -> tuple[int, ...]:
    require(2 <= m <= n, (n, m))
    shadow: set[tuple[int, int]] = set()
    profile = [0]
    for subset in colex_subsets(n, m):
        shadow.update(combinations(subset, 2))
        profile.append(len(shadow))
    require(profile[-1] == comb(n, 2), (n, m, profile[-1]))
    return tuple(profile)


def higher_overlap_cap(n: int, m: int, dual_shared: int) -> dict[str, int]:
    cap = quadratic_bound(n, dual_shared)
    profile = degree_two_shadow_profile(n, m)
    maximum = max(
        dimension
        for dimension, shadow in enumerate(profile)
        if shadow <= cap
    )
    first_excluded = maximum + 1
    return {
        "n": n,
        "m": m,
        "dual_shared": dual_shared,
        "quadratic_cap": cap,
        "higher_degree_overlap_cap": maximum,
        "shadow_at_cap": profile[maximum],
        "first_excluded_dimension": first_excluded,
        "shadow_at_first_excluded": profile[first_excluded],
    }


def build_payload() -> dict[str, object]:
    sharp_rows = []
    for n in range(2, 13):
        for dual_shared in range(n + 1):
            transition = sharp_transition(n, dual_shared)
            observed_shared = one_sparse_column_count(transition)
            diagonal_dimension = common_diagonal_dimension(transition)
            quadratic_dimension = common_quadratic_dimension(transition)
            expected_diagonal = dual_shared + (n - dual_shared) // 2
            expected_quadratic = quadratic_bound(n, dual_shared)
            require(observed_shared == dual_shared, (
                "shared count",
                n,
                dual_shared,
                observed_shared,
            ))
            require(diagonal_dimension == expected_diagonal, (
                "diagonal dimension",
                n,
                dual_shared,
                diagonal_dimension,
                expected_diagonal,
            ))
            require(quadratic_dimension == expected_quadratic, (
                "quadratic dimension",
                n,
                dual_shared,
                quadratic_dimension,
                expected_quadratic,
            ))
            sharp_rows.append({
                "n": n,
                "dual_shared": dual_shared,
                "common_diagonal_dimension": diagonal_dimension,
                "common_quadratic_dimension": quadratic_dimension,
            })

    dual_transition = [
        [0, 1, 0, -1],
        [0, 0, 0, 1],
        [0, 0, -1, -1],
        [1, 0, 0, 1],
    ]
    primal_transition = [
        [0, 1, 0, 0],
        [-1, 1, -1, 1],
        [0, 0, -1, 0],
        [1, 0, 0, 0],
    ]
    require(
        matrix_multiply(transpose(dual_transition), primal_transition)
        == identity(4),
        "primal transition is not inverse transpose",
    )
    distinction = {
        "dual_shared_direction_count": one_sparse_column_count(
            dual_transition
        ),
        "primal_shared_factor_count": one_sparse_column_count(
            primal_transition
        ),
        "common_quadratic_dimension": common_quadratic_dimension(
            dual_transition
        ),
    }
    require(
        distinction
        == {
            "dual_shared_direction_count": 3,
            "primal_shared_factor_count": 1,
            "common_quadratic_dimension": 5,
        },
        distinction,
    )

    central_rows = [
        higher_overlap_cap(n, n // 2, 0)
        for n in range(4, 13)
    ]
    expected_central = {
        4: (4, 4),
        5: (7, 7),
        6: (12, 11),
        7: (17, 21),
        8: (24, 36),
        9: (31, 71),
        10: (40, 127),
        11: (49, 253),
        12: (60, 463),
    }
    require(
        {
            row["n"]: (
                row["quadratic_cap"],
                row["higher_degree_overlap_cap"],
            )
            for row in central_rows
        }
        == expected_central,
        central_rows,
    )

    core = {
        "status": [
            "GENERAL_SAME_SPAN_QUADRATIC_OVERLAP_THEOREM",
            "SHARP_DUAL_FRAME_BOUND",
            "KRUSKAL_KATONA_HIGHER_DEGREE_COROLLARY",
            "EXACT_RATIONAL_REPLAYED",
        ],
        "theorem": {
            "quadratic_identity": (
                "dim(S_2(x) intersect S_2(y))="
                "binom(n,2)-n+kappa, where kappa is the intersection "
                "dimension of the two dual diagonal-square spaces"
            ),
            "sharp_bound": (
                "dim(S_2(x) intersect S_2(y)) <= "
                "binom(n,2)-ceil((n-s_dual)/2)"
            ),
            "dual_shared_definition": (
                "s_dual is the number of common projective directions "
                "between the two dual factor bases"
            ),
            "higher_degree_corollary": (
                "the degree-m overlap is at most the largest b whose "
                "Kruskal-Katona degree-two shadow does not exceed the "
                "sharp quadratic cap"
            ),
        },
        "sharp_construction_case_count": len(sharp_rows),
        "sharp_construction_table_sha256": canonical_hash(sharp_rows),
        "sharp_selected_rows": [
            row
            for row in sharp_rows
            if (row["n"], row["dual_shared"])
            in {
                (4, 0),
                (4, 3),
                (6, 0),
                (6, 3),
                (6, 5),
                (6, 6),
                (8, 0),
                (8, 4),
                (8, 8),
                (10, 0),
            }
        ],
        "dual_primal_distinction": distinction,
        "central_no_dual_shared_rows": central_rows,
        "claim_boundary": (
            "The theorem concerns two independent-factor Chow terms with "
            "the same n-dimensional factor span. It bounds literal "
            "derivative-space overlap, not a coupled catalectic image or "
            "the matched-difference map. Unequal or degenerate factor "
            "spans remain open. No unrestricted Chow-rank bound changes."
        ),
    }
    return {**core, "core_sha256": canonical_hash(core)}


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
    print("GENERAL_SAME_SPAN_CHOW_OVERLAP_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
