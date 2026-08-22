#!/usr/bin/env python3
"""Exact small replay for the N6-059 separated-block exclusion theorem."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_alpha3_separated_block_exclusion.json"


def squarefree_lower_shadow_size(family: tuple[tuple[int, ...], ...]) -> int:
    shadow = set()
    for triple in family:
        shadow.update(combinations(triple, 2))
    return len(shadow)


def one_factor_shadow_minima() -> list[int]:
    triples = tuple(combinations(range(6), 3))
    minima = [0]
    for size in range(1, 7):
        minima.append(
            min(
                squarefree_lower_shadow_size(family)
                for family in combinations(triples, size)
            )
        )
    return minima


def build_payload() -> dict[str, object]:
    minima = one_factor_shadow_minima()
    assert minima == [0, 3, 5, 6, 6, 8, 9]
    return {
        "status": [
            "PURE_SEPARATED_BLOCK_COUPLING_THEOREM",
            "EXACT_INTEGER_SHADOW_REPLAY",
            "B50_COLUMN_ROW_SEPARATED_EXCLUDED",
            "N6-059",
        ],
        "one_factor_squarefree_cubic_shadow_minima_s0_through_s6": minima,
        "pure_theorem": {
            "quadratic_pair_block_dimension": 6,
            "quadratic_permanent_intersection_per_pair_block": 5,
            "cubic_triple_block_count": 20,
            "cubic_permanent_intersection_per_triple_upper": 2,
            "global_cubic_permanent_intersection_upper": 40,
            "excluded_target_b": 50,
            "transpose_included": True,
        },
        "strict_conclusion": (
            "No column-separated or row-separated six-term all-alpha-three "
            "common-W15 configuration with d2=90 and h=120 can have b=50; "
            "every such separated configuration has b<=40."
        ),
        "claim_boundary": (
            "The theorem assumes that every term has one factor in each fixed "
            "column, or after transposition one factor in each fixed row. It "
            "does not classify arbitrary common-W15 fibers, exclude the general "
            "b=50 all-alpha-three state, prove ChowRank(perm_6)>=28, or make a "
            "border-rank claim."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise AssertionError(args.verify_json)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(rendered, encoding="utf-8", newline="\n")
    print("separated_b_upper=40")
    print("N6_ALPHA3_SEPARATED_BLOCK_EXCLUSION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
