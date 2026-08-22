from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_squarefree_coproduct_colored_barrier.py"
FROZEN = ROOT / "data" / "n6_squarefree_coproduct_colored_barrier.json"
SPEC = importlib.util.spec_from_file_location("n6_squarefree_coproduct_barrier", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class SquarefreeCoproductColoredBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_all_subset_caps(self) -> None:
        rows = self.payload["by_color_count"]
        expected_maxima = [0, 0, 0, 18, 34, 50]
        self.assertEqual(
            [
                rows[str(q)]["maximum_rational_kernel_dimension_upper_bound"]
                for q in range(1, 7)
            ],
            expected_maxima,
        )
        self.assertTrue(
            all(
                rows[str(q)]["maximum_rational_kernel_dimension_upper_bound"]
                <= rows[str(q)]["b50_subset_cap"]
                for q in range(1, 7)
            )
        )

    def test_full_kernel_is_fifty(self) -> None:
        row = self.payload["by_color_count"]["6"]
        self.assertEqual(
            row["rational_kernel_dimension_upper_bounds_in_lexicographic_subset_order"],
            [50],
        )
        self.assertEqual(self.payload["exact_rank_certificate"]["full_rank_over_Q"], 70)

    def test_fixed_parameters_and_all_subsets(self) -> None:
        self.assertEqual(len(self.payload["fixed_parameters"]["six_diagonals"]), 6)
        self.assertEqual(len(self.payload["fixed_parameters"]["five_shears"]), 5)
        self.assertEqual(len(self.payload["all_subset_rows"]), 63)
        self.assertTrue(self.payload["fixed_parameters"]["each_q_i_is_invertible_over_Q"])

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
