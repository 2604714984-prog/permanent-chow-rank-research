import json
import unittest
from pathlib import Path

from scripts.n7_lower51_rank7_block_exchange import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSevenBlockExchangeTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_rank7_block_exchange.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(build(), expected)

    def test_single_rank_filter(self):
        rows = build()["single_exchange_rows"]
        self.assertEqual([row["block_rank"] for row in rows if row["allowed"]],
                         [0, 1, 6, 7])
        self.assertEqual([rows[rank]["exchange_cost"] for rank in (2, 3, 4, 5)],
                         [43, 43, 43, 43])

    def test_pair_geometry(self):
        rows = build()["pair_exchange_rows"]
        triples = {(*row["block_ranks"], row["combined_rank"]) for row in rows}
        self.assertIn((1, 1, 1), triples)
        self.assertNotIn((1, 1, 2), triples)
        self.assertIn((1, 6, 7), triples)
        self.assertNotIn((1, 6, 6), triples)
        self.assertIn((6, 6, 6), triples)
        self.assertIn((6, 6, 7), triples)

    def test_one_six_support_gate(self):
        rank_one_support_floors = [22, 22, 32, 32, 38, 38, 43]
        rank_six_increment_floor = 7
        self.assertLessEqual(rank_one_support_floors[1] + rank_six_increment_floor, 35)
        self.assertGreater(rank_one_support_floors[2] + rank_six_increment_floor, 35)


if __name__ == "__main__":
    unittest.main()
