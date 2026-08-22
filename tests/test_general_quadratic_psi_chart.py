from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quadratic_psi_chart_audit.py"

SPEC = importlib.util.spec_from_file_location("general_quadratic_psi", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the general psi-chart audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class GeneralQuadraticPsiChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_full_and_relative_prolongation_dimensions(self) -> None:
        rows = self.payload["replayed_cases"]
        self.assertEqual([row["n"] for row in rows], [3, 4, 5, 6])
        self.assertEqual(
            [row["full_cubic_prolongation_nullity"] for row in rows],
            [1, 16, 100, 400],
        )
        self.assertEqual(
            [row["coordinate_relative_cubic_nullity"] for row in rows],
            [2, 17, 101, 401],
        )

    def test_n4_certificate_is_recovered(self) -> None:
        row = self.payload["replayed_cases"][1]
        self.assertEqual(row["base_quadratic_koszul_rank"], 560)
        self.assertEqual(row["psi_rank"], 99)
        self.assertEqual(row["one_new_quadratic_direction_gain"], 15)
        self.assertEqual(row["extended_quadratic_koszul_rank_lower"], 575)

    def test_n6_generalization(self) -> None:
        row = self.payload["replayed_cases"][3]
        self.assertEqual(row["base_quadratic_koszul_rank"], 7700)
        self.assertEqual(row["psi_source_dimension"], 441)
        self.assertEqual(row["psi_rank"], 440)
        self.assertEqual(row["one_new_quadratic_direction_gain"], 35)
        self.assertEqual(row["extended_quadratic_koszul_rank_lower"], 7735)

    def test_claim_boundary(self) -> None:
        self.assertIn(
            "does not make gains from several directions additive",
            self.payload["claim_boundary"],
        )

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (
                ROOT / "data" / "general_quadratic_psi_chart_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
