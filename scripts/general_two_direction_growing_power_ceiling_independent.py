#!/usr/bin/env python3
"""Independent arithmetic replay for the growing power-profile ceiling.

This file imports none of the primary audit or prior two-direction scripts. It
reconstructs the Boolean principal denominator and permanent source/target cap
directly from binomial coefficients.
"""

from __future__ import annotations

import math
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def level(n: int, degree: int) -> int:
    return comb(n, degree) if 0 <= degree <= n else 0


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def main() -> int:
    cells = 0
    exact_ratio_checks = 0
    polynomial_checks = 0
    block_checks = 0

    for n in range(2, 46):
        central = level(n, n // 2)
        explicit = math.ceil(
            4.0 * (n * math.log(n + 1)) ** 0.25 * central
        ) + 1

        even_num = 0
        even_den = 0
        odd_num = 0
        odd_den = 0

        for p in range(n + 1):
            for degree in range(p, n + 1):
                source = level(n, degree - p)
                target = level(n, degree)
                denominator = min(source, target)
                numerator = min((p + 1) * source**2, target**2)
                require(denominator > 0, (n, p, degree))
                cells += 1

                # Direct arithmetic form of the geometric-mean estimate.
                require(
                    numerator**2
                    <= (p + 1) * central**2 * denominator**2,
                    (n, p, degree),
                )
                exact_ratio_checks += 1

                ceiling = ceil_div(numerator, denominator)
                require(ceiling <= explicit, (n, p, degree, ceiling, explicit))
                polynomial_checks += 1

                if p % 2:
                    odd_num += numerator
                    odd_den += denominator
                else:
                    even_num += numerator
                    even_den += denominator

        require(ceil_div(even_num, even_den) <= explicit, (n, "even"))
        require(ceil_div(odd_num, odd_den) <= explicit, (n, "odd"))
        block_checks += 2

    require(cells == 17_292, cells)
    require(exact_ratio_checks == 17_292, exact_ratio_checks)
    require(polynomial_checks == 17_292, polynomial_checks)
    require(block_checks == 88, block_checks)

    print("independent_route_cells=17292")
    print("independent_exact_ratio_checks=17292")
    print("independent_polynomial_checks=17292")
    print("independent_block_checks=88")
    print("GENERAL_TWO_DIRECTION_GROWING_POWER_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
