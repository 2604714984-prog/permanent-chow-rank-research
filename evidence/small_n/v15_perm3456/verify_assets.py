#!/usr/bin/env python3
"""Fail-closed verifier for the v15 PDF and reviewer package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "MANIFEST.json"
PDF_NAME = "perm3456_chow_rank_v15_repaired_zh_ams.pdf"
ZIP_NAME = "perm3456_reviewer_submission_v15_20260822.zip"
EXPECTED_ARTIFACTS = {PDF_NAME, ZIP_NAME}
SHA256_PATTERN = re.compile(r"[0-9A-Fa-f]{64}")


def fail(message: str) -> None:
    raise SystemExit("V15_ASSET_VERIFY_FAIL: " + message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def validate_artifacts(payload: dict[str, object]) -> dict[str, dict[str, object]]:
    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, list) or len(artifacts) != 2:
        fail("manifest must contain exactly two artifacts")
    by_name: dict[str, dict[str, object]] = {}
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            fail("artifact record must be an object")
        if set(artifact) != {"file", "bytes", "sha256"}:
            fail("unexpected artifact schema")
        name = artifact.get("file")
        byte_count = artifact.get("bytes")
        digest = artifact.get("sha256")
        if not isinstance(name, str) or name in by_name:
            fail("invalid or duplicate artifact name")
        if type(byte_count) is not int or byte_count <= 0:
            fail(f"invalid byte count for {name}")
        if not isinstance(digest, str) or SHA256_PATTERN.fullmatch(digest) is None:
            fail(f"invalid SHA-256 for {name}")
        by_name[name] = artifact
    if set(by_name) != EXPECTED_ARTIFACTS:
        fail("artifact name set does not match the release")
    return by_name


def run_inner(script: str, extracted: Path) -> None:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(
        [sys.executable, "-B", script],
        cwd=extracted,
        env=environment,
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()

    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if payload.get("format") != "perm3456-v15-repaired-release-assets-v1":
        fail("unexpected manifest format")
    artifacts = validate_artifacts(payload)
    for name, artifact in artifacts.items():
        path = ROOT / name
        if not path.is_file():
            fail(f"missing {name}")
        if path.stat().st_size != artifact["bytes"] or sha256(path) != artifact["sha256"]:
            fail(f"identity mismatch for {name}")

    expected_entries = payload.get("zip_entries")
    if type(expected_entries) is not int or expected_entries <= 0:
        fail("invalid ZIP entry count")
    with ZipFile(ROOT / ZIP_NAME) as archive:
        entries = archive.infolist()
        if len(entries) != expected_entries:
            fail("ZIP entry count mismatch")
        names: set[str] = set()
        for entry in entries:
            name = entry.filename.replace("\\", "/")
            if not name or name.startswith("/") or ".." in Path(name).parts:
                fail(f"unsafe ZIP member {name!r}")
            if name in names:
                fail(f"duplicate ZIP member {name}")
            names.add(name)
        required = {
            "PACKAGE_MANIFEST.json",
            "REVIEWER_README.md",
            "verify_manifest.py",
            "replay_active_proof.py",
            "n6_exact_ordinary_chow_rank_32.py",
            "n6_exact_ordinary_chow_rank_32.json",
            "test_n6_exact_ordinary_chow_rank_32.py",
            "latex/perm3456_v15_repaired/n6_body.tex",
            "latex/perm3456_v15_repaired/n6_computation_spec.tex",
            "latex/perm3456_v15_repaired/perm3456_chow_rank_strict_proofs_zh_ams.pdf",
        }
        missing = required - names
        if missing:
            fail(f"required ZIP entries missing: {sorted(missing)}")
        with tempfile.TemporaryDirectory(prefix="perm3456_v15_asset_verify_") as temporary:
            extracted = Path(temporary)
            archive.extractall(extracted)
            run_inner("verify_manifest.py", extracted)
            if args.replay:
                run_inner("replay_active_proof.py", extracted)
                run_inner("verify_manifest.py", extracted)

    print(
        "PASS_V15_REPAIRED_RELEASE_ASSETS "
        f"files=2 zip_entries={expected_entries} replay={args.replay}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
