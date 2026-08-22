#!/usr/bin/env python3
"""Exact invalid-tail minors for two-direction coordinate shears in perm7."""

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
import n7_equality_packet_crossdegree_search as base  # noqa: E402
import n7_mixed_glynn_graph_search as graph  # noqa: E402


TAILS = tuple(graph.tail_dictionary(0))
SUPPORTS = tuple(
    ("same_target", fixed, first, second)
    for fixed in range(6)
    for first, second in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != fixed], 2
    )
) + tuple(
    ("same_source", fixed, first, second)
    for fixed in range(6)
    for first, second in itertools.combinations(
        [coordinate for coordinate in range(6) if coordinate != fixed], 2
    )
)
CANDIDATE_COUNT = len(SUPPORTS) * 5


def transformed_coordinate(
    tail: tuple[int, ...],
    coordinate: int,
    shape: str,
    fixed: int,
    first: int,
    second: int,
    first_parameter,
    second_parameter,
):
    value = tail[coordinate]
    if shape == "same_target":
        if coordinate == fixed:
            value += first_parameter * tail[first] + second_parameter * tail[second]
    elif shape == "same_source":
        if coordinate == first:
            value += first_parameter * tail[fixed]
        elif coordinate == second:
            value += second_parameter * tail[fixed]
    else:
        raise ValueError(shape)
    return value


def assignment_feature(
    assignment: tuple[int, ...],
    identity_count: int,
    shape: str,
    fixed: int,
    first: int,
    second: int,
    first_parameter,
    second_parameter,
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
                    first,
                    second,
                    first_parameter,
                    second_parameter,
                )
        feature.append(value)
    return feature


def add_modular_pivot(pivots, raw_row, assignment) -> None:
    row = [int(value) % base.PRIME for value in raw_row]
    while True:
        column = next((index for index, value in enumerate(row) if value), None)
        if column is None:
            return
        if column not in pivots:
            inverse = pow(row[column], base.PRIME - 2, base.PRIME)
            pivots[column] = (
                [value * inverse % base.PRIME for value in row],
                assignment,
            )
            return
        multiple = row[column]
        pivot = pivots[column][0]
        row = [
            (value - multiple * pivot_value) % base.PRIME
            for value, pivot_value in zip(row, pivot)
        ]


def witness_assignments(identity_count: int, support) -> tuple[tuple[int, ...], ...]:
    shape, fixed, first, second = support
    pivots = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = assignment_feature(
            assignment,
            identity_count,
            shape,
            fixed,
            first,
            second,
            1,
            1,
        )
        add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def trial(candidate) -> dict[str, object]:
    support, identity_count = candidate
    shape, fixed, first, second = support
    witnesses = witness_assignments(identity_count, support)
    if len(witnesses) != len(TAILS):
        return {
            "shape": shape,
            "fixed": fixed,
            "first": first,
            "second": second,
            "identity_count": identity_count,
            "rank_at_one_one": len(witnesses),
            "status": "RANK_DEFICIENT_AT_ONE_ONE",
        }
    first_parameter, second_parameter = sp.symbols("s t")
    matrix = sp.Matrix(
        [
            [
                value
                for value in assignment_feature(
                    assignment,
                    identity_count,
                    shape,
                    fixed,
                    first,
                    second,
                    first_parameter,
                    second_parameter,
                )
            ]
            for assignment in witnesses
        ]
    ).T
    determinant = sp.Poly(
        matrix.det(method="domain-ge"), first_parameter, second_parameter, domain=sp.ZZ
    )
    terms = determinant.terms()
    monomial = (
        len(terms) == 1
        and sum(terms[0][0]) > 0
        and terms[0][1] != 0
    )
    return {
        "shape": shape,
        "fixed": fixed,
        "first": first,
        "second": second,
        "identity_count": identity_count,
        "rank_at_one_one": len(witnesses),
        "determinant_total_degree": determinant.total_degree(),
        "determinant_term_count": len(terms),
        "determinant_coefficient": str(terms[0][1]) if monomial else None,
        "first_parameter_exponent": terms[0][0][0] if monomial else None,
        "second_parameter_exponent": terms[0][0][1] if monomial else None,
        "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
        "status": "NONZERO_BIVARIATE_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    single = json.loads(
        (
            ROOT
            / "data"
            / "n7_mixed_glynn_elementary_shear_tail_rank.json"
        ).read_text(encoding="utf-8")
    )
    if single["status_counts"] != {"NONZERO_MONOMIAL_MINOR": 150}:
        raise AssertionError("single-shear certificate mismatch")

    candidates = [
        (support, identity_count)
        for support in SUPPORTS
        for identity_count in range(1, 6)
    ]
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, candidates, chunksize=1))
    rows.sort(
        key=lambda row: (
            row["shape"],
            row["fixed"],
            row["first"],
            row["second"],
            row["identity_count"],
        )
    )
    witness_samples = [
        {
            "shape": row["shape"],
            "fixed": row["fixed"],
            "first": row["first"],
            "second": row["second"],
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
        if row.get("first_parameter_exponent") is not None:
            key = f"{row['first_parameter_exponent']}+{row['second_parameter_exponent']}"
            exponent_histogram[key] = exponent_histogram.get(key, 0) + 1
    complete = status_counts == {
        "NONZERO_BIVARIATE_MONOMIAL_MINOR": CANDIDATE_COUNT
    }
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_TWO_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_TWO_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "shape_counts": {"same_target": 60, "same_source": 60},
        "support_count": len(SUPPORTS),
        "multiplicity_split_count": 5,
        "candidate_formula": "(2 * 6 * binom(5,2)) * 5",
        "candidate_count": CANDIDATE_COUNT,
        "workers": args.workers,
        "status_counts": status_counts,
        "parameter_exponent_pair_histogram": dict(sorted(exponent_histogram.items())),
        "single_shear_axis_certificate": single["status"],
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The exact family consists of identity and one rank-one coordinate shear with either two sources and one target or one source and two targets.",
            "All 120 coordinate supports and five positive multiplicity splits are represented.",
            "For both parameters nonzero, each exact ZZ[s,t] minor is a nonzero monomial; the coordinate axes are covered by the imported single-shear certificate.",
            "Therefore every nonzero parameter pair in characteristic zero has invalid-tail rank 42 and zero local target intersection.",
            "The theorem does not cover three or more shear directions, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
