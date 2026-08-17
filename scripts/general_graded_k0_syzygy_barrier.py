#!/usr/bin/env python3
"""Audit the graded-K0 barrier for exact-additive syzygy scalars.

The proof document shows that every short-exact-additive scalar on finite-
length graded k[s,t]-modules is a weighted Hilbert function. This script
replays the theorem-facing finite interfaces:

* all monomial staircase quotients inside a 6 x 6 box;
* their Hilbert--Burch resolution numerators;
* every removable-corner short exact sequence; and
* permanent/Boolean weighted-ratio arithmetic.

Only exact integer arithmetic and the Python standard library are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any, Iterable


EXPECTED_CORE_SHA256 = (
    "8cabf216e75c6a3b83b56827f57d3689524cd94ef92120feecdd451743b6d23e"
)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def staircase_partitions(max_width: int, max_height: int) -> list[tuple[int, ...]]:
    """All nonempty nonincreasing positive partitions in the given box."""

    result: list[tuple[int, ...]] = []

    def recurse(prefix: list[int], upper: int, rows_left: int) -> None:
        if prefix:
            result.append(tuple(prefix))
        if rows_left == 0:
            return
        for value in range(upper, 0, -1):
            recurse(prefix + [value], value, rows_left - 1)

    recurse([], max_width, max_height)
    return result


def hilbert_function(partition: tuple[int, ...]) -> list[int]:
    values: Counter[int] = Counter()
    for t_degree, row_width in enumerate(partition):
        for s_degree in range(row_width):
            values[s_degree + t_degree] += 1
    return [values[degree] for degree in range(max(values) + 1)]


def ideal_generators(partition: tuple[int, ...]) -> list[tuple[int, int]]:
    """Minimal monomial generators of the complement staircase ideal."""

    generators = [(partition[0], 0)]
    for t_degree in range(1, len(partition)):
        if partition[t_degree] < partition[t_degree - 1]:
            generators.append((partition[t_degree], t_degree))
    generators.append((0, len(partition)))
    return generators


def hilbert_numerator(hilbert: list[int]) -> list[int]:
    """Coefficients of (1-z)^2 H(z)."""

    numerator = [0] * (len(hilbert) + 2)
    for degree, value in enumerate(hilbert):
        numerator[degree] += value
        numerator[degree + 1] -= 2 * value
        numerator[degree + 2] += value
    while numerator and numerator[-1] == 0:
        numerator.pop()
    return numerator


def resolution_numerator(partition: tuple[int, ...]) -> list[int]:
    """Hilbert--Burch numerator from adjacent monomial generators."""

    generators = ideal_generators(partition)
    syzygy_degrees = [
        max(left[0], right[0]) + max(left[1], right[1])
        for left, right in zip(generators, generators[1:])
    ]
    maximum = max(
        [left + right for left, right in generators] + syzygy_degrees
    )
    numerator = [0] * (maximum + 1)
    numerator[0] = 1
    for left, right in generators:
        numerator[left + right] -= 1
    for degree in syzygy_degrees:
        numerator[degree] += 1
    while numerator and numerator[-1] == 0:
        numerator.pop()
    return numerator


def removable_corners(
    partition: tuple[int, ...],
) -> Iterable[tuple[int, tuple[int, ...]]]:
    """Yield (degree, smaller staircase) for every removable corner cell."""

    for row, width in enumerate(partition):
        next_width = partition[row + 1] if row + 1 < len(partition) else 0
        if width <= next_width:
            continue
        smaller = list(partition)
        smaller[row] -= 1
        if smaller[row] == 0:
            require(row == len(smaller) - 1, (partition, row))
            smaller.pop()
        degree = row + width - 1
        yield degree, tuple(smaller)


def padded_difference(left: list[int], right: list[int], size: int) -> list[int]:
    return [
        (left[index] if index < len(left) else 0)
        - (right[index] if index < len(right) else 0)
        for index in range(size)
    ]


def weighted_ratio_audit() -> tuple[int, int, dict[str, list[int]]]:
    checks = 0
    diagnostics: dict[str, list[int]] = {}

    for n in range(2, 61):
        levels = [comb(n, degree) for degree in range(n + 1)]
        central = max(levels)
        weights: list[list[int]] = [
            [1] * (n + 1),
            [degree + 1 for degree in range(n + 1)],
            [(degree + 1) * (n - degree + 1) for degree in range(n + 1)],
            [1 if degree % 2 == 0 else 0 for degree in range(n + 1)],
            [
                ((degree + 1) * 2_654_435_761 + 17 * n) % 11
                for degree in range(n + 1)
            ],
        ]
        for degree in range(n + 1):
            singleton = [0] * (n + 1)
            singleton[degree] = 1
            weights.append(singleton)

        best = Fraction(0)
        for row in weights:
            denominator = sum(weight * level for weight, level in zip(row, levels))
            if denominator == 0:
                continue
            numerator = sum(
                weight * level * level
                for weight, level in zip(row, levels)
            )
            ratio = Fraction(numerator, denominator)
            require(ratio <= central, (n, row, ratio, central))
            best = max(best, ratio)
            checks += 1
        diagnostics[str(n)] = [best.numerator, best.denominator, central]

    exhaustive = 0
    for n in range(2, 11):
        levels = [comb(n, degree) for degree in range(n + 1)]
        central = max(levels)
        for mask in range(1, 1 << (n + 1)):
            denominator = sum(
                levels[degree]
                for degree in range(n + 1)
                if (mask >> degree) & 1
            )
            numerator = sum(
                levels[degree] ** 2
                for degree in range(n + 1)
                if (mask >> degree) & 1
            )
            require(Fraction(numerator, denominator) <= central, (n, mask))
            exhaustive += 1

    return checks, exhaustive, diagnostics


def build_payload() -> dict[str, Any]:
    partitions = staircase_partitions(6, 6)
    numerator_checks = 0
    corner_checks = 0
    composition_cells = 0
    diagnostics: list[dict[str, object]] = []

    for partition in partitions:
        hilbert = hilbert_function(partition)
        require(
            hilbert_numerator(hilbert) == resolution_numerator(partition),
            partition,
        )
        numerator_checks += 1
        composition_cells += sum(hilbert)

        local_corners = 0
        for degree, smaller in removable_corners(partition):
            smaller_hilbert = hilbert_function(smaller) if smaller else []
            size = max(len(hilbert), len(smaller_hilbert), degree + 1)
            difference = padded_difference(hilbert, smaller_hilbert, size)
            expected = [0] * size
            expected[degree] = 1
            require(difference == expected, (partition, smaller, degree))
            corner_checks += 1
            local_corners += 1

        if len(diagnostics) < 20:
            diagnostics.append(
                {
                    "partition": list(partition),
                    "hilbert": hilbert,
                    "generators": [list(value) for value in ideal_generators(partition)],
                    "corner_count": local_corners,
                }
            )

    weighted_checks, exhaustive_supports, ratio_diagnostics = weighted_ratio_audit()

    core: dict[str, Any] = {
        "status": [
            "GENERAL_GRADED_K0_HILBERT_CLASSIFICATION",
            "GENERAL_EXACT_ADDITIVE_SYZYGY_BARRIER",
            "CENTRAL_BINOMIAL_ROUTE_CEILING",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "graded_K0": (
                "K_0 of finite-length graded k[s,t]-modules is freely "
                "generated by the shifts k(-d), and "
                "[M]=sum_d dim(M_d)[k(-d)]."
            ),
            "exact_additive_scalar": (
                "Every short-exact-additive nonnegative scalar has the form "
                "Phi(M)=sum_d c_d dim(M_d) with c_d>=0."
            ),
            "resolution_Euler": (
                "Every exact-additive alternating scalar extracted from a "
                "finite graded free resolution factors through the Hilbert function."
            ),
            "chow_ceiling": (
                "For permanent versus the Boolean Chow-term envelope, every "
                "such scalar rank ratio is at most binom(n,floor(n/2))."
            ),
        },
        "exact_replay": {
            "monomial_staircase_modules": len(partitions),
            "hilbert_betti_numerator_checks": numerator_checks,
            "corner_short_exact_checks": corner_checks,
            "composition_factor_cells": composition_cells,
            "weighted_ratio_checks": weighted_checks,
            "exhaustive_boolean_weight_supports": exhaustive_supports,
            "diagnostics": diagnostics,
            "ratio_diagnostics": ratio_diagnostics,
        },
        "claim_boundary": (
            "The theorem closes only invariants additive on every short exact "
            "sequence, including Grothendieck-group and Euler-characteristic "
            "scalarizations of resolutions. It does not close raw Betti tables, "
            "non-exact partial Euler characteristics, persistence rank invariants, "
            "minimal syzygy functors with a separately proved monotone envelope, "
            "representation-valued data, nonlinear determinantal loci, valuative "
            "arguments, Chow-realizability defects, border rank, exact rank for "
            "n>=6, or general Glynn optimality."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    require(payload["core_sha256"] == EXPECTED_CORE_SHA256, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_GRADED_K0_SYZYGY_BARRIER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
