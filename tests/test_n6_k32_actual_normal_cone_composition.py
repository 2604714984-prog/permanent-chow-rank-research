from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_actual_normal_cone_composition.py"
FROZEN = ROOT / "data" / "n6_k32_actual_normal_cone_composition.json"


spec = importlib.util.spec_from_file_location("n6_k32_actual_normal_cone", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class K32ActualNormalConeCompositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_replay_matches_frozen(self) -> None:
        self.assertEqual(module.build_payload(), self.payload)

    def test_direction_partition(self) -> None:
        partition = self.payload["fixed_direction_partition"]
        self.assertEqual(partition, {
            "row_changing": 24,
            "same_row_relative": 4,
            "same_row_average_sign": 16,
            "total": 44,
        })

    def test_condition_is_explicit(self) -> None:
        hypothesis = self.payload["hypothesis"]
        self.assertIn("finite_point_realization", hypothesis)
        self.assertIn("unproved", self.payload["boundary"][0])

    def test_local_certificates(self) -> None:
        local = self.payload["local_inputs"]
        self.assertEqual(local["row_changing"]["certificate"], "N6-123")
        self.assertEqual(local["same_row_relative"]["certificate"], "N6-125")
        self.assertEqual(local["same_row_average_sign"]["certificate"], "N6-127")
        self.assertEqual(sum(item["directions"] for item in local.values()), 44)


if __name__ == "__main__":
    unittest.main()
