#!/usr/bin/env python3
"""Exact perm7 minors for singleton-versus-triple rank-one updates."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import math
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
    (orientation, shared, extras)
    for orientation in ("left_singleton", "right_singleton")
    for shared in range(6)
    for extras in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != shared], 2
    )
)
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "PROJECTIVE_SUPPORT_CLOSURE_COVERED_BY_ONE_EXACT_MINOR"
SELECTION_POINTS = ((1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 3, 2))


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("s t w")


def transformed_coordinate(tail, coordinate, support, s, t, w):
    orientation, shared, extras = support
    first, second = extras
    if orientation == "left_singleton":
        if coordinate != shared:
            return tail[coordinate]
        right_form = t * (
            tail[shared] + s * tail[first] + w * tail[second]
        )
        return tail[shared] + right_form
    if orientation == "right_singleton":
        if coordinate not in (shared, first, second):
            return tail[coordinate]
        right_form = t * tail[shared]
        if coordinate == shared:
            left_coefficient = 1
        elif coordinate == first:
            left_coefficient = s
        else:
            left_coefficient = w
        return tail[coordinate] + left_coefficient * right_form
    raise ValueError(orientation)


def assignment_feature(assignment, identity_count, support, s, t, w):
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
                    tail, coordinate, support, s, t, w
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
    s, t, w = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, s, t, w
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), s, t, w, domain=sp.ZZ
    )
    return witnesses, determinant


def allowed_boundary_polynomials():
    s, t, w = parameter_symbols()
    return {
        "support_face_s": sp.Poly(s, s, t, w, domain=sp.QQ).monic(),
        "identity_face_t": sp.Poly(t, s, t, w, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, s, t, w, domain=sp.QQ).monic(),
        "singular_face_1_plus_t": sp.Poly(
            1 + t, s, t, w, domain=sp.QQ
        ).monic(),
    }


def allowed_boundary_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    s, t, w = parameter_symbols()
    allowed = allowed_boundary_polynomials()
    _content, factors = sp.Poly(
        polynomial.as_expr(), s, t, w, domain=sp.QQ
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
    orientation, shared, extras = support
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
        attempt = {
            "selection_point": list(point),
            "rank": len(witnesses),
            "determinant_total_degree": determinant.total_degree(),
            "determinant_term_count": len(determinant.terms()),
            "determinant_factorization": str(sp.factor(determinant.as_expr())),
            "allowed_boundary_factor_exponents": exponents,
            "unresolved_factors": unresolved,
        }
        attempts.append(attempt)
        if covered:
            witness_sample = [list(assignment) for assignment in witnesses[:5]]
            break
    selected = attempts[-1] if attempts else None
    covered = bool(selected) and not selected.get("unresolved_factors", [1])
    return {
        "orientation": orientation,
        "shared_coordinate": shared,
        "extra_coordinates": list(extras),
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
        "disjoint_two_direction": exact_status(
            "data/n7_mixed_glynn_two_direction_shear_tail_rank.json"
        ),
    }


def build_payload(args):
    family = candidates()
    if len(family) != 2 * 6 * math.comb(5, 2) * 5:
        raise AssertionError("singleton-versus-triple support inventory drift")
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
            row["extra_coordinates"],
            row["identity_count"],
        )
    )
    samples = [
        {
            "orientation": row["orientation"],
            "shared_coordinate": row["shared_coordinate"],
            "extra_coordinates": row["extra_coordinates"],
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
            "EXACT_ALL_SINGLETON_TRIPLE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_SINGLETON_TRIPLE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * 6 * binom(5,2) * 5",
        "orientation_count": 2,
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": len(MULTIPLICITY_SPLITS),
        "candidate_count": CANDIDATE_COUNT,
        "parametrizations": {
            "left_singleton": (
                "u=e_a, v=t*(e_a^*+s*e_b^*+w*e_c^*) for distinct a,b,c"
            ),
            "right_singleton": (
                "u=e_a+s*e_b+w*e_c, v=t*e_a^* for distinct a,b,c"
            ),
        },
        "determinant_identity": "det(I+u*v^T)=1+t",
        "dense_chart_condition": "s*t*w*(1+t) != 0",
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 4.0,
        "status_counts": status_counts,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update whose supports have sizes one and three and overlap in the singleton coordinate, in both orientations.",
            "All 120 oriented supports and five positive identity/update multiplicity splits are represented.",
            "Each dense chart is covered by one exact 42-by-42 minor; no multivariate-gcd inference is used.",
            "The s=0 and w=0 faces are imported singleton-versus-pair layers, the projective face where the normalized shared coefficient vanishes is an imported disjoint two-direction shear, t=0 is the identity control, and 1+t=0 is outside GL(6).",
            "Consequently every nonidentity invertible update in the projective singleton-versus-triple support closure is covered.",
            "The result does not cover multi-coordinate support on both sides, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, exact rank 64, or border rank.",
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
        rows = [
            cover_trial(candidate) for candidate in candidates()[: args.probe_count]
        ]
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
