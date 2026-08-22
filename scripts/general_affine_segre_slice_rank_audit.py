#!/usr/bin/env python3
"""Exact audit for the affine-Segre Boolean-slice ceiling.

Let ``d>=1`` and let

    E_d = e_1 tensor ... tensor e_1 in (k^2)^(tensor d).

The companion proof shows that the minimum number of affine-chart Segre points

    (e_0+t_1 e_1) tensor ... tensor (e_0+t_d e_1)

needed to express ``E_d`` is exactly ``d+1`` over characteristic zero.
The lower bound is an induction by contraction; the script replays the matching
Lagrange/finite-difference construction exactly.

For the permanent Boolean diagonal slice, ``d=n-1``.  Hence the same slice that
forces ``2^(n-1)`` terms in the sign dictionary has rank only ``n`` in the
continuous anchored column-homogeneous dictionary.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Iterator
from fractions import Fraction
from math import factorial
from pathlib import Path

MIN_D = 1
MAX_D = 12
MAX_BOOLEAN_ASSIGNMENT_CANDIDATES = 1_000_000


def require(condition: bool, message: object) -> None:
    if not condition:
        raise AssertionError(message)


def lagrange_top_coefficient_weight(d: int, point: int) -> Fraction:
    """Coefficient of ``P(point)`` when extracting ``[lambda^d] P``."""

    if d < 0:
        raise ValueError("d must be nonnegative")
    if not 0 <= point <= d:
        raise ValueError("point outside 0..d")
    denominator = 1
    for other in range(d + 1):
        if other != point:
            denominator *= point - other
    return Fraction(1, denominator)


def closed_form_weight(d: int, point: int) -> Fraction:
    sign = -1 if (d - point) % 2 else 1
    return Fraction(sign, factorial(point) * factorial(d - point))


def atom_coefficient(point: int, mask: int) -> int:
    """Coefficient on a Boolean tensor basis vector of Hamming weight ``mask``."""

    return point ** mask.bit_count()


def lagrange_construction(d: int) -> dict[str, object]:
    weights = [lagrange_top_coefficient_weight(d, point) for point in range(d + 1)]
    closed = [closed_form_weight(d, point) for point in range(d + 1)]
    require(weights == closed, (d, weights, closed))
    require(all(weight != 0 for weight in weights), (d, weights))

    coefficient_by_hamming_weight: list[Fraction] = []
    for weight in range(d + 1):
        coefficient = sum(
            weights[point] * (point**weight)
            for point in range(d + 1)
        )
        expected = Fraction(1 if weight == d else 0)
        require(coefficient == expected, (d, weight, coefficient, expected))
        coefficient_by_hamming_weight.append(coefficient)

    assignment_checks = 0
    for mask in range(1 << d):
        coefficient = sum(
            weights[point] * atom_coefficient(point, mask)
            for point in range(d + 1)
        )
        expected = Fraction(1 if mask == (1 << d) - 1 else 0)
        require(coefficient == expected, (d, mask, coefficient, expected))
        assignment_checks += 1

    return {
        "d": d,
        "exact_affine_segre_rank": d + 1,
        "lower_bound_induction_value": d + 1,
        "construction_point_count": d + 1,
        "construction_points": list(range(d + 1)),
        "construction_weights": [
            {
                "numerator": weight.numerator,
                "denominator": weight.denominator,
            }
            for weight in weights
        ],
        "hamming_weight_coefficients": [
            {
                "numerator": coefficient.numerator,
                "denominator": coefficient.denominator,
            }
            for coefficient in coefficient_by_hamming_weight
        ],
        "boolean_assignment_checks": assignment_checks,
    }


def anchored_slice_vector(parameters: list[Fraction]) -> Iterator[Fraction]:
    """Yield anchored-slice coefficients without materializing ``2^d`` items."""

    d = len(parameters)
    for mask in range(1 << d):
        coefficient = Fraction(1)
        for index, parameter in enumerate(parameters):
            if (mask >> index) & 1:
                coefficient *= parameter
        yield coefficient


def deterministic_anchored_checks(max_d: int) -> int:
    checked = 0
    for d in range(1, max_d + 1):
        for variant in range(3):
            parameters = [
                Fraction(2 + 5 * index + 3 * variant, 1 + ((index + variant) % 5))
                for index in range(d)
            ]
            coefficient_count = 0
            for mask, coefficient in enumerate(anchored_slice_vector(parameters)):
                direct = Fraction(1)
                for index, parameter in enumerate(parameters):
                    direct *= parameter if (mask >> index) & 1 else 1
                require(coefficient == direct, (d, variant, mask))
                coefficient_count += 1
                checked += 1
            require(coefficient_count == 1 << d, (d, variant, coefficient_count))
    return checked


def compact_rows_sha256(rows: list[dict[str, object]]) -> str:
    encoded = (
        json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_payload(max_d: int = MAX_D) -> dict[str, object]:
    if max_d < MIN_D:
        raise ValueError("max_d must be positive")
    if max_d >= MAX_BOOLEAN_ASSIGNMENT_CANDIDATES.bit_length():
        raise ValueError(
            f"max_d={max_d} requires 2**{max_d} Boolean-assignment "
            f"candidates, exceeding the limit of "
            f"{MAX_BOOLEAN_ASSIGNMENT_CANDIDATES:,}"
        )
    rows = [lagrange_construction(d) for d in range(MIN_D, max_d + 1)]
    anchored_checks = deterministic_anchored_checks(max_d)

    selected_dimensions = sorted(
        {
            *range(1, min(max_d, 8) + 1),
            *(value for value in (10, 12, max_d) if value <= max_d),
        }
    )
    selected_rows = [rows[d - 1] for d in selected_dimensions]

    n6 = rows[5 - 1]
    require(n6["exact_affine_segre_rank"] == 6, n6)
    return {
        "status": "GENERAL_AFFINE_SEGRE_SLICE_RANK_REPLAYED",
        "field": "characteristic zero",
        "tested_tensor_order_range": [MIN_D, max_d],
        "validated_order_count": len(rows),
        "all_rows_sha256": compact_rows_sha256(rows),
        "selected_rows": selected_rows,
        "deterministic_anchored_slice_coefficients_checked": anchored_checks,
        "theorem": {
            "affine_segre_rank": (
                "The affine-chart Segre rank of e_1^(tensor d) is exactly d+1."
            ),
            "permanent_slice_consequence": (
                "For the n x n permanent Boolean diagonal slice, the exact "
                "rank in the anchored continuous column-homogeneous dictionary "
                "is n."
            ),
            "sign_contrast": (
                "The same slice has exact rank 2^(n-1) in the sign dictionary "
                "but only n in the continuous affine chart."
            ),
        },
        "n6": {
            "boolean_dimension": 5,
            "anchored_continuous_slice_rank": 6,
            "column_sign_slice_rank": 32,
            "unrestricted_chow_rank_changed": False,
        },
        "claim_boundary": (
            "This theorem determines the rank of one coefficient slice in an "
            "anchored column-homogeneous dictionary. It does not construct an "
            "n-term decomposition of the full permanent, determine arbitrary "
            "row-homogeneous tensor rank, or change unrestricted Chow rank."
        ),
        "route_decision": (
            "The Boolean diagonal slice cannot prove arbitrary anchored "
            "row- or column-homogeneous rank larger than n. The exponential "
            "sign lower bound relies essentially on the discrete plus/minus-one "
            "dictionary."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=MAX_D)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    try:
        payload = build_payload(args.max_d)
    except ValueError as error:
        parser.error(str(error))
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_AFFINE_SEGRE_SLICE_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
