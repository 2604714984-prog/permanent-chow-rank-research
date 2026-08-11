#!/usr/bin/env python3
"""Fail-closed verifier for the v14 PDF and reviewer package."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.json"


def fail(message: str) -> None:
    raise SystemExit("V14_ASSET_VERIFY_FAIL: " + message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()

    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if payload.get("format") != "perm345-v14-repaired-release-assets-v1":
        fail("unexpected manifest format")
    for artifact in payload.get("artifacts", []):
        path = ROOT / artifact["file"]
        if not path.is_file():
            fail(f"missing {path.name}")
        if path.stat().st_size != artifact["bytes"]:
            fail(f"byte count mismatch for {path.name}")
        if sha256(path) != artifact["sha256"]:
            fail(f"SHA-256 mismatch for {path.name}")

    zip_path = ROOT / "perm345_reviewer_submission_v14_repaired_20260812.zip"
    with ZipFile(zip_path) as archive:
        entries = archive.infolist()
        if len(entries) != payload.get("zip_entries"):
            fail("ZIP entry count mismatch")
        names = set()
        for entry in entries:
            name = entry.filename.replace("\\", "/")
            parts = Path(name).parts
            if not name or name.startswith("/") or ".." in parts:
                fail(f"unsafe ZIP member {name!r}")
            if name in names:
                fail(f"duplicate ZIP member {name}")
            names.add(name)
            if entry.file_size >= 100_000_000:
                fail(f"unexpectedly large ZIP member {name}")
        required = {
            "PACKAGE_MANIFEST.json",
            "REVIEWER_README.md",
            "verify_manifest.py",
            "replay_active_proof.py",
            "perm5_one_intersection_flag_standalone_exact.py",
            "n5_one_intersection_flag_standalone_exact.json",
            "latex/perm345_v14_repaired/n5_body.tex",
            "latex/perm345_v14_repaired/formal_computation_spec.tex",
        }
        missing = required - names
        if missing:
            fail(f"required ZIP entries missing: {sorted(missing)}")
        with tempfile.TemporaryDirectory(prefix="perm345_v14_asset_verify_") as temporary:
            extracted = Path(temporary)
            archive.extractall(extracted)
            subprocess.run(
                [sys.executable, "verify_manifest.py"], cwd=extracted, check=True
            )
            if args.replay:
                subprocess.run(
                    [sys.executable, "replay_active_proof.py"],
                    cwd=extracted,
                    check=True,
                )

    print(
        "PASS_V14_REPAIRED_RELEASE_ASSETS "
        f"files=2 zip_entries={payload['zip_entries']} replay={args.replay}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
