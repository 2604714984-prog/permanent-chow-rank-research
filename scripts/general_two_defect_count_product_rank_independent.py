#!/usr/bin/env python3
"""Independent replay of the finite interfaces in G-021.

This file does not import the primary audit. It builds the local sign truth
tables directly on three row values, performs its own exact elimination, and
replays the ``n=6`` construction and Fourier identity.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

PATTERNS = {
    "1": (1, 1, 1),
    "A": (1, -1, 1),
    "B": (1, 1, -1),
    "C": (1, -1, -1),
}
NONCONSTANT = ("A", "B", "C")
TARGET_PURE = (Fraction(0), Fraction(1), Fraction(1), Fraction(0))


def anova_column(left: str, right: str) -> tuple[Fraction, ...]:
    def value(i: int, j: int) -> Fraction:
        return Fraction(PATTERNS[left][i] * PATTERNS[right][j])

    constant = value(0, 0)
    left_unary = (value(1, 0) - constant, value(2, 0) - constant)
    right_unary = (value(0, 1) - constant, value(0, 2) - constant)
    pure = tuple(
        value(i, j) - value(i, 0) - value(0, j) + constant
        for i in (1, 2)
        for j in (1, 2)
    )
    return pure + left_unary + right_unary + (constant,)


ATOM_LABELS = tuple(product(NONCONSTANT, repeat=2))
COLUMNS = tuple(anova_column(left, right) for left, right in ATOM_LABELS)


def solve(columns: list[tuple[Fraction, ...]], target: tuple[Fraction, ...]):
    m, n = len(target), len(columns)
    a = [[columns[j][i] for j in range(n)] + [target[i]] for i in range(m)]
    row = 0
    pivots: list[int] = []
    for col in range(n):
        pivot = next((i for i in range(row, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [value / scale for value in a[row]]
        for i in range(m):
            if i != row and a[i][col]:
                q = a[i][col]
                a[i] = [a[i][j] - q * a[row][j] for j in range(n + 1)]
        pivots.append(col)
        row += 1
        if row == m:
            break
    if any(all(a[i][j] == 0 for j in range(n)) and a[i][n] for i in range(m)):
        return None
    free = [j for j in range(n) if j not in pivots]
    solution = [Fraction(0)] * n
    for i, col in enumerate(pivots):
        solution[col] = a[i][n]
    kernel = []
    for f in free:
        vector = [Fraction(0)] * n
        vector[f] = 1
        for i, col in enumerate(pivots):
            vector[col] = -a[i][f]
        kernel.append(tuple(vector))
    return tuple(solution), tuple(kernel)


def finite_catalog() -> dict[str, object]:
    counts: Counter[int] = Counter()
    genuine: Counter[int] = Counter()
    left_hist: Counter[tuple[Fraction, Fraction]] = Counter()
    right_hist: Counter[tuple[Fraction, Fraction]] = Counter()
    unique_two = None

    for size in (1, 2, 3):
        for support in combinations(range(9), size):
            result = solve([COLUMNS[index][:4] for index in support], TARGET_PURE)
            if result is None:
                continue
            coefficients, kernel = result
            if kernel:
                raise AssertionError((support, kernel))
            counts[size] += 1
            if all(coefficients):
                genuine[size] += 1
            left = tuple(
                sum(coefficients[i] * COLUMNS[index][4 + coordinate] for i, index in enumerate(support))
                for coordinate in range(2)
            )
            right = tuple(
                sum(coefficients[i] * COLUMNS[index][6 + coordinate] for i, index in enumerate(support))
                for coordinate in range(2)
            )
            if size == 2 and all(coefficients):
                unique_two = (support, coefficients, left, right)
            if size == 3:
                left_hist[left] += 1
                right_hist[right] += 1

    expected = Counter(
        {
            (Fraction(-1, 2), Fraction(-1, 2)): 9,
            (Fraction(0), Fraction(-1, 2)): 3,
            (Fraction(-1, 2), Fraction(0)): 3,
            (Fraction(0), Fraction(0)): 1,
            (Fraction(-1), Fraction(-1, 2)): 1,
            (Fraction(-1, 2), Fraction(-1)): 1,
        }
    )
    if counts != Counter({3: 18, 2: 1}):
        raise AssertionError(counts)
    if genuine != Counter({3: 11, 2: 1}):
        raise AssertionError(genuine)
    if left_hist != expected or right_hist != expected:
        raise AssertionError((left_hist, right_hist))
    if unique_two is None:
        raise AssertionError("missing two-atom expression")

    return {
        "compatible": {str(size): counts[size] for size in (1, 2, 3)},
        "genuine": {str(size): genuine[size] for size in (1, 2, 3)},
        "unique_two_support": [list(ATOM_LABELS[index]) for index in unique_two[0]],
        "unique_two_coefficients": [str(value) for value in unique_two[1]],
        "left_histogram": {f"{x},{y}": count for (x, y), count in sorted(left_hist.items())},
        "right_histogram": {f"{x},{y}": count for (x, y), count in sorted(right_hist.items())},
    }


def equal_unary_catalog(endpoint_offset: int) -> Counter[Fraction]:
    t_column = (Fraction(0),) * 4 + (Fraction(-1), Fraction(-1))
    target = TARGET_PURE + (Fraction(0), Fraction(0))
    histogram: Counter[Fraction] = Counter()
    for size in range(1, 5):
        for support in combinations(range(9), size):
            columns = [
                COLUMNS[index][:4] + COLUMNS[index][endpoint_offset : endpoint_offset + 2]
                for index in support
            ] + [t_column]
            result = solve(columns, target)
            if result is None:
                continue
            solution, kernel = result
            if any(vector[-1] for vector in kernel):
                raise AssertionError((support, solution, kernel))
            histogram[solution[-1]] += 1
    expected = Counter({Fraction(-1, 2): 42, Fraction(0): 10})
    if histogram != expected:
        raise AssertionError(histogram)
    return histogram


def sign(label: int, row: int) -> int:
    return 1 if row == 0 or not ((label >> (row - 1)) & 1) else -1


def character(left: int, right: int) -> int:
    return -1 if (left & right).bit_count() & 1 else 1


def parity(assignment: tuple[int, ...]) -> int:
    value = 0
    for row in assignment:
        if row:
            value ^= 1 << (row - 1)
    return value


def n6_replay() -> int:
    n, a, b = 6, 4, 5
    la, lb, lab = 8, 16, 24
    target_parity, zero_parity = 31, 7
    checks = 0
    for assignment in product(range(n), repeat=n):
        g = assignment.count(a) * assignment.count(b)
        value = Fraction(0)
        for j, k in combinations(range(n), 2):
            value += Fraction(1, 4) * sign(la, assignment[j]) * sign(lb, assignment[k])
            value += Fraction(1, 4) * sign(lb, assignment[j]) * sign(la, assignment[k])
        for j in range(n):
            value -= Fraction(5, 4) * sign(lab, assignment[j])
        if value != g:
            raise AssertionError((assignment, value, g))
        p = parity(assignment)
        aggregate = sum(
            Fraction(
                character(p, base)
                * (character(target_parity, base) - character(zero_parity, base)),
                32,
            )
            * g
            for base in range(32)
        )
        expected = Fraction(int(tuple(sorted(assignment)) == tuple(range(n))))
        if aggregate != expected:
            raise AssertionError((assignment, aggregate, expected))
        checks += 1
    return checks


def main() -> int:
    catalog = finite_catalog()
    left = equal_unary_catalog(4)
    right = equal_unary_catalog(6)
    checks = n6_replay()
    payload = {
        "status": "GENERAL_TWO_DEFECT_COUNT_PRODUCT_INDEPENDENT_AUDIT_PASS",
        "local_catalog": catalog,
        "left_equal_unary_histogram": {str(value): count for value, count in sorted(left.items())},
        "right_equal_unary_histogram": {str(value): count for value, count in sorted(right.items())},
        "n6_assignment_checks": checks,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("GENERAL_TWO_DEFECT_COUNT_PRODUCT_INDEPENDENT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
