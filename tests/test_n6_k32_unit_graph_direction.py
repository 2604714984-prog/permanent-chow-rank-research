from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_unit_graph_direction.py"
FROZEN = ROOT / "data" / "n6_k32_unit_graph_direction.json"


spec = importlib.util.spec_from_file_location("n6_k32_unit_graph_direction", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-122 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32UnitGraphDirectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_four_orbit_ranks(self) -> None:
        exact = self.payload["exact_certificate"]
        self.assertEqual(
            exact["symbolic_ranks_over_Q_t"],
            {
                "same_row_same_column": 7,
                "same_row_different_column": 7,
                "different_row_same_column": 6,
                "different_row_different_column": 6,
            },
        )

    def test_all_unit_directions_are_noncomplementary(self) -> None:
        records = self.payload["exact_certificate"]["all_36_records_at_t_1"]
        self.assertEqual(len(records), 36)
        self.assertTrue(all(record["sum_rank"] == 7 for record in records))
        self.assertEqual(
            sum(record["cross_rank"] == 6 for record in records), 24
        )


if __name__ == "__main__":
    unittest.main()
