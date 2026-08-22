#!/usr/bin/env python3
"""Exact rational counterexample to a higher-wedge psi extrapolation.

For n=3, m=2 and q=x_00^2, compute the quotient gain of adjoining q to
the quadratic permanent derivative space at every exterior degree.  All
elimination is over Fraction; no floating-point or finite-field inference is
used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb
from pathlib import Path


N = 3
VARIABLES = N * N
SYMMETRIC_MONOMIALS = list(combinations_with_replacement(range(VARIABLES), 2))
SYMMETRIC_INDEX = {
    monomial: index for index, monomial in enumerate(SYMMETRIC_MONOMIALS)
}


def permanent_quadrics() -> list[dict[int, Fraction]]:
    quadrics: list[dict[int, Fraction]] = []
    for rows in combinations(range(N), 2):
        for columns in combinations(range(N), 2):
            diagonal = tuple(
                sorted((rows[0] * N + columns[0], rows[1] * N + columns[1]))
            )
            antidiagonal = tuple(
                sorted((rows[0] * N + columns[1], rows[1] * N + columns[0]))
            )
            quadrics.append(
                {
                    SYMMETRIC_INDEX[diagonal]: Fraction(1),
                    SYMMETRIC_INDEX[antidiagonal]: Fraction(1),
                }
            )
    return quadrics


def rectangle_quadric(row: int, column: int) -> dict[int, Fraction]:
    diagonal = tuple(sorted((0, row * N + column)))
    antidiagonal = tuple(sorted((column, row * N)))
    return {
        SYMMETRIC_INDEX[diagonal]: Fraction(1),
        SYMMETRIC_INDEX[antidiagonal]: Fraction(1),
    }


def insertion_sign(variable: int, wedge: tuple[int, ...]) -> int:
    return -1 if sum(entry < variable for entry in wedge) % 2 else 1


def delta_column(
    polynomial: dict[int, Fraction],
    wedge: tuple[int, ...],
    target_wedge_index: dict[tuple[int, ...], int],
) -> dict[int, Fraction]:
    target_wedge_count = len(target_wedge_index)
    wedge_set = set(wedge)
    column: dict[int, Fraction] = {}
    for monomial_index, coefficient in polynomial.items():
        monomial = SYMMETRIC_MONOMIALS[monomial_index]
        for variable in set(monomial):
            if variable in wedge_set:
                continue
            derivative_variable = monomial[1] if monomial[0] == variable else monomial[0]
            output_wedge = tuple(sorted(wedge + (variable,)))
            row = (
                derivative_variable * target_wedge_count
                + target_wedge_index[output_wedge]
            )
            contribution = (
                coefficient
                * monomial.count(variable)
                * insertion_sign(variable, wedge)
            )
            column[row] = column.get(row, Fraction(0)) + contribution
    return {row: value for row, value in column.items() if value}


def add_column(
    column: dict[int, Fraction],
    pivots: dict[int, dict[int, Fraction]],
) -> bool:
    reduced = dict(column)
    while reduced:
        pivot_row = min(reduced)
        pivot_value = reduced[pivot_row]
        if pivot_row not in pivots:
            pivots[pivot_row] = {
                row: value / pivot_value for row, value in reduced.items()
            }
            return True
        pivot = pivots[pivot_row]
        for row, value in pivot.items():
            reduced[row] = reduced.get(row, Fraction(0)) - pivot_value * value
            if not reduced[row]:
                reduced.pop(row, None)
    return False


def rank_profile() -> tuple[list[int], list[int]]:
    base_ranks: list[int] = []
    extended_ranks: list[int] = []
    base_polynomials = permanent_quadrics()
    square = {SYMMETRIC_INDEX[(0, 0)]: Fraction(1)}
    for wedge_degree in range(VARIABLES):
        source_wedges = list(combinations(range(VARIABLES), wedge_degree))
        target_wedges = list(combinations(range(VARIABLES), wedge_degree + 1))
        target_wedge_index = {
            wedge: index for index, wedge in enumerate(target_wedges)
        }
        base_pivots: dict[int, dict[int, Fraction]] = {}
        for polynomial in base_polynomials:
            for wedge in source_wedges:
                add_column(
                    delta_column(polynomial, wedge, target_wedge_index),
                    base_pivots,
                )
        extended_pivots = {
            row: dict(column) for row, column in base_pivots.items()
        }
        for wedge in source_wedges:
            add_column(
                delta_column(square, wedge, target_wedge_index),
                extended_pivots,
            )
        base_ranks.append(len(base_pivots))
        extended_ranks.append(len(extended_pivots))
    return base_ranks, extended_ranks


def verify_explicit_p3_relations() -> int:
    """Verify the nine displayed characteristic-zero identities."""

    e, a, b, c, t, u, d, v, w = range(VARIABLES)
    square = {SYMMETRIC_INDEX[(e, e)]: Fraction(1)}
    relations = [
        [(2, 2, 2, (e, b, d)), (1, 0, 0, (b, d, w))],
        [
            (2, 2, 1, (e, b, d)),
            (2, 2, 2, (e, a, d)),
            (1, 0, 0, (a, d, w)),
            (1, 0, 0, (b, d, v)),
        ],
        [(2, 2, 1, (e, a, d)), (1, 0, 0, (a, d, v))],
        [
            (-2, 1, 2, (e, b, d)),
            (-2, 2, 2, (e, b, c)),
            (-1, 0, 0, (b, c, w)),
            (1, 0, 0, (b, u, d)),
        ],
        [
            (-2, 1, 1, (e, b, d)),
            (-2, 1, 2, (e, a, d)),
            (-2, 2, 1, (e, b, c)),
            (-2, 2, 2, (e, a, c)),
            (-1, 0, 0, (a, c, w)),
            (1, 0, 0, (a, u, d)),
            (-1, 0, 0, (b, c, v)),
            (1, 0, 0, (b, t, d)),
        ],
        [
            (-2, 1, 1, (e, a, d)),
            (-2, 2, 1, (e, a, c)),
            (-1, 0, 0, (a, c, v)),
            (1, 0, 0, (a, t, d)),
        ],
        [(2, 1, 2, (e, b, c)), (1, 0, 0, (b, c, u))],
        [
            (2, 1, 1, (e, b, c)),
            (2, 1, 2, (e, a, c)),
            (1, 0, 0, (a, c, u)),
            (1, 0, 0, (b, c, t)),
        ],
        [(2, 1, 1, (e, a, c)), (1, 0, 0, (a, c, t))],
    ]
    target_wedges = list(combinations(range(VARIABLES), 4))
    target_wedge_index = {
        wedge: index for index, wedge in enumerate(target_wedges)
    }
    seen_q_wedges: set[tuple[int, ...]] = set()
    for relation in relations:
        residual: dict[int, Fraction] = {}
        relation_q_wedges: set[tuple[int, ...]] = set()
        for scalar, row, column, wedge in relation:
            polynomial = square if row == 0 else rectangle_quadric(row, column)
            if row == 0:
                relation_q_wedges.add(wedge)
            for output_row, value in delta_column(
                polynomial, wedge, target_wedge_index
            ).items():
                residual[output_row] = (
                    residual.get(output_row, Fraction(0)) + scalar * value
                )
                if not residual[output_row]:
                    residual.pop(output_row)
        if residual:
            raise AssertionError(residual)
        if seen_q_wedges.intersection(relation_q_wedges):
            raise AssertionError("q-wedge supports are not disjoint")
        seen_q_wedges.update(relation_q_wedges)
    return len(relations)


def build_payload() -> dict[str, object]:
    explicit_relation_count = verify_explicit_p3_relations()
    base_ranks, extended_ranks = rank_profile()
    gains = [extended - base for base, extended in zip(base_ranks, extended_ranks)]
    binomial_extrapolation = [comb(VARIABLES - 1, p) for p in range(VARIABLES)]
    expected_base = [9, 80, 315, 720, 934, 720, 315, 80, 9]
    expected_extended = [10, 88, 343, 767, 966, 720, 315, 80, 9]
    expected_gains = [1, 8, 28, 47, 32, 0, 0, 0, 0]
    if base_ranks != expected_base:
        raise AssertionError(base_ranks)
    if extended_ranks != expected_extended:
        raise AssertionError(extended_ranks)
    if gains != expected_gains:
        raise AssertionError(gains)
    return {
        "status": "EXACT_RATIONAL_HIGHER_WEDGE_PSI_BARRIER",
        "field": "Q",
        "n": N,
        "derivative_output_degree": 2,
        "new_direction": "x_00^2",
        "base_koszul_ranks": base_ranks,
        "extended_koszul_ranks": extended_ranks,
        "quotient_gains": gains,
        "naive_binomial_extrapolation": binomial_extrapolation,
        "p3_explicit_independent_relations": explicit_relation_count,
        "p3_new_source_dimension": comb(VARIABLES - 1, 3),
        "p3_exact_gain": gains[3],
        "claim_boundary": (
            "This refutes the naive higher-wedge extrapolation of the one-direction "
            "psi theorem. It does not refute the proved p=1 theorem and gives no "
            "Chow-rank bound."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    print("HIGHER_WEDGE_PSI_BARRIER_PASS")


if __name__ == "__main__":
    main()
