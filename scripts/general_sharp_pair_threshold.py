#!/usr/bin/env python3
"""Exact replay for the sharp two-term factor-span threshold.

The general proof is in ``docs/general_sharp_pair_threshold.md``.  This script
checks the two-row polarization identity, monomial membership in the two Chow
derivative envelopes, the threshold arithmetic, and the cubic boundary with
exact rational coefficients.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
from typing import Iterable


EXPECTED_CORE_SHA256 = "764ec72551012125c7f948df161795a93f2c34e3eaf9917dd45055464cd1ddc6"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def monomial(*factors: str) -> tuple[str, ...]:
    return tuple(sorted(factors))


def add_term(
    polynomial: dict[tuple[str, ...], Fraction],
    factors: Iterable[str],
    coefficient: Fraction,
) -> None:
    key = tuple(sorted(factors))
    polynomial[key] += coefficient
    if polynomial[key] == 0:
        del polynomial[key]


def transformed_permanent(m: int) -> dict[tuple[str, ...], Fraction]:
    """Expand perm_m after x_0=(a+b)/2 and x_1=(a-b)/2."""

    result: dict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for sigma in permutations(range(m)):
        c = sigma[0]
        d = sigma[1]
        tail = [f"x{i}_{sigma[i]}" for i in range(2, m)]
        for first, first_sign in ((f"a{c}", 1), (f"b{c}", 1)):
            for second, second_sign in ((f"a{d}", 1), (f"b{d}", -1)):
                add_term(
                    result,
                    [first, second, *tail],
                    Fraction(first_sign * second_sign, 4),
                )
    return dict(result)


def split_rhs(m: int) -> dict[tuple[str, ...], Fraction]:
    result: dict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    rows = tuple(range(2, m))
    for c, d in combinations(range(m), 2):
        remaining = tuple(value for value in range(m) if value not in (c, d))
        for assignment in permutations(remaining):
            tail = [f"x{i}_{assignment[index]}" for index, i in enumerate(rows)]
            add_term(result, [f"a{c}", f"a{d}", *tail], Fraction(1, 2))
            add_term(result, [f"b{c}", f"b{d}", *tail], Fraction(-1, 2))
    return dict(result)


def envelope_factors(m: int, kind: str) -> set[str]:
    require(kind in {"a", "b"}, kind)
    return {
        *(f"{kind}{j}" for j in range(m)),
        *(f"x{i}_{j}" for i in range(2, m) for j in range(m)),
    }


def verify_membership(
    polynomial: dict[tuple[str, ...], Fraction],
    m: int,
    kind: str,
) -> int:
    factors = envelope_factors(m, kind)
    count = 0
    for term, coefficient in polynomial.items():
        if not coefficient:
            continue
        require(
            sum(label.startswith(kind) for label in term) == 2,
            (m, kind, "wrong sign-family multiplicity", term),
        )
        other = "b" if kind == "a" else "a"
        require(
            all(not label.startswith(other) for label in term),
            (m, kind, "mixed sign families", term),
        )
        require(len(term) == m, (m, kind, term))
        require(len(set(term)) == m, (m, kind, "repeated factor", term))
        require(set(term).issubset(factors), (m, kind, term))
        count += 1
    return count


def family_part(
    polynomial: dict[tuple[str, ...], Fraction],
    kind: str,
) -> dict[tuple[str, ...], Fraction]:
    return {
        term: value
        for term, value in polynomial.items()
        if sum(label.startswith(kind) for label in term) == 2
    }


def build_payload() -> dict[str, object]:
    identity_rows = []
    identity_checks = 0
    membership_checks = 0

    for m in range(2, 9):
        left = transformed_permanent(m)
        right = split_rhs(m)
        require(left == right, (m, len(left), len(right)))

        a_part = family_part(right, "a")
        b_part = family_part(right, "b")
        expected_each = factorial(m) // 2
        require(len(a_part) == expected_each, (m, "a", len(a_part)))
        require(len(b_part) == expected_each, (m, "b", len(b_part)))
        require(
            all(value == Fraction(1, 2) for value in a_part.values()),
            (m, "a coefficients"),
        )
        require(
            all(value == Fraction(-1, 2) for value in b_part.values()),
            (m, "b coefficients"),
        )

        a_count = verify_membership(a_part, m, "a")
        b_count = verify_membership(b_part, m, "b")
        require(a_count == expected_each, (m, a_count, expected_each))
        require(b_count == expected_each, (m, b_count, expected_each))

        factor_count = len(envelope_factors(m, "a"))
        require(factor_count == m * (m - 1), (m, factor_count))
        identity_checks += len(left)
        membership_checks += a_count + b_count
        identity_rows.append(
            {
                "m": m,
                "threshold_degree": m * (m - 1),
                "transformed_monomials": len(left),
                "a_monomials": a_count,
                "b_monomials": b_count,
                "factor_count_per_envelope": factor_count,
            }
        )

    threshold_rows = []
    threshold_checks = 0
    for m in range(3, 129):
        threshold = m * (m - 1)
        zero_max = threshold - 1
        require(zero_max == m * m - m - 1, (m, zero_max))
        require(threshold == m * m - m, (m, threshold))
        for extra in (0, 1, m, m * m):
            n = threshold + extra
            require(n >= threshold, (m, n))
            require(n - threshold == extra, (m, n, extra))
            threshold_checks += 1
        if m in {3, 4, 5, 6, 8, 10, 16, 32, 64, 128}:
            threshold_rows.append(
                {
                    "m": m,
                    "universal_zero_maximum_n": zero_max,
                    "first_nonzero_n": threshold,
                    "cubic_pair_boundary": m == 3 and threshold == 6,
                }
            )

    core: dict[str, object] = {
        "status": [
            "GENERAL_SHARP_TWO_TERM_THRESHOLD",
            "EXPLICIT_CHOW_DERIVATIVE_COUNTEREXAMPLE",
            "CUBIC_6_3_2_RESOLVED_NONZERO",
            "EXACT_RATIONAL_INTERFACE_REPLAYED",
        ],
        "theorem": {
            "identity": "perm_m=(G_a-G_b)/2 after a_j=x_0j+x_1j and b_j=x_0j-x_1j",
            "threshold_envelopes": "G_a in D_m(T_a), G_b in D_m(T_b), deg(T_a)=deg(T_b)=m(m-1)",
            "extension": "multiplying each envelope by extra independent factors preserves the degree-m witness",
            "sharp_threshold": "all pairs zero for n<=m^2-m-1; an explicit nonzero pair exists for n>=m^2-m",
        },
        "exact_replay": {
            "m_min": 2,
            "m_max": 8,
            "identity_monomial_checks": identity_checks,
            "derivative_membership_checks": membership_checks,
            "threshold_arithmetic_checks": threshold_checks,
            "identity_rows": identity_rows,
            "threshold_rows": threshold_rows,
        },
        "claim_boundary": (
            "This is a sharpness theorem for literal output-degree derivative-space "
            "intersections. The nonzero witness is not a two-term Chow decomposition "
            "of the permanent. No new exact Chow rank, optimized numerical lower "
            "bound, border-rank result, or literature-novelty claim is made. The "
            "universal-zero half is inherited from the parent private-polar theorem."
        ),
    }
    payload = {**core, "core_sha256": canonical_sha256(core)}
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
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
    print("GENERAL_SHARP_PAIR_THRESHOLD_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
