import json
import unittest
from pathlib import Path

from scripts.n7_lower51_rank6_endpoint_atoms import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSixEndpointAtomsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(
            (ROOT / "data/n7_rank6_normal_form_profiles.json").read_text(
                encoding="utf-8"
            )
        )

    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_rank6_endpoint_atoms.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(build(self.source), expected)

    def test_dual_endpoint_rows(self):
        rows = build(self.source)["rows"]
        self.assertEqual([row["increment_zero_surplus"] for row in rows],
                         [10, 10, 4, 1, 0, 0])
        self.assertEqual([row["increment_six_surplus"] for row in rows],
                         [0, 0, 6, 9, 10, 10])


if __name__ == "__main__":
    unittest.main()
