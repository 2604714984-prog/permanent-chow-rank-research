#!/usr/bin/env python3
"""Exact search over seven-character quotients of the perm_7 ``K_{4,3}`` map."""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import itertools
import json
import math
from pathlib import Path
import random
import time

import numpy as np
from flint import nmod_mat


N = 7
PRIME = 1009
REPLAY_PRIME = 953


def shifted(values: tuple[int, ...], amount: int) -> tuple[int, ...]:
    return tuple(sorted((value + amount) % N for value in values))


def pair_orbits(degree: int):
    subsets = tuple(itertools.combinations(range(N), degree))
    unseen = {(rows, columns) for rows in subsets for columns in subsets}
    representatives = []
    while unseen:
        seed = min(unseen)
        orbit = {
            (shifted(seed[0], row_shift), shifted(seed[1], column_shift))
            for row_shift in range(N)
            for column_shift in range(N)
        }
        if len(orbit) != N * N:
            raise AssertionError((seed, len(orbit)))
        representatives.append(min(orbit))
        unseen.difference_update(orbit)
    representatives.sort()
    return tuple(representatives)


def pair_transport(representatives):
    result = {}
    for orbit_index, (rows, columns) in enumerate(representatives):
        for row_shift in range(N):
            for column_shift in range(N):
                state = shifted(rows, row_shift), shifted(columns, column_shift)
                if state in result:
                    raise AssertionError(state)
                result[state] = orbit_index, row_shift, column_shift
    return result


def primitive_root(prime: int) -> int:
    for candidate in range(2, prime):
        root = pow(candidate, (prime - 1) // N, prime)
        if root != 1 and pow(root, N, prime) == 1:
            return root
    raise AssertionError(prime)


def add_character(first, second):
    return (first[0] + second[0]) % N, (first[1] + second[1]) % N


def subtract_character(first, second):
    return (first[0] - second[0]) % N, (first[1] - second[1]) % N


def wedge_character(characters, wedge):
    result = (0, 0)
    for index in wedge:
        result = add_character(result, characters[index])
    return result


def block_matrix(
    characters,
    total_character,
    source_representatives,
    target_lookup,
    prime,
    root,
):
    source_wedges = tuple(itertools.combinations(range(N), 3))
    target_wedges = tuple(itertools.combinations(range(N), 4))
    target_wedge_index = {value: index for index, value in enumerate(target_wedges)}
    size = len(source_representatives) * len(source_wedges)
    matrix = np.zeros((size, size), dtype=np.int64)
    powers = [pow(root, exponent, prime) for exponent in range(N)]
    for source_orbit, (rows, columns) in enumerate(source_representatives):
        for source_wedge_index, wedge in enumerate(source_wedges):
            column_index = source_orbit * len(source_wedges) + source_wedge_index
            wedge_set = set(wedge)
            source_fourier = subtract_character(
                total_character, wedge_character(characters, wedge)
            )
            for removed_row in rows:
                for removed_column in columns:
                    target_pair = (
                        tuple(value for value in rows if value != removed_row),
                        tuple(value for value in columns if value != removed_column),
                    )
                    target_orbit, row_shift, column_shift = target_lookup[target_pair]
                    for added_index, variable_character in enumerate(characters):
                        if added_index in wedge_set:
                            continue
                        output_wedge = tuple(sorted((*wedge, added_index)))
                        sign = -1 if output_wedge.index(added_index) % 2 else 1
                        target_fourier = subtract_character(
                            source_fourier, variable_character
                        )
                        coefficient_exponent = (
                            variable_character[0] * removed_row
                            + variable_character[1] * removed_column
                            + target_fourier[0] * row_shift
                            + target_fourier[1] * column_shift
                        ) % N
                        row_index = (
                            target_orbit * len(target_wedges)
                            + target_wedge_index[output_wedge]
                        )
                        matrix[row_index, column_index] += sign * powers[
                            coefficient_exponent
                        ]
    return matrix % prime


def quotient_rank(characters, prime, source_representatives, target_lookup):
    root = primitive_root(prime)
    block_ranks = []
    for total_character in itertools.product(range(N), repeat=2):
        matrix = block_matrix(
            characters,
            total_character,
            source_representatives,
            target_lookup,
            prime,
            root,
        )
        block_ranks.append(int(nmod_mat(matrix.tolist(), prime).rank()))
    return sum(block_ranks), block_ranks, root


def candidate_task(task):
    index, selected, prime = task
    source_representatives = pair_orbits(4)
    target_lookup = pair_transport(pair_orbits(3))
    rank, block_ranks, root = quotient_rank(
        selected, prime, source_representatives, target_lookup
    )
    return {
        "candidate_index": index,
        "characters": [list(value) for value in selected],
        "prime": prime,
        "primitive_seventh_root": root,
        "total_rank": rank,
        "minimum_block_rank": min(block_ranks),
        "maximum_block_rank": max(block_ranks),
    }


def build_payload(args):
    source_representatives = pair_orbits(4)
    target_representatives = pair_orbits(3)
    assert len(source_representatives) == len(target_representatives) == 25
    target_lookup = pair_transport(target_representatives)
    row_line = tuple((value, 0) for value in range(N))
    diagonal_line = tuple((value, value) for value in range(N))
    started = time.perf_counter()
    row_rank, row_blocks, _ = quotient_rank(
        row_line, PRIME, source_representatives, target_lookup
    )
    diagonal_rank, diagonal_blocks, _ = quotient_rank(
        diagonal_line, PRIME, source_representatives, target_lookup
    )
    if row_rank != 29_120 or diagonal_rank != 33_920:
        raise AssertionError((row_rank, diagonal_rank))
    rng = random.Random(args.seed)
    all_characters = tuple(itertools.product(range(N), repeat=2))
    tasks = []
    for index in range(args.candidates):
        selected = tuple(sorted(rng.sample(all_characters, N)))
        tasks.append((index, selected, PRIME))
    if args.workers == 1:
        candidates = [candidate_task(task) for task in tasks]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            candidates = list(pool.map(candidate_task, tasks))
    candidates.sort(key=lambda row: row["candidate_index"])
    best = max(candidates, key=lambda row: row["total_rank"])
    best_characters = tuple(tuple(value) for value in best["characters"])
    replay_rank, replay_blocks, replay_root = quotient_rank(
        best_characters, REPLAY_PRIME, source_representatives, target_lookup
    )
    threshold = 49 * 832
    return {
        "schema_version": 1,
        "status": "EXACT_SEVEN_CHARACTER_QUOTIENT_SEARCH",
        "n": N,
        "output_degree": 4,
        "wedge_degree": 3,
        "candidate_count_checked_before_search": args.candidates,
        "seed": args.seed,
        "workers": args.workers,
        "fourier_block_count": N * N,
        "fourier_block_shape": [875, 875],
        "controls": {
            "row_character_line_total_rank": row_rank,
            "row_character_line_block_ranks": row_blocks,
            "diagonal_character_line_total_rank": diagonal_rank,
            "diagonal_character_line_block_ranks": diagonal_blocks,
        },
        "candidates": candidates,
        "best_candidate": best,
        "best_candidate_replay": {
            "prime": REPLAY_PRIME,
            "primitive_seventh_root": replay_root,
            "total_rank": replay_rank,
            "minimum_block_rank": min(replay_blocks),
            "maximum_block_rank": max(replay_blocks),
            "matches_search_prime": replay_rank == best["total_rank"],
        },
        "one_term_rank_cap": 832,
        "rank_49_threshold": threshold,
        "strictly_exceeds_49_terms": min(best["total_rank"], replay_rank) > threshold,
        "flattening_lower_bound": math.ceil(
            min(best["total_rank"], replay_rank) / 832
        ),
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The search ranges over the displayed finite sample of seven-character quotients.",
            "A modular minor that survives both split primes lifts over the seventh cyclotomic field.",
            "The resulting Koszul inequality concerns ordinary Chow rank, not border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20260820)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if args.candidates < 1 or args.workers < 1:
        raise SystemExit("candidates and workers must be positive")
    payload = build_payload(args)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
