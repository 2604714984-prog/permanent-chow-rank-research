from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b48_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b48_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b48_equality", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ProductShadowB48EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_coordinate_classification_counts_and_unique_parent(self):
        fixed = self.payload["coordinate_fixed_points"]
        self.assertEqual(fixed["minimum_first_product_shadow"], 75)
        self.assertEqual(len(fixed["minimizing_ferrers_profiles"]), 8)
        self.assertEqual(fixed["labelled_fifty_hook_count"], 720)
        self.assertEqual(fixed["deletion_pairs_per_parent"], 1225)
        self.assertEqual(fixed["distinct_coordinate_equality_support_count"], 882_000)
        self.assertTrue(
            fixed[
                "every_coordinate_equality_support_is_a_two_cell_deletion_from_a_fifty_hook"
            ]
        )
        self.assertTrue(fixed["every_coordinate_equality_support_has_a_unique_fifty_hook_parent"])
        self.assertEqual(fixed["minimum_parent_lift_multiplicity"], 4)
        self.assertTrue(fixed["deleting_any_two_parent_cells_preserves_the_75_shadow"])
        self.assertTrue(fixed["coordinate_prolongation_of_each_parent_shadow_is_the_parent"])
        self.assertEqual(sum(row["count"] for row in fixed["profile_counts"]), 882_000)

    def test_small_equalities_and_thirty_six_stabilizer_orbits(self):
        fixed = self.payload["coordinate_fixed_points"]
        self.assertTrue(
            all(
                row["all_are_cliques_with_the_required_number_of_deletions"]
                for row in fixed["small_one_factor_equality_replay"].values()
            )
        )
        self.assertTrue(
            all(fixed["families_of_sizes_18_19_20_have_full_pair_shadow"].values())
        )
        self.assertEqual(fixed["stabilizer_orbit_count"], 36)
        self.assertEqual(len(fixed["stabilizer_orbits"]), 36)
        for orientation in ("row_hook", "transpose_hook"):
            self.assertEqual(
                sum(
                    row["orbit_size_within_standard_parent"]
                    for row in fixed["stabilizer_orbits"]
                    if row["orientation"] == orientation
                ),
                1225,
            )
        self.assertEqual(
            {row["deletion_type"]: row["stabilizer_orbit_count"] for row in fixed["deletion_type_counts"]},
            {
                "AA_full_row": 7,
                "AB_full_and_ordinary": 6,
                "BB_same_ordinary_row": 2,
                "BB_distinct_ordinary_rows": 3,
                "HH_same_high_row": 2,
                "HH_distinct_high_rows": 8,
                "HL_high_and_low": 6,
                "LL_two_low_rows": 2,
            },
        )

    def test_all_thirty_six_linear_certificates(self):
        rows = self.payload["local_orbit_certificates"]
        self.assertEqual(len(rows), 36)
        for row in rows:
            self.assertEqual(row["coordinate_prolongation"]["weight_count"], 50)
            self.assertTrue(
                row["coordinate_prolongation"]["is_the_unique_fifty_hook_parent"]
            )
            linear = row["linear_incidence"]
            self.assertEqual(linear["free_dimension"], 112)
            self.assertEqual(linear["parent_linear_dimension"], 16)
            self.assertEqual(linear["relative_grassmannian_dimension"], 96)
            self.assertEqual(linear["eta_only_root_count"], 0)
            self.assertTrue(linear["parent_and_relative_coordinates_are_disjoint"])
            self.assertEqual(linear["full_parent_plus_relative_jacobian_rank"], 112)

    def test_all_thirty_six_grounded_quadratic_certificates(self):
        for row in self.payload["local_orbit_certificates"]:
            quadratic = row["grounded_quadratic_initial_forms"]
            self.assertEqual(quadratic["parent_group_sizes"], [3, 4, 4, 5])
            self.assertEqual(quadratic["forbidden_unit_count"], 25)
            self.assertEqual(quadratic["exact_rank_over_Q"], 25)
            self.assertEqual(quadratic["raw_non_forbidden_monomial_count"], 0)
            self.assertEqual(quadratic["missing_forbidden_monomial_count"], 0)
            self.assertEqual(quadratic["raw_relative_monomial_count"], 0)
            self.assertTrue(
                quadratic["row_span_is_exactly_the_twenty_five_forbidden_units"]
            )

    def test_relative_branches_formal_germ_and_globalization(self):
        for row in self.payload["local_orbit_certificates"]:
            branches = row["relative_boolean_branches"]
            self.assertEqual(branches["count"], 240)
            self.assertEqual(branches["dimension"], 100)
            self.assertTrue(branches["n6064_boolean_jacobian_is_exact_4_by_4_identity"])
            self.assertTrue(
                branches["tautological_grassmannian_chart_jacobian_is_96_by_96_identity"]
            )
            self.assertTrue(branches["replayed_free_coordinate_sets_are_disjoint"])
            self.assertEqual(branches["combined_block_jacobian_rank"], 100)
        formal = self.payload["formal_germ"]
        self.assertTrue(formal["initial_ideal_is_parent_J_extended_by_96_smooth_variables"])
        self.assertTrue(formal["complete_formal_germ_is_union_of_relative_boolean_branches"])
        globalized = self.payload["projective_globalization"]
        self.assertTrue(
            globalized[
                "every_48_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"
            ]
        )
        self.assertEqual(globalized["second_shadow_dimension"], 23)
        self.assertTrue(globalized["second_shadow_is_a_projective_flag_hook"])

    def test_json_keys_are_strings(self):
        def visit(value):
            if isinstance(value, dict):
                self.assertTrue(all(isinstance(key, str) for key in value))
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)

        visit(self.payload)


if __name__ == "__main__":
    unittest.main()
