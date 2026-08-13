from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_biflag_three_by_four_chart.py"
DATA = ROOT / "data" / "n6_biflag_three_by_four_chart.json"
SPEC = importlib.util.spec_from_file_location("n6106", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestN6106(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_two_coordinate_orbits_are_distinguished(self) -> None:
        rows = self.payload["linear_only_graph_reduction"]["orbit_certificates"]
        self.assertEqual([row["kernel_dimension"] for row in rows], [31, 19])
        self.assertEqual([row["tail_parameter_count"] for row in rows], [12, 0])
        self.assertEqual([row["minimum_rank_outside_kernel"] for row in rows], [6, 6])

    def test_wing_chart_exact_kernel(self) -> None:
        rows = self.payload["linear_only_graph_reduction"]["orbit_certificates"]
        wing = next(row for row in rows if row["name"] == "3x4_missing_wing_column")
        self.assertEqual(wing["graph_variable_count"], 132)
        self.assertEqual(wing["linear_equation_rank_over_Q"], 113)
        self.assertEqual(wing["expected_normal_form_dimension"], 19)
        self.assertEqual(wing["minimum_rank_outside_kernel"], 6)

    def test_corner_defect_rank(self) -> None:
        rows = self.payload["tail_and_corner_defect_reduction"]["orbit_certificates"]
        self.assertEqual(
            [row["coordinate_corner_defect_ranks_over_Q"] for row in rows],
            [[6] * 12, [6] * 12],
        )
        self.assertEqual(
            [row["coordinate_tail_ranks_over_Q"] for row in rows],
            [[6] * 12, []],
        )

    def test_product_dimension_gate(self) -> None:
        gate = self.payload["product_dimension_gate"]
        self.assertEqual(gate["row_parameter_support_at_most_one"]["intersection_dimensions"], [15, 18])
        self.assertEqual(gate["row_parameter_support_at_least_two"]["intersection_dimensions"], [10, 12])

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude every 4x3 endpoint", boundary)
        self.assertIn("does not", boundary)

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text(encoding="utf-8")), self.payload)


if __name__ == "__main__":
    unittest.main()
