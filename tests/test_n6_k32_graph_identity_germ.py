import json
import unittest
from pathlib import Path

from scripts.n6_k32_graph_identity_germ import build_payload


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_k32_graph_identity_germ.json"


class K32GraphIdentityGermTest(unittest.TestCase):
    def test_frozen_payload(self):
        self.assertEqual(build_payload(), json.loads(DATA.read_text(encoding="utf-8")))

    def test_exact_jacobian(self):
        certificate = build_payload()["exact_certificate"]
        self.assertEqual(certificate["base_cross_rank"], 6)
        self.assertEqual(certificate["jacobian_rank"], 34)
        self.assertEqual(certificate["normal_minor_determinant"], -256)
        self.assertEqual(certificate["tangent_dimension"], 2)

    def test_diagonal_family(self):
        rows = build_payload()["diagonal_examples"]["examples"]
        self.assertEqual([row["cross_rank"] for row in rows], [6, 6, 6])
        self.assertEqual(
            build_payload()["exact_certificate"]["diagonal_schur_identically_zero"],
            True,
        )


if __name__ == "__main__":
    unittest.main()
