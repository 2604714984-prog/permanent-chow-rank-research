from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_rectangular_half_defect_reduction.py"
FROZEN = ROOT / "data" / "n7_rectangular_half_defect_reduction.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n7_rectangular_reduction", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N7RectangularHalfDefectReductionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_global_constants(self) -> None:
        self.assertEqual(self.payload["permanent_rectangular_catalectic_rank"], 1225)
        self.assertEqual(self.payload["required_combined_excess"], 1015)
        self.assertEqual(self.payload["required_two_sided_slope"], "145/7")

    def test_middle_rank_floors(self) -> None:
        floors = self.payload["middle_rank_floors_by_factor_span"]
        self.assertEqual(
            [floors[str(i)]["minimum_middle_rank"] for i in range(1, 8)],
            [1, 2, 4, 8, 15, 25, 35],
        )

    def test_full_quotient_is_an_exact_route_counterexample(self) -> None:
        self.assertFalse(self.payload["slope_below_capacity"])
        self.assertEqual(self.payload["full_quotient_symbol_capacity"], 70)
        self.assertEqual(self.payload["full_quotient_required_by_linear_slope"], "145")
        self.assertEqual(self.payload["full_quotient_gap"], "-75")
        self.assertIn("inequality is false", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
