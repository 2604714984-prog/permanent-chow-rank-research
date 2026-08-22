#!/usr/bin/env python3
"""Bounded exact mixed-catalectic obstruction for column-uniform N=49 packets.

For a column-uniform term indexed by ``a in k^7``, the squarefree-row
3/4 catalectic block is ``v_3(a) v_4(a)^T``.  A decomposition of the
permanent therefore requires a coefficient vector whose weighted sum is the
35 by 35 complementary-subset pairing matrix.  This script tests that exact
1225-equation linear system over a finite field.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
from flint import nmod_mat


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_equality_packet_crossdegree_search as base  # noqa: E402


PRIME = base.PRIME
N = base.N
TRIPLES = tuple(itertools.combinations(range(N), 3))
QUADS = tuple(itertools.combinations(range(N), 4))
PAIR_ROWS = tuple((left, right) for left in TRIPLES for right in QUADS)
TARGET = np.asarray(
    [1 if set(left).isdisjoint(right) else 0 for left, right in PAIR_ROWS],
    dtype=np.int64,
)


def squarefree_values(points: np.ndarray, subsets: tuple[tuple[int, ...], ...]) -> np.ndarray:
    values = np.ones((len(subsets), len(points)), dtype=np.int64)
    for row, subset in enumerate(subsets):
        for coordinate in subset:
            values[row] = values[row] * points[:, coordinate] % PRIME
    return values


def coefficient_matrix(points: np.ndarray) -> np.ndarray:
    ev3 = squarefree_values(points, TRIPLES)
    ev4 = squarefree_values(points, QUADS)
    # Column t is vec(v_3(a_t) v_4(a_t)^T), preserving the pair-row order.
    return (ev3[:, None, :] * ev4[None, :, :] % PRIME).reshape(1225, len(points))


def modular_rank(matrix: np.ndarray) -> int:
    return nmod_mat((np.asarray(matrix, dtype=np.int64) % PRIME).tolist(), PRIME).rank()


def trial(seed: int, line_count: int) -> dict[str, int]:
    points = base.packet_a_points(seed, line_count)
    matrix = coefficient_matrix(points)
    rank = modular_rank(matrix)
    augmented = modular_rank(np.column_stack((matrix, TARGET)))
    return {
        "seed": seed,
        "forced_line_count": line_count,
        "coefficient_rank": rank,
        "augmented_rank": augmented,
        "target_increment": augmented - rank,
        "equation_count": int(matrix.shape[0]),
        "unknown_count": int(matrix.shape[1]),
    }


def glynn_points() -> np.ndarray:
    return np.asarray(
        [(1, *tail) for tail in itertools.product((-1, 1), repeat=N - 1)],
        dtype=np.int64,
    ) % PRIME


def glynn_control() -> dict[str, int]:
    points = glynn_points()
    matrix = coefficient_matrix(points)
    rank = modular_rank(matrix)
    augmented = modular_rank(np.column_stack((matrix, TARGET)))
    return {
        "point_count": len(points),
        "coefficient_rank": rank,
        "augmented_rank": augmented,
        "target_increment": augmented - rank,
    }


def auto_workers() -> int:
    return max(1, (os.cpu_count() or 1) - 4)


def run(args: argparse.Namespace) -> dict[str, object]:
    workers = auto_workers() if args.workers == "auto" else int(args.workers)
    if workers < 1 or workers > auto_workers():
        raise SystemExit(f"workers must be in 1..{auto_workers()}; four logical CPUs stay free")
    jobs = [
        (args.seed + 100000 * line_count + index, line_count)
        for line_count in (2, 3, 7)
        for index in range(args.candidates)
    ]
    started = time.perf_counter()
    results: list[dict[str, int]] = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(trial, seed, line_count) for seed, line_count in jobs]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda row: (row["forced_line_count"], row["seed"]))
    elapsed = time.perf_counter() - started
    return {
        "schema_version": 1,
        "status": "BOUNDED_FINITE_FIELD_MIXED_CATALECTIC_SEARCH_NOT_A_RANK_CERTIFICATE",
        "field": f"F_{PRIME}",
        "seed": args.seed,
        "workers": workers,
        "logical_cpus_left_free": 4,
        "candidate_count": len(results),
        "matrix_shape": [1225, 49],
        "estimated_peak_memory_gib": 0.6,
        "elapsed_seconds": elapsed,
        "candidates_per_second": len(results) / elapsed if elapsed else None,
        "glynn_64_term_positive_control": glynn_control(),
        "summary_by_forced_line_count": {
            str(line_count): {
                "count": sum(row["forced_line_count"] == line_count for row in results),
                "minimum_coefficient_rank": min(
                    row["coefficient_rank"] for row in results if row["forced_line_count"] == line_count
                ),
                "minimum_target_increment": min(
                    row["target_increment"] for row in results if row["forced_line_count"] == line_count
                ),
                "consistent_count": sum(
                    row["forced_line_count"] == line_count and row["target_increment"] == 0
                    for row in results
                ),
            }
            for line_count in (2, 3, 7)
        },
        "results": results,
        "claim_boundary": [
            "A positive augmented-rank increment rigorously excludes that fixed finite-field column-uniform candidate.",
            "The 64-point Glynn control checks that the encoded mixed-catalectic target and flattening are consistent.",
            "The search covers only the displayed line-packet samples, not the full rank-at-most-47 fifth-Veronese locus.",
            "It proves no ordinary or border Chow-rank bound by itself.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=int, default=8, help="per forced-line family")
    parser.add_argument("--workers", default="auto")
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.candidates < 1:
        raise SystemExit("candidates must be positive")
    payload = run(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
