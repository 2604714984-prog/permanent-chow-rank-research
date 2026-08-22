from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_permutation_monomial_quotient_audit.py"
FROZEN = ROOT / "data" / "n6_two_permutation_monomial_quotient_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_two_permutation_monomial_quotient_audit", SCRIPT)


class N6TwoPermutationMonomialQuotientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_permanent_and_cycle_type_counts(self) -> None:
        self.assertEqual(self.payload["permanent_weight_block_count"], 5625)
        self.assertEqual(self.payload["permanent_koszul_rank_over_Q"], 14175)
        self.assertEqual(self.payload["relative_cycle_type_count"], 11)

    def test_exact_two_output_span_ranks(self) -> None:
        rows = self.payload["cycle_types"]
        self.assertEqual(
            [row["ordinary_two_output_span_rank_over_Q"] for row in rows],
            [705, 1267, 1374] + [1410] * 8,
        )
        self.assertEqual(
            [row["internal_output_relation_dimension_eta"] for row in rows],
            [705, 143, 36] + [0] * 8,
        )

    def test_all_aggregate_collisions_vanish(self) -> None:
        self.assertTrue(self.payload["all_aggregate_collision_dimensions_zero"])
        for row in self.payload["cycle_types"]:
            self.assertEqual(row["aggregate_collision_dimension_j"], 0)
            self.assertEqual(
                row["ordinary_two_output_span_rank_over_Q"],
                row["quotient_two_output_span_rank_over_Q"],
            )

    def test_scope_is_restricted(self) -> None:
        self.assertIn("permutation-monomial", self.payload["scope"])
        self.assertIn("does not control", self.payload["scope"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
