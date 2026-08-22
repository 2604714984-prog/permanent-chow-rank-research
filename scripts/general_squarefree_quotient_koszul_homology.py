#!/usr/bin/env python3
"""Exact maximal first Koszul homology for squarefree quotient symbols."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

THEOREM_ID = "G-SQUAREFREE-QUOTIENT-KOSZUL-HOMOLOGY-v1"
SCHEMA = "general_squarefree_quotient_koszul_homology/v1"
SELECTED_N = (4, 6, 8, 10)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def c(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def maximum_h1(n: int, k: int, d: int) -> int:
    require(n >= 1, n)
    require(1 <= k <= n, (n, k))
    require(0 <= d <= n, (n, d))
    return d * c(n - d, k - 1)


def adjacent_maximum_h1(n: int, k: int, d: int) -> int:
    require(1 <= k < n, (n, k))
    return maximum_h1(n, k, d) + maximum_h1(n, k + 1, d)


def all_degree_maximum_h1(n: int, d: int) -> int:
    require(0 <= d <= n, (n, d))
    return d * (1 << (n - d))


def profile(n: int) -> dict[str, Any]:
    middle = n // 2
    return {
        "n": n,
        "middle_degree": middle,
        "middle_h1_cap": [
            {"d": d, "dimension": maximum_h1(n, middle, d)}
            for d in range(n + 1)
        ],
        "adjacent_middle_h1_cap": [
            {"d": d, "dimension": adjacent_maximum_h1(n, middle, d)}
            for d in range(n + 1)
        ],
        "all_degree_h1_cap": [
            {"d": d, "dimension": all_degree_maximum_h1(n, d)}
            for d in range(n + 1)
        ],
    }


def theorem_core(profiles: list[dict[str, Any]]) -> str:
    core = {
        "theorem_id": THEOREM_ID,
        "h1_maximum": "d*C(n-d,k-1)",
        "adjacent_maximum": "d*C(n-d+1,k)",
        "all_degree_maximum": "d*2^(n-d)",
        "profiles": profiles,
    }
    return hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload() -> dict[str, Any]:
    profiles = [profile(n) for n in SELECTED_N]
    for n in range(2, 65):
        for d in range(n + 1):
            require(
                sum(maximum_h1(n, k, d) for k in range(1, n + 1))
                == all_degree_maximum_h1(n, d),
                (n, d),
            )
            for k in range(1, n):
                require(
                    adjacent_maximum_h1(n, k, d)
                    == d * c(n - d + 1, k),
                    (n, k, d),
                )
    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "field": "algebraically_closed_characteristic_zero",
        "complex": (
            "Sq^(k+1)(F) -> D tensor Sq^k(F) -> "
            "wedge^2(D) tensor Sq^(k-1)(F)"
        ),
        "theorem": {
            "maximum_h1_dimension": "d*C(n-d,k-1)",
            "coordinate_quotient_attains_maximum": True,
            "adjacent_maximum": "d*C(n-d+1,k)",
            "all_positive_degrees_maximum": "d*2^(n-d)",
            "rank_one_all_degree_cap": "2^(n-1)",
        },
        "selected_profiles": profiles,
        "theorem_core_sha256": theorem_core(profiles),
        "claim_boundary": {
            "independent_full_factor_term": "EXACT",
            "arbitrary_dependent_or_repeated_term": "OPEN",
            "permanent_side_homology": "NOT_COMPUTED",
            "sum_or_subquotient_inequality": "NOT_PROVED",
            "new_chow_rank_lower_bound": False,
            "border_rank_improvement": False,
            "general_glynn_optimality": "OPEN",
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    result = payload()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    if args.verify_json is not None:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        require(result == expected, "frozen payload mismatch")
    print("GENERAL_SQUAREFREE_QUOTIENT_KOSZUL_HOMOLOGY_PASS")


if __name__ == "__main__":
    main()
