#!/usr/bin/env python3
"""Independent replay of local rigidity of the compressed Glynn witness.

This implementation imports none of the primary helpers. It reconstructs each
quartic component from its six labeled factors and two active source subsets,
projects all 15 source variations and all 96 factor variations to column
multidegree (1,1,1,1), and checks deletion ranks over an independent prime.
"""

from __future__ import annotations

import argparse
from itertools import combinations, product

ORDER = 4
REFERENCE = (1, 1, 1, 1)
SIGNS = tuple((1,) + tail for tail in product((1, -1), repeat=3))
RETAINED = tuple(value for value in SIGNS if value != REFERENCE)
LABEL_SUBSETS = tuple(combinations(range(6), 4))
PRIME = 1_000_037
EXPECTED_CORE = "7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710"
MARKER = "GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_INDEPENDENT_PASS"

Vector = tuple[int, ...]
Factor = tuple[int, tuple[int, ...]]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def character(value: tuple[int, ...]) -> int:
    result = 1
    for entry in value:
        result *= entry
    return result


def sign_bits(value: tuple[int, ...]) -> int:
    result = 0
    for index, entry in enumerate(value[1:]):
        if entry == -1:
            result |= 1 << index
    return result


def basis(index: int) -> tuple[int, ...]:
    return tuple(1 if position == index else 0 for position in range(ORDER))


def tensor_from_columns(columns: tuple[tuple[int, ...], ...]) -> Vector:
    require(len(columns) == ORDER, columns)
    return tuple(
        columns[0][i] * columns[1][j] * columns[2][k] * columns[3][l]
        for i in range(ORDER)
        for j in range(ORDER)
        for k in range(ORDER)
        for l in range(ORDER)
    )


def add_scaled(target: list[int], scalar: int, vector: Vector) -> None:
    for index, entry in enumerate(vector):
        target[index] += scalar * entry


def projected_product(factors: tuple[Factor, ...], subset: tuple[int, ...]) -> Vector:
    selected = [factors[index] for index in subset]
    columns = [column for column, _ in selected]
    if sorted(columns) != list(range(ORDER)):
        return (0,) * (ORDER**4)
    ordered: list[tuple[int, ...] | None] = [None] * ORDER
    for column, vector in selected:
        ordered[column] = vector
    require(all(value is not None for value in ordered), ordered)
    return tensor_from_columns(tuple(value for value in ordered if value is not None))


def frame(value: tuple[int, ...]) -> tuple[Factor, ...]:
    return (
        (0, value),
        (1, value),
        (2, value),
        (3, value),
        (2, REFERENCE),
        (3, REFERENCE),
    )


def active_source(value: tuple[int, ...]) -> tuple[tuple[int, tuple[int, ...]], ...]:
    chi = character(value)
    return (
        (chi, (0, 1, 2, 3)),
        (-chi, (0, 1, 4, 5)),
    )


def atom(value: tuple[int, ...]) -> Vector:
    factors = frame(value)
    result = [0] * (ORDER**4)
    for coefficient, subset in active_source(value):
        add_scaled(result, coefficient, projected_product(factors, subset))
    return tuple(result)


def projected_generators(value: tuple[int, ...]) -> tuple[Vector, ...]:
    factors = frame(value)
    generators: list[Vector] = []

    source_nonzero = 0
    for subset in LABEL_SUBSETS:
        vector = projected_product(factors, subset)
        if any(vector):
            generators.append(vector)
            source_nonzero += 1
    require(source_nonzero == 4, (value, source_nonzero))

    factor_nonzero = 0
    for moving_label in range(6):
        for target_column in range(ORDER):
            for row in range(ORDER):
                moved = list(factors)
                moved[moving_label] = (target_column, basis(row))
                result = [0] * (ORDER**4)
                for coefficient, subset in active_source(value):
                    if moving_label in subset:
                        add_scaled(
                            result,
                            coefficient,
                            projected_product(tuple(moved), subset),
                        )
                vector = tuple(result)
                if any(vector):
                    generators.append(vector)
                    factor_nonzero += 1
    require(factor_nonzero == 24, (value, factor_nonzero))
    require(len(generators) == 28, len(generators))
    return tuple(generators)


def modular_rank(vectors: list[Vector], prime: int = PRIME) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for vector in vectors:
        current = {
            index: entry % prime
            for index, entry in enumerate(vector)
            if entry % prime
        }
        while current:
            pivot = max(current)
            known = pivots.get(pivot)
            if known is None:
                inverse = pow(current[pivot], prime - 2, prime)
                current = {
                    index: coefficient * inverse % prime
                    for index, coefficient in current.items()
                    if coefficient * inverse % prime
                }
                pivots[pivot] = current
                break
            factor = current[pivot]
            for index, coefficient in known.items():
                updated = (current.get(index, 0) - factor * coefficient) % prime
                if updated:
                    current[index] = updated
                elif index in current:
                    del current[index]
    return len(pivots)


def mode_rank(vector: Vector, mode: int) -> int:
    rows: list[list[int]] = [[0] * (ORDER**3) for _ in range(ORDER)]
    for i in range(ORDER):
        for j in range(ORDER):
            for k in range(ORDER):
                for l in range(ORDER):
                    indices = (i, j, k, l)
                    row = indices[mode]
                    others = tuple(
                        indices[position]
                        for position in range(4)
                        if position != mode
                    )
                    column = others[0] * ORDER * ORDER + others[1] * ORDER + others[2]
                    flat = ((i * ORDER + j) * ORDER + k) * ORDER + l
                    rows[row][column] = vector[flat]
    return modular_rank([tuple(row) for row in rows])


def replay(expected_core: str) -> None:
    require(expected_core == EXPECTED_CORE, expected_core)
    atoms = {value: atom(value) for value in RETAINED}
    tangents = {value: projected_generators(value) for value in RETAINED}

    require(modular_rank(list(atoms.values())) == 7, "atom rank")
    for value in RETAINED:
        require(modular_rank(list(tangents[value])) == 18, (value, "tangent"))

    pair_count = 0
    for left, right in combinations(RETAINED, 2):
        combined = tuple(
            a + b for a, b in zip(atoms[left], atoms[right], strict=True)
        )
        profile = tuple(mode_rank(combined, mode) for mode in range(4))
        require(profile == (2, 2, 3, 3), (left, right, profile))
        pair_count += 1
    require(pair_count == 21, pair_count)

    for missing in RETAINED:
        six = [
            generator
            for value in RETAINED
            if value != missing
            for generator in tangents[value]
        ]
        require(modular_rank(six) == 108, (sign_bits(missing), "six"))
        require(
            modular_rank(six + [atoms[missing]]) == 109,
            (sign_bits(missing), "augmented"),
        )

    all_seven = [
        generator for value in RETAINED for generator in tangents[value]
    ]
    require(modular_rank(all_seven) == 123, "all seven")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-core", default=EXPECTED_CORE)
    arguments = parser.parse_args()
    replay(arguments.expected_core)
    print(MARKER)
    print(EXPECTED_CORE)
    print(PRIME)


if __name__ == "__main__":
    main()
