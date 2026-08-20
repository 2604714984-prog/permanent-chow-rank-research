#!/usr/bin/env python3
"""Exact cyclic-projection rank for the perm_7 ``K_{4,3}`` flattening."""

from __future__ import annotations

import argparse
from fractions import Fraction
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
CHARACTER_CLASSES = (
    ((0, 0), 1, "trivial"),
    ((1, 0), 12, "one_nonzero_coordinate"),
    ((1, 1), 6, "ratio_1"),
    ((1, 6), 6, "ratio_minus_1"),
    ((1, 2), 12, "ratio_2_or_4"),
    ((1, 3), 12, "ratio_3_or_5"),
)
ACTIVE_K43_ONE_TERM_RANKS = (35, 224, 595, 832, 595, 224, 35, 0)


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


def projected_route_scan(active_adjacent_ranks: tuple[int, ...]) -> dict[str, object]:
    """Bound every quotient dimension at least seven by an adjacent arrow."""
    best = None
    checked = 0
    for quotient_dimension in range(7, 50):
        inactive = quotient_dimension - 7
        for wedge_degree in range(quotient_dimension):
            incoming_rank = 0
            term_cap = 0
            for inactive_wedge in range(inactive + 1):
                active_incoming = wedge_degree - 1 - inactive_wedge
                if 0 <= active_incoming < len(active_adjacent_ranks):
                    incoming_rank += (
                        math.comb(inactive, inactive_wedge)
                        * active_adjacent_ranks[active_incoming]
                    )
                active_central = wedge_degree - inactive_wedge
                if 0 <= active_central < len(ACTIVE_K43_ONE_TERM_RANKS):
                    term_cap += (
                        math.comb(inactive, inactive_wedge)
                        * ACTIVE_K43_ONE_TERM_RANKS[active_central]
                    )
            if term_cap == 0:
                continue
            domain = 1225 * math.comb(quotient_dimension, wedge_degree)
            codomain = 1225 * math.comb(quotient_dimension, wedge_degree + 1)
            central_ceiling = min(domain - incoming_rank, codomain)
            ratio = Fraction(central_ceiling, term_cap)
            checked += 1
            row = {
                "quotient_dimension": quotient_dimension,
                "wedge_degree": wedge_degree,
                "incoming_special_rank": incoming_rank,
                "central_rank_ceiling": central_ceiling,
                "one_term_rank_cap": term_cap,
                "ratio_numerator": ratio.numerator,
                "ratio_denominator": ratio.denominator,
                "integer_ceiling": math.ceil(ratio),
            }
            if best is None or ratio > Fraction(
                best["ratio_numerator"], best["ratio_denominator"]
            ):
                best = row
    assert best is not None
    return {
        "quotient_dimension_range": [7, 49],
        "checked_pair_count": checked,
        "maximum": best,
        "cannot_improve_lower_49": best["integer_ceiling"] <= 49,
    }


def build_payload() -> dict[str, object]:
    source = state_space(OUTPUT_DEGREE, WEDGE_DEGREE)
    target = state_space(OUTPUT_DEGREE - 1, WEDGE_DEGREE + 1)
    assert len(source) == len(target) == 42_875
    source_representatives = orbit_representatives(source)
    target_representatives = orbit_representatives(target)
    assert len(source_representatives) == len(target_representatives) == 875
    adjacent_spaces = []
    for wedge in range(7):
        adjacent_source = orbit_representatives(state_space(5, wedge))
        adjacent_target = orbit_representatives(state_space(4, wedge + 1))
        adjacent_spaces.append((wedge, adjacent_source, adjacent_target))
    started = time.perf_counter()
    prime_rows = []
    for prime in PRIMES:
        total, rows, root = class_replay(
            source_representatives,
            target_representatives,
            CHARACTER_CLASSES,
            prime,
        )
        adjacent_rows_by_wedge = []
        adjacent_totals = []
        for wedge, adjacent_source, adjacent_target in adjacent_spaces:
            adjacent_total, adjacent_rows, _ = class_replay(
                adjacent_source,
                adjacent_target,
                CHARACTER_CLASSES,
                prime,
            )
            adjacent_totals.append(adjacent_total)
            adjacent_rows_by_wedge.append(
                {
                    "wedge_degree": wedge,
                    "source_orbit_count": len(adjacent_source),
                    "target_orbit_count": len(adjacent_target),
                    "character_rows": adjacent_rows,
                    "total_rank": adjacent_total,
                }
            )
        prime_rows.append(
            {
                "prime": prime,
                "primitive_seventh_root": root,
                "character_rows": rows,
                "total_rank": total,
                "adjacent_k5_rank_by_wedge": adjacent_totals,
                "adjacent_k5_rows_by_wedge": adjacent_rows_by_wedge,
            }
        )
    totals = {row["total_rank"] for row in prime_rows}
    if len(totals) != 1:
        raise AssertionError(prime_rows)
    total_rank = totals.pop()
    adjacent_profiles = {
        tuple(row["adjacent_k5_rank_by_wedge"]) for row in prime_rows
    }
    expected_adjacent_profile = (441, 3_038, 8_919, 14_413, 13_741, 7_266, 1_225)
    if adjacent_profiles != {expected_adjacent_profile}:
        raise AssertionError(prime_rows)
    adjacent_profile = adjacent_profiles.pop()
    adjacent_rank = adjacent_profile[2]
    one_term_cap = 832
    threshold = 49 * one_term_cap
    universal_central_ceiling = len(source) - adjacent_rank
    route_scan = projected_route_scan(adjacent_profile)
    return {
        "schema_version": 2,
        "status": "EXACT_PROJECTED_KOSZUL_ROUTE_BARRIER",
        "n": N,
        "projection": "x_ij -> e_(i+j mod 7)",
        "output_degree": OUTPUT_DEGREE,
        "wedge_degree": WEDGE_DEGREE,
        "ambient_matrix_shape": [len(target), len(source)],
        "source_orbit_count": len(source_representatives),
        "target_orbit_count": len(target_representatives),
        "fourier_block_shape": [875, 875],
        "character_multiplicity_sum": sum(row[1] for row in CHARACTER_CLASSES),
        "prime_replays": prime_rows,
        "total_rank": total_rank,
        "adjacent_k52_source_orbit_count": len(adjacent_spaces[2][1]),
        "adjacent_k52_target_orbit_count": len(adjacent_spaces[2][2]),
        "adjacent_k52_exact_rank": adjacent_rank,
        "active_cyclic_adjacent_rank_by_wedge": list(adjacent_profile),
        "universal_seven_dimensional_central_rank_ceiling": universal_central_ceiling,
        "universal_seven_dimensional_lower_bound_ceiling": math.ceil(
            universal_central_ceiling / one_term_cap
        ),
        "independent_chow_term_rank_cap": one_term_cap,
        "rank_49_threshold": threshold,
        "strictly_exceeds_49_terms": total_rank > threshold,
        "flattening_lower_bound": math.ceil(total_rank / one_term_cap),
        "all_quotient_dimensions_at_least_seven": route_scan,
        "elapsed_seconds": time.perf_counter() - started,
        "claim_boundary": [
            "The modular full-rank minors lift to characteristic zero.",
            "The one-term cap uses only the seven-dimensional projected factor span.",
            "The adjacent-map rank and generic semicontinuity bound every seven-dimensional projected central rank by 33956.",
            "Inactive-wedge convolution extends the adjacent-map bound to every quotient dimension from seven through forty-nine.",
            "The resulting family-wide integer ceiling is 47, so these projected Koszul routes cannot improve the established lower bound 49.",
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
