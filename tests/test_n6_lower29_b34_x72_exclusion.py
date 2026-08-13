from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts import n6_lower29_b34_x72_exclusion as n6097


ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "data" / "n6_lower29_b34_x72_exclusion.json"


class N6Lower29B34X72ExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = n6097.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_three_packets_are_excluded(self) -> None:
        self.assertEqual(self.payload["input_frontier_packet_count"], 3)
        self.assertTrue(self.payload["one_relation_packet_excluded_by_N6_094"])
        self.assertTrue(self.payload["direct_packet"]["excluded"])
        self.assertTrue(self.payload["one_defective_packet"]["excluded"])

    def test_direct_cap_and_shortening(self) -> None:
        row = self.payload["direct_packet"]
        self.assertEqual(row["alpha_at_most_two_prolongation_cap_from_N6_096"], 464)
        self.assertEqual(row["required_prolongation_lower"], 468)
        self.assertEqual(row["six_selected_permanent_quadratic_intersection_cap"], 75)
        self.assertEqual(row["product_shadow_lower_m52"], 78)

    def test_defective_shortening(self) -> None:
        row = self.payload["one_defective_packet"]
        self.assertEqual(row["x72_shortening_floor_after_omitting_defective_term"], 52)
        self.assertEqual(row["six_full_permanent_quadratic_relation_dimension"], 75)
        self.assertEqual(row["product_shadow_lower_m52"], 78)

    def test_updated_boundary(self) -> None:
        self.assertTrue(self.payload["x72_actual_layer_excluded"])
        self.assertEqual(self.payload["updated_residual_seven_set_upper"], 71)
        self.assertIn("remaining x_A<=71", self.payload["claim_boundary"])
        self.assertIn("lower29", self.payload["claim_boundary"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
