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
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CoordinateSecondOrderEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_exact_maximum_and_equality_locus(self) -> None:
        self.assertEqual(self.payload["supports_checked"], 14893)
        self.assertEqual(self.payload["maximum_second_order_envelope"], 14)
        self.assertEqual(self.payload["equality_supports"], 96)
        self.assertEqual(self.payload["equality_row_column_orbits"], 1)
        self.assertEqual(
            self.payload["equality_partial_matching_counts"],
            {"r2": 9, "r3": 2, "r4": 0},
        )

    def test_six_extremal_envelopes_cover_the_target(self) -> None:
        self.assertEqual(self.payload["explicit_cover_frame_count"], 6)
        self.assertEqual(self.payload["explicit_cover_union"], 24)
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
