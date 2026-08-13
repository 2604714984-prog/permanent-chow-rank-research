import json
import unittest
from pathlib import Path

from scripts import n6_product_32_single_cross_tangent_reduction as cert


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_product_32_single_cross_tangent_reduction.json"


class Product32SingleCrossTangentReductionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_exact_linear_layer(self) -> None:
        row = self.payload["local_system"]
        self.assertEqual(row["linear_system_shape"], [360, 72])
        self.assertEqual(row["exact_QQ_linear_rank"], 64)
        self.assertEqual(row["explicit_QQ_kernel_dimension"], 8)

    def test_exact_quadratic_layer(self) -> None:
        row = self.payload["local_system"]
        self.assertEqual(row["quadratic_monomial_count"], 36)
        self.assertEqual(row["quadratic_cokernel_rank_over_QQ"], 7)
        self.assertEqual(len(row["quadratic_initial_generators"]), 7)
        self.assertTrue(row["squarefree_initial_ideal"])

    def test_four_eight_space_facets(self) -> None:
        row = self.payload["local_system"]
        self.assertEqual(len(row["maximal_facets"]), 4)
        self.assertTrue(row["every_facet_moves_inside_a_common_eight_space"])
        self.assertTrue(all(len(item) <= 2 for item in row["facet_extra_coordinate_sets"]))

    def test_boundary(self) -> None:
        missing = self.payload["boundary"]["not_proved"]
        self.assertIn(
            "the completed local germ is contained in the union of the four eight-space incidences",
            missing,
        )

    def test_frozen_replay(self) -> None:
        self.assertEqual(cert.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
