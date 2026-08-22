import json
import unittest
from pathlib import Path

from scripts.n7_lower51_rank7_full_block_control import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSevenFullBlockControlTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_rank7_full_block_control.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(build(), expected)

    def test_parallel_count(self):
        payload = build()
        self.assertEqual(payload["maximum_parallel_nonbasis"], 7)
        self.assertEqual(payload["minimum_nonparallel_nonbasis"], 36)
        self.assertLess(payload["common_plane_span"], payload["three_label_span_floor"])


if __name__ == "__main__":
    unittest.main()
