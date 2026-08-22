#!/usr/bin/env python3
"""Exact perm7 minors for singleton-versus-four rank-one updates."""

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
import n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank as base  # noqa: E402


TAILS = base.TAILS
SUPPORTS = tuple(
    (orientation, shared, extras)
    for orientation in ("left_singleton", "right_singleton")
    for shared in range(6)
    for extras in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != shared], 3
    )
)
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
    return sp.symbols("s t w x")


def transformed_coordinate(tail, coordinate, support, s, t, w, x):
    orientation, shared, extras = support
    first, second, third = extras
    if orientation == "left_singleton":
        if coordinate != shared:
            return tail[coordinate]
        right_form = t * (
            tail[shared]
            + s * tail[first]
            + w * tail[second]
            + x * tail[third]
        )
        return tail[shared] + right_form
    if orientation == "right_singleton":
        if coordinate not in (shared, first, second, third):
            return tail[coordinate]
        coefficients = {
            shared: 1,
            first: s,
            second: w,
            third: x,
        }
        return tail[coordinate] + coefficients[coordinate] * t * tail[shared]
    raise ValueError(orientation)


def assignment_feature(assignment, identity_count, support, s, t, w, x):
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
                    tail, coordinate, support, s, t, w, x
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
    s, t, w, x = parameter_symbols()
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, support, s, t, w, x
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), s, t, w, x, domain=sp.ZZ
    )
    return witnesses, determinant


def allowed_boundary_polynomials():
    s, t, w, x = parameter_symbols()
    variables = (s, t, w, x)
    return {
        "support_face_s": sp.Poly(s, *variables, domain=sp.QQ).monic(),
        "identity_face_t": sp.Poly(t, *variables, domain=sp.QQ).monic(),
        "support_face_w": sp.Poly(w, *variables, domain=sp.QQ).monic(),
        "support_face_x": sp.Poly(x, *variables, domain=sp.QQ).monic(),
        "singular_face_1_plus_t": sp.Poly(
            1 + t, *variables, domain=sp.QQ
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
    orientation, shared, extras = support
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
        "extra_coordinates": list(extras),
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
        "singleton_triple": exact_status(
            "data/n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.json"
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
    expected = 2 * 6 * math.comb(5, 3) * 5
    if len(family) != expected:
        raise AssertionError("singleton-versus-four support inventory drift")
    if len(family) > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    imported_certificates = face_certificates()
    started = time.perf_counter()
    rows = run_trials(family, args.workers)
    rows.sort(
        key=lambda row: (
            row["orientation"],
            row["shared_coordinate"],
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
            "EXACT_ALL_SINGLETON_FOUR_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
            if complete
            else "INCOMPLETE_SINGLETON_FOUR_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
        ),
        "field": "characteristic zero",
        "candidate_formula": "2 * 6 * binom(5,3) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "parameter_count": 4,
        "parametrizations": {
            "left_singleton": (
                "u=e_a, v=t*(e_a^*+s*e_b^*+w*e_c^*+x*e_d^*)"
            ),
            "right_singleton": (
                "u=e_a+s*e_b+w*e_c+x*e_d, v=t*e_a^*"
            ),
        },
        "determinant_identity": "det(I+u*v^T)=1+t",
        "dense_chart_condition": "s*t*w*x*(1+t) != 0",
        "face_certificates": imported_certificates,
        "workers": args.workers,
        "planned_peak_memory_budget_gib": 8.0,
        "status_counts": status_counts,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity versus one invertible rank-one update whose supports have sizes one and four and overlap in the singleton coordinate, in both orientations.",
            "Every dense row is covered by one exact 42-by-42 minor; no multivariate-gcd inference is used.",
            "Coordinate faces import singleton-versus-triple closure, while the projective normalized-shared-coefficient face imports the disjoint three-direction shear certificate.",
            "Consequently the full projective singleton-versus-four support closure is covered.",
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
