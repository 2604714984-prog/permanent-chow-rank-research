from __future__ import annotations

import importlib.util
import json
import os
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_coordinate29_koszul_minor.py"
SPEC = importlib.util.spec_from_file_location("n7_coordinate29_koszul_minor", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N7Coordinate29KoszulMinorTests(unittest.TestCase):
    def test_witness_support_count(self) -> None:
        self.assertEqual(AUDIT.ACTIVE_COUNT, 29)
        self.assertEqual(len(AUDIT.SUPPORTED_OUTPUTS), 1061)

    def test_frozen_summary(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_coordinate29_koszul_minor.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(frozen["active_edge_count"], 29)
        self.assertEqual(
            frozen["supported_degree_three_and_four_subpermanent_count"], 1061
        )
        self.assertEqual(len(frozen["rows"]), 29)
        self.assertFalse(frozen["any_lower_50_test_passes"])
        self.assertEqual(frozen["ordinary_chow_lower_bound_from_best_minor"], 31)
        self.assertEqual(frozen["rows"][14]["leading_minor_rank"], 42_294_534_282)

    @unittest.skipUnless(os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1", "full replay is opt-in")
    def test_full_replay(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_coordinate29_koszul_minor.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(AUDIT.build_payload(1), frozen)


if __name__ == "__main__":
    unittest.main()
