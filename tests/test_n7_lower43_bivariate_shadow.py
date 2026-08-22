from __future__ import annotations

import importlib.util
import json
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower43_bivariate_shadow.py"
SPEC = importlib.util.spec_from_file_location("n7_lower43_bivariate_shadow", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower43BivariateShadow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_one_dimensional_table(self) -> None:
        table = self.payload["one_dimensional_shadow_table"]
        self.assertEqual(len(table), math.comb(7, 4) + 1)
        self.assertEqual(table[:8], [0, 4, 7, 9, 10, 10, 13, 15])
        self.assertEqual(table[-4:], [35, 35, 35, 35])

    def test_selected_q_certificate(self) -> None:
        row = self.payload["selected_q_certificate"]
        self.assertEqual(row["selected_terms"], 14)
        self.assertEqual(row["shadow_budget"], 455)
        self.assertEqual(row["intersection_cap"], 238)
        self.assertEqual(row["residual_koszul_rank_lower_bound"], 47_138)
        self.assertEqual(row["remaining_terms_lower_bound"], 29)
        self.assertEqual(row["total_terms_lower_bound"], 43)

    def test_sharp_witness(self) -> None:
        witness = self.payload["sharp_witness"]
        self.assertEqual(witness["area"], 238)
        self.assertEqual(witness["shadow_size"], 452)

    def test_all_q_route_optimization(self) -> None:
        rows = self.payload["all_q_scan"]
        self.assertEqual(len(rows), 35)
        self.assertEqual(max(row["total_terms_lower_bound"] for row in rows), 43)
        self.assertIn(14, self.payload["maximizing_selected_q"])
        self.assertEqual(rows[34]["intersection_cap"], 1085)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower43_bivariate_shadow.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
