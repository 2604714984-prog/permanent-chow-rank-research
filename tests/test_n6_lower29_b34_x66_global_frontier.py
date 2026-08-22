import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x66_global_frontier.py"
DATA = ROOT / "data" / "n6_lower29_b34_x66_global_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6100_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Lower29B34X66GlobalFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_global_equalities(self):
        row = self.payload["hereditary_seven_set_equality"]
        self.assertEqual(row["global_central_space_dimension"], 366)
        self.assertEqual(row["therefore_every_literal_seven_set_intersection_dimension"], 66)
        self.assertEqual(row["every_fifteen_term_literal_sum_dimension"], 300)
        self.assertTrue(row["every_at_most_fifteen_term_family_is_literal_direct"])

    def test_thirteen_state_frontier(self):
        row = self.payload["forced_local_frontier"]
        self.assertEqual(row["N6_080_relation_state_count"], 56)
        self.assertEqual(row["N6_080_old_cap_excluded_count"], 43)
        self.assertEqual(row["open_exact_state_count"], 13)

    def test_critical_six_set(self):
        row = self.payload["critical_six_shortening"]
        self.assertEqual(row["therefore_selected_six_intersection_dimension"], 46)
        self.assertEqual(row["selected_six_product_shadow_dimension_range"], [72, 75])
        self.assertEqual(row["complementary_sixteen_term_literal_sum_dimension"], 320)
        self.assertTrue(row["complementary_sixteen_terms_are_literal_direct"])

    def test_boundary(self):
        self.assertIn("first unresolved b=34 layer", self.payload["strict_conclusion"])
        self.assertIn("not an exclusion of b=34", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
