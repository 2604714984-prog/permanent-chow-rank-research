#!/usr/bin/env python3
"""Exact cyclic-projection rank for the perm_7 ``K_{4,3}`` flattening."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import nmod_mat


N = 7
OUTPUT_DEGREE = 4
WEDGE_DEGREE = 3
PRIMES = (1009, 953)


def shifted_subset(values: tuple[int, ...], shift: int) -> tuple[tuple[int, ...], int]:
    moved = tuple((value + shift) % N for value in values)
    inversions = sum(
        moved[first] > moved[second]
        for first in range(len(moved))
        for second in range(first + 1, len(moved))
    )
    return tuple(sorted(moved)), (-1 if inversions % 2 else 1)


def act_state(
    state: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]],
    row_shift: int,
    column_shift: int,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]], int]:
    rows, columns, wedge = state
    moved_rows = tuple(sorted((value + row_shift) % N for value in rows))
    moved_columns = tuple(sorted((value + column_shift) % N for value in columns))
    moved_wedge, sign = shifted_subset(wedge, (row_shift + column_shift) % N)
    return (moved_rows, moved_columns, moved_wedge), sign


def state_space(degree: int, wedge: int):
    subsets = tuple(itertools.combinations(range(N), degree))
    wedges = tuple(itertools.combinations(range(N), wedge))
    return tuple((rows, columns, values) for rows in subsets for columns in subsets for values in wedges)


def orbit_representatives(states):
    unseen = set(states)
    representatives = []
    while unseen:
        seed = min(unseen)
        orbit = {
            act_state(seed, row_shift, column_shift)[0]
            for row_shift in range(N)
            for column_shift in range(N)
        }
        if len(orbit) != N * N:
            raise AssertionError((seed, len(orbit)))
        representative = min(orbit)
        representatives.append(representative)
        unseen.difference_update(orbit)
    representatives.sort()
    return tuple(representatives)


def target_transport(representatives):
    result = {}
    for orbit_index, representative in enumerate(representatives):
        for row_shift in range(N):
            for column_shift in range(N):
                state, sign = act_state(representative, row_shift, column_shift)
                if state in result:
                    raise AssertionError(state)
                result[state] = (orbit_index, row_shift, column_shift, sign)
    return result


def primitive_seventh_root(prime: int) -> int:
    if (prime - 1) % N:
        raise ValueError(f"prime {prime} is not 1 modulo 7")
    for candidate in range(2, prime):
        root = pow(candidate, (prime - 1) // N, prime)
        if root != 1 and pow(root, N, prime) == 1:
            return root
    raise AssertionError(prime)


def character_matrix(
    source_representatives,
    target_lookup,
    target_size: int,
    character: tuple[int, int],
    prime: int,
    root: int,
) -> np.ndarray:
    matrix = np.zeros((target_size, len(source_representatives)), dtype=np.int64)
    first_character, second_character = character
    for column_index, (rows, columns, wedge) in enumerate(source_representatives):
        wedge_set = set(wedge)
        for removed_row in rows:
            for removed_column in columns:
                color = (removed_row + removed_column) % N
                if color in wedge_set:
                    continue
                output_wedge = tuple(sorted((*wedge, color)))
                koszul_sign = -1 if output_wedge.index(color) % 2 else 1
                output_state = (
                    tuple(value for value in rows if value != removed_row),
                    tuple(value for value in columns if value != removed_column),
                    output_wedge,
                )
                row_index, row_shift, column_shift, transport_sign = target_lookup[
                    output_state
                ]
                exponent = (
                    first_character * row_shift + second_character * column_shift
                ) % N
                coefficient = koszul_sign * transport_sign * pow(root, exponent, prime)
                matrix[row_index, column_index] += coefficient
    matrix %= prime
    return matrix


def class_replay(
    source_representatives,
    target_representatives,
    character_classes,
    prime,
):
    root = primitive_seventh_root(prime)
    target_lookup = target_transport(target_representatives)
    rows = []
    total = 0
    for character, multiplicity, label in character_classes:
        matrix = character_matrix(
            source_representatives,
            target_lookup,
            len(target_representatives),
            character,
            prime,
            root,
        )
        rank = rank_mod(matrix, prime)
        rows.append(
            {
                "label": label,
                "character": list(character),
                "multiplicity": multiplicity,
                "block_rank": rank,
            }
        )
        total += multiplicity * rank
    return total, rows, root


def rank_mod(matrix: np.ndarray, prime: int) -> int:
    return int(nmod_mat(matrix.tolist(), prime).rank())


def build_payload() -> dict[str, object]:
    source = state_space(OUTPUT_DEGREE, WEDGE_DEGREE)
    target = state_space(OUTPUT_DEGREE - 1, WEDGE_DEGREE + 1)
    assert len(source) == len(target) == 42_875
    source_representatives = orbit_representatives(source)
    target_representatives = orbit_representatives(target)
    assert len(source_representatives) == len(target_representatives) == 875
    adjacent_source_representatives = orbit_representatives(state_space(5, 2))
    adjacent_target_representatives = orbit_representatives(state_space(4, 3))
    assert len(adjacent_source_representatives) == 189
    assert len(adjacent_target_representatives) == 875
    character_classes = (
        ((0, 0), 1, "trivial"),
        ((1, 0), 12, "one_nonzero_coordinate"),
        ((1, 1), 6, "ratio_1"),
        ((1, 6), 6, "ratio_minus_1"),
        ((1, 2), 12, "ratio_2_or_4"),
        ((1, 3), 12, "ratio_3_or_5"),
    )
    started = time.perf_counter()
    prime_rows = []
    for prime in PRIMES:
        total, rows, root = class_replay(
            source_representatives,
            target_representatives,
            character_classes,
            prime,
        )
        adjacent_total, adjacent_rows, _ = class_replay(
            adjacent_source_representatives,
            adjacent_target_representatives,
            character_classes,
            prime,
        )
        prime_rows.append(
            {
                "prime": prime,
                "primitive_seventh_root": root,
                "character_rows": rows,
                "total_rank": total,
                "adjacent_k52_character_rows": adjacent_rows,
                "adjacent_k52_total_rank": adjacent_total,
            }
        )
    totals = {row["total_rank"] for row in prime_rows}
    if len(totals) != 1:
        raise AssertionError(prime_rows)
    total_rank = totals.pop()
    adjacent_totals = {row["adjacent_k52_total_rank"] for row in prime_rows}
    if adjacent_totals != {8_919}:
        raise AssertionError(prime_rows)
    adjacent_rank = adjacent_totals.pop()
    one_term_cap = 832
    threshold = 49 * one_term_cap
    universal_central_ceiling = len(source) - adjacent_rank
    return {
        "schema_version": 1,
        "status": "EXACT_CYCLIC_PROJECTED_KOSZUL_RANK",
        "n": N,
        "projection": "x_ij -> e_(i+j mod 7)",
        "output_degree": OUTPUT_DEGREE,
        "wedge_degree": WEDGE_DEGREE,
        "ambient_matrix_shape": [len(target), len(source)],
        "source_orbit_count": len(source_representatives),
        "target_orbit_count": len(target_representatives),
        "fourier_block_shape": [875, 875],
        "character_multiplicity_sum": sum(row[1] for row in character_classes),
        "prime_replays": prime_rows,
        "total_rank": total_rank,
        "adjacent_k52_source_orbit_count": len(adjacent_source_representatives),
        "adjacent_k52_target_orbit_count": len(adjacent_target_representatives),
        "adjacent_k52_exact_rank": adjacent_rank,
        "universal_seven_dimensional_central_rank_ceiling": universal_central_ceiling,
        "universal_seven_dimensional_lower_bound_ceiling": math.ceil(
            universal_central_ceiling / one_term_cap
        ),
        "independent_chow_term_rank_cap": one_term_cap,
        "rank_49_threshold": threshold,
        "strictly_exceeds_49_terms": total_rank > threshold,
        "flattening_lower_bound": math.ceil(total_rank / one_term_cap),
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The modular full-rank minors lift to characteristic zero.",
            "The one-term cap uses only the seven-dimensional projected factor span.",
            "The adjacent-map rank and generic semicontinuity bound every seven-dimensional projected central rank by 33956.",
            "This is an ordinary Chow-rank flattening and makes no border-rank claim.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
