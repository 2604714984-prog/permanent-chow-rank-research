#!/usr/bin/env python3
"""Arithmetic replay for the conditional ordinary perm_6 rank-32 candidate.

This checks only the finite rows and the final cancellation.  The candidate
argument and its unresolved boundary are recorded in
docs/n6_exact_ordinary_chow_rank_32_candidate.md.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_JSON = HERE.parent / "data" / "n6_exact_ordinary_chow_rank_32_candidate.json"


def dominates_half_defect(row: tuple[Fraction, ...]) -> bool:
    return all(value >= Fraction(10 * d, 3) for d, value in enumerate(row))


def build_payload() -> dict[str, object]:
    low_span_rows = {
        "ell_1": (Fraction(19, 2), Fraction(21, 2)),
        "ell_2": (Fraction(8), Fraction(9), Fraction(11)),
        "ell_3": (Fraction(5), Fraction(15, 2), Fraction(9), Fraction(12)),
        "ell_4": (Fraction(0), Fraction(9, 2), Fraction(8), Fraction(10), Fraction(14)),
    }
    full_span_row = tuple(map(Fraction, (0, 7, 10, 10, 15, 17, 20)))
    five_span_rows = {
        "s_5": tuple(map(Fraction, (0, 7, 10, 10, 15, 17))),
        "s_4": tuple(map(Fraction, (0, 8, 12, 13, 16, 19))),
        "s_3": tuple(map(Fraction, (1, 8, 11, 11, 16, 18))),
        "s_1_2": tuple(map(Fraction, (3, 9, 9, 10, 16, 17))),
    }
    rows = {**low_span_rows, "ell_6": full_span_row, **five_span_rows}
    checks = {name: dominates_half_defect(row) for name, row in rows.items()}
    if not all(checks.values()):
        raise AssertionError(checks)

    # EX3 <= EX2 is 120 - Delta/2 <= 10N - 200 - Delta/2.
    # The individual-rank defect cancels identically.
    minimum_n = 32
    n31_gap = 120 - (10 * 31 - 200)
    n32_gap = 120 - (10 * 32 - 200)
    assert n31_gap == 10
    assert n32_gap == 0

    def encode(row: tuple[Fraction, ...]) -> list[str]:
        return [str(value) for value in row]

    return {
        "status": "CONDITIONAL_CANDIDATE_ARITHMETIC_REPLAY",
        "scope": "ordinary Chow rank over characteristic zero; not border rank",
        "claim_boundary": (
            "The replay checks the displayed rational rows and final "
            "cancellation only. It does not prove the geometric reductions "
            "or independently derive the local quotient-symbol ranks."
        ),
        "half_defect_coefficient": "1/2",
        "factor_increment_slope": "10/3",
        "factor_span_total": 36,
        "lower_symbol_constant": 120,
        "upper_symbol_formula": "10*N - 200 - Delta/2",
        "lower_symbol_formula": "120 - Delta/2",
        "minimum_n": minimum_n,
        "n31_gap": n31_gap,
        "n32_gap": n32_gap,
        "half_defect_rows": {name: encode(row) for name, row in rows.items()},
        "all_half_defect_rows_pass": all(checks.values()),
        "conclusion": (
            "If the half-defect quotient-symbol proposition holds, then "
            "ChowRank(perm_6) = 32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS: conditional rank-32 arithmetic payload matches")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
