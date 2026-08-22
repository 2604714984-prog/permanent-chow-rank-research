import json
import unittest
from pathlib import Path

from scripts.n6_k32_average_relative_germ import build_payload


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_k32_average_relative_germ.json"


class K32AverageRelativeGermTest(unittest.TestCase):
    def test_frozen_payload(self):
        self.assertEqual(build_payload(), json.loads(DATA.read_text(encoding="utf-8")))

    def test_full_jacobian(self):
        certificate = build_payload()["exact_certificate"]
        self.assertEqual(certificate["base_cross_rank"], 6)
        self.assertEqual(certificate["jacobian_rank"], 70)
        self.assertEqual(certificate["tangent_dimension"], 2)
        self.assertEqual(certificate["normal_minor_determinant"], -70368744177664)

    def test_average_is_absent(self):
        certificate = build_payload()["exact_certificate"]
        self.assertEqual(
            certificate["nullspace_generators"],
            ["relative_column_0_scaling", "relative_column_1_scaling"],
        )
        self.assertEqual(
            [row["cross_rank"] for row in build_payload()["examples"]["diagonal_relative_family"]],
            [6, 6, 6],
        )


if __name__ == "__main__":
    unittest.main()
