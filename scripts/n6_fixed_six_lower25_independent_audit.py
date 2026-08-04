#!/usr/bin/env python3
"""Independent labelled replay of the lower-25 epsilon arithmetic.

This implementation does not import the primary audit. It scans all
``16^6`` labelled epsilon tuples once and updates every defect budget
``0..16``. It is intentionally redundant and checks only the finite
arithmetic, not the algebraic lemmas.
"""

from __future__ import annotations

from itertools import product
from math import comb

EXPECTED_MINIMUM = {
    0: 120,
    1: 118,
    2: 116,
    3: 112,
    4: 110,
    5: 100,
    6: 98,
    7: 96,
    8: 92,
    9: 88,
    10: 80,
    11: 78,
    12: 74,
    13: 68,
    14: 60,
    15: 50,
    16: 48,
}

EXPECTED_LABELLED_COUNT = {
    0: 1,
    1: 7,
    2: 28,
    3: 84,
    4: 210,
    5: 463,
    6: 930,
    7: 1737,
    8: 3059,
    9: 5131,
    10: 8261,
    11: 12844,
    12: 19377,
    13: 28475,
    14: 40888,
    15: 57520,
    16: 79443,
}


def macaulay(value: int) -> int:
    if value == 0:
        return 0
    largest = 1
    while comb(largest + 1, 2) <= value:
        largest += 1
    remainder = value - comb(largest, 2)
    return comb(largest + 1, 3) + comb(remainder + 1, 2)


def central_lower(quadratic_dimension: int) -> int | None:
    if quadratic_dimension in {14, 15}:
        return 20
    if quadratic_dimension == 13:
        return 18
    if quadratic_dimension == 12:
        return None
    if quadratic_dimension == 11:
        return 14
    if 0 <= quadratic_dimension <= 10:
        return 0
    raise ValueError(quadratic_dimension)


def main() -> int:
    minima = {budget: 10**9 for budget in range(17)}
    labelled = {budget: 0 for budget in range(17)}
    feasible = {budget: 0 for budget in range(17)}

    for epsilon in product(range(16), repeat=6):
        required = sum(epsilon) - min(epsilon)
        if required > 16:
            continue
        central = [central_lower(15 - value) for value in epsilon]
        for budget in range(required, 17):
            labelled[budget] += 1
        if any(value is None for value in central):
            continue
        central_sum = sum(int(value) for value in central)
        for budget in range(required, 17):
            feasible[budget] += 1
            relation_cap = budget - required
            lower = central_sum - 2 * macaulay(relation_cap)
            minima[budget] = min(minima[budget], lower)

    if minima != EXPECTED_MINIMUM:
        raise AssertionError((minima, EXPECTED_MINIMUM))
    if labelled != EXPECTED_LABELLED_COUNT:
        raise AssertionError((labelled, EXPECTED_LABELLED_COUNT))

    for budget in range(17):
        print(
            f"D={budget} labelled={labelled[budget]} "
            f"feasible={feasible[budget]} minimum={minima[budget]}"
        )
    print("N6_FIXED_SIX_LOWER25_INDEPENDENT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
