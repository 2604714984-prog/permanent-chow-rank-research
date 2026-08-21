from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_coordinate_regular_first_order_zero.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_coordinate_regular_first_order_zero_independent.py"
DATA = ROOT / "data" / "general_quartic_coordinate_regular_first_order_zero.json"

spec = importlib.util.spec_from_file_location("coordinate_first_order_zero", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load coordinate first-order verifier")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CoordinateRegularFirstOrderZeroTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_exact_frame_count_and_local_caps(self) -> None:
        self.assertEqual(self.payload["coordinate_multiset_frames_checked"], 54264)
        self.assertEqual(self.payload["maximum_first_order_matching_envelope"], 6)
        self.assertEqual(self.payload["maximum_private_matching_capacity"], 2)

    def test_envelope_six_equality_state(self) -> None:
        self.assertEqual(self.payload["envelope_six_frames"], 288)
        self.assertEqual(self.payload["envelope_six_row_column_orbits"], 2)
        self.assertEqual(self.payload["envelope_six_private_histogram"], {"0": 288})

    def test_two_direct_matching_frames_have_envelope_two(self) -> None:
        self.assertEqual(self.payload["two_direct_envelope_sizes"], [2])

    def test_global_incidence_contradiction(self) -> None:
        incidence = self.payload["global_incidence"]
        self.assertEqual(incidence["six_component_incidence_cap"], 36)
        self.assertEqual(incidence["target_incidence_floor"], 36)
        self.assertEqual(incidence["frames_with_envelope_6_and_private_2"], 0)
        self.assertEqual(
            incidence["coordinate_regular_first_order_six_block_witness"],
            "IMPOSSIBLE",
        )

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text()))

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_COORDINATE_REGULAR_FIRST_ORDER_ZERO_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
