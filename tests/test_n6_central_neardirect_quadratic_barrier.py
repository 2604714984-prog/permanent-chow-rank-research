from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_central_neardirect_quadratic_barrier.py"
FROZEN = ROOT / "data" / "n6_central_neardirect_quadratic_barrier.json"
SPEC = importlib.util.spec_from_file_location(
    "n6_central_neardirect_quadratic_barrier", SCRIPT
)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class CentralNeardirectQuadraticBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_relation_dimensions(self) -> None:
        rows = self.payload["degree_rows"]
        self.assertEqual(
            [row["ordinary_relation_dimension_kappa"] for row in rows],
            [1, 0, 0],
        )
        self.assertEqual(
            [row["literal_sum_dimension"] for row in rows],
            [29, 40, 30],
        )

    def test_exact_coupled_ranks(self) -> None:
        self.assertEqual(
            [row["coupled_derivative_rank_of_TA_plus_TB"] for row in self.payload["degree_rows"]],
            [29, 40, 29],
        )

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
