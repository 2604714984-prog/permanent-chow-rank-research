from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VERIFIER_SOURCE = (
    REPOSITORY_ROOT / "evidence" / "small_n" / "v14_repaired" / "verify_assets.py"
)
PDF_NAME = "perm345_chow_rank_v14_repaired_zh_ams.pdf"
ZIP_NAME = "perm345_reviewer_submission_v14_repaired_20260812.zip"
REQUIRED_ZIP_ENTRIES = {
    "PACKAGE_MANIFEST.json": "{}\n",
    "REVIEWER_README.md": "fixture\n",
    "requirements-replay.txt": "\n",
    "perm5_one_intersection_flag_standalone_exact.py": "\n",
    "n5_one_intersection_flag_standalone_exact.json": "{}\n",
    "latex/perm345_v14_repaired/n5_body.tex": "fixture\n",
    "latex/perm345_v14_repaired/formal_computation_spec.tex": "fixture\n",
    "controlled.txt": "clean\n",
}
INNER_GUARD = """\
import os
import sys
from pathlib import Path

if not sys.dont_write_bytecode:
    raise SystemExit("bytecode writing was not disabled")
if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1":
    raise SystemExit("PYTHONDONTWRITEBYTECODE was not pinned")
if Path("controlled.txt").read_text(encoding="utf-8") != "clean\\n":
    raise SystemExit("controlled file changed")
"""
NOOP_REPLAY = """\
import os
import sys

if not sys.dont_write_bytecode:
    raise SystemExit("bytecode writing was not disabled")
if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1":
    raise SystemExit("PYTHONDONTWRITEBYTECODE was not pinned")
"""
MUTATING_REPLAY = """\
from pathlib import Path

Path("controlled.txt").write_text("dirty\\n", encoding="utf-8")
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


class V14AssetVerifierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="v14_outer_verifier_test_")
        self.root = Path(self.temporary.name)
        shutil.copy2(VERIFIER_SOURCE, self.root / "verify_assets.py")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def build_fixture(self, replay_script: str = NOOP_REPLAY) -> dict[str, object]:
        pdf_path = self.root / PDF_NAME
        pdf_path.write_bytes(b"%PDF-1.7 fixture\n")

        entries = dict(REQUIRED_ZIP_ENTRIES)
        entries["verify_manifest.py"] = INNER_GUARD
        entries["replay_active_proof.py"] = replay_script
        zip_path = self.root / ZIP_NAME
        with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
            for name, content in entries.items():
                archive.writestr(name, content)

        payload: dict[str, object] = {
            "format": "perm345-v14-repaired-release-assets-v1",
            "artifacts": [
                {
                    "file": PDF_NAME,
                    "bytes": pdf_path.stat().st_size,
                    "sha256": sha256(pdf_path),
                },
                {
                    "file": ZIP_NAME,
                    "bytes": zip_path.stat().st_size,
                    "sha256": sha256(zip_path),
                },
            ],
            "zip_entries": len(entries),
        }
        self.write_manifest(payload)
        return payload

    def write_manifest(self, payload: dict[str, object]) -> None:
        (self.root / "MANIFEST.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )

    def run_verifier(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", "verify_assets.py", *arguments],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_normal_package_passes(self) -> None:
        self.build_fixture()
        result = self.run_verifier()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS_V14_REPAIRED_RELEASE_ASSETS", result.stdout)

    def test_empty_artifact_list_fails(self) -> None:
        payload = self.build_fixture()
        payload["artifacts"] = []
        self.write_manifest(payload)
        result = self.run_verifier()
        self.assertNotEqual(result.returncode, 0)

    def test_missing_pdf_artifact_fails(self) -> None:
        payload = self.build_fixture()
        payload["artifacts"] = payload["artifacts"][1:]
        self.write_manifest(payload)
        result = self.run_verifier()
        self.assertNotEqual(result.returncode, 0)

    def test_duplicate_or_extra_artifact_fails(self) -> None:
        for mode in ("duplicate", "extra"):
            with self.subTest(mode=mode):
                payload = self.build_fixture()
                artifacts = list(payload["artifacts"])
                if mode == "duplicate":
                    payload["artifacts"] = [artifacts[0], dict(artifacts[0])]
                else:
                    payload["artifacts"] = artifacts + [
                        {"file": "extra.bin", "bytes": 1, "sha256": "0" * 64}
                    ]
                self.write_manifest(payload)
                result = self.run_verifier()
                self.assertNotEqual(result.returncode, 0)

    def test_replay_mutation_is_caught_by_post_verify(self) -> None:
        self.build_fixture(replay_script=MUTATING_REPLAY)
        result = self.run_verifier("--replay")
        self.assertNotEqual(result.returncode, 0)

    def test_replay_disables_bytecode_side_effects(self) -> None:
        self.build_fixture()
        result = self.run_verifier("--replay")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
