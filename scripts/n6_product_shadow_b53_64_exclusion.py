#!/usr/bin/env python3
"""Exact product-shadow compression certificate for N6-056."""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_product_shadow_b53_64_exclusion.json"
N = 6
TRIPLE_COUNT = 20
QUADRATIC_PROJECTION_CAP = 78


def colex_subsets(size: int) -> list[tuple[int, ...]]:
    """Fixed-size subsets in colex order."""

    return sorted(combinations(range(N), size), key=lambda s: sum(1 << x for x in s))


def one_factor_data() -> tuple[list[int], list[int]]:
    """Return k(m)=|partial(first m triples)| and first-occurrence weights."""

    triples = colex_subsets(3)
    seen: set[tuple[int, int]] = set()
    shadow_sizes = [0]
    first_occurrence_weights: list[int] = []
    for triple in triples:
        pairs = set(combinations(triple, 2))
        new_pairs = pairs - seen
        first_occurrence_weights.append(len(new_pairs))
        seen.update(pairs)
        shadow_sizes.append(len(seen))
    assert len(triples) == TRIPLE_COUNT
    assert len(seen) == 15
    return shadow_sizes, first_occurrence_weights


def ferrers_shadow(partition: tuple[int, ...]) -> int:
    """Product lower-shadow size of the Ferrers diagram with these row lengths."""

    shadow_sizes, weights = one_factor_data()
    assert len(partition) == TRIPLE_COUNT
    assert all(20 >= partition[i] >= partition[i + 1] >= 0 for i in range(19))
    return sum(weights[i] * shadow_sizes[partition[i]] for i in range(20))


def minimum_ferrers_shadow(
    total: int,
) -> tuple[int, int, tuple[int, ...], int]:
    """Memoized exact DP over all partitions in a 20 by 20 box.

    The returned tuple is (minimum, number of minimizing partitions,
    lexicographically first witness under the descending-x traversal).
    """

    shadow_sizes, weights = one_factor_data()
    infinity = 10**9

    @lru_cache(maxsize=None)
    def solve(index: int, previous: int, remaining: int):
        if index == TRIPLE_COUNT:
            return (0, 1, ()) if remaining == 0 else (infinity, 0, ())
        best = infinity
        count = 0
        witness: tuple[int, ...] = ()
        for value in range(min(previous, remaining), -1, -1):
            slots_after = TRIPLE_COUNT - index - 1
            if remaining - value > value * slots_after:
                continue
            tail_value, tail_count, tail = solve(
                index + 1, value, remaining - value
            )
            candidate = weights[index] * shadow_sizes[value] + tail_value
            if candidate < best:
                best = candidate
                count = tail_count
                witness = (value,) + tail
            elif candidate == best:
                count += tail_count
        return best, count, witness

    result = solve(0, TRIPLE_COUNT, total)
    assert result[0] < infinity
    assert sum(result[2]) == total
    assert ferrers_shadow(result[2]) == result[0]
    return result + (solve.cache_info().currsize,)


def build_payload() -> dict[str, object]:
    shadow_sizes, weights = one_factor_data()
    rows = []
    for middle_dimension in range(40, 66):
        minimum, count, witness, state_count = minimum_ferrers_shadow(
            middle_dimension
        )
        rows.append(
            {
                "middle_intersection_dimension_b": middle_dimension,
                "exact_product_shadow_minimum": minimum,
                "minimizing_ferrers_partition_count": count,
                "first_minimizing_partition": list(witness),
                "memoized_dp_state_count": state_count,
                "excluded_by_projection_cap_78": (
                    53 <= middle_dimension <= 64 and minimum > QUADRATIC_PROJECTION_CAP
                ),
            }
        )
    excluded = [
        row["middle_intersection_dimension_b"]
        for row in rows
        if row["excluded_by_projection_cap_78"]
    ]
    return {
        "status": [
            "PURE_PRODUCT_KRUSKAL_KATONA_COMPRESSION",
            "EXACT_INTEGER_DP_REPLAYED",
            "B53_TO_B64_EXCLUDED",
            "N6-056",
        ],
        "arithmetic": "exact integer colex construction and memoized dynamic programming",
        "colex_triples": [list(x) for x in colex_subsets(3)],
        "one_factor_initial_shadow_sizes_k_0_through_20": shadow_sizes,
        "first_occurrence_weight_vector": weights,
        "quadratic_projection_cap": QUADRATIC_PROJECTION_CAP,
        "rows": rows,
        "excluded_middle_dimensions": excluded,
        "b60_summary": {
            "minimum": rows[20]["exact_product_shadow_minimum"],
            "minimizer_count": rows[20]["minimizing_ferrers_partition_count"],
            "first_witness": rows[20]["first_minimizing_partition"],
        },
        "claim_boundary": (
            "The compression theorem and exact DP exclude only the fixed-six "
            "middle-intersection layers b=53,...,64 via shadow dimension greater "
            "than 78. They do not exclude b=45,...,52, prove ChowRank(perm_6)>=27, "
            "classify equality at b=51 or 52, or make a border-rank claim."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    payload = build_payload()
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload["b60_summary"], sort_keys=True))
    print(f"excluded={payload['excluded_middle_dimensions']}")


if __name__ == "__main__":
    main()
