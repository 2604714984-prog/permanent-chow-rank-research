import json
import unittest
from pathlib import Path

from scripts.n7_lower51_no_basis_two_plane import build


ROOT = Path(__file__).resolve().parents[1]


class Lower51NoBasisTwoPlaneTest(unittest.TestCase):
    def test_frozen_payload(self):
        expected = json.loads(
            (ROOT / "data/n7_lower51_no_basis_two_plane.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(build(), expected)

    def test_only_intrinsic_or_swapping(self):
        rows = build()["rows"]
        self.assertEqual(
            [row["second_plane_quotient_rank"] for row in rows if row["allowed"]],
            [1, 6],
        )
        self.assertEqual(build()["intrinsic_role_geometry"]["intersection_dimension"], 0)
        self.assertEqual(build()["swapping_role_geometry"]["intersection_dimension"], 5)


if __name__ == "__main__":
    unittest.main()
