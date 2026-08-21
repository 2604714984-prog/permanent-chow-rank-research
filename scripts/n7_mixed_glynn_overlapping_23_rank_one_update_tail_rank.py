#!/usr/bin/env python3
"""Exact perm7 minors for overlapping (2,3)/(3,2) rank-one updates."""

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
import n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank as nil23  # noqa: E402


TAILS = nil23.TAILS
SUPPORTS = nil23.SUPPORTS
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "DENSE_INVERTIBLE_CHART_COVERED_BY_EXACT_MINORS"
PRIMARY_SELECTION_POINT = (1, 2, 1, 1)
PIVOT_FACE_SELECTION_POINT = (2, -1, 1)
DOUBLE_PIVOT_FACE_SELECTION_POINT = (1, 1)


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("r s t w")


def transformed_coordinate(tail, coordinate, support, r, s, t, w):
    shape, core, extra = support
    first, second = core
    if shape == "extra_right":
        if coordinate not in core:
            return tail[coordinate]
        right_form = t * (
            s * tail[first] + tail[second] + w * tail[extra]
        )
        left_coefficient = 1 if coordinate == first else r
    elif shape == "extra_left":
        if coordinate not in core + (extra,):
            return tail[coordinate]
        right_form = t * (s * tail[first] + tail[second])
        if coordinate == first:
            left_coefficient = 1
        elif coordinate == second:
            left_coefficient = r
        else:
            left_coefficient = w
    else:
        raise ValueError(shape)
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(assignment, identity_count, support, r, s, t, w):
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
                    tail, coordinate, support, r, s, t, w
                )
            )
        feature.append(value)
    return feature


def pivot_face_assignment_feature(
    assignment, identity_count, support, r, t, w
):
    """Restrict to 1+s*t=0 without introducing a Laurent denominator."""
    shape, core, extra = support
    first, second = core
    feature = []
    for tail in TAILS:
        value = 1
        if shape == "extra_right":
            right_form = (
                -tail[first] + t * tail[second] + t * w * tail[extra]
            )
        elif shape == "extra_left":
            right_form = -tail[first] + t * tail[second]
        else:
            raise ValueError(shape)
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            if block < identity_count:
                transformed = tail[coordinate]
            elif shape == "extra_right":
                if coordinate not in core:
                    transformed = tail[coordinate]
                else:
                    left_coefficient = 1 if coordinate == first else r
                    transformed = tail[coordinate] + left_coefficient * right_form
            elif coordinate not in core + (extra,):
                transformed = tail[coordinate]
            else:
                if coordinate == first:
                    left_coefficient = 1
                elif coordinate == second:
                    left_coefficient = r
                else:
                    left_coefficient = w
                transformed = tail[coordinate] + left_coefficient * right_form
            value *= transformed
        feature.append(value)
    return feature


def double_pivot_face_assignment_feature(
    assignment, identity_count, support, t, w
):
    """Restrict to 1+s*t=1+r*t=0 and clear columnwise t denominators."""
    shape, core, extra = support
    if shape != "extra_right":
        raise ValueError("the double pivot face occurs only for extra_right")
    first, second = core
    feature = []
    for tail in TAILS:
        value = 1
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            if block < identity_count or coordinate not in core:
                transformed = tail[coordinate]
            elif coordinate == first:
                transformed = t * (tail[second] + w * tail[extra])
            else:
                # This is t times the actual transformed second coordinate.
                # The resulting feature column is rescaled by a nonzero power
                # of t, which preserves rank on the face torus t != 0.
                transformed = tail[first] - t * w * tail[extra]
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
        nil23.core22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def exact_minor(candidate, point):
    witnesses = witness_assignments(candidate, point)
    if len(witnesses) != len(TAILS):
        return witnesses, None
    support, identity_count = candidate
    r, s, t, w = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, r, s, t, w
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), r, s, t, w, domain=sp.ZZ
    )
    return witnesses, determinant


def exact_pivot_face_minor(candidate, point=PIVOT_FACE_SELECTION_POINT):
    support, identity_count = candidate
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = pivot_face_assignment_feature(
            assignment, identity_count, support, *point
        )
        nil23.core22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    witnesses = tuple(pivots[column][1] for column in sorted(pivots))
    if len(witnesses) != len(TAILS):
        return witnesses, None
    r, _s, t, w = parameter_symbols()
    matrix = sp.Matrix(
        [
            pivot_face_assignment_feature(
                assignment, identity_count, support, r, t, w
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), r, t, w, domain=sp.ZZ
    )
    return witnesses, determinant


def exact_double_pivot_face_minor(
    candidate, point=DOUBLE_PIVOT_FACE_SELECTION_POINT
):
    support, identity_count = candidate
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = double_pivot_face_assignment_feature(
            assignment, identity_count, support, *point
        )
        nil23.core22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    witnesses = tuple(pivots[column][1] for column in sorted(pivots))
    if len(witnesses) != len(TAILS):
        return witnesses, None
    _r, _s, t, w = parameter_symbols()
    matrix = sp.Matrix(
        [
            double_pivot_face_assignment_feature(
                assignment, identity_count, support, t, w
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), t, w, domain=sp.ZZ)
    return witnesses, determinant


def allowed_boundary_polynomials():
    r, s, t, w = parameter_symbols()
    return {
        "support_face_r": sp.Poly(r, r, s, t, w, domain=sp.QQ).monic(),
        "support_face_s": sp.Poly(s, r, s, t, w, domain=sp.QQ).monic(),
        "scale_face_t": sp.Poly(t, r, s, t, w, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, r, s, t, w, domain=sp.QQ).monic(),
        "nilpotent_face_r_plus_s": sp.Poly(
            r + s, r, s, t, w, domain=sp.QQ
        ).monic(),
        "singular_face_1_plus_t_times_r_plus_s": sp.Poly(
            1 + t * (r + s), r, s, t, w, domain=sp.QQ
        ).monic(),
    }


def allowed_boundary_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    r, s, t, w = parameter_symbols()
    allowed = allowed_boundary_polynomials()
    _content, factors = sp.Poly(
        polynomial.as_expr(), r, s, t, w, domain=sp.QQ
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
    r, _s, t, w = parameter_symbols()
    allowed = {
        "support_face_r": sp.Poly(r, r, t, w, domain=sp.QQ).monic(),
        "scale_face_t": sp.Poly(t, r, t, w, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, r, t, w, domain=sp.QQ).monic(),
        "nilpotent_subface_r_t_minus_1": sp.Poly(
            r * t - 1, r, t, w, domain=sp.QQ
        ).monic(),
    }
    _content, factors = sp.Poly(
        polynomial.as_expr(), r, t, w, domain=sp.QQ
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


def double_pivot_face_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    _r, _s, t, w = parameter_symbols()
    allowed = {
        "scale_face_t": sp.Poly(t, t, w, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, t, w, domain=sp.QQ).monic(),
    }
    _content, factors = sp.Poly(
        polynomial.as_expr(), t, w, domain=sp.QQ
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
    shape, core, extra = support
    witnesses, determinant = exact_minor(candidate, PRIMARY_SELECTION_POINT)
    if determinant is None or determinant.is_zero:
        return {
            "shape": shape,
            "core_support": list(core),
            "extra_coordinate": extra,
            "identity_count": identity_count,
            "primary_minor": None,
            "pivot_face_minor": None,
            "double_pivot_face_minor": None,
            "status": "UNRESOLVED_PRIMARY_MINOR",
        }
    covered, exponents, unresolved = allowed_boundary_factorization(determinant)
    primary_minor = {
        "selection_point": list(PRIMARY_SELECTION_POINT),
        "rank": len(witnesses),
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(determinant.terms()),
        "determinant_factorization": str(sp.factor(determinant.as_expr())),
        "allowed_boundary_factor_exponents": exponents,
        "unresolved_factors": unresolved,
    }
    pivot_face_minor = None
    double_pivot_face_minor = None
    if not covered:
        r, s, t, w = parameter_symbols()
        pivot_factor = sp.Poly(1 + s * t, r, s, t, w, domain=sp.QQ).monic()
        unresolved_is_pivot = bool(unresolved) and all(
            sp.Poly(
                sp.sympify(item["factor"]), r, s, t, w, domain=sp.QQ
            ).monic()
            == pivot_factor
            for item in unresolved
        )
        if unresolved_is_pivot:
            face_witnesses, face_determinant = exact_pivot_face_minor(candidate)
            face_covered, face_exponents, face_unresolved = (
                pivot_face_factorization(face_determinant)
            )
            pivot_face_minor = {
                "equation": "1+s*t=0",
                "selection_point_r_t_w": list(PIVOT_FACE_SELECTION_POINT),
                "rank_at_selection_point": len(face_witnesses),
                "determinant_total_degree": (
                    face_determinant.total_degree()
                    if face_determinant is not None
                    else None
                ),
                "determinant_term_count": (
                    len(face_determinant.terms())
                    if face_determinant is not None
                    else None
                ),
                "determinant_factorization": (
                    str(sp.factor(face_determinant.as_expr()))
                    if face_determinant is not None
                    else None
                ),
                "allowed_boundary_factor_exponents": face_exponents,
                "unresolved_factors": face_unresolved,
            }
            covered = face_covered
            if not covered:
                face_r, _face_s, face_t, face_w = parameter_symbols()
                double_pivot_factor = sp.Poly(
                    1 + face_r * face_t,
                    face_r,
                    face_t,
                    face_w,
                    domain=sp.QQ,
                ).monic()
                unresolved_is_double_pivot = bool(face_unresolved) and all(
                    sp.Poly(
                        sp.sympify(item["factor"]),
                        face_r,
                        face_t,
                        face_w,
                        domain=sp.QQ,
                    ).monic()
                    == double_pivot_factor
                    for item in face_unresolved
                )
                if unresolved_is_double_pivot:
                    double_witnesses, double_determinant = (
                        exact_double_pivot_face_minor(candidate)
                    )
                    double_covered, double_exponents, double_unresolved = (
                        double_pivot_face_factorization(double_determinant)
                    )
                    double_pivot_face_minor = {
                        "equations": ["1+s*t=0", "1+r*t=0"],
                        "selection_point_t_w": list(
                            DOUBLE_PIVOT_FACE_SELECTION_POINT
                        ),
                        "rank_at_selection_point": len(double_witnesses),
                        "laurent_column_scaling": (
                            "multiply each feature column by t^(number of "
                            "updated blocks selecting the core second coordinate)"
                        ),
                        "determinant_total_degree": (
                            double_determinant.total_degree()
                            if double_determinant is not None
                            else None
                        ),
                        "determinant_term_count": (
                            len(double_determinant.terms())
                            if double_determinant is not None
                            else None
                        ),
                        "determinant_factorization": (
                            str(sp.factor(double_determinant.as_expr()))
                            if double_determinant is not None
                            else None
                        ),
                        "allowed_boundary_factor_exponents": double_exponents,
                        "unresolved_factors": double_unresolved,
                    }
                    covered = double_covered
    return {
        "shape": shape,
        "core_support": list(core),
        "extra_coordinate": extra,
        "identity_count": identity_count,
        "primary_minor": primary_minor,
        "pivot_face_minor": pivot_face_minor,
        "double_pivot_face_minor": double_pivot_face_minor,
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
        "nilpotent_overlapping_23_32": exact_status(
            "data/n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json"
        )
    }


def build_payload(args):
    family = candidates()
    if len(family) != 2 * math.comb(6, 2) * 4 * 5:
        raise AssertionError("overlapping-(2,3)/(3,2) inventory drift")
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
            row["shape"],
            row["core_support"],
            row["extra_coordinate"],
            row["identity_count"],
        )
    )
    status_counts = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    complete = status_counts == {ROW_STATUS: CANDIDATE_COUNT}
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_OVERLAPPING_23_32_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_OVERLAPPING_23_32_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * binom(6,2) * 4 * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parametrization": (
            "extra_right: u=(1,r) on the core and v=t*(s,1,w) on core+extra; "
            "extra_left: u=(1,r,w) on core+extra and v=t*(s,1) on the core"
        ),
        "determinant_identity": "det(I+u*v^T)=1+t*(r+s)",
        "exact_support_condition": "r*s*t*w != 0",
        "invertibility_condition": "1+t*(r+s) != 0",
        "internal_face_equations": ["1+s*t=0", "1+r*t=0 inside the first face"],
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 8.0,
        "status_counts": status_counts,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update with support shapes (2,3) and (3,2), overlap two, and every coefficient nonzero.",
            "All 120 oriented supports and five positive identity/update multiplicity splits are represented.",
            "A primary exact minor covers the complement of 1+s*t=0; exact minors restricted first to that face and, when needed, to its 1+r*t=0 subface cover the remainder, so no multivariate-gcd inference is used.",
            "The internal nilpotent face r+s=0 is imported from its exact certificate.",
            "The coordinate and projective support faces are not asserted here; the singleton-versus-triple face families remain to be certified before support-closure language is valid.",
            "The result does not prove ordinary lower 50, exact rank 64, arbitrary GL(6), arbitrary endpoint-B packets, higher-rank perturbations, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-start", type=int)
    parser.add_argument("--probe-count", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if (args.probe_start is None) != (args.probe_count is None):
        raise ValueError("--probe-start and --probe-count must be used together")
    if args.probe_start is not None:
        stop = args.probe_start + args.probe_count
        if not 0 <= args.probe_start < stop <= CANDIDATE_COUNT:
            raise ValueError("probe range is outside the candidate family")
        started = time.perf_counter()
        rows = [
            cover_trial(candidate)
            for candidate in candidates()[args.probe_start:stop]
        ]
        payload = {
            "candidate_formula": "bounded contiguous probe",
            "candidate_count": len(rows),
            "start_index": args.probe_start,
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
