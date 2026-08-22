#!/usr/bin/env python3
"""Strict-growth correction for weighted common-graph Packet B."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


POINT_COUNT = 42
TARGET_H5_CEILING = 40
SOURCE_COMMIT = "170bd086a2c836c53160cf6b353e167b1228586c"

EQUALITY_RANK_STRATA = (
    (30, 42),
    (31, 41),
    (32, 40),
    (33, 39),
    (34, 38),
    (35, 37),
    (36, 36),
)
PRE_GROWTH_CANDIDATES = tuple(
    pair for pair in EQUALITY_RANK_STRATA if pair[1] <= TARGET_H5_CEILING
)


def admissible_h5_values(rank_pair: tuple[int, int]) -> tuple[int, ...]:
    """Return H_Z(5) values compatible with reduced-point strict growth."""
    h3, h4 = rank_pair
    if not (0 <= h3 <= h4 <= POINT_COUNT):
        raise ValueError("invalid Hilbert-function pair")
    if h3 == h4 and h4 < POINT_COUNT:
        return ()
    if h4 == POINT_COUNT:
        return (POINT_COUNT,)
    return tuple(range(h4 + 1, TARGET_H5_CEILING + 1))


TARGET_COMPATIBLE_STRATA = tuple(
    pair for pair in PRE_GROWTH_CANDIDATES if admissible_h5_values(pair)
)
TARGET_ADMISSIBLE_H5 = {
    pair: admissible_h5_values(pair) for pair in TARGET_COMPATIBLE_STRATA
}


def build_payload() -> dict[str, object]:
    eliminated = []
    for pair in PRE_GROWTH_CANDIDATES:
        values = admissible_h5_values(pair)
        if values:
            continue
        reason = (
            "H_Z(3)=H_Z(4)<42 is a forbidden plateau for a reduced "
            "length-42 projective scheme."
            if pair[0] == pair[1]
            else
            "Degree-six target containment gives H_Z(5)<=40, while reduced-"
            "point strict growth from H_Z(4)=40 requires H_Z(5)>=41."
        )
        eliminated.append({"stratum": list(pair), "reason": reason})

    remaining = [
        {
            "stratum": list(pair),
            "admissible_h5_values": list(TARGET_ADMISSIBLE_H5[pair]),
            "degree_five_growth": [
                value - pair[1] for value in TARGET_ADMISSIBLE_H5[pair]
            ],
        }
        for pair in TARGET_COMPATIBLE_STRATA
    ]

    return {
        "schema_version": 1,
        "status": "B1_STRICT_GROWTH_CORRECTION",
        "source_commit": SOURCE_COMMIT,
        "point_count": POINT_COUNT,
        "degree_six_target_h5_ceiling": TARGET_H5_CEILING,
        "pre_growth_candidates": [list(pair) for pair in PRE_GROWTH_CANDIDATES],
        "eliminated_strata": eliminated,
        "remaining_target_compatible_strata": remaining,
        "supersedes": [
            "The four-stratum target-compatible classification in "
            "docs/n7_weighted_common_graph_interface.md at the source commit.",
            "The field target_compatible_geometrically_feasible_strata in "
            "data/n7_weighted_common_graph_interface.json at the source commit.",
        ],
        "claim_boundary": [
            "The correction uses only the already proved H_Z(5)<=40 ceiling "
            "and strict growth of the Hilbert function of 42 distinct reduced "
            "projective points until it reaches 42.",
            "The surviving rank pairs are (33,39), (34,38), and (35,37), "
            "refined into six possible H_Z(5) cases.",
            "The curve-union constructions in the earlier checkpoint realize "
            "only the displayed H_Z(3),H_Z(4) profiles; they do not certify "
            "degree-six permanent-target containment.",
            "No weighted common-graph closure, Packet-B closure, lower-50 "
            "theorem, exact-rank-64 theorem, or border-rank conclusion follows.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.verify_json:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if payload != frozen:
            raise SystemExit("weighted common-graph strict-growth JSON mismatch")
        print("PASS weighted common-graph strict-growth correction")
        return
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
