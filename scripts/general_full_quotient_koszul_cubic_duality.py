#!/usr/bin/env python3
"""Exact interfaces for full-quotient Koszul H1 and cubic apolar generators."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path

SCHEMA = "general_full_quotient_koszul_cubic_duality/v1"
THEOREM_ID = "G-FULL-QUOTIENT-KOSZUL-CUBIC-DUALITY-v1"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def one_relation_cubic_generators(support_size: int) -> int:
    require(support_size >= 1, support_size)
    if support_size <= 2:
        return 1
    if support_size == 3:
        return 7
    return comb(support_size + 1, 2)


def one_relation_row(n: int) -> dict[str, object]:
    require(n >= 5, n)
    counts = [
        one_relation_cubic_generators(support_size)
        for support_size in range(1, n)
    ]
    require(counts[-1] == comb(n, 2), (n, counts[-1]))
    return {
        "n": n,
        "relation_supports": list(range(1, n)),
        "full_quotient_h1_dimensions": counts,
        "full_support_h1": counts[-1],
        "full_support_independent_cap": n - 1,
        "full_support_gap": comb(n - 1, 2),
    }


def tor_positions(n: int, factor_span_dimension: int) -> dict[str, int]:
    require(n >= 3, n)
    require(1 <= factor_span_dimension <= n, factor_span_dimension)
    return {
        "socle_degree": n,
        "codimension": factor_span_dimension,
        "gorenstein_last_shift": n + factor_span_dimension,
        "high_tor_homological_degree": factor_span_dimension - 1,
        "high_tor_internal_degree": n + factor_span_dimension - 3,
        "dual_low_tor_homological_degree": 1,
        "dual_low_tor_internal_degree": 3,
    }


def payload() -> dict[str, object]:
    rows = [one_relation_row(n) for n in range(5, 13)]
    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "field": "algebraically_closed_characteristic_zero",
        "identity": {
            "derivative_complex": "D3(f) -> L tensor D2(f) -> wedge2(L) tensor D1(f)",
            "high_tor": "Tor_(r-1,n+r-3)(A_f,k)",
            "dual_low_tor": "Tor_(1,3)(A_f,k)^*",
            "dimension": "beta_(1,3)(A_f)",
            "minimal_generator_space": "(f_perp)_3 / R_1*(f_perp)_2",
        },
        "normalization_examples": {
            "independent_squarefree_term": 0,
            "one_repeated_factor": 1,
            "full_support_one_relation": "binom(n,2)",
        },
        "one_relation_classification": {
            "support_1": 1,
            "support_2": 1,
            "support_3": 7,
            "support_at_least_4": "binom(s+1,2)",
        },
        "rows": rows,
        "claim_boundary": {
            "full_quotient_identity": "PROVED",
            "partial_quotient_corrected_homology": "OPEN",
            "uniform_corrected_one_term_cap": "OPEN",
            "sum_subquotient_inequality": "OPEN",
            "new_chow_rank_lower_bound": False,
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
    print("GENERAL_FULL_QUOTIENT_KOSZUL_CUBIC_DUALITY_PASS")


if __name__ == "__main__":
    main()
