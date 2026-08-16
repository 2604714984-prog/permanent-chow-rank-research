#!/usr/bin/env python3
"""Independent finite replay for the scalar-tower polynomial ceiling.

This file imports none of the primary audit or historical shadow/tower code.
It reconstructs hypergeometric slice distributions directly from binomial
coefficients, verifies the adjacent-CDF smoothing inequality on a disjoint
range, and checks the exact finite normalization table used as regression
evidence for the asymptotic theorem.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import ceil, comb, floor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL_TOWER_DATA = ROOT / "data" / "general_full_degree_tower_envelope.json"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def distribution(n: int, sample_size: int) -> tuple[list[int], int]:
    left = n // 2
    right = n - left
    denominator = comb(n, sample_size)
    values = []
    for intersection in range(sample_size + 1):
        complement = sample_size - intersection
        if 0 <= intersection <= left and 0 <= complement <= right:
            values.append(comb(left, intersection) * comb(right, complement))
        else:
            values.append(0)
    require(sum(values) == denominator, (n, sample_size))
    return values, denominator


def check_hypergeometric_interface() -> tuple[int, int]:
    parameter_pairs = 0
    inequalities = 0

    # This range is intentionally different from the primary audit.
    for n in range(18, 66):
        for sample_size in range(ceil(2 * n / 5), floor(3 * n / 5) + 1):
            current, current_denominator = distribution(n, sample_size)
            previous, previous_denominator = distribution(n, sample_size - 1)
            atom = max(current)

            # Exact universal diagnostic bound: max atom <= 20/sqrt(n).
            require(
                n * atom * atom <= 400 * current_denominator * current_denominator,
                (n, sample_size),
            )

            current_prefix = 0
            previous_prefix = 0
            for threshold in range(-1, sample_size + 1):
                if threshold >= 0:
                    current_prefix += current[threshold]
                previous_index = threshold + 1
                if 0 <= previous_index < len(previous):
                    previous_prefix += previous[previous_index]

                require(
                    Fraction(previous_prefix, previous_denominator)
                    <= Fraction(current_prefix, current_denominator)
                    + Fraction(2 * atom, current_denominator),
                    (n, sample_size, threshold),
                )
                inequalities += 1

            parameter_pairs += 1

    return parameter_pairs, inequalities


def check_geometric_start() -> int:
    checks = 0
    for n in range(8, 161):
        running = 0
        for degree in range(1, (n - 1) // 2 + 1):
            running += comb(n, degree)
            require(
                running * (n - 2 * degree + 1)
                <= comb(n, degree) * (n - degree + 1),
                (n, degree),
            )
            checks += 1
    return checks


def check_finite_table() -> None:
    payload = json.loads(FULL_TOWER_DATA.read_text(encoding="utf-8"))
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
    observed = {
        key: (value["theta"], comb(int(key), int(key) // 2))
        for key, value in payload["thresholds"].items()
    }
    require(observed == expected, observed)


def main() -> int:
    pairs, inequalities = check_hypergeometric_interface()
    geometric = check_geometric_start()
    check_finite_table()

    print(f"independent_hypergeometric_parameter_pairs={pairs}")
    print(f"independent_adjacent_cdf_checks={inequalities}")
    print(f"independent_geometric_start_checks={geometric}")
    print("independent_ceiling=O(n^(1/4)*central_binomial)")
    print("GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_INDEPENDENT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
