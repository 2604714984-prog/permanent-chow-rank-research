from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower26_average_subset_audit.py"

SPEC = importlib.util.spec_from_file_location("n6_lower26_average_subset", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the average-subset audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6Lower26AverageSubsetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_average_selects_central_rank_at_least_82(self) -> None:
        self.assertEqual(self.payload["total_relation_pairing_floor"], 340)
        self.assertEqual(self.payload["uniform_six_subset_average_floor"], "408/5")
        self.assertEqual(
            self.payload["selected_six_central_rank_lower_bound"],
            82,
        )
        self.assertEqual(
            self.payload["residual_forced_intersection_lower_bound"],
            51,
        )

    def test_every_high_intersection_layer_is_strict(self) -> None:
        layers = self.payload["fixed_six_central_exclusion_layers"]
        self.assertEqual([row["b"] for row in layers], list(range(51, 65)))
        self.assertTrue(
            all(
                row["central_rank_lower_bound"]
                > row["residual_central_rank_upper_bound"]
                for row in layers
            )
        )
        self.assertEqual(
            [row["central_rank_lower_bound"] for row in layers],
            [88, 88, 92, 96, 98, 98, 100, 110, 112, 112, 116, 118, 118, 120],
        )

    def test_shadow_cutoff(self) -> None:
        cutoff = self.payload["shadow_cutoff"]
        self.assertEqual(cutoff["first_excluded_b"], 65)
        self.assertEqual(cutoff["shadow_lower_bound"], 79)
        self.assertEqual(cutoff["quadratic_projection_cap"], 78)

    def test_claim_boundary(self) -> None:
        conclusion = self.payload["conclusion"]
        self.assertEqual(conclusion["ordinary_chow_rank_interval"], [26, 32])
        self.assertIn("does not prove border", self.payload["claim_boundary"])
        self.assertIn("does not determine", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
