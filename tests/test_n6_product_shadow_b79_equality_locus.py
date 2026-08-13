from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b79_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b79_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6084_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ProductShadowB79EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_coordinate_unique_parent(self) -> None:
        row = self.payload["coordinate_fixed_points"]
        self.assertEqual((row["minimum_first_product_shadow"], row["distinct_coordinate_79_plane_count"]), (90, 2400))
        self.assertEqual(row["parent_multiplicity_histogram"], {"1": 2400})

    def test_local_relative_factor(self) -> None:
        for row in self.payload["local_representatives"]:
            linear = row["linear_incidence"]
            self.assertEqual((linear["free_dimension"], linear["parent_linear_dimension"], linear["relative_hyperplane_dimension"]), (87, 8, 79))
            self.assertEqual(row["grounded_quadratic_initial_forms"]["exact_rank_over_Q"], 12)
            self.assertEqual((row["relative_boolean_branches"]["count"], row["relative_boolean_branches"]["dimension"]), (16, 81))

    def test_global_extension_and_boundary(self) -> None:
        row = self.payload["projective_globalization"]
        self.assertTrue(row["every_79_to_90_plane_extends_to_an_80_to_90_plane_with_the_same_90_shadow"])
        self.assertEqual(row["every_79_to_90_plane_has_second_shadow_dimension_24"], True)
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not classify 78-planes", boundary)
        self.assertIn("does not exclude global b=34", boundary)


if __name__ == "__main__":
    unittest.main()
