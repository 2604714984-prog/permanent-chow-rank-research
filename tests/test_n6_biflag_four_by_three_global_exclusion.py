from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_biflag_four_by_three_global_exclusion.py"
DATA = ROOT / "data" / "n6_biflag_four_by_three_global_exclusion.json"
SPEC = importlib.util.spec_from_file_location("n6107", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestN6107(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_three_linear_kernels(self) -> None:
        rows = self.payload["linear_graph_reduction"]["orbit_certificates"]
        self.assertEqual([row["kernel_dimension"] for row in rows], [18, 30, 28])
        self.assertEqual([row["factor_parameter_count"] for row in rows], [6, 6, 4])
        self.assertEqual([row["exception_parameter_count"] for row in rows], [12, 24, 24])
        self.assertEqual([row["minimum_rank_outside_kernel"] for row in rows], [6, 6, 6])

    def test_exception_coordinates_have_rank_six(self) -> None:
        rows = self.payload["exception_reduction"]["orbit_certificates"]
        self.assertEqual([row["pure_exception_weight_count"] for row in rows], [12, 24, 24])
        self.assertTrue(
            all(
                row["coordinate_exception_ranks_over_Q"]
                == [6] * row["exception_parameter_count"]
                for row in rows
            )
        )

    def test_product_dimension_gates(self) -> None:
        gate = self.payload["product_dimension_gate"]
        self.assertEqual(gate["noncore_R4_tensor_B3"]["branch_count"], 9)
        self.assertEqual(gate["noncore_R4_tensor_B3"]["branch_dimension"], 2)
        self.assertEqual(gate["tail_A4_tensor_C3"]["branch_count"], 1)
        self.assertEqual(gate["tail_A4_tensor_C3"]["branch_dimension"], 4)

    def test_all_six_coordinate_orbits_are_covered(self) -> None:
        globalization = self.payload["globalization"]
        self.assertEqual(globalization["coordinate_fixed_point_count"], 34)
        self.assertEqual(sum(globalization["local_chart_coverage"].values()), 6)
        self.assertIn("Every U in Z is a product", globalization["conclusion"])

    def test_claim_boundary(self) -> None:
        self.assertIn("other nine", self.payload["remaining_lower29_frontier"])
        self.assertIn("does not prove ordinary lower 29", self.payload["remaining_lower29_frontier"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text(encoding="utf-8")), self.payload)


if __name__ == "__main__":
    unittest.main()

