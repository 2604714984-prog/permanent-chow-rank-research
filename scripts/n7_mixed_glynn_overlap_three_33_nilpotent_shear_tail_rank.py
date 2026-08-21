#!/usr/bin/env python3
"""Exact perm7 minors for coincident three-coordinate nilpotent shears."""

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
import n7_mixed_glynn_overlap_two_rank_one_shear_tail_rank as base2  # noqa: E402


TAILS = base2.TAILS
SUPPORTS = tuple(itertools.combinations(range(6), 3))
CANDIDATE_COUNT = len(SUPPORTS) * 5
ROW_STATUS = "DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS"


def candidates():
    return [(support, identity_count) for support in SUPPORTS for identity_count in range(1, 6)]


def transformed_coordinate(tail, coordinate, support, parameters):
    """Apply I+u v^T with u=(1,a,b), v=t*(-a-b*q,1,q)."""

    a, b, scale, q = parameters
    first, second, third = support
    if coordinate not in support:
        return tail[coordinate]
    right_form = scale * (
        (-a - b * q) * tail[first] + tail[second] + q * tail[third]
    )
    if coordinate == first:
        left_coefficient = 1
    elif coordinate == second:
        left_coefficient = a
    else:
        left_coefficient = b
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(assignment, identity_count, support, parameters):
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
                else transformed_coordinate(tail, coordinate, support, parameters)
            )
        feature.append(value)
    return feature


def witness_assignments(identity_count, support, point, weighted=False):
    pivots = {}
    degrees = range(6 - identity_count + 1) if weighted else (None,)
    left_support = set(support)
    for target_degree in degrees:
        for assignment in itertools.product(range(7), repeat=6):
            if len(set(assignment)) == 6:
                continue
            if target_degree is not None:
                degree = sum(
                    1
                    for block, column in enumerate(assignment)
                    if block >= identity_count
                    and column != 0
                    and column - 1 in left_support
                )
                if degree != target_degree:
                    continue
            feature = assignment_feature(assignment, identity_count, support, point)
            base2.base23.core22.base.add_modular_pivot(pivots, feature, assignment)
            if len(pivots) == len(TAILS):
                return tuple(pivots[column][1] for column in sorted(pivots))
    return tuple(pivots[column][1] for column in sorted(pivots))


def allowed_boundary_factorization(polynomial, parameters):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    a, b, scale, q = parameters
    allowed = {
        "a": sp.Poly(a, *parameters, domain=sp.QQ).monic(),
        "b": sp.Poly(b, *parameters, domain=sp.QQ).monic(),
        "t": sp.Poly(scale, *parameters, domain=sp.QQ).monic(),
        "q": sp.Poly(q, *parameters, domain=sp.QQ).monic(),
        "a + b*q": sp.Poly(a + b * q, *parameters, domain=sp.QQ).monic(),
    }
    _content, factors = sp.Poly(
        polynomial.as_expr(), *parameters, domain=sp.QQ
    ).factor_list()
    allowed_exponents = {}
    unresolved = []
    for factor, exponent in factors:
        monic = factor.monic()
        label = next((name for name, item in allowed.items() if monic == item), None)
        if label is None:
            unresolved.append(
                {"factor": str(factor.as_expr()), "exponent": int(exponent)}
            )
        else:
            allowed_exponents[label] = allowed_exponents.get(label, 0) + int(exponent)
    return not unresolved, allowed_exponents, unresolved


def exact_minor(candidate, point, weighted=False):
    support, identity_count = candidate
    if len(point) != 4:
        raise ValueError("selection point must have four entries")
    witnesses = witness_assignments(identity_count, support, point, weighted=weighted)
    common = {
        "support": list(support),
        "identity_count": identity_count,
        "selection_point": list(point),
        "weighted_selection": weighted,
        "rank_at_selection_point": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return common, witnesses, None
    parameters = sp.symbols("a b t q")
    matrix = sp.Matrix(
        [
            assignment_feature(assignment, identity_count, support, parameters)
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), *parameters, domain=sp.ZZ
    )
    return common, witnesses, determinant


def minor_probe(candidate, point, weighted=False):
    common, witnesses, determinant = exact_minor(candidate, point, weighted=weighted)
    if determinant is None:
        return {**common, "status": "RANK_DEFICIENT_AT_SELECTION_POINT"}
    parameters = sp.symbols("a b t q")
    covered, allowed_exponents, unresolved = allowed_boundary_factorization(
        determinant, parameters
    )
    return {
        **common,
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(determinant.terms()),
        "determinant_factorization": str(sp.factor(determinant.as_expr())),
        "allowed_boundary_factor_exponents": allowed_exponents,
        "unresolved_factors": unresolved,
        "witness_assignments": [list(row) for row in witnesses],
        "status": "ALLOWED_BOUNDARY_MINOR_PROBE" if covered else "UNRESOLVED_MINOR_PROBE",
    }


def cover_trial(candidate, weighted=False):
    support, identity_count = candidate
    parameters = sp.symbols("a b t q")
    gcd_polynomial = None
    minors = []
    witness_sample_sets = []
    covered = False
    allowed_exponents = {}
    unresolved = []
    for point in base2.selection_points(4):
        common, witnesses, determinant = exact_minor(candidate, point, weighted=weighted)
        if determinant is None or determinant.is_zero:
            continue
        gcd_polynomial = (
            determinant if gcd_polynomial is None else sp.gcd(gcd_polynomial, determinant)
        )
        minors.append(
            {
                "selection_point": common["selection_point"],
                "determinant_total_degree": determinant.total_degree(),
                "determinant_term_count": len(determinant.terms()),
            }
        )
        witness_sample_sets.append(
            {
                "selection_point": common["selection_point"],
                "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
            }
        )
        covered, allowed_exponents, unresolved = allowed_boundary_factorization(
            gcd_polynomial, parameters
        )
        if covered:
            break
    return {
        "support": list(support),
        "identity_count": identity_count,
        "weighted_selection": weighted,
        "minor_count": len(minors),
        "minors": minors,
        "gcd_factorization": (
            str(sp.factor(gcd_polynomial.as_expr()))
            if gcd_polynomial is not None
            else None
        ),
        "allowed_boundary_factor_exponents": allowed_exponents,
        "unresolved_factors": unresolved,
        "witness_sample_sets": witness_sample_sets,
        "status": ROW_STATUS if covered else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS",
    }


def weighted_cover_trial(candidate):
    return cover_trial(candidate, weighted=True)


def build_payload(args):
    family = candidates()
    stop_index = (
        len(family)
        if args.limit is None
        else min(len(family), args.start_index + args.limit)
    )
    if not 0 <= args.start_index < len(family):
        raise ValueError("--start-index is outside the candidate family")
    selected = family[args.start_index:stop_index]
    if len(selected) > args.max_candidates:
        raise ValueError("selected candidate chunk exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    lower_path = (
        ROOT
        / "data"
        / "n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json"
    )
    lower = json.loads(lower_path.read_text(encoding="utf-8"))
    expected_lower = "EXACT_ALL_OVERLAPPING_23_32_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
    if lower["status"] != expected_lower:
        raise AssertionError("overlap-two face certificate mismatch")
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    trial_function = weighted_cover_trial if args.weighted_selection else cover_trial
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial_function, selected, chunksize=1))
    rows.sort(key=lambda row: (row["support"], row["identity_count"]))
    samples = [
        {
            "support": row["support"],
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
    complete = status_counts == {ROW_STATUS: len(selected)}
    whole_family = args.start_index == 0 and stop_index == len(family)
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_OVERLAP_THREE_33_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            if complete and whole_family
            else (
                "EXACT_CHUNK_OVERLAP_THREE_33_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
                if complete
                else "INCOMPLETE_CHUNK_OVERLAP_THREE_33_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            )
        ),
        "field": "characteristic zero",
        "left_support_size": 3,
        "right_support_size": 3,
        "overlap_size": 3,
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "binom(6,3) * 5",
        "candidate_count": len(selected),
        "full_candidate_count": len(family),
        "candidate_start_index": args.start_index,
        "candidate_stop_index_exclusive": stop_index,
        "parameter_count": 4,
        "parametrization": "u=(1,a,b), v=t*(-a-b*q,1,q) on the selected support",
        "nilpotence_identity": "v^T u = 0",
        "dense_full_support_condition": "a*b*t*q*(a+b*q) != 0",
        "allowed_boundary_divisors": ["a", "b", "t", "q", "a + b*q"],
        "workers": args.workers,
        "weighted_selection": args.weighted_selection,
        "status_counts": status_counts,
        "lower_face_certificate": lower["status"],
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family has coincident three-coordinate supports and v^T u=0.",
            "Every coordinate support and all five positive identity/shear multiplicity splits are represented.",
            "Exact minor gcd factors are confined to the complement of the dense full-support chart; every such divisor lowers support or gives the identity and is covered recursively.",
            "The result does not cover larger support shapes with overlap three, overlap four or more, non-unipotent rank-one updates, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--minor-probe-index", type=int)
    parser.add_argument("--selection-point")
    parser.add_argument("--weighted-selection", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.probe_index is not None and args.minor_probe_index is not None:
        raise ValueError("choose at most one probe mode")
    family = candidates()
    if args.minor_probe_index is not None:
        if not 0 <= args.minor_probe_index < len(family):
            raise ValueError("--minor-probe-index is outside the candidate family")
        if args.selection_point is None:
            raise ValueError("--selection-point is required for a minor probe")
        point = tuple(int(value) for value in args.selection_point.split(","))
        payload = minor_probe(
            family[args.minor_probe_index], point, weighted=args.weighted_selection
        )
    elif args.probe_index is not None:
        if not 0 <= args.probe_index < len(family):
            raise ValueError("--probe-index is outside the candidate family")
        payload = cover_trial(
            family[args.probe_index], weighted=args.weighted_selection
        )
    else:
        payload = build_payload(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
