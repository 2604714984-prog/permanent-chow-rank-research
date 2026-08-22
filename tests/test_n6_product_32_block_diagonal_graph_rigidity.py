import json
import unittest
from pathlib import Path

from scripts import n6_product_32_block_diagonal_graph_rigidity as cert


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_product_32_block_diagonal_graph_rigidity.json"


class Product32BlockDiagonalGraphRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_commutator_kernel(self) -> None:
        row = self.payload["commutator_scalar_lemma"]
        self.assertEqual(row["coefficient_matrix_shape"], [27, 9])
        self.assertEqual(row["exact_QQ_rank"], 8)
        self.assertEqual(row["exact_QQ_nullity"], 1)
        self.assertEqual(row["kernel_generator"], "identity_3")

    def test_examples(self) -> None:
        rows = self.payload["exact_examples"]["examples"]
        self.assertEqual(rows[0]["cross_rank_over_QQ"], 6)
        self.assertTrue(all(row["cross_rank_over_QQ"] > 6 for row in rows[1:]))

    def test_bounded_f3_screen(self) -> None:
        row = self.payload["finite_field_row_twist_screen"]
        self.assertEqual(row["candidate_count"], 19_683)
        self.assertEqual(row["invertible_matrix_count"], 12_792)
        self.assertEqual(row["rank_at_most_six_count"], 2)
        self.assertTrue(row["not_used_for_characteristic_zero_proof"])

    def test_boundary(self) -> None:
        missing = self.payload["boundary"]["not_proved"]
        self.assertIn(
            "the average-relative and non-graph charts of the full K23/K32 rank-six formal germ",
            missing,
        )

    def test_frozen_replay(self) -> None:
        self.assertEqual(cert.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
