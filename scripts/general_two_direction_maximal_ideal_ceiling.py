#!/usr/bin/env python3
"""Exact finite arithmetic for the two-direction maximal-ideal ceiling."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path
from typing import Any


FROZEN = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "general_two_direction_maximal_ideal_ceiling.json"
)

EXPECTED_CEILINGS = {
    "3": {"route_ceiling": 3, "existing_boundary": 4},
    "4": {"route_ceiling": 7, "existing_boundary": 8},
    "5": {"route_ceiling": 10, "existing_boundary": 16},
    "6": {"route_ceiling": 20, "existing_boundary": 28},
    "7": {"route_ceiling": 35, "existing_boundary": 49},
    "8": {"route_ceiling": 75, "existing_boundary": 90},
    "9": {"route_ceiling": 126, "existing_boundary": 164},
    "10": {"route_ceiling": 252, "existing_boundary": 307},
}


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, denominator)
    return -(-numerator // denominator)


def primitive_hilbert(size: int) -> list[int]:
    result = []
    previous = 0
    for degree in range(size // 2 + 1):
        current = comb(size, degree)
        result.append(current - previous)
        previous = current
    return result


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def split_quotient_hilbert(n: int) -> list[int]:
    first = n // 2
    second = n - first
    return convolution(primitive_hilbert(first), primitive_hilbert(second))


def route_ceiling_by_degree(n: int) -> dict[str, dict[str, int]]:
    quotient = split_quotient_hilbert(n)
    result: dict[str, dict[str, int]] = {}

    for degree in range(1, n + 1):
        target = comb(n, degree)
        source = comb(n, degree - 1)
        quotient_dimension = quotient[degree] if degree < len(quotient) else 0
        split_image = target - quotient_dimension
        principal_image = min(source, target)
        denominator = max(split_image, principal_image)
        numerator = min(target * target, 2 * source * source)
        ceiling = ceil_div(numerator, denominator)

        result[str(degree)] = {
            "source_boolean": source,
            "target_boolean": target,
            "split_quotient": quotient_dimension,
            "certified_denominator": denominator,
            "permanent_numerator_cap": numerator,
            "route_ceiling": ceiling,
        }
    return result


def build_payload() -> dict[str, Any]:
    profile_cells = 0
    finite: dict[str, dict[str, Any]] = {}

    for n in range(3, 11):
        by_degree = route_ceiling_by_degree(n)
        observed = max(row["route_ceiling"] for row in by_degree.values())
        expected = EXPECTED_CEILINGS[str(n)]
        require(observed == expected["route_ceiling"], (n, observed, expected))
        require(observed < expected["existing_boundary"], (n, observed, expected))
        profile_cells += len(by_degree)
        finite[str(n)] = {
            **expected,
            "central_binomial": comb(n, n // 2),
            "by_degree": by_degree,
        }

    require(profile_cells == 52, profile_cells)

    return {
        "status": [
            "GENERAL_TWO_DIRECTION_MAXIMAL_IDEAL_CEILING",
            "BOOLEAN_SPLIT_QUOTIENT_WITNESS",
            "ASYMPTOTIC_CENTRAL_BINOMIAL_BARRIER",
            "EXACT_FINITE_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "split_quotient": (
                "B_n/(s,t)B_n=(B_floor(n/2)/L) tensor "
                "(B_ceil(n/2)/L)."
            ),
            "boolean_denominator": (
                "beta_m(n,d)>=max(min(C(n,d-1),C(n,d)),C(n,d)-q_(n,d))."
            ),
            "permanent_numerator": (
                "lambda_m(A_perm,d)<=min(C(n,d)^2,2*C(n,d-1)^2)."
            ),
            "asymptotic_ceiling": (
                "R_n^m<=(1+O(n^(-1/2)))*C(n,floor(n/2))."
            ),
            "glynn_gap": "The maximal-ideal profile remains Omega(sqrt(n)) below Glynn.",
        },
        "finite_replay": {
            "profile_cells": profile_cells,
            "n_min": 3,
            "n_max": 10,
            "rows": finite,
        },
        "claim_boundary": (
            "This is a ceiling for the image profile of the linear maximal "
            "ideal (s,t), not an upper bound on Chow rank. It introduces no "
            "new numerical lower bound and does not close unequal-degree "
            "two-generator ideals, higher staircase ideals, relation modules, "
            "Chow-realizability defects, border rank or representation-valued "
            "methods. Literature novelty is not established."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN.exists():
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_TWO_DIRECTION_MAXIMAL_IDEAL_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
