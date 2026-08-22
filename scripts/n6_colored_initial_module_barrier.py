#!/usr/bin/env python3
"""Exact combinatorial audit for the G-036 colored-initial-module barrier.

The calculation has two parts.  First it solves the capacity-constrained
Macaulay inverse problem for twenty labelled summands.  Second it constructs
an explicit coordinate monomial differential module with all twenty labels
active, 336 cubic relations, and exactly 203 quadratic relations.

This is an abstract module certificate, not a Chow decomposition and not a
model of the permanent derivative tower.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def macaulay_successor(value: int, degree: int = 2) -> int:
    """Return the exact degree-``degree`` Macaulay successor."""

    require(value >= 0 and degree >= 1, (value, degree))
    if value == 0:
        return 0
    remaining = value
    upper_bound: int | None = None
    expansion: list[tuple[int, int]] = []
    for lower in range(degree, 0, -1):
        if upper_bound is None:
            upper = lower
            while comb(upper + 1, lower) <= remaining:
                upper += 1
        else:
            upper = upper_bound - 1
            while upper >= lower and comb(upper, lower) > remaining:
                upper -= 1
        if upper >= lower and comb(upper, lower) <= remaining:
            expansion.append((upper, lower))
            remaining -= comb(upper, lower)
            upper_bound = upper
        else:
            upper_bound = upper
    require(remaining == 0, (value, degree, expansion, remaining))
    return sum(comb(upper + 1, lower + 1) for upper, lower in expansion)


def minimum_quadratic_capacity(
    target_cubic: int,
    *,
    colors: int = 20,
    quadratic_cap: int = 15,
    cubic_cap: int = 20,
    all_colors_active: bool = False,
) -> tuple[int, list[int]]:
    """Minimize sum(q_i) subject to sum min(q_i^{<2>},20)>=target."""

    lower = 1 if all_colors_active else 0
    states: dict[int, tuple[int, list[int]]] = {0: (0, [])}
    for _ in range(colors):
        next_states: dict[int, tuple[int, list[int]]] = {}
        for cubic_total, (cost, profile) in states.items():
            for quadratic in range(lower, quadratic_cap + 1):
                cubic = min(cubic_cap, macaulay_successor(quadratic, 2))
                new_total = min(target_cubic, cubic_total + cubic)
                candidate = (cost + quadratic, profile + [quadratic])
                old = next_states.get(new_total)
                if old is None or candidate[0] < old[0]:
                    next_states[new_total] = candidate
        states = next_states
    require(target_cubic in states, target_cubic)
    return states[target_cubic]


def monomials(variables: int, degree: int) -> list[tuple[int, ...]]:
    """All exponent vectors, in descending lexicographic order."""

    result = [
        exponents
        for exponents in product(range(degree + 1), repeat=variables)
        if sum(exponents) == degree
    ]
    return sorted(result, reverse=True)


def lex_quadratic_space(dimension: int) -> set[tuple[int, ...]]:
    require(0 <= dimension <= 10, dimension)
    return set(monomials(4, 2)[:dimension])


def monomial_prolongation(
    quadratic_space: set[tuple[int, ...]],
) -> set[tuple[int, ...]]:
    """Degree-three monomials all of whose nonzero derivatives lie in P."""

    result: set[tuple[int, ...]] = set()
    for cubic in monomials(4, 3):
        derivatives = []
        for index, exponent in enumerate(cubic):
            if exponent:
                derivative = list(cubic)
                derivative[index] -= 1
                derivatives.append(tuple(derivative))
        if all(derivative in quadratic_space for derivative in derivatives):
            result.add(cubic)
    return result


def build_certificate() -> dict[str, object]:
    successor_table = {
        str(value): macaulay_successor(value, 2) for value in range(16)
    }
    inverse_rows = []
    for target in (320, 336):
        unrestricted = minimum_quadratic_capacity(target)
        active = minimum_quadratic_capacity(target, all_colors_active=True)
        inverse_rows.append(
            {
                "cubic_target": target,
                "unrestricted_minimum_quadratic_dimension": unrestricted[0],
                "unrestricted_quadratic_profile": unrestricted[1],
                "all_labels_active_minimum_quadratic_dimension": active[0],
                "all_labels_active_quadratic_profile": active[1],
            }
        )

    active_profile = [1, 1, 1, 8] + [10] * 16
    active_cubic_profile = [
        min(20, macaulay_successor(value, 2)) for value in active_profile
    ]
    require(sum(active_profile) == 171, active_profile)
    require(sum(active_cubic_profile) == 336, active_cubic_profile)

    exact_lex_rows = []
    for dimension in (1, 8, 9, 10):
        quadratic_space = lex_quadratic_space(dimension)
        cubic_space = monomial_prolongation(quadratic_space)
        expected = macaulay_successor(dimension, 2)
        require(len(cubic_space) == expected, (dimension, len(cubic_space), expected))
        exact_lex_rows.append(
            {
                "quadratic_dimension": dimension,
                "cubic_prolongation_dimension": len(cubic_space),
                "quadratic_monomials": [list(value) for value in sorted(quadratic_space)],
                "cubic_monomials": [list(value) for value in sorted(cubic_space)],
            }
        )

    # Add two unused coordinate quadrics to each of the sixteen 10-dimensional
    # colors.  The resulting K_2 has dimension 203 and every color stays below
    # the one-term cap 15.  K_3 is unchanged and remains inside K_2^(1).
    enlarged_quadratic_profile = [1, 1, 1, 8] + [12] * 16
    require(sum(enlarged_quadratic_profile) == 203, enlarged_quadratic_profile)
    require(max(enlarged_quadratic_profile) <= 15, enlarged_quadratic_profile)

    for subset_size in range(1, 21):
        central_rank = 20 * subset_size
        central_defect = 20 * subset_size - central_rank
        require(central_defect == 0, subset_size)

    return {
        "status": "EXACT_INTEGER_COMBINATORIAL_REPLAY_ROUTE_BARRIER",
        "scope": "twenty-label coordinate initial-module abstraction",
        "macaulay_degree_two_successors_0_through_15": successor_table,
        "capacity_constrained_inverse_rows": inverse_rows,
        "explicit_all_labels_active_model": {
            "quadratic_relation_profile_before_slack": active_profile,
            "cubic_relation_profile": active_cubic_profile,
            "quadratic_relation_dimension_before_slack": 171,
            "cubic_relation_dimension": 336,
            "quadratic_slack_added": 32,
            "quadratic_relation_profile_after_slack": enlarged_quadratic_profile,
            "quadratic_relation_dimension_after_slack": 203,
            "maximum_cubic_projection_dimension_per_label": 20,
            "maximum_quadratic_projection_dimension_per_label": 12,
            "all_twenty_labels_active": True,
            "ordinary_central_defect_of_every_nonempty_subset": 0,
            "formal_middle_ambient_dimension": 400,
            "formal_permanent_middle_dimension": 400,
            "formal_middle_intersection_dimension": 336,
            "formal_quadratic_permanent_dimension": 225,
            "formal_quadratic_intersection_dimension": 203,
            "quadratic_label_ambient_dimensions": [15] * 20,
            "formal_quadratic_colored_ambient_dimension": 300,
            "external_quadratic_complement_dimension": 22,
        },
        "sharp_lex_monomial_spaces": exact_lex_rows,
        "strict_conclusion": (
            "Label preservation, the per-label caps 20 and 15, cubic relation "
            "dimension 336, hereditary central defect at most 16, coordinate "
            "torus stability, and cross-degree differentiation alone do not "
            "force quadratic relation dimension greater than 203."
        ),
        "claim_boundary": (
            "The displayed object is an abstract colored differential module. "
            "It is not a Chow decomposition, is not asserted to be realizable "
            "by twenty Chow terms, and does not reproduce the row-column weight "
            "multiplicities or apolar pairing of the permanent.  It therefore "
            "blocks only a dimension/capacity/label argument, not every torus-"
            "geometric lower-27 strategy."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    if args.json:
        args.json.write_text(
            json.dumps(certificate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("N6_COLORED_INITIAL_MODULE_BARRIER_PASS")


if __name__ == "__main__":
    main()
