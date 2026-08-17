#!/usr/bin/env python3
"""Independent replay of the apolar multiplication-tensor framework.

This implementation imports none of the primary audit. It reconstructs the
same finite interfaces with modular catalecticants, squarefree top pairings,
and a separately written permanent multiplication table.
"""

from __future__ import annotations

from math import comb, factorial


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first, *tail)


def rank_mod(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows = [[value % PRIME for value in row] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [value * inverse % PRIME for value in rows[rank]]
        for index in range(row_count):
            if index == rank or not rows[index][column]:
                continue
            factor = rows[index][column]
            rows[index] = [
                (rows[index][entry] - factor * rows[rank][entry]) % PRIME
                for entry in range(column_count)
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def polynomial_product(factors):
    variable_count = len(factors[0])
    result = {(0,) * variable_count: 1}
    for factor in factors:
        updated = {}
        for exponent, coefficient in result.items():
            for variable, scalar in enumerate(factor):
                if not scalar:
                    continue
                target = list(exponent)
                target[variable] += 1
                target_tuple = tuple(target)
                updated[target_tuple] = (
                    updated.get(target_tuple, 0) + coefficient * scalar
                ) % PRIME
        result = updated
    return result


def catalecticant_rank(polynomial, variable_count, total_degree, degree):
    source = tuple(compositions(degree, variable_count))
    target = tuple(compositions(total_degree - degree, variable_count))
    matrix = []
    for remaining in target:
        row = []
        for derivative in source:
            full = tuple(
                remaining[index] + derivative[index]
                for index in range(variable_count)
            )
            coefficient = polynomial.get(full, 0)
            factor = 1
            for full_power, remaining_power in zip(full, remaining, strict=True):
                factor *= factorial(full_power) // factorial(remaining_power)
            row.append(coefficient * factor % PRIME)
        matrix.append(row)
    return rank_mod(matrix)


def psi_matrix(factors, degree):
    n = len(factors)
    variable_count = len(factors[0])
    masks = [mask for mask in range(1 << n) if mask.bit_count() == degree]
    mask_index = {mask: index for index, mask in enumerate(masks)}
    columns = []
    for monomial in compositions(degree, variable_count):
        state = {0: 1}
        for variable, count in enumerate(monomial):
            coefficients = [factor[variable] for factor in factors]
            for _ in range(count):
                updated = {}
                for mask, value in state.items():
                    for factor_index, scalar in enumerate(coefficients):
                        bit = 1 << factor_index
                        if scalar and not mask & bit:
                            updated[mask | bit] = (
                                updated.get(mask | bit, 0) + value * scalar
                            ) % PRIME
                state = updated
        column = [0] * len(masks)
        for mask, value in state.items():
            if mask in mask_index:
                column[mask_index[mask]] = value
        columns.append(column)
    return masks, columns


def column_basis(columns):
    if not columns:
        return []
    selected = []
    current = [[] for _ in range(len(columns[0]))]
    current_rank = 0
    for column in columns:
        candidate = [
            [*current[row], column[row]] for row in range(len(current))
        ]
        candidate_rank = rank_mod(candidate)
        if candidate_rank > current_rank:
            selected.append(column)
            current = candidate
            current_rank = candidate_rank
    return selected


def pairing_rank(factors, degree):
    n = len(factors)
    left_masks, left_columns = psi_matrix(factors, degree)
    right_masks, right_columns = psi_matrix(factors, n - degree)
    left_basis = column_basis(left_columns)
    right_basis = column_basis(right_columns)
    right_index = {mask: index for index, mask in enumerate(right_masks)}
    full = (1 << n) - 1
    pairing = []
    for left in left_basis:
        row = []
        for right in right_basis:
            value = 0
            for index, mask in enumerate(left_masks):
                value += left[index] * right[right_index[full ^ mask]]
            row.append(value % PRIME)
        pairing.append(row)
    return rank_mod(pairing)


def permanent_multiply(left, right):
    if left[0] & right[0] or left[1] & right[1]:
        return None
    return left[0] | right[0], left[1] | right[1]


def main() -> int:
    examples = (
        ((1,), (1,), (1,), (1,), (1,)),
        ((1, 0), (0, 1), (1, 2), (2, 1)),
        ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)),
        (
            (1, 0, 0, 0, 0),
            (0, 1, 0, 0, 0),
            (0, 0, 1, 0, 0),
            (0, 0, 0, 1, 0),
            (0, 0, 0, 0, 1),
        ),
    )

    pairing_checks = 0
    for factors in examples:
        n = len(factors)
        variable_count = len(factors[0])
        polynomial = polynomial_product(factors)
        hilbert = []
        for degree in range(n + 1):
            direct = catalecticant_rank(polynomial, variable_count, n, degree)
            paired = pairing_rank(factors, degree)
            require(direct == paired, (factors, degree, direct, paired))
            hilbert.append(direct)
            pairing_checks += 1
        require(hilbert == list(reversed(hilbert)), hilbert)
        require(sum(hilbert) <= 2**n, hilbert)

    multiplication_checks = 0
    for n in range(1, 7):
        levels = []
        for degree in range(n + 1):
            masks = [mask for mask in range(1 << n) if mask.bit_count() == degree]
            levels.extend((row, column) for row in masks for column in masks)
        require(len(levels) == comb(2 * n, n), (n, len(levels)))
        sample = levels[: min(160, len(levels))]
        for left in sample:
            for right in sample:
                product = permanent_multiply(left, right)
                if product is not None:
                    require(product[0].bit_count() == product[1].bit_count(), product)
                multiplication_checks += 1

    arithmetic_checks = 0
    for n in range(1, 51):
        dimension = comb(2 * n, n)
        border_bound = -(-dimension // (2**n))
        central = comb(n, n // 2)
        require(border_bound <= central, (n, border_bound, central))
        ordinary_upper = (n + 2) * 2 ** (n - 1)
        ordinary_bound = -(-(2 * dimension - 1) // ordinary_upper)
        require(ordinary_bound <= border_bound, (n, ordinary_bound))
        require(-(-(2 * dimension - 1) // (3**n)) <= ordinary_bound, n)
        arithmetic_checks += 3

    require(pairing_checks == 23, pairing_checks)
    require(multiplication_checks == 56_540, multiplication_checks)
    require(arithmetic_checks == 150, arithmetic_checks)

    print(f"independent_boolean_pairing_checks={pairing_checks}")
    print(f"independent_permanent_multiplication_checks={multiplication_checks}")
    print(f"independent_bound_arithmetic_checks={arithmetic_checks}")
    print("GENERAL_APOLAR_MULTIPLICATION_TENSOR_FRAMEWORK_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
