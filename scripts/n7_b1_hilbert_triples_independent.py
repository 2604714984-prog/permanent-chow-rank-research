#!/usr/bin/env python3
"""Independent bounded replay of the perm7 B1 Hilbert first differences."""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import comb
from pathlib import Path


TRIPLES = (
    ("S1", (33, 39, 40)),
    ("S2", (34, 38, 39)),
    ("S3", (34, 38, 40)),
    ("S4", (35, 37, 38)),
    ("S5", (35, 37, 39)),
    ("S6", (35, 37, 40)),
)


def successor(number: int, degree: int) -> int:
    if number == 0:
        return 0
    remaining = number
    top_limit = number + degree + 1
    result = 0
    for lower in range(degree, 0, -1):
        top = lower
        while top + 1 < top_limit and comb(top + 1, lower) <= remaining:
            top += 1
        if comb(top, lower) <= remaining:
            remaining -= comb(top, lower)
            result += comb(top + 1, lower + 1)
            top_limit = top
    if remaining:
        raise AssertionError("independent Macaulay expansion failed")
    return result


def positive_compositions(total: int) -> list[tuple[int, ...]]:
    """Enumerate every positive composition of a total at most four."""
    if not 0 <= total <= 4:
        raise ValueError("the frozen frontier has tail total at most four")
    if total == 0:
        return [()]
    rows: list[tuple[int, ...]] = []
    for length in range(1, total + 1):
        for row in product(range(1, total + 1), repeat=length):
            if sum(row) == total:
                rows.append(row)
    return rows


def is_o_sequence(vector: tuple[int, ...]) -> bool:
    return all(
        right <= successor(left, degree)
        for degree, (left, right) in enumerate(zip(vector[1:], vector[2:]), 1)
    )


def independent_inventory() -> dict[str, set[tuple[int, ...]]]:
    inventory: dict[str, set[tuple[int, ...]]] = {}
    for label, (hilbert3, hilbert4, hilbert5) in TRIPLES:
        rows: set[tuple[int, ...]] = set()
        for delta2 in range(22):
            prefix = (
                1,
                6,
                delta2,
                hilbert3 - 7 - delta2,
                hilbert4 - hilbert3,
                hilbert5 - hilbert4,
            )
            if any(value <= 0 for value in prefix):
                continue
            for tail in positive_compositions(42 - hilbert5):
                vector = prefix + tail
                if is_o_sequence(vector):
                    rows.add(vector)
        inventory[label] = rows
    return inventory


def frozen_inventory(path: Path) -> dict[str, set[tuple[int, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    answer = {}
    for row in payload["rows"]:
        raw = [tuple(vector) for vector in row["first_differences"]]
        if len(raw) != len(set(raw)) or len(raw) != row["formal_o_sequence_count"]:
            raise AssertionError((row["label"], "duplicate or missing frozen row"))
        answer[row["label"]] = set(raw)
    return answer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--frozen",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "data"
        / "n7_b1_hilbert_triples.json",
    )
    args = parser.parse_args()
    live = independent_inventory()
    frozen = frozen_inventory(args.frozen)
    if live != frozen:
        print("B1F_01_INDEPENDENT_REPLAY_FAIL")
        return 1
    counts = [len(live[f"S{index}"]) for index in range(1, 7)]
    if counts != [12, 12, 24, 12, 24, 0]:
        raise AssertionError(counts)
    print("B1F_01_INDEPENDENT_REPLAY_PASS", counts, sum(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
