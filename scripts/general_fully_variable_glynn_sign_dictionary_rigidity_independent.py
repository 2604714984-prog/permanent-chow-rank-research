#!/usr/bin/env python3
"""Independent XOR replay of the corrected four-direction lift barrier."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from pathlib import Path

ROW_CHARACTERS = (0, 1, 2, 4)
SIGNS = tuple(range(8))
EVEN = tuple(value for value in SIGNS if value.bit_count() % 2 == 0)
ODD = tuple(value for value in SIGNS if value.bit_count() % 2 == 1)
SPLITS = tuple(combinations(range(4), 2))
ROW_TUPLES = tuple(product(range(4), repeat=4))


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def parity(value: int) -> int:
    return 1 if value.bit_count() % 2 == 0 else -1


def character(sign: int, label: int) -> int:
    return -1 if (sign & label).bit_count() % 2 else 1


def atom(source: int, base: int, split: tuple[int, int]) -> tuple[int, ...]:
    shared = frozenset(split)
    result = []
    for rows in ROW_TUPLES:
        labels = [ROW_CHARACTERS[row] for row in rows]
        all_label = 0
        shared_label = 0
        tail_label = 0
        for column, label in enumerate(labels):
            all_label ^= label
            if column in shared:
                shared_label ^= label
            else:
                tail_label ^= label
        result.append(
            character(source, all_label)
            - character(source, shared_label) * character(base, tail_label)
        )
    return tuple(result)


def add_scaled(terms) -> tuple[int, ...]:
    result = [0] * 256
    for scalar, value in terms:
        for index, coefficient in enumerate(value):
            result[index] += scalar * coefficient
    return tuple(result)


def target() -> tuple[int, ...]:
    return tuple(2 if len(set(rows)) == 4 else 0 for rows in ROW_TUPLES)


def audit() -> dict[str, int]:
    cache = {
        (source, base, split_index): atom(source, base, SPLITS[split_index])
        for source in SIGNS
        for base in SIGNS
        if source != base
        for split_index in range(6)
    }
    goal = target()
    assignments = 0
    solutions = 0
    for even in EVEN:
        for odd in ODD:
            even_same = [
                (even, base, split)
                for base in SIGNS
                if base != even and parity(base) == parity(even)
                for split in range(6)
            ]
            odd_same = [
                (odd, base, split)
                for base in SIGNS
                if base != odd and parity(base) == parity(odd)
                for split in range(6)
            ]
            left = {}
            for left_even in even_same:
                for left_odd in odd_same:
                    value = add_scaled(
                        ((3, cache[left_even]), (-3, cache[left_odd]))
                    )
                    left[value] = left.get(value, 0) + 1
            for split_even in range(6):
                for split_odd in range(6):
                    right = add_scaled(
                        (
                            (-3, cache[even, odd, split_even]),
                            (3, cache[odd, even, split_odd]),
                        )
                    )
                    need = tuple(
                        goal[index] - right[index] for index in range(256)
                    )
                    solutions += left.get(need, 0)
                    assignments += len(even_same) * len(odd_same)
    require(assignments == 186_624, assignments)
    require(solutions == 0, solutions)
    return {"assignments_checked": assignments, "exact_solutions": solutions}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    arguments = parser.parse_args()
    result = audit()
    if arguments.json is not None:
        arguments.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(
        "GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_"
        "PROJECTION_CORRECTION_INDEPENDENT_PASS"
    )


if __name__ == "__main__":
    main()
