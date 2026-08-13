from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b49_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b49_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b49_equality", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ProductShadowB49EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_coordinate_classification_and_unique_parent(self):
        fixed = self.payload["coordinate_fixed_points"]
        self.assertEqual(fixed["minimum_first_product_shadow"], 75)
        self.assertEqual(len(fixed["minimizing_ferrers_profiles"]), 4)
        self.assertEqual(fixed["labelled_fifty_hook_count"], 720)
        self.assertEqual(fixed["distinct_coordinate_equality_support_count"], 36_000)
        self.assertEqual(fixed["parent_multiplicity_histogram"], {"1": 36_000})
        self.assertTrue(
            all(
                fixed[
                    "all_small_equality_families_have_the_claimed_clique_or_one_deletion_form"
                ].values()
            )
        )
        self.assertEqual(
            {tuple(row["profile"]): row["count"] for row in fixed["profile_counts"]},
            {
                (20, 10, 10, 9) + (0,) * 16: 10_800,
                (19, 10, 10, 10) + (0,) * 16: 7_200,
                (4,) * 9 + (3,) + (1,) * 10: 14_400,
                (4,) * 10 + (1,) * 9 + (0,): 3_600,
            },
        )

    def test_four_exact_linear_eliminations(self):
        rows = self.payload["local_representatives"]
        self.assertEqual(len(rows), 4)
        for row in rows:
            linear = row["linear_incidence"]
            self.assertEqual(linear["free_dimension"], 65)
            self.assertEqual(linear["parent_linear_dimension"], 16)
            self.assertEqual(linear["relative_hyperplane_dimension"], 49)
            self.assertEqual(linear["eta_only_root_count"], 0)
            self.assertEqual(linear["full_parent_plus_hyperplane_jacobian_rank"], 65)
            self.assertEqual(linear["coordinate_prolongation_weight_count"], 50)
            self.assertTrue(linear["coordinate_prolongation_is_the_unique_hook_parent"])

    def test_grounded_quadratic_initial_ideal(self):
        for row in self.payload["local_representatives"]:
            quadratic = row["grounded_quadratic_initial_forms"]
            self.assertEqual(quadratic["parent_group_sizes"], [3, 4, 4, 5])
            self.assertEqual(quadratic["forbidden_unit_count"], 25)
            self.assertEqual(quadratic["exact_rank_over_Q"], 25)
            self.assertEqual(quadratic["raw_non_forbidden_monomial_count"], 0)
            self.assertEqual(quadratic["raw_hyperplane_monomial_count"], 0)
            self.assertTrue(
                quadratic["row_span_is_exactly_the_twenty_five_forbidden_units"]
            )

    def test_relative_branches_formal_germ_and_globalization(self):
        for row in self.payload["local_representatives"]:
            branches = row["relative_boolean_branches"]
            self.assertEqual(branches["count"], 240)
            self.assertEqual(branches["dimension"], 53)
            self.assertTrue(branches["n6064_boolean_jacobian_is_exact_4_by_4_identity"])
            self.assertTrue(
                branches["tautological_hyperplane_chart_jacobian_is_49_by_49_identity"]
            )
            self.assertTrue(branches["replayed_free_coordinate_sets_are_disjoint"])
            self.assertEqual(branches["combined_block_jacobian_rank"], 53)
        formal = self.payload["formal_germ"]
        self.assertTrue(formal["initial_ideal_is_parent_J_extended_by_49_smooth_variables"])
        self.assertTrue(formal["complete_formal_germ_is_union_of_relative_boolean_branches"])
        globalized = self.payload["projective_globalization"]
        self.assertTrue(
            globalized[
                "every_49_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"
            ]
        )
        self.assertEqual(globalized["second_shadow_dimension"], 23)
        self.assertTrue(globalized["second_shadow_is_a_projective_flag_hook"])


if __name__ == "__main__":
    unittest.main()
