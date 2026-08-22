#!/usr/bin/env python3
"""Exact combinatorial replay of the general quadratic psi-chart theorem.

For ``n=3,4,5,6`` the script builds the coefficient constraints defining the
full and coordinate-relative cubic prolongations of the quadratic permanent
derivative space.  The constraints are weighted equalities and zero equations,
so connected-component propagation over ``Fraction`` computes the nullities
exactly.  No matrix rank over a finite field or floating point is used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path


Monomial = tuple[int, int, int]


def variable(row: int, column: int, n: int) -> int:
    return row * n + column


def is_matching_pair(first: int, second: int, n: int) -> bool:
    return (
        first != second
        and first // n != second // n
        and first % n != second % n
    )


def preimage(pair: tuple[int, int], direction: int) -> tuple[Monomial, int]:
    monomial = tuple(sorted((*pair, direction)))
    multiplier = monomial.count(direction)
    return monomial, multiplier


def prolongation_nullity(n: int, excluded_direction: int | None) -> int:
    variables = n * n
    monomials = list(combinations_with_replacement(range(variables), 3))
    index = {monomial: position for position, monomial in enumerate(monomials)}
    adjacency: list[list[tuple[int, Fraction]]] = [
        [] for _ in monomials
    ]
    forced_zero: set[int] = set()

    directions = [
        direction
        for direction in range(variables)
        if direction != excluded_direction
    ]
    quadratic_monomials = list(
        combinations_with_replacement(range(variables), 2)
    )

    for direction in directions:
        for pair in quadratic_monomials:
            if is_matching_pair(pair[0], pair[1], n):
                continue
            monomial, _ = preimage(pair, direction)
            forced_zero.add(index[monomial])

        for first_row in range(n):
            for second_row in range(first_row + 1, n):
                for first_column in range(n):
                    for second_column in range(first_column + 1, n):
                        first_pair = tuple(
                            sorted(
                                (
                                    variable(first_row, first_column, n),
                                    variable(second_row, second_column, n),
                                )
                            )
                        )
                        second_pair = tuple(
                            sorted(
                                (
                                    variable(first_row, second_column, n),
                                    variable(second_row, first_column, n),
                                )
                            )
                        )
                        first_monomial, first_multiplier = preimage(
                            first_pair,
                            direction,
                        )
                        second_monomial, second_multiplier = preimage(
                            second_pair,
                            direction,
                        )
                        left = index[first_monomial]
                        right = index[second_monomial]
                        # first_multiplier*c_left = second_multiplier*c_right
                        right_over_left = Fraction(
                            first_multiplier,
                            second_multiplier,
                        )
                        adjacency[left].append((right, right_over_left))
                        adjacency[right].append((left, 1 / right_over_left))

    visited: set[int] = set()
    nullity = 0
    for start in range(len(monomials)):
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


def build_payload() -> dict[str, object]:
    rows: list[dict[str, int]] = []
    for n in range(3, 7):
        ambient = n * n
        quadratic_dimension = comb(n, 2) ** 2
        cubic_dimension = comb(n, 3) ** 2
        full_nullity = prolongation_nullity(n, excluded_direction=None)
        relative_nullity = prolongation_nullity(n, excluded_direction=0)
        if full_nullity != cubic_dimension:
            raise AssertionError((n, full_nullity, cubic_dimension))
        if relative_nullity != cubic_dimension + 1:
            raise AssertionError((n, relative_nullity, cubic_dimension + 1))

        quotient_dimension = comb(ambient + 1, 2) - quadratic_dimension
        base_rank = ambient * quadratic_dimension - cubic_dimension
        rows.append(
            {
                "n": n,
                "ambient_variable_dimension": ambient,
                "quadratic_permanent_derivative_dimension": quadratic_dimension,
                "full_cubic_prolongation_nullity": full_nullity,
                "coordinate_relative_cubic_nullity": relative_nullity,
                "psi_source_dimension": quotient_dimension,
                "psi_rank": quotient_dimension - 1,
                "base_quadratic_koszul_rank": base_rank,
                "one_new_quadratic_direction_gain": ambient - 1,
                "extended_quadratic_koszul_rank_lower": (
                    base_rank + ambient - 1
                ),
            }
        )

    return {
        "status": "EXACT_GENERAL_QUADRATIC_PSI_CHART_REPLAY",
        "field": "characteristic zero",
        "method": (
            "exact weighted coefficient-constraint components over Fraction"
        ),
        "theorem": (
            "For every n>=3 and nonzero v, ker psi_v is the line spanned "
            "by [v^2]; every one-dimensional quadratic extension outside "
            "D_(n-2)(perm_n) adds at least n^2-1 first-Koszul dimensions."
        ),
        "replayed_cases": rows,
        "claim_boundary": (
            "The theorem controls one added quadratic direction. It does not "
            "make gains from several directions additive and does not prove "
            "the exact unrestricted Chow rank for n>=6."
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
    print("GENERAL_QUADRATIC_PSI_CHART_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
