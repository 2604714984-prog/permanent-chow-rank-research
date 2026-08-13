from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_shadow11_pair_incidence_diagnostic.py"
FROZEN = ROOT / "data" / "n6_shadow11_pair_incidence_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_shadow11_pair", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ShadowElevenPairIncidenceExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_coordinate_equality_locus_has_two_small_hook_orbits(self) -> None:
        equality = self.payload["equality_support_classification"]
        self.assertEqual(equality["minimum"], 11)
        self.assertEqual(
            equality["minimizing_ferrers_profiles"],
            [
                [6, 3, 3] + [0] * 12,
                [3, 3, 3, 1, 1, 1] + [0] * 9,
            ],
        )
        self.assertEqual(equality["row_oriented_count"], 3600)
        self.assertEqual(equality["transpose_oriented_count"], 3600)
        self.assertEqual(equality["overlap_count"], 0)
        self.assertEqual(equality["coordinate_shadow_histogram"], {"11": 7200})

    def test_coordinate_pair_fixed_points_are_exact(self) -> None:
        scan = self.payload["coordinate_cross_free_scan"]
        self.assertEqual(scan["ordered_five_pair_count"], 213_444)
        self.assertEqual(scan["cross_free_five_pair_count"], 1)
        self.assertEqual(
            scan["cross_free_five_pairs"][0]["intersection_dimension"], 5
        )
        self.assertEqual(scan["cross_free_five_six_pair_count"], 0)
        self.assertEqual(scan["cross_free_six_five_pair_count"], 0)
        self.assertEqual(scan["cross_free_six_pair_count"], 0)

    def test_full_linear_and_quadratic_elimination_is_sharp(self) -> None:
        linear = self.payload["linear_incidence"]
        self.assertEqual(linear["variable_count"], 2891)
        self.assertEqual(linear["derivative_incidence_nullity"], 82)
        self.assertEqual(linear["full_pair_incidence_nullity"], 17)
        self.assertEqual(linear["pair_separation_image_dimension"], 0)
        self.assertEqual(linear["pair_diagonal_image_dimension"], 0)
        self.assertEqual(sorted(linear["free_move_groups"].values()), [3, 3, 3, 4, 4])

        quadratic = self.payload["quadratic_initial_ideal"]
        self.assertEqual(quadratic["quadratic_monomial_count"], 153)
        self.assertEqual(quadratic["obstruction_rank"], 21)
        self.assertEqual(quadratic["expected_same_target_generator_count"], 21)
        self.assertEqual(quadratic["missing_expected_generators"], [])
        self.assertEqual(quadratic["unexpected_obstructed_monomials"], [])
        self.assertEqual(quadratic["radical_facets"], 432)

    def test_all_symbolic_branches_are_exact_and_diagonal(self) -> None:
        branches = self.payload["symbolic_branches"]
        self.assertEqual(branches["branch_count"], 432)
        self.assertEqual(branches["derivative_containment_failures"], 0)
        self.assertEqual(branches["diagonal_cross_free_failures"], 0)
        self.assertEqual(branches["selected_jacobian_failures"], 0)

    def test_kappa_zero_consequence_and_boundary_are_explicit(self) -> None:
        self.assertIn("pairwise transverse", self.payload["kappa_zero_consequence"])
        self.assertIn("23-plane", self.payload["kappa_zero_consequence"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not yet exclude", boundary)
        self.assertIn("lower 29", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
