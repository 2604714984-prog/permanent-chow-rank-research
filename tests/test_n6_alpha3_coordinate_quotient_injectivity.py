from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_coordinate_quotient_injectivity.py"
FROZEN = ROOT / "data" / "n6_alpha3_coordinate_quotient_injectivity.json"
SPEC = importlib.util.spec_from_file_location("n6_alpha3_coordinate_injectivity", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class AlphaThreeCoordinateQuotientInjectivityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_exact_counts_and_no_collision(self) -> None:
        self.assertEqual(self.payload["all_coordinate_six_cell_supports"], 1_947_792)
        self.assertEqual(self.payload["rectangle_free_coordinate_supports"], 1_837_392)
        self.assertEqual(self.payload["distinct_quotient_signatures"], 1_837_392)
        self.assertEqual(self.payload["collision_count"], 0)

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
