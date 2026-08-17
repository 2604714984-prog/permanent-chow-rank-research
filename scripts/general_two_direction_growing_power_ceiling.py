#!/usr/bin/env python3
"""Exact audit for the general two-direction growing-power ceiling.

The proof is in docs/general_two_direction_growing_power_ceiling.md.  This
script exhausts the integer source/target ratio behind the theorem for
2<=n<=80 and checks the binomial-decay and polynomial-envelope interfaces.
"""

from __future__ import annotations

import argparse
import json
import math
from math import comb
from pathlib import Path
from typing import Any


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def h(n: int, degree: int) -> int:
    return comb(n, degree) if 0 <= degree <= n else 0


def ceil_div(a: int, b: int) -> int:
    require(b > 0, (a, b))
    return -(-a // b)


def central_distance(n: int, degree: int) -> int:
    centers = {n // 2, (n + 1) // 2}
    return min(abs(degree - center) for center in centers)


def raw_route_data(n: int, p: int, degree: int) -> tuple[int, int, int, int]:
    source_level = h(n, degree - p)
    target_level = h(n, degree)
    denominator = min(source_level, target_level)
    if denominator == 0:
        return source_level, target_level, 0, 0
    numerator = min((p + 1) * source_level**2, target_level**2)
    return source_level, target_level, numerator, denominator


def route_ceiling(n: int, p: int, degree: int) -> int:
    _, _, numerator, denominator = raw_route_data(n, p, degree)
    return 0 if denominator == 0 else ceil_div(numerator, denominator)


def build_payload() -> dict[str, Any]:
    route_cells = 0
    decay_checks = 0
    polynomial_checks = 0
    block_checks = 0
    maxima: dict[str, dict[str, int]] = {}

    for n in range(2, 81):
        central = h(n, n // 2)
        maximum = 0
        maximizing_p = 0
        maximizing_degree = 0

        for degree in range(n + 1):
            level = h(n, degree)
            distance = central_distance(n, degree)
            if level:
                lhs = math.log(level / central)
                rhs = -(distance**2) / n
                require(lhs <= rhs + 1e-12, (n, degree, lhs, rhs))
                decay_checks += 1

        explicit_bound = math.ceil(
            3.0 * (n * math.log(n + 1)) ** 0.25 * central
        ) + 1

        block_numerator = 0
        block_denominator = 0

        for p in range(n + 1):
            for degree in range(p, n + 1):
                source, target, numerator, denominator = raw_route_data(
                    n, p, degree
                )
                route_cells += 1
                if denominator == 0:
                    continue

                # Exact geometric-mean interface behind (3.3).
                require(
                    numerator**2
                    <= (p + 1) * central**2 * denominator**2,
                    (n, p, degree, numerator, denominator),
                )

                # Floating replay of the independent endpoint-decay bound.
                exponential = (
                    n
                    * central
                    * math.exp(-((p - 1) ** 2) / (4 * n))
                )
                raw_ratio = numerator / denominator
                require(
                    raw_ratio <= exponential + 1e-8 * max(1.0, exponential),
                    (n, p, degree, raw_ratio, exponential),
                )

                ceiling = ceil_div(numerator, denominator)
                require(
                    ceiling <= explicit_bound,
                    (n, p, degree, ceiling, explicit_bound),
                )
                polynomial_checks += 1

                if ceiling > maximum:
                    maximum = ceiling
                    maximizing_p = p
                    maximizing_degree = degree

                # A deterministic finite block-family replay: every second
                # legal cell is accumulated. The same principal witness gives
                # the sum of denominators.
                if (p + degree) % 2 == 0:
                    block_numerator += numerator
                    block_denominator += denominator

        if block_denominator:
            require(
                ceil_div(block_numerator, block_denominator)
                <= explicit_bound,
                (n, block_numerator, block_denominator, explicit_bound),
            )
            block_checks += 1

        maxima[str(n)] = {
            "maximum_exact_route_ceiling": maximum,
            "maximizing_p": maximizing_p,
            "maximizing_degree": maximizing_degree,
            "central_binomial": central,
            "explicit_polynomial_bound": explicit_bound,
        }

    require(route_cells == 91_877, route_cells)
    require(decay_checks == 3_318, decay_checks)
    require(polynomial_checks == 91_877, polynomial_checks)
    require(block_checks == 79, block_checks)

    return {
        "status": [
            "GENERAL_GROWING_TWO_DIRECTION_POWER_CEILING",
            "FINITE_BLOCK_FAMILY_CEILING",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "principal_denominator": (
                "max_T dim((W^p A_T)_d)>=min(binom(n,d-p),binom(n,d))."
            ),
            "permanent_numerator": (
                "dim((W^p A_perm)_d)<=min((p+1)binom(n,d-p)^2,"
                "binom(n,d)^2)."
            ),
            "pointwise_route": (
                "R_(n,p,d)<=H_* min(sqrt(p+1),"
                "n exp(-(p-1)^2/(4n)))+1."
            ),
            "uniform_ceiling": (
                "R_n=O((n log(n+1))^(1/4) binom(n,floor(n/2)))."
            ),
            "glynn_separation": (
                "R_n=O(2^n(log n)^(1/4)/n^(1/4))=o(2^(n-1))."
            ),
        },
        "exact_replay": {
            "n_min": 2,
            "n_max": 80,
            "route_cells": route_cells,
            "pointwise_binomial_decay_checks": decay_checks,
            "polynomial_envelope_checks": polynomial_checks,
            "finite_block_family_checks": block_checks,
            "maxima": maxima,
        },
        "claim_boundary": (
            "This is a ceiling on power-image lower-bound mechanisms over a "
            "differential space of dimension at most two, including powers "
            "and finite block families depending on n. It is not an upper "
            "bound on actual Chow rank and does not cover arbitrary growing "
            "binary ideals, minimal syzygies, nonlinear determinantal data, "
            "valuative arguments, Chow-realizability defects or border rank. "
            "Literature novelty is not established."
        ),
    }


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
    print("GENERAL_TWO_DIRECTION_GROWING_POWER_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
