from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_target_integrability_core.py"
FROZEN = ROOT / "data" / "n7_target_integrability_core.json"
SPEC = importlib.util.spec_from_file_location("n7_target_integrability_core", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load corrected TI core")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TargetIntegrabilityCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload,
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_nonzero_gauge_changes_tensor_but_not_target(self) -> None:
        control = self.payload["control"]
        self.assertTrue(control["coefficient_fiber_preserved_by_nonzero_gauge"])
        self.assertEqual(control["base_relation_tensor_rank"], 0)
        self.assertGreater(control["shifted_relation_tensor_rank"], 0)
        self.assertTrue(control["shifted_tensor_columns_lie_in_r5"])
        self.assertTrue(control["gauge_difference_equals_d_a"])

    def test_frontier_gauge_dimensions(self) -> None:
        observed = [
            (
                row["frontier"],
                row["gauge_source_dimension"],
                row["relation_tensor_dimension"],
            )
            for row in self.payload["frontier_dimensions"]
        ]
        self.assertEqual(
            observed,
            [
                ("F1", 7, 42),
                ("F2", 14, 63),
                ("F3-H6-41", 7, 42),
                ("F3-H6-42", 0, 42),
                ("F4", 21, 84),
                ("F5-H6-40", 14, 63),
                ("F5-H6-41", 7, 63),
            ],
        )


if __name__ == "__main__":
    unittest.main()
