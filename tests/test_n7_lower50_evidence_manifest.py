from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower50_evidence_manifest.py"
SPEC = importlib.util.spec_from_file_location("n7_lower50_evidence_manifest", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Lower50EvidenceManifestTests(unittest.TestCase):
    def test_manifest_matches_files(self) -> None:
        actual = MODULE.build_manifest()
        frozen = json.loads(
            (ROOT / "data" / "n7_lower50_evidence_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(actual, frozen)
        self.assertFalse(actual["scope"]["border_rank_claim"])
        self.assertEqual(len(actual["files"]), len(MODULE.PATHS))


if __name__ == "__main__":
    unittest.main()
