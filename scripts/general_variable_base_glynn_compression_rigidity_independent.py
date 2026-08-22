#!/usr/bin/env python3
"""Independent modular replay for variable-base Glynn rigidity."""

from __future__ import annotations

import argparse
import json
from itertools import product

PRIME = 1_000_003
EXPECTED_PRIMARY_CORE = "6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def signs(order: int) -> tuple[tuple[int, ...], ...]:
    return tuple((1,) + tail for tail in product((1, -1), repeat=order - 1))


def character(value: tuple[int, ...]) -> int:
    return -1 if sum(entry == -1 for entry in value) % 2 else 1


def left_coordinates(order: int) -> tuple[tuple[int, ...], ...]:
    values = signs(order)
    chars = tuple(character(value) for value in values)
    dimension = len(values) - 1
    result = []
    result.append(tuple((-chars[index]) % PRIME for index in range(1, len(values))))
    for index in range(1, len(values)):
        row = [0] * dimension
        row[index - 1] = 1
        result.append(tuple(row))
    return tuple(result)


def tail(value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a * b) % PRIME for a in value for b in value)


def add_outer(target: list[int], left: tuple[int, ...], right: tuple[int, ...], scalar: int) -> None:
    width = len(right)
    scalar %= PRIME
    for row, a in enumerate(left):
        if not a:
            continue
        offset = row * width
        for column, b in enumerate(right):
            target[offset + column] = (target[offset + column] + scalar * a * b) % PRIME


def audit_order(order: int) -> dict[str, int]:
    values = signs(order)
    chars = tuple(character(value) for value in values)
    left = left_coordinates(order)
    tails = tuple(tail(value) for value in values)
    dimension = len(values) - 1
    width = order * order
    target = [0] * (dimension * width)
    for index in range(len(values)):
        add_outer(target, left[index], tails[index], chars[index])
    for omitted in range(len(values)):
        candidate = [0] * len(target)
        for index in range(len(values)):
            if index == omitted:
                continue
            difference = tuple((tails[index][j] - tails[omitted][j]) % PRIME for j in range(width))
            add_outer(candidate, left[index], difference, chars[index])
        require(candidate == target, (order, omitted))
    return {
        "order": order,
        "sign_count": len(values),
        "omitted_bases_checked": len(values),
        "minimum_atoms": len(values) - 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-core")
    parser.add_argument("--json")
    args = parser.parse_args()
    if args.expected_core is not None:
        require(args.expected_core == EXPECTED_PRIMARY_CORE, args.expected_core)
    rows = [audit_order(order) for order in range(3, 8)]
    require(rows[1]["sign_count"] == 8 and rows[1]["minimum_atoms"] == 7, rows[1])
    payload = {
        "schema": "general_variable_base_glynn_compression_rigidity_independent/v1",
        "prime": PRIME,
        "primary_core": EXPECTED_PRIMARY_CORE,
        "rows": rows,
    }
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
    print("GENERAL_VARIABLE_BASE_GLYNN_COMPRESSION_RIGIDITY_INDEPENDENT_PASS")
    print(EXPECTED_PRIMARY_CORE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
