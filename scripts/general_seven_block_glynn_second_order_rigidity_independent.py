#!/usr/bin/env python3
"""Independent modular replay of seven-block second-order local rigidity.

The implementation uses monomial tuples directly, rebuilds the 666-parameter
six-block tangent map, computes its nullspace over an independent prime, and
checks all polarized curvature directions without importing the primary code.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations, product
from typing import Mapping, Sequence

ORDER = 4
REFERENCE = (1, 1, 1, 1)
SIGNS = tuple((1,) + tail for tail in product((1, -1), repeat=3))
RETAINED = tuple(value for value in SIGNS if value != REFERENCE)
SUBSETS = tuple(combinations(range(6), 4))
ACTIVE = ((0, 1, 2, 3), (0, 1, 4, 5))
LOCAL_WIDTH = 15 + 6 * 16
PRIME = 1_000_037
EXPECTED_CORE = "e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c"
MARKER = "GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_INDEPENDENT_PASS"

Monomial = tuple[int, ...]
Form = dict[int, int]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def character(value: Sequence[int]) -> int:
    result = 1
    for entry in value:
        result *= int(entry)
    return result


def bits(value: Sequence[int]) -> int:
    result = 0
    for index, entry in enumerate(value[1:]):
        if entry == -1:
            result |= 1 << index
    return result


def frame(value: Sequence[int]) -> tuple[Form, ...]:
    result = []
    for column, vector in (
        (0, value),
        (1, value),
        (2, value),
        (3, value),
        (2, REFERENCE),
        (3, REFERENCE),
    ):
        result.append(
            {row * 4 + column: int(vector[row]) for row in range(4)}
        )
    return tuple(result)


def multiply(forms: Sequence[Mapping[int, int]]) -> dict[Monomial, int]:
    polynomial: dict[Monomial, int] = {(): 1}
    for form in forms:
        updated: dict[Monomial, int] = defaultdict(int)
        for monomial, coefficient in polynomial.items():
            for variable, scalar in form.items():
                target = tuple(sorted(monomial + (variable,)))
                updated[target] = (
                    updated[target] + coefficient * scalar
                ) % PRIME
        polynomial = {
            key: value for key, value in updated.items() if value
        }
    return polynomial


def add_scaled(
    target: dict[object, int],
    scalar: int,
    value: Mapping[object, int],
) -> None:
    for key, coefficient in value.items():
        updated = (target.get(key, 0) + scalar * coefficient) % PRIME
        if updated:
            target[key] = updated
        elif key in target:
            del target[key]


def projected(polynomial: Mapping[Monomial, int]) -> dict[int, int]:
    result: dict[int, int] = defaultdict(int)
    for monomial, coefficient in polynomial.items():
        if len(monomial) != 4:
            continue
        columns = [variable % 4 for variable in monomial]
        if sorted(columns) != [0, 1, 2, 3]:
            continue
        rows = [0] * 4
        for variable in monomial:
            rows[variable % 4] = variable // 4
        index = ((rows[0] * 4 + rows[1]) * 4 + rows[2]) * 4 + rows[3]
        result[index] = (result[index] + coefficient) % PRIME
    return {key: value for key, value in result.items() if value}


def tangent(value: Sequence[int]) -> tuple[dict[Monomial, int], ...]:
    factors = frame(value)
    result = [
        multiply([factors[index] for index in subset])
        for subset in SUBSETS
    ]
    coefficients = (character(value), -character(value))
    for label in range(6):
        for variable in range(16):
            column: dict[Monomial, int] = {}
            for scalar, subset in zip(
                coefficients,
                ACTIVE,
                strict=True,
            ):
                if label not in subset:
                    continue
                forms = [
                    {variable: 1} if index == label else factors[index]
                    for index in subset
                ]
                add_scaled(column, scalar, multiply(forms))
            result.append(column)
    require(len(result) == LOCAL_WIDTH, len(result))
    return tuple(result)


class ModularBasis:
    def __init__(self) -> None:
        self.rows: dict[object, dict[object, int]] = {}

    @property
    def rank(self) -> int:
        return len(self.rows)

    def reduce(self, value: Mapping[object, int]) -> dict[object, int]:
        current = {
            key: coefficient % PRIME
            for key, coefficient in value.items()
            if coefficient % PRIME
        }
        while current:
            pivot = max(current)
            known = self.rows.get(pivot)
            if known is None:
                return current
            factor = current[pivot]
            for key, coefficient in known.items():
                updated = (
                    current.get(key, 0) - factor * coefficient
                ) % PRIME
                if updated:
                    current[key] = updated
                elif key in current:
                    del current[key]
        return {}

    def add(self, value: Mapping[object, int]) -> bool:
        current = self.reduce(value)
        if not current:
            return False
        pivot = max(current)
        inverse = pow(current[pivot], PRIME - 2, PRIME)
        self.rows[pivot] = {
            key: coefficient * inverse % PRIME
            for key, coefficient in current.items()
            if coefficient * inverse % PRIME
        }
        return True


def kernel(
    columns: Sequence[Mapping[Monomial, int]],
) -> tuple[int, tuple[dict[int, int], ...]]:
    output_basis: dict[
        Monomial,
        tuple[dict[Monomial, int], dict[int, int]],
    ] = {}
    relations = []
    for column_index, column in enumerate(columns):
        current = dict(column)
        relation = {column_index: 1}
        while current:
            pivot = max(current)
            known = output_basis.get(pivot)
            if known is None:
                inverse = pow(current[pivot], PRIME - 2, PRIME)
                current = {
                    key: coefficient * inverse % PRIME
                    for key, coefficient in current.items()
                    if coefficient * inverse % PRIME
                }
                relation = {
                    key: coefficient * inverse % PRIME
                    for key, coefficient in relation.items()
                    if coefficient * inverse % PRIME
                }
                output_basis[pivot] = (current, relation)
                break
            known_output, known_relation = known
            factor = current[pivot]
            for key, coefficient in known_output.items():
                updated = (
                    current.get(key, 0) - factor * coefficient
                ) % PRIME
                if updated:
                    current[key] = updated
                elif key in current:
                    del current[key]
            for key, coefficient in known_relation.items():
                updated = (
                    relation.get(key, 0) - factor * coefficient
                ) % PRIME
                if updated:
                    relation[key] = updated
                elif key in relation:
                    del relation[key]
        else:
            relations.append(relation)
    return len(output_basis), tuple(relations)


def decode(index: int) -> tuple[str, int, int]:
    if index < 15:
        return "s", index, -1
    shifted = index - 15
    return "f", shifted // 16, shifted % 16


def local_bilinear(value: Sequence[int]):
    factors = frame(value)
    coefficients = (character(value), -character(value))
    cache: dict[tuple[int, int], dict[int, int]] = {}

    def evaluate(left: int, right: int) -> dict[int, int]:
        if left > right:
            left, right = right, left
        key = (left, right)
        if key in cache:
            return cache[key]
        left_data = decode(left)
        right_data = decode(right)
        result: dict[int, int] = {}

        if left_data[0] == "s" and right_data[0] == "f":
            subset = SUBSETS[left_data[1]]
            label, variable = right_data[1], right_data[2]
            if label in subset:
                forms = [
                    {variable: 1} if index == label else factors[index]
                    for index in subset
                ]
                result = projected(multiply(forms))

        elif left_data[0] == "f" and right_data[0] == "f":
            left_label, left_variable = left_data[1], left_data[2]
            right_label, right_variable = right_data[1], right_data[2]
            if left_label != right_label:
                for scalar, subset in zip(
                    coefficients,
                    ACTIVE,
                    strict=True,
                ):
                    if (
                        left_label not in subset
                        or right_label not in subset
                    ):
                        continue
                    forms = []
                    for index in subset:
                        if index == left_label:
                            forms.append({left_variable: 1})
                        elif index == right_label:
                            forms.append({right_variable: 1})
                        else:
                            forms.append(factors[index])
                    add_scaled(
                        result,
                        scalar,
                        projected(multiply(forms)),
                    )

        cache[key] = result
        return result

    return evaluate


def curvature(
    left: Mapping[int, int],
    right: Mapping[int, int],
    caches,
) -> dict[int, int]:
    left_blocks: dict[int, list[tuple[int, int]]] = defaultdict(list)
    right_blocks: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for index, coefficient in left.items():
        left_blocks[index // LOCAL_WIDTH].append(
            (index % LOCAL_WIDTH, coefficient)
        )
    for index, coefficient in right.items():
        right_blocks[index // LOCAL_WIDTH].append(
            (index % LOCAL_WIDTH, coefficient)
        )

    result: dict[int, int] = {}
    for block in set(left_blocks) & set(right_blocks):
        evaluate = caches[block]
        for left_index, left_scalar in left_blocks[block]:
            for right_index, right_scalar in right_blocks[block]:
                add_scaled(
                    result,
                    left_scalar * right_scalar,
                    evaluate(left_index, right_index),
                )
    return result


def standard_atom(value: Sequence[int]) -> dict[int, int]:
    factors = frame(value)
    result: dict[int, int] = {}
    for scalar, subset in zip(
        (character(value), -character(value)),
        ACTIVE,
        strict=True,
    ):
        add_scaled(
            result,
            scalar,
            projected(multiply([factors[index] for index in subset])),
        )
    return result


def audit(missing_index: int, all_tangents) -> None:
    kept = [index for index in range(7) if index != missing_index]
    columns = [
        column for index in kept for column in all_tangents[index]
    ]
    full_rank, nullspace = kernel(columns)
    require(full_rank == 574, (missing_index, full_rank))
    require(len(nullspace) == 92, (missing_index, len(nullspace)))

    projected_tangent = ModularBasis()
    for column in columns:
        projected_tangent.add(projected(column))
    require(
        projected_tangent.rank == 108,
        (missing_index, projected_tangent.rank),
    )

    caches = [local_bilinear(RETAINED[index]) for index in kept]
    curvature_basis = ModularBasis()
    nonzero = 0
    pairs = 0
    for left_index in range(len(nullspace)):
        for right_index in range(left_index, len(nullspace)):
            pairs += 1
            value = curvature(
                nullspace[left_index],
                nullspace[right_index],
                caches,
            )
            if value:
                nonzero += 1
                curvature_basis.add(value)
            require(
                not projected_tangent.reduce(value),
                (missing_index, left_index, right_index),
            )

    require(pairs == 4_278, pairs)
    require(nonzero == 306, (missing_index, nonzero))
    require(
        curvature_basis.rank == 24,
        (missing_index, curvature_basis.rank),
    )
    require(
        projected_tangent.add(standard_atom(RETAINED[missing_index])),
        (missing_index, bits(RETAINED[missing_index])),
    )
    require(projected_tangent.rank == 109, projected_tangent.rank)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-core", default=EXPECTED_CORE)
    arguments = parser.parse_args()
    require(arguments.expected_core == EXPECTED_CORE, arguments.expected_core)

    all_tangents = tuple(tangent(value) for value in RETAINED)
    for missing_index in range(7):
        audit(missing_index, all_tangents)

    print(MARKER)
    print(EXPECTED_CORE)
    print(PRIME)


if __name__ == "__main__":
    main()
