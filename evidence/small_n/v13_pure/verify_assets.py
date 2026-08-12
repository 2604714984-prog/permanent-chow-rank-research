#!/usr/bin/env python3
"""Verify the immutable v13 PDF and reviewer ZIP with the standard library."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
if payload.get("format") != "perm345-v13-release-assets-v1":
    raise SystemExit("FAIL: unexpected manifest format")

for artifact in payload["artifacts"]:
    path = ROOT / artifact["file"]
    if not path.is_file():
        raise SystemExit(f"FAIL: missing {path.name}")
    if path.stat().st_size != artifact["bytes"]:
        raise SystemExit(f"FAIL: byte count mismatch for {path.name}")
    if sha256(path) != artifact["sha256"]:
        raise SystemExit(f"FAIL: SHA-256 mismatch for {path.name}")

zip_path = ROOT / "perm345_reviewer_submission_v13_pure_20260810.zip"
with ZipFile(zip_path) as archive:
    entries = archive.infolist()
    if len(entries) != payload["zip_entries"]:
        raise SystemExit("FAIL: ZIP entry count mismatch")
    if max(item.file_size for item in entries) >= 100_000_000:
        raise SystemExit("FAIL: unexpectedly large embedded file")
    required = {
        "README_REVIEWER.md",
        "verify_manifest.py",
        "perm345_chow_rank_v13_pure_reviewer_candidate_20260810.pdf",
        "latex/perm345_v13_pure/attachment_manifest.json",
    }
    names = {item.filename.replace("\\", "/") for item in entries}
    missing = sorted(required - names)
    if missing:
        raise SystemExit(f"FAIL: required ZIP entries missing: {missing}")

print("PASS_V13_RELEASE_ASSETS files=2 zip_entries=105")
