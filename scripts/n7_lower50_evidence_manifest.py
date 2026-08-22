#!/usr/bin/env python3
"""Generate the compact immutable evidence manifest for the v6 proof."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATHS = (
    "docs/n7_ordinary_chow_rank_lower50.md",
    "docs/n7_lower50_v6_wave0_audit.md",
    "docs/n7_lower50_v6_core_audit.md",
    "docs/n7_lower50_v6_integration_audit.md",
    "scripts/n7_lower50_section_caps_audit.py",
    "data/n7_lower50_section_caps_audit.json",
    "scripts/n7_rank6_normal_form_profiles.py",
    "scripts/n7_rank6_normal_form_profiles_independent.py",
    "data/n7_rank6_normal_form_profiles.json",
    "scripts/n7_slope10_coordinate_symbol_table.py",
    "scripts/n7_slope10_coordinate_symbol_table_independent.py",
    "data/n7_slope10_coordinate_symbol_table.json",
    "scripts/n7_lower50_boolean_controls.py",
    "data/n7_lower50_boolean_controls.json",
    "scripts/n7_lower50_proof_contract.py",
    "scripts/rethlas_perm7_20260822/slope10_adversarial_modular.py",
    "tests/test_n7_lower50_section_caps_audit.py",
    "tests/test_n7_lower50_slope_replays.py",
    "tests/test_n7_lower50_boolean_controls.py",
    "tests/test_n7_lower50_proof_contract.py",
)


def sha256(path: Path) -> str:
    # Git stores these proof assets as text.  Normalize checkout-specific line
    # endings so one committed blob has the same receipt on Windows and Linux.
    payload = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(payload).hexdigest()


def build_manifest() -> dict[str, object]:
    files = []
    for relative in PATHS:
        path = ROOT / relative
        files.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return {
        "schema_version": 1,
        "hash_mode": "sha256 after CRLF-to-LF text normalization",
        "claim": "ChowRank(perm_7) >= 50",
        "scope": {
            "rank": "ordinary Chow rank",
            "field": "algebraically closed characteristic zero",
            "border_rank_claim": False,
        },
        "candidate_source": {
            "commit": "107912a550cc4688b160e69008e7f7bb33650447",
            "tree": "14495e67b2c77046dedb25a7228c68c433c3e99f",
            "proof_blob": "2e322ccc6b823721244962844e43a0815c804402",
            "merge_base": "111a022c8de36619c32a0c2cf660aa4dd5b5aeab",
        },
        "external_sources": [
            {
                "id": "Bukh-MDKK-1009.2375v2",
                "use": "Theorem 1 and compression Lemmas 2-3",
            },
            {
                "id": "Shafiei-Apolarity-1212.0515v2",
                "use": "Theorem 2.13 for the generic permanent apolar ideal",
            },
        ],
        "arithmetic_domains": {
            "section_caps": "exact integers; two DP orientations",
            "rank_six_primary": "exact rational elimination",
            "rank_six_independent": (
                "F_1000003 and F_1000033 lower-bound/equality replays"
            ),
            "slope_primary": "exact coordinate support counting",
            "slope_independent": "independent bit-mask enumeration",
            "arbitrary_quotient_search": "F_1000033 diagnostic only",
            "boolean_control": "exhaustive F_2 falsifier only",
        },
        "replay_commands": [
            "python scripts/n7_lower50_section_caps_audit.py --verify-json data/n7_lower50_section_caps_audit.json",
            "python scripts/n7_rank6_normal_form_profiles.py --verify-json data/n7_rank6_normal_form_profiles.json",
            "python scripts/n7_rank6_normal_form_profiles_independent.py",
            "python scripts/n7_slope10_coordinate_symbol_table.py --verify-json data/n7_slope10_coordinate_symbol_table.json",
            "python scripts/n7_slope10_coordinate_symbol_table_independent.py",
            "python scripts/n7_lower50_boolean_controls.py --verify-json data/n7_lower50_boolean_controls.json",
            "python scripts/n7_lower50_proof_contract.py",
            "python scripts/rethlas_perm7_20260822/slope10_adversarial_modular.py",
        ],
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    args = parser.parse_args()
    manifest = build_manifest()
    if args.json is not None:
        args.json.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.verify_json is not None:
        frozen = json.loads(args.verify_json.read_text(encoding="utf-8"))
        if manifest != frozen:
            raise SystemExit("lower-50 evidence manifest mismatch")
        print("LOWER50_EVIDENCE_MANIFEST_PASS")
    if args.json is None and args.verify_json is None:
        print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
