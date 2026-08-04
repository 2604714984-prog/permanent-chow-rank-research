from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "vector_valued_macaulay_audit.py"
FROZEN = ROOT / "data" / "vector_valued_macaulay_audit.json"

SPEC = importlib.util.spec_from_file_location("vector_valued_macaulay_audit", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load vector-valued Macaulay audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class VectorValuedMacaulayAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_explicit_weights(self) -> None:
        certificate = self.payload["explicit_weight_certificate"]
        self.assertTrue(certificate["all_weights_distinct"])
        self.assertEqual(certificate["colored_quadratic_weight_count"], 3996)

    def test_partition_identity_through_16(self) -> None:
        rows = self.payload["six_color_partition_certificate"]
        self.assertEqual(set(rows), {str(value) for value in range(17)})
        for key, row in rows.items():
            self.assertEqual(
                row["maximum_partition_sum"],
                row["scalar_macaulay_successor"],
                key,
            )

    def test_exhaustive_small_field_diagnostic(self) -> None:
        diagnostic = self.payload["small_field_exhaustive_diagnostic"]
        self.assertEqual(diagnostic["subspace_count"], 2825)
        self.assertFalse(diagnostic["counterexample_found"])
        self.assertEqual(diagnostic["logical_role"], "diagnostic only")

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
