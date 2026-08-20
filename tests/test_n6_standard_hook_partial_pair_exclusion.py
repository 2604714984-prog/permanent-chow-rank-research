from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_standard_hook_partial_pair_exclusion.py"
FROZEN = ROOT / "data" / "n6_standard_hook_partial_pair_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_standard_hook_partial", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6StandardHookPartialPairExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_coordinate_threshold_has_only_forty_three_product_points(self) -> None:
        coordinate = self.payload["coordinate_threshold_thirteen"]
        self.assertEqual(coordinate["coordinate_twelve_plane_count"], 1_352_078)
        self.assertEqual(coordinate["threshold_thirteen_fixed_point_count"], 43)
        self.assertTrue(
            coordinate["no_coordinate_values_thirteen_fourteen_sixteen_seventeen"]
        )

    def test_coordinate_threshold_orbit_compression_is_complete(self) -> None:
        _, _, representatives, represented = AUDIT.coordinate_threshold_orbits()
        self.assertEqual(representatives, 18_513)
        self.assertEqual(represented, AUDIT.comb(23, 12))

    def test_all_five_relative_normal_leakage_gaps_are_strict(self) -> None:
        rows = self.payload["relative_normal_leakage_certificates"]
        self.assertEqual([row["kernel_dimension"] for row in rows], [2, 11, 8, 7, 6])
        self.assertEqual(
            [row["minimum_nonproduct_fixed_weight_leakage_rank"] for row in rows],
            [5, 6, 6, 6, 6],
        )
        self.assertTrue(all(row["kernel_equals_product_tangent"] for row in rows))

    def test_nonlinear_corners_are_exact_products(self) -> None:
        rows = self.payload["nonlinear_product_corner_certificates"]
        self.assertEqual([row["compatible_corner_defects"] for row in rows], [12, 12])
        self.assertEqual([row["missing_corner_products"] for row in rows], [12, 0])
        for row in rows:
            self.assertTrue(all(rank == 6 for rank in row["compatible_corner_defect_ranks"]))
            self.assertTrue(all(rank == 6 for rank in row["missing_corner_product_ranks"]))

    def test_partial_two_row_lemmas_have_strict_dimension_gaps(self) -> None:
        partial = self.payload["partial_two_row_rigidity"]
        multiplier = partial["multiplier_projective_fixed_ranks"]
        self.assertEqual(multiplier["minimum_non_scalar_diagonal_rank"], 5)
        self.assertEqual(multiplier["off_diagonal_matrix_unit_rank_set"], [5])
        self.assertEqual(partial["invertible_member"]["coordinate_thirteen_planes"], 105)
        self.assertEqual(partial["ratio_algebra"]["maximum"], 12)
        self.assertEqual(partial["ratio_algebra"]["required_Q_dimension"], 13)

    def test_standard_hook_kappa_one_and_two_are_excluded(self) -> None:
        application = self.payload["a2_72_standard_hook_application"]
        self.assertEqual(application["newly_excluded_kappa2_values"], [1, 2])
        self.assertTrue(application["complementary_relation_graph_connected"])
        self.assertIn("divisible by 6", application["final_contradiction"])

    def test_boundary_is_explicit(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("kappa2=0", boundary)
        self.assertIn("73,74,75", boundary)
        self.assertIn("lower 29", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
