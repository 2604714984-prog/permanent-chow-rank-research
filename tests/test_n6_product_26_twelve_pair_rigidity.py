from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_26_twelve_pair_rigidity.py"
FROZEN = ROOT / "data" / "n6_product_26_twelve_pair_rigidity.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_product_26_twelve", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Product26TwelvePairRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_multiplier_gap_remains_strict_at_twelve(self) -> None:
        multiplier = self.payload["twelve_plane_multiplier"]
        self.assertEqual(multiplier["rank_allowed_by_codimension_three"], 3)
        self.assertEqual(multiplier["minimum_non_scalar_diagonal_rank"], 5)
        self.assertEqual(multiplier["off_diagonal_matrix_unit_rank_set"], [5])

    def test_every_twelve_plane_contains_an_invertible_member(self) -> None:
        invertible = self.payload["invertible_member"]
        self.assertEqual(invertible["coordinate_twelve_plane_count"], 455)
        self.assertEqual(invertible["perfect_matching_count"], 15)
        self.assertEqual(
            invertible["minimum_surviving_matchings_after_deleting_three_edges"],
            6,
        )

    def test_only_rank_three_invariant_equality_is_reduced(self) -> None:
        invariant = self.payload["proper_invariant_space_locus"]
        self.assertEqual(
            invariant["coordinate_maxima_by_dimension"],
            {"1": 11, "2": 10, "3": 12, "4": 10, "5": 11},
        )
        self.assertEqual(invariant["rank_three_coordinate_equality_pair_count"], 20)
        self.assertTrue(invariant["all_rank_three_fixed_pairs_are_complementary"])
        self.assertEqual(invariant["tangent_rank_over_Q"], 18)
        self.assertEqual(invariant["tangent_nullity"], 0)

    def test_exceptional_ratio_algebra_is_full_parabolic(self) -> None:
        algebra = self.payload["exceptional_ratio_algebra"]
        self.assertEqual(algebra["coordinate_Q_dimension"], 12)
        self.assertEqual(algebra["generated_algebra_dimension"], 27)
        self.assertEqual(
            algebra["full_three_by_three_block_upper_parabolic_dimension"], 27
        )
        self.assertTrue(
            algebra["every_generated_basis_matrix_has_zero_lower_left_block"]
        )

    def test_boundary_is_explicit(self) -> None:
        self.assertIn("L=p tensor k6", self.payload["theorem"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not classify every twelve-plane", boundary)
        self.assertIn("lower 29", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()

