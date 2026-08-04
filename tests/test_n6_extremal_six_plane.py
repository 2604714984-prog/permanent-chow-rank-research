from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_extremal_six_plane_audit.py"
FROZEN = ROOT / "data" / "n6_extremal_six_plane.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_extremal_six_plane_audit",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load extremal six-plane audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6ExtremalSixPlaneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_unimodular_rank_chart_and_exact_tangent_rank(self) -> None:
        self.assertEqual(self.payload["pivot_minor_determinant"], 1)
        self.assertEqual(self.payload["base_rank"], 18)
        self.assertEqual(self.payload["base_kernel_dimension"], 3)
        self.assertEqual(self.payload["grassmann_chart_dimension"], 180)
        self.assertEqual(self.payload["jacobian_rank_mod_prime"], 163)
        self.assertEqual(
            self.payload["explicit_characteristic_zero_kernel_dimension"],
            17,
        )
        self.assertEqual(
            self.payload["characteristic_zero_jacobian_rank"],
            163,
        )

    def test_second_order_obstructions_are_exactly_disjoint_support(self) -> None:
        second = self.payload["second_order"]
        self.assertEqual(second["bad_monomial_count"], 13)
        self.assertEqual(second["good_monomial_count"], 140)
        self.assertEqual(second["obstruction_rank_mod_prime"], 13)
        self.assertTrue(
            second["all_good_quadratic_monomials_have_integral_corrections"]
        )

        labels = {
            (tuple(row["first"]), tuple(row["second"]))
            for row in second["bad_monomials"]
        }
        expected = {
            (("row", 0, target), ("row", 1, target))
            for target in range(2, 6)
        }
        expected.update(
            {
                (("column", first, target), ("column", second, target))
                for target in range(3, 6)
                for first, second in ((0, 1), (0, 2), (1, 2))
            }
        )
        self.assertEqual(labels, expected)

    def test_local_and_global_component_counts(self) -> None:
        initial = self.payload["squarefree_initial_ideal"]
        self.assertEqual(initial["generators"], 13)
        self.assertEqual(initial["dimension"], 7)
        self.assertEqual(initial["minimal_primes"], 432)
        self.assertEqual(initial["multiplicity"], 432)
        self.assertEqual(self.payload["classified_local_branches"], 432)

        global_components = self.payload["global_support_components"]
        self.assertEqual(global_components["stirling_6_2"], 31)
        self.assertEqual(global_components["stirling_6_3"], 90)
        self.assertEqual(global_components["row_2_column_3"], 2790)
        self.assertEqual(global_components["row_3_column_2"], 2790)
        self.assertEqual(global_components["total"], 5580)
        self.assertEqual(global_components["dimension_each"], 7)

    def test_frozen_certificate_matches_live_replay(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_claim_boundary_remains_fail_closed(self) -> None:
        self.assertIn("local", self.payload["claim_boundary"])
        self.assertIn("proof note", self.payload["claim_boundary"])
        self.assertNotIn("ChowRank(perm_6)=32", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
