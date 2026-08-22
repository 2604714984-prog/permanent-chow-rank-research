#!/usr/bin/env python3
"""Exact dimension enumeration for the no-basis one-six quotient pair."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build() -> dict:
    rows = []
    for second_plane_rank in range(1, 8):
        reversed_increments = [second_plane_rank, 7 - second_plane_rank]
        allowed = sorted(reversed_increments) == [1, 6]
        rows.append(
            {
                "second_plane_quotient_rank": second_plane_rank,
                "reversed_increments": reversed_increments,
                "allowed": allowed,
            }
        )
    assert [row["second_plane_quotient_rank"] for row in rows if row["allowed"]] == [1, 6]
    return {
        "schema_version": 1,
        "ambient_quotient_dimension": 7,
        "fixed_first_plane_rank": 6,
        "positive_increment_profile": [1, 6, 7, 7, 7, 7, 7, 7],
        "rows": rows,
        "intrinsic_role_geometry": {"ranks": [6, 1], "intersection_dimension": 0},
        "swapping_role_geometry": {"ranks": [6, 6], "intersection_dimension": 5},
        "claim_boundary": (
            "This is a quotient-dimension classification only. Graph maps, "
            "multiplication compatibility, and a permanent identity are not supplied."
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
    print(rendered, end="")
    print("N7_LOWER51_NO_BASIS_TWO_PLANE_PASS")


if __name__ == "__main__":
    main()
