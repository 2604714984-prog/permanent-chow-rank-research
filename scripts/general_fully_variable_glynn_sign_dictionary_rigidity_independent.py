#!/usr/bin/env python3
"""Independent XOR-character replay of the fully variable sign audit."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path

ROW_CHARACTERS = (0, 1, 2, 4)
SIGNS = tuple(range(8))
EVEN = tuple(value for value in SIGNS if value.bit_count() % 2 == 0)
ODD = tuple(value for value in SIGNS if value.bit_count() % 2 == 1)
SPLITS = tuple(combinations(range(4), 2))
ROW_TUPLES = tuple(product(range(4), repeat=4))
THEOREM_ID = "G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def character(sign: int, label: int) -> int:
    return -1 if (sign & label).bit_count() % 2 else 1


def atom(source: int, base: int, split: tuple[int, int]) -> tuple[int, ...]:
    shared = frozenset(split)
    result = []
    for rows in ROW_TUPLES:
        labels = [ROW_CHARACTERS[row] for row in rows]
        total = 0
        shared_total = 0
        tail_total = 0
        for column, label in enumerate(labels):
            total ^= label
            if column in shared:
                shared_total ^= label
            else:
                tail_total ^= label
        result.append(
            character(source, total)
            - character(source, shared_total) * character(base, tail_total)
        )
    return tuple(result)


def add(values):
    result = [0] * 256
    for value in values:
        for index, coefficient in enumerate(value):
            result[index] += coefficient
    return tuple(result)


def target() -> tuple[int, ...]:
    return tuple(6 if len(set(rows)) == 4 else 0 for rows in ROW_TUPLES)


def audit() -> dict[str, int]:
    cache = {
        (source, base, split_index): atom(source, base, SPLITS[split_index])
        for source in SIGNS
        for base in SIGNS
        if source != base
        for split_index in range(6)
    }
    goal = target()
    checked = 0
    solutions = 0
    for omitted_even in EVEN:
        for omitted_odd in ODD:
            positive = [
                (source, omitted_odd)
                for source in EVEN
                if source != omitted_even
            ]
            negative = [
                (source, omitted_even)
                for source in ODD
                if source != omitted_odd
            ]
            left = Counter()
            for choices in product(range(6), repeat=3):
                value = add(
                    cache[source, base, split]
                    for (source, base), split in zip(
                        positive, choices, strict=True
                    )
                )
                left[
                    tuple(value[index] - goal[index] for index in range(256))
                ] += 1
            for choices in product(range(6), repeat=3):
                value = add(
                    cache[source, base, split]
                    for (source, base), split in zip(
                        negative, choices, strict=True
                    )
                )
                checked += sum(left.values())
                solutions += left.get(value, 0)
    require(checked == 746_496, checked)
    require(solutions == 0, solutions)
    return {"assignments_checked": checked, "exact_solutions": solutions}


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
        "RIGIDITY_INDEPENDENT_PASS"
    )
    print(THEOREM_ID)


if __name__ == "__main__":
    main()
