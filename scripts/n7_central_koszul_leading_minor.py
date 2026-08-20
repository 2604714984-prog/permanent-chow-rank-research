#!/usr/bin/env python3
"""Explicit unitriangular minor for the central perm_7 Koszul map.

The full matrix is never materialized.  For each output subpermanent there
are only sixteen possible parents.  Inclusion--exclusion counts output wedges
for which at least one parent has that row as its leading term.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import random
from itertools import combinations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n7_central_koszul_leading_minor.json"
N = 7
OUTPUT_DEGREE = 4
WEDGE_DEGREE = 24
INTERNAL_TERM_ROW = (35, 224, 595, 832, 595, 224, 35, 0)
_OUTPUT_ORDER: tuple[int, ...] | None = None


def set_output_order(order: tuple[int, ...] | None) -> None:
    global _OUTPUT_ORDER
    _OUTPUT_ORDER = order


def random_output_order(output_count: int, seed: int) -> tuple[int, ...]:
    ordered = list(range(output_count))
    random.Random(seed).shuffle(ordered)
    ranks = [0] * output_count
    for rank, output_id in enumerate(ordered):
        ranks[output_id] = rank
    return tuple(ranks)


def candidate_event_masks(
    n: int, output_rows: tuple[int, ...], output_columns: tuple[int, ...]
) -> tuple[int, ...]:
    """Required output-wedge variables for every possible parent."""

    row_set = set(output_rows)
    column_set = set(output_columns)
    output_subsets = tuple(combinations(range(n), len(output_rows)))
    output_index = {subset: index for index, subset in enumerate(output_subsets)}
    output_count = len(output_subsets)
    events: list[int] = []
    for added_row in range(n):
        if added_row in row_set:
            continue
        for added_column in range(n):
            if added_column in column_set:
                continue
            rows = tuple(sorted((*output_rows, added_row)))
            columns = tuple(sorted((*output_columns, added_column)))
            candidates = []
            for row in rows:
                for column in columns:
                    candidates.append(
                        (
                            tuple(entry for entry in rows if entry != row),
                            tuple(entry for entry in columns if entry != column),
                            n * row + column,
                        )
                    )
            candidates.sort(
                key=lambda candidate: (
                    _OUTPUT_ORDER[
                        output_index[candidate[0]] * output_count
                        + output_index[candidate[1]]
                    ]
                    if _OUTPUT_ORDER is not None
                    else output_index[candidate[0]] * output_count
                    + output_index[candidate[1]],
                    candidate[2],
                )
            )
            variable = n * added_row + added_column
            position = next(
                index
                for index, candidate in enumerate(candidates)
                if candidate
                == (output_rows, output_columns, variable)
            )
            required = 1 << variable
            for candidate in candidates[:position]:
                required |= 1 << candidate[2]
            events.append(required)
    return tuple(events)


def union_of_events_count(
    variable_count: int, output_wedge_size: int, events: tuple[int, ...]
) -> int:
    """Count fixed-size subsets containing at least one required event set."""

    choose = [
        comb(variable_count - size, output_wedge_size - size)
        if size <= output_wedge_size
        else 0
        for size in range(variable_count + 1)
    ]
    unions = [0] * (1 << len(events))
    total = 0
    for subset in range(1, 1 << len(events)):
        low_bit = subset & -subset
        event_index = low_bit.bit_length() - 1
        union = unions[subset ^ low_bit] | events[event_index]
        unions[subset] = union
        value = choose[union.bit_count()]
        total += value if subset.bit_count() & 1 else -value
    return total


def output_block_count(args: tuple[int, int, int, int]) -> int:
    n, output_degree, wedge_degree, encoded = args
    subsets = tuple(combinations(range(n), output_degree - 1))
    row_index, column_index = divmod(encoded, len(subsets))
    events = candidate_event_masks(n, subsets[row_index], subsets[column_index])
    return union_of_events_count(n * n, wedge_degree + 1, events)


def leading_minor_rank(
    n: int,
    output_degree: int,
    wedge_degree: int,
    workers: int = 1,
    output_order: tuple[int, ...] | None = None,
) -> int:
    subset_count = comb(n, output_degree - 1)
    tasks = (
        (n, output_degree, wedge_degree, encoded)
        for encoded in range(subset_count * subset_count)
    )
    if workers <= 1:
        set_output_order(output_order)
        try:
            return sum(output_block_count(task) for task in tasks)
        finally:
            set_output_order(None)
    method = "fork" if os.name != "nt" else "spawn"
    with mp.get_context(method).Pool(
        processes=workers, initializer=set_output_order, initargs=(output_order,)
    ) as pool:
        return sum(pool.imap(output_block_count, tasks, chunksize=2))


def one_term_rank() -> int:
    inactive = N * N - N
    return sum(
        comb(inactive, WEDGE_DEGREE - active_wedge) * rank
        for active_wedge, rank in enumerate(INTERNAL_TERM_ROW)
        if 0 <= WEDGE_DEGREE - active_wedge <= inactive
    )


def build_payload(workers: int = 1, order_seed: int | None = None) -> dict[str, object]:
    output_count = comb(N, OUTPUT_DEGREE - 1) ** 2
    order = random_output_order(output_count, order_seed) if order_seed is not None else None
    rank = leading_minor_rank(N, OUTPUT_DEGREE, WEDGE_DEGREE, workers, order)
    term = one_term_rank()
    threshold = 50 * term
    output_basis_count = output_count
    event_count = (N - OUTPUT_DEGREE + 1) ** 2
    return {
        "status": "EXACT_UNITRIANGULAR_MINOR_ROUTE_DIAGNOSTIC",
        "field": "integer minor; valid in characteristic zero",
        "n": N,
        "map": {
            "output_degree": OUTPUT_DEGREE,
            "wedge_degree": WEDGE_DEGREE,
            "source": "E_4(perm_7) tensor exterior^24(k^49)",
            "target": "E_3(perm_7) tensor exterior^25(k^49)",
        },
        "bounded_enumeration": {
            "output_subpermanent_count": output_basis_count,
            "parent_events_per_output": event_count,
            "inclusion_exclusion_states_per_output": (1 << event_count) - 1,
            "total_inclusion_exclusion_states": output_basis_count * ((1 << event_count) - 1),
            "full_matrix_materialized": False,
            "output_order": "lexicographic" if order_seed is None else "deterministic shuffled",
            "output_order_seed": order_seed,
        },
        "leading_minor_rank": rank,
        "one_independent_chow_term_rank": {
            "active_internal_row": list(INTERNAL_TERM_ROW),
            "inactive_variable_count": N * N - N,
            "rank": term,
        },
        "lower_50_test": {
            "threshold": threshold,
            "strict_gap": rank - threshold,
            "passes": rank > threshold,
        },
        "ordinary_chow_consequence": {
            "integer_lower_bound": (rank + term - 1) // term,
            "applies_to": "ordinary Chow rank",
        },
        "claim_boundary": [
            "The certificate is an explicit integer unitriangular minor, not a numerical rank estimate.",
            "It is only a lower bound for the full central Koszul rank, not an upper bound.",
            "This explicit minor does not improve the established ordinary lower bound 49.",
            "The one-term denominator is the maximum attained by seven independent factors.",
            "No border Chow-rank claim is made.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--order-seed", type=int)
    parser.add_argument("--search-order-seeds", type=int, default=0)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    if args.search_order_seeds:
        output_count = comb(N, OUTPUT_DEGREE - 1) ** 2
        for seed in range(args.search_order_seeds):
            order = random_output_order(output_count, seed)
            rank = leading_minor_rank(N, OUTPUT_DEGREE, WEDGE_DEGREE, max(1, args.workers), order)
            print(json.dumps({"seed": seed, "rank": rank}, separators=(",", ":")), flush=True)
        return 0
    payload = build_payload(max(1, args.workers), args.order_seed)
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
