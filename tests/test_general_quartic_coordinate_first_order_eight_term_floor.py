from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_coordinate_first_order_eight_term_floor.py"
DATA = ROOT / "data" / "general_quartic_coordinate_first_order_eight_term_floor.json"

spec = importlib.util.spec_from_file_location("coordinate_eight_term_floor", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CoordinateFirstOrderEightTermFloorTests(unittest.TestCase):
    def test_frozen_payload_and_margins(self) -> None:
        payload = module.payload()
        self.assertEqual(payload, json.loads(DATA.read_text(encoding="utf-8")))
        self.assertEqual(payload["minimum_component_count"], 8)
        self.assertEqual(payload["q6_margin"], 12)
        self.assertEqual(payload["q7_margin"], 6)
        self.assertEqual(
            payload["conclusion"]["coordinate_regular_first_order_q_le_7"],
            "IMPOSSIBLE",
        )
        self.assertEqual(
            payload["conclusion"]["coordinate_regular_first_order_q8_existence"],
            "OPEN",
        )


if __name__ == "__main__":
    unittest.main()
