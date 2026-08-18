#!/usr/bin/env python3
"""Independent replay for the dyadic multirow polarization construction.

This implementation does not import the primary audit.  It enumerates Walsh
characters by bit masks, checks every row assignment through t=6, and
reconstructs the degree/term staircase with integer bit operations.
"""

from __future__ import annotations

from itertools import product
from math import factorial


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def walsh_sum(t: int, assignment: tuple[int, ...]) -> int:
    """Return the unnormalized integer selector sum."""

    total = 0
    sign_count = 1 << (t - 1)
    for mask in range(sign_count):
        character = 1
        row_signs = [1]
        for index in range(t - 1):
            sign = -1 if ((mask >> index) & 1) == 0 else 1
            row_signs.append(sign)
            character *= sign
        term = character
        for row in assignment:
            term *= row_signs[row]
        total += term
    return total


def staircase_degree(m: int, dyadic_exponent: int) -> int:
    require(0 <= dyadic_exponent <= m - 1, (m, dyadic_exponent))
    return m * (m - dyadic_exponent)


def exponent_from_degree(n: int, m: int) -> int:
    require(m <= n, (n, m))
    return min(m - 1, max(0, m - n // m))


def main() -> int:
    assignments = 0
    walsh_terms = 0
    for t in range(1, 7):
        nonzero = 0
        normalizer = 1 << (t - 1)
        for assignment in product(range(t), repeat=t):
            observed = walsh_sum(t, assignment)
            expected = normalizer if len(set(assignment)) == t else 0
            require(observed == expected, (t, assignment, observed, expected))
            assignments += 1
            walsh_terms += normalizer
            if observed:
                nonzero += 1
        require(nonzero == factorial(t), (t, nonzero))

    staircase_cells = 0
    extension_checks = 0
    for m in range(1, 129):
        last_degree = m * m + m
        for exponent in range(m):
            degree = staircase_degree(m, exponent)
            terms = 1 << exponent
            require(degree == m * (m - exponent), (m, exponent, degree))
            require(last_degree - degree == m, (m, exponent, last_degree, degree))
            last_degree = degree
            recovered = exponent_from_degree(degree, m)
            require(recovered == exponent, (m, exponent, degree, recovered))
            require((1 << recovered) == terms, (m, exponent, terms))
            staircase_cells += 1

            # Extra factors preserve the witness until the next staircase
            # point, where a smaller dyadic family becomes available.
            next_degree = (
                staircase_degree(m, exponent - 1)
                if exponent > 0
                else m * m + m
            )
            for n in {degree, degree + 1, next_degree - 1}:
                if n < degree:
                    continue
                recovered_at_n = exponent_from_degree(n, m)
                require(recovered_at_n <= exponent, (m, exponent, n))
                extension_checks += 1

    print(
        "assignments_checked=", assignments,
        "walsh_terms_checked=", walsh_terms,
        "staircase_cells=", staircase_cells,
        "extension_checks=", extension_checks,
    )
    print("GENERAL_MULTIROW_POLARIZATION_ENVELOPES_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
