#!/usr/bin/env python3
"""Exact remaining disjoint-support rank-one shear minors for perm7."""

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
import n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank as base  # noqa: E402


TAILS = base.TAILS
ALLOWED_SIZES = ((2, 3), (3, 2), (2, 4), (4, 2), (3, 3))


def supports(left_size: int, right_size: int):
    return tuple(
        (left, right)
        for left in itertools.combinations(range(6), left_size)
        for right in itertools.combinations(
            [coordinate for coordinate in range(6) if coordinate not in left],
            right_size,
        )
    )


def candidates(left_size: int, right_size: int):
    return [
        (support, identity_count, left_size, right_size)
        for support in supports(left_size, right_size)
        for identity_count in range(1, 6)
    ]


def transformed_coordinate(
    tail: tuple[int, ...],
    coordinate: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
    parameters,
):
    left_parameters = (1,) + tuple(parameters[: len(left) - 1])
    right_parameters = parameters[len(left) - 1 :]
    if coordinate not in left:
        return tail[coordinate]
    left_coefficient = left_parameters[left.index(coordinate)]
    right_form = sum(
        coefficient * tail[index]
        for coefficient, index in zip(right_parameters, right)
    )
    return tail[coordinate] + left_coefficient * right_form


def assignment_feature(
    assignment: tuple[int, ...],
    identity_count: int,
    left: tuple[int, ...],
    right: tuple[int, ...],
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
                else transformed_coordinate(tail, coordinate, left, right, parameters)
            )
        feature.append(value)
    return feature


def witness_assignments(
    identity_count: int,
    support,
    parameter_count: int,
) -> tuple[tuple[int, ...], ...]:
    left, right = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment,
            identity_count,
            left,
            right,
            (1,) * parameter_count,
        )
        base.two.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def trial(candidate) -> dict[str, object]:
    support, identity_count, left_size, right_size = candidate
    left, right = support
    parameter_count = left_size + right_size - 1
    witnesses = witness_assignments(identity_count, support, parameter_count)
    common = {
        "left_support": list(left),
        "right_support": list(right),
        "identity_count": identity_count,
        "rank_at_all_one": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return {**common, "status": "RANK_DEFICIENT_AT_ALL_ONE"}

    parameters = sp.symbols(f"p0:{parameter_count}")
    matrix = sp.Matrix(
        [
            assignment_feature(
                assignment, identity_count, left, right, parameters
            )
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(matrix.det(method="domain-ge"), *parameters, domain=sp.ZZ)
    terms = determinant.terms()
    monomial = len(terms) == 1 and sum(terms[0][0]) > 0 and terms[0][1] != 0
    return {
        **common,
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(terms),
        "determinant_coefficient": str(terms[0][1]) if monomial else None,
        "parameter_exponents": list(terms[0][0]) if monomial else None,
        "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
        "status": "NONZERO_MULTIVARIATE_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def face_certificate_paths(left_size: int, right_size: int):
    paths = [ROOT / "data" / "n7_mixed_glynn_five_direction_shear_tail_rank.json"]
    if left_size >= 2 and right_size >= 2:
        paths.append(
            ROOT / "data" / "n7_mixed_glynn_disjoint_22_rank_one_shear_tail_rank.json"
        )
    if (left_size, right_size) in ((2, 4), (3, 3)):
        paths.append(
            ROOT / "data" / "n7_mixed_glynn_disjoint_23_rank_one_shear_tail_rank.json"
        )
    if (left_size, right_size) in ((4, 2), (3, 3)):
        paths.append(
            ROOT / "data" / "n7_mixed_glynn_disjoint_32_rank_one_shear_tail_rank.json"
        )
    return tuple(dict.fromkeys(paths))


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    family = candidates(args.left_size, args.right_size)
    candidate_count = len(family)
    if candidate_count > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")

    face_certificates = []
    for path in face_certificate_paths(args.left_size, args.right_size):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not str(payload["status"]).startswith("EXACT_ALL_"):
            raise AssertionError(f"coordinate-face certificate mismatch: {path.name}")
        face_certificates.append(payload["status"])

    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, family, chunksize=1))
    rows.sort(
        key=lambda row: (
            row["left_support"], row["right_support"], row["identity_count"]
        )
    )
    witness_samples = [
        {
            "left_support": row["left_support"],
            "right_support": row["right_support"],
            "identity_count": row["identity_count"],
            "witness_assignments_first_5": row["witness_assignments_first_5"],
        }
        for row in rows[:5]
        if "witness_assignments_first_5" in row
    ]
    for row in rows:
        row.pop("witness_assignments_first_5", None)

    status_counts = {}
    exponent_histogram = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        if row.get("parameter_exponents") is not None:
            key = "+".join(str(value) for value in row["parameter_exponents"])
            exponent_histogram[key] = exponent_histogram.get(key, 0) + 1
    complete = status_counts == {
        "NONZERO_MULTIVARIATE_MONOMIAL_MINOR": candidate_count
    }
    size_label = f"{args.left_size}{args.right_size}"
    return {
        "schema_version": 1,
        "status": (
            f"EXACT_ALL_DISJOINT_{size_label}_RANK_ONE_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else f"INCOMPLETE_DISJOINT_{size_label}_RANK_ONE_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "left_support_size": args.left_size,
        "right_support_size": args.right_size,
        "support_count": len(supports(args.left_size, args.right_size)),
        "multiplicity_split_count": 5,
        "candidate_formula": (
            f"binom(6,{args.left_size}) * "
            f"binom({6-args.left_size},{args.right_size}) * 5"
        ),
        "candidate_count": candidate_count,
        "parameter_count": args.left_size + args.right_size - 1,
        "normalization": "first left-support coefficient equals one",
        "workers": args.workers,
        "status_counts": status_counts,
        "parameter_exponent_histogram": dict(sorted(exponent_histogram.items())),
        "coordinate_face_certificates": face_certificates,
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            f"The exact dense-support family is I+u v^T with disjoint support sizes ({args.left_size},{args.right_size}), modulo rank-one scaling.",
            "Every ordered coordinate support and all five positive identity/shear multiplicity splits are represented.",
            "A monomial minor covers the full-support parameter torus; imported lower-support certificates cover every proper coordinate face.",
            "The result does not cover overlapping supports, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left-size", type=int, required=True)
    parser.add_argument("--right-size", type=int, required=True)
    parser.add_argument("--max-candidates", type=int, default=300)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if (args.left_size, args.right_size) not in ALLOWED_SIZES:
        raise ValueError("unsupported disjoint-support size pair")
    family = candidates(args.left_size, args.right_size)
    if args.probe_index is None:
        payload = build_payload(args)
    else:
        if not 0 <= args.probe_index < len(family):
            raise ValueError("--probe-index is outside the candidate family")
        payload = trial(family[args.probe_index])
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
