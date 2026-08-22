#!/usr/bin/env python3
"""Exact perm7 minors for overlapping (2,3)/(3,2) nilpotent shears."""

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
import n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank as core22  # noqa: E402


TAILS = core22.TAILS
SUPPORTS = tuple(
    (shape, core, extra)
    for shape in ("extra_right", "extra_left")
    for core in itertools.combinations(range(6), 2)
    for extra in range(6)
    if extra not in core
)
CANDIDATE_COUNT = len(SUPPORTS) * 5


def transformed_coordinate(tail, coordinate, shape, core, extra, parameters):
    ratio, scale, extra_coefficient = parameters
    first, second = core
    if shape == "extra_right":
        left = core
        if coordinate not in left:
            return tail[coordinate]
        right_form = scale * (-ratio * tail[first] + tail[second])
        right_form += extra_coefficient * tail[extra]
        left_coefficient = 1 if coordinate == first else ratio
    elif shape == "extra_left":
        left = core + (extra,)
        if coordinate not in left:
            return tail[coordinate]
        right_form = scale * (-ratio * tail[first] + tail[second])
        if coordinate == first:
            left_coefficient = 1
        elif coordinate == second:
            left_coefficient = ratio
        else:
            left_coefficient = extra_coefficient
    else:
        raise ValueError(shape)
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(
    assignment, identity_count, shape, core, extra, parameters
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
                else transformed_coordinate(
                    tail, coordinate, shape, core, extra, parameters
                )
            )
        feature.append(value)
    return feature


def witness_assignments(identity_count, support, point):
    shape, core, extra = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, shape, core, extra, point
        )
        core22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def cover_trial(candidate):
    support, identity_count = candidate
    shape, core, extra = support
    parameters = sp.symbols("r t w")
    gcd_polynomial = None
    minors = []
    witness_sample_sets = []
    for point in ((1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 3, 5)):
        witnesses = witness_assignments(identity_count, support, point)
        if len(witnesses) != len(TAILS):
            continue
        matrix = sp.Matrix(
            [
                assignment_feature(
                    assignment,
                    identity_count,
                    shape,
                    core,
                    extra,
                    parameters,
                )
                for assignment in witnesses
            ]
        ).T
        determinant = sp.Poly(
            matrix.det(method="domain-ge"), *parameters, domain=sp.ZZ
        )
        if determinant.is_zero:
            continue
        gcd_polynomial = (
            determinant if gcd_polynomial is None else sp.gcd(gcd_polynomial, determinant)
        )
        minors.append(
            {
                "selection_point": list(point),
                "determinant_total_degree": determinant.total_degree(),
                "determinant_term_count": len(determinant.terms()),
                "determinant_factorization": str(sp.factor(determinant.as_expr())),
            }
        )
        witness_sample_sets.append(
            {
                "selection_point": list(point),
                "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
            }
        )
        gcd_terms = gcd_polynomial.terms()
        if len(gcd_terms) == 1 and gcd_terms[0][1] != 0:
            break
    gcd_terms = [] if gcd_polynomial is None else gcd_polynomial.terms()
    covered = len(gcd_terms) == 1 and gcd_terms[0][1] != 0
    return {
        "shape": shape,
        "core_support": list(core),
        "extra_coordinate": extra,
        "identity_count": identity_count,
        "minor_count": len(minors),
        "minors": minors,
        "gcd_factorization": (
            str(sp.factor(gcd_polynomial.as_expr()))
            if gcd_polynomial is not None
            else None
        ),
        "gcd_exponents": list(gcd_terms[0][0]) if covered else None,
        "witness_sample_sets": witness_sample_sets,
        "status": (
            "DENSE_TORUS_COVERED_BY_EXACT_MINORS"
            if covered
            else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS"
        ),
    }


def candidates():
    return [(support, count) for support in SUPPORTS for count in range(1, 6)]


def build_payload(args):
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    lower = json.loads(
        (ROOT / "data" / "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json").read_text(
            encoding="utf-8"
        )
    )
    if lower["status"] != "EXACT_ALL_OVERLAPPING_22_NILPOTENT_SHEAR_INVALID_TAIL_MINORS":
        raise AssertionError("overlapping-core face certificate mismatch")
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(cover_trial, candidates(), chunksize=1))
    rows.sort(
        key=lambda row: (
            row["shape"],
            row["core_support"],
            row["extra_coordinate"],
            row["identity_count"],
        )
    )
    samples = [
        {
            "shape": row["shape"],
            "core_support": row["core_support"],
            "extra_coordinate": row["extra_coordinate"],
            "identity_count": row["identity_count"],
            "witness_sample_sets": row["witness_sample_sets"],
        }
        for row in rows[:5]
    ]
    for row in rows:
        row.pop("witness_sample_sets", None)
    status_counts = {}
    for row in rows:
        status = row["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
    complete = status_counts == {
        "DENSE_TORUS_COVERED_BY_EXACT_MINORS": CANDIDATE_COUNT
    }
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_OVERLAPPING_23_32_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_OVERLAPPING_23_32_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "shape_counts": {"extra_right": 60, "extra_left": 60},
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "2 * binom(6,2) * 4 * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parametrization": "orthogonal two-coordinate core plus one extra coordinate on exactly one side",
        "workers": args.workers,
        "status_counts": status_counts,
        "lower_face_certificate": lower["status"],
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family has support sizes (2,3) or (3,2), overlap two, and v^T u=0 on the overlapping core.",
            "All 120 oriented supports and five positive identity/shear multiplicity splits are represented.",
            "Exact minor gcds cover the dense parameter torus; proper parameter faces reduce to certified overlapping-two or disjoint/star layers.",
            "The result does not cover larger overlapping supports, non-unipotent rank-one updates, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main():
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
        payload = cover_trial(candidates()[args.probe_index])
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
