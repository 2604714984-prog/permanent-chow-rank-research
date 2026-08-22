#!/usr/bin/env python3
"""Exact perm7 rank-one nilpotent shear minors for support overlap 4--6."""

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
import n7_mixed_glynn_overlap_three_rank_one_shear_tail_rank as base3  # noqa: E402


TAILS = base3.TAILS
ROW_STATUS = "DENSE_FULL_SUPPORT_COVERED_BY_EXACT_MINORS"
OVERLAP_WORDS = {3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX"}
ALLOWED_FAMILIES = tuple(
    (overlap_size, left_size, right_size)
    for overlap_size in range(4, 7)
    for left_size in range(overlap_size, 7)
    for right_size in range(overlap_size, 7)
    if left_size + right_size - overlap_size <= 6
)


def supports(overlap_size: int, left_size: int, right_size: int):
    rows = []
    for core in itertools.combinations(range(6), overlap_size):
        outside = [coordinate for coordinate in range(6) if coordinate not in core]
        for left_extra in itertools.combinations(outside, left_size - overlap_size):
            remaining = [
                coordinate for coordinate in outside if coordinate not in left_extra
            ]
            for right_extra in itertools.combinations(
                remaining, right_size - overlap_size
            ):
                rows.append((core, left_extra, right_extra))
    return tuple(rows)


def candidates(overlap_size: int, left_size: int, right_size: int):
    return [
        (support, identity_count, overlap_size, left_size, right_size)
        for support in supports(overlap_size, left_size, right_size)
        for identity_count in range(1, 6)
    ]


def parameter_symbols(overlap_size: int, left_size: int, right_size: int):
    left_core = sp.symbols(f"u1:{overlap_size}")
    scale = sp.symbols("t")
    right_ratios = sp.symbols(f"q2:{overlap_size}")
    left_extra = sp.symbols(f"l0:{left_size - overlap_size}")
    right_extra = sp.symbols(f"r0:{right_size - overlap_size}")
    return (*left_core, scale, *right_ratios, *left_extra, *right_extra)


def split_parameters(parameters, overlap_size, left_extra_count):
    left_core_count = overlap_size - 1
    right_ratio_count = overlap_size - 2
    left_core = parameters[:left_core_count]
    scale = parameters[left_core_count]
    right_ratios = parameters[
        left_core_count + 1 : left_core_count + 1 + right_ratio_count
    ]
    left_extra_start = left_core_count + 1 + right_ratio_count
    left_extra = parameters[
        left_extra_start : left_extra_start + left_extra_count
    ]
    right_extra = parameters[left_extra_start + left_extra_count :]
    return left_core, scale, right_ratios, left_extra, right_extra


def leading_right_core_form(left_core, right_ratios):
    return left_core[0] + sum(
        left_coefficient * right_ratio
        for left_coefficient, right_ratio in zip(left_core[1:], right_ratios)
    )


def selection_points(parameter_count: int):
    points = [[1] * parameter_count]
    for index in range(parameter_count):
        point = [1] * parameter_count
        point[index] = 2
        points.append(point)
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    points.append(list(primes[:parameter_count]))
    return tuple(tuple(point) for point in points)


def transformed_coordinate(
    tail,
    coordinate,
    core,
    left_extra_support,
    right_extra_support,
    parameters,
):
    overlap_size = len(core)
    left_core, scale, right_ratios, left_extra, right_extra = split_parameters(
        parameters, overlap_size, len(left_extra_support)
    )
    left_support = core + left_extra_support
    if coordinate not in left_support:
        return tail[coordinate]
    leading = leading_right_core_form(left_core, right_ratios)
    right_core_coefficients = (-scale * leading, scale) + tuple(
        scale * ratio for ratio in right_ratios
    )
    right_form = sum(
        coefficient * tail[index]
        for coefficient, index in zip(right_core_coefficients, core)
    )
    right_form += sum(
        coefficient * tail[index]
        for coefficient, index in zip(right_extra, right_extra_support)
    )
    left_core_coefficients = (1,) + tuple(left_core)
    if coordinate in core:
        left_coefficient = left_core_coefficients[core.index(coordinate)]
    else:
        left_coefficient = left_extra[left_extra_support.index(coordinate)]
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


def witness_assignments(identity_count, support, point, weighted=False):
    core, left_extra, right_extra = support
    pivots = {}
    degrees = range(6 - identity_count + 1) if weighted else (None,)
    left_support = set(core + left_extra)
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
            feature = assignment_feature(
                assignment,
                identity_count,
                core,
                left_extra,
                right_extra,
                point,
            )
            base3.base33.base2.base23.core22.base.add_modular_pivot(
                pivots, feature, assignment
            )
            if len(pivots) == len(TAILS):
                return tuple(pivots[column][1] for column in sorted(pivots))
    return tuple(pivots[column][1] for column in sorted(pivots))


def allowed_boundary_polynomials(
    parameters, overlap_size, left_extra_count, right_extra_count
):
    left_core, scale, right_ratios, left_extra, right_extra = split_parameters(
        parameters, overlap_size, left_extra_count
    )
    expressions = {str(item): item for item in parameters}
    leading = leading_right_core_form(left_core, right_ratios)
    expressions["leading_right_core"] = leading
    return {
        label: sp.Poly(expression, *parameters, domain=sp.QQ).monic()
        for label, expression in expressions.items()
    }


def allowed_boundary_factorization(
    polynomial,
    parameters,
    overlap_size,
    left_extra_count,
    right_extra_count,
):
    if polynomial is None or polynomial.is_zero:
        return False, {}, []
    allowed = allowed_boundary_polynomials(
        parameters, overlap_size, left_extra_count, right_extra_count
    )
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
    support, identity_count, overlap_size, left_size, right_size = candidate
    core, left_extra, right_extra = support
    parameter_count = left_size + right_size - 2
    if len(point) != parameter_count:
        raise ValueError("selection point has the wrong parameter count")
    witnesses = witness_assignments(identity_count, support, point, weighted=weighted)
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
        return common, witnesses, None
    parameters = parameter_symbols(overlap_size, left_size, right_size)
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
    return common, witnesses, determinant


def minor_probe(candidate, point, weighted=False):
    common, witnesses, determinant = exact_minor(candidate, point, weighted=weighted)
    _support, _count, overlap_size, left_size, right_size = candidate
    if determinant is None:
        return {**common, "status": "RANK_DEFICIENT_AT_SELECTION_POINT"}
    parameters = parameter_symbols(overlap_size, left_size, right_size)
    covered, allowed_exponents, unresolved = allowed_boundary_factorization(
        determinant,
        parameters,
        overlap_size,
        left_size - overlap_size,
        right_size - overlap_size,
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
    support, identity_count, overlap_size, left_size, right_size = candidate
    parameter_count = left_size + right_size - 2
    parameters = parameter_symbols(overlap_size, left_size, right_size)
    gcd_polynomial = None
    minors = []
    witness_sample_sets = []
    covered = False
    allowed_exponents = {}
    unresolved = []
    for point in selection_points(parameter_count):
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
            gcd_polynomial,
            parameters,
            overlap_size,
            left_size - overlap_size,
            right_size - overlap_size,
        )
        if covered:
            break
    core, left_extra, right_extra = support
    return {
        "core_support": list(core),
        "left_extra_support": list(left_extra),
        "right_extra_support": list(right_extra),
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
        "status": ROW_STATUS if covered else "UNRESOLVED_COMMON_MINOR_ZERO_LOCUS",
        "witness_sample_sets": witness_sample_sets,
    }


def weighted_cover_trial(candidate):
    return cover_trial(candidate, weighted=True)


def overlap_face_path(overlap_size: int, pair):
    if overlap_size == 3:
        return base3.overlap_three_face_path(pair)
    word = OVERLAP_WORDS[overlap_size].lower()
    name = (
        f"n7_mixed_glynn_overlap_{word}_{pair[0]}{pair[1]}_"
        "nilpotent_shear_tail_rank.json"
    )
    return ROOT / "data" / name


def face_certificates(overlap_size: int, left_size: int, right_size: int):
    paths = [
        overlap_face_path(overlap_size - 1, (left_size - 1, right_size)),
        overlap_face_path(overlap_size - 1, (left_size, right_size - 1)),
    ]
    if left_size > overlap_size:
        paths.append(
            overlap_face_path(overlap_size, (left_size - 1, right_size))
        )
    if right_size > overlap_size:
        paths.append(
            overlap_face_path(overlap_size, (left_size, right_size - 1))
        )
    right_extra_count = right_size - overlap_size
    if right_extra_count:
        paths.append(base3.disjoint_face_path(left_size, right_extra_count))
    return [base3.exact_status(path) for path in dict.fromkeys(paths)]


def build_payload(args):
    family = candidates(args.overlap_size, args.left_size, args.right_size)
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
    imported_certificates = face_certificates(
        args.overlap_size, args.left_size, args.right_size
    )
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    trial_function = weighted_cover_trial if args.weighted_selection else cover_trial
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial_function, selected, chunksize=1))
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
    complete = status_counts == {ROW_STATUS: len(selected)}
    whole_family = args.start_index == 0 and stop_index == len(family)
    pair_label = f"{args.left_size}{args.right_size}"
    overlap_label = OVERLAP_WORDS[args.overlap_size]
    return {
        "schema_version": 1,
        "status": (
            f"EXACT_ALL_OVERLAP_{overlap_label}_{pair_label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            if complete and whole_family
            else (
                f"EXACT_CHUNK_OVERLAP_{overlap_label}_{pair_label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
                if complete
                else f"INCOMPLETE_CHUNK_OVERLAP_{overlap_label}_{pair_label}_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
            )
        ),
        "field": "characteristic zero",
        "left_support_size": args.left_size,
        "right_support_size": args.right_size,
        "overlap_size": args.overlap_size,
        "support_count": len(
            supports(args.overlap_size, args.left_size, args.right_size)
        ),
        "multiplicity_split_count": 5,
        "candidate_count": len(selected),
        "full_candidate_count": len(family),
        "candidate_start_index": args.start_index,
        "candidate_stop_index_exclusive": stop_index,
        "parameter_count": args.left_size + args.right_size - 2,
        "parametrization": "u=(1,u_core,left extras), v=t*(-sum(u_i*q_i),1,q_core) plus independent right extras",
        "nilpotence_identity": "v^T u = 0 because the extra supports are disjoint",
        "dense_full_support_condition": "all coordinate parameters and the leading right-core form are nonzero",
        "allowed_boundary_divisors": list(
            allowed_boundary_polynomials(
                parameter_symbols(
                    args.overlap_size, args.left_size, args.right_size
                ),
                args.overlap_size,
                args.left_size - args.overlap_size,
                args.right_size - args.overlap_size,
            )
        ),
        "workers": args.workers,
        "weighted_selection": args.weighted_selection,
        "status_counts": status_counts,
        "face_certificates": imported_certificates,
        "witness_samples_first_5": samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            f"The exact family has support sizes ({args.left_size},{args.right_size}), overlap exactly {args.overlap_size}, and v^T u=0.",
            "Every oriented coordinate support and all five positive identity/shear multiplicity splits are represented.",
            "Exact minor gcd factors are confined to the complement of the dense full-support chart; every such divisor reduces to an imported smaller-overlap, same-overlap lower-support, or disjoint-support certificate.",
            "The result remains local to rank-one nilpotent shears in the synchronized mixed-Glynn endpoint model and does not prove arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--overlap-size", type=int, required=True)
    parser.add_argument("--left-size", type=int, required=True)
    parser.add_argument("--right-size", type=int, required=True)
    parser.add_argument("--max-candidates", type=int, default=150)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--minor-probe-index", type=int)
    parser.add_argument("--selection-point")
    parser.add_argument("--weighted-selection", action="store_true")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    family_label = (args.overlap_size, args.left_size, args.right_size)
    if family_label not in ALLOWED_FAMILIES:
        raise ValueError("unsupported higher-overlap support family")
    family = candidates(*family_label)
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
