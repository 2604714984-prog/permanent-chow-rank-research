#!/usr/bin/env python3
"""Exact invalid-tail minors for four/five-direction rank-one perm7 shears."""

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
import n7_mixed_glynn_three_direction_shear_tail_rank as three  # noqa: E402


TAILS = three.TAILS


def supports(arm_count: int):
    return tuple(
        ("same_target", fixed, directions)
        for fixed in range(6)
        for directions in itertools.combinations(
            [coordinate for coordinate in range(6) if coordinate != fixed],
            arm_count,
        )
    ) + tuple(
        ("same_source", fixed, directions)
        for fixed in range(6)
        for directions in itertools.combinations(
            [coordinate for coordinate in range(6) if coordinate != fixed],
            arm_count,
        )
    )


def candidates(arm_count: int):
    return [
        (support, identity_count, arm_count)
        for support in supports(arm_count)
        for identity_count in range(1, 6)
    ]


def witness_assignments(
    identity_count: int, support, arm_count: int
) -> tuple[tuple[int, ...], ...]:
    shape, fixed, directions = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = three.assignment_feature(
            assignment,
            identity_count,
            shape,
            fixed,
            directions,
            (1,) * arm_count,
        )
        three.two.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def trial(candidate) -> dict[str, object]:
    support, identity_count, arm_count = candidate
    shape, fixed, directions = support
    witnesses = witness_assignments(identity_count, support, arm_count)
    common = {
        "arm_count": arm_count,
        "shape": shape,
        "fixed": fixed,
        "directions": list(directions),
        "identity_count": identity_count,
        "rank_at_all_one": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return {**common, "status": "RANK_DEFICIENT_AT_ALL_ONE"}

    parameters = sp.symbols(f"p0:{arm_count}")
    matrix = sp.Matrix(
        [
            three.assignment_feature(
                assignment,
                identity_count,
                shape,
                fixed,
                directions,
                parameters,
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


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    family = candidates(args.arms)
    candidate_count = len(family)
    if candidate_count > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")

    face_name = (
        "n7_mixed_glynn_three_direction_shear_tail_rank.json"
        if args.arms == 4
        else "n7_mixed_glynn_four_direction_shear_tail_rank.json"
    )
    face = json.loads((ROOT / "data" / face_name).read_text(encoding="utf-8"))
    expected_face_status = (
        "EXACT_ALL_THREE_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
        if args.arms == 4
        else "EXACT_ALL_FOUR_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
    )
    if face["status"] != expected_face_status:
        raise AssertionError("coordinate-face certificate mismatch")

    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, family, chunksize=1))
    rows.sort(
        key=lambda row: (
            row["shape"],
            row["fixed"],
            row["directions"],
            row["identity_count"],
        )
    )
    witness_samples = [
        {
            "shape": row["shape"],
            "fixed": row["fixed"],
            "directions": row["directions"],
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
    arm_word = "FOUR" if args.arms == 4 else "FIVE"
    return {
        "schema_version": 1,
        "status": (
            f"EXACT_ALL_{arm_word}_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else f"INCOMPLETE_{arm_word}_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "arm_count": args.arms,
        "shape_counts": {
            "same_target": len(supports(args.arms)) // 2,
            "same_source": len(supports(args.arms)) // 2,
        },
        "support_count": len(supports(args.arms)),
        "multiplicity_split_count": 5,
        "candidate_formula": f"(2 * 6 * binom(5,{args.arms})) * 5",
        "candidate_count": candidate_count,
        "workers": args.workers,
        "status_counts": status_counts,
        "parameter_exponent_histogram": dict(sorted(exponent_histogram.items())),
        "coordinate_face_certificate": face["status"],
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            f"The exact family consists of identity and one rank-one coordinate shear with a {args.arms}-edge star support.",
            "Every coordinate support and all five positive multiplicity splits are represented.",
            "A monomial minor covers the dense parameter torus; imported lower-direction certificates cover every proper coordinate face.",
            "The result remains local to rank-one coordinate shears and does not prove arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arms", type=int, choices=(4, 5), required=True)
    parser.add_argument("--max-candidates", type=int, default=300)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--probe-index", type=int)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    family = candidates(args.arms)
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
