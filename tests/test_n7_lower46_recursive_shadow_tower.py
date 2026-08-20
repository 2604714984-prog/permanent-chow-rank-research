from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower46_recursive_shadow_tower.py"
SPEC = importlib.util.spec_from_file_location("n7_lower46_recursive_shadow_tower", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower46RecursiveShadowTower(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_recursive_local_caps(self) -> None:
        tower = self.payload["recursive_shadow_tower"]
        self.assertEqual(tower["two_term_quadratic_section"]["capacity"], 22)
        self.assertEqual(tower["five_term_quadratic_section_cap"], 85)
        self.assertEqual(tower["five_term_cubic_section"]["capacity"], 64)
        self.assertEqual(tower["twenty_term_cubic_section_cap"], 589)
        self.assertEqual(tower["twenty_term_degree_four_section"]["capacity"], 341)

    def test_critical_witnesses(self) -> None:
        tower = self.payload["recursive_shadow_tower"]
        self.assertEqual(tower["two_term_quadratic_section"]["witness_shadow"], 14)
        self.assertEqual(tower["five_term_cubic_section"]["witness_shadow"], 84)
        self.assertEqual(tower["twenty_term_degree_four_section"]["witness_shadow"], 586)

    def test_unique_recursive_maximizer(self) -> None:
        scan = self.payload["full_recursive_scan"]
        self.assertEqual(scan["triple_count"], 7_770)
        self.assertEqual(scan["best_total_lower_bound"], 46)
        self.assertEqual(
            scan["maximizers"],
            [{
                "selected_terms": 20,
                "local_cubic_terms": 5,
                "inner_quadratic_terms": 2,
                "total_terms_lower_bound": 46,
            }],
        )

    def test_final_koszul_gap(self) -> None:
        self.assertEqual(self.payload["koszul_residual_rank_lower_bound"], 42_091)
        self.assertEqual(self.payload["twenty_five_term_koszul_capacity"], 42_000)
        self.assertGreater(
            self.payload["koszul_residual_rank_lower_bound"],
            self.payload["twenty_five_term_koszul_capacity"],
        )
        self.assertEqual(self.payload["chosen_route"]["total_terms_lower_bound"], 46)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower46_recursive_shadow_tower.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
