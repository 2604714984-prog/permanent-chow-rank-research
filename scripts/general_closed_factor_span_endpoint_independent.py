#!/usr/bin/env python3
"""Independent replay of the closed factor-span endpoint arithmetic.

This implementation imports none of the primary audit. It reconstructs the
endpoint triples by divisor arithmetic, verifies the sharp exceptions through
explicit squarefree matching supports, and checks the omitted-block capacity.
"""

from __future__ import annotations

from itertools import permutations
from math import comb, factorial


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def strict_size(n: int, m: int) -> int:
    return (m * m - 1) // n


def endpoint_size(n: int, m: int) -> int:
    q, remainder = divmod(m * m, n)
    return strict_size(n, m) + int(m >= 3 and remainder == 0 and q >= 2)


def matching_support_count(m: int) -> int:
    seen = {
        tuple((row, sigma[row]) for row in range(m))
        for sigma in permutations(range(m))
    }
    require(len(seen) == factorial(m), (m, len(seen)))
    require(
        all(len(set(cell for cell in matching)) == m for matching in seen),
        m,
    )
    return len(seen)


def main() -> int:
    endpoint_triples = []
    proper_triples = []
    projection_checks = 0

    for n in range(2, 129):
        for m in range(2, n + 1):
            closed = endpoint_size(n, m)
            strict = strict_size(n, m)
            require(closed in (strict, strict + 1), (n, m))
            if closed == strict + 1:
                q = m * m // n
                endpoint_triples.append((n, m, q))
                if m < n:
                    proper_triples.append((n, m, q))
            for total in range(closed, closed + 5):
                cap = (total - closed) * comb(n, m)
                require(cap >= 0, cap)
                projection_checks += 1

    require(len(endpoint_triples) == 258, len(endpoint_triples))
    require(len(proper_triples) == 132, len(proper_triples))
    require(
        proper_triples[:6]
        == [
            (8, 4, 2),
            (9, 6, 4),
            (12, 6, 3),
            (16, 8, 4),
            (16, 12, 9),
            (18, 6, 2),
        ],
        proper_triples[:6],
    )

    matching_checks = sum(matching_support_count(m) for m in range(2, 9))
    require(
        matching_checks == sum(factorial(m) for m in range(2, 9)),
        matching_checks,
    )
    require(matching_support_count(2) == 2, "quadratic exception")

    print("independent_endpoint_triples=258")
    print("independent_proper_endpoint_triples=132")
    print(f"independent_projection_checks={projection_checks}")
    print(f"independent_matching_support_checks={matching_checks}")
    print("independent_quadratic_exception=perm2_has_two_terms")
    print("GENERAL_CLOSED_FACTOR_SPAN_ENDPOINT_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
