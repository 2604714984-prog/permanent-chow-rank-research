from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_coordinate_first_order_closure.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_coordinate_first_order_closure_independent.py"
DATA = ROOT / "data" / "general_quartic_coordinate_first_order_closure.json"

spec = importlib.util.spec_from_file_location("coordinate_first_order_closure", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CoordinateFirstOrderClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_support_profile(self) -> None:
        audit = self.payload["support_audit"]
        self.assertEqual(audit["supports_checked"], 14893)
        self.assertEqual(
            audit["maximum_envelope_by_support_size"],
            {"0": 0, "1": 0, "2": 0, "3": 1, "4": 2, "5": 4, "6": 6},
        )
        self.assertEqual(audit["two_direct_six_cell_supports"], 72)

    def test_source_fiber_budget(self) -> None:
        audit = self.payload["frame_audit"]
        self.assertEqual(audit["coordinate_multisets_checked"], 54264)
        self.assertEqual(audit["maximum_vertical_non_direct_support"], 2)
        self.assertEqual(audit["maximum_local_score_e_plus_p_plus_v"], 6)

    def test_global_contradiction(self) -> None:
        audit = self.payload["global_incidence"]
        self.assertEqual(audit["minimum_required_sum_e_plus_p_plus_v"], 48)
        self.assertEqual(audit["maximum_available_sum_e_plus_p_plus_v"], 36)
        self.assertEqual(audit["contradiction_margin"], 12)
        self.assertEqual(
            self.payload["conclusion"]["coordinate_regular_first_order_six_block_lift"],
            "IMPOSSIBLE",
        )

    def test_independent_replay(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_CLOSURE_INDEPENDENT_PASS",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
