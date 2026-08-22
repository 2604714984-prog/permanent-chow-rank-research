#!/usr/bin/env python3
"""Exact minors for general overlapping (2,4)/(4,2) rank-one updates."""

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
SUPPORTS = tuple(
    (shape, core, extras)
    for shape in ("extra_right", "extra_left")
    for core in itertools.combinations(range(6), 2)
    for extras in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate not in core], 2
    )
)
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "DENSE_INVERTIBLE_CHART_COVERED_BY_EXACT_MINORS"
PRIMARY_SELECTION_POINT = (1, 2, 1, 1, 1)
PIVOT_FACE_SELECTION_POINT = (2, -1, 1, 1)
DOUBLE_PIVOT_FACE_SELECTION_POINT = (1, 1, 1)


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("r s t w x")


def transformed_coordinate(tail, coordinate, support, r, s, t, w, x):
    shape, core, extras = support
    first, second = core
    first_extra, second_extra = extras
    if shape == "extra_right":
        if coordinate not in core:
            return tail[coordinate]
        right_form = t * (
            s * tail[first]
            + tail[second]
            + w * tail[first_extra]
            + x * tail[second_extra]
        )
        left_coefficient = 1 if coordinate == first else r
    elif shape == "extra_left":
        if coordinate not in core + extras:
            return tail[coordinate]
        right_form = t * (s * tail[first] + tail[second])
        if coordinate == first:
            left_coefficient = 1
        elif coordinate == second:
            left_coefficient = r
        elif coordinate == first_extra:
            left_coefficient = w
        else:
            left_coefficient = x
    else:
        raise ValueError(shape)
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(assignment, identity_count, support, r, s, t, w, x):
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
                    tail, coordinate, support, r, s, t, w, x
                )
            )
        feature.append(value)
    return feature


def pivot_face_assignment_feature(
    assignment, identity_count, support, r, t, w, x
):
    """Restrict to 1+s*t=0 without introducing a Laurent denominator."""
    shape, core, extras = support
    first, second = core
    first_extra, second_extra = extras
    feature = []
    for tail in TAILS:
        value = 1
        if shape == "extra_right":
            right_form = (
                -tail[first]
                + t * tail[second]
                + t * w * tail[first_extra]
                + t * x * tail[second_extra]
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
            elif coordinate not in core + extras:
                transformed = tail[coordinate]
            else:
                if coordinate == first:
                    left_coefficient = 1
                elif coordinate == second:
                    left_coefficient = r
                elif coordinate == first_extra:
                    left_coefficient = w
                else:
                    left_coefficient = x
                transformed = tail[coordinate] + left_coefficient * right_form
            value *= transformed
        feature.append(value)
    return feature


def double_pivot_face_assignment_feature(
    assignment, identity_count, support, t, w, x
):
    """Restrict to 1+s*t=1+r*t=0 and clear columnwise t denominators."""
    shape, core, extras = support
    first, second = core
    first_extra, second_extra = extras
    feature = []
    for tail in TAILS:
        value = 1
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            if block < identity_count:
                transformed = tail[coordinate]
            elif shape == "extra_right":
                if coordinate not in core:
                    transformed = tail[coordinate]
                elif coordinate == first:
                    transformed = t * (
                        tail[second]
                        + w * tail[first_extra]
                        + x * tail[second_extra]
                    )
                else:
                    # This is t times the actual transformed second coordinate.
                    transformed = (
                        tail[first]
                        - t * w * tail[first_extra]
                        - t * x * tail[second_extra]
                    )
            elif shape == "extra_left":
                right_form = -tail[first] + t * tail[second]
                if coordinate not in core + extras:
                    transformed = tail[coordinate]
                elif coordinate == first:
                    transformed = t * tail[second]
                elif coordinate == second:
                    # This is t times the actual transformed second coordinate.
                    transformed = tail[first]
                elif coordinate == first_extra:
                    transformed = tail[coordinate] + w * right_form
                else:
                    transformed = tail[coordinate] + x * right_form
            else:
                raise ValueError(shape)
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


def exact_minor(candidate, point=PRIMARY_SELECTION_POINT):
    witnesses = witness_assignments(candidate, point)
    if len(witnesses) != len(TAILS):
        return witnesses, None
    support, identity_count = candidate
    r, s, t, w, x = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, r, s, t, w, x
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), r, s, t, w, x, domain=sp.ZZ
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
    r, _s, t, w, x = parameter_symbols()
    matrix = sp.Matrix(
        [
            pivot_face_assignment_feature(
                assignment, identity_count, support, r, t, w, x
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), r, t, w, x, domain=sp.ZZ
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
    _r, _s, t, w, x = parameter_symbols()
    matrix = sp.Matrix(
        [
            double_pivot_face_assignment_feature(
                assignment, identity_count, support, t, w, x
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), t, w, x, domain=sp.ZZ
    )
    return witnesses, determinant


def allowed_boundary_polynomials():
    r, s, t, w, x = parameter_symbols()
    return {
        "support_face_r": sp.Poly(r, r, s, t, w, x, domain=sp.QQ).monic(),
        "support_face_s": sp.Poly(s, r, s, t, w, x, domain=sp.QQ).monic(),
        "scale_face_t": sp.Poly(t, r, s, t, w, x, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, r, s, t, w, x, domain=sp.QQ).monic(),
        "support_face_x": sp.Poly(x, r, s, t, w, x, domain=sp.QQ).monic(),
        "nilpotent_face_r_plus_s": sp.Poly(
            r + s, r, s, t, w, x, domain=sp.QQ
        ).monic(),
        "singular_face_1_plus_t_times_r_plus_s": sp.Poly(
            1 + t * (r + s), r, s, t, w, x, domain=sp.QQ
        ).monic(),
    }


def factorization_against(polynomial, variables, allowed):
    if polynomial is None or polynomial.is_zero:
        return False, {}, [], None
    content, factors = sp.Poly(
        polynomial.as_expr(), *variables, domain=sp.QQ
    ).factor_list()
    exponents = {}
    unresolved = []
    displayed_factors = [sp.sympify(content)]
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
        displayed_factors.append(
            sp.Pow(factor.as_expr(), int(exponent), evaluate=False)
        )
    factorization = str(sp.Mul(*displayed_factors, evaluate=False))
    return not unresolved, exponents, unresolved, factorization


def factorization_record(polynomial):
    return factorization_against(
        polynomial, parameter_symbols(), allowed_boundary_polynomials()
    )


def pivot_face_factorization(polynomial):
    r, _s, t, w, x = parameter_symbols()
    variables = (r, t, w, x)
    allowed = {
        "support_face_r": sp.Poly(r, *variables, domain=sp.QQ).monic(),
        "scale_face_t": sp.Poly(t, *variables, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, *variables, domain=sp.QQ).monic(),
        "support_face_x": sp.Poly(x, *variables, domain=sp.QQ).monic(),
        "nilpotent_subface_r_t_minus_1": sp.Poly(
            r * t - 1, *variables, domain=sp.QQ
        ).monic(),
    }
    return factorization_against(polynomial, variables, allowed)


def double_pivot_face_factorization(polynomial):
    _r, _s, t, w, x = parameter_symbols()
    variables = (t, w, x)
    allowed = {
        "scale_face_t": sp.Poly(t, *variables, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, *variables, domain=sp.QQ).monic(),
        "support_face_x": sp.Poly(x, *variables, domain=sp.QQ).monic(),
    }
    return factorization_against(polynomial, variables, allowed)


def cover_trial(candidate):
    support, identity_count = candidate
    shape, core, extras = support
    witnesses, determinant = exact_minor(candidate)
    if determinant is None or determinant.is_zero:
        return {
            "shape": shape,
            "core_support": list(core),
            "extra_coordinates": list(extras),
            "identity_count": identity_count,
            "primary_minor": None,
            "pivot_face_minor": None,
            "double_pivot_face_minor": None,
            "status": "UNRESOLVED_PRIMARY_MINOR",
        }
    covered, exponents, unresolved, factorization = factorization_record(
        determinant
    )
    primary_minor = {
        "selection_point": list(PRIMARY_SELECTION_POINT),
        "rank": len(witnesses),
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(determinant.terms()),
        "determinant_factorization": factorization,
        "allowed_boundary_factor_exponents": exponents,
        "unresolved_factors": unresolved,
    }
    pivot_face_minor = None
    double_pivot_face_minor = None
    if not covered:
        r, s, t, w, x = parameter_symbols()
        pivot_factor = sp.Poly(
            1 + s * t, r, s, t, w, x, domain=sp.QQ
        ).monic()
        unresolved_is_pivot = bool(unresolved) and all(
            sp.Poly(
                sp.sympify(item["factor"]), r, s, t, w, x, domain=sp.QQ
            ).monic()
            == pivot_factor
            for item in unresolved
        )
        if unresolved_is_pivot:
            face_witnesses, face_determinant = exact_pivot_face_minor(candidate)
            face_covered, face_exponents, face_unresolved, face_factorization = (
                pivot_face_factorization(face_determinant)
            )
            pivot_face_minor = {
                "equation": "1+s*t=0",
                "selection_point_r_t_w_x": list(PIVOT_FACE_SELECTION_POINT),
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
                "determinant_factorization": face_factorization,
                "allowed_boundary_factor_exponents": face_exponents,
                "unresolved_factors": face_unresolved,
            }
            covered = face_covered
            if not covered:
                face_r, _face_s, face_t, face_w, face_x = parameter_symbols()
                double_pivot_factor = sp.Poly(
                    1 + face_r * face_t,
                    face_r,
                    face_t,
                    face_w,
                    face_x,
                    domain=sp.QQ,
                ).monic()
                unresolved_is_double_pivot = bool(face_unresolved) and all(
                    sp.Poly(
                        sp.sympify(item["factor"]),
                        face_r,
                        face_t,
                        face_w,
                        face_x,
                        domain=sp.QQ,
                    ).monic()
                    == double_pivot_factor
                    for item in face_unresolved
                )
                if unresolved_is_double_pivot:
                    double_witnesses, double_determinant = (
                        exact_double_pivot_face_minor(candidate)
                    )
                    (
                        double_covered,
                        double_exponents,
                        double_unresolved,
                        double_factorization,
                    ) = double_pivot_face_factorization(double_determinant)
                    double_pivot_face_minor = {
                        "equations": ["1+s*t=0", "1+r*t=0"],
                        "selection_point_t_w_x": list(
                            DOUBLE_PIVOT_FACE_SELECTION_POINT
                        ),
                        "rank_at_selection_point": len(double_witnesses),
                        "laurent_column_scaling": (
                            "multiply each feature column by t^(number of updated "
                            "blocks selecting the core second coordinate)"
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
                        "determinant_factorization": double_factorization,
                        "allowed_boundary_factor_exponents": double_exponents,
                        "unresolved_factors": double_unresolved,
                    }
                    covered = double_covered
    return {
        "shape": shape,
        "core_support": list(core),
        "extra_coordinates": list(extras),
        "identity_count": identity_count,
        "primary_minor": primary_minor,
        "pivot_face_minor": pivot_face_minor,
        "double_pivot_face_minor": double_pivot_face_minor,
        "status": ROW_STATUS if covered else "UNRESOLVED_SINGLE_MINOR_FACTOR",
    }


def run_trials(family, workers):
    if workers == 1:
        return [cover_trial(candidate) for candidate in family]
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        return list(pool.map(cover_trial, family, chunksize=1))


def exact_status(relative_path):
    payload = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    status = str(payload["status"])
    if not status.startswith("EXACT_"):
        raise AssertionError(f"face certificate mismatch: {relative_path}")
    return status


def dense_face_certificates():
    audit_path = "data/n7_mixed_glynn_lower_overlap_torus_audit_status.json"
    audit_payload = json.loads((ROOT / audit_path).read_text(encoding="utf-8"))
    audited = {
        str(item["family"]): str(item["status"])
        for item in audit_payload["audited_families"]
    }
    if audited.get("24") != "EXACT_TORUS_IDEAL_AUDITED":
        raise AssertionError("missing overlap-two (2,4) torus audit")
    if audited.get("42") != "EXACT_TORUS_IDEAL_AUDITED":
        raise AssertionError("missing overlap-two (4,2) torus audit")
    return {
        "nilpotent_overlap_two_24": exact_status(
            "data/n7_mixed_glynn_overlap_two_24_nilpotent_shear_tail_rank.json"
        ),
        "nilpotent_overlap_two_42": exact_status(
            "data/n7_mixed_glynn_overlap_two_42_nilpotent_shear_tail_rank.json"
        ),
        "lower_overlap_torus_audit": exact_status(audit_path),
    }


def build_payload(args):
    family = candidates()
    expected = 2 * math.comb(6, 2) * math.comb(4, 2) * 5
    if len(family) != expected:
        raise AssertionError("overlapping-(2,4)/(4,2) inventory drift")
    if len(family) > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    imported_certificates = dense_face_certificates()
    started = time.perf_counter()
    rows = run_trials(family, args.workers)
    rows.sort(
        key=lambda row: (
            row["shape"],
            row["core_support"],
            row["extra_coordinates"],
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
            "EXACT_ALL_OVERLAPPING_24_42_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_OVERLAPPING_24_42_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * binom(6,2) * binom(4,2) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parameter_count": 5,
        "parametrization": (
            "extra_right: u=(1,r) on the core and v=t*(s,1,w,x) on core+extras; "
            "extra_left: u=(1,r,w,x) on core+extras and v=t*(s,1) on the core"
        ),
        "determinant_identity": "det(I+u*v^T)=1+t*(r+s)",
        "dense_face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 8.0,
        "status_counts": status_counts,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "A primary exact minor covers the complement of 1+s*t=0; exact minors restricted first to that face and, when needed, to its 1+r*t=0 subface cover the remainder, so no multivariate-gcd inference is used.",
            "The dense r+s=0 nilpotent face is imported from the exact overlap-two (2,4)/(4,2) certificates together with their exact Laurent-torus audit.",
            "This certificate concerns only the dense invertible chart; projective support faces require separate imported certificates.",
            "It does not prove ordinary lower 50, exact rank 64, or border rank.",
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
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    if (args.probe_start is None) != (args.probe_count is None):
        raise ValueError("--probe-start and --probe-count must be used together")
    if args.probe_start is not None:
        stop = args.probe_start + args.probe_count
        if not 0 <= args.probe_start < stop <= CANDIDATE_COUNT:
            raise ValueError("probe range is outside the candidate family")
        started = time.perf_counter()
        rows = run_trials(candidates()[args.probe_start:stop], args.workers)
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
