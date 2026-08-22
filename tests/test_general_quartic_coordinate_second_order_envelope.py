from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_coordinate_second_order_envelope.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_coordinate_second_order_envelope_independent.py"
DATA = ROOT / "data" / "general_quartic_coordinate_second_order_envelope.json"

spec = importlib.util.spec_from_file_location("coordinate_second_order_envelope", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(SCRIPT)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CoordinateSecondOrderEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_correct_unrestricted_maximum(self) -> None:
        data = self.payload["unrestricted"]
        self.assertEqual(data["maximum_second_order_envelope"], 18)
        self.assertEqual(data["equality_supports"], 16)
        self.assertEqual(data["equality_row_column_orbits"], 1)
        self.assertEqual(data["equality_graph"], "PUNCTURED_ROW_COLUMN_CROSS")
        self.assertEqual(
            data["equality_partial_matching_counts"],
            {"r2": 9, "r3": 0, "r4": 0},
        )

    def test_c6_maximum_under_degree_cap_two(self) -> None:
        data = self.payload["row_column_degree_cap_two"]
        self.assertEqual(data["maximum_second_order_envelope"], 14)
        self.assertEqual(data["equality_supports"], 96)
        self.assertEqual(data["equality_row_column_orbits"], 1)
        self.assertEqual(
            data["equality_partial_matching_counts"],
            {"r2": 9, "r3": 2, "r4": 0},
        )

    def test_six_c6_envelopes_cover_the_target(self) -> None:
        cover = self.payload["explicit_c6_cover"]
        self.assertEqual(cover["frame_count"], 6)
        self.assertEqual(cover["union"], 24)
        self.assertEqual(
            self.payload["claim_boundary"]["raw_second_order_support_route"],
            "INSUFFICIENT",
        )
        self.assertFalse(
            self.payload["claim_boundary"]["second_order_six_block_witness"]
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
            "GENERAL_QUARTIC_COORDINATE_SECOND_ORDER_ENVELOPE_INDEPENDENT_PASS",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
