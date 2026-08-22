import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b73_76_equality_locus.py"
DATA = ROOT / "data" / "n6_product_shadow_b73_76_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6090_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6ProductShadowB7376EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_coordinate_plateau(self):
        rows = self.payload["coordinate_fixed_points"]["dimensions"]
        self.assertEqual([row["dimension"] for row in rows], [73, 74, 75, 76])
        self.assertTrue(all(row["minimum_first_product_shadow"] == 90 for row in rows))
        self.assertEqual([row["minimizing_ferrers_profile_count"] for row in rows], [22, 18, 12, 10])
        self.assertTrue(
            self.payload["coordinate_fixed_points"][
                "johnson_J_6_3_remains_connected_after_any_seven_vertex_deletions"
            ]
        )

    def test_uniform_linear_stability(self):
        linear = self.payload["uniform_linear_stability"]
        self.assertEqual(linear["restricted_tangent_vertex_cut_for_each_parent_component"], [8] * 8)
        self.assertEqual(linear["grounded_eta_source_witness_histogram"], {"8": 11790})
        self.assertEqual(
            linear["complete_linear_dimensions"],
            {"73": 519, "74": 452, "75": 383, "76": 312},
        )

    def test_uniform_quadratic_stability(self):
        quadratic = self.payload["uniform_quadratic_stability"]
        self.assertEqual(quadratic["forbidden_generator_count"], 12)
        self.assertEqual(quadratic["distinct_source_support_histogram_per_forbidden_generator"], {"40": 12})
        self.assertEqual(quadratic["potential_relative_variable_grounded_monomial_count"], 0)
        self.assertEqual(quadratic["grounded_equation_with_an_inside_parent_outside_count"], 0)

    def test_global_extension_and_boundary(self):
        global_ = self.payload["projective_globalization"]
        self.assertTrue(global_["every_73_to_76_plane_with_first_shadow_90_extends_to_an_80_plane_with_the_same_shadow"])
        self.assertEqual(global_["every_equality_plane_has_second_shadow_dimension"], 24)
        self.assertIn("does not treat dimension 72", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
