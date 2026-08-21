#!/usr/bin/env python3
"""Exact perm7 minors for overlap-one (2,2) rank-one updates."""

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
import n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank as nil22  # noqa: E402


TAILS = nil22.TAILS
SUPPORTS = tuple(
    (shared, left_extra, right_extra)
    for shared in range(6)
    for left_extra in range(6)
    if left_extra != shared
    for right_extra in range(6)
    if right_extra not in (shared, left_extra)
)
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "DENSE_INVERTIBLE_CHART_COVERED_BY_ONE_EXACT_MINOR"
SELECTION_POINTS = ((1, 2, 1), (2, 1, 1), (1, 3, 2), (3, 2, 2))


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("r s t")


def transformed_coordinate(tail, coordinate, support, r, s, t):
    shared, left_extra, right_extra = support
    if coordinate not in (shared, left_extra):
        return tail[coordinate]
    right_form = t * (s * tail[shared] + tail[right_extra])
    left_coefficient = 1 if coordinate == shared else r
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(assignment, identity_count, support, r, s, t):
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
                    tail, coordinate, support, r, s, t
                )
            )
        feature.append(value)
    return feature


def witness_assignments(candidate, point):
    support, identity_count = candidate
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, support, *point
        )
        nil22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def exact_minor(candidate, point):
    witnesses = witness_assignments(candidate, point)
    if len(witnesses) != len(TAILS):
        return witnesses, None
    support, identity_count = candidate
    r, s, t = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, r, s, t
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), r, s, t, domain=sp.ZZ
    )
    return witnesses, determinant


def allowed_boundary_polynomials():
    r, s, t = parameter_symbols()
    return {
        "left_support_face_r": sp.Poly(r, r, s, t, domain=sp.QQ).monic(),
        "right_support_face_s": sp.Poly(s, r, s, t, domain=sp.QQ).monic(),
        "identity_face_t": sp.Poly(t, r, s, t, domain=sp.QQ).monic(),
        "singular_face_1_plus_s_t": sp.Poly(
            1 + s * t, r, s, t, domain=sp.QQ
        ).monic(),
    }


def allowed_boundary_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    r, s, t = parameter_symbols()
    allowed = allowed_boundary_polynomials()
    _content, factors = sp.Poly(
        polynomial.as_expr(), r, s, t, domain=sp.QQ
    ).factor_list()
    exponents = {}
    unresolved = []
    for factor, exponent in factors:
        monic = factor.monic()
        label = next(
            (name for name, allowed_factor in allowed.items() if monic == allowed_factor),
            None,
        )
        if label is None:
            unresolved.append(
                {"factor": str(factor.as_expr()), "exponent": int(exponent)}
            )
        else:
            exponents[label] = exponents.get(label, 0) + int(exponent)
    return not unresolved, exponents, unresolved


def cover_trial(candidate):
    support, identity_count = candidate
    attempts = []
    witness_sample = None
    for point in SELECTION_POINTS:
        witnesses, determinant = exact_minor(candidate, point)
        if determinant is None or determinant.is_zero:
            attempts.append(
                {"selection_point": list(point), "rank": len(witnesses)}
            )
            continue
        covered, exponents, unresolved = allowed_boundary_factorization(
            determinant
        )
        attempts.append(
            {
                "selection_point": list(point),
                "rank": len(witnesses),
                "determinant_total_degree": determinant.total_degree(),
                "determinant_term_count": len(determinant.terms()),
                "determinant_factorization": str(
                    sp.factor(determinant.as_expr())
                ),
                "allowed_boundary_factor_exponents": exponents,
                "unresolved_factors": unresolved,
            }
        )
        if covered:
            witness_sample = [list(assignment) for assignment in witnesses[:5]]
            break
    selected = attempts[-1] if attempts else None
    covered = bool(selected) and not selected.get("unresolved_factors", [1])
    return {
        "shared_coordinate": support[0],
        "left_extra_coordinate": support[1],
        "right_extra_coordinate": support[2],
        "identity_count": identity_count,
        "attempt_count": len(attempts),
        "selected_minor": selected if covered else None,
        "failed_attempts": attempts[:-1] if covered else attempts,
        "witness_assignments_first_5": witness_sample,
        "status": ROW_STATUS if covered else "UNRESOLVED_SINGLE_MINOR_FACTOR",
    }


def exact_status(relative_path):
    payload = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    status = str(payload["status"])
    if not status.startswith("EXACT_"):
        raise AssertionError(f"face certificate mismatch: {relative_path}")
    return status


def face_certificates():
    return {
        "oriented_singleton_overlap": exact_status(
            "data/n7_mixed_glynn_singleton_overlap_rank_one_update_tail_rank.json"
        ),
        "disjoint_coordinate_star": exact_status(
            "data/n7_mixed_glynn_two_direction_shear_tail_rank.json"
        ),
    }


def build_payload(args):
    family = candidates()
    if len(family) != 6 * 5 * 4 * 5:
        raise AssertionError("overlap-one support inventory drift")
    if len(family) > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    imported_certificates = face_certificates()
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(cover_trial, family, chunksize=1))
    rows.sort(
        key=lambda row: (
            row["shared_coordinate"],
            row["left_extra_coordinate"],
            row["right_extra_coordinate"],
            row["identity_count"],
        )
    )
    samples = [
        {
            "shared_coordinate": row["shared_coordinate"],
            "left_extra_coordinate": row["left_extra_coordinate"],
            "right_extra_coordinate": row["right_extra_coordinate"],
            "identity_count": row["identity_count"],
            "witness_assignments_first_5": row[
                "witness_assignments_first_5"
            ],
        }
        for row in rows[:5]
    ]
    for row in rows:
        row.pop("witness_assignments_first_5", None)
    status_counts = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    complete = status_counts == {ROW_STATUS: CANDIDATE_COUNT}
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_OVERLAP_ONE_22_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_OVERLAP_ONE_22_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "6 * 5 * 4 * 5",
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": len(MULTIPLICITY_SPLITS),
        "candidate_count": CANDIDATE_COUNT,
        "parametrization": (
            "u=e_a+r*e_b, v=t*(s*e_a^*+e_c^*) for distinct a,b,c"
        ),
        "determinant_identity": "det(I+u*v^T)=1+s*t",
        "dense_chart_condition": "r*s*t*(1+s*t) != 0",
        "allowed_boundary_divisors": list(allowed_boundary_polynomials()),
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 8.0,
        "status_counts": status_counts,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update whose two exact two-coordinate supports overlap in exactly one coordinate.",
            "All 120 ordered overlap-one supports and five positive identity/update multiplicity splits are represented.",
            "Each covered dense chart uses one exact 42-by-42 minor; no multivariate-gcd inference is used.",
            "The r=0 and projective v_c=0 faces are the two orientations of the singleton-overlap certificate; the s=0 and projective u_a=0 faces are disjoint coordinate-star layers; t=0 is the identity control; and 1+s*t=0 is outside GL(6).",
            "Consequently every nonidentity invertible update in this overlap-one support closure is covered, not only the dense exact-support chart.",
            "The result does not cover larger overlapping supports, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, exact rank 64, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--probe-count", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.probe_index is not None and args.probe_count is not None:
        raise ValueError("choose either --probe-index or --probe-count")
    if args.probe_index is not None:
        if not 0 <= args.probe_index < CANDIDATE_COUNT:
            raise ValueError("--probe-index is outside the candidate family")
        payload = cover_trial(candidates()[args.probe_index])
    elif args.probe_count is not None:
        if not 1 <= args.probe_count <= CANDIDATE_COUNT:
            raise ValueError("--probe-count is outside the candidate family")
        started = time.perf_counter()
        rows = [cover_trial(candidate) for candidate in candidates()[: args.probe_count]]
        payload = {
            "candidate_formula": "bounded prefix",
            "candidate_count": len(rows),
            "rows": rows,
            "elapsed_seconds": time.perf_counter() - started,
        }
    else:
        payload = build_payload(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
