#!/usr/bin/env python3
"""Exact zero- and full-increment atoms for all rank-six normal forms."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build(profile_payload: dict) -> dict:
    rows = []
    for normal_form in profile_payload["normal_forms"]:
        support = normal_form["support_size"]
        middle = normal_form["hilbert_profile"][3]
        delta = 35 - middle
        rows.append(
            {
                "support_size": support,
                "middle_dimension": middle,
                "delta": delta,
                "increment_zero_surplus": delta,
                "increment_six_surplus": middle - 25,
            }
        )
    assert [row["increment_zero_surplus"] for row in rows] == [10, 10, 4, 1, 0, 0]
    assert [row["increment_six_surplus"] for row in rows] == [0, 0, 6, 9, 10, 10]
    return {
        "schema_version": 1,
        "claim": (
            "For every rank-six seven-factor normal form, the d=0 surplus is "
            "delta=35-u and the full d=6 surplus is u-25."
        ),
        "proof": (
            "At d=0 both symbols vanish. At the full quotient both symbols are "
            "injective by the lower-50 full-symbol argument, so the surplus is "
            "2u+(35-u)-60=u-25."
        ),
        "claim_boundary": (
            "Intermediate increments d=1,...,5 and their orientation jump loci "
            "are not classified here; this is not the complete R6 surplus atlas."
        ),
        "source": "data/n7_rank6_normal_form_profiles.json",
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/n7_rank6_normal_form_profiles.json"),
    )
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    payload = build(json.loads(args.source.read_text(encoding="utf-8")))
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    if args.verify_json:
        assert payload == json.loads(args.verify_json.read_text(encoding="utf-8"))
    print(rendered, end="")
    print("N7_LOWER51_RANK6_ENDPOINT_ATOMS_PASS")


if __name__ == "__main__":
    main()
