from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower44_pair_shadow.py"
SPEC = importlib.util.spec_from_file_location("n7_lower44_pair_shadow", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower44PairShadow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_pair_shadow_cap(self) -> None:
        pair = self.payload["pair_shadow"]
        self.assertEqual(pair["budget"], 42)
        self.assertEqual(pair["capacity"], 17)
        self.assertEqual(pair["witness_area"], 17)
        self.assertEqual(pair["witness_shadow"], 42)

    def test_eighteen_term_linear_algebra_constant(self) -> None:
        self.assertEqual(self.payload["eighteen_term_intersection_cap"], 577)

    def test_degree_four_shadow_cap(self) -> None:
        row = self.payload["degree_four_shadow"]
        self.assertEqual(row["budget"], 577)
        self.assertEqual(row["capacity"], 332)
        self.assertEqual(row["witness_area"], 332)
        self.assertEqual(row["witness_shadow"], 577)

    def test_final_koszul_gap(self) -> None:
        row = self.payload["koszul"]
        self.assertEqual(row["residual_rank_lower_bound"], 42_532)
        self.assertGreater(row["residual_rank_lower_bound"], row["twenty_five_term_capacity"])
        self.assertEqual(row["remaining_terms_lower_bound"], 26)
        self.assertEqual(row["total_terms_lower_bound"], 44)

    def test_all_selected_q_route(self) -> None:
        rows = self.payload["all_selected_q_pair_route"]
        self.assertEqual(len(rows), 34)
        self.assertEqual(self.payload["best_total_lower_bound_in_pair_route"], 44)
        self.assertEqual(self.payload["maximizing_selected_q"], [17, 18, 27])

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower44_pair_shadow.json").read_text(encoding="utf-8")
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
