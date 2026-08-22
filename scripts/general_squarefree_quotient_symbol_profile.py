#!/usr/bin/env python3
"""Exact squarefree quotient-symbol profiles and additivity barriers."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

THEOREM_ID = "G-SQUAREFREE-QUOTIENT-SYMBOL-PROFILE-v1"
SCHEMA = "general_squarefree_quotient_symbol_profile/v1"
SELECTED_N = (4, 6, 8)


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def c(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def minimum_symbol_rank(n: int, k: int, d: int) -> int:
    require(n >= 1, n)
    require(1 <= k <= n, (n, k))
    require(0 <= d <= n, (n, d))
    return c(n, k) - c(n - d, k)


def adjacent_minimum_rank(n: int, k: int, d: int) -> int:
    require(1 <= k < n, (n, k))
    return minimum_symbol_rank(n, k, d) + minimum_symbol_rank(n, k + 1, d)


def all_positive_degrees_minimum_rank(n: int, d: int) -> int:
    require(0 <= d <= n, (n, d))
    return (1 << n) - (1 << (n - d))


def profile(n: int) -> dict[str, Any]:
    middle = n // 2
    return {
        "n": n,
        "middle_degree": middle,
        "single_degree": [
            {"d": d, "rank": minimum_symbol_rank(n, middle, d)}
            for d in range(n + 1)
        ],
        "adjacent_middle": [
            {
                "d": d,
                "rank": adjacent_minimum_rank(n, middle, d)
                if middle < n
                else minimum_symbol_rank(n, middle, d),
            }
            for d in range(n + 1)
        ],
        "all_positive_degrees": [
            {"d": d, "rank": all_positive_degrees_minimum_rank(n, d)}
            for d in range(n + 1)
        ],
    }


def theorem_core(profiles: list[dict[str, Any]]) -> str:
    core = {
        "theorem_id": THEOREM_ID,
        "single_degree_minimum": "C(n,k)-C(n-d,k)",
        "adjacent_minimum": (
            "C(n,k)+C(n,k+1)-C(n-d,k)-C(n-d,k+1)"
        ),
        "all_degree_minimum": "2^n-2^(n-d)",
        "profiles": profiles,
    }
    return hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def payload() -> dict[str, Any]:
    profiles = [profile(n) for n in SELECTED_N]

    for n in range(2, 25):
        for d in range(n + 1):
            require(
                sum(minimum_symbol_rank(n, k, d) for k in range(1, n + 1))
                == all_positive_degrees_minimum_rank(n, d),
                (n, d),
            )
            for k in range(1, n):
                require(
                    adjacent_minimum_rank(n, k, d)
                    == minimum_symbol_rank(n, k, d)
                    + minimum_symbol_rank(n, k + 1, d),
                    (n, k, d),
                )

    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "field": "characteristic_zero",
        "object": (
            "squarefree derivative module of an independent n-factor Chow term"
        ),
        "theorem": {
            "single_degree_minimum": "C(n,k)-C(n-d,k)",
            "kernel_maximum": "C(n-d,k)",
            "adjacent_shared_quotient_minimum": (
                "C(n,k)+C(n,k+1)-C(n-d,k)-C(n-d,k+1)"
            ),
            "all_positive_degrees_shared_quotient_minimum": "2^n-2^(n-d)",
            "conclusion": (
                "sharing the factor quotient without a cross-degree relation "
                "quotient gives exact additivity"
            ),
        },
        "selected_profiles": profiles,
        "theorem_core_sha256": theorem_core(profiles),
        "claim_boundary": {
            "arbitrary_degenerate_term_profile": "NOT_CLASSIFIED",
            "cross_degree_homology_quotient": "NOT_COVERED",
            "new_chow_rank_lower_bound": False,
            "general_glynn_optimality": "OPEN",
            "border_rank_improvement": False,
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

    print("GENERAL_SQUAREFREE_QUOTIENT_SYMBOL_PROFILE_PASS")


if __name__ == "__main__":
    main()
