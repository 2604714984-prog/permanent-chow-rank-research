#!/usr/bin/env python3
"""Fail-closed theorem-facing contract for the integrated lower-50 proof."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "docs" / "n7_ordinary_chow_rank_lower50.md"


REQUIRED_MARKERS = (
    "For \\(d=3,4\\), correctly graded Gorenstein duality",
    "E_2^{(1)}=E_3,\\qquad E_3^{(1)}=E_4",
    "symbol ranks are lower bounds for the original symbols",
    "W=\\sum_{c=1}^7\\operatorname{im}P_{tc}=\\operatorname{im}N_t^*",
    "its square is \\(2abxy\\)",
    "a rank-five full quotient with \\(u=15\\)",
    "scripts/n7_lower50_section_caps_audit.py",
    "scripts/n7_rank6_normal_form_profiles.py",
    "scripts/n7_slope10_coordinate_symbol_table.py",
)

FORBIDDEN_MARKERS = (
    "quadratic restriction is onto",
    "symbol ranks are upper bounds for the original symbols",
    "W=\\ker N_t",
)


def audit_text(text: str) -> None:
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    forbidden = [marker for marker in FORBIDDEN_MARKERS if marker in text]
    if missing or forbidden:
        raise ValueError({"missing": missing, "forbidden": forbidden})


def audit_payloads() -> None:
    section = json.loads(
        (ROOT / "data" / "n7_lower50_section_caps_audit.json").read_text(
            encoding="utf-8"
        )
    )
    profiles = json.loads(
        (ROOT / "data" / "n7_rank6_normal_form_profiles.json").read_text(
            encoding="utf-8"
        )
    )
    slope = json.loads(
        (ROOT / "data" / "n7_slope10_coordinate_symbol_table.json").read_text(
            encoding="utf-8"
        )
    )
    boolean = json.loads(
        (ROOT / "data" / "n7_lower50_boolean_controls.json").read_text(
            encoding="utf-8"
        )
    )
    assert section["recursive_cap_spot_checks"]["C6_47"] == 37
    assert section["recursive_cap_spot_checks"]["C6_48"] == 44
    assert [row["hilbert_profile"][3] for row in profiles["normal_forms"]] == [
        25,
        25,
        31,
        34,
        35,
        35,
    ]
    assert slope["rank_six"]["minimum_combined_rank_by_quotient_rank"] == [
        0,
        22,
        33,
        37,
        41,
        44,
        48,
    ]
    assert boolean["five_planes_checked"] == 2_667
    assert boolean["minimum_rank_W_times_A3"] == 35


def main() -> None:
    audit_text(PROOF.read_text(encoding="utf-8"))
    audit_payloads()
    print("LOWER50_PROOF_CONTRACT_PASS")


if __name__ == "__main__":
    main()
