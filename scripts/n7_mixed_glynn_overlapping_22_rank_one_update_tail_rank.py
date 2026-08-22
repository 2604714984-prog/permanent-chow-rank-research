#!/usr/bin/env python3
"""Exact perm7 invalid-tail minors for coincident (2,2) rank-one updates."""

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
SUPPORTS = tuple(itertools.combinations(range(6), 2))
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "INVERTIBLE_CHART_COVERED_BY_EXACT_MINORS_AND_PIVOT_FACE"
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
    first, second = support
    if coordinate not in support:
        return tail[coordinate]
    right_form = t * (s * tail[first] + tail[second])
    left_coefficient = 1 if coordinate == first else r
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


def pivot_face_assignment_feature(assignment, identity_count, support, r, t):
    """Restrict to 1+s*t=0 without introducing a Laurent denominator."""
    first, second = support
    feature = []
    for tail in TAILS:
        value = 1
        right_form = -tail[first] + t * tail[second]
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            if block < identity_count or coordinate not in support:
                transformed = tail[coordinate]
            else:
                left_coefficient = 1 if coordinate == first else r
                transformed = tail[coordinate] + left_coefficient * right_form
            value *= transformed
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


def exact_pivot_face_minor(candidate, point=(1, 1)):
    support, identity_count = candidate
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = pivot_face_assignment_feature(
            assignment, identity_count, support, *point
        )
        nil22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    witnesses = tuple(pivots[column][1] for column in sorted(pivots))
    if len(witnesses) != len(TAILS):
        return witnesses, None
    r, _s, t = parameter_symbols()
    matrix = sp.Matrix(
        [
            pivot_face_assignment_feature(
                assignment, identity_count, support, r, t
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), r, t, domain=sp.ZZ)
    return witnesses, determinant


def allowed_boundary_polynomials():
    r, s, t = parameter_symbols()
    return {
        "r": sp.Poly(r, r, s, t, domain=sp.QQ).monic(),
        "s": sp.Poly(s, r, s, t, domain=sp.QQ).monic(),
        "t": sp.Poly(t, r, s, t, domain=sp.QQ).monic(),
        "nilpotent_face_r_plus_s": sp.Poly(
            r + s, r, s, t, domain=sp.QQ
        ).monic(),
        "pivot_face_1_plus_s_t": sp.Poly(
            1 + s * t, r, s, t, domain=sp.QQ
        ).monic(),
        "singular_face_1_plus_t_times_r_plus_s": sp.Poly(
            1 + t * (r + s), r, s, t, domain=sp.QQ
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


def pivot_face_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    r, _s, t = parameter_symbols()
    allowed = {
        "r": sp.Poly(r, r, t, domain=sp.QQ).monic(),
        "t": sp.Poly(t, r, t, domain=sp.QQ).monic(),
        "monomial_subface_1_plus_r_t": sp.Poly(
            1 + r * t, r, t, domain=sp.QQ
        ).monic(),
    }
    _content, factors = sp.Poly(
        polynomial.as_expr(), r, t, domain=sp.QQ
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
    gcd_polynomial = None
    minors = []
    witness_samples = []
    covered = False
    exponents = {}
    unresolved = []
    pivot_face_minor = None
    for point in SELECTION_POINTS:
        witnesses, determinant = exact_minor(candidate, point)
        if determinant is None or determinant.is_zero:
            continue
        gcd_polynomial = (
            determinant
            if gcd_polynomial is None
            else sp.gcd(gcd_polynomial, determinant)
        )
        minors.append(
            {
                "selection_point": list(point),
                "determinant_total_degree": determinant.total_degree(),
                "determinant_term_count": len(determinant.terms()),
            }
        )
        witness_samples.append(
            {
                "selection_point": list(point),
                "witness_assignments_first_5": [
                    list(assignment) for assignment in witnesses[:5]
                ],
            }
        )
        covered, exponents, unresolved = allowed_boundary_factorization(
            gcd_polynomial
        )
        if covered:
            if exponents.get("pivot_face_1_plus_s_t", 0):
                face_witnesses, face_determinant = exact_pivot_face_minor(candidate)
                if face_determinant is None or face_determinant.is_zero:
                    covered = False
                    unresolved = [{"factor": "1+s*t pivot face", "exponent": 1}]
                    break
                face_terms = face_determinant.terms()
                face_covered, face_exponents, face_unresolved = (
                    pivot_face_factorization(face_determinant)
                )
                pivot_face_minor = {
                    "equation": "1+s*t=0",
                    "selection_point_r_t": [1, 1],
                    "rank_at_selection_point": len(face_witnesses),
                    "determinant_total_degree": face_determinant.total_degree(),
                    "determinant_term_count": len(face_terms),
                    "determinant_factorization": str(
                        sp.factor(face_determinant.as_expr())
                    ),
                    "allowed_boundary_factor_exponents": face_exponents,
                    "unresolved_factors": face_unresolved,
                    "monomial_subface_matrix": (
                        "[[0,t],[1/t,0]]"
                        if face_exponents.get("monomial_subface_1_plus_r_t", 0)
                        else None
                    ),
                }
                if not face_covered:
                    covered = False
                    unresolved = [
                        {"factor": "1+s*t pivot face minor", "exponent": 1}
                    ]
                    break
            break
    return {
        "support": list(support),
        "identity_count": identity_count,
        "minor_count": len(minors),
        "minors": minors,
        "gcd_factorization": (
            str(sp.factor(gcd_polynomial.as_expr()))
            if gcd_polynomial is not None
            else None
        ),
        "allowed_boundary_factor_exponents": exponents,
        "pivot_face_minor": pivot_face_minor,
        "unresolved_factors": unresolved,
        "status": ROW_STATUS if covered else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS",
        "witness_samples": witness_samples,
    }


def exact_status(path):
    payload = json.loads(path.read_text(encoding="utf-8"))
    status = str(payload["status"])
    if not status.startswith("EXACT_"):
        raise AssertionError(f"face certificate mismatch: {path.name}")
    return status


def face_certificates():
    return [
        exact_status(ROOT / "data" / "n7_mixed_glynn_elementary_shear_tail_rank.json"),
        exact_status(ROOT / "data" / "n7_mixed_glynn_two_direction_shear_tail_rank.json"),
        exact_status(ROOT / "data" / "n7_mixed_glynn_monomial_classification.json"),
        exact_status(
            ROOT
            / "data"
            / "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json"
        ),
    ]


def build_payload(args):
    family = candidates()
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
    rows.sort(key=lambda row: (row["support"], row["identity_count"]))
    samples = [
        {
            "support": row["support"],
            "identity_count": row["identity_count"],
            "witness_samples": row["witness_samples"],
        }
        for row in rows[:5]
    ]
    for row in rows:
        row.pop("witness_samples", None)
    status_counts = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    complete = status_counts == {ROW_STATUS: CANDIDATE_COUNT}
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_COINCIDENT_22_INVERTIBLE_RANK_ONE_UPDATE_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_COINCIDENT_22_INVERTIBLE_RANK_ONE_UPDATE_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "binom(6,2) * 5",
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": len(MULTIPLICITY_SPLITS),
        "candidate_count": CANDIDATE_COUNT,
        "parametrization": "u=(1,r), v=t*(s,1) on the selected coordinate pair",
        "determinant_identity": "det(I+u*v^T)=1+t*(r+s)",
        "dense_chart_condition": "r*s*t*(r+s)*(1+t*(r+s)) != 0",
        "allowed_boundary_divisors": list(allowed_boundary_polynomials()),
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "estimated_peak_memory_gib": 8.0,
        "status_counts": status_counts,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update I+u*v^T whose two exact supports coincide on a coordinate pair.",
            "All 15 coordinate pairs and five positive identity/update multiplicity splits are represented.",
            "The affine chart covers exact two-coordinate support; coordinate faces use the imported elementary and two-direction certificates, and r+s=0 uses the imported nilpotent certificate.",
            "Whenever the generic minor vanishes on 1+s*t=0, a separately selected exact minor factors only over r, t, and the possible subface 1+r*t=0.",
            "If that face minor also vanishes on 1+r*t=0, the update matrix is [[0,t],[1/t,0]], so the imported invertible-monomial classification covers the remaining subface.",
            "The singular divisor det(I+u*v^T)=0 is outside GL(6), while t=0 is the identity control.",
            "The result does not cover larger coincident supports, distinct or partially overlapping supports, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
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
