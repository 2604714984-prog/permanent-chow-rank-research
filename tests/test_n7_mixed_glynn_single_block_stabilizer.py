from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_mixed_glynn_single_block_stabilizer.py"
SPEC = importlib.util.spec_from_file_location("n7_mixed_glynn_stabilizer", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class MixedGlynnSingleBlockStabilizerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = AUDIT.input_data(97_531, 400)
        AUDIT.initialize_worker(*data)
        cls.frozen = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_single_block_stabilizer.json").read_text(
                encoding="utf-8"
            )
        )

    def test_identity_and_one_nonidentity(self) -> None:
        identity = AUDIT.trial(63 * 720)
        nonidentity = AUDIT.trial(0)
        self.assertEqual(identity["degree_six_target_intersection"], 7)
        self.assertEqual(nonidentity["degree_six_target_intersection"], 1)

    def test_frozen_exhaustion_summary(self) -> None:
        self.assertEqual(self.frozen["candidate_count"], 46_080)
        self.assertEqual(self.frozen["intersection_histogram"], {"1": 46_079, "7": 1})
        self.assertEqual(self.frozen["maximizer_count"], 1)
        self.assertEqual(self.frozen["maximizers"][0]["index"], 45_360)


if __name__ == "__main__":
    unittest.main()
