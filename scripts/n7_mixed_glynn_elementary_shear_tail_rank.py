#!/usr/bin/env python3
"""Exact invalid-tail minors for all elementary GL(6) shears in perm7."""

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
DIRECTIONS = tuple(
    (target, source) for target in range(6) for source in range(6) if target != source
)
CANDIDATE_COUNT = len(DIRECTIONS) * 5


def numeric_coefficient(
    tail: tuple[int, ...], column: int, shear: bool, target: int, source: int
) -> int:
    if column == 0:
        return 1
    coordinate = column - 1
    value = tail[coordinate]
    if shear and coordinate == target:
        value += tail[source]
    return value


def add_modular_pivot(
    pivots: dict[int, tuple[list[int], tuple[int, ...]]],
    raw_row: list[int],
    assignment: tuple[int, ...],
) -> None:
    row = [value % base.PRIME for value in raw_row]
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


def witness_assignments(
    identity_count: int, target: int, source: int
) -> tuple[tuple[int, ...], ...]:
    pivots: dict[int, tuple[list[int], tuple[int, ...]]] = {}
    for assignment in itertools.product(range(7), repeat=6):
        if len(set(assignment)) == 6:
            continue
        feature = []
        for tail in TAILS:
            value = 1
            for block, column in enumerate(assignment):
                value *= numeric_coefficient(
                    tail,
                    column,
                    block >= identity_count,
                    target,
                    source,
                )
            feature.append(value)
        add_modular_pivot(pivots, feature, assignment)
        if len(pivots) == len(TAILS):
            break
    return tuple(pivots[column][1] for column in sorted(pivots))


def polynomial_coefficient(
    tail: tuple[int, ...],
    column: int,
    shear: bool,
    target: int,
    source: int,
    parameter: sp.Symbol,
) -> sp.Expr:
    if column == 0:
        return sp.Integer(1)
    coordinate = column - 1
    value: sp.Expr = sp.Integer(tail[coordinate])
    if shear and coordinate == target:
        value += parameter * tail[source]
    return value


def trial(candidate: tuple[int, int, int]) -> dict[str, object]:
    target, source, identity_count = candidate
    witnesses = witness_assignments(identity_count, target, source)
    if len(witnesses) != len(TAILS):
        return {
            "target": target,
            "source": source,
            "identity_count": identity_count,
            "rank_at_one": len(witnesses),
            "status": "RANK_DEFICIENT_AT_ONE",
        }

    parameter = sp.Symbol("t")
    matrix = sp.Matrix(
        [
            [
                sp.prod(
                    polynomial_coefficient(
                        tail,
                        column,
                        block >= identity_count,
                        target,
                        source,
                        parameter,
                    )
                    for block, column in enumerate(assignment)
                )
                for assignment in witnesses
            ]
            for tail in TAILS
        ]
    )
    determinant = sp.Poly(matrix.det(method="domain-ge"), parameter, domain=sp.ZZ)
    terms = determinant.terms()
    monomial = len(terms) == 1 and terms[0][0][0] > 0 and terms[0][1] != 0
    return {
        "target": target,
        "source": source,
        "identity_count": identity_count,
        "rank_at_one": len(witnesses),
        "determinant_degree": determinant.degree(),
        "determinant_term_count": len(terms),
        "determinant_coefficient": str(terms[0][1]) if monomial else None,
        "determinant_parameter_exponent": terms[0][0][0] if monomial else None,
        "witness_assignments_first_5": [list(row) for row in witnesses[:5]],
        "status": "NONZERO_MONOMIAL_MINOR" if monomial else "NON_MONOMIAL_MINOR",
    }


def identity_control_rank() -> int:
    return len(witness_assignments(6, 0, 1))


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    candidates = [
        (target, source, identity_count)
        for target, source in DIRECTIONS
        for identity_count in range(1, 6)
    ]
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        rows = list(pool.map(trial, candidates, chunksize=1))
    rows.sort(key=lambda row: (row["target"], row["source"], row["identity_count"]))
    witness_samples = [
        {
            "target": row["target"],
            "source": row["source"],
            "identity_count": row["identity_count"],
            "witness_assignments_first_5": row["witness_assignments_first_5"],
        }
        for row in rows[:5]
        if "witness_assignments_first_5" in row
    ]
    for row in rows:
        row.pop("witness_assignments_first_5", None)
    status_counts = {}
    exponent_counts = {}
    for row in rows:
        status = str(row["status"])
        status_counts[status] = status_counts.get(status, 0) + 1
        exponent = row.get("determinant_parameter_exponent")
        if exponent is not None:
            exponent_counts[str(exponent)] = exponent_counts.get(str(exponent), 0) + 1
    complete = status_counts == {"NONZERO_MONOMIAL_MINOR": CANDIDATE_COUNT}
    return {
        "schema_version": 1,
        "status": (
            "EXACT_ALL_ELEMENTARY_SHEAR_INVALID_TAIL_MINORS"
            if complete
            else "INCOMPLETE_ELEMENTARY_SHEAR_INVALID_TAIL_MINORS"
        ),
        "field": "characteristic zero",
        "tail_count": len(TAILS),
        "direction_count": len(DIRECTIONS),
        "multiplicity_split_count": 5,
        "candidate_formula": "6 * 5 * 5",
        "candidate_count": CANDIDATE_COUNT,
        "identity_control_invalid_tail_rank": identity_control_rank(),
        "workers": args.workers,
        "status_counts": status_counts,
        "determinant_exponent_histogram": dict(sorted(exponent_counts.items())),
        "witness_samples_first_5": witness_samples,
        "rows": rows,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "Every ordered elementary shear I+t*E_ab with a!=b and every positive two-type multiplicity split is represented.",
            "Each displayed 42-by-42 determinant is computed over ZZ[t] and is a nonzero integer multiple of a positive power of t.",
            "Therefore every t!=0 in characteristic zero gives invalid-tail rank 42 and zero local permanent-target intersection.",
            "The theorem covers exactly two graph-transform types, identity and one elementary shear, up to a common monomial coordinate change.",
            "It does not cover several independent shears, arbitrary GL(6) transforms, arbitrary endpoint-B packets, ordinary lower 50, or border rank.",
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
