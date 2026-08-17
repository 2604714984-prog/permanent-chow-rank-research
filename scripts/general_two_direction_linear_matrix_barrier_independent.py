#!/usr/bin/env python3
"""Independent finite replay for canonical 2 x 2 linear pencils.

This implementation imports none of the primary audit.  It uses a second prime,
a smaller independent coefficient cube, and direct canonical Boolean matrices.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb


PRIME = 1_000_033
EXPECTED_OVERALL = {3: 3, 4: 7, 5: 10, 6: 20, 7: 35, 8: 75, 9: 126, 10: 252}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def subsets(n: int, degree: int) -> list[frozenset[int]]:
    if not 0 <= degree <= n:
        return []
    return [frozenset(value) for value in combinations(range(n), degree)]


def multiplication_columns(
    n: int,
    source_degree: int,
    coefficients: list[int],
) -> list[list[int]]:
    source = subsets(n, source_degree)
    target = subsets(n, source_degree + 1)
    columns: list[list[int]] = []
    for lower in source:
        column = []
        for upper in target:
            difference = upper - lower
            if lower <= upper and len(difference) == 1:
                variable = next(iter(difference))
                column.append(coefficients[variable])
            else:
                column.append(0)
        columns.append(column)
    return columns


def column_rank(columns: list[list[int]], prime: int = PRIME) -> int:
    if not columns:
        return 0
    basis: dict[int, list[int]] = {}
    for original in columns:
        vector = [value % prime for value in original]
        while True:
            pivot = next((index for index, value in enumerate(vector) if value), None)
            if pivot is None:
                break
            if pivot not in basis:
                inverse = pow(vector[pivot], prime - 2, prime)
                basis[pivot] = [(value * inverse) % prime for value in vector]
                break
            factor = vector[pivot]
            vector = [
                (left - factor * right) % prime
                for left, right in zip(vector, basis[pivot])
            ]
    return len(basis)


def concatenate_domain(
    first: list[list[int]],
    second: list[list[int]],
) -> list[list[int]]:
    return first + second


def direct_sum_codomain(
    first: list[list[int]],
    second: list[list[int]],
) -> list[list[int]]:
    if not first:
        return []
    row_count = len(first[0])
    result = []
    for column in first:
        result.append(column + [0] * row_count)
    for column in second:
        result.append([0] * row_count + column)
    return result


def vertical_column_map(
    first: list[list[int]],
    second: list[list[int]],
) -> list[list[int]]:
    require(len(first) == len(second), (len(first), len(second)))
    return [left + right for left, right in zip(first, second)]


def det_coefficients(values: tuple[int, ...]) -> tuple[int, int, int]:
    a, b, c, d, e, f, g, h = values
    return (
        a * d - b * c,
        a * h + e * d - b * g - f * c,
        e * h - f * g,
    )


def proportional(vectors: list[tuple[int, int]]) -> bool:
    return all(
        left[0] * right[1] == left[1] * right[0]
        for index, left in enumerate(vectors)
        for right in vectors[index + 1 :]
    )


def independent_singular_classification_checks() -> int:
    checks = 0
    for values in product((0, 1), repeat=8):
        if any(det_coefficients(values)):
            checks += 1
            continue

        left = values[:4]
        right = values[4:]
        dependent = all(
            left[i] * right[j] == left[j] * right[i]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        if dependent:
            checks += 1
            continue

        columns = [(left[0], left[2]), (left[1], left[3]), (right[0], right[2]), (right[1], right[3])]
        rows = [(left[0], left[1]), (left[2], left[3]), (right[0], right[1]), (right[2], right[3])]
        require(proportional(columns) != proportional(rows), values)
        checks += 1

    require(checks == 2**8, checks)
    return checks


def primitive_hilbert(size: int) -> list[int]:
    previous = 0
    result = []
    for degree in range(size // 2 + 1):
        current = comb(size, degree)
        result.append(current - previous)
        previous = current
    return result


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def maximal_ceiling(n: int) -> int:
    first = n // 2
    second = n - first
    quotient = convolution(primitive_hilbert(first), primitive_hilbert(second))
    values = []
    for degree in range(1, n + 1):
        source = comb(n, degree - 1)
        target = comb(n, degree)
        quotient_dimension = quotient[degree] if degree < len(quotient) else 0
        denominator = max(min(source, target), target - quotient_dimension)
        numerator = min(target * target, 2 * source * source)
        values.append(-(-numerator // denominator))
    return max(values)


def main() -> int:
    classification_checks = independent_singular_classification_checks()
    canonical_cells = 0
    duality_cells = 0

    for n in range(2, 8):
        lefschetz = [1] * n
        split_first = [1 if index < n // 2 else 0 for index in range(n)]
        split_second = [1 if index >= n // 2 else 0 for index in range(n)]

        for degree in range(1, n + 1):
            source = comb(n, degree - 1)
            target = comb(n, degree)
            expected = min(source, target)
            linear = multiplication_columns(n, degree - 1, lefschetz)

            # Regular witness: s=L, t=0 in [[s,t],[-t,s]].
            regular = direct_sum_codomain(linear, linear)
            require(column_rank(regular) == 2 * expected, (n, degree, "regular"))

            # Principal witness: diag(L,0).
            require(column_rank(linear) == expected, (n, degree, "principal"))
            canonical_cells += 2

            first_columns = multiplication_columns(n, degree - 1, split_first)
            second_columns = multiplication_columns(n, degree - 1, split_second)
            column_map = vertical_column_map(first_columns, second_columns)
            column_value = column_rank(column_map)

            complementary = n - degree + 1
            first_complement = multiplication_columns(n, complementary - 1, split_first)
            second_complement = multiplication_columns(n, complementary - 1, split_second)
            row_map = concatenate_domain(first_complement, second_complement)
            row_value = column_rank(row_map)
            require(column_value == row_value, (n, degree, column_value, row_value))
            duality_cells += 1

    require(canonical_cells == 54, canonical_cells)
    require(duality_cells == 27, duality_cells)

    observed = {n: maximal_ceiling(n) for n in range(3, 11)}
    require(observed == EXPECTED_OVERALL, observed)

    print(f"independent_small_pencil_checks={classification_checks}")
    print(f"independent_regular_principal_cells={canonical_cells}")
    print(f"independent_gorenstein_duality_cells={duality_cells}")
    print("independent_overall_ceilings=3,7,10,20,35,75,126,252")
    print("GENERAL_TWO_DIRECTION_LINEAR_MATRIX_BARRIER_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
