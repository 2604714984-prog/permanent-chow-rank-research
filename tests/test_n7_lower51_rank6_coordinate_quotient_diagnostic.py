import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Lower51RankSixCoordinateDiagnosticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(
            (ROOT / "data/n7_lower51_rank6_coordinate_quotient_diagnostic.json").read_text(
                encoding="utf-8"
            )
        )

    def test_bounded_scope(self):
        self.assertEqual(self.payload["candidate_coordinate_quotients"], 384)
        self.assertIn("do not prove arbitrary-orientation", self.payload["claim_boundary"])

    def test_exact_R0_rows(self):
        rows = {
            row["support_size"]: [
                cell["minimum_R0_surplus"] for cell in row["quotient_rows"]
            ]
            for row in self.payload["rows"]
        }
        self.assertEqual(rows[1], [10, 25, 29, 26, 19, 10, 0])
        self.assertEqual(rows[6], [0, 25, 35, 35, 29, 20, 10])

    def test_endpoint_consistency(self):
        endpoints = json.loads(
            (ROOT / "data/n7_lower51_rank6_endpoint_atoms.json").read_text(
                encoding="utf-8"
            )
        )
        diagnostic = {row["support_size"]: row for row in self.payload["rows"]}
        for endpoint in endpoints["rows"]:
            cells = diagnostic[endpoint["support_size"]]["quotient_rows"]
            self.assertEqual(cells[0]["minimum_R0_surplus"], endpoint["increment_zero_surplus"])
            self.assertEqual(cells[6]["minimum_R0_surplus"], endpoint["increment_six_surplus"])


if __name__ == "__main__":
    unittest.main()
