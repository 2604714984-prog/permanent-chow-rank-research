#!/usr/bin/env python3
"""Exact quartic audit for the fully variable compressed-Glynn sign dictionary."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence

ORDER = 4
SIGNS = tuple(range(8))
EVEN = tuple(value for value in SIGNS if value.bit_count() % 2 == 0)
ODD = tuple(value for value in SIGNS if value.bit_count() % 2 == 1)
SPLITS = tuple(combinations(range(ORDER), 2))
ROWS = tuple(product(range(ORDER), repeat=ORDER))
THEOREM_ID = "G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def parity(value: int) -> int:
    return 1 if value.bit_count() % 2 == 0 else -1


def sign_vector(value: int) -> tuple[int, int, int, int]:
    return (
        1,
        -1 if value & 1 else 1,
        -1 if value & 2 else 1,
        -1 if value & 4 else 1,
    )


def evaluation_direction(source: int, base: int) -> tuple[int, ...]:
    """Return one eighth of the eight-point diagonal evaluation vector."""
    require(source != base, (source, base))
    if parity(source) == parity(base):
        return tuple(32 if point == source else 0 for point in SIGNS)
    result = []
    for point in SIGNS:
        if parity(point) == parity(source):
            result.append(24 if point == source else 0)
        else:
            result.append(-6 if point == base else 2)
    return tuple(result)


def evaluation_target() -> tuple[int, ...]:
    """Return one eighth of the diagonal evaluation of perm_4."""
    return tuple(3 * parity(point) for point in SIGNS)


def projected_candidates() -> tuple[dict[str, object], ...]:
    candidates = []
    target = evaluation_target()
    for omitted_even in EVEN:
        for omitted_odd in ODD:
            positive = tuple(
                (source, omitted_odd)
                for source in EVEN
                if source != omitted_even
            )
            negative = tuple(
                (source, omitted_even)
                for source in ODD
                if source != omitted_odd
            )
            total = [Fraction(0) for _ in SIGNS]
            for source, base in positive:
                for index, coefficient in enumerate(
                    evaluation_direction(source, base)
                ):
                    total[index] += Fraction(coefficient, 6)
            for source, base in negative:
                for index, coefficient in enumerate(
                    evaluation_direction(source, base)
                ):
                    total[index] -= Fraction(coefficient, 6)
            require(
                tuple(total) == tuple(Fraction(value) for value in target),
                total,
            )
            candidates.append(
                {
                    "omitted_even": omitted_even,
                    "omitted_odd": omitted_odd,
                    "positive_atoms": [list(value) for value in positive],
                    "negative_atoms": [list(value) for value in negative],
                    "positive_coefficient": "1/6",
                    "negative_coefficient": "-1/6",
                }
            )
    require(len(candidates) == 16, len(candidates))
    return tuple(candidates)


def atom_vector(source: int, base: int, split_index: int) -> tuple[int, ...]:
    source_vector = sign_vector(source)
    base_vector = sign_vector(base)
    shared = frozenset(SPLITS[split_index])
    result = []
    for rows in ROWS:
        pure = 1
        hybrid = 1
        for column, row in enumerate(rows):
            pure *= source_vector[row]
            hybrid *= (
                source_vector[row]
                if column in shared
                else base_vector[row]
            )
        result.append(pure - hybrid)
    return tuple(result)


def scaled_target() -> tuple[int, ...]:
    return tuple(6 if len(set(rows)) == ORDER else 0 for rows in ROWS)


def add_vectors(values: Iterable[Sequence[int]]) -> tuple[int, ...]:
    result = [0] * len(ROWS)
    for value in values:
        for index, coefficient in enumerate(value):
            result[index] += int(coefficient)
    return tuple(result)


@lru_cache(maxsize=1)
def full_split_scan() -> dict[str, object]:
    atoms = {
        (source, base, split): atom_vector(source, base, split)
        for source in SIGNS
        for base in SIGNS
        if source != base
        for split in range(len(SPLITS))
    }
    target = scaled_target()
    per_candidate = []
    total_solutions = 0

    for candidate in projected_candidates():
        positive = [tuple(value) for value in candidate["positive_atoms"]]
        negative = [tuple(value) for value in candidate["negative_atoms"]]

        left_counter: Counter[tuple[int, ...]] = Counter()
        for choices in product(range(len(SPLITS)), repeat=3):
            value = add_vectors(
                atoms[source, base, split]
                for (source, base), split in zip(
                    positive, choices, strict=True
                )
            )
            left_counter[
                tuple(
                    entry - target[index]
                    for index, entry in enumerate(value)
                )
            ] += 1

        solutions = 0
        right_states = 0
        for choices in product(range(len(SPLITS)), repeat=3):
            right_states += 1
            value = add_vectors(
                atoms[source, base, split]
                for (source, base), split in zip(
                    negative, choices, strict=True
                )
            )
            solutions += left_counter.get(value, 0)

        require(right_states == 216, right_states)
        require(solutions == 0, (candidate, solutions))
        total_solutions += solutions
        per_candidate.append(
            {
                "omitted_even": candidate["omitted_even"],
                "omitted_odd": candidate["omitted_odd"],
                "left_states": sum(left_counter.values()),
                "distinct_left_states": len(left_counter),
                "right_states": right_states,
                "exact_solutions": solutions,
            }
        )

    assignments = len(projected_candidates()) * len(SPLITS) ** 6
    require(assignments == 746_496, assignments)
    require(total_solutions == 0, total_solutions)
    return {
        "candidate_supports": len(projected_candidates()),
        "split_choices_per_atom": len(SPLITS),
        "assignments_per_support": len(SPLITS) ** 6,
        "assignments_checked": assignments,
        "exact_solutions": total_solutions,
        "candidate_checks": per_candidate,
    }


def payload() -> dict[str, object]:
    scan = full_split_scan()
    return {
        "schema": "general_fully_variable_glynn_sign_dictionary_rigidity/v1",
        "theorem_id": THEOREM_ID,
        "classification": "STRICT_FULL_SIGN_DICTIONARY_ROUTE_THEOREM",
        "field": "characteristic_zero",
        "dictionary": {
            "sign_count": 8,
            "ordered_source_base_pairs": 56,
            "oriented_two_column_splits": 6,
            "raw_atoms": 336,
        },
        "diagonal_evaluation": {
            "unique_projected_directions": 40,
            "supports_checked_through_six": 4_598_478,
            "minimum_projected_term_count": 6,
            "minimal_projected_supports": 16,
            "candidate_family": (
                "one omitted even sign and one omitted odd sign; "
                "three stars in each direction"
            ),
            "candidate_coefficients": "parity(source)/6",
            "large_prime_certificate": 2_305_843_009_213_693_951,
            "hadamard_minor_bound": "(32*sqrt(7))^7 < 3.2e13 < prime",
        },
        "full_tensor_scan": scan,
        "conclusion": {
            "fully_variable_quartic_sign_dictionary_threshold": 7,
            "six_atom_representation": "IMPOSSIBLE",
            "seven_atom_representation": "EXPLICIT_ONE_TERM_GLYNN_COMPRESSION",
        },
        "claim_boundary": {
            "global_six_block_literal_sum": "OPEN",
            "mu_6_4": "OPEN_IN_[6,7]",
            "non_sign_mixed_frames": "NOT_EXCLUDED",
            "singular_or_puiseux_paths": "NOT_EXCLUDED",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    result = payload()
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_RIGIDITY_PASS")
    print(THEOREM_ID)


if __name__ == "__main__":
    main()
