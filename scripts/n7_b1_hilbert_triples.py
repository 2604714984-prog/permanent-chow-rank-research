#!/usr/bin/env python3
"""Enumerate the Macaulay-admissible h-vectors at the perm7 B1 frontier."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path


TRIPLES = (
    ("S1", (33, 39, 40)),
    ("S2", (34, 38, 39)),
    ("S3", (34, 38, 40)),
    ("S4", (35, 37, 38)),
    ("S5", (35, 37, 39)),
    ("S6", (35, 37, 40)),
)
POINT_COUNT = 42


def macaulay_successor(value: int, degree: int) -> int:
    """Return the exact Macaulay successor ``value^{<degree>}``."""
    if value < 0 or degree < 1:
        raise ValueError("invalid Macaulay arguments")
    if value == 0:
        return 0
    remainder = value
    upper = value + degree
    expansion: list[tuple[int, int]] = []
    for lower in range(degree, 0, -1):
        while comb(upper, lower) > remainder:
            upper -= 1
        expansion.append((upper, lower))
        remainder -= comb(upper, lower)
        upper -= 1
    if remainder != 0:
        raise AssertionError("incomplete Macaulay expansion")
    return sum(comb(upper + 1, lower + 1) for upper, lower in expansion)


def positive_tails(previous: int, degree: int, remaining: int) -> list[tuple[int, ...]]:
    """Enumerate positive continuations until the total point count is reached."""
    if remaining == 0:
        return [()]
    bound = min(remaining, macaulay_successor(previous, degree))
    tails: list[tuple[int, ...]] = []
    for value in range(1, bound + 1):
        for tail in positive_tails(value, degree + 1, remaining - value):
            tails.append((value,) + tail)
    return tails


def admissible_h_vectors(triple: tuple[int, int, int]) -> list[tuple[int, ...]]:
    h3_total, h4_total, h5_total = triple
    delta4 = h4_total - h3_total
    delta5 = h5_total - h4_total
    vectors: list[tuple[int, ...]] = []
    # Nondegeneracy in P^6 fixes delta_0=1 and delta_1=6.  Macaulay gives
    # delta_2 <= 6^{<1>}=21, so this loop is the complete bounded prefix scan.
    for delta2 in range(1, macaulay_successor(6, 1) + 1):
        delta3 = h3_total - 7 - delta2
        if delta3 < 1 or delta3 > macaulay_successor(delta2, 2):
            continue
        if delta4 < 1 or delta4 > macaulay_successor(delta3, 3):
            continue
        if delta5 < 1 or delta5 > macaulay_successor(delta4, 4):
            continue
        prefix = (1, 6, delta2, delta3, delta4, delta5)
        remaining = POINT_COUNT - sum(prefix)
        for tail in positive_tails(delta5, 5, remaining):
            vectors.append(prefix + tail)
    return vectors


def build_payload() -> dict[str, object]:
    rows = []
    for label, triple in TRIPLES:
        vectors = admissible_h_vectors(triple)
        rows.append(
            {
                "label": label,
                "hilbert_3_4_5": list(triple),
                "formal_o_sequence_count": len(vectors),
                "status": "FORMAL-O-SEQUENCES" if vectors else "MACAULAY-EXCLUDED",
                "first_differences": [list(vector) for vector in vectors],
            }
        )
    return {
        "schema_version": 1,
        "status": "B1F-01-HILBERT-FIRST-DIFFERENCES",
        "candidate_prefix_count_checked_before_materialization": (
            len(TRIPLES) * macaulay_successor(6, 1)
        ),
        "formal_o_sequence_count": sum(
            int(row["formal_o_sequence_count"]) for row in rows
        ),
        "rows": rows,
        "claim_boundary": [
            "The enumeration is complete for first-difference O-sequences with H0=1, H1=7, the displayed H3/H4/H5 values, total length 42, and positive growth until stabilization.",
            "S6 is impossible already by Macaulay growth because its degree-four and degree-five first differences are 2 and 3.",
            "The surviving formal O-sequences are not asserted to be Hilbert functions of 42 distinct reduced graph points.",
            "No weighted coupling, permanent containment, lower-50 theorem, or border-rank conclusion follows.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("B1F_01_FROZEN_REPLAY_FAIL")
            return 1
        print("B1F_01_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
