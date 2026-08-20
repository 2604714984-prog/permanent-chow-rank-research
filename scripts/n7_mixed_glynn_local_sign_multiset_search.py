#!/usr/bin/env python3
"""Exhaust normalized six-block sign multisets in one omitted-row block."""

from __future__ import annotations

import argparse
import concurrent.futures
import itertools
import json
import math
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
import n7_mixed_glynn_two_type_sign_search as two_type  # noqa: E402


_TAILS: np.ndarray | None = None
_A_BLOCKS: np.ndarray | None = None
_W_VALUES: np.ndarray | None = None
_TARGET_ROWS: np.ndarray | None = None
_TYPE_COUNT = 0
_COMPOSITIONS: tuple[tuple[int, ...], ...] = ()


def positive_compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    rows = []
    for cuts in itertools.combinations(range(1, total), parts - 1):
        endpoints = (0, *cuts, total)
        rows.append(tuple(endpoints[i + 1] - endpoints[i] for i in range(parts)))
    return tuple(rows)


def unrank_combination(n: int, size: int, index: int) -> tuple[int, ...]:
    if index < 0 or index >= math.comb(n, size):
        raise ValueError("combination rank is outside the valid range")
    result = []
    start = 0
    for position in range(size):
        remaining = size - position - 1
        for value in range(start, n):
            count = math.comb(n - value - 1, remaining) if remaining else 1
            if index < count:
                result.append(value)
                start = value + 1
                break
            index -= count
    return tuple(result)


def initialize_worker(
    tails: np.ndarray,
    a_blocks: np.ndarray,
    w_values: np.ndarray,
    target_rows: np.ndarray,
    type_count: int,
) -> None:
    global _TAILS, _A_BLOCKS, _W_VALUES, _TARGET_ROWS, _TYPE_COUNT, _COMPOSITIONS
    _TAILS = tails
    _A_BLOCKS = a_blocks
    _W_VALUES = w_values
    _TARGET_ROWS = target_rows
    _TYPE_COUNT = type_count
    _COMPOSITIONS = positive_compositions(6, type_count)


def decode_candidate(index: int, type_count: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    compositions = positive_compositions(6, type_count)
    combination_rank, composition_index = divmod(index, len(compositions))
    nonidentity = unrank_combination(63, type_count - 1, combination_rank)
    return (63, *nonidentity), compositions[composition_index]


def local_rows(digits: tuple[int, ...], counts: tuple[int, ...]) -> np.ndarray:
    assert _TAILS is not None and _A_BLOCKS is not None and _W_VALUES is not None
    signs = []
    for digit, count in zip(digits, counts):
        signs.extend([two_type.sign_vector(digit)] * count)
    if len(signs) != 6:
        raise AssertionError(len(signs))
    rows = []
    for tail in _TAILS:
        product = np.ones(_W_VALUES.shape[1], dtype=np.int64)
        for block, sign in enumerate(signs):
            factor = (_W_VALUES[block] + (tail * sign) @ _A_BLOCKS[block]) % base.PRIME
            product = product * factor % base.PRIME
        rows.append(product)
    return np.asarray(rows, dtype=np.int64)


def trial(index: int):
    assert _TARGET_ROWS is not None
    digits, counts = decode_candidate(index, _TYPE_COUNT)
    rows = local_rows(digits, counts)
    rank = base.modular_rank(rows)
    augmented = base.modular_rank(np.vstack((rows, _TARGET_ROWS)))
    return index, rank, rank + 7 - augmented


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if args.type_count < 1 or args.type_count > 6:
        raise ValueError("type_count must lie in [1, 6]")
    composition_count = math.comb(5, args.type_count - 1)
    combination_count = math.comb(63, args.type_count - 1)
    candidate_count = composition_count * combination_count
    if candidate_count > args.max_candidates:
        raise ValueError(
            f"candidate count {candidate_count} exceeds --max-candidates {args.max_candidates}"
        )
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    _, degree_six_targets, tails, a_blocks, w_values = single.input_data(
        args.seed, args.evaluation_columns
    )
    target_rows = degree_six_targets[6 * 7 : 7 * 7]
    initargs = (tails, a_blocks, w_values, target_rows, args.type_count)
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
        "status": "EXHAUSTIVE_NORMALIZED_LOCAL_SIGN_MULTISET_SEARCH",
        "field": f"F_{base.PRIME}",
        "seed": args.seed,
        "evaluation_columns": args.evaluation_columns,
        "type_count": args.type_count,
        "normalization": "one marked sign type is normalized to digit 63",
        "combination_count": combination_count,
        "composition_count": composition_count,
        "candidate_formula": f"binom(63,{args.type_count - 1}) * binom(5,{args.type_count - 1})",
        "candidate_count": candidate_count,
        "workers": args.workers,
        "local_derivative_rank_histogram": dict(sorted(rank_histogram.items())),
        "local_target_intersection_histogram": dict(sorted(histogram.items())),
        "maximum_local_target_intersection": maximum,
        "maximizer_count": histogram[maximum],
        "maximizer_indices_first_100": maximizers,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The target and graph derivatives are restricted to one fixed omitted-row multidegree block.",
            "Common sign multiplication and row-block permutation justify the normalized marked multisets.",
            "The modular full-rank minors lift the zero-intersection conclusions to characteristic zero.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type-count", type=int, required=True)
    parser.add_argument("--max-candidates", type=int, default=8_000_000)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=64)
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


if __name__ == "__main__":
    main()
