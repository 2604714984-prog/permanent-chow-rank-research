#!/usr/bin/env python3
"""Finite interfaces for the biflag common-quotient anchor reduction (N6-104)."""

from __future__ import annotations

import argparse
import importlib.util
import json
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "n6_biflag_common_quotient_anchor_reduction.json"
INJECTIVITY_SCRIPT = ROOT / "scripts" / "n6_alpha3_coordinate_quotient_injectivity.py"


def module_from_path(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def row_signatures() -> list[tuple[int, int, int]]:
    rows = []
    for zero in range(2):
        for short in range(3 - zero):
            high = 6 - zero - short
            if high >= 4:
                rows.append((high, short, zero))
    return sorted(rows, reverse=True)


def column_signatures() -> list[tuple[int, int, int]]:
    rows = []
    for zero in range(2):
        for wing in range(4 - zero):
            high = 6 - zero - wing
            if high >= 3:
                rows.append((high, wing, zero))
    return sorted(rows, reverse=True)


def permutation_matching_signatures() -> tuple[int, int]:
    injectivity = module_from_path("n6_coordinate_injectivity", INJECTIVITY_SCRIPT)
    signatures = set()
    count = 0
    for permutation in permutations(range(6)):
        support = tuple(sorted(6 * row + permutation[row] for row in range(6)))
        assert injectivity.is_rectangle_free(support)
        signatures.add(injectivity.signature(support))
        count += 1
    return count, len(signatures)


def build_payload() -> dict[str, object]:
    rows = row_signatures()
    columns = column_signatures()
    matching_count, distinct_signatures = permutation_matching_signatures()
    assert rows == [(6, 0, 0), (5, 1, 0), (5, 0, 1), (4, 2, 0), (4, 1, 1)]
    assert columns == [
        (6, 0, 0),
        (5, 1, 0),
        (5, 0, 1),
        (4, 2, 0),
        (4, 1, 1),
        (3, 3, 0),
        (3, 2, 1),
    ]
    assert (matching_count, distinct_signatures) == (720, 720)
    return {
        "status": [
            "PURE_BIFLAG_COMMON_QUOTIENT_ANCHOR_REDUCTION",
            "EXACT_COORDINATE_MATCHING_REPLAY",
            "N6-104",
        ],
        "biflag": {
            "shape": "R4 tensor C5 + R5 tensor C3",
            "flags": "R4 subset R5 and C3 subset C5",
            "row_contraction_dimensions": [5, 3, 0],
            "column_contraction_dimensions": [5, 4, 0],
        },
        "coordinate_contraction_signatures": {
            "row_high_short_zero": [list(row) for row in rows],
            "column_high_wing_zero": [list(row) for row in columns],
        },
        "block_dichotomy": (
            "At every nonzero coordinate contraction N of dimension d>=2, either all "
            "colors have rank d with common image N, or all blocks have rank at most "
            "one, zero quadratic compression, coordinate domain covectors, and image "
            "lines spanning N."
        ),
        "all_rank_one_branch": {
            "permutation_matching_support_count": matching_count,
            "distinct_quotient_signature_count": distinct_signatures,
            "excluded": True,
            "reason": (
                "Injectivity forces all six row labels and all six column labels to be "
                "permutations, so every frame is a coordinate matching. Coordinate "
                "quotient injectivity then makes all common-W frames identical."
            ),
        },
        "surviving_anchor_ranks": {
            "row": [3, 5],
            "column": [4, 5],
            "four_combinations": [[3, 4], [3, 5], [5, 4], [5, 5]],
        },
        "claim_boundary": (
            "This is a strict normal-form reduction for the N6-103 biflag survivor. "
            "It does not exclude the four anchor combinations, the biflag branch, "
            "ordinary lower 29, exact rank 32, or border rank."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen JSON does not match exact replay")
    if args.json:
        args.json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
