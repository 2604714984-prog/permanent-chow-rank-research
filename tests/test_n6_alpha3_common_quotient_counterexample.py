from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_common_quotient_counterexample.py"
FROZEN = ROOT / "data" / "n6_alpha3_common_quotient_counterexample.json"
SPEC = importlib.util.spec_from_file_location("n6_alpha3_common_W_counterexample", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class AlphaThreeCommonQuotientCounterexampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_exact_quadratic_data(self) -> None:
        row = self.payload["coupled_quadratic_data"]
        self.assertTrue(row["six_F_literal_direct"])
        self.assertEqual((row["d2"], row["a2"], row["t2"]), (90, 75, 15))
        self.assertEqual(row["pairwise_F_intersection_dimension"], 0)

    def test_exact_cubic_boundary(self) -> None:
        row = self.payload["coupled_cubic_data"]
        self.assertEqual((row["h"], row["b"]), (120, 0))
        self.assertEqual(row["required_b_in_residual_state"], 60)

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
