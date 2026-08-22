#!/usr/bin/env python3
"""Build the reversible H-02 signatures from the frozen B1 O-sequences."""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path


LABELS = {"S1": "F1", "S2": "F2", "S3": "F3", "S4": "F4", "S5": "F5"}


def cumulative(vector: tuple[int, ...]) -> tuple[int, ...]:
    total = 0
    answer = []
    for value in vector:
        total += value
        answer.append(total)
    return tuple(answer)


def group_signatures(frozen_path: Path) -> list[dict[str, object]]:
    payload = json.loads(frozen_path.read_text(encoding="utf-8"))
    groups: dict[tuple[str, tuple[int, ...]], list[tuple[int, ...]]] = {}
    for row in payload["rows"]:
        if row["label"] not in LABELS:
            continue
        for raw in row["first_differences"]:
            vector = tuple(int(value) for value in raw)
            groups.setdefault((LABELS[row["label"]], vector[6:]), []).append(vector)

    answer = []
    for (label, tail), vectors in sorted(groups.items()):
        vectors.sort()
        first = vectors[0]
        hilbert = cumulative(first)
        delta2_values = sorted({vector[2] for vector in vectors})
        if delta2_values != list(range(10, 22)):
            raise AssertionError((label, tail, delta2_values))
        if any(vector[3] + vector[2] != first[2] + first[3] for vector in vectors):
            raise AssertionError("signature is not reversible by delta2")
        h3, h4, h5, h6 = hilbert[3], hilbert[4], hilbert[5], hilbert[6]
        answer.append(
            {
                "frontier": label,
                "sequence_count": len(vectors),
                "delta2_values": delta2_values,
                "delta3_plus_delta2": first[2] + first[3],
                "fixed_delta4_delta5": [first[4], first[5]],
                "tail_after_degree5": list(tail),
                "hilbert_3_4_5": [h3, h4, h5],
                "hilbert_6_to_stabilization": list(hilbert[6:]),
                "q3_q4_q5_q6": [42 - h3, 42 - h4, 42 - h5, 42 - h6],
                "ideal_dimensions_4_5_6": [
                    comb(10, 6) - h4,
                    comb(11, 6) - h5,
                    comb(12, 6) - h6,
                ],
                "strict_growth_tail_type": "-".join(str(value) for value in tail),
            }
        )
    return answer


def reconstruct(signatures: list[dict[str, object]]) -> set[tuple[int, ...]]:
    vectors: set[tuple[int, ...]] = set()
    for row in signatures:
        delta4, delta5 = row["fixed_delta4_delta5"]
        for delta2 in row["delta2_values"]:
            vectors.add(
                (
                    1,
                    6,
                    delta2,
                    row["delta3_plus_delta2"] - delta2,
                    delta4,
                    delta5,
                    *row["tail_after_degree5"],
                )
            )
    return vectors


def frozen_vectors(frozen_path: Path) -> set[tuple[int, ...]]:
    payload = json.loads(frozen_path.read_text(encoding="utf-8"))
    return {
        tuple(vector)
        for row in payload["rows"]
        if row["label"] in LABELS
        for vector in row["first_differences"]
    }


def build_payload(frozen_path: Path) -> dict[str, object]:
    signatures = group_signatures(frozen_path)
    input_vectors = frozen_vectors(frozen_path)
    raw_payload = json.loads(frozen_path.read_text(encoding="utf-8"))
    raw_count = sum(
        len(row["first_differences"])
        for row in raw_payload["rows"]
        if row["label"] in LABELS
    )
    if raw_count != len(input_vectors):
        raise AssertionError("the frozen input contains duplicate sequences")
    if reconstruct(signatures) != input_vectors:
        raise AssertionError("compressed signatures are not reversible")
    return {
        "schema_version": 1,
        "status": "H-02-REVERSIBLE-HILBERT-SIGNATURES",
        "input_formal_sequence_count": raw_count,
        "signature_count": len(signatures),
        "reconstructed_sequence_count": len(reconstruct(signatures)),
        "signatures": signatures,
        "claim_boundary": [
            "The seven signatures reversibly encode all 84 surviving formal O-sequences.",
            "They are numerical inputs to H-03 and do not assert reduced-point or target-compatible realizability.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--frozen",
        type=Path,
        default=root / "data" / "n7_b1_hilbert_triples.json",
    )
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(args.frozen), indent=2, sort_keys=True) + "\n"
    if args.verify is not None:
        if args.verify.read_text(encoding="utf-8") != text:
            print("H02_SIGNATURE_FROZEN_REPLAY_FAIL")
            return 1
        print("H02_SIGNATURE_FROZEN_REPLAY_PASS")
    if args.json is not None:
        args.json.write_text(text, encoding="utf-8")
    if args.verify is None and args.json is None:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
