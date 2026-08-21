#!/usr/bin/env python3
"""Merge exact perm7 candidate chunks after strict range validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pattern", required=True)
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    paths = sorted(args.root.glob(args.pattern))
    segments = []
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not str(payload.get("status", "")).startswith("EXACT_CHUNK_"):
            continue
        start = int(payload["candidate_start_index"])
        stop = int(payload["candidate_stop_index_exclusive"])
        if stop - start != len(payload["rows"]):
            raise AssertionError(f"row/range mismatch: {path}")
        segments.append((start, stop, path, payload))
    segments.sort(key=lambda item: item[0])
    cursor = 0
    for start, stop, path, _payload in segments:
        if start != cursor:
            raise AssertionError(
                f"candidate range gap or overlap at {cursor}: {path} starts {start}"
            )
        cursor = stop
    if cursor != args.expected_count:
        raise AssertionError(
            f"candidate coverage stops at {cursor}, expected {args.expected_count}"
        )

    base = dict(segments[0][3])
    rows = []
    status_counts = {}
    selection_counts = {}
    elapsed = 0.0
    workers_used = set()
    for _start, _stop, _path, payload in segments:
        weighted = bool(payload.get("weighted_selection", False))
        selection_name = "weighted" if weighted else "lexicographic"
        selection_counts[selection_name] = (
            selection_counts.get(selection_name, 0) + len(payload["rows"])
        )
        for row in payload["rows"]:
            row = dict(row)
            row.setdefault("weighted_selection", weighted)
            rows.append(row)
            status = str(row["status"])
            status_counts[status] = status_counts.get(status, 0) + 1
        elapsed += float(payload["elapsed_seconds"])
        workers_used.add(int(payload["workers"]))

    if status_counts != {
        "DENSE_TORUS_COVERED_BY_EXACT_MINORS": args.expected_count
    }:
        raise AssertionError(f"incomplete exact rows: {status_counts}")
    base.update(
        {
            "status": args.status,
            "candidate_count": args.expected_count,
            "full_candidate_count": args.expected_count,
            "candidate_start_index": 0,
            "candidate_stop_index_exclusive": args.expected_count,
            "chunk_count": len(segments),
            "source_chunk_files": [path.name for _, _, path, _ in segments],
            "selection_strategy_counts": selection_counts,
            "workers_used": sorted(workers_used),
            "status_counts": status_counts,
            "rows": rows,
            "elapsed_seconds_sum": elapsed,
        }
    )
    base.pop("elapsed_seconds", None)
    base.pop("workers", None)
    base.pop("weighted_selection", None)
    args.json.write_text(
        json.dumps(base, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
