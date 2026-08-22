from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower51_rank5_binary_equality.py"
SPEC = importlib.util.spec_from_file_location("n7_lower51_rank5_binary_equality", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RankFiveBinaryEqualityTests(unittest.TestCase):
    def test_symbolic_rank_split(self) -> None:
        payload = MODULE.build()
        self.assertEqual(payload["diagonal_binary_tail_rank"], 15)
        self.assertEqual(payload["second_equality_component_sample_rank"], 15)
        self.assertEqual(payload["pure_cross_tail_rank"], 18)
        self.assertEqual(payload["generic_binary_tail_rank"], 18)
        self.assertEqual(payload["binary_middle_determinant"], "8*c*(9*a*b-2*c^2)")
        self.assertEqual(payload["ternary_middle_matrix_shape"], [6, 10])
        self.assertGreater(payload["nonzero_five_minor_polynomials"], 0)
        self.assertEqual(payload["non_equality_middle_lower_bound"], 18)
        self.assertEqual(payload["non_equality_full_increment_surplus_floor"], 3)
        self.assertEqual(len(payload["equality_orbit_types"]), 3)


if __name__ == "__main__":
    unittest.main()
