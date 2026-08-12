from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b50_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b50_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b50_equality", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ProductShadowB50EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_linear_and_quadratic_certificates(self):
        self.assertEqual(self.payload["linear_incidence"]["free_group_sizes"], [3, 4, 4, 5])
        quadratic = self.payload["quadratic_elimination"]
        self.assertEqual(quadratic["matrix_shape"], [1140, 136])
        self.assertEqual(quadratic["rank_over_Q"], 25)
        self.assertTrue(quadratic["rref_is_exactly_the_forbidden_unit_vectors"])

    def test_all_symbolic_branches_and_jacobians(self):
        branches = self.payload["boolean_shear_branches"]
        self.assertEqual(branches["count"], 240)
        self.assertTrue(branches["all_first_shadow_symbolic_containments_hold"])
        self.assertTrue(branches["all_second_shadow_symbolic_containments_hold"])
        self.assertTrue(branches["all_selected_chart_jacobians_are_identity"])

    def test_transpose_and_second_shadow(self):
        self.assertEqual(self.payload["transpose_hook"]["free_group_sizes"], [3, 4, 4, 5])
        self.assertEqual(self.payload["second_product_shadow"]["universal_minimum_at_dimension_75"], 23)
        self.assertEqual(self.payload["second_product_shadow"]["equality_branch_second_shadow_dimension"], 23)


if __name__ == "__main__":
    unittest.main()
