#!/usr/bin/env python3
"""Exact audit for the derivative-profile ceiling theorem.

For a degree-``n`` polynomial ``f``, write

    h_m(f) = dim D_m(f) = rank C_{n-m,m}(f).

The companion proof shows that every monotone, positively homogeneous,
subadditive lower-bound functional that factors only through the vector
``(h_0,...,h_n)`` is bounded by the central binomial coefficient on
``perm_n``.  The script replays the finite arithmetic interfaces:

* the generic Chow-term profile ``binom(n,m)``;
* the permanent profile ``binom(n,m)^2``;
* the coordinatewise domination by ``M_n binom(n,m)``;
* the Vandermonde identity for the equal-weight all-degree direct sum; and
* exact weighted-ratio checks through ``n=50``.

No floating point, random search, or finite-field calculation is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import ceil, comb
from pathlib import Path
from typing import Sequence

DEFAULT_MAX_N = 50


def term_profile(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return [comb(n, m) for m in range(n + 1)]


def permanent_profile(n: int) -> list[int]:
    return [value * value for value in term_profile(n)]


def central_bound(n: int) -> int:
    return comb(n, n // 2)


def central_degrees(n: int) -> list[int]:
    bound = central_bound(n)
    return [m for m, value in enumerate(term_profile(n)) if value == bound]


def fraction_payload(value: Fraction) -> dict[str, int]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def weighted_profile_ratio(n: int, weights: Sequence[int]) -> Fraction:
    """Return the normalized scalar profile ratio for nonnegative weights."""

    if len(weights) != n + 1:
        raise ValueError("weights must have length n+1")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights must be nonnegative")
    if not any(weights):
        raise ValueError("at least one weight must be positive")

    chow = term_profile(n)
    permanent = permanent_profile(n)
    numerator = sum(weight * value for weight, value in zip(weights, permanent))
    denominator = sum(weight * value for weight, value in zip(weights, chow))
    if denominator <= 0:
        raise AssertionError("positive weights produced a zero denominator")
    return Fraction(numerator, denominator)


def deterministic_weight_families(n: int) -> dict[str, list[int]]:
    """Small exact stress set for the weighted direct-sum corollary."""

    chow = term_profile(n)
    central = set(central_degrees(n))
    return {
        "equal": [1] * (n + 1),
        "degree_plus_one": [m + 1 for m in range(n + 1)],
        "reverse_degree_plus_one": [n - m + 1 for m in range(n + 1)],
        "binomial": chow,
        "endpoints": [1 if m in {0, n} else 0 for m in range(n + 1)],
        "central_only": [1 if m in central else 0 for m in range(n + 1)],
        "alternating_support": [1 if m % 2 == 0 else 0 for m in range(n + 1)],
    }


def validate_boolean_weight_supports(max_n: int = 12) -> int:
    """Exhaustively replay the equality condition for small Boolean supports."""

    checked = 0
    for n in range(2, max_n + 1):
        central = set(central_degrees(n))
        bound = central_bound(n)
        for mask in range(1, 1 << (n + 1)):
            weights = [
                1 if (mask >> m) & 1 else 0
                for m in range(n + 1)
            ]
            ratio = weighted_profile_ratio(n, weights)
            if ratio > bound:
                raise AssertionError((n, mask, ratio, bound))
            support_is_central = all(
                m in central
                for m, weight in enumerate(weights)
                if weight
            )
            if (ratio == bound) != support_is_central:
                raise AssertionError(
                    (n, mask, ratio, bound, support_is_central)
                )
            checked += 1
    return checked


def canonical_profile_sha256(n: int) -> str:
    chow = term_profile(n)
    permanent = permanent_profile(n)
    bound = central_bound(n)
    payload = {
        "n": n,
        "term_profile": chow,
        "permanent_profile": permanent,
        "coordinatewise_slacks": [
            bound * chow[m] - permanent[m] for m in range(n + 1)
        ],
    }
    encoded = (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_degree(n: int) -> dict[str, object]:
    chow = term_profile(n)
    permanent = permanent_profile(n)
    bound = central_bound(n)
    central = central_degrees(n)

    if max(chow) != bound:
        raise AssertionError((n, max(chow), bound))
    if central != ([n // 2] if n % 2 == 0 else [n // 2, n // 2 + 1]):
        raise AssertionError((n, central))
    if any(
        permanent[m] > bound * chow[m]
        for m in range(n + 1)
    ):
        raise AssertionError((n, "coordinatewise profile ceiling failed"))
    equality_degrees = [
        m
        for m in range(n + 1)
        if permanent[m] == bound * chow[m]
    ]
    if equality_degrees != central:
        raise AssertionError((n, equality_degrees, central))

    if sum(chow) != 2**n:
        raise AssertionError((n, sum(chow), 2**n))
    if sum(permanent) != comb(2 * n, n):
        raise AssertionError((n, sum(permanent), comb(2 * n, n)))

    all_degree_ratio = Fraction(sum(permanent), sum(chow))
    expected_all_degree = Fraction(comb(2 * n, n), 2**n)
    if all_degree_ratio != expected_all_degree:
        raise AssertionError((n, all_degree_ratio, expected_all_degree))
    if n >= 2 and not all_degree_ratio < bound:
        raise AssertionError((n, all_degree_ratio, bound))

    weighted_checks: dict[str, dict[str, int]] = {}
    for name, weights in deterministic_weight_families(n).items():
        ratio = weighted_profile_ratio(n, weights)
        if ratio > bound:
            raise AssertionError((n, name, ratio, bound))
        if name == "central_only" and ratio != bound:
            raise AssertionError((n, name, ratio, bound))
        if name != "central_only" and all(
            weights[m] == 0 for m in range(n + 1) if m not in central
        ):
            raise AssertionError((n, name, "unexpected central-only support"))
        weighted_checks[name] = fraction_payload(ratio)

    glynn_upper = 2 ** (n - 1)
    if n == 2:
        if glynn_upper != bound:
            raise AssertionError((n, glynn_upper, bound))
    elif n >= 3 and not glynn_upper > bound:
        raise AssertionError((n, glynn_upper, bound))

    return {
        "n": n,
        "central_bound": bound,
        "central_degrees": central,
        "glynn_upper_bound": glynn_upper,
        "glynn_to_profile_ceiling": fraction_payload(
            Fraction(glynn_upper, bound)
        ),
        "all_degree_direct_sum_ratio": {
            **fraction_payload(all_degree_ratio),
            "ceiling": ceil(all_degree_ratio),
        },
        "deterministic_weight_check_count": len(weighted_checks),
        "full_profile_sha256": canonical_profile_sha256(n),
    }


def build_payload(max_n: int = DEFAULT_MAX_N) -> dict[str, object]:
    if max_n < 3:
        raise ValueError("max_n must be at least 3")

    rows = [validate_degree(n) for n in range(2, max_n + 1)]
    rows_encoded = (
        json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    selected_degrees = sorted(
        {
            *range(2, min(max_n, 12) + 1),
            *(
                degree
                for degree in (20, 30, 40, max_n)
                if degree <= max_n
            ),
        }
    )
    selected_rows = [
        rows[degree - 2]
        for degree in selected_degrees
    ]
    boolean_supports_checked = validate_boolean_weight_supports(
        min(max_n, 12)
    )
    return {
        "status": "GENERAL_DERIVATIVE_PROFILE_CEILING_REPLAYED",
        "tested_degree_range": [2, max_n],
        "validated_degree_count": len(rows),
        "all_degree_rows_sha256": hashlib.sha256(rows_encoded).hexdigest(),
        "selected_rows": selected_rows,
        "boolean_weight_supports_checked_through_n12": (
            boolean_supports_checked
        ),
        "theorem": {
            "profile_ceiling": (
                "Every monotone, positively homogeneous, subadditive "
                "Chow-rank lower-bound functional that factors only through "
                "(dim D_0(f),...,dim D_n(f)) is at most "
                "binom(n,floor(n/2)) on perm_n."
            ),
            "weighted_direct_sum_corollary": (
                "Every nonnegative weighted direct sum of scalar "
                "catalecticants has normalized rank ratio at most the "
                "central binomial coefficient; equality requires support "
                "only in central degree(s)."
            ),
            "asymptotic_missing_factor": (
                "The Glynn upper bound divided by the profile ceiling is "
                "asymptotic to sqrt(pi*n/8)."
            ),
        },
        "claim_boundary": (
            "The theorem applies only to invariants that factor through the "
            "scalar derivative-dimension profile. It does not constrain "
            "Koszul maps, cross-degree incidence, multigraded syzygies, "
            "representation-valued homology, quotient geometry, or coupled "
            "relation modules."
        ),
        "next_route": (
            "Any route to the conjectural 2^(n-1) lower bound must use "
            "structure discarded by the scalar profile, such as maps "
            "between derivative degrees or relations among summands."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=DEFAULT_MAX_N)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    payload = build_payload(args.max_n)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("GENERAL_DERIVATIVE_PROFILE_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
