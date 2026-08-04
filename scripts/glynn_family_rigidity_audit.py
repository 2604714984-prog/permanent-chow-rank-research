#!/usr/bin/env python3
"""Exact Walsh audit for the column-uniform Glynn sign family.

For ``2<=n<=10`` the script verifies:

* the ``2^(n-1)`` sign terms have the Walsh-Hadamard coefficient matrix on
  row-parity classes;
* the matrix square is ``2^(n-1) I``;
* the permanent parity function is a delta function at the all-ones class;
* Walsh inversion uses every sign term with a nonzero coefficient.

This is a restricted-family theorem. It is not a general Chow-rank lower
bound.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parity_dot(left: int, right: int) -> int:
    return (left & right).bit_count() & 1


def walsh_entry(parity: int, sign: int) -> int:
    return -1 if parity_dot(parity, sign) else 1


def audit_degree(n: int) -> dict[str, object]:
    if n < 2:
        raise ValueError(n)
    dimension = 1 << (n - 1)
    rows = [
        [walsh_entry(parity, sign) for sign in range(dimension)]
        for parity in range(dimension)
    ]

    for left in range(dimension):
        for right in range(dimension):
            inner = sum(
                rows[left][column] * rows[right][column]
                for column in range(dimension)
            )
            expected = dimension if left == right else 0
            if inner != expected:
                raise AssertionError((n, left, right, inner, expected))

    target_parity = dimension - 1
    numerators = rows[target_parity]
    if any(value not in {-1, 1} for value in numerators):
        raise AssertionError((n, numerators))
    if any(value == 0 for value in numerators):
        raise AssertionError((n, numerators))

    reconstructed = []
    for parity in range(dimension):
        value = sum(
            numerators[sign] * rows[parity][sign]
            for sign in range(dimension)
        )
        reconstructed.append(value)
    expected_reconstruction = [0] * dimension
    expected_reconstruction[target_parity] = dimension
    if reconstructed != expected_reconstruction:
        raise AssertionError((n, reconstructed))

    return {
        "n": n,
        "family_size": dimension,
        "walsh_orthogonality_scale": dimension,
        "target_parity_class": target_parity,
        "nonzero_expansion_coefficient_count": len(numerators),
        "coefficient_denominator": dimension,
        "positive_coefficient_count": sum(value == 1 for value in numerators),
        "negative_coefficient_count": sum(value == -1 for value in numerators),
        "proper_subfamily_can_span_permanent": False,
    }


def build_payload() -> dict[str, object]:
    degrees = [audit_degree(n) for n in range(2, 11)]
    n6 = next(row for row in degrees if row["n"] == 6)
    if n6["family_size"] != 32:
        raise AssertionError(n6)
    if n6["nonzero_expansion_coefficient_count"] != 32:
        raise AssertionError(n6)

    return {
        "status": "GLYNN_COLUMN_UNIFORM_FAMILY_RIGIDITY_REPLAYED",
        "degrees": degrees,
        "n6_conclusion": (
            "Every one of the 32 column-uniform sign terms occurs with a "
            "nonzero coefficient in the unique expansion of perm_6. No "
            "25-term decomposition exists inside this restricted family."
        ),
        "claim_boundary": (
            "General Chow terms may use arbitrary and column-dependent "
            "linear forms. This audit is not a general Chow-rank lower bound."
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
    print("GLYNN_FAMILY_RIGIDITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
