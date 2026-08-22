from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_c6_second_order_source_reduction.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_c6_second_order_source_reduction_independent.py"
DATA = ROOT / "data" / "general_quartic_c6_second_order_source_reduction.json"

spec = importlib.util.spec_from_file_location("c6_source_reduction", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class C6SecondOrderSourceReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_order_zero_source_kernel(self) -> None:
        self.assertEqual(self.payload["source_coordinates"], 90)
        self.assertEqual(self.payload["distinct_source_monomials"], 81)
        self.assertEqual(
            self.payload["source_multiplicity_distribution"],
            {"1": 72, "2": 9},
        )
        self.assertEqual(self.payload["order_zero_kernel_dimension"], 9)
        self.assertEqual(
            self.payload["order_zero_kernel_basis"],
            "NINE_PAIRWISE_CROSS_DIFFERENCES",
        )

    def test_collision_graph_and_targets(self) -> None:
        graph = self.payload["source_collision_graph"]
        self.assertEqual(graph, {
            "vertices": 9,
            "degree": 4,
            "edges": 18,
            "common_tangent_channels_per_edge": 4,
        })
        self.assertEqual(self.payload["cross_boundary_target_count"], 18)
        self.assertTrue(self.payload["cross_boundary_target_edge_bijection"])
        self.assertEqual(self.payload["fixed_33_target_count"], 6)
        self.assertEqual(self.payload["source_modes_per_fixed_33_target"], [6])

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertTrue(boundary["coefficient_system_reduced"])
        self.assertFalse(boundary["second_order_lift_decided"])
        self.assertEqual(boundary["mu_6_4_exact_value"], "OPEN_IN_[6,8]")

    def test_independent_replay(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_C6_SECOND_ORDER_SOURCE_REDUCTION_INDEPENDENT_PASS",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
