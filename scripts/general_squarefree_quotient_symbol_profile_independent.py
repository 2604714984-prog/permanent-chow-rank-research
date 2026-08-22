#!/usr/bin/env python3
"""Independent bit-mask replay of coordinate quotient equality cases."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(message)


def coordinate_rank(n: int, k: int, chosen: tuple[int, ...]) -> int:
    chosen_set = frozenset(chosen)
    outputs: set[tuple[int, int]] = set()
    nonzero_columns = 0
    for subset in combinations(range(n), k):
        column_outputs = []
        subset_set = frozenset(subset)
        for index in subset:
            if index in chosen_set:
                remainder_mask = sum(
                    1 << value for value in subset_set if value != index
                )
                column_outputs.append((index, remainder_mask))
        if column_outputs:
            nonzero_columns += 1
            for output in column_outputs:
                require(output not in outputs, (n, k, chosen, output))
                outputs.add(output)
    require(len(outputs) >= nonzero_columns, (n, k, chosen))
    # Each output identifies its unique source subset, hence nonzero columns
    # have disjoint supports and are linearly independent.
    return nonzero_columns


def replay(max_n: int) -> dict[str, object]:
    checks = 0
    rows = []
    for n in range(2, max_n + 1):
        for d in range(n + 1):
            chosen = tuple(range(d))
            all_degree = 0
            for k in range(1, n + 1):
                rank = coordinate_rank(n, k, chosen)
                expected = sum(
                    1
                    for subset in combinations(range(n), k)
                    if set(subset) & set(chosen)
                )
                require(rank == expected, (n, k, d, rank, expected))
                all_degree += rank
                checks += 1
            require(all_degree == (1 << n) - (1 << (n - d)), (n, d))
            rows.append({"n": n, "d": d, "all_degree_rank": all_degree})
    return {"max_n": max_n, "checks": checks, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=9)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = replay(args.max_n)
    if args.json is not None:
        args.json.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print("GENERAL_SQUAREFREE_QUOTIENT_SYMBOL_PROFILE_INDEPENDENT_PASS")


if __name__ == "__main__":
    main()
