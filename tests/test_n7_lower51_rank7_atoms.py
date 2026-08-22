import json
import unittest
from pathlib import Path

from scripts.n7_lower51_rank7_atoms import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSevenAtomsTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_rank7_atoms.json").read_text(encoding="utf-8")
        )
        self.assertEqual(build(), expected)

    def test_support_jump(self):
        rows = {row["support_size"]: row for row in build()["rank_one_support_rows"]}
        self.assertEqual([rows[s]["rank_one_surplus_floor"] for s in range(1, 8)],
                         [22, 22, 32, 32, 38, 38, 43])
        self.assertGreater(rows[3]["rank_one_surplus_floor"] + 7, 35)

    def test_unique_profile(self):
        self.assertEqual(build()["unique_eight_positive_profile"],
                         [1, 6, 7, 7, 7, 7, 7, 7])


if __name__ == "__main__":
    unittest.main()
