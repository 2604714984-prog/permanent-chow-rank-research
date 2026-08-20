from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower47_dual_koszul_shadow_tower.py"
SPEC = importlib.util.spec_from_file_location("n7_lower47_dual_koszul_shadow_tower", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Lower47DualKoszulShadowTower(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_recursive_degree_five_cap(self) -> None:
        self.assertEqual(self.payload["degree_five_section_cap_for_46_terms"], 405)
        self.assertEqual(
            [(row["degree"], row["terms"], row["local_terms"]) for row in self.payload["recursive_degree_five_trace"]],
            [(5, 46, 42), (4, 42, 20), (3, 20, 5), (2, 5, 2)],
        )

    def test_degree_five_ferrers_boundary(self) -> None:
        row = self.payload["degree_five_critical_shadow"]
        self.assertEqual(row["budget"], 1_111)
        self.assertEqual(row["capacity"], 321)
        self.assertEqual(row["witness_shadow"], 1_105)
        self.assertEqual(row["next_area_minimum_shadow"], 1_113)

    def test_correct_dual_degree_scan(self) -> None:
        scan = self.payload["correct_dual_koszul_scan"]
        self.assertEqual([row["koszul_degree"] for row in scan], [2, 3, 4, 5, 6])
        self.assertEqual([row["dual_catalectic_degree"] for row in scan], [5, 4, 3, 2, 1])
        self.assertEqual([row["best_total_lower_bound"] for row in scan], [47, 46, 46, 46, 46])

    def test_strict_residual(self) -> None:
        chosen = self.payload["chosen_koszul_degree_two_route"]
        self.assertEqual(chosen["selected_terms"], 46)
        self.assertEqual(chosen["dual_intersection_cap"], 405)
        self.assertEqual(chosen["residual_rank_lower_bound"], 539)
        self.assertEqual(chosen["remaining_terms_lower_bound"], 1)
        self.assertEqual(chosen["total_terms_lower_bound"], 47)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower47_dual_koszul_shadow_tower.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
