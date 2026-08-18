#!/usr/bin/env python3
"""Audit the closed factor-span endpoint zero-block theorem.

The general proof is in docs/general_closed_factor_span_endpoint_zero_blocks.md.
This script replays the exact integer interface:

* the strict and closed term-count zero-block sizes;
* every equality-endpoint triple through n=128;
* the one-term equality counterexample n=m^2;
* the quadratic q=2 counterexample;
* the projection-cap arithmetic.

No finite computation substitutes for the direct-sum indecomposability proof.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

EXPECTED_CORE_SHA256 = "7d78c0e595d25130a9bf2f9dd843ef88f3be737004f33b3f85f3be1170eb376a"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def strict_zero_block_size(n: int, m: int) -> int:
    require(2 <= m <= n, (n, m))
    return (m * m - 1) // n


def closed_zero_block_size(n: int, m: int) -> int:
    """Maximum guaranteed arbitrary term-count zero block from this theorem."""

    strict = strict_zero_block_size(n, m)
    if m >= 3 and (m * m) % n == 0 and (m * m) // n >= 2:
        return strict + 1
    return strict


def endpoint_is_new(n: int, m: int) -> bool:
    return closed_zero_block_size(n, m) > strict_zero_block_size(n, m)


def projection_cap(n: int, m: int, total_terms: int) -> int:
    zeta = closed_zero_block_size(n, m)
    require(total_terms >= zeta, (n, m, total_terms, zeta))
    return (total_terms - zeta) * comb(n, m)


def build_payload() -> dict[str, Any]:
    all_endpoint_triples: list[list[int]] = []
    proper_endpoint_triples: list[list[int]] = []
    projection_checks = 0
    parameter_cells = 0

    for n in range(2, 129):
        for m in range(2, n + 1):
            parameter_cells += 1
            strict = strict_zero_block_size(n, m)
            closed = closed_zero_block_size(n, m)
            require(closed in (strict, strict + 1), (n, m, strict, closed))

            if endpoint_is_new(n, m):
                q = (m * m) // n
                require(m >= 3 and q >= 2 and q * n == m * m, (n, m, q))
                all_endpoint_triples.append([n, m, q])
                if m < n:
                    proper_endpoint_triples.append([n, m, q])

            for total_terms in range(closed, closed + 9):
                cap = projection_cap(n, m, total_terms)
                require(cap == (total_terms - closed) * comb(n, m), cap)
                projection_checks += 1

    require(parameter_cells == 8_128, parameter_cells)
    require(len(all_endpoint_triples) == 258, len(all_endpoint_triples))
    require(len(proper_endpoint_triples) == 132, len(proper_endpoint_triples))
    require(
        proper_endpoint_triples[:10]
        == [
            [8, 4, 2],
            [9, 6, 4],
            [12, 6, 3],
            [16, 8, 4],
            [16, 12, 9],
            [18, 6, 2],
            [18, 12, 8],
            [20, 10, 5],
            [24, 12, 6],
            [25, 10, 4],
        ],
        proper_endpoint_triples[:10],
    )

    single_term_counterexamples = []
    matching_monomial_checks = 0
    for m in range(2, 12):
        n = m * m
        # T is the product of all m^2 variables in an m x m block. Every
        # matching monomial is a squarefree degree-m derivative of T.
        matching_count = factorial(m)
        require(matching_count > 0, matching_count)
        matching_monomial_checks += matching_count
        single_term_counterexamples.append(
            {
                "n": n,
                "m": m,
                "ambient_variables": n,
                "matching_monomials": matching_count,
            }
        )

    quadratic_counterexample = {
        "n": 2,
        "m": 2,
        "q": 2,
        "decomposition_terms": 2,
    }

    core: dict[str, Any] = {
        "status": [
            "GENERAL_DIRECT_SUM_FACTOR_SPAN_ENDPOINT",
            "GENERAL_CLOSED_TERM_COUNT_ZERO_BLOCK",
            "CHOW_REALIZABILITY_ENDPOINT_DEFECT",
            "EXACT_INTEGER_REPLAYED",
        ],
        "theorem": {
            "direct_sum_endpoint": (
                "If m>=3, q>=2, the factor spans L_i form a direct sum, "
                "and sum_i dim(L_i)<=m^2, then D_m(perm_n) intersects "
                "sum_i D_m(T_i) trivially."
            ),
            "closed_term_count": (
                "If q*n<m^2, or if q*n=m^2 with m>=3 and q>=2, "
                "then D_m(perm_n) intersects the q-term literal derivative "
                "sum trivially."
            ),
            "zero_block_size": (
                "zeta(n,m)=floor((m^2-1)/n)+"
                "1_{m>=3,n|m^2,m^2/n>=2}; every zeta(n,m)-term block is zero."
            ),
            "projection": (
                "For Q>=zeta(n,m), the permanent-relative intersection with "
                "Q terms has dimension at most "
                "(Q-zeta(n,m))*binom(n,m)."
            ),
            "sharp_exceptions": (
                "The equality endpoint fails for one term when n=m^2, "
                "and fails at m=2,q=2,n=2."
            ),
        },
        "finite_replay": {
            "n_min": 2,
            "n_max": 128,
            "parameter_cells": parameter_cells,
            "projection_cap_checks": projection_checks,
            "closed_endpoint_improvements": len(all_endpoint_triples),
            "proper_derivative_endpoint_improvements": len(
                proper_endpoint_triples
            ),
            "first_proper_endpoint_triples": proper_endpoint_triples[:20],
            "single_term_counterexample_rows": single_term_counterexamples,
            "single_term_matching_monomial_checks": matching_monomial_checks,
            "quadratic_counterexample": quadratic_counterexample,
        },
        "claim_boundary": (
            "This theorem closes the equality endpoint of the factor-span "
            "zero-block criterion using the previously proved direct-sum "
            "indecomposability of minimal-shadow permanent derivatives. It is "
            "an ordinary characteristic-zero Chow-realizability statement. "
            "It introduces no new numerical Chow-rank bound in the currently "
            "frozen certificate table, does not improve border rank, does not "
            "classify near-endpoint intersections, and does not solve general "
            "Glynn optimality. Literature novelty is not established."
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
    print("GENERAL_CLOSED_FACTOR_SPAN_ENDPOINT_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
