from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower45_four_term_shadow.py"
SPEC = importlib.util.spec_from_file_location("n7_lower45_four_term_shadow", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower45FourTermShadow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_local_four_term_cap(self) -> None:
        row = self.payload["local_four_term_shadow"]
        self.assertEqual(row["budget"], 84)
        self.assertEqual(row["capacity"], 64)
        self.assertEqual(row["witness_area"], 64)
        self.assertEqual(row["witness_shadow"], 84)

    def test_global_shadow_cap(self) -> None:
        self.assertEqual(self.payload["nineteen_term_cubic_intersection_cap"], 589)
        row = self.payload["degree_four_shadow"]
        self.assertEqual(row["capacity"], 341)
        self.assertEqual(row["witness_area"], 341)
        self.assertEqual(row["witness_shadow"], 586)

    def test_unique_route_maximizer(self) -> None:
        self.assertEqual(self.payload["best_total_lower_bound_in_this_route"], 45)
        self.assertEqual(self.payload["maximizers"], [self.payload["chosen_route"]])
        self.assertEqual(self.payload["chosen_route"]["selected_terms"], 19)
        self.assertEqual(self.payload["chosen_route"]["local_terms"], 4)

    def test_final_koszul_gap(self) -> None:
        self.assertEqual(self.payload["koszul_residual_rank_lower_bound"], 42_091)
        self.assertGreater(
            self.payload["koszul_residual_rank_lower_bound"],
            self.payload["twenty_five_term_koszul_capacity"],
        )
        self.assertEqual(self.payload["chosen_route"]["remaining_terms_lower_bound"], 26)
        self.assertEqual(self.payload["chosen_route"]["total_terms_lower_bound"], 45)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower45_four_term_shadow.json").read_text(encoding="utf-8")
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
