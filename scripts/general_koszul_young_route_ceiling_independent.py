#!/usr/bin/env python3
"""Independent replay of the all-wedge Koszul--Young route ceiling.

This file imports none of the primary audit.  Active Boolean ranks are rebuilt
from the fixed-total-degree Koszul recurrence and the complete-intersection
homology, rather than from the simplex-component formula used by the primary
implementation.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(maxsize=None)
def active_rank(n: int, m: int, p: int) -> int:
    q = m + p
    previous = 0
    for index in range(p + 1):
        module_degree = q - index
        chain_dimension = choose(n, module_degree) * choose(n, index)
        homology = choose(n, index) if q == 2 * index else 0
        current = chain_dimension - homology - previous
        require(current >= 0, (n, m, p, index, current))
        previous = current
    return previous


def term_rank(n: int, m: int, p: int) -> int:
    N = n * n
    inactive = N - n
    return sum(
        choose(inactive, h) * active_rank(n, m, p - h)
        for h in range(max(0, p - n), min(p, inactive) + 1)
    )


def main() -> int:
    active_checks = 0
    quarter_checks = 0
    duality_checks = 0
    ceiling_checks = 0
    observed = {}

    for n in range(2, 11):
        N = n * n
        central = choose(n, n // 2)
        best = 0
        for m in range(1, n + 1):
            for a in range(n + 1):
                rank = active_rank(n, m, a)
                source = choose(n, m) * choose(n, a)
                target = choose(n, m - 1) * choose(n, a + 1)
                require(2 * rank >= min(source, target), (n, m, a))
                active_checks += 1

            for p in range(N):
                rank = term_rank(n, m, p)
                source = choose(n, m) * choose(N, p)
                target = choose(n, m - 1) * choose(N, p + 1)
                require(4 * rank >= min(source, target), (n, m, p))
                quarter_checks += 1
                require(rank == term_rank(n, n - m + 1, N - p - 1), (n, m, p))
                duality_checks += 1

                numerator = min(
                    choose(n, m) ** 2 * choose(N, p),
                    choose(n, m - 1) ** 2 * choose(N, p + 1),
                )
                ceiling = -(-numerator // rank)
                require(ceiling <= 4 * central, (n, m, p, ceiling))
                ceiling_checks += 1
                best = max(best, ceiling)
        observed[n] = best

    require(active_checks == 438, active_checks)
    require(quarter_checks == 3024, quarter_checks)
    require(duality_checks == 3024, duality_checks)
    require(ceiling_checks == 3024, ceiling_checks)
    require(
        observed == {2: 2, 3: 5, 4: 8, 5: 17, 6: 30, 7: 61, 8: 110, 9: 225, 10: 413},
        observed,
    )

    print("independent_active_half_rank_checks=438")
    print("independent_term_quarter_rank_checks=3024")
    print("independent_transpose_duality_checks=3024")
    print("independent_route_ceiling_checks=3024")
    print("independent_maxima_n2_to_n10=2,5,8,17,30,61,110,225,413")
    print("GENERAL_KOSZUL_YOUNG_ROUTE_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
