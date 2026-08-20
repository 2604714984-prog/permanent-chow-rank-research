#!/usr/bin/env python3
"""Exact Koszul leading minors for a 29-edge restriction of perm_7."""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import random
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
from pathlib import Path


N = 7
VARIABLE_COUNT = N * N
OUTPUT_DEGREE = 4
ACTIVE_EDGES = (
    (0, 0), (0, 3), (0, 4), (0, 5),
    (1, 1), (1, 2), (1, 3), (1, 5),
    (2, 1), (2, 4), (2, 5), (2, 6),
    (3, 2), (3, 3), (3, 4), (3, 6),
    (4, 0), (4, 1), (4, 3), (4, 4), (4, 6),
    (5, 0), (5, 2), (5, 5), (5, 6),
    (6, 0), (6, 1), (6, 2), (6, 4),
)
ACTIVE = frozenset(N * row + column for row, column in ACTIVE_EDGES)
ACTIVE_TUPLE = tuple(sorted(ACTIVE))
ACTIVE_POSITION = {edge: index for index, edge in enumerate(ACTIVE_TUPLE)}
ACTIVE_COUNT = len(ACTIVE)
INTERNAL_TERM_ROW = (35, 224, 595, 832, 595, 224, 35, 0)
DEFAULT_JSON = Path(__file__).resolve().parents[1] / "data" / "n7_coordinate29_koszul_minor.json"
_OUTPUT_ORDER: tuple[int, ...] | None = None


def set_output_order(order: tuple[int, ...] | None) -> None:
    global _OUTPUT_ORDER
    _OUTPUT_ORDER = order


def random_output_order(seed: int) -> tuple[int, ...]:
    output_count = len(OUTPUT_SUBSETS) ** 2
    ordered = list(range(output_count))
    random.Random(seed).shuffle(ordered)
    ranks = [0] * output_count
    for rank, output_id in enumerate(ordered):
        ranks[output_id] = rank
    return tuple(ranks)


def supported(rows: tuple[int, ...], columns: tuple[int, ...]) -> bool:
    return any(
        all(N * row + column in ACTIVE for row, column in zip(rows, order))
        for order in permutations(columns)
    )


def derivative_supported(rows: tuple[int, ...], columns: tuple[int, ...]) -> bool:
    row_set = set(rows)
    column_set = set(columns)
    complement_rows = tuple(row for row in range(N) if row not in row_set)
    complement_columns = tuple(column for column in range(N) if column not in column_set)
    return supported(rows, columns) and supported(complement_rows, complement_columns)


OUTPUT_SUBSETS = tuple(combinations(range(N), OUTPUT_DEGREE - 1))
OUTPUT_INDEX = {subset: index for index, subset in enumerate(OUTPUT_SUBSETS)}
SUPPORTED_OUTPUTS = tuple(
    (rows, columns)
    for rows in OUTPUT_SUBSETS
    for columns in OUTPUT_SUBSETS
    if derivative_supported(rows, columns)
)


def candidate_event_masks(
    output_rows: tuple[int, ...], output_columns: tuple[int, ...]
) -> tuple[int, ...]:
    row_set = set(output_rows)
    column_set = set(output_columns)
    events = []
    for added_row in range(N):
        if added_row in row_set:
            continue
        for added_column in range(N):
            if added_column in column_set:
                continue
            variable = N * added_row + added_column
            if variable not in ACTIVE:
                continue
            rows = tuple(sorted((*output_rows, added_row)))
            columns = tuple(sorted((*output_columns, added_column)))
            if not derivative_supported(rows, columns):
                continue
            candidates = []
            for row in rows:
                for column in columns:
                    candidate_variable = N * row + column
                    candidate_rows = tuple(entry for entry in rows if entry != row)
                    candidate_columns = tuple(entry for entry in columns if entry != column)
                    if candidate_variable in ACTIVE and derivative_supported(
                        candidate_rows, candidate_columns
                    ):
                        candidates.append(
                            (candidate_rows, candidate_columns, candidate_variable)
                        )
            candidates.sort(
                key=lambda candidate: (
                    _OUTPUT_ORDER[
                        OUTPUT_INDEX[candidate[0]] * len(OUTPUT_SUBSETS)
                        + OUTPUT_INDEX[candidate[1]]
                    ]
                    if _OUTPUT_ORDER is not None
                    else OUTPUT_INDEX[candidate[0]] * len(OUTPUT_SUBSETS)
                    + OUTPUT_INDEX[candidate[1]],
                    candidate[2],
                )
            )
            current = (output_rows, output_columns, variable)
            position = candidates.index(current)
            required = 1 << ACTIVE_POSITION[variable]
            for candidate in candidates[:position]:
                required |= 1 << ACTIVE_POSITION[candidate[2]]
            events.append(required)
    return tuple(events)


def signed_union_size_histogram(events: tuple[int, ...]) -> tuple[int, ...]:
    unions = [0] * (1 << len(events))
    histogram = [0] * (ACTIVE_COUNT + 1)
    for subset in range(1, 1 << len(events)):
        low_bit = subset & -subset
        event_index = low_bit.bit_length() - 1
        union = unions[subset ^ low_bit] | events[event_index]
        unions[subset] = union
        histogram[union.bit_count()] += 1 if subset.bit_count() & 1 else -1
    return tuple(histogram)


def output_histogram(encoded: int) -> tuple[int, ...]:
    rows, columns = SUPPORTED_OUTPUTS[encoded]
    return signed_union_size_histogram(candidate_event_masks(rows, columns))


def aggregate_histogram(
    workers: int, output_order: tuple[int, ...] | None = None
) -> tuple[int, ...]:
    total = [0] * (ACTIVE_COUNT + 1)
    tasks = range(len(SUPPORTED_OUTPUTS))
    if workers <= 1:
        set_output_order(output_order)
        rows = map(output_histogram, tasks)
        pool = None
    else:
        method = "fork" if os.name != "nt" else "spawn"
        pool = mp.get_context(method).Pool(
            processes=workers,
            initializer=set_output_order,
            initargs=(output_order,),
        )
        rows = pool.imap(output_histogram, tasks, chunksize=2)
    try:
        for row in rows:
            for size, value in enumerate(row):
                total[size] += value
    finally:
        if pool is not None:
            pool.close()
            pool.join()
        else:
            set_output_order(None)
    return tuple(total)


def leading_rank(histogram: tuple[int, ...], wedge_degree: int) -> int:
    output_wedge_size = wedge_degree + 1
    return sum(
        coefficient * comb(ACTIVE_COUNT - size, output_wedge_size - size)
        for size, coefficient in enumerate(histogram)
        if coefficient and size <= output_wedge_size
    )


def one_term_rank(wedge_degree: int) -> int:
    inactive = ACTIVE_COUNT - N
    return sum(
        comb(inactive, wedge_degree - active_wedge) * rank
        for active_wedge, rank in enumerate(INTERNAL_TERM_ROW)
        if 0 <= wedge_degree - active_wedge <= inactive
    )


def build_payload(workers: int = 1) -> dict[str, object]:
    if ACTIVE_COUNT != 29 or len(SUPPORTED_OUTPUTS) != 1061:
        raise AssertionError((ACTIVE_COUNT, len(SUPPORTED_OUTPUTS)))
    histogram = aggregate_histogram(max(1, workers))
    rows = []
    for wedge_degree in range(ACTIVE_COUNT):
        rank = leading_rank(histogram, wedge_degree)
        term = one_term_rank(wedge_degree)
        rows.append(
            {
                "wedge_degree": wedge_degree,
                "leading_minor_rank": rank,
                "one_independent_chow_term_rank": term,
                "ratio_numerator": rank,
                "ratio_denominator": term,
                "integer_lower_bound": (rank + term - 1) // term,
                "passes_lower_50_test": rank > 50 * term,
            }
        )
    best = max(
        rows,
        key=lambda row: Fraction(row["ratio_numerator"], row["ratio_denominator"]),
    )
    return {
        "schema_version": 1,
        "status": "EXACT_COORDINATE_RESTRICTION_UNITRIANGULAR_MINOR_SCAN",
        "field": "integer minors; valid in characteristic zero",
        "n": N,
        "active_edge_count": ACTIVE_COUNT,
        "ambient_coordinate_graph_candidate_count": comb(VARIABLE_COUNT, ACTIVE_COUNT),
        "active_edges": [list(edge) for edge in ACTIVE_EDGES],
        "supported_degree_three_and_four_subpermanent_count": len(SUPPORTED_OUTPUTS),
        "bounded_enumeration": {
            "maximum_parent_events_per_output": 16,
            "full_matrices_materialized": False,
            "wedge_degrees_recovered_from_one_histogram": ACTIVE_COUNT,
        },
        "signed_union_size_histogram": list(histogram),
        "rows": rows,
        "best_row": best,
        "any_lower_50_test_passes": any(row["passes_lower_50_test"] for row in rows),
        "ordinary_chow_lower_bound_from_best_minor": best["integer_lower_bound"],
        "claim_boundary": [
            "Coordinate restriction preserves every ordinary Chow decomposition termwise.",
            "Each displayed rank is an exact integer unitriangular minor of the restricted permanent Koszul map.",
            "The independent seven-factor rank is a uniform upper cap for a specialized Chow term.",
            "The finite graph search that found the witness is not used in the proof.",
            "No border Chow-rank claim is made.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--search-order-seeds", type=int, default=0)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    if args.search_order_seeds:
        term = one_term_rank(14)
        for seed in range(args.search_order_seeds):
            histogram = aggregate_histogram(
                max(1, args.workers), random_output_order(seed)
            )
            rank = leading_rank(histogram, 14)
            print(
                json.dumps(
                    {
                        "seed": seed,
                        "wedge_degree": 14,
                        "rank": rank,
                        "ratio_numerator": rank,
                        "ratio_denominator": term,
                        "passes_lower_50_test": rank > 50 * term,
                    },
                    separators=(",", ":"),
                ),
                flush=True,
            )
        return 0
    payload = build_payload(max(1, args.workers))
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("frozen payload mismatch")
        print("PASS")
    elif args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
