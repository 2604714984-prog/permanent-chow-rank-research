import json
import unittest
from pathlib import Path

from scripts.n7_lower51_rank6_mixed_count_dp import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSixMixedCountDPTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = build()

    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_rank6_mixed_count_dp.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, expected)

    def test_candidate_cardinality(self):
        self.assertEqual(self.payload["candidate_basis_compositions_before_budget"], 792)
        self.assertEqual(self.payload["surviving_basis_compositions"], 272)
        self.assertEqual(self.payload["compressed_count_patterns"], 11_683_105)

    def test_cost_rows(self):
        self.assertEqual(self.payload["basis_cost_by_support_1_through_6"], [0, 0, 6, 9, 10, 10])
        self.assertEqual(
            self.payload["outside_zero_increment_cost_by_support_1_through_6"],
            [10, 10, 4, 1, 0, 0],
        )


if __name__ == "__main__":
    unittest.main()
