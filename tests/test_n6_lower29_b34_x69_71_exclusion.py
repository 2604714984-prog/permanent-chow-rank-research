import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x69_71_exclusion.py"
DATA = ROOT / "data" / "n6_lower29_b34_x69_71_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6098_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Lower29B34X6971ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_three_layers(self):
        rows = self.payload["layer_exclusions"]
        self.assertEqual([row["central_dimension"] for row in rows], [71, 70, 69])
        self.assertEqual(
            [row["six_term_shortening_dimension"] for row in rows],
            [51, 50, 49],
        )
        self.assertEqual([row["product_shadow_minimum"] for row in rows], [78, 75, 75])
        self.assertTrue(all(row["excluded"] for row in rows))

    def test_same_three_packets(self):
        for row in self.payload["layer_exclusions"]:
            self.assertEqual(row["scalar_state_count"], 21)
            self.assertEqual(row["existing_cap_excluded_count"], 18)
            self.assertEqual(row["remaining_packet_count_before_shortening"], 3)
            self.assertEqual(row["selected_six_permanent_relation_cap"], 75)

    def test_flag_hook_interface(self):
        common = self.payload["common_equality_consequence"]
        self.assertTrue(all(common.values()))

    def test_strict_boundary(self):
        self.assertEqual(self.payload["updated_residual_seven_set_upper"], 68)
        self.assertIn("x_A<=68", self.payload["strict_conclusion"])
        self.assertIn("global b=34 remain open", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
