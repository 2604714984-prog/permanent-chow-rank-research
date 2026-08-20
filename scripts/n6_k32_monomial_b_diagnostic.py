"""Exact QQ diagnostic for the monomial (permutation) graph subfamily.

This is deliberately a finite certificate, not a classification of arbitrary
invertible graph operators.  It exhausts S_6 and records the b(T) values from
N6-129 after the exact A-space quotient fix.
"""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from pathlib import Path

import sympy as sp

try:
    from scripts.n6_k32_annihilator_reduction import reduction_dimensions
except ModuleNotFoundError:  # Direct script execution.
    from n6_k32_annihilator_reduction import reduction_dimensions


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_k32_monomial_b_diagnostic.json"


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    matrix = sp.zeros(6)
    for column, row in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def build_payload() -> dict[str, object]:
    histogram: dict[str, int] = {}
    high: list[dict[str, object]] = []
    mismatches: list[list[object]] = []
    for permutation in permutations(range(6)):
        matrix = permutation_matrix(permutation)
        cross, annihilator, b_dimension, c_dimension = reduction_dimensions(matrix)
        key = str(b_dimension)
        histogram[key] = histogram.get(key, 0) + 1
        if annihilator != b_dimension + c_dimension or cross != 18 - b_dimension - c_dimension:
            mismatches.append([list(permutation), cross, annihilator, b_dimension, c_dimension])
        if b_dimension >= 9:
            high.append(
                {
                    "permutation": list(permutation),
                    "cross_rank_over_QQ": cross,
                    "annihilator_dimension": annihilator,
                    "b_dimension": b_dimension,
                    "c_dimension": c_dimension,
                }
            )
    return {
        "certificate": "N6-130",
        "status": "FINITE_EXACT_MONOMIAL_B_DIAGNOSTIC",
        "field": "QQ",
        "candidate_count": 720,
        "threshold": "b(T) >= 9 is necessary for cross rank <= 6",
        "formula_checked": "cross rank = 18 - b(T) - c(T)",
        "histogram_by_b": dict(sorted(histogram.items(), key=lambda item: int(item[0]))),
        "high_threshold_count": len(high),
        "high_threshold_cases": high,
        "formula_mismatch_count": len(mismatches),
        "boundary": [
            "This exhausts permutation matrices only.",
            "It does not cover diagonal-scaled or arbitrary invertible graph operators.",
            "It does not prove the general 2+2 matching lemma or ChowRank(perm_6).",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError("frozen payload mismatch")
    print("certificate=N6-130")
    print("permutations=720")
    print("high_b_cases=" + str(len(payload["high_threshold_cases"])))
    print("status=PASS")


if __name__ == "__main__":
    main()
