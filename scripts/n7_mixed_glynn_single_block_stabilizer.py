#!/usr/bin/env python3
"""Exhaust one signed-coordinate transform in the mixed Glynn packet.

Six graph blocks remain synchronized.  The seventh runs over all
``6! * 2^6 = 46,080`` signed permutations.  Each candidate is tested by exact
modular ranks of at most 392 rows and 400 deterministic evaluation columns.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import multiprocessing
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_equality_packet_crossdegree_search as base  # noqa: E402
import n7_mixed_glynn_graph_search as directed  # noqa: E402


P = base.PRIME
N = base.N
TRANSFORM_COUNT = 46_080
PERMUTATIONS = tuple(itertools.permutations(range(6)))
_FIXED_ROWS: np.ndarray | None = None
_TARGET_ROWS: np.ndarray | None = None
_TAILS: np.ndarray | None = None
_A_BLOCKS: np.ndarray | None = None
_W_VALUES: np.ndarray | None = None


def initialize_worker(
    fixed_rows: np.ndarray,
    target_rows: np.ndarray,
    tails: np.ndarray,
    a_blocks: np.ndarray,
    w_values: np.ndarray,
) -> None:
    global _FIXED_ROWS, _TARGET_ROWS, _TAILS, _A_BLOCKS, _W_VALUES
    _FIXED_ROWS = fixed_rows
    _TARGET_ROWS = target_rows
    _TAILS = tails
    _A_BLOCKS = a_blocks
    _W_VALUES = w_values


def transform_from_index(index: int) -> tuple[np.ndarray, np.ndarray]:
    sign_index, permutation_index = divmod(index, 720)
    permutation = np.asarray(PERMUTATIONS[permutation_index], dtype=np.int64)
    signs = np.asarray(
        [1 if (sign_index >> bit) & 1 else -1 for bit in range(6)],
        dtype=np.int64,
    )
    return permutation, signs


def graph_derivative_rows(permutation: np.ndarray, signs: np.ndarray) -> np.ndarray:
    assert _TAILS is not None and _A_BLOCKS is not None and _W_VALUES is not None
    rows = []
    for tail in _TAILS:
        factor_values = []
        for block in range(N):
            coefficients = tail if block else tail[permutation] * signs
            factor_values.append(
                (_W_VALUES[block] + coefficients @ _A_BLOCKS[block]) % P
            )
        rows.extend(base.omitted_products(np.asarray(factor_values, dtype=np.int64)))
    return np.asarray(rows, dtype=np.int64)


def trial(index: int) -> dict[str, int]:
    assert _FIXED_ROWS is not None and _TARGET_ROWS is not None
    permutation, signs = transform_from_index(index)
    derivative_rows = np.vstack(
        (_FIXED_ROWS, graph_derivative_rows(permutation, signs))
    )
    rank = base.modular_rank(derivative_rows)
    augmented_rank = base.modular_rank(np.vstack((derivative_rows, _TARGET_ROWS)))
    return {
        "index": index,
        "degree_six_rank": rank,
        "degree_six_target_intersection": rank + 49 - augmented_rank,
    }


def input_data(seed: int, evaluation_columns: int):
    rng = np.random.default_rng(seed)
    evaluations = rng.integers(
        0, P, size=(base.V_DIM, evaluation_columns), dtype=np.int64
    )
    degree_six_targets, _ = base.permanent_targets(evaluations)
    a_indices = [row * N + column for row in range(N) for column in range(1, N)]
    w_indices = [row * N for row in range(N)]
    a_blocks = evaluations[a_indices].reshape((N, 6, evaluation_columns))
    w_values = evaluations[w_indices]
    fixed_rows = []
    for block in range(N):
        basis = a_blocks[block]
        fixed_rows.extend(base.omitted_products(np.vstack((basis, basis[0]))))
    tails = np.asarray(directed.tail_dictionary(0), dtype=np.int64)
    return (
        np.asarray(fixed_rows, dtype=np.int64),
        degree_six_targets,
        tails,
        a_blocks,
        w_values,
    )


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    data = input_data(args.seed, args.evaluation_columns)
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers,
        mp_context=context,
        initializer=initialize_worker,
        initargs=data,
    ) as pool:
        rows = list(pool.map(trial, range(TRANSFORM_COUNT), chunksize=args.chunksize))
    rows.sort(key=lambda row: (-row["degree_six_target_intersection"], row["index"]))
    histogram = Counter(row["degree_six_target_intersection"] for row in rows)
    maximizers = [
        row for row in rows if row["degree_six_target_intersection"] == rows[0]["degree_six_target_intersection"]
    ]
    return {
        "schema_version": 1,
        "status": "EXHAUSTIVE_SINGLE_BLOCK_SIGNED_COORDINATE_SEARCH",
        "field": f"F_{P}",
        "seed": args.seed,
        "evaluation_columns": args.evaluation_columns,
        "candidate_formula": "6! * 2^6",
        "candidate_count": TRANSFORM_COUNT,
        "workers": args.workers,
        "intersection_histogram": dict(sorted(histogram.items())),
        "maximum_target_intersection": rows[0]["degree_six_target_intersection"],
        "maximizer_count": len(maximizers),
        "maximizers": maximizers[:100],
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "Exactly one of the seven graph blocks is transformed.",
            "The transform group is signed coordinate permutations, not GL(6).",
            "This finite-field exhaustion is not a general lower-fifty proof.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=8)
    parser.add_argument("--seed", type=int, default=97_531)
    parser.add_argument("--evaluation-columns", type=int, default=400)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    if args.json is None and args.verify_json is None:
        parser.error("one of --json or --verify-json is required")
    payload = build_payload(args)
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        replay_semantics = dict(payload)
        frozen_semantics = dict(frozen)
        replay_semantics.pop("elapsed_seconds", None)
        frozen_semantics.pop("elapsed_seconds", None)
        if replay_semantics != frozen_semantics:
            raise SystemExit("frozen payload mismatch")
        print("PASS frozen payload")
    print(json.dumps({
        "maximum": payload["maximum_target_intersection"],
        "maximizer_count": payload["maximizer_count"],
        "elapsed_seconds": payload["elapsed_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
