#!/usr/bin/env python3
"""Exact invalid-tail minors for three-direction rank-one shears in perm7."""

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
import n7_mixed_glynn_two_direction_shear_tail_rank as two  # noqa: E402


TAILS = two.TAILS
SUPPORTS = tuple(
    ("same_target", fixed, directions)
    for fixed in range(6)
    for directions in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != fixed], 3
    )
) + tuple(
    ("same_source", fixed, directions)
    for fixed in range(6)
    for directions in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != fixed], 3
    )
)
CANDIDATE_COUNT = len(SUPPORTS) * 5


def transformed_coordinate(
    tail: tuple[int, ...],
    coordinate: int,
    shape: str,
    fixed: int,
    directions: tuple[int, ...],
    parameters,
):
    value = tail[coordinate]
    if shape == "same_target":
        if coordinate == fixed:
            value += sum(
                parameter * tail[direction]
                for parameter, direction in zip(parameters, directions)
            )
    elif shape == "same_source":
        for parameter, direction in zip(parameters, directions):
            if coordinate == direction:
                value += parameter * tail[fixed]
    else:
        raise ValueError(shape)
    return value


def assignment_feature(
    assignment: tuple[int, ...],
    identity_count: int,
    shape: str,
    fixed: int,
    directions: tuple[int, ...],
    parameters,
):
    feature = []
    for tail in TAILS:
        value = 1
        for block, column in enumerate(assignment):
            if column == 0:
                continue
            coordinate = column - 1
            if block < identity_count:
                value *= tail[coordinate]
            else:
                value *= transformed_coordinate(
                    tail,
                    coordinate,
                    shape,
                    fixed,
                    directions,
                    parameters,
                )
        feature.append(value)
    return feature


def witness_assignments(identity_count: int, support) -> tuple[tuple[int, ...], ...]:
    shape, fixed, directions = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment,
            identity_count,
            shape,
            fixed,
            directions,
            (1, 1, 1),
        )
        two.add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def trial(candidate) -> dict[str, object]:
    support, identity_count = candidate
    shape, fixed, directions = support
    witnesses = witness_assignments(identity_count, support)
    common = {
        "shape": shape,
        "fixed": fixed,
        "directions": list(directions),
        "identity_count": identity_count,
        "rank_at_all_one": len(witnesses),
    }
    if len(witnesses) != len(TAILS):
        return {**common, "status": "RANK_DEFICIENT_AT_ALL_ONE"}

    parameters = sp.symbols("s t u")
    matrix = sp.Matrix(
        [
            assignment_feature(
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
        "status": "NONZERO_TRIVARIATE_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def candidates():
    return [
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in range(1, 6)
    ]


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    all_candidates = candidates()
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")

    two_direction = json.loads(
        (ROOT / "data" / "n7_mixed_glynn_two_direction_shear_tail_rank.json").read_text(
            encoding="utf-8"
        )
    )
    if two_direction["status_counts"] != {
        "NONZERO_BIVARIATE_MONOMIAL_MINOR": 600
    }:
        raise AssertionError("two-direction coordinate-face certificate mismatch")

    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, all_candidates, chunksize=1))
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
        "NONZERO_TRIVARIATE_MONOMIAL_MINOR": CANDIDATE_COUNT
    }
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_THREE_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_THREE_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "shape_counts": {"same_target": 60, "same_source": 60},
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "(2 * 6 * binom(5,3)) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "workers": args.workers,
        "status_counts": status_counts,
        "parameter_exponent_triple_histogram": dict(sorted(exponent_histogram.items())),
        "coordinate_face_certificate": two_direction["status"],
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity and one rank-one coordinate shear with a three-edge star support.",
            "All 120 supports and five positive multiplicity splits are represented.",
            "A monomial minor proves full invalid-tail rank when all three parameters are nonzero; coordinate faces are imported from the two-direction certificate.",
            "The theorem does not cover four or more directions, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
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
        payload = trial(candidates()[args.probe_index])
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
