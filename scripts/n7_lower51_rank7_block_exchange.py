#!/usr/bin/env python3
"""Exact finite exchange table for rank-seven direct-basis blocks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SURPLUS = (0, 22, 29, 26, 17, 14, 7, 0)
BUDGET = 35


def single_exchange_cost(rank: int) -> int:
    return SURPLUS[rank] + SURPLUS[7 - rank]


def completion_cost(combined_rank: int, last_rank: int) -> int:
    increments = (
        combined_rank,
        7 - combined_rank + last_rank,
        7 - last_rank,
    )
    assert sum(increments) == 14
    return sum(SURPLUS[increment] for increment in increments)


def build() -> dict:
    single_rows = [
        {
            "block_rank": rank,
            "complement_rank": 7 - rank,
            "exchange_cost": single_exchange_cost(rank),
            "allowed": single_exchange_cost(rank) <= BUDGET,
        }
        for rank in range(8)
    ]
    assert [row["block_rank"] for row in single_rows if row["allowed"]] == [0, 1, 6, 7]

    pair_rows = []
    for first_rank in range(8):
        for second_rank in range(first_rank, 8):
            for combined_rank in range(
                max(first_rank, second_rank),
                min(7, first_rank + second_rank) + 1,
            ):
                first_last_cost = completion_cost(combined_rank, first_rank)
                second_last_cost = completion_cost(combined_rank, second_rank)
                if max(first_last_cost, second_last_cost) > BUDGET:
                    continue
                pair_rows.append(
                    {
                        "block_ranks": [first_rank, second_rank],
                        "combined_rank": combined_rank,
                        "completion_costs": [first_last_cost, second_last_cost],
                    }
                )

    expected = [
        (0, 0, 0), (0, 1, 1), (0, 6, 6), (0, 7, 7),
        (1, 1, 1), (1, 6, 7), (1, 7, 7),
        (6, 6, 6), (6, 6, 7), (6, 7, 7), (7, 7, 7),
    ]
    assert [(*row["block_ranks"], row["combined_rank"]) for row in pair_rows] == expected
    return {
        "schema_version": 1,
        "budget": BUDGET,
        "surplus_by_increment_0_through_7": list(SURPLUS),
        "claim": (
            "Every rank-seven nonbasis restriction block has rank 0,1,6,or 7. "
            "The table gives every pair-rank/combined-rank state surviving both "
            "basis-completion orders under budget 35."
        ),
        "claim_boundary": (
            "This is a necessary projection-rank classification. It does not "
            "construct compatible factor planes or close the partial-block branch."
        ),
        "single_exchange_rows": single_rows,
        "pair_exchange_rows": pair_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    print(rendered, end="")
    print("N7_LOWER51_RANK7_BLOCK_EXCHANGE_PASS")


if __name__ == "__main__":
    main()
