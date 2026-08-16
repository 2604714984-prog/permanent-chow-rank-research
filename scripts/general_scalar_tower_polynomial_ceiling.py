#!/usr/bin/env python3
"""Audit finite interfaces for a polynomial ceiling on the scalar tower.

The proof document establishes

    Theta_n = O(n^(1/4) * binom(n,floor(n/2)))
            = O(2^n / n^(1/4)).

Thus the complete exact scalar derivative tower remains a factor
Omega(n^(1/4)) below Glynn's 2^(n-1) scale.  This file checks exact finite
interfaces used by the proof.  It is regression evidence, not a substitute
for the uniform Stirling and Hoeffding arguments.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import ceil, comb, floor
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FULL_TOWER_DATA = ROOT / "data" / "general_full_degree_tower_envelope.json"
FROZEN_DATA = ROOT / "data" / "general_scalar_tower_polynomial_ceiling.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def hypergeometric_counts(n: int, sample_size: int) -> tuple[list[int], int]:
    half = n // 2
    other = n - half
    denominator = comb(n, sample_size)
    counts = [
        comb(half, value) * comb(other, sample_size - value)
        if 0 <= value <= half and 0 <= sample_size - value <= other
        else 0
        for value in range(sample_size + 1)
    ]
    require(sum(counts) == denominator, (n, sample_size, sum(counts), denominator))
    return counts, denominator


def exact_hypergeometric_diagnostics() -> dict[str, int]:
    pair_count = 0
    cdf_count = 0

    for n in range(12, 81):
        first_k = ceil(n / 3)
        last_k = floor(2 * n / 3)
        for sample_size in range(first_k, last_k + 1):
            upper_counts, upper_denominator = hypergeometric_counts(n, sample_size)
            lower_counts, lower_denominator = hypergeometric_counts(n, sample_size - 1)
            maximum_count = max(upper_counts)

            # Deliberately loose exact finite diagnostic.  The proof uses a
            # uniform Stirling estimate and only needs O(n^(-1/2)).
            require(
                n * maximum_count * maximum_count
                <= 400 * upper_denominator * upper_denominator,
                (n, sample_size, maximum_count, upper_denominator),
            )

            upper_prefix = 0
            lower_prefix = 0
            for threshold in range(-1, sample_size + 1):
                if threshold >= 0:
                    upper_prefix += upper_counts[threshold]
                lower_index = threshold + 1
                if 0 <= lower_index < len(lower_counts):
                    lower_prefix += lower_counts[lower_index]

                left = Fraction(lower_prefix, lower_denominator)
                right = Fraction(upper_prefix, upper_denominator) + Fraction(
                    2 * maximum_count,
                    upper_denominator,
                )
                require(left <= right, (n, sample_size, threshold, left, right))
                cdf_count += 1

            pair_count += 1

    require(pair_count == 1_081, pair_count)
    require(cdf_count == 31_579, cdf_count)
    return {
        "hypergeometric_parameter_pairs": pair_count,
        "adjacent_cdf_checks": cdf_count,
        "finite_atom_constant_squared": 400,
    }


def geometric_start_diagnostics() -> int:
    checks = 0
    for n in range(4, 201):
        running = 0
        for degree in range(1, (n - 1) // 2 + 1):
            running += comb(n, degree)
            numerator = n - degree + 1
            denominator = n - 2 * degree + 1
            require(
                running * denominator <= comb(n, degree) * numerator,
                (n, degree, running, numerator, denominator),
            )
            checks += 1

        central = comb(n, n // 2)
        # A uniform exact normalization sufficient for the finite replay.
        require(2 * (n + 1) * central * central >= 4**n, (n, central))

    require(checks == 9_899, checks)
    return checks


def finite_normalization_rows() -> dict[str, dict[str, int]]:
    payload = json.loads(FULL_TOWER_DATA.read_text(encoding="utf-8"))
    rows: dict[str, dict[str, int]] = {}
    for key, value in payload["thresholds"].items():
        n = int(key)
        theta = value["theta"]
        central = comb(n, n // 2)
        rows[key] = {
            "theta": theta,
            "central_binomial": central,
            "ratio_numerator": theta,
            "ratio_denominator": central,
        }
    return rows


def build_payload() -> dict[str, Any]:
    hypergeometric = exact_hypergeometric_diagnostics()
    geometric_checks = geometric_start_diagnostics()
    normalization = finite_normalization_rows()

    expected = {
        "3": (4, 3),
        "4": (8, 6),
        "5": (15, 10),
        "6": (27, 20),
        "7": (49, 35),
        "8": (90, 70),
        "9": (164, 126),
        "10": (307, 252),
    }
    require(
        {
            key: (value["theta"], value["central_binomial"])
            for key, value in normalization.items()
        }
        == expected,
        normalization,
    )

    return {
        "status": [
            "GENERAL_CENTRAL_PRODUCT_SHADOW_SMOOTHING",
            "GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING",
            "SCALAR_TOWER_ROUTE_SEPARATED_FROM_GLYNN",
            "EXACT_FINITE_INTERFACES_REPLAYED",
        ],
        "theorem": {
            "central_smoothing": (
                "For k in [n/3,2n/3], "
                "F_(n,k)(b)/binom(n,k-1)^2 <= "
                "b/binom(n,k)^2 + O(n^(-1/2))."
            ),
            "parameterized_ceiling": (
                "For sqrt(n)<<w<<n, Theta_n/binom(n,floor(n/2)) "
                "=O(n/w+w/sqrt(n)+1)+"
                "O(sqrt(n)*exp(-2*w^2/n))."
            ),
            "optimized_ceiling": (
                "With w=ceil(n^(3/4)), "
                "Theta_n=O(n^(1/4)*binom(n,floor(n/2)))."
            ),
            "power_form": "Theta_n=O(2^n/n^(1/4)).",
            "route_gap": (
                "2^(n-1)/Theta_n=Omega(n^(1/4)); the complete scalar "
                "derivative tower cannot prove general Glynn optimality."
            ),
        },
        "finite_diagnostics": {
            **hypergeometric,
            "geometric_start_and_central_binomial_checks": geometric_checks,
            "normalization_rows": normalization,
        },
        "proof_parameter": {
            "window": "w_n=ceil(n^(3/4))",
            "central_band": "d=n/2+O(w_n)",
            "terminal_tail": "Hoeffding: 2^n*exp(-2*w_n^2/n)",
        },
        "claim_boundary": (
            "This is an upper ceiling on the lower bound certified by the "
            "complete scalar derivative-tower system, not an upper bound on "
            "the actual Chow rank. It introduces no new numerical finite-n "
            "lower bound, no border-rank result and no exact rank for n>=6. "
            "It does not rule out non-scalar, representation-valued, "
            "valuative or Chow-realizability arguments reaching Glynn. "
            "Literature novelty is not established."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    if FROZEN_DATA.exists():
        frozen = json.loads(FROZEN_DATA.read_text(encoding="utf-8"))
        require(frozen == payload, "frozen payload mismatch")

    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
