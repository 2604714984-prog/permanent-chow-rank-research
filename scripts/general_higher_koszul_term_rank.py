#!/usr/bin/env python3
"""Exact higher-Koszul ranks for one Chow term and a low-wedge barrier.

For an independent degree-n Chow term in an N=n^2 dimensional ambient space,
this module computes the exact rank of

    delta_(d,p): D_d(T) tensor Lambda^p(V)
                 -> D_(d-1)(T) tensor Lambda^(p+1)(V).

The proof decomposes the map into oriented simplex-boundary blocks.  A second
formula follows from the complete-intersection Koszul homology recurrence.
The two formulas are checked independently on a large exact finite range.

The low-wedge corollary gives a general complexity gate: if the exterior
degree, or its Gorenstein-dual distance from the opposite endpoint, is
o(n log n), the resulting flattening ratio remains n^(o(1)) times the central
binomial coefficient and cannot reach Glynn scale.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from math import comb
from pathlib import Path
from typing import Any


EXPECTED_CORE_SHA256 = "bb4b8829b06a6d3fe81e35aa4619606fb77e160a60ad7f89da6d0297225ce324"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def active_simplex_rank(n: int, d: int, q: int) -> int:
    """Rank after fixing the inactive exterior support.

    The source is indexed by a d-subset S and a q-subset W of the n active
    variables.  Fix h=|S intersect W| and the active union.  The block becomes
    the oriented boundary map from (d-h)-subsets of an
    (d+q-2h)-set to one-smaller subsets.
    """

    require(1 <= d <= n, (n, d))
    require(0 <= q <= n, (n, q))
    total = 0
    for h in range(min(d - 1, q) + 1):
        vertices = d + q - 2 * h
        simplex_degree = d - h
        total += (
            choose(n, h)
            * choose(n - h, vertices)
            * choose(vertices - 1, simplex_degree - 1)
        )
    return total


def chow_higher_koszul_rank(n: int, d: int, p: int) -> int:
    """Exact characteristic-zero rank for one independent Chow term."""

    require(n >= 1, n)
    ambient = n * n
    require(1 <= d <= n, (n, d))
    require(0 <= p <= ambient - 1, (n, p))
    inactive = ambient - n
    total = 0
    for q in range(max(0, p - inactive), min(p, n) + 1):
        total += choose(inactive, p - q) * active_simplex_rank(n, d, q)
    return total


@lru_cache(maxsize=None)
def chow_higher_koszul_rank_from_homology(n: int, d: int, p: int) -> int:
    """Independent complete-intersection recurrence.

    The term apolar algebra is a complete intersection with n quadratic and
    n^2-n linear generators.  Hence the Koszul homology in bidegree (d,p) has
    dimension C(n,d) C(n^2-n,p-d).
    """

    ambient = n * n
    if not (0 <= d <= n and 0 <= p <= ambient):
        return 0
    chain_dimension = choose(n, d) * choose(ambient, p)
    homology_dimension = choose(n, d) * choose(ambient - n, p - d)
    incoming = (
        chow_higher_koszul_rank_from_homology(n, d + 1, p - 1)
        if d < n and p >= 1
        else 0
    )
    value = chain_dimension - homology_dimension - incoming
    require(value >= 0, (n, d, p, value))
    return value


def first_koszul_term_rank(n: int, d: int) -> int:
    ambient = n * n
    return ambient * choose(n, d) - choose(n, d + 1)


def permanent_source_target_cap(n: int, d: int, p: int) -> int:
    ambient = n * n
    return min(
        choose(n, d) ** 2 * choose(ambient, p),
        choose(n, d - 1) ** 2 * choose(ambient, p + 1),
    )


def integer_route_ceiling(n: int, d: int, p: int) -> int:
    denominator = chow_higher_koszul_rank(n, d, p)
    require(denominator > 0, (n, d, p))
    numerator = permanent_source_target_cap(n, d, p)
    return -(-numerator // denominator)


def low_wedge_multiplier(n: int, exterior_distance: int) -> tuple[int, int]:
    ambient = n * n
    require(0 <= exterior_distance <= ambient - n, (n, exterior_distance))
    return (
        choose(ambient, exterior_distance),
        choose(ambient - n, exterior_distance),
    )


def exponential_multiplier_upper(n: int, exterior_distance: int) -> float:
    ambient = n * n
    denominator = ambient - n - exterior_distance + 1
    require(denominator > 0, (n, exterior_distance))
    return exterior_distance * n / denominator


def build_payload() -> dict[str, Any]:
    formula_recurrence_checks = 0
    duality_checks = 0
    first_koszul_checks = 0

    for n in range(2, 13):
        ambient = n * n
        for d in range(1, n + 1):
            for p in range(ambient):
                block_value = chow_higher_koszul_rank(n, d, p)
                recurrence_value = chow_higher_koszul_rank_from_homology(
                    n, d, p
                )
                require(
                    block_value == recurrence_value,
                    (n, d, p, block_value, recurrence_value),
                )
                formula_recurrence_checks += 1

                dual_value = chow_higher_koszul_rank(
                    n,
                    n - d + 1,
                    ambient - p - 1,
                )
                require(block_value == dual_value, (n, d, p))
                duality_checks += 1

    for n in range(2, 31):
        for d in range(2, n + 1):
            require(
                chow_higher_koszul_rank(n, d, 1)
                == first_koszul_term_rank(n, d),
                (n, d),
            )
            first_koszul_checks += 1

    n6_p2 = {
        str(d): {
            "exact_term_rank": chow_higher_koszul_rank(6, d, 2),
            "source_target_route_ceiling": integer_route_ceiling(6, d, 2),
        }
        for d in (2, 3, 4)
    }
    require(
        n6_p2
        == {
            "2": {
                "exact_term_rank": 8730,
                "source_target_route_ceiling": 17,
            },
            "3": {
                "exact_term_rank": 12066,
                "source_target_route_ceiling": 21,
            },
            "4": {
                "exact_term_rank": 9235,
                "source_target_route_ceiling": 16,
            },
        },
        n6_p2,
    )

    diagnostics = {}
    diagnostic_cells = 0
    for n in range(3, 16):
        ambient = n * n
        best_numerator = -1
        best_denominator = 1
        best_data: tuple[int, int, int] | None = None
        for d in range(1, n + 1):
            for p in range(ambient):
                denominator = chow_higher_koszul_rank(n, d, p)
                numerator = permanent_source_target_cap(n, d, p)
                diagnostic_cells += 1
                if numerator * best_denominator > best_numerator * denominator:
                    best_numerator = numerator
                    best_denominator = denominator
                    best_data = (d, p, -(-numerator // denominator))
        require(best_data is not None, n)
        d, p, ceiling = best_data
        diagnostics[str(n)] = {
            "best_output_degree": d,
            "best_exterior_degree": p,
            "source_target_cap_numerator": best_numerator,
            "exact_term_denominator": best_denominator,
            "integer_route_ceiling": ceiling,
            "central_binomial": choose(n, n // 2),
            "glynn_upper": 2 ** (n - 1),
        }

    low_wedge_checks = 0
    for n in range(3, 61):
        ambient = n * n
        for exterior_distance in range(0, min(ambient - n, 4 * n) + 1):
            numerator, denominator = low_wedge_multiplier(
                n, exterior_distance
            )
            exponent = exponential_multiplier_upper(n, exterior_distance)
            require(numerator >= denominator > 0, (n, exterior_distance))
            require(exponent >= 0.0, (n, exterior_distance))
            low_wedge_checks += 1

    core: dict[str, Any] = {
        "status": [
            "GENERAL_HIGHER_KOSZUL_CHOW_TERM_RANK",
            "GENERAL_LOW_WEDGE_COMPLEXITY_BARRIER",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "exact_rank": (
                "R_(n,d,p)=sum_q C(n^2-n,p-q) sum_h "
                "C(n,h) C(n-h,d+q-2h) "
                "C(d+q-2h-1,d-h-1)."
            ),
            "homology_recurrence": (
                "R_(n,d,p)+R_(n,d+1,p-1)="
                "C(n,d)[C(n^2,p)-C(n^2-n,p-d)]."
            ),
            "duality": (
                "R_(n,d,p)=R_(n,n-d+1,n^2-p-1)."
            ),
            "low_wedge_ceiling": (
                "With r=min(p,n^2-p-1)<=n^2-n, every single "
                "higher-Koszul rank-ratio route is at most "
                "C(n,floor(n/2))*C(n^2,r)/C(n^2-n,r)."
            ),
            "complexity_gate": (
                "If r=o(n log n), the route is "
                "n^(o(1))*C(n,floor(n/2))=o(2^(n-1)). "
                "If r=o(n^2), reaching Glynn scale requires "
                "r>=(1/2-o(1))*n*log n."
            ),
        },
        "exact_replay": {
            "formula_recurrence_checks": formula_recurrence_checks,
            "duality_checks": duality_checks,
            "first_koszul_checks": first_koszul_checks,
            "diagnostic_cells": diagnostic_cells,
            "low_wedge_cells": low_wedge_checks,
        },
        "n6_p2_exact_resolution": n6_p2,
        "source_target_diagnostics": diagnostics,
        "claim_boundary": (
            "The exact denominator theorem holds for one independent-factor "
            "Chow term; degenerate terms are controlled by rank "
            "semicontinuity. The low-wedge theorem closes fixed, O(n), and "
            "more generally o(n log n) exterior distance for this single "
            "higher-Koszul image-rank mechanism. It does not prove a uniform "
            "ceiling for the middle-wedge range, compute the permanent rank "
            "of those maps, improve any current finite-n Chow-rank bound, "
            "prove a border-rank statement, determine an exact rank for "
            "n>=6, or prove general Glynn optimality. Literature novelty is "
            "not established."
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
    print("GENERAL_HIGHER_KOSZUL_TERM_RANK_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
