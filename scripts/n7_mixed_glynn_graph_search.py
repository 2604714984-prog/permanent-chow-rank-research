#!/usr/bin/env python3
"""Directed signed-permutation search around the mixed Glynn32 graph packet."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
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


P = base.PRIME
N = base.N


def tail_dictionary(extra_offset: int) -> list[tuple[int, ...]]:
    normalized = [(1, *tail) for tail in itertools.product((-1, 1), repeat=5)]
    negative = [(-1, *tail) for tail in itertools.product((-1, 1), repeat=5)]
    extras = [negative[(extra_offset + index) % len(negative)] for index in range(10)]
    return normalized + extras


def signed_permutations(seed: int) -> list[tuple[np.ndarray, np.ndarray]]:
    rng = random.Random(seed)
    transforms = []
    for _ in range(N):
        permutation = np.asarray(rng.sample(range(6), 6), dtype=np.int64)
        signs = np.asarray([rng.choice((-1, 1)) for _ in range(6)], dtype=np.int64)
        transforms.append((permutation, signs))
    return transforms


def packet_values(seed: int, evaluations: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    rng = random.Random(seed)
    tails = tail_dictionary(rng.randrange(32))
    transforms = signed_permutations(seed + 17)
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

    for raw_tail in tails:
        tail = np.asarray(raw_tail, dtype=np.int64)
        graph = np.zeros((42, N), dtype=np.int64)
        for row, (permutation, signs) in enumerate(transforms):
            transformed = tail[permutation] * signs % P
            graph[6 * row : 6 * (row + 1), row] = transformed
        factors = (graph.T @ a_values + w_values) % P
        derivative_rows.extend(base.omitted_products(factors))
        term_rows.append(base.modular_product_rows(factors))
    return np.asarray(derivative_rows), np.asarray(term_rows)


def trial(
    index: int,
    seed: int,
    evaluations: np.ndarray,
    degree_six_targets: np.ndarray,
    degree_seven_target: np.ndarray,
) -> dict[str, int]:
    derivative_rows, term_rows = packet_values(seed, evaluations)
    d6_rank = base.modular_rank(derivative_rows)
    d6_augmented = base.modular_rank(np.vstack((derivative_rows, degree_six_targets)))
    d7_rank = base.modular_rank(term_rows)
    d7_augmented = base.modular_rank(np.vstack((term_rows, degree_seven_target)))
    increment = d6_augmented - d6_rank
    return {
        "index": index,
        "seed": seed,
        "degree_six_rank": d6_rank,
        "degree_six_target_increment": increment,
        "degree_six_target_intersection": 49 - increment,
        "degree_seven_rank": d7_rank,
        "degree_seven_target_increment": d7_augmented - d7_rank,
    }


def identity_control(
    evaluations: np.ndarray,
    degree_six_targets: np.ndarray,
    degree_seven_target: np.ndarray,
) -> dict[str, int]:
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
    for tail in tail_dictionary(0):
        graph = np.zeros((42, N), dtype=np.int64)
        for row in range(N):
            graph[6 * row : 6 * (row + 1), row] = np.asarray(tail) % P
        factors = (graph.T @ a_values + w_values) % P
        derivative_rows.extend(base.omitted_products(factors))
        term_rows.append(base.modular_product_rows(factors))
    derivative_rows = np.asarray(derivative_rows)
    term_rows = np.asarray(term_rows)
    d6_rank = base.modular_rank(derivative_rows)
    d6_augmented = base.modular_rank(np.vstack((derivative_rows, degree_six_targets)))
    d7_rank = base.modular_rank(term_rows)
    d7_augmented = base.modular_rank(np.vstack((term_rows, degree_seven_target)))
    return {
        "degree_six_rank": d6_rank,
        "degree_six_target_increment": d6_augmented - d6_rank,
        "degree_six_target_intersection": 49 - (d6_augmented - d6_rank),
        "degree_seven_rank": d7_rank,
        "degree_seven_target_increment": d7_augmented - d7_rank,
    }


def run(args: argparse.Namespace) -> dict[str, object]:
    if args.trials < 1:
        raise ValueError("trials must be positive")
    if args.workers < 1 or args.workers > (base.os.cpu_count() or 1):
        raise ValueError("workers exceed the visible CPU count")
    rng = np.random.default_rng(args.seed)
    evaluations = rng.integers(0, P, size=(base.V_DIM, args.evaluations), dtype=np.int64)
    degree_six_targets, degree_seven_target = base.permanent_targets(evaluations)
    control = identity_control(evaluations, degree_six_targets, degree_seven_target)
    started = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(
                trial,
                index,
                args.seed + 1_000_003 * index,
                evaluations,
                degree_six_targets,
                degree_seven_target,
            )
            for index in range(args.trials)
        ]
        rows = [future.result() for future in concurrent.futures.as_completed(futures)]
    rows.sort(key=lambda row: (-row["degree_six_target_intersection"], row["index"]))
    histogram = Counter(row["degree_six_target_intersection"] for row in rows)
    elapsed = time.perf_counter() - started
    return {
        "schema_version": 1,
        "status": "DIRECTED_GLYNN_GRAPH_SEARCH_NOT_A_RANK_PROOF",
        "field": f"F_{P}",
        "seed": args.seed,
        "trial_count": args.trials,
        "workers": args.workers,
        "evaluation_columns": args.evaluations,
        "identity_control": control,
        "degree_six_intersection_histogram": dict(sorted(histogram.items())),
        "maximum_degree_six_target_intersection": rows[0]["degree_six_target_intersection"],
        "best_examples": rows[:20],
        "elapsed_seconds": elapsed,
        "claim_boundary": [
            "The complete normalized 32-point Glynn tail dictionary is present in every trial.",
            "The search varies only seven independent signed coordinate permutations and ten extras.",
            "The result is a finite-field subfamily diagnostic and not a lower-fifty proof.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=100)
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
