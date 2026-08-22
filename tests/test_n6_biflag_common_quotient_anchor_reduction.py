from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_biflag_common_quotient_anchor_reduction.py"
DATA = ROOT / "data" / "n6_biflag_common_quotient_anchor_reduction.json"
SPEC = importlib.util.spec_from_file_location("n6104", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestN6104(unittest.TestCase):
    def test_row_signatures(self) -> None:
        self.assertEqual(len(MODULE.row_signatures()), 5)
        self.assertTrue(all(high >= 4 for high, _, _ in MODULE.row_signatures()))

    def test_column_signatures(self) -> None:
        self.assertEqual(len(MODULE.column_signatures()), 7)
        self.assertTrue(all(high >= 3 for high, _, _ in MODULE.column_signatures()))

    def test_coordinate_matching_injectivity(self) -> None:
        self.assertEqual(MODULE.permutation_matching_signatures(), (720, 720))

    def test_anchor_frontier(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(
            payload["surviving_anchor_ranks"]["four_combinations"],
            [[3, 4], [3, 5], [5, 4], [5, 5]],
        )
        self.assertTrue(payload["all_rank_one_branch"]["excluded"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text(encoding="utf-8")), MODULE.build_payload())


if __name__ == "__main__":
    unittest.main()
