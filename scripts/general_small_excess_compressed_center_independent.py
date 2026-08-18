#!/usr/bin/env python3
"""Independent replay of the small-excess compressed-center interface.

This file imports none of the primary matrix helpers.  It uses the explicit
``B=[I;V]`` / ``C=[I-WV|W]`` retraction model and a separate exact elimination
routine over ``Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Matrix = list[list[Fraction]]


def fail_unless(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def unit(size: int) -> Matrix:
    return [
        [Fraction(1 if row == column else 0) for column in range(size)]
        for row in range(size)
    ]


def blank(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def times(left: Matrix, right: Matrix) -> Matrix:
    fail_unless(left and right, "empty multiplication")
    fail_unless(len(left[0]) == len(right), (len(left[0]), len(right)))
    return [
        [
            sum(
                left[row][middle] * right[middle][column]
                for middle in range(len(right))
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def minus(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        ]
        for row in range(len(left))
    ]


def plus(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            left[row][column] + right[row][column]
            for column in range(len(left[0]))
        ]
        for row in range(len(left))
    ]


def flip(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix, strict=True)]


def exact_rank(matrix: Matrix) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot = 0
    column = 0
    while pivot < row_count and column < column_count:
        selected = None
        for row in range(pivot, row_count):
            if work[row][column]:
                selected = row
                break
        if selected is None:
            column += 1
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        pivot_value = work[pivot][column]
        for row in range(pivot + 1, row_count):
            if not work[row][column]:
                continue
            factor = work[row][column] / pivot_value
            for current in range(column, column_count):
                work[row][current] -= factor * work[pivot][current]
        pivot += 1
        column += 1
    return pivot


def positive_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first, *tail)


def explicit_injection_retraction(
    essential_dimension: int,
    kernel_dimension: int,
    seed: int,
) -> tuple[Matrix, Matrix]:
    if kernel_dimension == 0:
        return unit(essential_dimension), unit(essential_dimension)

    vertical = [
        [
            Fraction(((row + 2) * (column + 3) + seed) % 7 - 3)
            for column in range(essential_dimension)
        ]
        for row in range(kernel_dimension)
    ]
    correction = [
        [
            Fraction(((row + 1) * (column + 4) + 2 * seed) % 5 - 2)
            for column in range(kernel_dimension)
        ]
        for row in range(essential_dimension)
    ]

    injection = unit(essential_dimension) + vertical
    product = times(correction, vertical)
    left = minus(unit(essential_dimension), product)
    retraction = [
        [*left[row], *correction[row]]
        for row in range(essential_dimension)
    ]
    fail_unless(times(retraction, injection) == unit(essential_dimension), "CB")
    return injection, retraction


def coordinate_projection(total: int, start: int, size: int) -> Matrix:
    result = blank(total, total)
    for index in range(start, start + size):
        result[index][index] = Fraction(1)
    return result


def second_block_hessian(blocks: tuple[int, ...]) -> Matrix:
    total = sum(blocks)
    result = blank(total, total)
    offset = 0
    for block, size in enumerate(blocks):
        for row in range(size):
            for column in range(size):
                result[offset + row][offset + column] = Fraction(
                    (block + 2) * (row + 1) * (column + 1)
                    + row
                    + column
                    + (5 if row == column else 1)
                )
        offset += size
    return result


def replay_one(total: int, kernel: int, blocks: tuple[int, ...]) -> tuple[int, int, int]:
    essential = total - kernel
    injection, retraction = explicit_injection_retraction(
        essential,
        kernel,
        total + kernel + sum((i + 2) * b for i, b in enumerate(blocks)),
    )
    compression = times(injection, retraction)
    fail_unless(exact_rank(minus(unit(total), compression)) == kernel, "I-Q")

    projections: list[Matrix] = []
    operators: list[Matrix] = []
    start = 0
    for size in blocks:
        projection = coordinate_projection(total, start, size)
        projections.append(projection)
        operators.append(times(times(retraction, projection), injection))
        start += size

    accumulated = blank(essential, essential)
    for operator in operators:
        accumulated = plus(accumulated, operator)
    fail_unless(accumulated == unit(essential), "sum")

    lifted = second_block_hessian(blocks)
    hessian = times(times(flip(injection), lifted), injection)

    maximum_idempotence = 0
    maximum_center = 0
    ranks = []
    for index, operator in enumerate(operators):
        operator_rank = exact_rank(operator)
        ranks.append(operator_rank)
        fail_unless(operator_rank <= blocks[index], "rank cap")

        idempotence = exact_rank(minus(times(operator, operator), operator))
        maximum_idempotence = max(maximum_idempotence, idempotence)
        fail_unless(idempotence <= kernel, "idempotence")

        center = exact_rank(
            minus(
                times(hessian, operator),
                times(flip(operator), hessian),
            )
        )
        maximum_center = max(maximum_center, center)
        fail_unless(center <= 2 * kernel, "center")

        one_eigenspace = essential - exact_rank(minus(operator, unit(essential)))
        fail_unless(one_eigenspace == operator_rank - idempotence, "eigenspace")

    maximum_cross = 0
    for left, right in combinations(range(len(operators)), 2):
        for first, second in ((left, right), (right, left)):
            cross = exact_rank(times(operators[first], operators[second]))
            maximum_cross = max(maximum_cross, cross)
            fail_unless(cross <= kernel, "cross")

    fail_unless(0 <= sum(ranks) - essential <= kernel, "rank budget")
    return maximum_idempotence, maximum_cross, maximum_center


def main() -> int:
    cases = 0
    operator_checks = 0
    ordered_cross_checks = 0
    sharp_idempotence = False
    sharp_cross = False
    sharp_center = False

    for total in range(4, 9):
        for block_count in range(2, min(3, total) + 1):
            for blocks in positive_compositions(total, block_count):
                for kernel in range(0, min(2, total - 2) + 1):
                    idempotence, cross, center = replay_one(total, kernel, blocks)
                    cases += 1
                    operator_checks += block_count
                    ordered_cross_checks += block_count * (block_count - 1)
                    sharp_idempotence |= kernel > 0 and idempotence == kernel
                    sharp_cross |= kernel > 0 and cross == kernel
                    sharp_center |= kernel > 0 and center == 2 * kernel

    fail_unless(cases == 240, cases)
    fail_unless(operator_checks == 645, operator_checks)
    fail_unless(ordered_cross_checks == 1_140, ordered_cross_checks)
    fail_unless(sharp_idempotence, "no sharp idempotence witness")
    fail_unless(sharp_cross, "no sharp cross witness")
    fail_unless(sharp_center, "no sharp center witness")

    print(f"independent_matrix_cases={cases}")
    print(f"independent_operator_checks={operator_checks}")
    print(f"independent_ordered_cross_checks={ordered_cross_checks}")
    print("GENERAL_SMALL_EXCESS_COMPRESSED_CENTER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
