import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_34_rank_five_normal_exclusion.py"
DATA = ROOT / "data" / "n6_product_34_rank_five_normal_exclusion.json"
SPEC = importlib.util.spec_from_file_location("n6_product_34_rank_five", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Product34RankFiveNormalExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frozen = json.loads(DATA.read_text(encoding="utf-8"))

    def test_exact_normal_weight_classification(self):
        rows = self.frozen["rank_five_fixed_orbits"]
        row42 = rows["row_42_diagonal"]
        row33 = rows["row_33_intersection_4"]
        self.assertEqual(row42["normal_weight_group_count"], 20)
        self.assertEqual(row33["normal_weight_group_count"], 26)
        self.assertEqual(
            row42[
                "groups_excluded_because_all_variable_squares_lie_in_the_exact_minor_span"
            ],
            19,
        )
        self.assertEqual(
            row33[
                "groups_excluded_because_all_variable_squares_lie_in_the_exact_minor_span"
            ],
            24,
        )
        self.assertEqual(len(row42["surviving_weight_groups"]), 1)
        self.assertEqual(len(row33["surviving_weight_groups"]), 2)

    def test_characteristic_zero_fixed_points(self):
        rows = self.frozen["rank_five_fixed_orbits"]
        self.assertEqual(
            rows["row_42_diagonal"]["characteristic_zero_fixed_points"],
            [[1, 1, 1, 1], [1, -1, 1, -1]],
        )
        self.assertEqual(
            rows["row_33_intersection_4"]["characteristic_zero_fixed_points"],
            [[1, 1, 1, -1, -1, -1], [1, 1, 1, -1, -1, -1]],
        )

    def test_local_node_certificates(self):
        rows = self.frozen["finite_exceptional_local_models"]
        self.assertEqual(rows["row_42_reduced_point"]["exact_tangent_dimension"], 1)
        for name in ("row_42_node", "row_33_endpoint_node"):
            row = rows[name]
            self.assertEqual(row["exact_QQ_linear_rank"], 69)
            self.assertEqual(row["quadratic_cokernel_rank"], 1)
            self.assertEqual(row["unique_forbidden_monomial"], [1, 2])
            self.assertEqual(
                row["completed_local_ideal"],
                "(x1*x2) after linear elimination",
            )

    def test_symbolic_branches_are_noncomplementary(self):
        rows = self.frozen["exact_symbolic_branch_ranks"]
        self.assertEqual(rows["row42_reduced_point_curve"]["generic_sum_rank"], 6)
        for name in (
            "row42_node_branch",
            "row33_projective_pencil",
            "row33_endpoint_extra_branch",
        ):
            self.assertEqual(rows[name]["generic_cross_rank"], 6)
            self.assertEqual(rows[name]["generic_sum_rank"], 10)

    def test_frozen_payload(self):
        self.assertEqual(MODULE.build_payload(), self.frozen)


if __name__ == "__main__":
    unittest.main()
