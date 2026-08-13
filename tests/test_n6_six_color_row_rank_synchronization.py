from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_six_color_row_rank_synchronization.py"
FROZEN = ROOT / "data" / "n6_six_color_row_rank_synchronization.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_six_color_sync", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SixColorRowRankSynchronizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_frozen_payload(self):
        self.assertEqual(cls_payload := self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))
        self.assertEqual(cls_payload["status"][-1], "N6-071")

    def test_rank_five_kernel_support_formula(self):
        rows = self.payload["rank_five_kernel_support_replay"]
        self.assertEqual(len(rows), 6)
        self.assertEqual(
            [row["exact_compression_rank"] for row in rows],
            [15, 14, 13, 12, 11, 10],
        )
        for row in rows:
            self.assertEqual(row["exact_compression_rank"], row["formula_rank"])
            self.assertEqual(row["row_block_rank"], 5)

    def test_claim_boundary_is_strict(self):
        boundary = self.payload["claim_boundary"]
        self.assertIn("no additional single-row equation", boundary)
        self.assertIn("does not exclude", boundary)
        self.assertIn("full permanent quotient", boundary)
        self.assertIn("K75", boundary)


if __name__ == "__main__":
    unittest.main()
