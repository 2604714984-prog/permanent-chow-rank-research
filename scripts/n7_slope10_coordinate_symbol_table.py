#!/usr/bin/env python3
"""Exact coordinate tables used in the perm_7 slope-ten local lemma.

For the rank-six monomial x0^2*x1*...*x5 and the rank-seven squarefree
monomial, enumerate every coordinate factor quotient and every coordinate
quadratic quotient subspace of dimension at most three.  Distinct source
monomials have disjoint symbol supports, so the ranks are obtained by exact
support counting.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def bounded_monomials(caps: tuple[int, ...], degree: int):
    return tuple(
        exponent
        for exponent in itertools.product(
            *(range(cap + 1) for cap in caps)
        )
        if sum(exponent) == degree
    )


def derivative(exponent: tuple[int, ...], variable: int):
    if exponent[variable] == 0:
        return None
    answer = list(exponent)
    answer[variable] -= 1
    return tuple(answer)


def minimum_rows(caps: tuple[int, ...]) -> dict[str, object]:
    variables = len(caps)
    degree_two = bounded_monomials(caps, 2)
    degree_three = bounded_monomials(caps, 3)
    degree_four = bounded_monomials(caps, 4)
    rows = []
    for quotient_rank in range(variables + 1):
        best = None
        for active_tuple in itertools.combinations(
            range(variables), quotient_rank
        ):
            active = frozenset(active_tuple)
            plus_rank = sum(
                any(exponent[index] for index in active)
                for exponent in degree_four
            )
            for relation_dimension in range(4):
                for relation_tuple in itertools.combinations(
                    degree_two, relation_dimension
                ):
                    relations = frozenset(relation_tuple)
                    killed = sum(
                        all(
                            derivative(exponent, index) in relations
                            for index in active
                            if exponent[index]
                        )
                        for exponent in degree_three
                    )
                    minus_rank = len(degree_three) - killed
                    combined = plus_rank + minus_rank
                    witness = {
                        "active_coordinates": list(active_tuple),
                        "quadratic_relations": [
                            list(exponent) for exponent in relation_tuple
                        ],
                        "plus_rank": plus_rank,
                        "minus_rank": minus_rank,
                        "combined_rank": combined,
                    }
                    if best is None or combined < best["combined_rank"]:
                        best = witness
        assert best is not None
        rows.append(best)
    return {
        "exponent_caps": list(caps),
        "hilbert_2_3_4": [
            len(degree_two),
            len(degree_three),
            len(degree_four),
        ],
        "minimum_combined_rank_by_quotient_rank": [
            row["combined_rank"] for row in rows
        ],
        "witness_rows": rows,
    }


def minimum_minus_rank(caps: tuple[int, ...], quotient_rank: int) -> int:
    variables = len(caps)
    degree_two = bounded_monomials(caps, 2)
    degree_three = bounded_monomials(caps, 3)
    answer = len(degree_three)
    for active_tuple in itertools.combinations(
        range(variables), quotient_rank
    ):
        active = frozenset(active_tuple)
        for relation_dimension in range(4):
            for relation_tuple in itertools.combinations(
                degree_two, relation_dimension
            ):
                relations = frozenset(relation_tuple)
                killed = sum(
                    all(
                        derivative(exponent, index) in relations
                        for index in active
                        if exponent[index]
                    )
                    for exponent in degree_three
                )
                answer = min(answer, len(degree_three) - killed)
    return answer


def build_certificate() -> dict[str, object]:
    rank_five_a_full = minimum_rows((3, 1, 1, 1, 1))
    rank_five_b_full = minimum_rows((2, 2, 1, 1, 1))
    rank_six_full = minimum_rows((2, 1, 1, 1, 1, 1))
    rank_seven_full = minimum_rows((1, 1, 1, 1, 1, 1, 1))
    assert rank_five_a_full[
        "minimum_combined_rank_by_quotient_rank"
    ] == [0, 12, 17, 21, 24, 27]
    assert rank_five_b_full[
        "minimum_combined_rank_by_quotient_rank"
    ] == [0, 15, 22, 24, 30, 34]
    assert rank_six_full["minimum_combined_rank_by_quotient_rank"] == [
        0,
        22,
        33,
        37,
        41,
        44,
        48,
    ]
    assert rank_seven_full["minimum_combined_rank_by_quotient_rank"] == [
        0,
        32,
        49,
        56,
        57,
        64,
        67,
        69,
    ]
    rank_six_d5_minus = minimum_minus_rank(
        (2, 1, 1, 1, 1, 1), 5
    )
    assert rank_six_d5_minus == 19
    rank_six = {
        "exponent_caps": rank_six_full["exponent_caps"],
        "hilbert_2_3_4": rank_six_full["hilbert_2_3_4"],
        "minimum_combined_rank_by_quotient_rank": (
            rank_six_full["minimum_combined_rank_by_quotient_rank"]
        ),
        "minimum_minus_rank_at_quotient_rank_five": rank_six_d5_minus,
    }
    rank_seven = {
        "exponent_caps": rank_seven_full["exponent_caps"],
        "hilbert_2_3_4": rank_seven_full["hilbert_2_3_4"],
        "minimum_combined_rank_by_quotient_rank": (
            rank_seven_full["minimum_combined_rank_by_quotient_rank"]
        ),
    }
    rank_five = [
        {
            "exponent_caps": row["exponent_caps"],
            "hilbert_2_3_4": row["hilbert_2_3_4"],
            "minimum_combined_rank_by_quotient_rank": (
                row["minimum_combined_rank_by_quotient_rank"]
            ),
        }
        for row in (rank_five_a_full, rank_five_b_full)
    ]
    return {
        "schema_version": 1,
        "method": (
            "Exhaust all coordinate quotient subsets and all coordinate "
            "quadratic relation sets of cardinality at most three."
        ),
        "rank_six": rank_six,
        "rank_seven": rank_seven,
        "rank_five_positive_partitions": rank_five,
        "full_quotient_correction": (
            "For the actual permanent intersection R, quadratic generation "
            "gives E2^(1)=E3 and D3(T) cap E3=0, so the full minus symbol is "
            "injective. The last combined ranks are therefore 50 and 70."
        ),
        "claim_boundary": (
            "The table is the finite coordinate endpoint of a separate "
            "torus-degeneration argument. By itself it does not prove that "
            "arbitrary quotients specialize with the required scope."
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
        raise SystemExit("slope-ten coordinate table JSON mismatch")
    print("PASS slope-ten coordinate symbol table")


if __name__ == "__main__":
    main()
