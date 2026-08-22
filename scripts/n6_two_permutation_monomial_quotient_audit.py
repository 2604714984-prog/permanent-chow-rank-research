#!/usr/bin/env python3
"""Exact rational two-permutation-monomial quotient audit for ``perm_6``."""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
BASE_SCRIPT = ROOT / "scripts" / "n6_coordinate_monomial_full_gain_audit.py"


def load_base_audit() -> ModuleType:
    spec = importlib.util.spec_from_file_location("n6_coordinate_base", BASE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base_audit()
N = 6
VARIABLES = 36
SparseColumn = dict[int, int]
Weight = tuple[int, ...]


def integer_partitions(total: int, minimum: int = 1):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def permutation_with_cycle_type(cycle_type: tuple[int, ...]) -> list[int]:
    permutation = [-1] * N
    start = 0
    for length in cycle_type:
        cycle = list(range(start, start + length))
        start += length
        for index, value in enumerate(cycle):
            permutation[value] = cycle[(index + 1) % length]
    if sorted(permutation) != list(range(N)):
        raise AssertionError((cycle_type, permutation))
    return permutation


def integer_delta_column(
    polynomial: list[tuple[int, ...]], tensor_variable: int
) -> SparseColumn:
    entries: Counter[int] = Counter()
    for monomial in polynomial:
        if len(monomial) != 3:
            raise ValueError(monomial)
        for position, variable in enumerate(monomial):
            if variable == tensor_variable:
                continue
            remaining = sorted(
                monomial[index] for index in range(3) if index != position
            )
            first, second = sorted((variable, tensor_variable))
            sign = 1 if variable < tensor_variable else -1
            row = (
                BASE.SYMMETRIC_INDEX[(remaining[0], remaining[1])] * 630
                + BASE.WEDGE_INDEX[(first, second)]
            )
            entries[row] += sign
    return {row: value for row, value in entries.items() if value}


def exact_sparse_rank(columns: list[SparseColumn]) -> int:
    pivots: dict[int, dict[int, Fraction]] = {}
    for raw in columns:
        vector = {
            row: Fraction(value) for row, value in raw.items() if value
        }
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in pivots:
                pivots[pivot] = {
                    row: value / coefficient for row, value in vector.items()
                }
                break
            reference = pivots[pivot]
            for row, value in reference.items():
                updated = vector.get(row, Fraction(0)) - coefficient * value
                if updated:
                    vector[row] = updated
                else:
                    vector.pop(row, None)
    return len(pivots)


def monomial_weight(monomial: tuple[int, ...], tensor_variable: int) -> Weight:
    row_counts = [0] * N
    column_counts = [0] * N
    for variable in monomial + (tensor_variable,):
        row_counts[variable // N] += 1
        column_counts[variable % N] += 1
    return tuple(row_counts + column_counts)


def permanent_weight(
    rows: tuple[int, ...], columns: tuple[int, ...], tensor_variable: int
) -> Weight:
    return tuple(
        [int(row in rows) + int(tensor_variable // N == row) for row in range(N)]
        + [
            int(column in columns) + int(tensor_variable % N == column)
            for column in range(N)
        ]
    )


def permanent_blocks() -> dict[Weight, list[SparseColumn]]:
    blocks: dict[Weight, list[SparseColumn]] = defaultdict(list)
    for rows in combinations(range(N), 3):
        for columns in combinations(range(N), 3):
            polynomial = BASE.permanent_cubic(rows, columns)
            for tensor_variable in range(VARIABLES):
                weight = permanent_weight(rows, columns, tensor_variable)
                blocks[weight].append(
                    integer_delta_column(polynomial, tensor_variable)
                )
    return dict(blocks)


def term_blocks(edges: list[int]) -> dict[Weight, list[SparseColumn]]:
    blocks: dict[Weight, list[SparseColumn]] = defaultdict(list)
    for monomial in BASE.degree_three_divisors(edges):
        for tensor_variable in range(VARIABLES):
            weight = monomial_weight(monomial, tensor_variable)
            blocks[weight].append(
                integer_delta_column([monomial], tensor_variable)
            )
    return dict(blocks)


def build_payload() -> dict[str, object]:
    base_blocks = permanent_blocks()
    base_ranks = {
        weight: exact_sparse_rank(columns)
        for weight, columns in base_blocks.items()
    }
    permanent_rank = sum(base_ranks.values())
    if permanent_rank != 14_175:
        raise AssertionError(permanent_rank)

    diagonal_edges = [row * N + row for row in range(N)]
    diagonal_blocks = term_blocks(diagonal_edges)
    rows: list[dict[str, object]] = []
    for cycle_type in integer_partitions(N):
        permutation = permutation_with_cycle_type(cycle_type)
        second_edges = [row * N + permutation[row] for row in range(N)]
        second_blocks = term_blocks(second_edges)
        weights = set(base_blocks) | set(diagonal_blocks) | set(second_blocks)
        ordinary_span_rank = 0
        combined_rank = 0
        for weight in weights:
            term_columns = (
                diagonal_blocks.get(weight, [])
                + second_blocks.get(weight, [])
            )
            base_columns = base_blocks.get(weight, [])
            if term_columns:
                ordinary_span_rank += exact_sparse_rank(term_columns)
            if base_columns or term_columns:
                combined_rank += exact_sparse_rank(base_columns + term_columns)
        quotient_span_rank = combined_rank - permanent_rank
        internal_relation_dimension = 1_410 - ordinary_span_rank
        aggregate_collision_dimension = (
            ordinary_span_rank - quotient_span_rank
        )
        rows.append(
            {
                "relative_cycle_type": list(cycle_type),
                "shared_permutation_edges": cycle_type.count(1),
                "same_term": len(cycle_type) == N,
                "ordinary_two_output_span_rank_over_Q": ordinary_span_rank,
                "quotient_two_output_span_rank_over_Q": quotient_span_rank,
                "internal_output_relation_dimension_eta": (
                    internal_relation_dimension
                ),
                "aggregate_collision_dimension_j": (
                    aggregate_collision_dimension
                ),
            }
        )

    if any(row["aggregate_collision_dimension_j"] != 0 for row in rows):
        raise AssertionError(rows)
    expected_ordinary = [705, 1267, 1374] + [1410] * 8
    if [row["ordinary_two_output_span_rank_over_Q"] for row in rows] != expected_ordinary:
        raise AssertionError(rows)

    return {
        "method": "exact-rational-row-column-torus-block-elimination",
        "field": "Q",
        "permanent_weight_block_count": len(base_blocks),
        "permanent_koszul_rank_over_Q": permanent_rank,
        "individual_permutation_monomial_koszul_rank": 705,
        "relative_cycle_type_count": len(rows),
        "cycle_types": rows,
        "all_aggregate_collision_dimensions_zero": True,
        "conclusion": (
            "For any two degree-six permutation monomials, the sum of their "
            "Koszul output spaces is disjoint from im K_3(perm_6). Hence the "
            "coupled sum of the two terms has full quotient gain."
        ),
        "scope": (
            "This is exact only for the permutation-monomial subfamily. It "
            "does not control arbitrary coordinate monomials or arbitrary "
            "pairs of Chow terms."
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
