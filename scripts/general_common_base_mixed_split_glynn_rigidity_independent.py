#!/usr/bin/env python3
"""Independent modular replay of common-base mixed-split Glynn rigidity."""

from __future__ import annotations

import argparse
from itertools import combinations, product

PRIME = 1_000_003
PRIMARY_CORE = "b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def signs() -> tuple[tuple[int, ...], ...]:
    return tuple((1,) + tail for tail in product((1, -1), repeat=3))


def chi(value: tuple[int, ...]) -> int:
    result = 1
    for entry in value:
        result *= entry
    return result


def atom(source: tuple[int, ...], base: tuple[int, ...], shared: tuple[int, int]) -> tuple[int, ...]:
    tail = tuple(index for index in range(4) if index not in shared)
    output = []
    for assignment in product(range(4), repeat=4):
        prefix = source[assignment[shared[0]]] * source[assignment[shared[1]]]
        difference = (
            source[assignment[tail[0]]] * source[assignment[tail[1]]]
            - base[assignment[tail[0]]] * base[assignment[tail[1]]]
        )
        output.append(prefix * difference % PRIME)
    return tuple(output)


def target(values: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    output = []
    for assignment in product(range(4), repeat=4):
        coefficient = 0
        for value in values:
            term = chi(value)
            for mode in range(4):
                term *= value[assignment[mode]]
            coefficient += term
        output.append(coefficient % PRIME)
    return tuple(output)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % PRIME for a, b in zip(left, right, strict=True))


def subtract(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a - b) % PRIME for a, b in zip(left, right, strict=True))


def quartic_scan() -> dict[str, int]:
    values = signs()
    base = values[0]
    retained = values[1:]
    splits = tuple(combinations(range(4), 2))
    wanted = target(values)
    contributions = tuple(
        tuple(tuple(chi(value) * entry % PRIME for entry in atom(value, base, split)) for split in splits)
        for value in retained
    )
    last = {contributions[-1][index]: index for index in range(6)}
    solutions = []
    zero = (0,) * 256
    for choice in product(range(6), repeat=6):
        partial = zero
        for source, split in enumerate(choice):
            partial = add(partial, contributions[source][split])
        final = last.get(subtract(wanted, partial))
        if final is not None:
            solutions.append(choice + (final,))
    require(solutions == [tuple([index] * 7) for index in range(6)], solutions)
    return {"assignments": 6**7, "solutions": len(solutions)}


def defect_relation_check() -> None:
    vectors = []
    coefficients = []
    for mask in range(1, 8):
        value = tuple((mask >> index) & 1 for index in range(3))
        vectors.append(tuple(value[i] * value[j] for i in range(3) for j in range(3)))
        coefficients.append(-1 if mask.bit_count() % 2 else 1)
    zero_selections = []
    for selection in range(1 << 7):
        total = [0] * 9
        for index in range(7):
            if selection >> index & 1:
                for position, entry in enumerate(vectors[index]):
                    total[position] += coefficients[index] * entry
        if total == [0] * 9:
            zero_selections.append(selection)
    require(zero_selections == [0, 127], zero_selections)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-core")
    args = parser.parse_args()
    if args.expected_core:
        require(args.expected_core == PRIMARY_CORE, args.expected_core)
    defect_relation_check()
    result = quartic_scan()
    require(result == {"assignments": 279936, "solutions": 6}, result)
    print("GENERAL_COMMON_BASE_MIXED_SPLIT_GLYNN_RIGIDITY_INDEPENDENT_PASS")
    print(PRIMARY_CORE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
