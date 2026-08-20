#!/usr/bin/env python3
"""Arithmetic replay for the exact ordinary Chow-rank theorem for perm_6.

The script checks the finite half-defect rows and the final cancellation.
The characteristic-zero geometry and linear algebra are written in the
adjacent theorem document; this replay is not a substitute for that proof.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_exact_ordinary_chow_rank_32.json"


def dominates_half_defect(row: tuple[Fraction, ...]) -> bool:
    return all(value >= Fraction(10 * d, 3) for d, value in enumerate(row))


def build_payload() -> dict[str, object]:
    rows = {
        "ell_1": (Fraction(19, 2), Fraction(21, 2)),
        "ell_2": (Fraction(8), Fraction(9), Fraction(11)),
        "ell_3": (Fraction(5), Fraction(15, 2), Fraction(9), Fraction(12)),
        "ell_4": (Fraction(0), Fraction(9, 2), Fraction(8), Fraction(10), Fraction(14)),
        "ell_6": tuple(map(Fraction, (0, 7, 10, 10, 15, 17, 20))),
        "ell_5_s5": tuple(map(Fraction, (0, 7, 10, 10, 15, 17))),
        "ell_5_s4": tuple(map(Fraction, (0, 8, 12, 13, 16, 19))),
        "ell_5_s3": tuple(map(Fraction, (1, 8, 11, 11, 16, 18))),
        "ell_5_s1_s2": tuple(map(Fraction, (3, 9, 9, 10, 16, 17))),
    }
    checks = {name: dominates_half_defect(row) for name, row in rows.items()}
    if not all(checks.values()):
        raise AssertionError(checks)

    # 120 - Delta/2 <= 10*N - 200 - Delta/2.
    n31_gap = 120 - (10 * 31 - 200)
    n32_gap = 120 - (10 * 32 - 200)
    assert n31_gap == 10
    assert n32_gap == 0

    return {
        "status": "PURE_THEOREM_ARITHMETIC_REPLAY",
        "scope": "ordinary Chow rank over characteristic zero; not border rank",
        "half_defect_coefficient": "1/2",
        "factor_increment_slope": "10/3",
        "factor_span_total": 36,
        "lower_symbol_constant": 120,
        "upper_symbol_formula": "10*N - 200 - Delta/2",
        "lower_symbol_formula": "120 - Delta/2",
        "minimum_n": 32,
        "n31_gap": n31_gap,
        "n32_gap": n32_gap,
        "half_defect_rows": {
            name: [str(value) for value in row] for name, row in rows.items()
        },
        "all_half_defect_rows_pass": all(checks.values()),
        "conclusion": "ChowRank(perm_6) = 32",
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
        print("PASS: exact ordinary rank-32 arithmetic payload matches")
    if not args.json and not args.verify_json:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
