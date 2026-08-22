#!/usr/bin/env python3
"""Exact arithmetic interfaces for the regular-sequence torsion cap."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def cap(r: int, q: int, d: int) -> int:
    require(r >= 1 and 0 <= q <= r and 0 <= d <= r, (r, q, d))
    e = r - d
    h = max(q - d, 0)
    return e * (q - h)


def payload() -> dict[str, object]:
    checks = 0
    for r in range(1, 51):
        for q in range(r + 1):
            for d in range(r + 1):
                checks += 1
                value = cap(r, q, d)
                require(value == (r - d) * min(q, d), (r, q, d))
                require(value <= d * (r - d), (r, q, d))
    return {
        "schema": "general_partial_quotient_regular_sequence_cap/v1",
        "field": "infinite_characteristic_zero",
        "hypothesis": "I_2 is a q-quadric regular sequence in r variables",
        "linear_section_height_floor": "max(q-d,0)",
        "corrected_torsion_cap": "(r-d)*min(q,d)",
        "independent_scale": "d*(r-d)",
        "integer_rows_checked": checks,
        "largest_r": 50,
        "sharpness": "independent square quadrics and coordinate quotient",
        "claim_boundary": {
            "arbitrary_chow_term_quadrics_regular": "OPEN",
            "new_chow_rank_bound": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    result = payload()
    if args.verify_json:
        require(json.loads(args.verify_json.read_text()) == result, "frozen mismatch")
    if args.json:
        args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("GENERAL_PARTIAL_QUOTIENT_REGULAR_SEQUENCE_CAP_PASS")


if __name__ == "__main__":
    main()
