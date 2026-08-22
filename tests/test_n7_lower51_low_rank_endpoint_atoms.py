import json
import unittest
from pathlib import Path

from scripts.n7_lower51_low_rank_endpoint_atoms import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51LowRankEndpointAtomsTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_low_rank_endpoint_atoms.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(build(), expected)

    def test_minimum_middle_and_full_cost(self):
        rows = build()["rows"]
        self.assertEqual([row["minimum_middle_dimension"] for row in rows],
                         [1, 2, 4, 8, 15])
        self.assertEqual([row["full_increment_surplus_floor"] for row in rows],
                         [26, 17, 9, 3, 0])

    def test_pair_floor_rank_filter(self):
        floor = build()["pair_span_floor"]
        impossible_rank_pairs = [(1, 1), (1, 2), (1, 3), (2, 2)]
        self.assertTrue(all(left + right < floor for left, right in impossible_rank_pairs))


if __name__ == "__main__":
    unittest.main()
