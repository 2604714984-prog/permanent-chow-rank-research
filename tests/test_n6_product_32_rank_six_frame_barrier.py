import json
import unittest
from pathlib import Path

from scripts import n6_product_32_rank_six_frame_barrier as cert


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_product_32_rank_six_frame_barrier.json"


class Product32RankSixFrameBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.frozen = json.loads(DATA.read_text(encoding="utf-8"))

    def test_symbolic_column_chart(self) -> None:
        row = cert.column_graph_symbolic_certificate()
        self.assertEqual(row["rank_at_most_two_forces"], ["c=-a", "d=-b"])
        self.assertTrue(row["substitution_kills_every_three_minor"])

    def test_product_block_rank_barrier(self) -> None:
        row = self.frozen["common_A_product_family"]
        self.assertEqual(row["E34_cross_rank"], 6)
        self.assertEqual(row["E34_cross_free_kernel_dimension"], 12)
        self.assertEqual(row["E34_block_projection_rank"], 9)

    def test_tiny_counterexample_screen(self) -> None:
        row = self.frozen["finite_field_counterexample_screen"]
        self.assertEqual(row["grassmannian_point_count"], 130)
        self.assertEqual(row["ordered_pair_count"], 16_900)
        self.assertEqual(row["complementary_cross_rank_at_most_two_count"], 12)
        self.assertTrue(row["not_used_for_characteristic_zero_proof"])

    def test_signed_permutation_counts(self) -> None:
        row = self.frozen["bounded_signed_permutation_scan"]
        self.assertEqual(row["K32"]["candidate_count"], 23_040)
        self.assertEqual(row["K23"]["candidate_count"], 23_040)
        self.assertEqual(len(row["K32_exact_QQ_rank_six_candidates"]), 4)
        self.assertEqual(row["K23"]["modular_rank_six_candidates"], [])

    def test_exact_survivor_projections(self) -> None:
        rows = self.frozen["bounded_signed_permutation_scan"][
            "K32_exact_QQ_rank_six_candidates"
        ]
        for row in rows:
            self.assertEqual(row["ambient_sum_rank_over_QQ"], 12)
            self.assertEqual(row["cross_rank_over_QQ"], 6)
            self.assertEqual(row["cross_free_kernel_dimension"], 12)
            self.assertEqual(row["left_block_projection_rank_over_QQ"], 9)
            self.assertEqual(row["right_block_projection_rank_over_QQ"], 9)

    def test_claim_boundary(self) -> None:
        missing = self.frozen["boundary"]["not_proved"]
        self.assertIn(
            "every complementary K32 rank-six component is a common-A product component",
            missing,
        )
        self.assertIn("ordinary lower 29 or exact ChowRank(perm6)=32", missing)


if __name__ == "__main__":
    unittest.main()
