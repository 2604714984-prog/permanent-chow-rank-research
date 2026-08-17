#!/usr/bin/env python3
"""Independent replay of exact higher-Koszul ranks for one Chow term.

This file imports none of the primary block formula. It reconstructs ranks from
the complete-intersection Koszul homology and independently builds the full
sparse matrices for every bidegree at n=2,3.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import comb


PRIME = 1_000_003


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(maxsize=None)
def ci_rank(n: int, d: int, p: int) -> int:
    ambient = n * n
    if not (0 <= d <= n and 0 <= p <= ambient):
        return 0
    chain = choose(n, d) * choose(ambient, p)
    homology = choose(n, d) * choose(ambient - n, p - d)
    incoming = ci_rank(n, d + 1, p - 1) if d < n and p >= 1 else 0
    value = chain - homology - incoming
    require(value >= 0, (n, d, p, value))
    return value


def wedge_insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def sparse_rank(columns: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    rank = 0
    for raw in columns:
        vector = {
            row: coefficient % PRIME
            for row, coefficient in raw.items()
            if coefficient % PRIME
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            existing = pivots.get(pivot)
            if existing is None:
                inverse = pow(coefficient, PRIME - 2, PRIME)
                vector = {
                    row: value * inverse % PRIME
                    for row, value in vector.items()
                }
                pivots[pivot] = vector
                rank += 1
                break
            for row, value in existing.items():
                updated = (
                    vector.get(row, 0) - coefficient * value
                ) % PRIME
                if updated:
                    vector[row] = updated
                else:
                    vector.pop(row, None)
    return rank


def direct_rank(n: int, d: int, p: int) -> int:
    ambient = n * n
    active = tuple(range(n))
    source_monomials = tuple(combinations(active, d))
    source_wedges = tuple(combinations(range(ambient), p))
    target_monomials = tuple(combinations(active, d - 1))
    target_wedges = tuple(combinations(range(ambient), p + 1))
    monomial_index = {
        value: index for index, value in enumerate(target_monomials)
    }
    wedge_index = {
        value: index for index, value in enumerate(target_wedges)
    }
    wedge_count = len(target_wedges)

    columns = []
    for monomial in source_monomials:
        for wedge in source_wedges:
            wedge_set = set(wedge)
            column: dict[int, int] = {}
            for variable in monomial:
                if variable in wedge_set:
                    continue
                target_monomial = tuple(
                    value for value in monomial if value != variable
                )
                target_wedge = tuple(sorted(wedge + (variable,)))
                row = (
                    monomial_index[target_monomial] * wedge_count
                    + wedge_index[target_wedge]
                )
                column[row] = (
                    column.get(row, 0)
                    + wedge_insertion_sign(variable, wedge)
                )
            columns.append(column)
    return sparse_rank(columns)


def main() -> int:
    direct_checks = 0
    for n in (2, 3):
        ambient = n * n
        for d in range(1, n + 1):
            for p in range(ambient):
                direct = direct_rank(n, d, p)
                recurrence = ci_rank(n, d, p)
                require(direct == recurrence, (n, d, p, direct, recurrence))
                direct_checks += 1

    duality_checks = 0
    for n in range(2, 17):
        ambient = n * n
        for d in range(1, n + 1):
            for p in range(ambient):
                require(
                    ci_rank(n, d, p)
                    == ci_rank(n, n - d + 1, ambient - p - 1),
                    (n, d, p),
                )
                duality_checks += 1

    require(
        [ci_rank(6, d, 2) for d in (2, 3, 4)]
        == [8730, 12066, 9235],
        "n=6 p=2",
    )

    print(f"independent_direct_sparse_checks={direct_checks}")
    print(f"independent_duality_checks={duality_checks}")
    print("independent_n6_p2_exact=8730,12066,9235")
    print("GENERAL_HIGHER_KOSZUL_TERM_RANK_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
