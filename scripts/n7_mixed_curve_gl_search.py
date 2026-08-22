#!/usr/bin/env python3
"""Random independent GL(6) stress test of mixed moment-curve packets."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_crossdegree_search as base  # noqa: E402
import n7_mixed_curve_endpoint_search as curve  # noqa: E402


P = base.PRIME
N = base.N


def random_gl6(rng: random.Random) -> np.ndarray:
    matrix = np.eye(6, dtype=np.int64)
    for _ in range(20):
        source, target = rng.sample(range(6), 2)
        scalar = rng.randrange(1, P)
        matrix[target] = (matrix[target] + scalar * matrix[source]) % P
    permutation = np.asarray(rng.sample(range(6), 6))
    scales = np.asarray([rng.randrange(1, P) for _ in range(6)], dtype=np.int64)
    return matrix[permutation] * scales[:, None] % P


def transformed_packet_values(
    weights: tuple[int, ...], seed: int, evaluations: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    rng = random.Random(seed)
    transforms = [random_gl6(rng) for _ in range(N)]
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
            graph[6 * row : 6 * (row + 1), row] = transforms[row] @ tail % P
        factors = (graph.T @ a_values + w_values) % P
        derivative_rows.extend(base.omitted_products(factors))
        term_rows.append(base.modular_product_rows(factors))
    return np.asarray(derivative_rows), np.asarray(term_rows)


def trial(
    index: int,
    weights: tuple[int, ...],
    seed: int,
    evaluations: np.ndarray,
    degree_six_targets: np.ndarray,
    degree_seven_target: np.ndarray,
) -> dict[str, object]:
    derivative_rows, term_rows = transformed_packet_values(weights, seed, evaluations)
    d6_rank = base.modular_rank(derivative_rows)
    d6_augmented = base.modular_rank(np.vstack((derivative_rows, degree_six_targets)))
    d7_rank = base.modular_rank(term_rows)
    d7_augmented = base.modular_rank(np.vstack((term_rows, degree_seven_target)))
    return {
        "index": index,
        "seed": seed,
        "weights": list(weights),
        "degree_six_rank": d6_rank,
        "degree_six_target_increment": d6_augmented - d6_rank,
        "degree_seven_rank": d7_rank,
        "degree_seven_target_increment": d7_augmented - d7_rank,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    if args.trials < 1:
        raise ValueError("trials must be positive")
    if args.workers < 1 or args.workers > (base.os.cpu_count() or 1):
        raise ValueError("workers exceed the visible CPU count")
    _, approximate = curve.scan_weight_profiles(args.max_weight)
    weights = [
        item
        for item in approximate
        if curve.exact_curve_rank(item, 3) + curve.exact_curve_rank(item, 4) == 74
    ]
    if not weights:
        raise RuntimeError("no endpoint weight profiles found")
    rng = np.random.default_rng(args.seed)
    evaluations = rng.integers(0, P, size=(base.V_DIM, args.evaluations), dtype=np.int64)
    degree_six_targets, degree_seven_target = base.permanent_targets(evaluations)
    started = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(
                trial,
                index,
                weights[index % len(weights)],
                args.seed + 1_000_003 * index,
                evaluations,
                degree_six_targets,
                degree_seven_target,
            )
            for index in range(args.trials)
        ]
        rows = [future.result() for future in concurrent.futures.as_completed(futures)]
    rows.sort(key=lambda row: (row["degree_six_target_increment"], row["index"]))
    d6_histogram = Counter(int(row["degree_six_target_increment"]) for row in rows)
    d7_histogram = Counter(int(row["degree_seven_target_increment"]) for row in rows)
    elapsed = time.perf_counter() - started
    return {
        "schema_version": 1,
        "status": "BOUNDED_GL_STRESS_TEST_NOT_A_RANK_PROOF",
        "field": f"F_{P}",
        "seed": args.seed,
        "max_weight": args.max_weight,
        "endpoint_weight_profile_count": len(weights),
        "trial_count": args.trials,
        "workers": args.workers,
        "evaluation_columns": args.evaluations,
        "elapsed_seconds": elapsed,
        "degree_six_increment_histogram": dict(sorted(d6_histogram.items())),
        "degree_seven_increment_histogram": dict(sorted(d7_histogram.items())),
        "minimum_degree_six_target_increment": int(rows[0]["degree_six_target_increment"]),
        "best_examples": rows[:20],
        "claim_boundary": [
            "Each trial independently changes the seven off-diagonal six-block coordinates.",
            "A positive target increment excludes only that displayed finite-field packet.",
            "The experiment does not quantify over GL(6)^7 or arbitrary graph complements.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--max-weight", type=int, default=24)
    parser.add_argument("--evaluations", type=int, default=400)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
