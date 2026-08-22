#!/usr/bin/env python3
"""Directed packet-B search on generalized moment-curve graph complements."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from flint import nmod_mat


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_crossdegree_search as base  # noqa: E402


P = base.PRIME
N = base.N
RANK_SIX_TERM_COUNT = 7
RANK_SIX_MIDDLE_RANK = 25
GRAPH_TERM_COUNT = 42
GRAPH_MIDDLE_PROFILE_SUM = 72
RECTANGULAR_ENDPOINT_SUM = 2870


def exponent_sums(weights: tuple[int, ...], degree: int) -> tuple[int, ...]:
    values = (0, *weights)
    return tuple(
        sorted(
            {
                sum(choice)
                for choice in itertools.combinations_with_replacement(values, degree)
            }
        )
    )


def exact_curve_rank(weights: tuple[int, ...], degree: int) -> int:
    exponents = exponent_sums(weights, degree)
    rows = [
        [pow(parameter, exponent, P) for exponent in exponents]
        for parameter in range(1, 43)
    ]
    return nmod_mat(rows, P).rank()


def scan_weight_profiles(max_weight: int) -> tuple[int, list[tuple[int, ...]]]:
    candidate_count = math.comb(max_weight, 6)
    matches: list[tuple[int, ...]] = []
    for weights in itertools.combinations(range(1, max_weight + 1), 6):
        h3 = min(42, len(exponent_sums(weights, 3)))
        h4 = min(42, len(exponent_sums(weights, 4)))
        if h3 + h4 == GRAPH_MIDDLE_PROFILE_SUM:
            matches.append(weights)
    return candidate_count, matches


def curve_packet_values(
    weights: tuple[int, ...], evaluations: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    a_indices = [row * N + column for row in range(N) for column in range(1, N)]
    w_indices = [row * N for row in range(N)]
    a_values = evaluations[a_indices]
    w_values = evaluations[w_indices]
    derivative_rows: list[np.ndarray] = []
    term_rows: list[np.ndarray] = []

    for block in range(N):
        basis = a_values[6 * block : 6 * (block + 1)]
        factors = np.vstack((basis, basis[0]))
        derivative_rows.extend(base.omitted_products(factors))
        term_rows.append(base.modular_product_rows(factors))

    for parameter in range(1, 43):
        tail = np.asarray([pow(parameter, weight, P) for weight in weights], dtype=np.int64)
        graph = np.zeros((42, N), dtype=np.int64)
        for row in range(N):
            graph[6 * row : 6 * (row + 1), row] = tail
        factors = (graph.T @ a_values + w_values) % P
        derivative_rows.extend(base.omitted_products(factors))
        term_rows.append(base.modular_product_rows(factors))
    return np.asarray(derivative_rows), np.asarray(term_rows)


def trial(
    weights: tuple[int, ...],
    evaluations: np.ndarray,
    degree_six_targets: np.ndarray,
    degree_seven_target: np.ndarray,
) -> dict[str, object]:
    h3 = exact_curve_rank(weights, 3)
    h4 = exact_curve_rank(weights, 4)
    h5 = exact_curve_rank(weights, 5)
    h6 = exact_curve_rank(weights, 6)
    derivative_rows, term_rows = curve_packet_values(weights, evaluations)
    d6_rank = base.modular_rank(derivative_rows)
    d6_augmented = base.modular_rank(np.vstack((derivative_rows, degree_six_targets)))
    d7_rank = base.modular_rank(term_rows)
    d7_augmented = base.modular_rank(np.vstack((term_rows, degree_seven_target)))
    return {
        "weights": list(weights),
        "point_code_hilbert_3_to_6": [h3, h4, h5, h6],
        "rectangular_middle_rank_sum": (
            2 * RANK_SIX_TERM_COUNT * RANK_SIX_MIDDLE_RANK + 35 * (h3 + h4)
        ),
        "degree_six_rank": d6_rank,
        "degree_six_target_increment": d6_augmented - d6_rank,
        "degree_seven_rank": d7_rank,
        "degree_seven_target_increment": d7_augmented - d7_rank,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    if args.max_weight < 6:
        raise ValueError("max_weight must be at least six")
    workers = int(args.workers)
    if workers < 1 or workers > (base.os.cpu_count() or 1):
        raise ValueError("workers must be between one and the visible CPU count")
    started = time.perf_counter()
    scanned, approximate_matches = scan_weight_profiles(args.max_weight)
    exact_matches = [
        weights
        for weights in approximate_matches
        if exact_curve_rank(weights, 3) + exact_curve_rank(weights, 4)
        == GRAPH_MIDDLE_PROFILE_SUM
    ]
    rng = np.random.default_rng(args.seed)
    evaluations = rng.integers(0, P, size=(base.V_DIM, args.evaluations), dtype=np.int64)
    degree_six_targets, degree_seven_target = base.permanent_targets(evaluations)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(
                trial,
                weights,
                evaluations,
                degree_six_targets,
                degree_seven_target,
            )
            for weights in exact_matches
        ]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    results.sort(key=lambda row: tuple(row["weights"]))
    elapsed = time.perf_counter() - started
    return {
        "schema_version": 1,
        "status": "DIRECTED_FINITE_FIELD_CURVE_SUBFAMILY_SEARCH_NOT_A_RANK_PROOF",
        "field": f"F_{P}",
        "endpoint_middle_rank_sum": RECTANGULAR_ENDPOINT_SUM,
        "graph_point_code_middle_profile_sum": GRAPH_MIDDLE_PROFILE_SUM,
        "max_weight": args.max_weight,
        "weight_candidate_count": scanned,
        "approximate_endpoint_profile_count": len(approximate_matches),
        "exact_endpoint_profile_count": len(exact_matches),
        "workers": workers,
        "evaluation_columns": args.evaluations,
        "elapsed_seconds": elapsed,
        "zero_degree_six_increment_count": sum(
            row["degree_six_target_increment"] == 0 for row in results
        ),
        "zero_degree_seven_increment_count": sum(
            row["degree_seven_target_increment"] == 0 for row in results
        ),
        "minimum_degree_six_target_increment": min(
            (row["degree_six_target_increment"] for row in results), default=None
        ),
        "results": results,
        "claim_boundary": [
            "The scan exhausts only strictly increasing monomial-curve weights in the displayed box.",
            "The profile sum 72 is forced by seven rank-six terms of middle rank 25 and forty-two rank-seven graph terms.",
            "A positive target increment excludes that fixed finite-field graph packet.",
            "The evaluation projection is a diagnostic; a zero increment would require exact lifting.",
            "This does not classify either N=49 equality packet or prove lower fifty.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-weight", type=int, default=24)
    parser.add_argument("--evaluations", type=int, default=400)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.evaluations < 392:
        raise SystemExit("evaluations must be at least 392")
    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
