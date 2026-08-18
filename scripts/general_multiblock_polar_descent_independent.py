#!/usr/bin/env python3
"""Independent replay of the multiblock polar descent arithmetic.

This file imports no primary helper.  It reconstructs the lifting increment as
``ceil(d^2/n)-1``, simulates the term-peeling process and verifies the closed
sum formula on a disjoint finite range.
"""

from __future__ import annotations

from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(a: int, b: int) -> int:
    require(b > 0, (a, b))
    return -(-a // b)


def independent_increment(n: int, degree: int) -> int:
    return ceil_div(degree * degree, n) - 1


def independent_counts(n: int) -> list[int]:
    values = [0] * (n + 1)
    for degree in range(2, n + 1):
        values[degree] = values[degree - 1] + independent_increment(n, degree)
    return values


def peel(n: int, degree: int, terms: int) -> int:
    current = terms
    for output_degree in range(degree, 1, -1):
        removable = independent_increment(n, output_degree)
        if current <= removable:
            return 0
        current -= removable
    return current


def main() -> int:
    increment_checks = 0
    recurrence_checks = 0
    exhaustive_checks = 0
    top_checks = 0

    selected = {}
    for n in range(2, 513):
        values = independent_counts(n)
        direct_sum = 0
        for degree in range(2, n + 1):
            increment = independent_increment(n, degree)
            require(
                increment == (degree * degree - 1) // n,
                (n, degree, increment),
            )
            increment_checks += 1
            direct_sum += (degree * degree - 1) // n
            require(values[degree] == direct_sum, (n, degree, values[degree]))
            recurrence_checks += 1

        rank_lower = values[n] + 1
        require(rank_lower <= 2 ** (n - 1), (n, rank_lower))
        if n >= 4:
            require(rank_lower <= comb(n, n // 2), (n, rank_lower))
        top_checks += 1

        for degree in range(2, min(n, 48) + 1):
            for terms in range(values[degree] + 1):
                require(peel(n, degree, terms) == 0, (n, degree, terms))
                exhaustive_checks += 1

        if n in {3, 4, 5, 8, 9, 10, 16, 32, 64, 100, 256, 512}:
            selected[n] = values[n]

    require(
        selected
        == {
            3: 3,
            4: 5,
            5: 8,
            8: 22,
            9: 26,
            10: 33,
            16: 86,
            32: 344,
            64: 1368,
            100: 3333,
            256: 21852,
            512: 87396,
        },
        selected,
    )

    print(f"independent_increment_checks={increment_checks}")
    print(f"independent_recurrence_checks={recurrence_checks}")
    print(f"independent_exhaustive_peeling_checks={exhaustive_checks}")
    print(f"independent_top_checks={top_checks}")
    print(f"independent_selected_top_zero_counts={selected}")
    print("GENERAL_MULTIBLOCK_POLAR_DESCENT_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
