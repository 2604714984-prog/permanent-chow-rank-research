#!/usr/bin/env python3
"""Exact second-order local rigidity of the seven-block Glynn witness.

For each deleted standard summand, this script constructs the full first-order
map of the other six degree-six derivative blocks, lifts a complete modular
kernel to an exact rational kernel, and verifies that every polarized
second-order direction projects back into the projected tangent sum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
from typing import Callable, Mapping, Sequence

ORDER = 4
VARIABLE_COUNT = ORDER * ORDER
REFERENCE = (1, 1, 1, 1)
SIGNS = tuple((1,) + tail for tail in product((1, -1), repeat=3))
RETAINED = tuple(value for value in SIGNS if value != REFERENCE)
SOURCE_SUBSETS = tuple(combinations(range(6), 4))
ACTIVE_SUBSETS = ((0, 1, 2, 3), (0, 1, 4, 5))
PARAMETERS_PER_BLOCK = len(SOURCE_SUBSETS) + 6 * VARIABLE_COUNT
KERNEL_PRIME = 1_000_003
EXPECTED_CORE = "e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c"

MONOMIALS = tuple(combinations_with_replacement(range(VARIABLE_COUNT), 4))
MONOMIAL_INDEX = {value: index for index, value in enumerate(MONOMIALS)}
PROJECTED_INDEX = {
    tuple(
        sorted(row * ORDER + column for column, row in enumerate(rows))
    ): ((rows[0] * ORDER + rows[1]) * ORDER + rows[2]) * ORDER + rows[3]
    for rows in product(range(ORDER), repeat=ORDER)
}

SparseInt = dict[int, int]
SparseFraction = dict[int, Fraction]
Factor = dict[int, int]


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def character(value: Sequence[int]) -> int:
    result = 1
    for entry in value:
        result *= int(entry)
    return result


def sign_bits(value: Sequence[int]) -> int:
    result = 0
    for index, entry in enumerate(value[1:]):
        if entry == -1:
            result |= 1 << index
    return result


def factors_for(value: Sequence[int]) -> tuple[Factor, ...]:
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
            {row * ORDER + column: int(vector[row]) for row in range(ORDER)}
        )
    return tuple(result)


def multiply_forms(
    forms: Sequence[Mapping[int, int]],
) -> dict[tuple[int, ...], int]:
    polynomial: dict[tuple[int, ...], int] = {(): 1}
    for form in forms:
        updated: dict[tuple[int, ...], int] = defaultdict(int)
        for monomial, coefficient in polynomial.items():
            for variable, scalar in form.items():
                target = tuple(sorted(monomial + (variable,)))
                updated[target] += coefficient * scalar
        polynomial = {key: value for key, value in updated.items() if value}
    return polynomial


def full_vector(forms: Sequence[Mapping[int, int]]) -> SparseInt:
    return {
        MONOMIAL_INDEX[monomial]: coefficient
        for monomial, coefficient in multiply_forms(forms).items()
        if coefficient
    }


def projected_vector(forms: Sequence[Mapping[int, int]]) -> SparseInt:
    result: dict[int, int] = defaultdict(int)
    for monomial, coefficient in multiply_forms(forms).items():
        target = PROJECTED_INDEX.get(monomial)
        if target is not None:
            result[target] += coefficient
    return {key: value for key, value in result.items() if value}


def add_scaled(
    target: dict[int, int],
    scalar: int,
    value: Mapping[int, int],
) -> None:
    for index, coefficient in value.items():
        updated = target.get(index, 0) + scalar * coefficient
        if updated:
            target[index] = updated
        elif index in target:
            del target[index]


def source_column(
    factors: tuple[Factor, ...],
    subset: tuple[int, ...],
) -> SparseInt:
    return full_vector([factors[index] for index in subset])


def factor_column(
    factors: tuple[Factor, ...],
    value: Sequence[int],
    label: int,
    variable: int,
) -> SparseInt:
    result: dict[int, int] = {}
    for coefficient, subset in zip(
        (character(value), -character(value)),
        ACTIVE_SUBSETS,
        strict=True,
    ):
        if label not in subset:
            continue
        forms = [
            {variable: 1} if index == label else factors[index]
            for index in subset
        ]
        add_scaled(result, coefficient, full_vector(forms))
    return result


def tangent_columns(value: Sequence[int]) -> tuple[SparseInt, ...]:
    factors = factors_for(value)
    result = [
        source_column(factors, subset) for subset in SOURCE_SUBSETS
    ]
    for label in range(6):
        for variable in range(VARIABLE_COUNT):
            result.append(factor_column(factors, value, label, variable))
    require(len(result) == PARAMETERS_PER_BLOCK, len(result))
    return tuple(result)


def reduce_modular(
    vector: Mapping[int, int],
    basis: dict[int, tuple[dict[int, int], dict[int, int]]],
    combination: dict[int, int],
    prime: int,
) -> tuple[dict[int, int], dict[int, int]]:
    current = {
        index: coefficient % prime
        for index, coefficient in vector.items()
        if coefficient % prime
    }
    relation = {
        index: coefficient % prime
        for index, coefficient in combination.items()
        if coefficient % prime
    }
    while current:
        pivot = max(current)
        known = basis.get(pivot)
        if known is None:
            return current, relation
        known_vector, known_relation = known
        factor = current[pivot]
        for index, coefficient in known_vector.items():
            updated = (current.get(index, 0) - factor * coefficient) % prime
            if updated:
                current[index] = updated
            elif index in current:
                del current[index]
        for index, coefficient in known_relation.items():
            updated = (
                relation.get(index, 0) - factor * coefficient
            ) % prime
            if updated:
                relation[index] = updated
            elif index in relation:
                del relation[index]
    return current, relation


def modular_kernel(
    columns: Sequence[Mapping[int, int]],
    prime: int,
) -> tuple[int, tuple[dict[int, int], ...]]:
    basis: dict[int, tuple[dict[int, int], dict[int, int]]] = {}
    kernel = []
    for column_index, column in enumerate(columns):
        current, relation = reduce_modular(
            column,
            basis,
            {column_index: 1},
            prime,
        )
        if current:
            pivot = max(current)
            inverse = pow(current[pivot], prime - 2, prime)
            current = {
                index: coefficient * inverse % prime
                for index, coefficient in current.items()
                if coefficient * inverse % prime
            }
            relation = {
                index: coefficient * inverse % prime
                for index, coefficient in relation.items()
                if coefficient * inverse % prime
            }
            basis[pivot] = (current, relation)
        else:
            kernel.append(relation)
    return len(basis), tuple(kernel)


def lift_coefficient(value: int, prime: int) -> Fraction:
    signed = value if value <= prime // 2 else value - prime
    if abs(signed) <= 2:
        return Fraction(signed)
    inverse_two = (prime + 1) // 2
    if value == inverse_two:
        return Fraction(1, 2)
    if value == (prime - inverse_two) % prime:
        return Fraction(-1, 2)
    raise RuntimeError((value, prime))


def lift_kernel(
    modular_basis: Sequence[Mapping[int, int]],
    prime: int,
) -> tuple[SparseFraction, ...]:
    return tuple(
        {
            index: lift_coefficient(coefficient, prime)
            for index, coefficient in relation.items()
        }
        for relation in modular_basis
    )


def verify_exact_kernel(
    columns: Sequence[Mapping[int, int]],
    kernel: Sequence[Mapping[int, Fraction]],
) -> None:
    for relation_index, relation in enumerate(kernel):
        result: dict[int, Fraction] = defaultdict(Fraction)
        for column_index, scalar in relation.items():
            for row, coefficient in columns[column_index].items():
                result[row] += scalar * coefficient
        require(
            not any(result.values()),
            (
                relation_index,
                {key: value for key, value in result.items() if value},
            ),
        )


def project_full(value: Mapping[int, int]) -> SparseInt:
    result: dict[int, int] = defaultdict(int)
    for monomial_index, coefficient in value.items():
        target = PROJECTED_INDEX.get(MONOMIALS[monomial_index])
        if target is not None:
            result[target] += coefficient
    return {
        key: coefficient for key, coefficient in result.items() if coefficient
    }


class RationalSparseBasis:
    def __init__(self) -> None:
        self._basis: dict[int, SparseFraction] = {}

    @property
    def rank(self) -> int:
        return len(self._basis)

    def reduce(
        self,
        value: Mapping[int, int | Fraction],
    ) -> SparseFraction:
        current = {
            index: Fraction(coefficient)
            for index, coefficient in value.items()
            if coefficient
        }
        while current:
            pivot = max(current)
            known = self._basis.get(pivot)
            if known is None:
                return current
            factor = current[pivot]
            for index, coefficient in known.items():
                updated = (
                    current.get(index, Fraction()) - factor * coefficient
                )
                if updated:
                    current[index] = updated
                elif index in current:
                    del current[index]
        return {}

    def add(self, value: Mapping[int, int | Fraction]) -> bool:
        current = self.reduce(value)
        if not current:
            return False
        pivot = max(current)
        scale = current[pivot]
        self._basis[pivot] = {
            index: coefficient / scale
            for index, coefficient in current.items()
            if coefficient / scale
        }
        return True


def decode_parameter(index: int) -> tuple[str, int, int | None]:
    if index < len(SOURCE_SUBSETS):
        return "source", index, None
    shifted = index - len(SOURCE_SUBSETS)
    return (
        "factor",
        shifted // VARIABLE_COUNT,
        shifted % VARIABLE_COUNT,
    )


def bilinear_cache(
    value: Sequence[int],
) -> Callable[[int, int], SparseInt]:
    factors = factors_for(value)
    coefficients = (character(value), -character(value))
    cache: dict[tuple[int, int], SparseInt] = {}

    def evaluate(left: int, right: int) -> SparseInt:
        if left > right:
            left, right = right, left
        key = (left, right)
        if key in cache:
            return cache[key]
        left_data = decode_parameter(left)
        right_data = decode_parameter(right)
        result: dict[int, int] = {}

        if left_data[0] == "source" and right_data[0] == "factor":
            subset = SOURCE_SUBSETS[left_data[1]]
            label = right_data[1]
            variable = int(right_data[2])
            if label in subset:
                forms = [
                    {variable: 1} if index == label else factors[index]
                    for index in subset
                ]
                result = projected_vector(forms)

        elif left_data[0] == "factor" and right_data[0] == "factor":
            left_label = left_data[1]
            left_variable = int(left_data[2])
            right_label = right_data[1]
            right_variable = int(right_data[2])
            if left_label != right_label:
                for coefficient, subset in zip(
                    coefficients,
                    ACTIVE_SUBSETS,
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
                        coefficient,
                        projected_vector(forms),
                    )

        cache[key] = result
        return result

    return evaluate


def bilinear_value(
    left: Mapping[int, Fraction],
    right: Mapping[int, Fraction],
    caches: Sequence[Callable[[int, int], SparseInt]],
) -> SparseFraction:
    left_by_block: dict[int, list[tuple[int, Fraction]]] = defaultdict(list)
    right_by_block: dict[int, list[tuple[int, Fraction]]] = defaultdict(list)
    for index, coefficient in left.items():
        left_by_block[index // PARAMETERS_PER_BLOCK].append(
            (index % PARAMETERS_PER_BLOCK, coefficient)
        )
    for index, coefficient in right.items():
        right_by_block[index // PARAMETERS_PER_BLOCK].append(
            (index % PARAMETERS_PER_BLOCK, coefficient)
        )

    result: dict[int, Fraction] = defaultdict(Fraction)
    for block in set(left_by_block) & set(right_by_block):
        cache = caches[block]
        for left_index, left_coefficient in left_by_block[block]:
            for right_index, right_coefficient in right_by_block[block]:
                scalar = left_coefficient * right_coefficient
                for target, coefficient in cache(
                    left_index,
                    right_index,
                ).items():
                    result[target] += scalar * coefficient
    return {key: value for key, value in result.items() if value}


def atom(value: Sequence[int]) -> SparseInt:
    factors = factors_for(value)
    result: dict[int, int] = {}
    for coefficient, subset in zip(
        (character(value), -character(value)),
        ACTIVE_SUBSETS,
        strict=True,
    ):
        add_scaled(
            result,
            coefficient,
            projected_vector([factors[index] for index in subset]),
        )
    return result


def audit_deletion(
    missing_index: int,
    all_columns: Sequence[Sequence[SparseInt]],
) -> dict[str, object]:
    kept_indices = [
        index for index in range(len(RETAINED)) if index != missing_index
    ]
    columns = [
        column for index in kept_indices for column in all_columns[index]
    ]
    full_rank, modular_basis = modular_kernel(columns, KERNEL_PRIME)
    kernel = lift_kernel(modular_basis, KERNEL_PRIME)
    verify_exact_kernel(columns, kernel)

    require(full_rank == 574, (missing_index, full_rank))
    require(len(kernel) == 92, (missing_index, len(kernel)))

    tangent = RationalSparseBasis()
    for column in columns:
        tangent.add(project_full(column))
    require(tangent.rank == 108, (missing_index, tangent.rank))

    caches = [bilinear_cache(RETAINED[index]) for index in kept_indices]
    curvature = RationalSparseBasis()
    nonzero_pairs = 0
    pair_count = 0
    for left_index in range(len(kernel)):
        for right_index in range(left_index, len(kernel)):
            pair_count += 1
            value = bilinear_value(
                kernel[left_index],
                kernel[right_index],
                caches,
            )
            if value:
                nonzero_pairs += 1
                curvature.add(value)
            require(
                not tangent.reduce(value),
                (missing_index, left_index, right_index),
            )

    require(pair_count == 4_278, pair_count)
    require(nonzero_pairs == 306, (missing_index, nonzero_pairs))
    require(curvature.rank == 24, (missing_index, curvature.rank))

    missing_remainder = tangent.reduce(atom(RETAINED[missing_index]))
    require(missing_remainder, missing_index)

    coefficient_set = sorted(
        {
            str(coefficient)
            for relation in kernel
            for coefficient in relation.values()
        }
    )
    support_patterns = Counter(
        tuple(
            sorted(
                {
                    index // PARAMETERS_PER_BLOCK
                    for index in relation
                }
            )
        )
        for relation in kernel
    )

    return {
        "missing_sign_bits": sign_bits(RETAINED[missing_index]),
        "missing_hamming_weight": sign_bits(
            RETAINED[missing_index]
        ).bit_count(),
        "full_first_order_rank": full_rank,
        "full_first_order_kernel_dimension": len(kernel),
        "projected_tangent_rank": tangent.rank,
        "kernel_pair_count": pair_count,
        "nonzero_polarized_curvature_pairs": nonzero_pairs,
        "curvature_span_rank": curvature.rank,
        "curvature_quotient_rank": 0,
        "missing_summand_outside_projected_tangent": True,
        "missing_remainder_support": len(missing_remainder),
        "kernel_coefficient_set": coefficient_set,
        "kernel_support_pattern_counts": {
            str(pattern): count
            for pattern, count in sorted(support_patterns.items())
        },
    }


def build_core() -> dict[str, object]:
    all_columns = tuple(tangent_columns(value) for value in RETAINED)
    deletion_checks = [
        audit_deletion(missing_index, all_columns)
        for missing_index in range(len(RETAINED))
    ]

    require(
        all(
            check["full_first_order_rank"] == 574
            for check in deletion_checks
        ),
        deletion_checks,
    )
    require(
        all(
            check["curvature_quotient_rank"] == 0
            for check in deletion_checks
        ),
        deletion_checks,
    )

    return {
        "schema": "general_seven_block_glynn_second_order_rigidity/v1",
        "classification": "STRICT_LOCAL_SECOND_ORDER_ROUTE_BARRIER",
        "field": "characteristic_zero",
        "standard_witness": {
            "retained_summands": 7,
            "inherited_witness_core": "045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e",
            "first_order_local_rigidity_core": "7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710",
        },
        "parameter_model": {
            "source_parameters_per_block": len(SOURCE_SUBSETS),
            "factor_parameters_per_block": 6 * VARIABLE_COUNT,
            "total_parameters_per_block": PARAMETERS_PER_BLOCK,
            "six_block_parameter_count": 6 * PARAMETERS_PER_BLOCK,
            "full_degree_four_ambient_dimension": len(MONOMIALS),
            "projected_column_multidegree_dimension": len(PROJECTED_INDEX),
            "kernel_prime": KERNEL_PRIME,
        },
        "uniform_exact_data": {
            "full_first_order_rank": 574,
            "full_first_order_kernel_dimension": 92,
            "projected_tangent_rank": 108,
            "kernel_pair_count": 4_278,
            "nonzero_polarized_curvature_pairs": 306,
            "curvature_span_rank": 24,
            "curvature_quotient_rank": 0,
            "missing_augmented_projected_rank": 109,
        },
        "deletion_checks": deletion_checks,
        "conclusion": {
            "first_order_absorption": "IMPOSSIBLE",
            "second_order_absorption": "IMPOSSIBLE",
            "standard_seven_block_witness_locally_six_irreducible_through_order_two": True,
        },
        "claim_boundary": {
            "global_six_block_literal_sum": "OPEN",
            "third_or_higher_order_coalescence": "NOT_EXCLUDED",
            "remote_or_singular_six_block_witness": "NOT_EXCLUDED",
            "mu_6_4": "OPEN_IN_[6,7]",
            "unrestricted_chow_rank_improvement": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--print-core-only", action="store_true")
    arguments = parser.parse_args()

    core = build_core()
    digest = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    require(digest == EXPECTED_CORE, digest)
    payload = dict(core)
    payload["core_sha256"] = digest
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.print_core_only:
        print(digest)
    else:
        print("GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_PASS")
        print(digest)


if __name__ == "__main__":
    main()
