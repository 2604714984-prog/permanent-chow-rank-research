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
PENDING = {
    family: f"data/n7_mixed_glynn_overlap_two_{family}_nilpotent_shear_tail_rank.json"
    for family in ("24", "25", "33", "42")
}


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
    pending_rows = []
    for family, source_path in PENDING.items():
        count = multi_minor_count(source_path)
        source = json.loads((ROOT / source_path).read_text(encoding="utf-8"))
        missing_determinants = all(
            "determinant_factorization" not in minor
            for row in source["rows"]
            if row["minor_count"] > 1
            for minor in row["minors"]
        )
        if not missing_determinants:
            raise AssertionError(f"unexpected saved determinant for {family}")
        pending_rows.append(
            {
                "family": family,
                "source_certificate": source_path,
                "multi_minor_row_count": count,
                "next_required_evidence": (
                    "reconstruct exact minors and prove Laurent-torus ideal "
                    "emptiness by dimension reduction or saturation"
                ),
                "status": "PENDING_TORUS_IDEAL_AUDIT",
            }
        )
    audited_count = sum(row["multi_minor_row_count"] for row in audited_rows)
    pending_count = sum(row["multi_minor_row_count"] for row in pending_rows)
    if (audited_count, pending_count) != (386, 803):
        raise AssertionError("lower-overlap audit inventory drift")
    return {
        "schema_version": 1,
        "status": "PARTIAL_LOWER_OVERLAP_TORUS_IDEAL_AUDIT_386_OF_1189",
        "multi_minor_row_count": audited_count + pending_count,
        "audited_multi_minor_row_count": audited_count,
        "pending_multi_minor_row_count": pending_count,
        "audited_families": audited_rows,
        "pending_families": pending_rows,
        "claim_boundary": [
            "The audited rows have exact Laurent-torus Bezout certificates, not merely multivariate gcd evidence.",
            "The 803 pending rows prevent a full recursive overlap-two or higher-overlap boundary theorem.",
            "Single-minor dense-chart certificates are not downgraded by this audit gate.",
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
