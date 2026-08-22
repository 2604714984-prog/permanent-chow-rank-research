#!/usr/bin/env python3
"""Audit the projective support closure of overlapping (2,4)/(4,2) updates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


CERTIFICATES = {
    "dense_overlapping_24_42": (
        "n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.json",
        "EXACT_ALL_OVERLAPPING_24_42_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
    ),
    "overlapping_23_32_closure": (
        "n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.json",
        "EXACT_ALL_OVERLAPPING_23_32_PROJECTIVE_SUPPORT_CLOSURE",
    ),
    "overlap_one_23_32_closure": (
        "n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.json",
        "EXACT_ALL_OVERLAP_ONE_23_32_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
    ),
    "singleton_four_closure": (
        "n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.json",
        "EXACT_ALL_SINGLETON_FOUR_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
    ),
    "nilpotent_overlap_two_24": (
        "n7_mixed_glynn_overlap_two_24_nilpotent_shear_tail_rank.json",
        "EXACT_ALL_OVERLAP_TWO_24_NILPOTENT_SHEAR_INVALID_TAIL_MINORS",
    ),
    "nilpotent_overlap_two_42": (
        "n7_mixed_glynn_overlap_two_42_nilpotent_shear_tail_rank.json",
        "EXACT_ALL_OVERLAP_TWO_42_NILPOTENT_SHEAR_INVALID_TAIL_MINORS",
    ),
    "lower_overlap_torus_audit": (
        "n7_mixed_glynn_lower_overlap_torus_audit_status.json",
        "EXACT_ALL_1189_LOWER_OVERLAP_TORUS_IDEALS_AUDITED",
    ),
}


FACE_MAP = {
    "extra_right": {
        "homogeneous_coordinates": (
            "u=x*e_a+y*e_b; "
            "v=p*e_a^*+q*e_b^*+h*e_c^*+k*e_d^* for distinct a,b,c,d"
        ),
        "x=0": "singleton_four_closure",
        "y=0": "singleton_four_closure",
        "p=0": "overlap_one_23_32_closure",
        "q=0": "overlap_one_23_32_closure",
        "h=0": "overlapping_23_32_closure",
        "k=0": "overlapping_23_32_closure",
    },
    "extra_left": {
        "homogeneous_coordinates": (
            "u=x*e_a+y*e_b+z*e_c+g*e_d; "
            "v=p*e_a^*+q*e_b^* for distinct a,b,c,d"
        ),
        "x=0": "overlap_one_23_32_closure",
        "y=0": "overlap_one_23_32_closure",
        "z=0": "overlapping_23_32_closure",
        "g=0": "overlapping_23_32_closure",
        "p=0": "singleton_four_closure",
        "q=0": "singleton_four_closure",
    },
}


def load_exact_certificates():
    loaded = {}
    for label, (filename, expected_status) in CERTIFICATES.items():
        payload = json.loads((DATA / filename).read_text(encoding="utf-8"))
        actual_status = str(payload.get("status"))
        if actual_status != expected_status:
            raise AssertionError(
                f"certificate mismatch for {label}: {actual_status}"
            )
        loaded[label] = payload
    return loaded


def dense_chart_summary(payload):
    rows = payload["rows"]
    if len(rows) != 900:
        raise AssertionError("dense overlapping-(2,4)/(4,2) inventory drift")
    if any(
        row["status"] != "DENSE_INVERTIBLE_CHART_COVERED_BY_EXACT_MINORS"
        for row in rows
    ):
        raise AssertionError("incomplete dense overlapping-(2,4)/(4,2) row")
    direct = sum(row["pivot_face_minor"] is None for row in rows)
    double = sum(row["double_pivot_face_minor"] is not None for row in rows)
    pivot_only = len(rows) - direct - double
    if (direct, pivot_only, double) != (325, 527, 48):
        raise AssertionError("internal-face coverage count drift")
    if any(
        row["double_pivot_face_minor"]
        and row["double_pivot_face_minor"]["unresolved_factors"]
        for row in rows
    ):
        raise AssertionError("unresolved double-pivot face")
    expected_dense_faces = {
        "lower_overlap_torus_audit": CERTIFICATES[
            "lower_overlap_torus_audit"
        ][1],
        "nilpotent_overlap_two_24": CERTIFICATES[
            "nilpotent_overlap_two_24"
        ][1],
        "nilpotent_overlap_two_42": CERTIFICATES[
            "nilpotent_overlap_two_42"
        ][1],
    }
    if payload.get("dense_face_certificates") != expected_dense_faces:
        raise AssertionError("dense nilpotent-face certificate drift")
    return {
        "candidate_count": len(rows),
        "direct_primary_minor_rows": direct,
        "first_internal_face_rows": pivot_only,
        "second_internal_face_rows": double,
        "unresolved_rows": 0,
    }


def build_payload():
    certificates = load_exact_certificates()
    if certificates["singleton_four_closure"].get("candidate_count") != 600:
        raise AssertionError("singleton-four inventory drift")
    if certificates["overlap_one_23_32_closure"].get("candidate_count") != 1800:
        raise AssertionError("overlap-one-(2,3)/(3,2) inventory drift")
    return {
        "schema_version": 1,
        "status": "EXACT_ALL_OVERLAPPING_24_42_PROJECTIVE_SUPPORT_CLOSURE",
        "field": "characteristic zero",
        "certificate_statuses": {
            label: payload["status"]
            for label, payload in certificates.items()
        },
        "dense_chart_summary": dense_chart_summary(
            certificates["dense_overlapping_24_42"]
        ),
        "boundary_face_map": FACE_MAP,
        "face_intersections": (
            "Every nonempty intersection drops to a proper support face of an "
            "imported projective-closure certificate; no new support type occurs."
        ),
        "conclusion": (
            "Every nonidentity invertible rank-one update in the projective "
            "support closure of the overlapping (2,4)/(4,2) patterns has "
            "invalid-tail rank 42 in the synchronized mixed-Glynn "
            "two-transform packet."
        ),
        "claim_boundary": [
            "This is a finite projective support-closure theorem for one identity transform and one rank-one update in the synchronized mixed-Glynn endpoint model.",
            "It combines exact dense, internal-face, nilpotent, Laurent-torus, and proper-support certificates; it introduces no multivariate-gcd inference.",
            "It does not cover larger nonnilpotent supports, higher-rank perturbations, arbitrary GL(6), arbitrary endpoint-B packets, ordinary lower 50, exact rank 64, or border rank.",
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
