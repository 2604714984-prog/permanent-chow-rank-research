#!/usr/bin/env python3
"""Exact catalectic profiles of all rank-six seven-factor normal forms.

After choosing six independent factors as coordinates, every seventh factor
is equivalent to x1+...+xs for a unique support size 1 <= s <= 6.  This
script regenerates every catalectic matrix over the integers and computes its
rank over Q.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


VARIABLES = 6
DEGREE = 7
EXPECTED = {
    1: [1, 6, 16, 25, 25, 16, 6, 1],
    2: [1, 6, 16, 25, 25, 16, 6, 1],
    3: [1, 6, 18, 31, 31, 18, 6, 1],
    4: [1, 6, 19, 34, 34, 19, 6, 1],
    5: [1, 6, 20, 35, 35, 20, 6, 1],
    6: [1, 6, 21, 35, 35, 21, 6, 1],
}


def compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    if parts == 1:
        return ((total,),)
    rows = []
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            rows.append((first, *tail))
    return tuple(rows)


def coefficients(support_size: int) -> dict[tuple[int, ...], int]:
    answer = {}
    for doubled in range(support_size):
        exponent = [1] * VARIABLES
        exponent[doubled] = 2
        answer[tuple(exponent)] = 1
    return answer


def rational_rank(integer_rows: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in integer_rows]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (r for r in range(pivot_row, row_count) if rows[r][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or not rows[r][column]:
                continue
            scale = rows[r][column]
            rows[r] = [
                left - scale * right
                for left, right in zip(rows[r], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def catalectic_rows(
    support_size: int, output_degree: int
) -> tuple[list[list[int]], int, int]:
    outputs = compositions(output_degree, VARIABLES)
    operators = compositions(DEGREE - output_degree, VARIABLES)
    coeff = coefficients(support_size)
    matrix = []
    for operator in operators:
        row = []
        for output in outputs:
            source = tuple(a + b for a, b in zip(operator, output))
            value = coeff.get(source, 0)
            multiplier = 1
            for source_power, output_power in zip(source, output):
                multiplier *= (
                    math.factorial(source_power)
                    // math.factorial(output_power)
                )
            row.append(value * multiplier)
        matrix.append(row)
    return matrix, len(operators), len(outputs)


def profile_row(support_size: int) -> dict[str, object]:
    degree_rows = []
    for output_degree in range(DEGREE + 1):
        matrix, sources, targets = catalectic_rows(
            support_size, output_degree
        )
        degree_rows.append(
            {
                "degree": output_degree,
                "source_monomials": sources,
                "target_monomials": targets,
                "rank_Q": rational_rank(matrix),
            }
        )
    profile = [row["rank_Q"] for row in degree_rows]
    assert profile == EXPECTED[support_size]
    return {
        "support_size": support_size,
        "normal_form": (
            "x1*x2*x3*x4*x5*x6*("
            + "+".join(f"x{index}" for index in range(1, support_size + 1))
            + ")"
        ),
        "hilbert_profile": profile,
    }


def build_certificate() -> dict[str, object]:
    return {
        "schema_version": 1,
        "field": "Q",
        "classification": (
            "Every nonzero product of seven linear forms with essential "
            "factor-span dimension six is GL-equivalent, after individual "
            "factor rescaling, to exactly one listed support normal form."
        ),
        "normal_forms": [profile_row(s) for s in range(1, VARIABLES + 1)],
        "case_B_direct_basis_middle_sum": 7 * 25 + 35,
        "case_B_capacity_threshold": 245,
        "conclusion": (
            "The direct-factor-basis capacity lemma does not exclude seven "
            "mutually direct support-one/two rank-six terms plus one "
            "rank-seven complement: their local middle sum is 210."
        ),
        "claim_boundary": (
            "This classifies one-term catalectic profiles. It neither proves "
            "the external slope-ten endpoint classification nor constructs "
            "a permanent decomposition."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    result = build_certificate()
    if args.verify_json is None:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
    if result != frozen:
        raise SystemExit("rank-six normal-form profile JSON mismatch")
    print("PASS rank-six normal-form profiles")


if __name__ == "__main__":
    main()
