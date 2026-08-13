from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b47_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b47_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("g052_b47_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class ProductShadowB47EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_profiles_and_generated_family(self) -> None:
        self.assertEqual(self.payload["ferrers_minimum_first_shadow"], 75)
        self.assertEqual(self.payload["ferrers_minimizing_profile_count"], 14)
        row = self.payload["coordinate_fixed_points"]
        self.assertEqual((row["deletions_per_parent"], row["distinct_coordinate_equality_support_count"], row["stabilizer_orbit_count"]), (19600, 14112000, 224))
        self.assertTrue(row["every_coordinate_equality_support_is_a_three_cell_deletion_from_a_fifty_hook"])

    def test_all_orbit_linear_and_quadratic_signatures(self) -> None:
        self.assertEqual(self.payload["linear_signature_histogram"], [{
            "free_dimension": 157,
            "parent_linear_dimension": 16,
            "relative_Gr_47_50_dimension": 141,
            "eta_only_root_count": 0,
            "parent_plus_relative_rank": 157,
            "orbit_count": 224,
        }])
        rows = self.payload["quadratic_signature_histogram"]
        self.assertEqual(sum(row["orbit_count"] for row in rows), 224)
        self.assertEqual({row["exact_forbidden_unit_rank"] for row in rows}, {25})
        self.assertEqual({row["raw_relative_monomial_count"] for row in rows}, {0})

    def test_formal_germ_and_globalization(self) -> None:
        formal = self.payload["formal_germ"]
        self.assertEqual((formal["free_dimension"], formal["relative_Gr_47_50_dimension"], formal["relative_boolean_branch_dimension"]), (157, 141, 145))
        self.assertTrue(formal["completed_local_scheme_is_the_union_of_the_240_relative_branches"])
        global_row = self.payload["projective_globalization"]
        self.assertTrue(global_row["every_47_plane_with_first_shadow_75_extends_to_a_50_plane_with_first_shadow_75"])
        self.assertEqual(global_row["second_shadow_dimension"], 23)

    def test_boundary_is_exact(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not treat the dimension-46", boundary)
        self.assertIn("does not by itself prove ChowRank(perm_6)>=29", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()
