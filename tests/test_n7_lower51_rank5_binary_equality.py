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


if __name__ == "__main__":
    unittest.main()
