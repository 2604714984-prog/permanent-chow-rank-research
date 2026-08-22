from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower50_boolean_controls.py"
SPEC = importlib.util.spec_from_file_location("n7_lower50_boolean_controls", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Lower50BooleanControlTests(unittest.TestCase):
    def test_all_five_planes_and_no_socle(self) -> None:
        payload = MODULE.build_certificate()
        self.assertEqual(payload["five_planes_checked"], 2_667)
        self.assertEqual(payload["minimum_rank_W_times_A3"], 35)
        self.assertEqual(payload["degree_three_no_socle_rank"], 35)
        frozen = json.loads(
            (ROOT / "data" / "n7_lower50_boolean_controls.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload, frozen)


if __name__ == "__main__":
    unittest.main()
