#!/usr/bin/env python3
"""Exact G-045 barrier to reversing the relation shadow.

Two squarefree sextic Chow terms have no literal relations in degrees three
and four, but they do have a quadratic relation.  Their coupled derivative
ranks in output degrees two, three, and four are 29, 40, and 29.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


SUPPORT_A = frozenset(range(6))
SUPPORT_B = frozenset((0, 1, 6, 7, 8, 9))
VARIABLE_COUNT = 10


def derivative_column(
    operator: frozenset[int], output_degree: int
) -> dict[frozenset[int], int]:
    """Column of C_(6-m,m)(T_A+T_B), in squarefree bases."""

    answer: dict[frozenset[int], int] = {}
    for support in (SUPPORT_A, SUPPORT_B):
        if operator <= support:
            output = support - operator
            if len(output) != output_degree:
                raise AssertionError((operator, output_degree, output))
            answer[output] = answer.get(output, 0) + 1
    return answer


def sparse_exact_rank(columns: list[dict[frozenset[int], int]]) -> int:
    """Exact rational column rank of a sparse integer matrix."""

    pivots: dict[frozenset[int], dict[frozenset[int], Fraction]] = {}
    rank = 0
    for raw in columns:
        column = {key: Fraction(value) for key, value in raw.items() if value}
        while column:
            pivot = min(column, key=lambda item: tuple(sorted(item)))
            if pivot not in pivots:
                scale = column[pivot]
                normalized = {key: value / scale for key, value in column.items()}
                pivots[pivot] = normalized
                rank += 1
                break
            multiplier = column[pivot]
            for key, value in pivots[pivot].items():
                updated = column.get(key, Fraction(0)) - multiplier * value
                if updated:
                    column[key] = updated
                else:
                    column.pop(key, None)
    return rank


def coupled_derivative_rank(output_degree: int) -> int:
    operator_degree = 6 - output_degree
    columns = [
        derivative_column(frozenset(operator), output_degree)
        for operator in combinations(range(VARIABLE_COUNT), operator_degree)
    ]
    return sparse_exact_rank(columns)


def audit() -> dict[str, object]:
    overlap = len(SUPPORT_A & SUPPORT_B)
    rows = []
    coupled_ranks = {}
    for degree in (2, 3, 4):
        individual = comb(6, degree)
        literal_intersection = comb(overlap, degree) if degree <= overlap else 0
        literal_sum = 2 * individual - literal_intersection
        relation_dimension = literal_intersection
        coupled_rank = coupled_derivative_rank(degree)
        coupled_ranks[str(degree)] = coupled_rank
        rows.append(
            {
                "output_degree": degree,
                "individual_derivative_dimensions": [individual, individual],
                "literal_intersection_dimension": literal_intersection,
                "literal_sum_dimension": literal_sum,
                "ordinary_relation_dimension_kappa": relation_dimension,
                "coupled_derivative_rank_of_TA_plus_TB": coupled_rank,
            }
        )

    if overlap != 2:
        raise AssertionError(overlap)
    if coupled_ranks != {"2": 29, "3": 40, "4": 29}:
        raise AssertionError(coupled_ranks)
    if [row["ordinary_relation_dimension_kappa"] for row in rows] != [1, 0, 0]:
        raise AssertionError(rows)

    return {
        "status": "EXACT_N6_CENTRAL_NEARDIRECT_QUADRATIC_BARRIER",
        "arithmetic": "pure support counting plus exact rational sparse elimination",
        "terms": {
            "TA": "x0*x1*x2*x3*x4*x5",
            "TB": "x0*x1*x6*x7*x8*x9",
            "support_intersection": [0, 1],
            "support_intersection_dimension": overlap,
        },
        "degree_rows": rows,
        "strict_conclusion": (
            "Even literal directness in degrees three and four does not force "
            "quadratic literal directness for sextic Chow terms: kappa_3=kappa_4=0 "
            "while kappa_2=1. Hence any backward shortcut requiring kappa_2=0 "
            "fails; this does not rule out quantitative relation-shadow inequalities."
        ),
        "claim_boundary": (
            "This two-term example does not involve E_m(perm_6), does not realize "
            "the lower-28 b=34 relative incidence, and neither proves nor refutes "
            "ordinary lower 28, exact rank 32, or a border-rank statement."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    arguments = parser.parse_args()
    payload = audit()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.verify_json is not None:
        expected = json.loads(arguments.verify_json.read_text(encoding="utf-8"))
        if payload != expected:
            raise AssertionError("frozen JSON differs from exact replay")
    print("degree_2_coupled_rank=29")
    print("degree_3_coupled_rank=40")
    print("degree_4_coupled_rank=29")
    print("ordinary_relation_dimensions=(1,0,0)")
    print("N6_CENTRAL_NEARDIRECT_QUADRATIC_BARRIER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
