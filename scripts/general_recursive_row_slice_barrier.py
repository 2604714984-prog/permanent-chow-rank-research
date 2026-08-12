#!/usr/bin/env python3
"""Exact integer replay for the recursive-row mixed-derivative barrier.

No finite-field or floating-point calculation is used.  The formulas are
dimensions of explicitly described subpermanent bases.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path


def choose(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def row_slice_entry(n: int, m: int) -> dict[str, int]:
    cap = choose(n, m)
    rank = choose(n - 1, m) * cap
    component_rank = choose(n - 1, m) ** 2
    sum_of_component_ranks = n * component_rank
    return {
        "m": m,
        "permanent_rank": rank,
        "one_term_cap": cap,
        "rank_ratio": rank // cap,
        "one_cofactor_rank": component_rank,
        "sum_of_cofactor_ranks": sum_of_component_ranks,
        "overlap_loss": sum_of_component_ranks - rank,
    }


def intersection_entry(n: int, m: int, s: int) -> dict[str, int]:
    """Intersection of s distinct omitted-column cofactor derivative spaces."""
    return {
        "number_of_cofactors": s,
        "intersection_dimension": choose(n - 1, m) * choose(n - s, m),
    }


def cofactor_basis(n: int, m: int, omitted_column: int) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    """Explicit subpermanent basis of one last-row cofactor derivative space."""
    rows = combinations(range(n - 1), m)
    columns = tuple(j for j in range(n) if j != omitted_column)
    return {
        (row_set, column_set)
        for row_set in rows
        for column_set in combinations(columns, m)
    }


def build_payload() -> dict[str, object]:
    small_n = []
    preceding_row_max = None
    for n in range(3, 7):
        rows = [row_slice_entry(n, m) for m in range(n)]
        row_max = max(row["rank_ratio"] for row in rows)
        mixed_ceiling = max(choose(n, m) for m in range(n + 1))
        recurrence = None
        if preceding_row_max is not None:
            recurrence = {
                "twice_previous": 2 * preceding_row_max,
                "holds": row_max >= 2 * preceding_row_max,
            }
        small_n.append(
            {
                "n": n,
                "target_two_to_n_minus_1": 2 ** (n - 1),
                "large_splitting_mixed_ceiling": mixed_ceiling,
                "row_slice_max_ratio": row_max,
                "row_slice_doubling_from_previous_n": recurrence,
                "degrees": rows,
                "central_intersections": [
                    intersection_entry(n, n // 2, s) for s in range(1, n + 1)
                ],
            }
        )
        preceding_row_max = row_max

    # Include n=2 only as the base value for the first displayed recurrence.
    n2_max = max(choose(1, m) for m in range(2))
    small_n[0]["row_slice_doubling_from_previous_n"] = {
        "twice_previous": 2 * n2_max,
        "holds": small_n[0]["row_slice_max_ratio"] >= 2 * n2_max,
    }

    return {
        "status": "PURE_ROUTE_BARRIER_EXACT_INTEGER_REPLAY",
        "identifier": "G-038",
        "theorems": {
            "uniform_one_term_cap": "rank M_(U,W)^(q,m)(T) <= binom(n,m)",
            "sharpness_condition": "dim(U)>=n and dim(W)>=n",
            "permanent_large_splitting_ceiling": "rank/cap <= binom(n,m)",
            "last_row_exact_rank": "binom(n-1,m)*binom(n,m)",
            "last_row_exact_ratio": "binom(n-1,m)",
            "s_cofactor_intersection": "binom(n-1,m)*binom(n-s,m)",
        },
        "small_n": small_n,
        "boundary": (
            "This closes only mixed-derivative flattenings obtained from a fixed "
            "linear splitting V=U direct-sum W.  It is not a Chow-rank upper "
            "bound and does not exclude nonlinear, quotient, or coupled "
            "common-domain invariants."
        ),
    }


def validate(payload: dict[str, object]) -> None:
    expected_row = {3: 2, 4: 3, 5: 6, 6: 10}
    expected_mixed = {3: 3, 4: 6, 5: 10, 6: 20}
    for item in payload["small_n"]:
        n = item["n"]
        assert item["row_slice_max_ratio"] == expected_row[n]
        assert item["large_splitting_mixed_ceiling"] == expected_mixed[n]
        assert item["large_splitting_mixed_ceiling"] < item["target_two_to_n_minus_1"]
        for row in item["degrees"]:
            assert row["permanent_rank"] == row["rank_ratio"] * row["one_term_cap"]
            assert row["overlap_loss"] >= 0
            m = row["m"]
            bases = [cofactor_basis(n, m, j) for j in range(n)]
            assert len(set().union(*bases)) == row["permanent_rank"]
            for s in range(1, n + 1):
                common = set.intersection(*bases[:s])
                assert len(common) == choose(n - 1, m) * choose(n - s, m)

    doubling = {
        item["n"]: item["row_slice_doubling_from_previous_n"]["holds"]
        for item in payload["small_n"]
    }
    assert doubling == {3: True, 4: False, 5: True, 6: False}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    validate(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
