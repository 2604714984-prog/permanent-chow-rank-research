#!/usr/bin/env python3
"""Exact Venn-type audit for three squarefree degree-six Chow terms."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


def rank_q(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    data = [[Fraction(value) for value in row] for row in matrix]
    rows = len(data)
    columns = len(data[0])
    pivot_row = 0
    for column in range(columns):
        source = next(
            (row for row in range(pivot_row, rows) if data[row][column]),
            None,
        )
        if source is None:
            continue
        data[pivot_row], data[source] = data[source], data[pivot_row]
        scale = data[pivot_row][column]
        data[pivot_row] = [value / scale for value in data[pivot_row]]
        for row in range(pivot_row + 1, rows):
            if not data[row][column]:
                continue
            scale = data[row][column]
            data[row] = [
                data[row][index] - scale * data[pivot_row][index]
                for index in range(columns)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def canonical_supports(
    parameters: tuple[int, int, int, int]
) -> tuple[tuple[int, ...], ...] | None:
    ab_only, ac_only, bc_only, triple = parameters
    a_only = 6 - ab_only - ac_only - triple
    b_only = 6 - ab_only - bc_only - triple
    c_only = 6 - ac_only - bc_only - triple
    if min(a_only, b_only, c_only) < 0:
        return None

    next_variable = 0

    def take(size: int) -> list[int]:
        nonlocal next_variable
        values = list(range(next_variable, next_variable + size))
        next_variable += size
        return values

    cell_a = take(a_only)
    cell_b = take(b_only)
    cell_c = take(c_only)
    cell_ab = take(ab_only)
    cell_ac = take(ac_only)
    cell_bc = take(bc_only)
    cell_abc = take(triple)
    supports = (
        tuple(sorted(cell_a + cell_ab + cell_ac + cell_abc)),
        tuple(sorted(cell_b + cell_ab + cell_bc + cell_abc)),
        tuple(sorted(cell_c + cell_ac + cell_bc + cell_abc)),
    )
    if len(set(supports)) != 3:
        return None
    return supports


def relation_pairing_matrix(
    supports: tuple[tuple[int, ...], ...]
) -> tuple[int, list[list[int]]]:
    coordinates: list[tuple[int, tuple[int, ...]]] = []
    occurrences: dict[tuple[int, ...], list[int]] = {}
    for term, support in enumerate(supports):
        for monomial in combinations(support, 3):
            coordinates.append((term, monomial))
            occurrences.setdefault(monomial, []).append(term)
    position = {coordinate: index for index, coordinate in enumerate(coordinates)}
    relations: list[dict[int, int]] = []
    for monomial, terms in sorted(occurrences.items()):
        for term in terms[1:]:
            relations.append(
                {
                    position[(terms[0], monomial)]: -1,
                    position[(term, monomial)]: 1,
                }
            )

    support_sets = [set(support) for support in supports]
    matrix: list[list[int]] = []
    for first in relations:
        row: list[int] = []
        for second in relations:
            value = 0
            for coordinate, coefficient in first.items():
                term, monomial = coordinates[coordinate]
                complement = tuple(
                    sorted(support_sets[term] - set(monomial))
                )
                value += coefficient * second.get(
                    position[(term, complement)], 0
                )
            row.append(value)
        matrix.append(row)
    return len(relations), matrix


def central_catalectic_rank(
    supports: tuple[tuple[int, ...], ...]
) -> int:
    variables = sorted(set().union(*(set(support) for support in supports)))
    triples = list(combinations(variables, 3))
    position = {triple: index for index, triple in enumerate(triples)}
    matrix = [[0] * len(triples) for _ in triples]
    for support in supports:
        support_set = set(support)
        for triple in combinations(support, 3):
            complement = tuple(sorted(support_set - set(triple)))
            matrix[position[triple]][position[complement]] += 1
    return rank_q(matrix)


def record(parameters: tuple[int, int, int, int]) -> dict[str, object] | None:
    supports = canonical_supports(parameters)
    if supports is None:
        return None
    rho, pairing = relation_pairing_matrix(supports)
    pairing_rank = rank_q(pairing)
    radical = rho - pairing_rank
    central_rank = 60 - 2 * rho + pairing_rank
    return {
        "venn_parameters_ab_ac_bc_only_and_triple": list(parameters),
        "supports": [list(support) for support in supports],
        "rho": rho,
        "pairing_rank_over_Q": pairing_rank,
        "radical_dimension": radical,
        "central_rank": central_rank,
    }


def build_payload() -> dict[str, object]:
    records = []
    for parameters in product(range(7), repeat=4):
        item = record(parameters)
        if item is not None:
            records.append(item)
    strict = [item for item in records if item["central_rank"] > 40]
    maximum = max(int(item["radical_dimension"]) for item in strict)
    equality = [
        item for item in strict if item["radical_dimension"] == maximum
    ]
    rho_nine = [item for item in records if item["rho"] == 9]

    witness = canonical_supports((0, 0, 0, 4))
    if witness is None:
        raise AssertionError("missing equality witness")
    witness_direct_rank = central_catalectic_rank(witness)
    if maximum != 8 or witness_direct_rank != 44:
        raise AssertionError((maximum, witness_direct_rank))
    if any(item["pairing_rank_over_Q"] != 4 for item in rho_nine):
        raise AssertionError(rho_nine)

    return {
        "method": "exact-rational-exhaustion-of-three-set-venn-types",
        "field": "Q",
        "degree": 6,
        "term_count": 3,
        "valid_ordered_venn_types": len(records),
        "types_with_central_rank_strictly_above_two_term_cap": len(strict),
        "two_term_central_rank_cap": 40,
        "maximum_radical_dimension_among_strict_types": maximum,
        "equality_type_count": len(equality),
        "equality_types": equality,
        "rho_nine_type_count": len(rho_nine),
        "rho_nine_types": rho_nine,
        "equality_witness_direct_central_rank_over_Q": witness_direct_rank,
        "conclusion": (
            "For three distinct squarefree degree-six coordinate monomials, "
            "central rank above 40 certifies Chow rank three and forces the "
            "central pairing radical to have dimension at most 8; equality "
            "is attained."
        ),
        "scope": (
            "This is a coordinate-squarefree three-term theorem. It does not "
            "classify arbitrary three-term Chow decompositions or q>=4."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
