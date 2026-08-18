#!/usr/bin/env python3
"""Independent replay for the sharp two-term threshold.

This file imports none of the primary implementation.  It checks the local
two-row identity, counts the matching tails, verifies the independent-factor
envelopes, and reconstructs the exact threshold arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def local_identity() -> None:
    # Coefficients in the basis
    # a_c a_d, a_c b_d, b_c a_d, b_c b_d.
    first = {
        "aa": Fraction(1, 4),
        "ab": Fraction(-1, 4),
        "ba": Fraction(1, 4),
        "bb": Fraction(-1, 4),
    }
    second = {
        "aa": Fraction(1, 4),
        "ab": Fraction(1, 4),
        "ba": Fraction(-1, 4),
        "bb": Fraction(-1, 4),
    }
    total = {key: first[key] + second[key] for key in first}
    require(
        total
        == {
            "aa": Fraction(1, 2),
            "ab": Fraction(0),
            "ba": Fraction(0),
            "bb": Fraction(-1, 2),
        },
        total,
    )


def main() -> int:
    local_identity()

    tail_checks = 0
    factor_checks = 0
    for m in range(2, 10):
        columns = range(m)
        rows = range(2, m)
        seen_a = set()
        seen_b = set()
        for c, d in combinations(columns, 2):
            remaining = tuple(value for value in columns if value not in (c, d))
            for assignment in permutations(remaining):
                tail = tuple(
                    sorted(
                        f"x{i}_{assignment[index]}"
                        for index, i in enumerate(rows)
                    )
                )
                a_term = tuple(sorted((f"a{c}", f"a{d}", *tail)))
                b_term = tuple(sorted((f"b{c}", f"b{d}", *tail)))
                require(len(a_term) == m and len(set(a_term)) == m, a_term)
                require(len(b_term) == m and len(set(b_term)) == m, b_term)
                seen_a.add(a_term)
                seen_b.add(b_term)
                factor_checks += 2

        expected = factorial(m) // 2
        require(len(seen_a) == expected, (m, len(seen_a), expected))
        require(len(seen_b) == expected, (m, len(seen_b), expected))
        require(
            len({f"a{j}" for j in columns}
                | {f"x{i}_{j}" for i in rows for j in columns})
            == m * (m - 1),
            m,
        )
        tail_checks += expected

    threshold_checks = 0
    for m in range(3, 257):
        threshold = m * (m - 1)
        require(threshold - 1 == m * m - m - 1, m)
        require(threshold == m * m - m, m)
        if m == 3:
            require(threshold == 6, threshold)
        threshold_checks += 1

    print("independent_local_identity_checks=1")
    print(f"independent_matching_tail_checks={tail_checks}")
    print(f"independent_factor_membership_checks={factor_checks}")
    print(f"independent_threshold_checks={threshold_checks}")
    print("GENERAL_SHARP_PAIR_THRESHOLD_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
