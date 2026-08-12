#!/usr/bin/env python3
"""Exact coefficient replay for the derivative-degree psi-chart theorem.

For selected pairs ``(n,m)`` with ``2 <= m <= n-1``, this script builds the
weighted coefficient constraints defining the full and one-coordinate
relative prolongations of

    D_(n-m)(perm_n) subset Sym^m(V).

Connected-component propagation over ``Fraction`` computes the nullities
exactly.  Floating point and finite fields are not used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import comb
from pathlib import Path


Monomial = tuple[int, ...]

CASES = ((3, 2), (4, 2), (4, 3), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3))


def variable(row: int, column: int, n: int) -> int:
    return row * n + column


def is_matching(monomial: Monomial, n: int) -> bool:
    return (
        len(set(monomial)) == len(monomial)
        and len({entry // n for entry in monomial}) == len(monomial)
        and len({entry % n for entry in monomial}) == len(monomial)
    )


def preimage(monomial: Monomial, direction: int) -> tuple[Monomial, int]:
    lifted = tuple(sorted((*monomial, direction)))
    return lifted, lifted.count(direction)


def matching_block(rows: tuple[int, ...], columns: tuple[int, ...], n: int) -> list[Monomial]:
    return [
        tuple(sorted(variable(row, column, n) for row, column in zip(rows, order)))
        for order in permutations(columns)
    ]


def prolongation_nullity(n: int, degree: int, excluded_direction: int | None) -> int:
    variables = n * n
    lifted_monomials = list(
        combinations_with_replacement(range(variables), degree + 1)
    )
    index = {
        monomial: position for position, monomial in enumerate(lifted_monomials)
    }
    adjacency: list[list[tuple[int, Fraction]]] = [
        [] for _ in lifted_monomials
    ]
    forced_zero: set[int] = set()

    degree_monomials = list(
        combinations_with_replacement(range(variables), degree)
    )
    row_sets = list(combinations(range(n), degree))
    column_sets = list(combinations(range(n), degree))
    blocks = [
        matching_block(rows, columns, n)
        for rows in row_sets
        for columns in column_sets
    ]

    for direction in range(variables):
        if direction == excluded_direction:
            continue

        for monomial in degree_monomials:
            if is_matching(monomial, n):
                continue
            lifted, _ = preimage(monomial, direction)
            forced_zero.add(index[lifted])

        for block in blocks:
            first_lifted, first_multiplier = preimage(block[0], direction)
            left = index[first_lifted]
            for monomial in block[1:]:
                second_lifted, second_multiplier = preimage(monomial, direction)
                right = index[second_lifted]
                # first_multiplier*c_left = second_multiplier*c_right.
                right_over_left = Fraction(first_multiplier, second_multiplier)
                adjacency[left].append((right, right_over_left))
                adjacency[right].append((left, 1 / right_over_left))

    visited: set[int] = set()
    nullity = 0
    for start in range(len(lifted_monomials)):
        if start in visited:
            continue
        values = {start: Fraction(1)}
        stack = [start]
        component: list[int] = []
        inconsistent = False
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            component.append(current)
            for target, target_over_current in adjacency[current]:
                candidate = values[current] * target_over_current
                if target in values:
                    if values[target] != candidate:
                        inconsistent = True
                    continue
                values[target] = candidate
                stack.append(target)
        if inconsistent or any(node in forced_zero for node in component):
            continue
        nullity += 1
    return nullity


def case_payload(n: int, degree: int) -> dict[str, int]:
    variables = n * n
    derivative_dimension = comb(n, degree) ** 2
    next_dimension = comb(n, degree + 1) ** 2
    full = prolongation_nullity(n, degree, excluded_direction=None)
    relative = prolongation_nullity(n, degree, excluded_direction=0)
    if full != next_dimension:
        raise AssertionError((n, degree, full, next_dimension))
    if relative != next_dimension + 1:
        raise AssertionError((n, degree, relative, next_dimension + 1))

    source_dimension = comb(variables + degree - 1, degree) - derivative_dimension
    base_rank = variables * derivative_dimension - next_dimension
    return {
        "n": n,
        "degree_m": degree,
        "ambient_variable_dimension": variables,
        "permanent_derivative_dimension": derivative_dimension,
        "full_prolongation_nullity": full,
        "coordinate_relative_prolongation_nullity": relative,
        "psi_source_dimension": source_dimension,
        "psi_rank": source_dimension - 1,
        "base_first_koszul_rank": base_rank,
        "one_new_direction_gain": variables - 1,
        "extended_first_koszul_rank_lower": base_rank + variables - 1,
    }


def build_payload() -> dict[str, object]:
    rows = [case_payload(n, degree) for n, degree in CASES]
    return {
        "status": "EXACT_GENERAL_DERIVATIVE_PSI_CHART_REPLAY",
        "field": "characteristic zero",
        "method": "exact weighted coefficient-constraint components over Fraction",
        "theorem": (
            "For every n>=3, 2<=m<=n-1, and nonzero v, the degree-m "
            "permanent derivative psi chart has kernel span([v^m]); one new "
            "degree-m direction adds at least n^2-1 first-Koszul dimensions."
        ),
        "replayed_cases": rows,
        "claim_boundary": (
            "The proof is uniform, but the conclusion controls one added "
            "direction. It does not make several quotient gains additive and "
            "does not prove the exact unrestricted Chow rank for n>=6."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    print("GENERAL_DERIVATIVE_PSI_CHART_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
