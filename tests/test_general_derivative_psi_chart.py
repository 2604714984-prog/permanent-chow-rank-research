from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_derivative_psi_chart_audit.py"

SPEC = importlib.util.spec_from_file_location("general_derivative_psi", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the derivative-degree psi-chart audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class GeneralDerivativePsiChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.rows = {
            (row["n"], row["degree_m"]): row
            for row in cls.payload["replayed_cases"]
        }

    def test_selected_cases(self) -> None:
        self.assertEqual(set(self.rows), set(AUDIT.CASES))

    def test_full_and_relative_dimensions(self) -> None:
        for (n, degree), row in self.rows.items():
            expected = AUDIT.comb(n, degree + 1) ** 2
            self.assertEqual(row["full_prolongation_nullity"], expected)
            self.assertEqual(
                row["coordinate_relative_prolongation_nullity"],
                expected + 1,
            )

    def test_n6_middle_degree_chart(self) -> None:
        row = self.rows[(6, 3)]
        self.assertEqual(row["permanent_derivative_dimension"], 400)
        self.assertEqual(row["full_prolongation_nullity"], 225)
        self.assertEqual(row["coordinate_relative_prolongation_nullity"], 226)
        self.assertEqual(row["base_first_koszul_rank"], 14_175)
        self.assertEqual(row["one_new_direction_gain"], 35)
        self.assertEqual(row["extended_first_koszul_rank_lower"], 14_210)

    def test_claim_boundary(self) -> None:
        self.assertIn(
            "does not make several quotient gains additive",
            self.payload["claim_boundary"],
        )

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (
                ROOT / "data" / "general_derivative_psi_chart_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
