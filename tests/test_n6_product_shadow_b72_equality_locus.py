import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b72_equality_locus.py"
DATA = ROOT / "data" / "n6_product_shadow_b72_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6092_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6ProductShadowB72EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_coordinate_classification(self):
        fixed = self.payload["coordinate_fixed_points"]
        self.assertEqual(fixed["minimum_first_product_shadow"], 89)
        self.assertEqual(fixed["coordinate_fixed_point_count"], 2700)
        self.assertTrue(fixed["every_coordinate_equality_support_has_a_unique_product_parent"])

    def test_linear_and_quadratic_germ(self):
        local = self.payload["standard_local_certificate"]
        self.assertEqual(local["linear_incidence"]["free_dimension"], 20)
        self.assertEqual(local["grounded_quadratic_initial_forms"]["group_sizes_in_symbolic_order"], [4, 4, 2, 2, 4, 4])
        self.assertEqual(local["grounded_quadratic_initial_forms"]["exact_rank_over_Q"], 26)

    def test_symbolic_branches(self):
        branches = self.payload["standard_local_certificate"]["symbolic_boolean_branches"]
        self.assertEqual((branches["count"], branches["dimension"]), (1024, 6))
        self.assertTrue(branches["all_degree_three_to_two_containments_hold"])
        self.assertTrue(branches["all_degree_two_to_one_containments_hold"])

    def test_globalization_and_boundary(self):
        global_ = self.payload["projective_globalization"]
        self.assertTrue(global_["every_72_to_89_point_lies_in_a_partitioned_80_to_90_product_parent"])
        self.assertEqual(global_["every_equality_point_has_second_shadow_dimension"], 24)
        self.assertIn("need not be ambient linear transports", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
