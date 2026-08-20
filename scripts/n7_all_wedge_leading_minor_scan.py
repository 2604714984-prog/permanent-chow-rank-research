#!/usr/bin/env python3
"""Scan every wedge degree for one exact perm_7 Koszul leading rule.

The sixteen parent events for a fixed output subpermanent do not depend on
the wedge size.  We therefore compute their signed union-size histogram once
and recover all 49 fixed-size union counts by binomial convolution.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import sys
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import n7_central_koszul_leading_minor as central  # noqa: E402


N = central.N
OUTPUT_DEGREE = central.OUTPUT_DEGREE
VARIABLE_COUNT = N * N
OUTPUT_BASIS_COUNT = comb(N, OUTPUT_DEGREE - 1) ** 2
EVENT_COUNT = (N - OUTPUT_DEGREE + 1) ** 2
DEFAULT_JSON = HERE.parent / "data" / "n7_all_wedge_leading_minor_scan.json"


def signed_union_size_histogram(events: tuple[int, ...]) -> tuple[int, ...]:
    """Inclusion--exclusion coefficient grouped by union cardinality."""

    unions = [0] * (1 << len(events))
    histogram = [0] * (VARIABLE_COUNT + 1)
    for subset in range(1, 1 << len(events)):
        low_bit = subset & -subset
        event_index = low_bit.bit_length() - 1
        union = unions[subset ^ low_bit] | events[event_index]
        unions[subset] = union
        size = union.bit_count()
        histogram[size] += 1 if subset.bit_count() & 1 else -1
    return tuple(histogram)


def output_histogram(encoded: int) -> tuple[int, ...]:
    subsets = tuple(combinations(range(N), OUTPUT_DEGREE - 1))
    row_index, column_index = divmod(encoded, len(subsets))
    events = central.candidate_event_masks(
        N, subsets[row_index], subsets[column_index]
    )
    return signed_union_size_histogram(events)


def aggregate_histogram(workers: int) -> tuple[int, ...]:
    total = [0] * (VARIABLE_COUNT + 1)
    tasks = range(OUTPUT_BASIS_COUNT)
    if workers <= 1:
        rows = map(output_histogram, tasks)
    else:
        method = "fork" if os.name != "nt" else "spawn"
        pool = mp.get_context(method).Pool(processes=workers)
        rows = pool.imap(output_histogram, tasks, chunksize=2)
    try:
        for row in rows:
            for size, value in enumerate(row):
                total[size] += value
    finally:
        if workers > 1:
            pool.close()
            pool.join()
    return tuple(total)


def leading_rank(histogram: tuple[int, ...], wedge_degree: int) -> int:
    output_wedge_size = wedge_degree + 1
    return sum(
        coefficient * comb(VARIABLE_COUNT - size, output_wedge_size - size)
        for size, coefficient in enumerate(histogram)
        if coefficient
        and size <= output_wedge_size
        and output_wedge_size - size <= VARIABLE_COUNT - size
    )


def one_term_rank(wedge_degree: int) -> int:
    inactive = VARIABLE_COUNT - N
    return sum(
        comb(inactive, wedge_degree - active_wedge) * rank
        for active_wedge, rank in enumerate(central.INTERNAL_TERM_ROW)
        if 0 <= wedge_degree - active_wedge <= inactive
    )


def build_payload(workers: int = 1) -> dict[str, object]:
    histogram = aggregate_histogram(max(1, workers))
    rows = []
    for wedge_degree in range(VARIABLE_COUNT):
        rank = leading_rank(histogram, wedge_degree)
        term = one_term_rank(wedge_degree)
        source_dimension = comb(N, OUTPUT_DEGREE) ** 2 * comb(
            VARIABLE_COUNT, wedge_degree
        )
        target_dimension = comb(N, OUTPUT_DEGREE - 1) ** 2 * comb(
            VARIABLE_COUNT, wedge_degree + 1
        )
        if rank > min(source_dimension, target_dimension):
            raise AssertionError((wedge_degree, rank, source_dimension, target_dimension))
        rows.append(
            {
                "wedge_degree": wedge_degree,
                "leading_minor_rank": rank,
                "one_independent_chow_term_rank": term,
                "ratio_numerator": rank,
                "ratio_denominator": term,
                "integer_lower_bound": (rank + term - 1) // term if term else 0,
                "passes_lower_50_test": bool(term and rank > 50 * term),
            }
        )
    best = max(
        rows,
        key=lambda row: (
            row["integer_lower_bound"],
            Fraction(row["ratio_numerator"], row["ratio_denominator"])
            if row["ratio_denominator"]
            else Fraction(-1),
        ),
    )
    central_row = rows[central.WEDGE_DEGREE]
    if central_row["leading_minor_rank"] != 32_506_369_177_539_449:
        raise AssertionError(central_row)
    return {
        "schema_version": 1,
        "status": "EXACT_ALL_WEDGE_UNITRIANGULAR_MINOR_SCAN",
        "field": "integer minors; valid in characteristic zero",
        "n": N,
        "output_degree": OUTPUT_DEGREE,
        "bounded_enumeration": {
            "output_subpermanent_count": OUTPUT_BASIS_COUNT,
            "parent_events_per_output": EVENT_COUNT,
            "inclusion_exclusion_states_per_output": (1 << EVENT_COUNT) - 1,
            "total_inclusion_exclusion_states": OUTPUT_BASIS_COUNT * ((1 << EVENT_COUNT) - 1),
            "wedge_degrees_recovered_from_one_histogram": VARIABLE_COUNT,
            "full_matrices_materialized": False,
        },
        "signed_union_size_histogram": list(histogram),
        "rows": rows,
        "best_row": best,
        "any_lower_50_test_passes": any(row["passes_lower_50_test"] for row in rows),
        "claim_boundary": [
            "Every row is an exact explicit integer unitriangular-minor lower bound.",
            "The scan exhausts all wedge degrees for this one lexicographic leading rule.",
            "It does not compute or upper-bound the full Koszul ranks.",
            "It makes no border Chow-rank claim.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
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
