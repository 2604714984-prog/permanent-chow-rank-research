from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_c6_second_order_pair_cancellation.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_c6_second_order_pair_cancellation_independent.py"
DATA = ROOT / "data" / "general_quartic_c6_second_order_pair_cancellation.json"

spec = importlib.util.spec_from_file_location("c6_pair_cancellation", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class C6SecondOrderPairCancellationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_boundary_tangent_separation(self) -> None:
        self.assertEqual(self.payload["source_mode_count"], 9)
        self.assertEqual(self.payload["boundary_cell_count"], 7)
        self.assertEqual(self.payload["boundary_tangent_rows"], 252)
        self.assertEqual(self.payload["boundary_tangent_row_multiplicity"], 1)

    def test_cross_target_pair_cancellation(self) -> None:
        self.assertEqual(self.payload["cross_boundary_target_count"], 18)
        self.assertEqual(self.payload["source_modes_per_cross_target"], 2)
        self.assertEqual(self.payload["pair_cancellation_checks"], 36)
        self.assertEqual(
            self.payload["conclusion"]["canonical_fixed_3x3_six_c6_second_order_cover"],
            "ZERO_ON_18_CROSS_TARGETS",
        )
        self.assertEqual(
            self.payload["conclusion"]["permanent_target"],
            "IMPOSSIBLE_IN_THIS_SUBCASE",
        )

    def test_claim_boundary(self) -> None:
        boundary = self.payload["conclusion"]
        self.assertEqual(boundary["general_coordinate_second_order_covers"], "OPEN")
        self.assertEqual(boundary["mu_6_4_exact_value"], "OPEN_IN_[6,8]")
        self.assertFalse(boundary["new_unrestricted_chow_rank_bound"])
        self.assertFalse(boundary["new_border_rank_bound"])

    def test_independent_replay(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_C6_SECOND_ORDER_PAIR_CANCELLATION_INDEPENDENT_PASS",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
