#!/usr/bin/env python3
"""Exact replay for the N6-065 single-grade common-row-slice exclusion."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_common_rowslice_collision_exclusion.json"
N = 6
VARIABLES = [
    (normal_row, output_column, input_column)
    for normal_row in range(1, N)
    for output_column in range(N)
    for input_column in range(N)
]
VARIABLE_INDEX = {variable: index for index, variable in enumerate(VARIABLES)}


def rank_q(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, Fraction]] = {}
    for integer_row in rows:
        row = {
            column: Fraction(value)
            for column, value in integer_row.items()
            if value
        }
        while row:
            column = min(row)
            if column not in pivots:
                value = row[column]
                pivots[column] = {
                    index: entry / value for index, entry in row.items()
                }
                break
            value = row[column]
            for index, entry in pivots[column].items():
                row[index] = row.get(index, Fraction(0)) - value * entry
                if not row[index]:
                    row.pop(index, None)
    return len(pivots)


def permanent_containment_equations() -> list[dict[int, int]]:
    equations: list[dict[int, int]] = []
    for left_column, right_column in combinations(range(N), 2):
        for normal_row in range(1, N):
            # In x_(0,left) phi(e_right), only output column right can
            # participate in a row-column rectangle.  The other half is
            # analogous.
            for output_column in range(N):
                if output_column != right_column:
                    equations.append(
                        {
                            VARIABLE_INDEX[
                                (normal_row, output_column, right_column)
                            ]: 1
                        }
                    )
                if output_column != left_column:
                    equations.append(
                        {
                            VARIABLE_INDEX[
                                (normal_row, output_column, left_column)
                            ]: 1
                        }
                    )
            # The two cross corners of the permanent rectangle have the
            # same coefficient.
            equations.append(
                {
                    VARIABLE_INDEX[
                        (normal_row, right_column, right_column)
                    ]: 1,
                    VARIABLE_INDEX[
                        (normal_row, left_column, left_column)
                    ]: -1,
                }
            )
    return equations


def support_counts() -> dict[str, int]:
    column_pairs = list(combinations(range(N), 2))
    five_leading_spaces = {
        ((0, normal_row), column_pair)
        for normal_row in range(1, N)
        for column_pair in column_pairs
    }
    derivative_shadow = {
        (row, column)
        for (row_pair, column_pair) in five_leading_spaces
        for row in row_pair
        for column in column_pair
    }
    return {
        "one_leading_D_dimension": len(column_pairs),
        "five_space_direct_sum_dimension": len(five_leading_spaces),
        "joint_derivative_shadow_dimension": len(derivative_shadow),
        "b50_equality_shadow_dimension": 23,
    }


def build_payload() -> dict[str, object]:
    equations = permanent_containment_equations()
    rank = rank_q(equations)
    nullity = len(VARIABLES) - rank
    counts = support_counts()
    assert len(VARIABLES) == 180
    assert len(equations) == 825
    assert rank == 175
    assert nullity == 5
    assert counts == {
        "one_leading_D_dimension": 15,
        "five_space_direct_sum_dimension": 75,
        "joint_derivative_shadow_dimension": 36,
        "b50_equality_shadow_dimension": 23,
    }
    return {
        "status": [
            "PURE_SINGLE_GRADE_COMMON_ROWSLICE_EXCLUSION",
            "EXACT_QQ_LINEAR_REPLAY",
            "N6-065",
        ],
        "single_grade_scope": {
            "quotient_gauge_is_eliminated": (
                "An arbitrary first-order GL15 quotient identification adds "
                "F0*A. The same-row weight of F0*A is disjoint from both the "
                "normal row-pair weight of Q_phi and the permanent rectangle "
                "space E2, so containment in E2 forces A=0."
            ),
            "flat_limit_hypothesis": (
                "The five first nonzero D_i occur in one shared grade and "
                "their leading fifteen-planes are direct. Hence their sum is "
                "the Grassmann flat limit K0 of the seventy-five-plane K(t)."
            ),
            "shadow_twenty_three_is_derived": (
                "Derivative rank is at most twenty-three under specialization "
                "from K(t), and the universal product-shadow lower bound for "
                "a seventy-five-plane is twenty-three, so partial(K0) has "
                "dimension exactly twenty-three."
            ),
        },
        "normal_graph_system": {
            "unknown_count": len(VARIABLES),
            "equation_count": len(equations),
            "exact_QQ_rank": rank,
            "exact_QQ_nullity": nullity,
            "mathematical_kernel": "phi(e_c)=w tensor e_c, w in A/<p>",
        },
        "five_color_support_audit": counts,
        "strict_conclusion": (
            "A collision of all six factor planes to one common complete row "
            "slice cannot have all five first nonzero relative section-"
            "difference fifteen-planes in one shared grade and direct. The "
            "transpose statement holds for a common complete column slice."
        ),
        "claim_boundary": (
            "This excludes only the shared-grade layer in which the five "
            "first nonzero relative D_i are direct and therefore give the flat "
            "Grassmann limit of K. If their leading spaces are dependent, "
            "higher orders can enter that flat limit. The result does not "
            "classify collision trees, unequal valuations, successive clusters "
            "with new base slices, or every complete-collineation boundary. It "
            "does not exclude every common-row-slice collision, the full b=50 "
            "endpoint, or prove ChowRank(perm_6)>=28."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    system = payload["normal_graph_system"]
    print(
        "normal_graph",
        system["unknown_count"],
        system["equation_count"],
        system["exact_QQ_rank"],
        system["exact_QQ_nullity"],
    )
    print("five_color", payload["five_color_support_audit"])


if __name__ == "__main__":
    main()
