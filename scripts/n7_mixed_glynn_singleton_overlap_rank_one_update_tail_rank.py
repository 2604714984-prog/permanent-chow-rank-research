#!/usr/bin/env python3
"""Exact perm7 minors for singleton-overlap rank-one updates."""

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
    (orientation, shared, extra)
    for orientation in ("left_singleton", "right_singleton")
    for shared in range(6)
    for extra in range(6)
    if extra != shared
)
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "DENSE_INVERTIBLE_CHART_COVERED_BY_ONE_EXACT_MINOR"
SELECTION_POINTS = ((2, 1), (1, 2), (3, 2))


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("s t")


def transformed_coordinate(tail, coordinate, support, s, t):
    orientation, shared, extra = support
    if orientation == "left_singleton":
        if coordinate != shared:
            return tail[coordinate]
        return tail[shared] + t * (s * tail[shared] + tail[extra])
    if orientation == "right_singleton":
        if coordinate not in (shared, extra):
            return tail[coordinate]
        right_form = t * tail[shared]
        left_coefficient = 1 if coordinate == shared else s
        return tail[coordinate] + left_coefficient * right_form
    raise ValueError(orientation)


def assignment_feature(assignment, identity_count, support, s, t):
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
                else transformed_coordinate(tail, coordinate, support, s, t)
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
    s, t = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, s, t
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), s, t, domain=sp.ZZ
    )
    return witnesses, determinant


def allowed_boundary_polynomials(orientation):
    s, t = parameter_symbols()
    allowed = {
        "identity_face_t": sp.Poly(t, s, t, domain=sp.QQ).monic(),
    }
    if orientation == "left_singleton":
        allowed["elementary_shear_face_s"] = sp.Poly(
            s, s, t, domain=sp.QQ
        ).monic()
        allowed["singular_face_1_plus_s_t"] = sp.Poly(
            1 + s * t, s, t, domain=sp.QQ
        ).monic()
    elif orientation == "right_singleton":
        allowed["diagonal_monomial_face_s"] = sp.Poly(
            s, s, t, domain=sp.QQ
        ).monic()
        allowed["singular_face_1_plus_t"] = sp.Poly(
            1 + t, s, t, domain=sp.QQ
        ).monic()
    else:
        raise ValueError(orientation)
    return allowed


def allowed_boundary_factorization(polynomial, orientation):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    s, t = parameter_symbols()
    allowed = allowed_boundary_polynomials(orientation)
    _content, factors = sp.Poly(
        polynomial.as_expr(), s, t, domain=sp.QQ
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
    orientation, shared, extra = support
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
            determinant, orientation
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
        "orientation": orientation,
        "shared_coordinate": shared,
        "extra_coordinate": extra,
        "identity_count": identity_count,
        "attempt_count": len(attempts),
        "selected_minor": selected if covered else None,
        "failed_attempts": attempts[:-1] if covered else attempts,
        "witness_assignments_first_5": witness_sample,
        "status": ROW_STATUS if covered else "UNRESOLVED_SINGLE_MINOR_FACTOR",
    }


def exact_status(relative_path):
    payload = json.loads(
        (ROOT / relative_path).read_text(encoding="utf-8")
    )
    status = str(payload["status"])
    if not status.startswith("EXACT_"):
        raise AssertionError(f"face certificate mismatch: {relative_path}")
    return status


def face_certificates():
    return {
        "elementary_shear": exact_status(
            "data/n7_mixed_glynn_elementary_shear_tail_rank.json"
        ),
        "invertible_monomial": exact_status(
            "data/n7_mixed_glynn_monomial_classification.json"
        ),
    }


def build_payload(args):
    family = candidates()
    if len(family) != 2 * 6 * 5 * 5:
        raise AssertionError("singleton-overlap support inventory drift")
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
            row["orientation"],
            row["shared_coordinate"],
            row["extra_coordinate"],
            row["identity_count"],
        )
    )
    samples = [
        {
            "orientation": row["orientation"],
            "shared_coordinate": row["shared_coordinate"],
            "extra_coordinate": row["extra_coordinate"],
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
            "EXACT_ALL_ORIENTED_SINGLETON_OVERLAP_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_ORIENTED_SINGLETON_OVERLAP_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * 6 * 5 * 5",
        "orientation_count": 2,
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": len(MULTIPLICITY_SPLITS),
        "candidate_count": CANDIDATE_COUNT,
        "parametrizations": {
            "left_singleton": "u=e_a, v=t*(s*e_a^*+e_c^*) for a != c",
            "right_singleton": "u=e_a+s*e_b, v=t*e_a^* for a != b",
        },
        "determinant_identities": {
            "left_singleton": "det(I+u*v^T)=1+s*t",
            "right_singleton": "det(I+u*v^T)=1+t",
        },
        "dense_chart_conditions": {
            "left_singleton": "s*t*(1+s*t) != 0",
            "right_singleton": "s*t*(1+t) != 0",
        },
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 4.0,
        "status_counts": status_counts,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update with one singleton support and one two-coordinate support sharing the singleton coordinate, in both orientations.",
            "All 60 oriented supports and five positive identity/update multiplicity splits are represented.",
            "Each dense chart uses one exact 42-by-42 minor; no multivariate-gcd inference is used.",
            "The s=0 faces are covered directly or by the imported elementary/monomial layers, t=0 is the identity control, and the displayed determinant-zero divisors are outside GL(6).",
            "The result does not cover multi-coordinate support on both sides, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, exact rank 64, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-count", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.probe_count is not None:
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
