#!/usr/bin/env python3
"""Machine-readable gate for the lower-overlap multiminor torus audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITED = {
    "overlapping_22": (
        "data/n7_mixed_glynn_overlapping_22_nilpotent_shear_tail_rank.json",
        "data/n7_mixed_glynn_overlapping_22_torus_ideal_audit.json",
    ),
    "overlapping_23_32": (
        "data/n7_mixed_glynn_overlapping_23_nilpotent_shear_tail_rank.json",
        "data/n7_mixed_glynn_overlapping_23_torus_ideal_audit.json",
    ),
}
RECONSTRUCTED = {
    family: f"data/n7_mixed_glynn_overlap_two_{family}_nilpotent_shear_tail_rank.json"
    for family in ("24", "25", "33", "42")
}
RECONSTRUCTED_AUDIT = (
    "data/n7_mixed_glynn_overlap_two_pending_torus_ideal_audit.json"
)


def multi_minor_count(relative_path):
    payload = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    return sum(row["minor_count"] > 1 for row in payload["rows"])


def build_payload():
    audited_rows = []
    for family, (source_path, audit_path) in AUDITED.items():
        source_count = multi_minor_count(source_path)
        audit = json.loads((ROOT / audit_path).read_text(encoding="utf-8"))
        if audit["multi_minor_row_count"] != source_count:
            raise AssertionError(f"audit count mismatch for {family}")
        audited_rows.append(
            {
                "family": family,
                "source_certificate": source_path,
                "audit_certificate": audit_path,
                "multi_minor_row_count": source_count,
                "status": "EXACT_TORUS_IDEAL_AUDITED",
            }
        )
    reconstructed_audit = json.loads(
        (ROOT / RECONSTRUCTED_AUDIT).read_text(encoding="utf-8")
    )
    if (
        reconstructed_audit["status"]
        != "EXACT_ALL_803_PENDING_OVERLAP_TWO_TORUS_IDEALS_AUDITED"
    ):
        raise AssertionError("unexpected reconstructed-minor audit status")
    reconstructed_inventory = {
        tuple(row["family"]): row
        for row in reconstructed_audit["source_inventory"]
    }
    for family, source_path in RECONSTRUCTED.items():
        count = multi_minor_count(source_path)
        family_tuple = (int(family[0]), int(family[1]))
        inventory = reconstructed_inventory[family_tuple]
        if inventory["multi_minor_row_count"] != count:
            raise AssertionError(f"reconstructed audit count mismatch for {family}")
        audited_rows.append(
            {
                "family": family,
                "source_certificate": source_path,
                "audit_certificate": RECONSTRUCTED_AUDIT,
                "multi_minor_row_count": count,
                "status": "EXACT_TORUS_IDEAL_AUDITED",
            }
        )
    audited_count = sum(row["multi_minor_row_count"] for row in audited_rows)
    pending_rows = []
    pending_count = 0
    if (audited_count, pending_count) != (1189, 0):
        raise AssertionError("lower-overlap audit inventory drift")
    return {
        "schema_version": 1,
        "status": "EXACT_ALL_1189_LOWER_OVERLAP_TORUS_IDEALS_AUDITED",
        "multi_minor_row_count": audited_count + pending_count,
        "audited_multi_minor_row_count": audited_count,
        "pending_multi_minor_row_count": pending_count,
        "audited_families": audited_rows,
        "pending_families": pending_rows,
        "claim_boundary": [
            "The audited rows have exact Laurent-torus Bezout certificates, not merely multivariate gcd evidence.",
            "All 1,189 formerly multiminor rows are now audited, so the recursive nilpotent rank-one overlap boundary gate is restored.",
            "This does not prove arbitrary non-nilpotent rank-one updates, arbitrary GL(6), ordinary lower 50, exact rank 64, or border rank.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    text = json.dumps(build_payload(), indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
