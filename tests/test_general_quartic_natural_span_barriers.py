from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_natural_span_barriers.py"
DATA = ROOT / "data" / "general_quartic_natural_span_barriers.json"

spec = importlib.util.spec_from_file_location("quartic_natural_span", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class QuarticNaturalSpanBarrierTests(unittest.TestCase):
    def test_laplace_basis_partitions_permanent_support(self) -> None:
        basis = module.laplace_22_basis()
        self.assertEqual(len(basis), 6)
        self.assertEqual(sum(len(value) for value in basis.values()), 24)
        self.assertEqual(len(set().union(*basis.values())), 24)

    def test_laplace_essential_floor(self) -> None:
        audit = module.audit_laplace_span()
        self.assertEqual(audit["minimum_nonzero_essential_dimension"], 8)
        self.assertEqual(
            audit["essential_dimension_distribution"],
            {"8": 6, "12": 12, "14": 8, "16": 37},
        )

    def test_glynn_sign_tensors_are_a_basis(self) -> None:
        audit = module.audit_glynn_span()
        self.assertEqual(audit["basis_size"], 8)
        self.assertEqual(audit["walsh_rank"], 8)
        self.assertEqual(audit["low_essential_line_count"], 8)

    def test_unique_glynn_coefficients_are_nonzero(self) -> None:
        audit = module.audit_glynn_span()
        self.assertTrue(audit["all_glynn_coefficients_nonzero"])
        self.assertEqual(len(audit["glynn_coefficients"]), 8)
        self.assertTrue(
            all(value not in {"0", "0/1"} for value in audit["glynn_coefficients"])
        )

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text())
        self.assertEqual(module.payload(), expected)


if __name__ == "__main__":
    unittest.main()
