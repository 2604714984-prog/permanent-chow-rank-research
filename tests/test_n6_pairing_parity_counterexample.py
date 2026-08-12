from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_pairing_parity_counterexample.py"
FROZEN = ROOT / "data" / "n6_pairing_parity_counterexample.json"
SPEC = importlib.util.spec_from_file_location("n6_pairing_parity_counterexample", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class PairingParityCounterexampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_unique_relation(self) -> None:
        row = self.payload["middle_derivative_data"]
        self.assertEqual(row["individual_ranks"], [20, 20])
        self.assertEqual(row["sum_of_spaces_dimension"], 39)
        self.assertEqual(row["intersection_dimension"], 1)
        self.assertEqual(row["relation_dimension"], 1)
        self.assertTrue(row["explicit_relation_residual_is_zero"])

    def test_nonisotropic_pairing_and_direct_rank(self) -> None:
        pairing = self.payload["relation_pairing"]
        self.assertEqual(pairing["total_value"], -24)
        self.assertEqual(pairing["restricted_pairing_rank"], 1)
        self.assertTrue(pairing["relation_is_nonisotropic"])
        self.assertEqual(self.payload["direct_middle_catalectic_rank_of_T1_plus_T2"], 39)

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
