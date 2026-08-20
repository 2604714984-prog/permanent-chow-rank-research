import json
import unittest
from pathlib import Path

from scripts.n6_common_column_mix_k32_rigidity import build_payload


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "n6_common_column_mix_k32_rigidity.json"


class CommonColumnMixK32RigidityTest(unittest.TestCase):
    def test_frozen_payload(self):
        self.assertEqual(build_payload(), json.loads(DATA.read_text(encoding="utf-8")))

    def test_rank_formula_examples(self):
        rows = build_payload()["exact_examples"]["examples"]
        self.assertEqual([row["cross_rank"] for row in rows], [6, 6, 9, 9])
        self.assertTrue(all(row["mixed_rank"] == 3 for row in rows))

    def test_symbolic_certificate(self):
        symbolic = build_payload()["symbolic_certificate"]
        self.assertEqual(symbolic["mixed_generic_rank"], 3)
        self.assertEqual(symbolic["same_generic_rank"], 6)
        self.assertIn("a*c=0", symbolic["same_rank_condition"])


if __name__ == "__main__":
    unittest.main()
