from __future__ import annotations

import importlib.util
import json
import os
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
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_counts_and_no_collision(self) -> None:
        self.assertEqual(self.payload["all_coordinate_six_cell_supports"], 1_947_792)
        self.assertEqual(self.payload["rectangle_free_coordinate_supports"], 1_837_392)
        self.assertEqual(self.payload["distinct_quotient_signatures"], 1_837_392)
        self.assertEqual(self.payload["collision_count"], 0)

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)

    def test_streaming_recovery_representatives(self) -> None:
        supports = (
            (0, 1, 2, 3, 4, 5),
            (0, 1, 2, 3, 10, 17),
            (0, 1, 2, 9, 16, 23),
            (0, 1, 2, 3, 4, 11),
            (0, 7, 14, 21, 28, 29),
            (0, 7, 14, 21, 28, 35),
        )
        for support in supports:
            self.assertTrue(AUDIT.is_rectangle_free(support))
            self.assertEqual(AUDIT.recover_signature(AUDIT.signature(support)), support)

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to scan all 1,947,792 supports",
    )
    def test_full_streaming_replay(self) -> None:
        self.assertEqual(AUDIT.audit(), self.payload)


if __name__ == "__main__":
    unittest.main()
