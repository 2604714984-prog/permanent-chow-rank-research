#!/usr/bin/env python3
"""Independent modular replay of cubic apolar generators for one relations."""

from __future__ import annotations

from math import comb

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


def falling(value: int, order: int) -> int:
    result = 1
    for offset in range(order):
        result *= value - offset
    return result


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def nullspace_mod(matrix: list[list[int]], prime: int = PRIME) -> list[list[int]]:
    if not matrix:
        return []
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[entry % prime for entry in row] for row in matrix]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], prime - 2, prime)
        work[pivot_row] = [
            (entry * inverse) % prime for entry in work[pivot_row]
        ]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[pivot_row], strict=True)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break

    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(columns) if column not in pivot_set]
    basis: list[list[int]] = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = (-work[row][free]) % prime
        basis.append(vector)
    return basis


def derivative_matrix(n: int, support_size: int, degree: int):
    r = n - 1
    operators = tuple(compositions(degree, r))
    terms = []
    for special in range(support_size):
        exponent = [1] * r
        exponent[special] += 1
        terms.append(tuple(exponent))

    columns = []
    output_support = set()
    for operator in operators:
        value: dict[tuple[int, ...], int] = {}
        for exponent in terms:
            if any(order > power for order, power in zip(operator, exponent, strict=True)):
                continue
            coefficient = 1
            output = []
            for power, order in zip(exponent, operator, strict=True):
                coefficient *= falling(power, order)
                output.append(power - order)
            key = tuple(output)
            value[key] = (value.get(key, 0) + coefficient) % PRIME
        value = {key: coefficient for key, coefficient in value.items() if coefficient}
        output_support.update(value)
        columns.append(value)

    rows = tuple(sorted(output_support))
    row_index = {value: index for index, value in enumerate(rows)}
    matrix = [[0] * len(operators) for _ in rows]
    for column, value in enumerate(columns):
        for output, coefficient in value.items():
            matrix[row_index[output]][column] = coefficient
    return operators, matrix


def expected(support_size: int) -> int:
    if support_size <= 2:
        return 1
    if support_size == 3:
        return 7
    return comb(support_size + 1, 2)


def replay(n: int, support_size: int) -> dict[str, int]:
    r = n - 1
    degree_two, matrix_two = derivative_matrix(n, support_size, 2)
    degree_three, matrix_three = derivative_matrix(n, support_size, 3)
    kernel_two = nullspace_mod(matrix_two)
    kernel_three_dimension = len(degree_three) - rank_mod(matrix_three)
    degree_three_index = {
        exponent: index for index, exponent in enumerate(degree_three)
    }

    product_columns: list[list[int]] = []
    for relation in kernel_two:
        for variable in range(r):
            product = [0] * len(degree_three)
            for coefficient, exponent in zip(relation, degree_two, strict=True):
                if not coefficient:
                    continue
                lifted = list(exponent)
                lifted[variable] += 1
                product[degree_three_index[tuple(lifted)]] = (
                    product[degree_three_index[tuple(lifted)]] + coefficient
                ) % PRIME
            product_columns.append(product)

    if product_columns:
        product_matrix = [
            [column[row] for column in product_columns]
            for row in range(len(degree_three))
        ]
        generated_cubics = rank_mod(product_matrix)
    else:
        generated_cubics = 0

    minimal_cubics = kernel_three_dimension - generated_cubics
    require(minimal_cubics == expected(support_size), (n, support_size, minimal_cubics))
    return {
        "n": n,
        "support_size": support_size,
        "quadratic_ideal_dimension": len(kernel_two),
        "cubic_ideal_dimension": kernel_three_dimension,
        "linear_times_quadrics_rank": generated_cubics,
        "minimal_cubic_generators": minimal_cubics,
    }


def main() -> None:
    rows = [
        replay(n, support_size)
        for n in range(5, 10)
        for support_size in range(1, n)
    ]
    require(len(rows) == sum(n - 1 for n in range(5, 10)), len(rows))
    print("GENERAL_FULL_QUOTIENT_KOSZUL_CUBIC_DUALITY_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
