#!/usr/bin/env python3
"""Exact remaining overlap-two rank-one nilpotent shear minors for perm7."""

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
import n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank as base23  # noqa: E402


TAILS = base23.TAILS
ALLOWED_SIZES = tuple(
    (left_size, right_size)
    for left_size in range(2, 7)
    for right_size in range(2, 7)
    if left_size + right_size - 2 <= 6
    and (left_size, right_size) not in ((2, 2), (2, 3), (3, 2))
)


def supports(left_size: int, right_size: int):
    rows = []
    for core in itertools.combinations(range(6), 2):
        outside = [coordinate for coordinate in range(6) if coordinate not in core]
        for left_extra in itertools.combinations(outside, left_size - 2):
            remaining = [
                coordinate for coordinate in outside if coordinate not in left_extra
            ]
            for right_extra in itertools.combinations(remaining, right_size - 2):
                rows.append((core, left_extra, right_extra))
    return tuple(rows)


def candidates(left_size: int, right_size: int):
    return [
        (support, count, left_size, right_size)
        for support in supports(left_size, right_size)
        for count in range(1, 6)
    ]


def transformed_coordinate(
    tail, coordinate, core, left_extra, right_extra, parameters
):
    ratio, scale = parameters[:2]
    left_parameters = parameters[2 : 2 + len(left_extra)]
    right_parameters = parameters[2 + len(left_extra) :]
    first, second = core
    left_support = core + left_extra
    if coordinate not in left_support:
        return tail[coordinate]
    right_form = scale * (-ratio * tail[first] + tail[second])
    right_form += sum(
        coefficient * tail[index]
        for coefficient, index in zip(right_parameters, right_extra)
    )
    if coordinate == first:
        left_coefficient = 1
    elif coordinate == second:
        left_coefficient = ratio
    else:
        left_coefficient = left_parameters[left_extra.index(coordinate)]
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(
    assignment,
    identity_count,
    core,
    left_extra,
    right_extra,
    parameters,
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
                    tail,
                    coordinate,
                    core,
                    left_extra,
                    right_extra,
                    parameters,
                )
            )
        feature.append(value)
    return feature


def witness_assignments(identity_count, support, point):
    core, left_extra, right_extra = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment,
            identity_count,
            core,
            left_extra,
            right_extra,
            point,
        )
        base23.core22.base.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def weighted_witness_assignments(identity_count, support, point):
    core, left_extra, right_extra = support
    left_support = set(core + left_extra)
    pivots = {}
    maximum_degree = 6 - identity_count
    for target_degree in range(maximum_degree + 1):
        for assignment in itertools.product(range(7), repeat=6):
            if len(set(assignment)) == 6:
                continue
            degree = sum(
                1
                for block, column in enumerate(assignment)
                if block >= identity_count
                and column != 0
                and column - 1 in left_support
            )
            if degree != target_degree:
                continue
            feature = assignment_feature(
                assignment,
                identity_count,
                core,
                left_extra,
                right_extra,
                point,
            )
            base23.core22.base.add_modular_pivot(pivots, feature, assignment)
            if len(pivots) == len(TAILS):
                return tuple(pivots[column][1] for column in sorted(pivots))
    return tuple(pivots[column][1] for column in sorted(pivots))


def selection_points(parameter_count: int):
    points = [[1] * parameter_count]
    for index in range(parameter_count):
        point = [1] * parameter_count
        point[index] = 2
        points.append(point)
    primes = (2, 3, 5, 7, 11, 13)
    points.append(list(primes[:parameter_count]))
    return tuple(tuple(point) for point in points)


def cover_trial(candidate, weighted=False):
    support, identity_count, left_size, right_size = candidate
    core, left_extra, right_extra = support
    parameter_count = left_size + right_size - 2
    parameters = sp.symbols(f"p0:{parameter_count}")
    gcd_polynomial = None
    minors = []
    witness_sample_sets = []
    for point in selection_points(parameter_count):
        witnesses = (
            weighted_witness_assignments(identity_count, support, point)
            if weighted
            else witness_assignments(identity_count, support, point)
        )
        if len(witnesses) != len(TAILS):
            continue
        matrix = sp.Matrix(
            [
                assignment_feature(
                    assignment,
                    identity_count,
                    core,
                    left_extra,
                    right_extra,
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
        "core_support": list(core),
        "left_extra_support": list(left_extra),
        "right_extra_support": list(right_extra),
        "identity_count": identity_count,
        "weighted_selection": weighted,
        "minor_count": len(minors),
        "minors": minors,
        "gcd": gcd_polynomial.as_expr().__str__() if gcd_polynomial is not None else None,
        "gcd_exponents": list(gcd_terms[0][0]) if covered else None,
        "gcd_term_count": len(gcd_terms),
        "witness_sample_sets": witness_sample_sets,
        "status": (
            "DENSE_TORUS_COVERED_BY_EXACT_MINORS"
            if covered
            else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS"
        ),
    }


def weighted_cover_trial(candidate):
    return cover_trial(candidate, weighted=True)


def minor_probe(candidate, point, weighted=False):
    support, identity_count, left_size, right_size = candidate
    core, left_extra, right_extra = support
    parameter_count = left_size + right_size - 2
    if len(point) != parameter_count:
        raise ValueError("probe point has the wrong parameter count")
    witnesses = (
        weighted_witness_assignments(identity_count, support, point)
        if weighted
        else witness_assignments(identity_count, support, point)
    )
    common = {
        "core_support": list(core),
        "left_extra_support": list(left_extra),
        "right_extra_support": list(right_extra),
        "identity_count": identity_count,
        "selection_point": list(point),
        "weighted_selection": weighted,
        "rank_at_selection_point": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return {**common, "status": "RANK_DEFICIENT_AT_SELECTION_POINT"}
    parameters = sp.symbols(f"p0:{parameter_count}")
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment,
                identity_count,
                core,
                left_extra,
                right_extra,
                parameters,
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), *parameters, domain=sp.ZZ
    )
    terms = determinant.terms()
    monomial = len(terms) == 1 and terms[0][1] != 0
    return {
        **common,
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(terms),
        "monomial_exponents": list(terms[0][0]) if monomial else None,
        "monomial_coefficient": str(terms[0][1]) if monomial else None,
        "witness_assignments": [list(row) for row in witnesses],
        "status": "MONOMIAL_MINOR_PROBE" if monomial else "NONMONOMIAL_MINOR_PROBE",
    }


def immediate_face_paths(left_size: int, right_size: int):
    paths = []
    for pair in ((left_size - 1, right_size), (left_size, right_size - 1)):
        if pair in ((2, 2),):
            name = "n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json"
        elif pair in ((2, 3), (3, 2)):
            name = "n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json"
        elif pair in ALLOWED_SIZES:
            name = f"n7_mixed_glynn_overlap_two_{pair[0]}{pair[1]}_nilpotent_shear_tail_rank.json"
        else:
            continue
        paths.append(ROOT / "data" / name)
    return tuple(dict.fromkeys(paths))


def build_payload(args):
    complete_family = candidates(args.left_size, args.right_size)
    candidate_count = len(complete_family)
    stop_index = (
        candidate_count
        if args.limit is None
        else min(candidate_count, args.start_index + args.limit)
    )
    if not 0 <= args.start_index < candidate_count:
        raise ValueError("--start-index is outside the candidate family")
    family = complete_family[args.start_index:stop_index]
    if len(family) > args.max_candidates:
        raise ValueError("selected candidate chunk exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    face_certificates = []
    for path in immediate_face_paths(args.left_size, args.right_size):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not str(payload["status"]).startswith("EXACT_ALL_"):
            raise AssertionError(f"coordinate-face certificate mismatch: {path.name}")
        face_certificates.append(payload["status"])
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        trial_function = weighted_cover_trial if args.weighted_selection else cover_trial
        rows = list(pool.map(trial_function, family, chunksize=1))
    rows.sort(
        key=lambda row: (
            row["core_support"],
            row["left_extra_support"],
            row["right_extra_support"],
            row["identity_count"],
        )
    )
    samples = [
        {
            "core_support": row["core_support"],
            "left_extra_support": row["left_extra_support"],
            "right_extra_support": row["right_extra_support"],
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
        "DENSE_TORUS_COVERED_BY_EXACT_MINORS": len(family)
    }
    label = f"{args.left_size}{args.right_size}"
    return {
        "schema_version": 1,
        "status": (
            (
                f"EXACT_ALL_OVERLAP_TWO_{label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
                if args.start_index == 0 and stop_index == candidate_count
                else f"EXACT_CHUNK_OVERLAP_TWO_{label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            )
            if complete
            else f"INCOMPLETE_CHUNK_OVERLAP_TWO_{label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "left_support_size": args.left_size,
        "right_support_size": args.right_size,
        "overlap_size": 2,
        "support_count": len(supports(args.left_size, args.right_size)),
        "multiplicity_split_count": 5,
        "candidate_count": len(family),
        "full_candidate_count": candidate_count,
        "candidate_start_index": args.start_index,
        "candidate_stop_index_exclusive": stop_index,
        "parameter_count": args.left_size + args.right_size - 2,
        "workers": args.workers,
        "weighted_selection": args.weighted_selection,
        "status_counts": status_counts,
        "coordinate_face_certificates": face_certificates,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            f"The exact family has support sizes ({args.left_size},{args.right_size}), overlap exactly two, and v^T u=0 on the overlapping core.",
            "Every oriented coordinate support and all five positive identity/shear multiplicity splits are represented.",
            "Exact minor gcds cover the dense parameter torus; proper coefficient faces reduce to previously certified support strata.",
            "The result does not cover overlap three or more, non-unipotent rank-one updates, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--left-size", type=int, required=True)
    parser.add_argument("--right-size", type=int, required=True)
    parser.add_argument("--max-candidates", type=int, default=900)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--minor-probe-index", type=int)
    parser.add_argument("--selection-point")
    parser.add_argument("--weighted-selection", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    pair = (args.left_size, args.right_size)
    if pair not in ALLOWED_SIZES:
        raise ValueError("unsupported overlap-two support-size pair")
    family = candidates(*pair)
    if args.probe_index is not None and args.minor_probe_index is not None:
        raise ValueError("choose at most one probe mode")
    if args.minor_probe_index is not None:
        if not 0 <= args.minor_probe_index < len(family):
            raise ValueError("--minor-probe-index is outside the candidate family")
        if args.selection_point is None:
            raise ValueError("--selection-point is required for a minor probe")
        point = tuple(int(value) for value in args.selection_point.split(","))
        payload = minor_probe(
            family[args.minor_probe_index], point, weighted=args.weighted_selection
        )
    elif args.probe_index is None:
        payload = build_payload(args)
    else:
        if not 0 <= args.probe_index < len(family):
            raise ValueError("--probe-index is outside the candidate family")
        payload = cover_trial(
            family[args.probe_index], weighted=args.weighted_selection
        )
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
