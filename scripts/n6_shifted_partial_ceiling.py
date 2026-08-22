#!/usr/bin/env python3
"""Exact ceiling for every shifted-partial flattening of ``perm_6``."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb
from pathlib import Path


N = 6
VARIABLES = N * N
TAIL_START_TOTAL_DEGREE = 53


def single_term_rank(output_degree: int, shift: int) -> int:
    """Maximum shifted-partial rank of one sextic Chow term."""

    if output_degree == 0:
        return comb(VARIABLES + shift - 1, shift)
    total_degree = output_degree + shift
    inactive = VARIABLES - N
    return sum(
        comb(N, support)
        * comb(total_degree + inactive - 1, support + inactive - 1)
        for support in range(
            output_degree,
            min(N, total_degree) + 1,
        )
    )


def permanent_dimension_upper(output_degree: int, shift: int) -> int:
    source = (
        comb(N, output_degree) ** 2
        * comb(VARIABLES + shift - 1, shift)
    )
    target = comb(
        VARIABLES + output_degree + shift - 1,
        output_degree + shift,
    )
    return min(source, target)


def finite_rows() -> list[dict[str, int]]:
    rows = []
    for output_degree in range(N + 1):
        for shift in range(TAIL_START_TOTAL_DEGREE - output_degree):
            term_rank = single_term_rank(output_degree, shift)
            upper = permanent_dimension_upper(output_degree, shift)
            rows.append(
                {
                    "output_degree": output_degree,
                    "shift": shift,
                    "total_degree": output_degree + shift,
                    "permanent_rank_upper": upper,
                    "single_term_rank": term_rank,
                }
            )
    return rows


def tail_ratio(total_degree: int) -> Fraction:
    """Target divided by the full-six-support contribution of one term."""

    return Fraction(
        comb(total_degree + VARIABLES - 1, VARIABLES - 1),
        comb(total_degree + VARIABLES - N - 1, VARIABLES - 1),
    )


def build_payload() -> dict[str, object]:
    rows = finite_rows()
    best = max(
        rows,
        key=lambda row: Fraction(
            row["permanent_rank_upper"],
            row["single_term_rank"],
        ),
    )
    best_ratio = Fraction(
        best["permanent_rank_upper"],
        best["single_term_rank"],
    )
    expected = Fraction(843_600, 35_009)
    if best_ratio != expected or (
        best["output_degree"],
        best["shift"],
    ) != (3, 3):
        raise AssertionError((best, best_ratio))

    tail_at_start = tail_ratio(TAIL_START_TOTAL_DEGREE)
    if tail_at_start >= best_ratio:
        raise AssertionError((tail_at_start, best_ratio))
    if not all(
        tail_ratio(total_degree + 1) < tail_ratio(total_degree)
        for total_degree in range(
            TAIL_START_TOTAL_DEGREE,
            TAIL_START_TOTAL_DEGREE + 100,
        )
    ):
        raise AssertionError("diagnostic tail monotonicity failed")

    return {
        "status": "N6_ALL_SHIFTED_PARTIAL_CEILING_REPLAYED",
        "finite_total_degree_range": [0, TAIL_START_TOTAL_DEGREE - 1],
        "finite_state_count": len(rows),
        "maximizing_state": best,
        "global_ratio_upper": [best_ratio.numerator, best_ratio.denominator],
        "tail_start_total_degree": TAIL_START_TOTAL_DEGREE,
        "tail_ratio_at_start": [
            tail_at_start.numerator,
            tail_at_start.denominator,
        ],
        "theorem": (
            "Every shifted-partial flattening of perm_6 has rank at most "
            "843600/35009 times the maximum rank of one Chow term."
        ),
        "integer_lower_bound_ceiling": 25,
        "claim_boundary": (
            "This family cannot certify Chow rank at least 26. This is a "
            "method ceiling and does not change 26 <= ChowRank(perm_6) <= 32."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    print("N6_ALL_SHIFTED_PARTIAL_CEILING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
