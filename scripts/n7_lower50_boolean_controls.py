#!/usr/bin/env python3
"""Bounded finite controls for the Boolean lemmas in the lower-50 audit.

The exhaustive F_2 calculation is a falsifier and interface check.  The
characteristic-zero theorem is proved separately in the audit note.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


N = 7


def squarefree_basis(degree: int) -> tuple[int, ...]:
    return tuple(
        sum(1 << index for index in subset)
        for subset in itertools.combinations(range(N), degree)
    )


DEGREE_THREE = squarefree_basis(3)
DEGREE_FOUR = squarefree_basis(4)
INDEX_FOUR = {monomial: index for index, monomial in enumerate(DEGREE_FOUR)}


def rank_bits(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def vector_basis(vectors: list[int]) -> tuple[int, ...]:
    pivots: dict[int, int] = {}
    for vector in vectors:
        row = vector
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return tuple(pivots[pivot] for pivot in sorted(pivots, reverse=True))


def multiply_linear_by_cubic(linear: int, cubic: int) -> int:
    output = 0
    available = linear & ~cubic
    while available:
        variable = available & -available
        available ^= variable
        output ^= 1 << INDEX_FOUR[cubic | variable]
    return output


def all_two_planes() -> tuple[tuple[int, int], ...]:
    planes: dict[frozenset[int], tuple[int, int]] = {}
    for left in range(1, 1 << N):
        for right in range(left + 1, 1 << N):
            if right == left:
                continue
            plane = frozenset((0, left, right, left ^ right))
            planes.setdefault(plane, (left, right))
    return tuple(planes.values())


def orthogonal_kernel(left: int, right: int) -> tuple[int, ...]:
    vectors = [
        vector
        for vector in range(1, 1 << N)
        if (vector & left).bit_count() % 2 == 0
        and (vector & right).bit_count() % 2 == 0
    ]
    basis = vector_basis(vectors)
    assert len(basis) == 5
    return basis


def build_certificate() -> dict[str, object]:
    planes = all_two_planes()
    assert len(planes) == 2_667
    product_ranks = []
    for left, right in planes:
        basis = orthogonal_kernel(left, right)
        rows = [
            multiply_linear_by_cubic(linear, cubic)
            for linear in basis
            for cubic in DEGREE_THREE
        ]
        product_ranks.append(rank_bits(rows))

    no_socle_columns = []
    for cubic in DEGREE_THREE:
        column = 0
        for variable in range(N):
            product = multiply_linear_by_cubic(1 << variable, cubic)
            column |= product << (variable * len(DEGREE_FOUR))
        no_socle_columns.append(column)

    assert min(product_ranks) == max(product_ranks) == len(DEGREE_FOUR)
    assert rank_bits(no_socle_columns) == len(DEGREE_THREE)
    return {
        "schema_version": 1,
        "field": "F_2",
        "five_planes_checked": len(planes),
        "minimum_rank_W_times_A3": min(product_ranks),
        "dimension_A4": len(DEGREE_FOUR),
        "degree_three_no_socle_rank": rank_bits(no_socle_columns),
        "dimension_A3": len(DEGREE_THREE),
        "claim_boundary": (
            "Exhaustive finite-field falsifier only; the arbitrary-W "
            "characteristic-zero Boolean quotient lemma is proved in the "
            "v6 core audit note."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_certificate()
    if args.json is not None:
        args.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("lower-50 Boolean control payload mismatch")
        print("LOWER50_BOOLEAN_CONTROLS_PASS")
    if args.json is None and args.verify_json is None:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
