#!/usr/bin/env python3
"""Exact invalid-tail minors for disjoint-support (2,2) rank-one shears."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import os
from pathlib import Path
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_mixed_glynn_two_direction_shear_tail_rank as two  # noqa: E402


TAILS = two.TAILS
SUPPORTS = tuple(
    (left, right)
    for left in itertools.combinations(range(6), 2)
    for right in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate not in left], 2
    )
)
CANDIDATE_COUNT = len(SUPPORTS) * 5


def transformed_coordinate(
    tail: tuple[int, ...],
    coordinate: int,
    left: tuple[int, int],
    right: tuple[int, int],
    parameters,
):
    left_ratio, right_first, right_second = parameters
    if coordinate not in left:
        return tail[coordinate]
    left_coefficient = 1 if coordinate == left[0] else left_ratio
    right_form = right_first * tail[right[0]] + right_second * tail[right[1]]
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(
    assignment: tuple[int, ...],
    identity_count: int,
    left: tuple[int, int],
    right: tuple[int, int],
    parameters,
):
    feature = []
    for tail in TAILS:
        value = 1
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            value *= (
                tail[coordinate]
                if block < identity_count
                else transformed_coordinate(tail, coordinate, left, right, parameters)
            )
        feature.append(value)
    return feature


def witness_assignments(identity_count: int, support) -> tuple[tuple[int, ...], ...]:
    left, right = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, left, right, (1, 1, 1)
        )
        two.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def trial(candidate) -> dict[str, object]:
    support, identity_count = candidate
    left, right = support
    witnesses = witness_assignments(identity_count, support)
    common = {
        "left_support": list(left),
        "right_support": list(right),
        "identity_count": identity_count,
        "rank_at_all_one": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return {**common, "status": "RANK_DEFICIENT_AT_ALL_ONE"}

    parameters = sp.symbols("r s t")
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, left, right, parameters
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), *parameters, domain=sp.ZZ)
    terms = determinant.terms()
    monomial = len(terms) == 1 and sum(terms[0][0]) > 0 and terms[0][1] != 0
    return {
        **common,
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(terms),
        "determinant_coefficient": str(terms[0][1]) if monomial else None,
        "parameter_exponents": list(terms[0][0]) if monomial else None,
        "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
        "status": "NONZERO_TRIVARIATE_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def candidates():
    return [
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in range(1, 6)
    ]


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")

    star = json.loads(
        (ROOT / "data" / "n7_mixed_glynn_five_direction_shear_tail_rank.json").read_text(
            encoding="utf-8"
        )
    )
    if star["status"] != "EXACT_ALL_FIVE_DIRECTION_SHEAR_INVALID_TAIL_MINORS":
        raise AssertionError("coordinate-star face certificate mismatch")

    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, candidates(), chunksize=1))
    rows.sort(
        key=lambda row: (
            row["left_support"], row["right_support"], row["identity_count"]
        )
    )
    witness_samples = [
        {
            "left_support": row["left_support"],
            "right_support": row["right_support"],
            "identity_count": row["identity_count"],
            "witness_assignments_first_5": row["witness_assignments_first_5"],
        }
        for row in rows[:5]
        if "witness_assignments_first_5" in row
    ]
    for row in rows:
        row.pop("witness_assignments_first_5", None)

    status_counts = {}
    exponent_histogram = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        if row.get("parameter_exponents") is not None:
            key = "+".join(str(value) for value in row["parameter_exponents"])
            exponent_histogram[key] = exponent_histogram.get(key, 0) + 1
    complete = status_counts == {
        "NONZERO_TRIVARIATE_MONOMIAL_MINOR": CANDIDATE_COUNT
    }
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_DISJOINT_22_RANK_ONE_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_DISJOINT_22_RANK_ONE_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "binom(6,2) * binom(4,2) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "normalization": "u_left_first=1; parameters=(u_left_second,v_right_first,v_right_second)",
        "workers": args.workers,
        "status_counts": status_counts,
        "parameter_exponent_histogram": dict(sorted(exponent_histogram.items())),
        "coordinate_face_certificate": star["status"],
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family is I+u v^T with disjoint two-coordinate supports for u and v, modulo the rank-one scaling redundancy.",
            "All 90 ordered supports and five positive identity/shear multiplicity splits are represented.",
            "A monomial minor covers the full-support parameter torus; coordinate-star certificates cover every proper support face.",
            "The result does not cover overlapping supports, larger support on both sides, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.probe_index is None:
        payload = build_payload(args)
    else:
        if not 0 <= args.probe_index < CANDIDATE_COUNT:
            raise ValueError("--probe-index is outside the candidate family")
        payload = trial(candidates()[args.probe_index])
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
