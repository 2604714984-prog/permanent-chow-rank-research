import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b46_equality_locus.py"
DATA = ROOT / "data" / "n6_product_shadow_b46_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6101", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProductShadowB46EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_coordinate_classification(self):
        coordinate = self.payload["coordinate_fixed_points"]
        self.assertEqual(coordinate["minimum_first_product_shadow"], 72)
        self.assertEqual(coordinate["coordinate_model_count"], 7200)
        self.assertEqual(coordinate["coordinate_symmetry_orbit_count"], 4)
        self.assertEqual({row["count"] for row in coordinate["profile_counts"]}, {1800})

    def test_linear_and_quadratic_signatures(self):
        rows = self.payload["local_orbit_certificates"]
        self.assertEqual({row["linear_free_dimension"] for row in rows}, {20})
        self.assertEqual({row["eta_only_root_count"] for row in rows}, {0})
        self.assertEqual(
            Counter(row["quadratic_initial"]["edge_generator_count"] for row in rows),
            {31: 2, 32: 2},
        )

    def test_all_symbolic_branch_orbits(self):
        rows = self.payload["local_orbit_certificates"]
        self.assertEqual(
            Counter(row["maximal_independent_facet_count"] for row in rows),
            {900: 2, 960: 2},
        )
        self.assertTrue(
            all(
                row["all_orbit_representative_branches_pass_both_symbolic_containments"]
                and row["all_orbit_representative_branch_jacobians_are_identity_5_by_5"]
                for row in rows
            )
        )

    def test_second_shadow_shapes(self):
        rows = self.payload["local_orbit_certificates"]
        self.assertEqual(
            {row["coordinate_second_shadow_flag_shape"] for row in rows},
            {
                "standard_flag_hook",
                "transpose_standard_flag_hook",
                "biflag_rectangle_hook",
                "transpose_biflag_rectangle_hook",
            },
        )
        self.assertEqual(
            self.payload["projective_globalization"][
                "every_46_plane_with_first_shadow_72_has_second_shadow_dimension"
            ],
            23,
        )

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
