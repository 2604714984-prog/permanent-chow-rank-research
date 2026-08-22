#!/usr/bin/env python3
"""Bounded count DP for the rank6/rank7 mixed direct-basis scalar frontier."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from pathlib import Path


MIDDLE = (25, 25, 31, 34, 35, 35)
BASIS_COST = tuple(value - 25 for value in MIDDLE)
ZERO_COST = tuple(35 - value for value in MIDDLE)
BUDGET = 35


def compositions(total: int, length: int, prefix: tuple[int, ...] = ()):
    if length == 1:
        yield (*prefix, total)
        return
    for first in range(total + 1):
        yield from compositions(total - first, length - 1, (*prefix, first))


@lru_cache(maxsize=None)
def count_outside(type_index: int, labels_left: int, budget_left: int) -> int:
    if type_index == 6:
        return 1  # all unused labels are rank seven
    cost = ZERO_COST[type_index]
    maximum = labels_left if cost == 0 else min(labels_left, budget_left // cost)
    return sum(
        count_outside(
            type_index + 1,
            labels_left - count,
            budget_left - count * cost,
        )
        for count in range(maximum + 1)
    )


def coefficient_dp(labels: int, budget: int) -> int:
    # Independent generating-function DP. Rank-seven labels fill unused slots.
    states = {(0, 0): 1}
    for cost in ZERO_COST:
        following = {}
        for (used, spent), ways in states.items():
            maximum = labels - used if cost == 0 else min(labels - used, (budget - spent) // cost)
            for count in range(maximum + 1):
                key = (used + count, spent + count * cost)
                following[key] = following.get(key, 0) + ways
        states = following
    return sum(ways for (used, spent), ways in states.items() if used <= labels and spent <= budget)


def build() -> dict:
    basis_rows = []
    total_patterns = 0
    distribution = {}
    for counts in compositions(7, 6):
        cost = sum(count * atom for count, atom in zip(counts, BASIS_COST))
        if cost > BUDGET:
            continue
        outside_patterns = count_outside(0, 42, BUDGET - cost)
        independent = coefficient_dp(42, BUDGET - cost)
        assert outside_patterns == independent
        basis_rows.append(
            {
                "rank6_support_counts": list(counts),
                "basis_surplus": cost,
                "outside_count_patterns": outside_patterns,
            }
        )
        total_patterns += outside_patterns
        distribution[str(cost)] = distribution.get(str(cost), 0) + outside_patterns

    assert len(basis_rows) == 272
    assert total_patterns == 11_683_105
    return {
        "schema_version": 1,
        "candidate_basis_compositions_before_budget": 792,
        "surviving_basis_compositions": len(basis_rows),
        "compressed_count_patterns": total_patterns,
        "basis_cost_by_support_1_through_6": list(BASIS_COST),
        "outside_zero_increment_cost_by_support_1_through_6": list(ZERO_COST),
        "patterns_by_basis_surplus": distribution,
        "basis_rows": basis_rows,
        "claim": (
            "In the rank6/rank7-only mixed direct-basis lane, the basis has seven "
            "rank-six terms and one rank-seven term. This payload counts every "
            "support-type count vector fitting the 35-unit scalar budget."
        ),
        "claim_boundary": (
            "The count vectors are not represented subspace arrangements or Chow "
            "identities. Partial increments, low-factor-rank terms, and multiplication "
            "compatibility are outside this scalar table."
        ),
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
    print(json.dumps({k: payload[k] for k in (
        "candidate_basis_compositions_before_budget",
        "surviving_basis_compositions",
        "compressed_count_patterns",
        "patterns_by_basis_surplus",
    )}, indent=2, sort_keys=True))
    print("N7_LOWER51_RANK6_MIXED_COUNT_DP_PASS")


if __name__ == "__main__":
    main()
