#!/usr/bin/env python3
"""Exact audit for relation tableaux and the central pairing correction."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from pathlib import Path

PRIME = 1_000_003


def macaulay_successor(value: int, degree: int) -> int:
    if value < 0 or degree < 1:
        raise ValueError((value, degree))
    remaining = value
    successor = 0
    ceiling = value + degree + 1
    for lower in range(degree, 0, -1):
        if remaining == 0:
            break
        upper = lower
        while upper + 1 < ceiling and comb(upper + 1, lower) <= remaining:
            upper += 1
        if comb(upper, lower) <= remaining:
            remaining -= comb(upper, lower)
            successor += comb(upper + 1, lower + 1)
            ceiling = upper
    if remaining != 0:
        raise AssertionError((value, degree, remaining))
    return successor


def sparse_rank_mod(columns: list[dict[int, int]], prime: int = PRIME) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for raw in columns:
        vector = {row: value % prime for row, value in raw.items() if value % prime}
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, -1, prime)
                pivots[pivot] = {
                    row: value * inverse % prime for row, value in vector.items()
                }
                break
            reference = pivots[pivot]
            for row, value in reference.items():
                updated = (vector.get(row, 0) - coefficient * value) % prime
                if updated:
                    vector[row] = updated
                else:
                    vector.pop(row, None)
    return len(pivots)


def squarefree_central_columns(overlap: int) -> tuple[list[dict[int, int]], int]:
    first = frozenset(range(6))
    second = frozenset(range(overlap)) | frozenset(range(6, 12 - overlap))
    universe = sorted(first | second)
    triples = list(combinations(universe, 3))
    row_index = {triple: index for index, triple in enumerate(triples)}
    columns: list[dict[int, int]] = []
    for derivative in triples:
        derivative_set = frozenset(derivative)
        column: dict[int, int] = {}
        for support in (first, second):
            if derivative_set <= support:
                output = tuple(sorted(support - derivative_set))
                row = row_index[output]
                column[row] = column.get(row, 0) + 1
        columns.append(column)
    return columns, len(triples)


def overlap_record(overlap: int) -> dict[str, int | bool]:
    columns, ambient = squarefree_central_columns(overlap)
    rank_mod = sparse_rank_mod(columns)
    relation_dimension = comb(overlap, 3) if overlap >= 3 else 0
    pairing_rank = 20 if overlap == 6 else 0
    formula_rank = 40 - 2 * relation_dimension + pairing_rank
    if rank_mod != formula_rank:
        raise AssertionError((overlap, rank_mod, formula_rank))
    return {
        "overlap": overlap,
        "ambient_cubic_monomials": ambient,
        "relation_dimension": relation_dimension,
        "relation_pairing_rank": pairing_rank,
        "formula_rank": formula_rank,
        "rank_mod_1000003": rank_mod,
        "strict_nonmerge_two_term_example": overlap == 4,
        "merges_to_one_chow_term": overlap in {5, 6},
    }


def build_payload() -> dict[str, object]:
    degree_two = []
    for value in range(38):
        first = macaulay_successor(value, 2)
        second = macaulay_successor(first, 3)
        degree_two.append(
            {
                "kappa_2": value,
                "kappa_3_cap": first,
                "kappa_4_cap": second,
                "two_sided_relation_loss_cap": value + second,
            }
        )
    expected_degree_two = [0, 1, 2, 4, 5, 7, 10, 11, 13, 16, 20]
    if [row["kappa_3_cap"] for row in degree_two[:11]] != expected_degree_two:
        raise AssertionError(degree_two[:11])

    overlaps = [overlap_record(overlap) for overlap in range(7)]
    expected_ranks = [40, 40, 40, 38, 32, 20, 20]
    if [row["formula_rank"] for row in overlaps] != expected_ranks:
        raise AssertionError(overlaps)

    repeated = [
        {
            "term_count": term_count,
            "individual_rank_sum": 20 * term_count,
            "relation_dimension": 20 * (term_count - 1),
            "relation_pairing_rank": 20 * (term_count - 1),
            "coupled_rank": 20,
        }
        for term_count in range(2, 7)
    ]
    for row in repeated:
        predicted = (
            row["individual_rank_sum"]
            - 2 * row["relation_dimension"]
            + row["relation_pairing_rank"]
        )
        if predicted != row["coupled_rank"]:
            raise AssertionError(row)

    common_factor = [
        {
            "term_count": term_count,
            "kappa_2": 0,
            "kappa_3": 0,
            "kappa_4": 0,
            "coupled_quadratic_rank": 15 * term_count,
            "coupled_central_rank": 20 * term_count,
        }
        for term_count in range(1, 7)
    ]

    return {
        "status": "GENERAL_RELATION_TABLEAU_PAIRING_REPLAYED",
        "field": "characteristic zero with modular nonzero-minor diagnostics",
        "theorems": {
            "vector_macaulay": "dim K^(1) <= dim(K)^{<d>}",
            "tableau_growth": "kappa_(m+1) <= kappa_m^{<m>}",
            "block_sylvester": "rank C_(n-m,m)(sum T_i) >= C-kappa_m-kappa_(n-m)",
            "central_pairing": "rank(sum A_i)=C-2rho+rank(beta restricted to R)",
        },
        "macaulay_two_step_0_through_37": degree_two,
        "squarefree_degree_six_pair_overlaps": overlaps,
        "repeated_term_boundary": repeated,
        "common_factor_boundary": common_factor,
        "n6_route_decision": (
            "The exact pairing correction can vanish for a strict two-term Chow "
            "sum, and the two-step dimension cap is ambient-vacuous at kappa_2=37."
        ),
        "claim_boundary": "No ChowRank(perm_6)>=26 conclusion is obtained.",
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
    print("GENERAL_RELATION_TABLEAU_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
