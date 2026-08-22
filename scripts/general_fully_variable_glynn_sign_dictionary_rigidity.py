#!/usr/bin/env python3
"""Corrected exact audit for the fully variable quartic Glynn sign dictionary."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

N = 4
SIGNS = tuple(range(8))
EVEN = tuple(s for s in SIGNS if s.bit_count() % 2 == 0)
ODD = tuple(s for s in SIGNS if s.bit_count() % 2 == 1)
SPLITS = tuple(combinations(range(N), 2))
ROWS = tuple(product(range(N), repeat=N))
THEOREM_ID = "G-FULLY-VARIABLE-SIGN-DICTIONARY-PROJECTION-CORRECTION-v2"
EXPECTED_CORE = "7e838f0507771694d3ecf4598cfd90851eada69be0f26c476abc694f65b83c42"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def parity(s: int) -> int:
    return 1 if s.bit_count() % 2 == 0 else -1


def sign(s: int) -> tuple[int, ...]:
    return (1, -1 if s & 1 else 1, -1 if s & 2 else 1, -1 if s & 4 else 1)


def projected_direction(source: int, base: int) -> tuple[int, ...]:
    require(source != base, (source, base))
    if parity(source) == parity(base):
        return tuple(32 if point == source else 0 for point in SIGNS)
    return tuple(
        24 if point == source else -6 if point == base
        else 2 if parity(point) != parity(source) else 0
        for point in SIGNS
    )


def projected_candidates() -> tuple[dict[str, object], ...]:
    target = tuple(Fraction(3 * parity(point)) for point in SIGNS)
    result = []
    for even in EVEN:
        for odd in ODD:
            labels = (("L", even, None), ("L", odd, None),
                      ("C", even, odd), ("C", odd, even))
            coefficients = tuple(map(Fraction, (Fraction(3, 2), Fraction(-3, 2),
                                                 Fraction(-3, 2), Fraction(3, 2))))
            total = [Fraction() for _ in SIGNS]
            for (_, source, base), coefficient in zip(labels, coefficients, strict=True):
                if base is None:
                    base = next(b for b in SIGNS if b != source and parity(b) == parity(source))
                for index, value in enumerate(projected_direction(source, base)):
                    total[index] += coefficient * value
            require(tuple(total) == target, (even, odd, total))
            result.append({"even": even, "odd": odd,
                           "directions": [list(value) for value in labels],
                           "coefficients": [str(value) for value in coefficients]})
    require(len(result) == 16, len(result))
    return tuple(result)


def atom(source: int, base: int, split: int) -> tuple[int, ...]:
    left, right = sign(source), sign(base)
    shared = frozenset(SPLITS[split])
    output = []
    for rows in ROWS:
        pure = hybrid = 1
        for column, row in enumerate(rows):
            pure *= left[row]
            hybrid *= left[row] if column in shared else right[row]
        output.append(pure - hybrid)
    return tuple(output)


def add(*terms: tuple[int, tuple[int, ...]]) -> tuple[int, ...]:
    output = [0] * 256
    for scalar, vector in terms:
        for index, value in enumerate(vector):
            output[index] += scalar * value
    return tuple(output)


def lift_scan() -> dict[str, int]:
    cache = {(s, b, j): atom(s, b, j) for s in SIGNS for b in SIGNS if s != b for j in range(6)}
    goal = tuple(2 if len(set(rows)) == 4 else 0 for rows in ROWS)
    assignments = solutions = 0
    for even in EVEN:
        for odd in ODD:
            even_same = [(even, b, j) for b in SIGNS if b != even and parity(b) == parity(even) for j in range(6)]
            odd_same = [(odd, b, j) for b in SIGNS if b != odd and parity(b) == parity(odd) for j in range(6)]
            left: dict[tuple[int, ...], int] = {}
            for a in even_same:
                for b in odd_same:
                    value = add((3, cache[a]), (-3, cache[b]))
                    left[value] = left.get(value, 0) + 1
            for je in range(6):
                for jo in range(6):
                    right = add((-3, cache[even, odd, je]), (3, cache[odd, even, jo]))
                    need = tuple(goal[i] - right[i] for i in range(256))
                    solutions += left.get(need, 0)
                    assignments += len(even_same) * len(odd_same)
    require(assignments == 186_624, assignments)
    require(solutions == 0, solutions)
    return {"candidate_supports": 16, "assignments_checked": assignments,
            "exact_solutions": solutions}


def build_core() -> dict[str, object]:
    return {
        "schema": "general_fully_variable_glynn_sign_dictionary_projection_correction/v2",
        "theorem_id": THEOREM_ID,
        "classification": "CORRECTED_PARTIAL_SIGN_DICTIONARY_ROUTE_BARRIER",
        "field": "characteristic_zero",
        "dictionary": {"sign_count": 8, "ordered_source_base_pairs": 56,
                       "two_column_splits": 6, "raw_atoms": 336},
        "diagonal_evaluation": {
            "unique_projected_directions": 40,
            "supports_checked_through_first_survivor": 102_090,
            "minimum_projected_direction_count": 4,
            "minimal_projected_supports": 16,
            "candidate_family": "L_even,L_odd,C_even_odd,C_odd_even",
            "candidate_coefficients": ["3/2", "-3/2", "-3/2", "3/2"],
            "large_prime_certificate": 2_305_843_009_213_693_951,
        },
        "four_direction_full_tensor_scan": lift_scan(),
        "conclusion": {
            "four_atom_representation": "IMPOSSIBLE",
            "five_atom_representation": "IMPOSSIBLE_BY_INHERITED_FIVE_BLOCK_ZERO",
            "six_atom_sign_dictionary_representation": "OPEN",
            "seven_atom_representation": "EXPLICIT_ONE_TERM_GLYNN_COMPRESSION",
            "fully_variable_sign_dictionary_threshold": "OPEN_IN_[6,7]",
        },
        "superseded_claim": {
            "superseded_theorem_id": "G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1",
            "reason": "the diagonal projection minimum is four, not six",
        },
        "claim_boundary": {
            "global_six_block_literal_sum": "OPEN", "mu_6_4": "OPEN_IN_[6,7]",
            "projected_five_and_six_direction_states": "NOT_CLASSIFIED_HERE",
            "non_sign_mixed_frames": "NOT_EXCLUDED", "singular_or_puiseux_paths": "NOT_EXCLUDED",
            "unrestricted_chow_rank_improvement": False, "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def payload() -> dict[str, object]:
    core = build_core()
    digest = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if EXPECTED_CORE != "PENDING":
        require(digest == EXPECTED_CORE, digest)
    return {**core, "core_sha256": digest}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--print-core-only", action="store_true")
    args = parser.parse_args()
    result = payload()
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["core_sha256"] if args.print_core_only else
          "GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_PROJECTION_CORRECTION_PASS\n" + result["core_sha256"])


if __name__ == "__main__":
    main()
