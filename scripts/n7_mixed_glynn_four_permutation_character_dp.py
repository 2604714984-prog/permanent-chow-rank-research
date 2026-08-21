#!/usr/bin/env python3
"""Conjugacy-reduced Walsh DP for four local permutation types.

The raw normalized family has ``binom(719, 3) * binom(5, 3)`` multisets.
To cover it, choose one of the three nonidentity types as a marked type and
conjugate that type to one of the ten nonidentity cycle types in ``S_6``.
The other two types and the ten positive compositions of six are streamed.
This cover has duplicates, but it cannot omit a normalized four-type packet.
"""

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
import n7_mixed_glynn_permutation_character_dp as character  # noqa: E402
import n7_mixed_glynn_local_sign_multiset_search as local  # noqa: E402


PERMUTATIONS = character.PERMUTATIONS
IDENTITY = character.IDENTITY
COMPOSITIONS = local.positive_compositions(6, 4)


def cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen = set()
    lengths = []
    for start in range(6):
        if start in seen:
            continue
        length = 0
        value = start
        while value not in seen:
            seen.add(value)
            length += 1
            value = permutation[value]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def conjugacy_representatives() -> tuple[tuple[int, tuple[int, ...]], ...]:
    representatives = {}
    for index, permutation in enumerate(PERMUTATIONS):
        kind = cycle_type(permutation)
        if kind != (1, 1, 1, 1, 1, 1):
            representatives.setdefault(kind, (index, permutation))
    return tuple(representatives[kind] for kind in sorted(representatives))


REPRESENTATIVES = conjugacy_representatives()
PAIR_COUNT = math.comb(718, 2)
CANDIDATE_COUNT = len(REPRESENTATIVES) * PAIR_COUNT * len(COMPOSITIONS)


def _actual_nonidentity_index(reduced_index: int, excluded: int) -> int:
    """Map ``range(718)`` to permutation indices excluding 0 and ``excluded``."""
    value = reduced_index + 1
    return value if value < excluded else value + 1


def decode_candidate(index: int):
    if index < 0 or index >= CANDIDATE_COUNT:
        raise ValueError("candidate index out of range")
    cover_index, composition_index = divmod(index, len(COMPOSITIONS))
    representative_index, pair_rank = divmod(cover_index, PAIR_COUNT)
    marked_index, marked = REPRESENTATIVES[representative_index]
    first, second = local.unrank_combination(718, 2, pair_rank)
    other_indices = (
        _actual_nonidentity_index(first, marked_index),
        _actual_nonidentity_index(second, marked_index),
    )
    permutations = (
        IDENTITY,
        marked,
        PERMUTATIONS[other_indices[0]],
        PERMUTATIONS[other_indices[1]],
    )
    return permutations, COMPOSITIONS[composition_index]


def trial(index: int):
    types, counts = decode_candidate(index)
    packet = tuple(
        permutation
        for permutation, count in zip(types, counts)
        for _ in range(count)
    )
    protected = character.protected_characters(packet)
    return index, len(protected), protected


def build_payload(args: argparse.Namespace) -> dict[str, object]:
    stop = CANDIDATE_COUNT if args.stop is None else args.stop
    if args.start < 0 or stop < args.start or stop > CANDIDATE_COUNT:
        raise ValueError("invalid candidate interval")
    count = stop - args.start
    if count > args.max_candidates:
        raise ValueError("candidate interval exceeds --max-candidates")
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
        for index, protected_count, protected in pool.map(
            trial, range(args.start, stop), chunksize=args.chunksize
        ):
            histogram[protected_count] += 1
            if protected_count > maximum:
                maximum = protected_count
                maximizers = [(index, protected)]
            elif protected_count == maximum and len(maximizers) < 100:
                maximizers.append((index, protected))

    complete = args.start == 0 and stop == CANDIDATE_COUNT
    return {
        "schema_version": 1,
        "status": (
            "EXHAUSTIVE_FOUR_PERMUTATION_CHARACTER_COLLISION_DP"
            if complete
            else "DIAGNOSTIC_FOUR_PERMUTATION_CHARACTER_COLLISION_DP"
        ),
        "raw_normalized_candidate_formula": "binom(719, 3) * binom(5, 3)",
        "raw_normalized_candidate_count": math.comb(719, 3) * math.comb(5, 3),
        "cover_candidate_formula": "10 * binom(718, 2) * binom(5, 3)",
        "cover_candidate_count": CANDIDATE_COUNT,
        "candidate_interval": [args.start, stop],
        "workers": args.workers,
        "protected_character_count_histogram": dict(sorted(histogram.items())),
        "maximum_protected_character_count": maximum,
        "maximizers_first_100": [
            {"index": index, "protected_characters": list(protected)}
            for index, protected in maximizers
        ],
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "Common output-coordinate normalization makes one type the identity.",
            "Simultaneous input/output relabelling conjugates all relative permutations without changing protected-character existence.",
            "Marking any nonidentity type and reducing it to one of the ten nonidentity cycle types covers every four-type packet, with harmless duplicates.",
            "A zero protected-character count on the complete cover proves zero local target intersection independently of signs.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--max-candidates", type=int, default=CANDIDATE_COUNT)
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
