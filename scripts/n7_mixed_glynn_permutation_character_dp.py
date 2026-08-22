#!/usr/bin/env python3
"""Walsh-character collision DP for three local permutation types."""

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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import n7_mixed_glynn_single_block_stabilizer as single  # noqa: E402
import n7_mixed_glynn_local_sign_multiset_search as local  # noqa: E402


PERMUTATIONS = single.PERMUTATIONS
IDENTITY = tuple(range(6))
COMPOSITIONS = local.positive_compositions(6, 3)
PAIR_COUNT = math.comb(719, 2)
CANDIDATE_COUNT = PAIR_COUNT * len(COMPOSITIONS)


def decode_candidate(index: int):
    if index < 0 or index >= CANDIDATE_COUNT:
        raise ValueError("candidate index out of range")
    pair_rank, composition_index = divmod(index, len(COMPOSITIONS))
    first, second = local.unrank_combination(719, 2, pair_rank)
    return (first + 1, second + 1), COMPOSITIONS[composition_index]


def protected_characters(permutations: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    valid = {(0, 0)}
    invalid: set[int] = set()
    for permutation in permutations:
        labels = (0, *(1 << permutation[index] for index in range(6)))
        next_invalid = {value ^ label for value in invalid for label in labels}
        next_valid = set()
        for value, used_columns in valid:
            for column, label in enumerate(labels):
                image = value ^ label
                if (used_columns >> column) & 1:
                    next_invalid.add(image)
                else:
                    next_valid.add((image, used_columns | (1 << column)))
        valid, invalid = next_valid, next_invalid
    return tuple(sorted({value for value, _ in valid} - invalid))


def trial(index: int):
    (first, second), counts = decode_candidate(index)
    permutations = (
        (IDENTITY,) * counts[0]
        + (PERMUTATIONS[first],) * counts[1]
        + (PERMUTATIONS[second],) * counts[2]
    )
    protected = protected_characters(permutations)
    return index, len(protected), protected


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    if CANDIDATE_COUNT > args.max_candidates:
        raise ValueError("candidate family exceeds --max-candidates")
    if args.workers < 1 or args.workers > (os.cpu_count() or 1):
        raise ValueError("workers exceed visible CPUs")
    histogram: Counter[int] = Counter()
    maximum = -1
    maximizers = []
    started = time.perf_counter()
    context = multiprocessing.get_context("fork") if os.name != "nt" else None
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers, mp_context=context
    ) as pool:
        for index, count, protected in pool.map(
            trial, range(CANDIDATE_COUNT), chunksize=args.chunksize
        ):
            histogram[count] += 1
            if count > maximum:
                maximum = count
                maximizers = [(index, protected)]
            elif count == maximum and len(maximizers) < 100:
                maximizers.append((index, protected))
    return {
        "schema_version": 1,
        "status": "EXHAUSTIVE_THREE_PERMUTATION_CHARACTER_COLLISION_DP",
        "normalized_permutation_count": 719,
        "composition_count": len(COMPOSITIONS),
        "candidate_formula": "binom(719, 2) * binom(5, 2)",
        "candidate_count": CANDIDATE_COUNT,
        "workers": args.workers,
        "protected_character_count_histogram": dict(sorted(histogram.items())),
        "maximum_protected_character_count": maximum,
        "maximizers_first_100": [
            {"index": index, "protected_characters": list(protected)}
            for index, protected in maximizers
        ],
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The DP records whether a Walsh character has a valid distinct-column realization and no repeated-column realization.",
            "Every multiset with exactly three permutation types is represented after common normalization and row permutation.",
            "A zero protected-character count proves zero local target intersection independently of signs.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-candidates", type=int, default=2_600_000)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--chunksize", type=int, default=256)
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
