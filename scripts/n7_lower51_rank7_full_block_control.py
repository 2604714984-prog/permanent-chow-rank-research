#!/usr/bin/env python3
"""Finite arithmetic controls for the full-block direct-basis reduction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build() -> dict:
    basis_labels = 7
    total_labels = 50
    nonbasis_labels = total_labels - basis_labels
    maximum_parallel_per_basis_plane = 1
    maximum_parallel_nonbasis = basis_labels * maximum_parallel_per_basis_plane
    minimum_nonparallel = nonbasis_labels - maximum_parallel_nonbasis
    assert minimum_nonparallel == 36
    return {
        "schema_version": 1,
        "claim": (
            "The three-label span floor 12 permits at most one nonbasis label "
            "parallel to each of seven basis planes, leaving at least 36 "
            "nonparallel labels."
        ),
        "claim_boundary": (
            "This controls only the counting step in the proof; multiplication "
            "propagation and the centroid obstruction are mathematical lemmas."
        ),
        "basis_labels": basis_labels,
        "nonbasis_labels": nonbasis_labels,
        "three_label_span_floor": 12,
        "common_plane_span": 7,
        "maximum_parallel_nonbasis": maximum_parallel_nonbasis,
        "minimum_nonparallel_nonbasis": minimum_nonparallel,
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
    print("N7_LOWER51_RANK7_FULL_BLOCK_CONTROL_PASS")


if __name__ == "__main__":
    main()
