#!/usr/bin/env python3
"""Enumerate the H-03 numerical multiplication-rank envelopes."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path


def macaulay_successor(value: int, degree: int) -> int:
    """Return the exact degree-``degree`` Macaulay successor."""
    if value < 0 or degree < 1:
        raise ValueError("invalid Macaulay arguments")
    if value == 0:
        return 0
    remainder = value
    top_limit = value + degree + 1
    result = 0
    for lower in range(degree, 0, -1):
        top = lower
        while top + 1 < top_limit and comb(top + 1, lower) <= remainder:
            top += 1
        if comb(top, lower) <= remainder:
            remainder -= comb(top, lower)
            result += comb(top + 1, lower + 1)
            top_limit = top
    if remainder != 0:
        raise AssertionError("incomplete Macaulay expansion")
    return result


def rank_interval(h_source: int, h_target: int, degree: int) -> tuple[int, int]:
    ambient_target = comb(degree + 7, 6)
    ideal_target = ambient_target - h_target
    lower = ambient_target - macaulay_successor(h_source, degree)
    return lower, ideal_target


def build_payload(signature_path: Path) -> dict[str, object]:
    source = json.loads(signature_path.read_text(encoding="utf-8"))
    rows = []
    compressed_count = 0
    expanded_count = 0
    for signature in source["signatures"]:
        h4, h5 = signature["hilbert_3_4_5"][1:]
        h6 = 42 - signature["q3_q4_q5_q6"][3]
        ideal_dimensions = [comb(10, 6) - h4, comb(11, 6) - h5, comb(12, 6) - h6]
        if ideal_dimensions != signature["ideal_dimensions_4_5_6"]:
            raise AssertionError("H-02 ideal dimensions disagree with the Hilbert values")
        r45 = rank_interval(h4, h5, 4)
        r56 = rank_interval(h5, h6, 5)
        pair_count = (r45[1] - r45[0] + 1) * (r56[1] - r56[0] + 1)
        sequence_count = int(signature["sequence_count"])
        compressed_count += pair_count
        expanded_count += pair_count * sequence_count
        rows.append(
            {
                "frontier": signature["frontier"],
                "strict_growth_tail_type": signature["strict_growth_tail_type"],
                "hilbert_4_5_6": [h4, h5, h6],
                "ideal_dimensions_4_5_6": ideal_dimensions,
                "rank_I4_times_S1_interval": list(r45),
                "minimal_generators_degree5_interval": [0, r45[1] - r45[0]],
                "rank_I5_times_S1_interval": list(r56),
                "minimal_generators_degree6_interval": [0, r56[1] - r56[0]],
                "cartesian_envelope_candidate_count": pair_count,
                "formal_sequence_count": sequence_count,
                "expanded_rank_pair_count": pair_count * sequence_count,
            }
        )
    return {
        "schema_version": 1,
        "status": "H-03-NUMERICAL-MULTIPLICATION-RANK-ENVELOPES",
        "signature_count": len(rows),
        "compressed_cartesian_envelope_candidate_count": compressed_count,
        "expanded_cartesian_envelope_candidate_count": expanded_count,
        "rows": rows,
        "claim_boundary": [
            "The intervals are necessary numerical envelopes from Macaulay growth and ideal dimensions.",
            "No row asserts realizability by a saturated reduced point ideal or compatibility with the permanent target.",
            "Because S1 I4 is contained in I5, the degree-six image S2 I4 plus S1 I5 equals S1 I5.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--signatures",
        type=Path,
        default=root / "data" / "n7_lower50_hilbert_signatures.json",
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(args.signatures), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("H03_MULTIPLICATION_ENVELOPE_FROZEN_REPLAY_FAIL")
            return 1
        print("H03_MULTIPLICATION_ENVELOPE_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
