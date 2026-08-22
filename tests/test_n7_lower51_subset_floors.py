import json
import unittest
from pathlib import Path

from scripts.n7_lower51_subset_floors import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51SubsetFloorsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = json.loads(
            (ROOT / "data/n7_lower50_section_caps_audit.json").read_text(
                encoding="utf-8"
            )
        )
        cls.payload = build(source)
        cls.rows = {
            row["retained_terms"]: row for row in cls.payload["rows"]
        }

    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_subset_floors.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, expected)

    def test_load_bearing_factor_span_floors(self):
        self.assertEqual(
            [self.rows[k]["factor_span_floor_from_degree6"] for k in (1, 2, 3, 4)],
            [0, 5, 12, 16],
        )
        self.assertEqual(self.rows[50]["factor_span_floor_from_degree6"], 49)

    def test_cross_degree_controls(self):
        self.assertEqual(
            [self.rows[k]["degree5_derivative_floor"] for k in (1, 2, 3, 4)],
            [0, 0, 15, 36],
        )
        self.assertEqual(
            [self.rows[k]["degree4_derivative_floor"] for k in (1, 2, 3, 4, 5)],
            [0, 0, 0, 0, 9],
        )


if __name__ == "__main__":
    unittest.main()
