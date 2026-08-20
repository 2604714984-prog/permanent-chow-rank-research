from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower49_complementary_catalectic.py"
SPEC = importlib.util.spec_from_file_location("n7_lower49_complementary_catalectic", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower49ComplementaryCatalectic(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_degree_six_shadow_boundary(self) -> None:
        row = self.payload["degree_six_section"]
        self.assertEqual(row["input_shadow_budget"], 405)
        self.assertEqual(row["capacity"], 33)
        self.assertEqual(row["witness_shadow"], 405)
        self.assertEqual(row["next_area_minimum_shadow"], 411)

    def test_complementary_catalectic_gap(self) -> None:
        row = self.payload["chosen_route"]
        self.assertEqual(row["degree_six_intersection_cap"], 33)
        self.assertEqual(row["residual_catalectic_rank_lower_bound"], 16)
        self.assertEqual(row["remaining_terms_lower_bound"], 3)
        self.assertEqual(row["total_terms_lower_bound"], 49)

    def test_unique_selected_size(self) -> None:
        self.assertEqual(self.payload["best_total_lower_bound"], 49)
        self.assertEqual(self.payload["maximizers"], [self.payload["chosen_route"]])
        self.assertEqual(self.payload["chosen_route"]["selected_terms"], 46)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower49_complementary_catalectic.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
