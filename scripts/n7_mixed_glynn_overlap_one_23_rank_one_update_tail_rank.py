#!/usr/bin/env python3
"""Exact perm7 minors for overlap-one (2,3)/(3,2) rank-one updates."""

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
import n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank as base  # noqa: E402


TAILS = base.TAILS
EXTRA_RIGHT_SUPPORTS = tuple(
    ("extra_right", shared, (left_extra,), right_extras)
    for shared in range(6)
    for left_extra in range(6)
    if left_extra != shared
    for right_extras in itertools.combinations(
        [
            coordinate
            for coordinate in range(6)
            if coordinate not in (shared, left_extra)
        ],
        2,
    )
)
EXTRA_LEFT_SUPPORTS = tuple(
    ("extra_left", shared, left_extras, (right_extra,))
    for shared in range(6)
    for right_extra in range(6)
    if right_extra != shared
    for left_extras in itertools.combinations(
        [
            coordinate
            for coordinate in range(6)
            if coordinate not in (shared, right_extra)
        ],
        2,
    )
)
SUPPORTS = EXTRA_RIGHT_SUPPORTS + EXTRA_LEFT_SUPPORTS
MULTIPLICITY_SPLITS = tuple(range(1, 6))
CANDIDATE_COUNT = len(SUPPORTS) * len(MULTIPLICITY_SPLITS)
ROW_STATUS = "PROJECTIVE_SUPPORT_CLOSURE_COVERED_BY_ONE_EXACT_MINOR"
SELECTION_POINTS = (
    (1, 1, 1, 1),
    (2, 1, 1, 1),
    (1, 2, 1, 1),
    (1, 1, 2, 1),
    (2, 3, 2, 1),
)


def candidates():
    return tuple(
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in MULTIPLICITY_SPLITS
    )


def parameter_symbols():
    return sp.symbols("r s t w")


def transformed_coordinate(tail, coordinate, support, r, s, t, w):
    orientation, shared, left_extras, right_extras = support
    if orientation == "extra_right":
        left_extra = left_extras[0]
        first_right, second_right = right_extras
        if coordinate not in (shared, left_extra):
            return tail[coordinate]
        right_form = t * (
            s * tail[shared]
            + tail[first_right]
            + w * tail[second_right]
        )
        left_coefficient = 1 if coordinate == shared else r
        return tail[coordinate] + left_coefficient * right_form
    if orientation == "extra_left":
        first_left, second_left = left_extras
        right_extra = right_extras[0]
        if coordinate not in (shared, first_left, second_left):
            return tail[coordinate]
        right_form = t * (s * tail[shared] + tail[right_extra])
        if coordinate == shared:
            left_coefficient = 1
        elif coordinate == first_left:
            left_coefficient = r
        else:
            left_coefficient = w
        return tail[coordinate] + left_coefficient * right_form
    raise ValueError(orientation)


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


def witness_assignments(candidate, point):
    support, identity_count = candidate
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment, identity_count, support, *point
        )
        base.nil22.base.add_modular_pivot(pivots, feature, assignment)
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


def allowed_boundary_polynomials():
    r, s, t, w = parameter_symbols()
    variables = (r, s, t, w)
    return {
        "left_support_face_r": sp.Poly(r, *variables, domain=sp.QQ).monic(),
        "shared_pairing_face_s": sp.Poly(s, *variables, domain=sp.QQ).monic(),
        "identity_face_t": sp.Poly(t, *variables, domain=sp.QQ).monic(),
        "opposite_support_face_w": sp.Poly(w, *variables, domain=sp.QQ).monic(),
        "singular_face_1_plus_s_t": sp.Poly(
            1 + s * t, *variables, domain=sp.QQ
        ).monic(),
    }


def allowed_boundary_factorization(polynomial):
    if polynomial is None or polynomial.is_zero:
        return False, {}, [], None
    variables = parameter_symbols()
    allowed = allowed_boundary_polynomials()
    content, factors = sp.Poly(
        polynomial.as_expr(), *variables, domain=sp.QQ
    ).factor_list()
    exponents = {}
    unresolved = []
    displayed = [sp.sympify(content)]
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
        displayed.append(sp.Pow(factor.as_expr(), int(exponent), evaluate=False))
    return (
        not unresolved,
        exponents,
        unresolved,
        str(sp.Mul(*displayed, evaluate=False)),
    )


def cover_trial(candidate):
    support, identity_count = candidate
    orientation, shared, left_extras, right_extras = support
    attempts = []
    selected = None
    for point in SELECTION_POINTS:
        witnesses, determinant = exact_minor(candidate, point)
        if determinant is None or determinant.is_zero:
            attempts.append({"selection_point": list(point), "rank": len(witnesses)})
            continue
        covered, exponents, unresolved, factorization = (
            allowed_boundary_factorization(determinant)
        )
        attempt = {
            "selection_point": list(point),
            "rank": len(witnesses),
            "determinant_total_degree": determinant.total_degree(),
            "determinant_term_count": len(determinant.terms()),
            "determinant_factorization": factorization,
            "allowed_boundary_factor_exponents": exponents,
            "unresolved_factors": unresolved,
        }
        attempts.append(attempt)
        if covered:
            selected = attempt
            break
    return {
        "orientation": orientation,
        "shared_coordinate": shared,
        "left_extra_coordinates": list(left_extras),
        "right_extra_coordinates": list(right_extras),
        "identity_count": identity_count,
        "attempt_count": len(attempts),
        "selected_minor": selected,
        "failed_attempts": attempts[:-1] if selected is not None else attempts,
        "status": ROW_STATUS if selected is not None else "UNRESOLVED_SINGLE_MINOR_FACTOR",
    }


def exact_status(relative_path):
    payload = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    status = str(payload["status"])
    if not status.startswith("EXACT_"):
        raise AssertionError(f"face certificate mismatch: {relative_path}")
    return status


def face_certificates():
    return {
        "overlap_one_22": exact_status(
            "data/n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank.json"
        ),
        "singleton_triple": exact_status(
            "data/n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.json"
        ),
        "disjoint_22": exact_status(
            "data/n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.json"
        ),
        "disjoint_three_direction": exact_status(
            "data/n7_mixed_glynn_three_direction_shear_tail_rank.json"
        ),
    }


def run_trials(family, workers):
    if workers == 1:
        return [cover_trial(candidate) for candidate in family]
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as pool:
        return list(pool.map(cover_trial, family, chunksize=1))


def build_payload(args):
    family = candidates()
    expected = 2 * 6 * 5 * math.comb(4, 2) * 5
    if len(family) != expected:
        raise AssertionError("overlap-one (2,3)/(3,2) inventory drift")
    if len(family) > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    imported_certificates = face_certificates()
    started = time.perf_counter()
    rows = run_trials(family, args.workers)
    rows.sort(
        key=lambda row: (
            row["orientation"],
            row["shared_coordinate"],
            row["left_extra_coordinates"],
            row["right_extra_coordinates"],
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
            "EXACT_ALL_OVERLAP_ONE_23_32_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_OVERLAP_ONE_23_32_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * 6 * 5 * binom(4,2) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parameter_count": 4,
        "parametrizations": {
            "extra_right": (
                "u=e_a+r*e_b, v=t*(s*e_a^*+e_c^*+w*e_d^*)"
            ),
            "extra_left": (
                "u=e_a+r*e_b+w*e_c, v=t*(s*e_a^*+e_d^*)"
            ),
        },
        "determinant_identity": "det(I+u*v^T)=1+s*t",
        "dense_chart_condition": "r*s*t*w*(1+s*t) != 0",
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 8.0,
        "status_counts": status_counts,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update with support sizes (2,3) or (3,2) and overlap exactly one.",
            "Every dense row is covered by one exact 42-by-42 minor; no multivariate-gcd inference is used.",
            "All proper projective coordinate faces import exact overlap-one (2,2), singleton-versus-triple, disjoint (2,2), or disjoint three-direction certificates.",
            "Consequently the full projective overlap-one (2,3)/(3,2) support closure is covered.",
            "The result does not prove ordinary lower 50, exact rank 64, or border rank.",
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
