#!/usr/bin/env python3
"""Exact arithmetic for the even-order middle-symbol capacity ceiling."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

THEOREM_ID = "G-EVEN-MIDDLE-SYMBOL-CAPACITY-CEILING-v1"
SCHEMA = "general_even_middle_symbol_capacity_ceiling/v1"
DEFAULT_MAX_N = 64
SELECTED_N = (4, 6, 8, 10, 12, 16, 32, 64)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def central_binomial(n: int) -> int:
    require(n >= 0 and n % 2 == 0, n)
    return comb(n, n // 2)


def route_ceiling(n: int) -> int:
    """Maximum integer lower bound available to the named route class."""
    return central_binomial(n) + 2 * n


def glynn_target(n: int) -> int:
    require(n >= 1, n)
    return 1 << (n - 1)


def missing_rank_units(n: int) -> int:
    return max(0, glynn_target(n) - route_ceiling(n))


def missing_global_symbol_charge(n: int) -> int:
    """Additional h-charge required in the normalization of the theorem."""
    c = central_binomial(n)
    gap = missing_rank_units(n)
    require((c * gap) % 2 == 0, (n, c, gap))
    return c * gap // 2


def row(n: int) -> dict[str, Any]:
    c = central_binomial(n)
    ceiling = route_ceiling(n)
    target = glynn_target(n)
    return {
        "n": n,
        "middle_degree": n // 2,
        "one_term_middle_rank_cap": c,
        "constant_slope_cap_numerator": c,
        "constant_slope_cap_denominator": n,
        "route_ceiling": ceiling,
        "glynn_target": target,
        "missing_rank_units": max(0, target - ceiling),
        "missing_global_symbol_charge": missing_global_symbol_charge(n),
        "route_reaches_glynn_capacity": ceiling >= target,
    }


def theorem_core(rows: list[dict[str, Any]]) -> str:
    core = {
        "theorem_id": THEOREM_ID,
        "route_class": "constant_slope_single_middle_layer_half_defect_filtration",
        "slope_ceiling": "binom(n,n/2)/n",
        "rank_ceiling": "binom(n,n/2)+2n",
        "n6_equality": True,
        "strict_failure_from_n8": True,
        "rows": rows,
    }
    encoded = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def payload(max_n: int = DEFAULT_MAX_N) -> dict[str, Any]:
    require(max_n >= 8 and max_n % 2 == 0, max_n)
    rows = [row(n) for n in SELECTED_N if n <= max_n]

    require(row(6)["route_ceiling"] == 32, row(6))
    require(row(6)["glynn_target"] == 32, row(6))
    require(
        all(route_ceiling(n) < glynn_target(n) for n in range(8, max_n + 1, 2)),
        max_n,
    )

    previous_num = previous_den = None
    for n in range(4, max_n + 1, 2):
        num = route_ceiling(n)
        den = glynn_target(n)
        if previous_num is not None:
            require(num * previous_den <= previous_num * den, (n, num, den))
        previous_num, previous_den = num, den

    core = theorem_core(rows)
    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "field": "characteristic_zero",
        "scope": "ordinary_chow_rank_route_barrier",
        "route_class": {
            "middle_order": "n=2m",
            "global_upper": "h <= (c*N-c^2-Delta)/2",
            "local_form": "rank(beta_(T,P)) + delta(T)/2 >= s*rank(P)",
            "factor_filtration": "sum rank(P_i)=n^2",
            "full_rank_test_term": "T=z_1*...*z_n, P=id",
        },
        "theorem": {
            "slope_ceiling": "s <= c/n, c=binom(n,n/2)",
            "certifiable_rank_ceiling": "N <= c+2n as a route-capacity ceiling",
            "n6": "c+2n=32=2^(n-1)",
            "even_n_ge_8": "c+2n<2^(n-1)",
            "asymptotic_ratio": "sqrt(8/(pi*n))*(1+o(1))",
        },
        "selected_rows": rows,
        "monotone_ratio_verified_through": max_n,
        "theorem_core_sha256": core,
        "claim_boundary": {
            "new_chow_rank_lower_bound": False,
            "general_glynn_optimality": "OPEN",
            "multi_degree_coupled_symbols": "NOT_COVERED",
            "nonlinear_relation_modules": "NOT_COVERED",
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    parser.add_argument("--max-n", type=int, default=DEFAULT_MAX_N)
    args = parser.parse_args()

    result = payload(args.max_n)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(result == expected, "frozen payload mismatch")

    print("GENERAL_EVEN_MIDDLE_SYMBOL_CAPACITY_CEILING_PASS")


if __name__ == "__main__":
    main()
