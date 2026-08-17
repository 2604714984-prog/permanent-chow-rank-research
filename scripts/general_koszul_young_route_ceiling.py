#!/usr/bin/env python3
"""Audit a central-binomial ceiling for all standard Koszul--Young flattenings.

For a degree-n form in N=n^2 variables, the standard Koszul--Young map is

    K_(m,p)(f): S^(n-m)V* tensor Lambda^p V
                 -> S^(m-1)V tensor Lambda^(p+1)V.

The proof document shows that one independent-factor Chow term has rank at
least one quarter of the smaller term-side source/target dimension.  Since the
permanent derivative dimensions are binom(n,m)^2, every rank-ratio lower bound
from one standard Koszul--Young map, or a block diagonal direct sum of such
maps, is at most four times the central binomial coefficient.

This script performs exact integer reconstruction of the Boolean term ranks,
the component boundary ranks, duality, the quarter-rank inequality and the
resulting finite route ceilings.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any


EXPECTED_CORE_SHA256 = "12c52a1ae78bd4f7526dfb78cd18a0fc56bae2bd97f5736526a5ec262cfa39d4"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def ceil_div(a: int, b: int) -> int:
    require(b > 0, b)
    return -(-a // b)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def active_component_rank(n: int, m: int, a: int) -> int:
    """Rank on B_n[m] tensor Lambda^a(k^n), by simplex components.

    A basis pair consists of an m-subset S and an a-subset A.  The Koszul
    differential preserves I=S intersect A and J=S union A.  On each fixed
    (I,J) component it is the oriented boundary from q-subsets to
    (q-1)-subsets of an r-set, of rank binom(r-1,q-1).
    """

    require(1 <= m <= n, (n, m))
    require(0 <= a <= n, (n, a))
    total = 0
    for t in range(min(m, a) + 1):
        r = m + a - 2 * t
        q = m - t
        if not (0 <= r <= n - t and 1 <= q <= r):
            continue
        component_count = choose(n, t) * choose(n - t, r)
        boundary_rank = choose(r - 1, q - 1)
        total += component_count * boundary_rank
    return total


def active_dimensions(n: int, m: int, a: int) -> tuple[int, int]:
    return choose(n, m) * choose(n, a), choose(n, m - 1) * choose(n, a + 1)


def term_rank(n: int, m: int, p: int) -> int:
    """Exact rank for an independent-factor term in N=n^2 variables."""

    N = n * n
    inactive = N - n
    require(1 <= m <= n, (n, m))
    require(0 <= p <= N - 1, (n, p))
    total = 0
    for a in range(max(0, p - inactive), min(n, p) + 1):
        h = p - a
        total += choose(inactive, h) * active_component_rank(n, m, a)
    return total


def term_dimensions(n: int, m: int, p: int) -> tuple[int, int]:
    N = n * n
    return (
        choose(n, m) * choose(N, p),
        choose(n, m - 1) * choose(N, p + 1),
    )


def permanent_dimension_cap(n: int, m: int, p: int) -> int:
    """Source/target cap for the permanent Koszul--Young rank."""

    N = n * n
    source = choose(n, m) ** 2 * choose(N, p)
    target = choose(n, m - 1) ** 2 * choose(N, p + 1)
    return min(source, target)


def route_ceiling(n: int, m: int, p: int) -> int:
    denominator = term_rank(n, m, p)
    require(denominator > 0, (n, m, p))
    return ceil_div(permanent_dimension_cap(n, m, p), denominator)


def build_payload() -> dict[str, Any]:
    active_half_checks = 0
    term_quarter_checks = 0
    duality_checks = 0
    route_ceiling_checks = 0
    finite_maxima: dict[str, Any] = {}

    for n in range(2, 13):
        N = n * n
        central = choose(n, n // 2)
        best = (-1, -1, -1)

        for m in range(1, n + 1):
            for a in range(n + 1):
                rank = active_component_rank(n, m, a)
                source, target = active_dimensions(n, m, a)
                require(2 * rank >= min(source, target), (n, m, a, rank, source, target))
                active_half_checks += 1

            for p in range(N):
                rank = term_rank(n, m, p)
                source, target = term_dimensions(n, m, p)
                require(4 * rank >= min(source, target), (n, m, p, rank, source, target))
                term_quarter_checks += 1

                dual_rank = term_rank(n, n - m + 1, N - p - 1)
                require(rank == dual_rank, (n, m, p, rank, dual_rank))
                duality_checks += 1

                ceiling = route_ceiling(n, m, p)
                require(ceiling <= 4 * central, (n, m, p, ceiling, central))
                route_ceiling_checks += 1
                if ceiling > best[0]:
                    best = (ceiling, m, p)

        finite_maxima[str(n)] = {
            "central_binomial": central,
            "four_central_ceiling": 4 * central,
            "maximum_dimension_route_ceiling": best[0],
            "attaining_output_degree": best[1],
            "attaining_wedge_degree": best[2],
            "glynn_upper": 2 ** (n - 1),
        }

    require(active_half_checks == 726, active_half_checks)
    require(term_quarter_checks == 6083, term_quarter_checks)
    require(duality_checks == 6083, duality_checks)
    require(route_ceiling_checks == 6083, route_ceiling_checks)

    expected_maxima = {
        "2": 2,
        "3": 5,
        "4": 8,
        "5": 17,
        "6": 30,
        "7": 61,
        "8": 110,
        "9": 225,
        "10": 413,
        "11": 840,
        "12": 1565,
    }
    require(
        {key: value["maximum_dimension_route_ceiling"] for key, value in finite_maxima.items()}
        == expected_maxima,
        finite_maxima,
    )

    core: dict[str, Any] = {
        "status": [
            "GENERAL_STANDARD_KOSZUL_YOUNG_ROUTE_CEILING",
            "ALL_WEDGE_DEGREES",
            "FINITE_DIRECT_SUMS_CLOSED",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "term_quarter_rank": (
                "For every independent degree-n Chow term in N=n^2 variables, "
                "rank K_(m,p)(T) >= (1/4)*min(term source dimension, term target dimension)."
            ),
            "single_map_ceiling": (
                "Every standard Koszul--Young rank-ratio lower bound for perm_n "
                "is at most 4*binom(n,floor(n/2))."
            ),
            "direct_sum_ceiling": (
                "Every finite block-diagonal direct sum of standard Koszul--Young maps "
                "has the same 4*central-binomial ceiling."
            ),
            "asymptotic_gap": (
                "The named route remains Omega(sqrt(n)) below the Glynn scale 2^(n-1)."
            ),
        },
        "exact_replay": {
            "n_min": 2,
            "n_max": 12,
            "active_half_rank_checks": active_half_checks,
            "term_quarter_rank_checks": term_quarter_checks,
            "transpose_duality_checks": duality_checks,
            "route_ceiling_checks": route_ceiling_checks,
            "finite_maxima": finite_maxima,
        },
        "claim_boundary": (
            "This is a ceiling on the standard exterior Koszul--Young flattenings and "
            "their finite block-diagonal direct sums. It is not an upper bound on actual "
            "Chow rank and does not cover representation projections, arbitrary Young/Pieri "
            "flattenings, nonlinear minors, higher syzygy modules, valuative arguments, "
            "Chow-realizability defects, border rank, exact rank for n>=6, or general "
            "Glynn optimality. Literature novelty is not established."
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
    print("GENERAL_KOSZUL_YOUNG_ROUTE_CEILING_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
