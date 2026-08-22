from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_squarefree_gradient_simultaneous_waring.py"
SPEC = importlib.util.spec_from_file_location("n7_squarefree_gradient_simultaneous_waring", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N7SquarefreeGradientSimultaneousWaringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_colon_length(self) -> None:
        section = self.payload["coordinate_colon_section"]
        self.assertEqual(section["standard_monomial_hilbert_vector"], [1, 6, 15, 20, 15, 6, 0])
        self.assertEqual(section["standard_monomial_count"], 63)

    def test_glynn_upper_bound(self) -> None:
        self.assertTrue(self.payload["glynn_identity_check"]["identity_verified"])
        self.assertEqual(self.payload["simultaneous_waring"]["strict_interval"], [63, 64])

    def test_endpoint_boundary(self) -> None:
        consequence = self.payload["endpoint_consequence"]
        self.assertTrue(consequence["excluded"])
        self.assertEqual(consequence["scope"], "column-uniform/tensor-split endpoint only")

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_squarefree_gradient_simultaneous_waring.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
