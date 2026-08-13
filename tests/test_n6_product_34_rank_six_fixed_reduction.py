from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_34_rank_six_fixed_reduction.py"
DATA = ROOT / "data" / "n6_product_34_rank_six_fixed_reduction.json"
SPEC = importlib.util.spec_from_file_location("n6_product_34_rank_six", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class N6Product34RankSixFixedReductionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text())

    def test_coordinate_rank_six_classification(self) -> None:
        coordinate = self.payload["coordinate_classification"]
        self.assertEqual(coordinate["ordered_coordinate_pair_count"], 853_776)
        self.assertEqual(coordinate["rank_distribution"], {"3": 18, "5": 72, "6": 2424})
        self.assertEqual(coordinate["rank_six_orbit_count"], 20)
        self.assertEqual(coordinate["coordinate_complementary_rank_six_pair_count"], 0)
        self.assertEqual(
            sum(row["orbit_size"] for row in coordinate["rank_six_orbits"]),
            2424,
        )

    def test_common_two_row_stratum_is_normal_rigid(self) -> None:
        common = self.payload["common_two_row_stratum"]
        self.assertEqual(common["representative_orbit_count"], 18)
        self.assertEqual(common["ordered_fixed_pair_count"], 2268)
        self.assertEqual(common["internal_graph_variable_count"], 24)
        self.assertEqual(common["normal_graph_variable_count"], 48)
        self.assertEqual(common["normal_linear_rank_histogram"], {"48": 18})
        self.assertEqual(common["internal_linear_rank_histogram"], {"0": 18})
        self.assertTrue(common["formal_germ_is_contained_in_the_fixed_eight_space"])

    def test_diagonal_411_replays_quickly(self) -> None:
        replay = MODULE.diagonal_411_certificate()
        frozen = self.payload["diagonal_411_stratum"]
        self.assertEqual(replay, frozen)
        self.assertEqual(replay["exact_QQ_rank"], 69)
        self.assertEqual(replay["difference_variable_rank"], 36)
        self.assertTrue(replay["formal_swap_uniqueness_forces_L_equals_M"])

    def test_staircase_quadratic_and_weight_obstruction(self) -> None:
        staircase = self.payload["diagonal_321_staircase_stratum"]
        self.assertEqual(staircase["exact_linear_rank"], 61)
        self.assertEqual(staircase["exact_tangent_nullity"], 11)
        self.assertEqual(staircase["diagonal_tangent_dimension"], 9)
        self.assertEqual(staircase["separating_tangent_dimension"], 2)
        self.assertEqual(staircase["quadratic_cokernel_rank"], 20)
        self.assertEqual(
            staircase["quadratic_generator_weight_block_size_histogram"],
            {"1": 12, "2": 4},
        )
        self.assertEqual(
            staircase["facet_dimension_histogram"], {"3": 2, "4": 2, "5": 5}
        )
        self.assertTrue(
            staircase[
                "no_surviving_tangent_monomial_has_the_complement_determinant_weight"
            ]
        )
        self.assertTrue(
            staircase["complement_determinant_vanishes_in_the_completed_local_ring"]
        )

    def test_scope_is_strict(self) -> None:
        self.assertEqual(
            self.payload["status"],
            "EXACT_RANK_SIX_FIXED_STRATUM_COMPLEMENT_EXCLUSION",
        )
        conclusion = self.payload["projective_conclusion"]
        self.assertTrue(
            conclusion[
                "a_complementary_rank_at_most_six_component_must_specialize_to_rank_three_or_five"
            ]
        )
        boundary = self.payload["boundary"]
        self.assertIn("rank-three or rank-five", boundary)
        self.assertIn("does not yet exclude every", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
