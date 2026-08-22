#!/usr/bin/env python3
"""Build the bounded v7 subset-floor table from the frozen section caps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TARGET_DIMENSIONS = {4: 1225, 5: 441, 6: 49}


def build(cap_payload: dict) -> dict:
    caps = {
        int(degree): values
        for degree, values in cap_payload["full_section_cap_table"].items()
    }
    assert all(len(caps[degree]) == 50 for degree in TARGET_DIMENSIONS)

    rows = []
    for retained in range(1, 51):
        complement = 50 - retained
        floors = {
            degree: TARGET_DIMENSIONS[degree] - caps[degree][complement]
            for degree in TARGET_DIMENSIONS
        }
        rows.append(
            {
                "retained_terms": retained,
                "complement_terms": complement,
                "degree4_derivative_floor": floors[4],
                "degree5_derivative_floor": floors[5],
                "factor_span_floor_from_degree6": floors[6],
            }
        )

    for key in (
        "degree4_derivative_floor",
        "degree5_derivative_floor",
        "factor_span_floor_from_degree6",
    ):
        values = [row[key] for row in rows]
        assert values == sorted(values)

    return {
        "schema_version": 1,
        "claim": (
            "For a hypothetical minimal 50-term identity, every retained "
            "k-subpacket has degree-d derivative-space sum dimension at least "
            "dim(E_d)-C_d(50-k), for d=4,5,6; the d=6 row is its factor-span floor."
        ),
        "claim_boundary": (
            "These are necessary subpacket floors. They do not assert that every "
            "integer rank function is representable or Chow-realizable, and they "
            "do not prove lower 51."
        ),
        "source": "data/n7_lower50_section_caps_audit.json",
        "candidate_rows": 50,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/n7_lower50_section_caps_audit.json"),
    )
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()

    payload = build(json.loads(args.source.read_text(encoding="utf-8")))
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        expected = json.loads(args.verify_json.read_text(encoding="utf-8"))
        assert payload == expected

    rows = payload["rows"]
    controls = {
        retained: rows[retained - 1]
        for retained in (1, 2, 3, 4, 10, 20, 30, 40, 50)
    }
    print(json.dumps(controls, indent=2, sort_keys=True))
    print("N7_LOWER51_SUBSET_FLOORS_PASS")


if __name__ == "__main__":
    main()
