from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_first_shortening.py"
FROZEN = ROOT / "data" / "n6_lower29_b34_first_shortening.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6081_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B34FirstShorteningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_shadow_jump_and_literal_floors(self) -> None:
        row = self.payload["seven_set_shortening"]
        self.assertEqual(row["exact_product_shadow_table_66_to_81"]["80"], 90)
        self.assertEqual(row["exact_product_shadow_table_66_to_81"]["81"], 96)
        self.assertEqual(row["universal_x_A_upper"], 80)
        self.assertEqual(row["every_fifteen_set_literal_dimension_floor"], 286)
        self.assertEqual(row["every_seven_set_literal_dimension_floor"], 126)

    def test_conditional_state_pruning(self) -> None:
        row = self.payload["conditional_f80_state_pruning"]
        self.assertEqual((row["state_count"], row["existing_cap_excluded_count"], row["pre_geometry_survivor_count"]), (11, 10, 1))
        survivors = [state for state in row["states"] if not state["excluded_by_existing_cap"]]
        self.assertEqual(survivors[0]["epsilon"], [0] * 7)
        self.assertEqual((survivors[0]["kappa2"], survivors[0]["d2"], survivors[0]["t2_upper"]), (0, 105, 15))

    def test_unique_geometric_endpoint(self) -> None:
        row = self.payload["unique_endpoint"]
        self.assertEqual(row["alpha"], [3] * 7)
        self.assertEqual((row["a2"], row["literal_middle_dimension"]), (90, 140))
        self.assertGreater(row["required_prolongation_lower"], row["alpha_at_most_two_cap"])
        self.assertTrue(row["all_quotient_images_equal_one_common_W15"])
        self.assertTrue(row["six_anchor_differences_span_the_90_plane"])

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude global b=34", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
