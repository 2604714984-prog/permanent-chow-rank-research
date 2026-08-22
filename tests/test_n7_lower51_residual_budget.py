import json
import unittest
from pathlib import Path

from scripts.n7_lower51_residual_budget import build, residual_cap


ROOT = Path(__file__).resolve().parents[1]


class Lower51ResidualBudgetTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_residual_budget.json").read_text(encoding="utf-8")
        )
        self.assertEqual(build(), expected)

    def test_endpoint_controls(self):
        payload = build()
        self.assertEqual(payload["all_rank7_50_residual_cap"], 35)
        self.assertEqual(payload["mixed_50_minimum_profile_residual_cap"], 35)
        self.assertEqual(payload["mixed_49_endpoint_residual_cap"], 0)

    def test_symbolic_mixed_identity(self):
        for basis_cost in range(36):
            for outside_cost in range(36 - basis_cost):
                basis_middle = 210 + basis_cost
                sum_all = basis_middle + 42 * 35 - outside_cost
                self.assertEqual(
                    residual_cap(sum_all, basis_middle),
                    35 - basis_cost - outside_cost,
                )


if __name__ == "__main__":
    unittest.main()
