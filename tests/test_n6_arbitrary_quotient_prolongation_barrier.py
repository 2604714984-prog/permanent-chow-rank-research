from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_arbitrary_quotient_prolongation_barrier.py"
FROZEN = ROOT / "data" / "n6_arbitrary_quotient_prolongation_barrier.json"
SPEC = importlib.util.spec_from_file_location("n6_arbitrary_barrier", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class N6ArbitraryQuotientProlongationBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload, json.loads(FROZEN.read_text(encoding="utf-8"))
        )

    def test_exact_475(self) -> None:
        self.assertEqual(self.payload["selected_axis_count"], 13)
        self.assertEqual(self.payload["changed_cubic_weight_block_count"], 75)
        self.assertEqual(self.payload["exact_QQ_prolongation_dimension"], 475)
        self.assertEqual(
            self.payload["modular_regression_prolongation_dimension"], 475
        )
        self.assertEqual(self.payload["strict_excess_over_457"], 18)

    def test_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("not asserted to arise", boundary)
        self.assertIn("does not contradict N6-047", boundary)
        self.assertIn("does not prove", boundary)


if __name__ == "__main__":
    unittest.main()
