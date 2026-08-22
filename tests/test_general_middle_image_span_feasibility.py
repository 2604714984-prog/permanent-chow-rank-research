from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_middle_image_span_feasibility.py"
FROZEN = ROOT / "data" / "general_middle_image_span_feasibility.json"


def load_module():
    spec = importlib.util.spec_from_file_location("middle_span_feasibility", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class GeneralMiddleImageSpanFeasibilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_perm6_recovers_the_proved_slope(self) -> None:
        row = AUDIT.row(6)
        self.assertEqual(row["required_local_slope"], "10/3")
        self.assertEqual(row["one_direction_capacity"], 10)

    def test_perm7_single_layer_target_exceeds_full_quotient_capacity(self) -> None:
        row = AUDIT.row(7)
        self.assertEqual(row["middle_subset_rank_q"], 35)
        self.assertEqual(row["glynn_target"], 64)
        self.assertEqual(row["required_local_slope"], "145/7")
        self.assertEqual(row["one_direction_capacity"], 35)
        self.assertEqual(row["full_quotient_average_slope_capacity"], "10")
        self.assertFalse(row["slope_feasible"])

    def test_perm6_is_last_even_single_layer_feasibility_case(self) -> None:
        self.assertEqual(self.payload["last_feasible_even_n"], 6)
        self.assertEqual(AUDIT.row(8)["required_local_slope"], "1015/32")
        self.assertFalse(AUDIT.row(10)["slope_feasible"])

    def test_perm5_is_last_odd_single_layer_feasibility_case(self) -> None:
        self.assertEqual(self.payload["last_feasible_odd_n"], 5)
        self.assertFalse(AUDIT.row(7)["slope_feasible"])
        self.assertFalse(AUDIT.row(9)["slope_feasible"])

    def test_boundary_is_not_a_rank_theorem(self) -> None:
        self.assertIn("does not prove", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
