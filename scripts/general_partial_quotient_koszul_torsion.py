#!/usr/bin/env python3
"""Exact finite interfaces for cubic-corrected partial quotient Koszul homology."""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

SCHEMA = "general_partial_quotient_koszul_torsion/v1"
THEOREM_ID = "G-PARTIAL-QUOTIENT-KOSZUL-TORSION-v1"
THEOREM_CORE = "f8c9b5ff8a9f09c9dd31dd9c4d123ce68aa6a0ea49e593ecc97da548dbd82bd2"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def corrected_torsion_cap(r: int, q: int, d: int) -> int:
    require(r >= 1 and 0 <= q <= r and 0 <= d <= r, (r, q, d))
    return (r - d) * min(q, d)


def fixed_point_torsion(
    r: int,
    quadratic_axes: tuple[int, ...],
    quotient_axes: tuple[int, ...],
) -> int:
    a = frozenset(quadratic_axes)
    b = frozenset(quotient_axes)
    require(len(a) == len(quadratic_axes), quadratic_axes)
    require(len(b) == len(quotient_axes), quotient_axes)
    require(all(0 <= value < r for value in a | b), (r, a, b))
    return (r - len(b)) * len(a & b)


def exhaustive_fixed_point_maximum(r: int, q: int, d: int) -> int:
    maximum = -1
    for a in combinations(range(r), q):
        for b in combinations(range(r), d):
            maximum = max(maximum, fixed_point_torsion(r, a, b))
    expected = corrected_torsion_cap(r, q, d)
    require(maximum == expected, (r, q, d, maximum, expected))
    return maximum


def replay_all_fixed_points(max_r: int = 8) -> None:
    for r in range(1, max_r + 1):
        for q in range(r + 1):
            for d in range(r + 1):
                exhaustive_fixed_point_maximum(r, q, d)


def one_relation_quadratic_count(r: int, support_size: int) -> int:
    require(r >= 1 and 1 <= support_size <= r, (r, support_size))
    return r - support_size + (1 if support_size == 2 else 0)


def one_relation_caps(r: int, support_size: int) -> list[int]:
    q = one_relation_quadratic_count(r, support_size)
    caps = [corrected_torsion_cap(r, q, d) for d in range(r + 1)]
    require(all(value <= d * (r - d) for d, value in enumerate(caps)), (r, support_size, caps))
    return caps


def payload() -> dict[str, object]:
    replay_all_fixed_points()
    for r in range(2, 13):
        for support_size in range(1, r + 1):
            one_relation_caps(r, support_size)

    selected_fixed = [
        {"r": r, "q": q, "d": d, "maximum": corrected_torsion_cap(r, q, d)}
        for r, q, d in ((3, 3, 1), (4, 2, 2), (5, 4, 3), (6, 6, 3), (8, 5, 4))
    ]
    selected_one_relation = [
        {
            "r": r,
            "support_size": support_size,
            "quadratic_dimension": one_relation_quadratic_count(r, support_size),
            "caps": one_relation_caps(r, support_size),
        }
        for r, support_size in ((4, 2), (4, 4), (6, 3), (8, 8), (12, 2))
    ]

    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "theorem_core": THEOREM_CORE,
        "field": "algebraically_closed_characteristic_zero",
        "exact_sequence": {
            "partial_low_h1": "(I_3 intersect W*S_2)/(W*I_2)",
            "full_cubic_generators": "I_3/(V*I_2)",
            "corrected_kernel": "(V*I_2 intersect W*S_2)/(W*I_2)",
            "base_change_tor": "Tor_1^S(S/(I_2),S/(W))_3",
        },
        "simultaneously_diagonalizable_cap": {
            "formula": "(r-d)*min(q,d)",
            "independent_scale": "d*(r-d)",
            "fixed_point_replay_through_r": 8,
            "selected_rows": selected_fixed,
        },
        "one_relation_family": {
            "normal_form": "x_1*...*x_r*(x_1+...+x_s)",
            "quadratic_dimension": "r-s+1_(s=2)",
            "all_supports_and_quotients_checked_through_r": 12,
            "selected_rows": selected_one_relation,
            "passes_independent_scale": True,
        },
        "claim_boundary": {
            "exact_sequence": "PROVED",
            "simultaneously_diagonalizable_cap": "PROVED",
            "complete_one_relation_family": "PASS",
            "arbitrary_multi_relation_chow_term": "OPEN",
            "sum_subquotient_inequality": "OPEN",
            "new_general_chow_rank_lower_bound": False,
            "border_rank_improvement": False,
            "literature_novelty": "NOT_ESTABLISHED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    result = payload()
    if arguments.verify_json is not None:
        frozen = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        require(frozen == result, "frozen payload mismatch")
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_PARTIAL_QUOTIENT_KOSZUL_TORSION_PASS")


if __name__ == "__main__":
    main()
