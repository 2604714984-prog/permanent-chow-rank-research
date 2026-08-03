#!/usr/bin/env python3
"""Exact coordinate-line and tangent diagnostics for the n=6 central space.

The ambient vector space is the 400-dimensional central derivative space
spanned by the 3-by-3 subpermanents ``P_{I,J}``. The script proves finite
combinatorial statements about the first catalecticant ``C_{1,2}`` on this
coordinate basis. It does not prove an exact Chow-rank result for ``perm_6``.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable

N = 6
PRIME = 1_000_003
Triple = tuple[int, int, int]
BasisIndex = tuple[Triple, Triple]


def triples() -> list[Triple]:
    return list(combinations(range(N), 3))


def pairs() -> list[tuple[int, int]]:
    return list(combinations(range(N), 2))


def basis_indices() -> list[BasisIndex]:
    ts = triples()
    return [(rows, cols) for rows in ts for cols in ts]


def line_rank_from_overlap(row_overlap: int, column_overlap: int) -> int:
    """Rank of ``C_{1,2}(a P_{I,J}+b P_{I',J'})`` for nonzero ``a,b``.

    The two index pairs must be distinct. The union of the two matching
    matrices has 18 edges. Each shared variable merges two edges into one
    rank-one star, and each shared output does the same. The two kinds of
    stars are disjoint for distinct basis points.
    """

    if not 0 <= row_overlap <= 3 or not 0 <= column_overlap <= 3:
        raise ValueError("overlap values must lie between 0 and 3")
    if row_overlap == column_overlap == 3:
        raise ValueError("the two basis points must be distinct")
    shared_variables = row_overlap * column_overlap
    shared_outputs = comb(row_overlap, 2) * comb(column_overlap, 2)
    return 18 - shared_variables - shared_outputs


def derivative_edges(index: BasisIndex) -> list[tuple[tuple[int, int], BasisIndex]]:
    """Return variable/output edges of the first catalecticant matching."""

    rows, cols = index
    edges: list[tuple[tuple[int, int], BasisIndex]] = []
    for row in rows:
        for col in cols:
            output_rows = tuple(value for value in rows if value != row)
            output_cols = tuple(value for value in cols if value != col)
            edges.append(((row, col), (output_rows, output_cols)))
    return edges


def sparse_rank_mod_prime(
    columns: Iterable[dict[int, int]],
    prime: int = PRIME,
) -> int:
    """Return the exact rank over ``F_prime`` by sparse column elimination."""

    pivots: dict[int, dict[int, int]] = {}
    rank = 0
    for raw_column in columns:
        column = {
            row: value % prime
            for row, value in raw_column.items()
            if value % prime
        }
        while column:
            pivot = min(column)
            if pivot not in pivots:
                inverse = pow(column[pivot], prime - 2, prime)
                column = {
                    row: value * inverse % prime
                    for row, value in column.items()
                    if value * inverse % prime
                }
                pivots[pivot] = column
                rank += 1
                break

            factor = column[pivot]
            pivot_column = pivots[pivot]
            for row, value in pivot_column.items():
                updated = (column.get(row, 0) - factor * value) % prime
                if updated:
                    column[row] = updated
                else:
                    column.pop(row, None)
    return rank


def tangent_certificate() -> dict[str, object]:
    """Certify the tangent dimension at one coordinate point.

    Row-column permutations act transitively on the 400 coordinate points,
    so one exact representative controls all of them.
    """

    basis = basis_indices()
    base: BasisIndex = ((0, 1, 2), (0, 1, 2))
    active_variables = {variable for variable, _ in derivative_edges(base)}
    active_outputs = {output for _, output in derivative_edges(base)}

    violation_keys: set[tuple[BasisIndex, tuple[int, int]]] = set()
    violations_by_column: list[list[tuple[BasisIndex, tuple[int, int]]]] = []
    tangent_coordinate_directions: list[BasisIndex] = []

    for index in basis:
        violations = [
            (output, variable)
            for variable, output in derivative_edges(index)
            if variable not in active_variables and output not in active_outputs
        ]
        violations_by_column.append(violations)
        violation_keys.update(violations)
        if not violations:
            tangent_coordinate_directions.append(index)

    row_number = {key: position for position, key in enumerate(sorted(violation_keys))}
    sparse_columns = [
        dict(Counter(row_number[key] for key in violations))
        for violations in violations_by_column
    ]
    rank_mod_prime = sparse_rank_mod_prime(sparse_columns)
    ambient_dimension = len(basis)
    nullity_mod_prime = ambient_dimension - rank_mod_prime

    explicit_tangent_count = len(tangent_coordinate_directions)
    if explicit_tangent_count != 19:
        raise AssertionError(explicit_tangent_count)
    if nullity_mod_prime != explicit_tangent_count:
        raise AssertionError((nullity_mod_prime, explicit_tangent_count))

    expected_directions = {base}
    base_rows, base_cols = base
    for index in basis:
        rows, cols = index
        if rows == base_rows and len(set(cols) & set(base_cols)) == 2:
            expected_directions.add(index)
        if cols == base_cols and len(set(rows) & set(base_rows)) == 2:
            expected_directions.add(index)
    if set(tangent_coordinate_directions) != expected_directions:
        raise AssertionError("unexpected tangent-coordinate directions")

    # The 19 explicit coordinate directions show characteristic-zero
    # nullity >= 19. Rank 381 modulo PRIME shows characteristic-zero rank
    # >= 381, hence nullity <= 19. Therefore the rational tangent dimension
    # is exactly 19.
    return {
        "representative": {
            "rows": list(base_rows),
            "columns": list(base_cols),
        },
        "ambient_affine_dimension": ambient_dimension,
        "violation_equations": len(violation_keys),
        "tangent_map_rank_mod_prime": rank_mod_prime,
        "explicit_tangent_coordinate_directions": explicit_tangent_count,
        "affine_tangent_dimension_over_Q": explicit_tangent_count,
        "projective_tangent_dimension_over_Q": explicit_tangent_count - 1,
        "transitivity_covers_coordinate_points": ambient_dimension,
    }


def pair_distribution() -> dict[str, object]:
    basis = basis_indices()
    rank_distribution: Counter[int] = Counter()
    overlap_distribution: Counter[tuple[int, int]] = Counter()
    overlap_types_by_rank: defaultdict[int, Counter[tuple[int, int]]] = defaultdict(Counter)

    checked = 0
    for first, second in combinations(basis, 2):
        row_overlap = len(set(first[0]) & set(second[0]))
        column_overlap = len(set(first[1]) & set(second[1]))
        rank = line_rank_from_overlap(row_overlap, column_overlap)
        rank_distribution[rank] += 1
        overlap_distribution[(row_overlap, column_overlap)] += 1
        overlap_types_by_rank[rank][(row_overlap, column_overlap)] += 1
        checked += 1

    expected_pairs = comb(len(basis), 2)
    if checked != expected_pairs:
        raise AssertionError((checked, expected_pairs))

    expected_rank_distribution = {
        9: 3_600,
        13: 16_200,
        15: 3_600,
        16: 32_400,
        17: 16_200,
        18: 7_800,
    }
    if dict(sorted(rank_distribution.items())) != expected_rank_distribution:
        raise AssertionError(rank_distribution)

    rank_nine_types = set(overlap_types_by_rank[9])
    if rank_nine_types != {(3, 2), (2, 3)}:
        raise AssertionError(rank_nine_types)
    if min(rank for rank in rank_distribution if rank > 9) != 13:
        raise AssertionError("the rank gap after 9 was not reproduced")

    def encode_counter(counter: Counter[tuple[int, int]]) -> dict[str, int]:
        return {
            f"{row_overlap},{column_overlap}": count
            for (row_overlap, column_overlap), count in sorted(counter.items())
        }

    return {
        "coordinate_basis_size": len(basis),
        "unordered_pairs_checked": checked,
        "rank_distribution": {
            str(rank): count for rank, count in sorted(rank_distribution.items())
        },
        "overlap_distribution": encode_counter(overlap_distribution),
        "overlap_types_by_rank": {
            str(rank): encode_counter(counter)
            for rank, counter in sorted(overlap_types_by_rank.items())
        },
        "rank_nine_overlap_types": [[2, 3], [3, 2]],
        "next_rank_after_nine": 13,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "data"
        / "n6_coordinate_secant_audit.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = {
        "status": "COMPUTATION_REPLAYED",
        "scope": "coordinate first-catalectic lines and tangent space inside D_3(perm_6)",
        "pair_audit": pair_distribution(),
        "tangent_audit": tangent_certificate(),
        "mathematical_claim_boundary": (
            "This is a route diagnostic. It does not certify ChowRank(perm_6)=32."
        ),
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("N6_COORDINATE_SECANT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
