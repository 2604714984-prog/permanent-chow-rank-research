#!/usr/bin/env python3
"""Exact replay for pairwise Chow derivative-space overlap.

The companion proof separates two statements.

1. In a transverse common-factor frame, two degree-n Chow terms sharing
   exactly s projective factors have output-degree-m derivative-space
   intersection of dimension binom(s,m).
2. Shared-factor count alone is not a global bound.  A block-rotation pair
   with no common projective factor has intersection
   2^m * binom(r,m) in degree m for n=2r and m<=r.

All calculations use exact integer/Fraction arithmetic.  The script concerns
literal derivative spaces.  It never identifies them with the coupled
catalectic image of a sum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Iterable


Exponent = tuple[int, ...]
SparseVector = dict[Exponent, int]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def sparse_rank_q(vectors: Iterable[SparseVector]) -> int:
    """Exact sparse row rank over Q."""

    pivots: dict[Exponent, dict[Exponent, Fraction]] = {}
    for raw in vectors:
        vector = {
            exponent: Fraction(coefficient)
            for exponent, coefficient in raw.items()
            if coefficient
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                if coefficient != 1:
                    vector = {
                        exponent: value / coefficient
                        for exponent, value in vector.items()
                    }
                pivots[pivot] = vector
                break
            for exponent, value in existing.items():
                updated = vector.get(exponent, Fraction(0)) - coefficient * value
                if updated:
                    vector[exponent] = updated
                else:
                    vector.pop(exponent, None)
    return len(pivots)


def multiply(left: SparseVector, right: SparseVector) -> SparseVector:
    output: defaultdict[Exponent, int] = defaultdict(int)
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                a + b
                for a, b in zip(left_exponent, right_exponent, strict=True)
            )
            output[exponent] += left_coefficient * right_coefficient
    return {
        exponent: coefficient
        for exponent, coefficient in output.items()
        if coefficient
    }


def coordinate_factor(variable_count: int, variable: int) -> SparseVector:
    exponent = [0] * variable_count
    exponent[variable] = 1
    return {tuple(exponent): 1}


def rotation_factor(variable_count: int, factor_index: int) -> SparseVector:
    """x_i+y_i or x_i-y_i in the factor pair containing factor_index."""

    block = factor_index // 2
    sign = 1 if factor_index % 2 == 0 else -1
    x_exponent = [0] * variable_count
    y_exponent = [0] * variable_count
    x_exponent[2 * block] = 1
    y_exponent[2 * block + 1] = 1
    return {
        tuple(x_exponent): 1,
        tuple(y_exponent): sign,
    }


def rotation_intersection_dimension(n: int, m: int) -> int:
    """Exact intersection with the coordinate squarefree derivative space."""

    require(n >= 2 and n % 2 == 0, ("n must be positive and even", n))
    require(0 <= m <= n, (n, m))

    projected_columns: list[SparseVector] = []
    for selected in combinations(range(n), m):
        polynomial: SparseVector = {(0,) * n: 1}
        for factor_index in selected:
            polynomial = multiply(
                polynomial,
                rotation_factor(n, factor_index),
            )
        projected_columns.append(
            {
                exponent: coefficient
                for exponent, coefficient in polynomial.items()
                if any(value >= 2 for value in exponent)
            }
        )

    # The products of m distinct independent rotated factors are independent.
    # Projecting D_m(U) modulo D_m(T) has kernel D_m(U) intersect D_m(T).
    projection_rank = sparse_rank_q(projected_columns)
    return comb(n, m) - projection_rank


def transversal_intersection_dimension(n: int, shared: int, m: int) -> int:
    """Enumerate the transverse common-factor monomial bases."""

    require(0 <= shared <= n, (n, shared))
    require(0 <= m <= n, (n, m))

    shared_labels = tuple(range(shared))
    left_only = tuple(range(shared, n))
    right_only = tuple(range(n, n + (n - shared)))
    left_factors = shared_labels + left_only
    right_factors = shared_labels + right_only

    left_basis = {
        tuple(sorted(selected))
        for selected in combinations(left_factors, m)
    }
    right_basis = {
        tuple(sorted(selected))
        for selected in combinations(right_factors, m)
    }
    return len(left_basis & right_basis)


def build_payload() -> dict[str, object]:
    transversal_rows: list[dict[str, int]] = []
    for n in range(3, 10):
        for shared in range(n + 1):
            for m in range(n + 1):
                observed = transversal_intersection_dimension(n, shared, m)
                expected = comb(shared, m) if m <= shared else 0
                require(
                    observed == expected,
                    ("transversal formula mismatch", n, shared, m, observed, expected),
                )
                transversal_rows.append(
                    {
                        "n": n,
                        "shared_factor_count": shared,
                        "output_degree": m,
                        "intersection_dimension": observed,
                    }
                )

    rotation_rows: list[dict[str, object]] = []
    for n in (4, 6, 8, 10):
        half = n // 2
        degree_rows: list[dict[str, int]] = []
        for m in range(1, n + 1):
            observed = rotation_intersection_dimension(n, m)
            expected = (2**m) * comb(half, m) if m <= half else 0
            require(
                observed == expected,
                ("rotation formula mismatch", n, m, observed, expected),
            )
            degree_rows.append(
                {
                    "output_degree": m,
                    "one_term_dimension": comb(n, m),
                    "intersection_dimension": observed,
                }
            )
        rotation_rows.append(
            {
                "n": n,
                "block_count": half,
                "common_projective_factor_count": 0,
                "degrees": degree_rows,
            }
        )

    merge_rows = [
        {
            "n": n,
            "shared_factor_count": n - 1,
            "two_terms_merge_to_one": True,
        }
        for n in range(2, 11)
    ]

    core = {
        "status": [
            "GENERAL_PAIRWISE_CHOW_OVERLAP_PROOF_DRAFT",
            "EXACT_RATIONAL_REPLAYED",
            "COMMON_FACTOR_ONLY_BOUND_REJECTED",
        ],
        "transverse_common_factor_theorem": {
            "statement": (
                "If T and U share s factors and all shared and unshared "
                "factors form one independent frame, then "
                "dim(D_m(T) intersect D_m(U))=binom(s,m)."
            ),
            "tested_n": [3, 9],
            "tested_case_count": len(transversal_rows),
            "table_sha256": canonical_hash(transversal_rows),
            "representative_cases": [
                {
                    "n": 6,
                    "shared_factor_count": 2,
                    "output_degree": 2,
                    "intersection_dimension": 1,
                },
                {
                    "n": 8,
                    "shared_factor_count": 4,
                    "output_degree": 3,
                    "intersection_dimension": 4,
                },
                {
                    "n": 9,
                    "shared_factor_count": 8,
                    "output_degree": 4,
                    "intersection_dimension": 70,
                },
            ],
        },
        "block_rotation_theorem": {
            "statement": (
                "For n=2r, T=prod_i x_i y_i and "
                "U=prod_i (x_i+y_i)(x_i-y_i), the terms share no "
                "projective factor and dim(D_m(T) intersect D_m(U))="
                "2^m binom(r,m) for m<=r, and zero for m>r."
            ),
            "rows": rotation_rows,
            "central_examples": {
                "n6_m3": 8,
                "n8_m4": 16,
                "n10_m5": 32,
            },
        },
        "minimal_support_merge": {
            "statement": (
                "Two nonzero terms sharing n-1 projective factors combine "
                "into one Chow term, so they cannot both occur in a "
                "support-minimal decomposition."
            ),
            "rows": merge_rows,
        },
        "route_decision": {
            "shared_factor_count_alone_controls_literal_overlap": False,
            "transverse_frame_formula_is_exact": True,
            "pairwise_literal_overlap_still_requires_frame_geometry": True,
            "new_unrestricted_chow_rank_bound": False,
        },
        "claim_boundary": (
            "All statements concern literal derivative spaces of two Chow "
            "terms.  No equality with the coupled catalectic image of T+U "
            "is used or claimed.  The theorem does not improve a permanent "
            "Chow-rank bound and does not classify arbitrary nontransverse "
            "pairs."
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
    print("GENERAL_PAIRWISE_CHOW_OVERLAP_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
