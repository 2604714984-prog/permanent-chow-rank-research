#!/usr/bin/env python3
"""Exhaust normalized mixed-Glynn packets with exactly three sign types."""

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
import n7_mixed_glynn_multiblock_sign_search as multi  # noqa: E402
import n7_mixed_glynn_single_block_stabilizer as single  # noqa: E402
import n7_mixed_glynn_two_type_sign_search as two_type  # noqa: E402


_FIXED_ROWS: np.ndarray | None = None
_TARGET_ROWS: np.ndarray | None = None


def candidate_rows() -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for second in range(63):
        for third in range(second + 1, 63):
            for identity_count in range(1, 6):
                for second_count in range(1, 7 - identity_count):
                    third_count = 7 - identity_count - second_count
                    if third_count >= 1:
                        rows.append(
                            (
                                second,
                                third,
                                identity_count,
                                second_count,
                                third_count,
                            )
                        )
    result = tuple(rows)
    if len(result) != (63 * 62 // 2) * 15:
        raise AssertionError(len(result))
    return result


def initialize_worker(*data) -> None:
    global _FIXED_ROWS, _TARGET_ROWS
    fixed_rows, target_rows, tails, a_blocks, w_values = data
    _FIXED_ROWS = fixed_rows
    _TARGET_ROWS = target_rows
    multi.initialize_worker(fixed_rows, target_rows, tails, a_blocks, w_values, 0)


def trial(candidate: tuple[int, int, int, int, int]):
    assert _FIXED_ROWS is not None and _TARGET_ROWS is not None
    second, third, identity_count, second_count, third_count = candidate
    signs = np.asarray(
        [two_type.sign_vector(63)] * identity_count
        + [two_type.sign_vector(second)] * second_count
        + [two_type.sign_vector(third)] * third_count
    )
    derivative_rows = np.vstack((_FIXED_ROWS, multi.graph_derivative_rows(signs)))
    rank = base.modular_rank(derivative_rows)
    augmented_rank = base.modular_rank(np.vstack((derivative_rows, _TARGET_ROWS)))
    return candidate, rank, rank + 49 - augmented_rank


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    candidates = candidate_rows()
    if len(candidates) > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    data = single.input_data(args.seed, args.evaluation_columns)
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
        initargs=data,
    ) as pool:
        for candidate, rank, intersection in pool.map(
            trial, candidates, chunksize=args.chunksize
        ):
            histogram[intersection] += 1
            rank_histogram[rank] += 1
            if intersection > maximum:
                maximum = intersection
                maximizers = [candidate]
            elif intersection == maximum and len(maximizers) < 100:
                maximizers.append(candidate)
    return {
        "schema_version": 1,
        "status": "EXHAUSTIVE_NORMALIZED_THREE_SIGN_TYPE_PACKET_SEARCH",
        "field": f"F_{base.PRIME}",
        "seed": args.seed,
        "evaluation_columns": args.evaluation_columns,
        "normalization": "the first sign type is the all-positive digit 63",
        "candidate_formula": "binom(63, 2) * binom(6, 2)",
        "candidate_count": len(candidates),
        "workers": args.workers,
        "degree_six_rank_histogram": dict(sorted(rank_histogram.items())),
        "intersection_histogram": dict(sorted(histogram.items())),
        "maximum_target_intersection": maximum,
        "maximizer_count": histogram[maximum],
        "maximizers_first_100": [list(row) for row in maximizers],
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "A common sign change on all seven graph blocks is normalized away.",
            "Every packet with exactly three diagonal sign types is represented up to row-block permutation.",
            "Coordinate permutations, four or more sign types, and general GL(6) changes remain outside the family.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=30_000)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=16)
    parser.add_argument("--seed", type=int, default=97_531)
    parser.add_argument("--evaluation-columns", type=int, default=400)
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
