#!/usr/bin/env python3
"""Exhaust independent sign changes on several mixed-Glynn graph blocks."""

from __future__ import annotations

import argparse
import concurrent.futures
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
import n7_mixed_glynn_single_block_stabilizer as single  # noqa: E402


P = base.PRIME
N = base.N
_FIXED_ROWS: np.ndarray | None = None
_TARGET_ROWS: np.ndarray | None = None
_TAILS: np.ndarray | None = None
_A_BLOCKS: np.ndarray | None = None
_W_VALUES: np.ndarray | None = None
_VARYING_BLOCKS = 0


def initialize_worker(
    fixed_rows: np.ndarray,
    target_rows: np.ndarray,
    tails: np.ndarray,
    a_blocks: np.ndarray,
    w_values: np.ndarray,
    varying_blocks: int,
) -> None:
    global _FIXED_ROWS, _TARGET_ROWS, _TAILS, _A_BLOCKS, _W_VALUES
    global _VARYING_BLOCKS
    _FIXED_ROWS = fixed_rows
    _TARGET_ROWS = target_rows
    _TAILS = tails
    _A_BLOCKS = a_blocks
    _W_VALUES = w_values
    _VARYING_BLOCKS = varying_blocks


def signs_from_index(index: int, varying_blocks: int) -> np.ndarray:
    signs = np.ones((N, 6), dtype=np.int64)
    for block in range(varying_blocks):
        digit = index & 63
        index >>= 6
        signs[block] = [1 if (digit >> bit) & 1 else -1 for bit in range(6)]
    if index:
        raise ValueError("candidate index exceeds the declared search space")
    return signs


def graph_derivative_rows(signs: np.ndarray) -> np.ndarray:
    assert _TAILS is not None and _A_BLOCKS is not None and _W_VALUES is not None
    rows = []
    for tail in _TAILS:
        factor_values = np.asarray(
            [
                (_W_VALUES[block] + (tail * signs[block]) @ _A_BLOCKS[block]) % P
                for block in range(N)
            ],
            dtype=np.int64,
        )
        rows.extend(base.omitted_products(factor_values))
    return np.asarray(rows, dtype=np.int64)


def trial(index: int) -> tuple[int, int, int]:
    assert _FIXED_ROWS is not None and _TARGET_ROWS is not None
    signs = signs_from_index(index, _VARYING_BLOCKS)
    derivative_rows = np.vstack((_FIXED_ROWS, graph_derivative_rows(signs)))
    rank = base.modular_rank(derivative_rows)
    augmented_rank = base.modular_rank(np.vstack((derivative_rows, _TARGET_ROWS)))
    intersection = rank + 49 - augmented_rank
    return index, rank, intersection


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if args.varying_blocks < 1 or args.varying_blocks > N:
        raise ValueError("varying_blocks must lie in [1, 7]")
    candidate_count = 64**args.varying_blocks
    if candidate_count > args.max_candidates:
        raise ValueError(
            f"candidate count {candidate_count} exceeds --max-candidates {args.max_candidates}"
        )
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    fixed_rows, target_rows, tails, a_blocks, w_values = single.input_data(
        args.seed, args.evaluation_columns
    )
    initargs = (
        fixed_rows,
        target_rows,
        tails,
        a_blocks,
        w_values,
        args.varying_blocks,
    )
    histogram: Counter[int] = Counter()
    rank_histogram: Counter[int] = Counter()
    maximum = -1
    maximizers: list[int] = []
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers,
        mp_context=context,
        initializer=initialize_worker,
        initargs=initargs,
    ) as pool:
        for index, rank, intersection in pool.map(
            trial, range(candidate_count), chunksize=args.chunksize
        ):
            histogram[intersection] += 1
            rank_histogram[rank] += 1
            if intersection > maximum:
                maximum = intersection
                maximizers = [index]
            elif intersection == maximum and len(maximizers) < 100:
                maximizers.append(index)
    return {
        "schema_version": 1,
        "status": "EXHAUSTIVE_MULTIBLOCK_SIGN_SEARCH",
        "field": f"F_{P}",
        "seed": args.seed,
        "evaluation_columns": args.evaluation_columns,
        "varying_blocks": args.varying_blocks,
        "candidate_formula": f"64^{args.varying_blocks}",
        "candidate_count": candidate_count,
        "workers": args.workers,
        "degree_six_rank_histogram": dict(sorted(rank_histogram.items())),
        "intersection_histogram": dict(sorted(histogram.items())),
        "maximum_target_intersection": maximum,
        "maximizer_count": histogram[maximum],
        "maximizer_indices_first_100": maximizers,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "Only independent diagonal sign changes on the selected graph blocks are varied.",
            "The complete finite family is exhausted, but permutations and general GL(6) changes are not included.",
            "This is an endpoint-family computation and not an ordinary lower-fifty proof.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--varying-blocks", type=int, default=2)
    parser.add_argument("--max-candidates", type=int, default=300_000)
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
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        live_semantics = dict(payload)
        frozen_semantics = dict(frozen)
        for row in (live_semantics, frozen_semantics):
            row.pop("elapsed_seconds", None)
            row.pop("workers", None)
        if live_semantics != frozen_semantics:
            raise SystemExit("frozen payload mismatch")
        print("PASS frozen payload")
    if args.json is None and args.verify_json is None:
        print(text, end="")


if __name__ == "__main__":
    main()
