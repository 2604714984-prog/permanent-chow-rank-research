#!/usr/bin/env python3
"""Exhaust local two-type signed-coordinate mixed-Glynn packets."""

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
import n7_mixed_glynn_single_block_stabilizer as single  # noqa: E402


GROUP_ORDER = 46_080
IDENTITY_INDEX = 63 * 720
CANDIDATE_COUNT = 5 * (GROUP_ORDER - 1)
_TAILS: np.ndarray | None = None
_A_BLOCKS: np.ndarray | None = None
_W_VALUES: np.ndarray | None = None
_TARGET_ROWS: np.ndarray | None = None


def initialize_worker(tails, a_blocks, w_values, target_rows) -> None:
    global _TAILS, _A_BLOCKS, _W_VALUES, _TARGET_ROWS
    _TAILS = tails
    _A_BLOCKS = a_blocks
    _W_VALUES = w_values
    _TARGET_ROWS = target_rows


def decode_candidate(index: int) -> tuple[int, int]:
    if index < 0 or index >= CANDIDATE_COUNT:
        raise ValueError("candidate index out of range")
    raw_transform, remainder = divmod(index, 5)
    transform_index = raw_transform if raw_transform < IDENTITY_INDEX else raw_transform + 1
    return transform_index, remainder + 1


def local_rows(transform_index: int, identity_count: int) -> np.ndarray:
    assert _TAILS is not None and _A_BLOCKS is not None and _W_VALUES is not None
    permutation, signs = single.transform_from_index(transform_index)
    coefficients = []
    for block in range(6):
        if block < identity_count:
            coefficients.append(_TAILS)
        else:
            coefficients.append(_TAILS[:, permutation] * signs)
    rows = []
    for tail_index in range(len(_TAILS)):
        product = np.ones(_W_VALUES.shape[1], dtype=np.int64)
        for block in range(6):
            factor = (
                _W_VALUES[block]
                + coefficients[block][tail_index] @ _A_BLOCKS[block]
            ) % base.PRIME
            product = product * factor % base.PRIME
        rows.append(product)
    return np.asarray(rows, dtype=np.int64)


def trial(index: int):
    assert _TARGET_ROWS is not None
    transform_index, identity_count = decode_candidate(index)
    rows = local_rows(transform_index, identity_count)
    rank = base.modular_rank(rows)
    augmented = base.modular_rank(np.vstack((rows, _TARGET_ROWS)))
    return index, rank, rank + 7 - augmented


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    _, targets, tails, a_blocks, w_values = single.input_data(
        args.seed, args.evaluation_columns
    )
    initargs = (tails, a_blocks, w_values, targets[42:49])
    histogram: Counter[int] = Counter()
    rank_histogram: Counter[int] = Counter()
    maximum = -1
    maximizers = []
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers,
        mp_context=context,
        initializer=initialize_worker,
        initargs=initargs,
    ) as pool:
        for index, rank, intersection in pool.map(
            trial, range(CANDIDATE_COUNT), chunksize=args.chunksize
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
        "status": "EXHAUSTIVE_LOCAL_TWO_MONOMIAL_TYPE_SEARCH",
        "field": f"F_{base.PRIME}",
        "seed": args.seed,
        "evaluation_columns": args.evaluation_columns,
        "signed_permutation_group_order": GROUP_ORDER,
        "normalized_identity_index": IDENTITY_INDEX,
        "candidate_formula": "5 * (6! * 2^6 - 1)",
        "candidate_count": CANDIDATE_COUNT,
        "workers": args.workers,
        "local_derivative_rank_histogram": dict(sorted(rank_histogram.items())),
        "local_target_intersection_histogram": dict(sorted(histogram.items())),
        "maximum_local_target_intersection": maximum,
        "maximizer_count": histogram[maximum],
        "maximizer_indices_first_100": maximizers,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "A common signed coordinate permutation is normalized to the identity.",
            "Every local packet with exactly two signed-coordinate types is covered, for all five positive multiplicity splits.",
            "Packets with three or more monomial types and general GL(6) transforms remain open.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=240_000)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=128)
    parser.add_argument("--seed", type=int, default=97_531)
    parser.add_argument("--evaluation-columns", type=int, default=64)
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
