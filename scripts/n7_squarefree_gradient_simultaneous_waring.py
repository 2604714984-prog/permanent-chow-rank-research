#!/usr/bin/env python3
"""Exact apolar lower bound for the squarefree septic gradient.

This certificate concerns the seven sextics obtained by differentiating
``x_0 ... x_6``.  It closes the column-uniform 49-term endpoint only; it does
not assert that an arbitrary Chow decomposition is column-uniform.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_squarefree_gradient_simultaneous_waring.json"
N = 7


def annihilates(exponent: tuple[int, ...], missing: int) -> bool:
    """Whether the differential monomial annihilates prod_{i != missing} x_i."""

    return any(value > (0 if index == missing else 1) for index, value in enumerate(exponent))


def in_common_apolar_ideal(exponent: tuple[int, ...]) -> bool:
    return all(annihilates(exponent, missing) for missing in range(N))


def in_coordinate_colon_section(exponent: tuple[int, ...]) -> bool:
    """Membership in (Y_0) + ((intersection M_i^perp) : Y_0)."""

    if exponent[0] > 0:
        return True
    shifted = list(exponent)
    shifted[0] += 1
    return in_common_apolar_ideal(tuple(shifted))


def compositions(total: int, length: int, prefix: tuple[int, ...] = ()):
    if length == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, length - 1, prefix + (value,))


def multinomial(exponent: tuple[int, ...]) -> int:
    value = factorial(sum(exponent))
    for part in exponent:
        value //= factorial(part)
    return value


def glynn_numerator_coefficient(exponent: tuple[int, ...]) -> int:
    """Numerator before division by 2^(n-1)n! in the polarization identity."""

    sign_sum = 0
    for tail in product((-1, 1), repeat=N - 1):
        signs = (1, *tail)
        term = 1
        for sign, power in zip(signs, exponent):
            term *= sign ** (power + 1)
        sign_sum += term
    return multinomial(exponent) * sign_sum


def build_payload() -> dict[str, object]:
    bounded = tuple(product(range(3), repeat=N))
    common = tuple(exponent for exponent in bounded if in_common_apolar_ideal(exponent))
    generator_test = all(
        in_common_apolar_ideal(exponent)
        == (any(value >= 2 for value in exponent) or all(value >= 1 for value in exponent))
        for exponent in bounded
    )

    standard = tuple(exponent for exponent in bounded if not in_coordinate_colon_section(exponent))
    hilbert = [sum(sum(exponent) == degree for exponent in standard) for degree in range(N)]

    degree_n = tuple(compositions(N, N))
    coefficients = {
        exponent: glynn_numerator_coefficient(exponent) for exponent in degree_n
    }
    target = (1,) * N
    denominator = 2 ** (N - 1) * factorial(N)
    identity_ok = coefficients[target] == denominator and all(
        value == 0 for exponent, value in coefficients.items() if exponent != target
    )

    assert generator_test
    assert len(common) > 0
    assert hilbert == [1, 6, 15, 20, 15, 6, 0]
    assert len(standard) == 63
    assert identity_ok

    return {
        "status": "EXACT_COLUMN_UNIFORM_ENDPOINT_EXCLUSION",
        "field": "characteristic zero",
        "n": N,
        "collection": "the seven first derivatives of x_0*x_1*...*x_6",
        "common_apolar_ideal": {
            "generators": ["Y_i^2 for 0 <= i < 7", "Y_0*Y_1*...*Y_6"],
            "bounded_monomial_membership_check_count": len(bounded),
            "generator_description_verified": generator_test,
        },
        "coordinate_colon_section": {
            "linear_form": "Y_0",
            "ideal": "(Y_0) + ((intersection_i M_i^perp) : Y_0)",
            "standard_monomial_hilbert_vector": hilbert,
            "standard_monomial_count": len(standard),
        },
        "simultaneous_waring": {
            "apolar_lower_bound": len(standard),
            "glynn_differentiated_upper_bound": 2 ** (N - 1),
            "strict_interval": [len(standard), 2 ** (N - 1)],
        },
        "glynn_identity_check": {
            "degree_seven_coefficient_count": len(degree_n),
            "normalizing_denominator": denominator,
            "nonzero_coefficient_count": sum(value != 0 for value in coefficients.values()),
            "identity_verified": identity_ok,
            "shared_sixth_power_count_after_differentiation": 2 ** (N - 1),
        },
        "endpoint_consequence": {
            "forbidden_shared_power_count": 49,
            "excluded": 49 < len(standard),
            "scope": "column-uniform/tensor-split endpoint only",
        },
        "claim_boundary": [
            "This does not prove that every 49-term Chow endpoint is column-uniform.",
            "It does not prove ordinary ChowRank(perm_7) >= 50 by itself.",
            "It makes no statement about border Chow rank.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS")
    elif args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
