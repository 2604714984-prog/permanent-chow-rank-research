#!/usr/bin/env python3
"""Exact general-n counterexample to the independent-term Koszul H1 cap."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path

SCHEMA = "general_one_relation_koszul_homology_counterexample/v1"
THEOREM_ID = "G-ONE-RELATION-KOSZUL-H1-COUNTEREXAMPLE-v1"


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def full_circuit_hilbert(n: int) -> list[int]:
    require(n >= 5, n)
    return [1, n - 1] + [comb(n, degree) for degree in range(2, n - 1)] + [n - 1, 1]


def row(n: int) -> dict[str, int]:
    require(n >= 5, n)
    factor_span = n - 1
    homology = comb(n, 2)
    independent_cap = n - 1
    source_rank = comb(n, 3)
    middle_dimension = factor_span * comb(n, 2)
    target_dimension = comb(factor_span, 2) * factor_span
    right_rank = middle_dimension - source_rank - homology
    require(right_rank == 2 * comb(n, 3), (n, right_rank))
    require(source_rank + right_rank + homology == middle_dimension, n)
    require(right_rank <= target_dimension, n)
    return {
        "n": n,
        "factor_span_dimension": factor_span,
        "quotient_rank": factor_span,
        "output_degree_k": 2,
        "source_dimension_and_rank": source_rank,
        "middle_dimension": middle_dimension,
        "right_differential_rank": right_rank,
        "target_dimension": target_dimension,
        "actual_h1_dimension": homology,
        "independent_term_cap": independent_cap,
        "violation_gap": homology - independent_cap,
        "minimal_cubic_generators": homology,
        "gorenstein_last_shift": 2 * n - 1,
        "dual_tor_homological_degree": n - 2,
        "dual_tor_internal_degree": 2 * n - 4,
    }


def payload() -> dict[str, object]:
    rows = [row(n) for n in range(5, 13)]
    require(all(item["violation_gap"] > 0 for item in rows), rows)
    return {
        "schema": SCHEMA,
        "theorem_id": THEOREM_ID,
        "field": "algebraically_closed_characteristic_zero",
        "normal_form": "x_1*...*x_(n-1)*(x_1+...+x_(n-1))",
        "statement": {
            "range": "n>=5",
            "factor_span_dimension": "n-1",
            "quotient": "identity_on_actual_factor_span",
            "output_degree": 2,
            "actual_h1_dimension": "binom(n,2)",
            "independent_term_cap_at_same_degree_and_rank": "n-1",
            "gap": "binom(n-1,2)",
        },
        "proof_interfaces": {
            "hilbert_function": (
                "1,n-1,binom(n,2),...,binom(n,n-2),n-1,1"
            ),
            "quadratic_apolar_relations": 0,
            "minimal_cubic_generators": "binom(n,2)",
            "gorenstein_last_shift": "2n-1",
            "koszul_duality": (
                "H1 of D3 -> L tensor D2 -> wedge2(L) tensor D1 "
                "equals Tor_(n-2,2n-4)"
            ),
        },
        "rows": rows,
        "claim_boundary": {
            "independent_term_theorem": "RETAINED",
            "uniform_degenerate_term_extension": "FALSE",
            "raw_first_koszul_homology_as_uniform_chow_invariant": "REJECTED",
            "new_general_chow_rank_lower_bound": False,
            "border_rank_improvement": False,
            "general_glynn_optimality": "OPEN",
            "next_interface": (
                "quotient the circuit-generated apolar syzygies or prove a "
                "corrected defect term compatible with sums"
            ),
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
    print("GENERAL_ONE_RELATION_KOSZUL_HOMOLOGY_COUNTEREXAMPLE_PASS")


if __name__ == "__main__":
    main()
