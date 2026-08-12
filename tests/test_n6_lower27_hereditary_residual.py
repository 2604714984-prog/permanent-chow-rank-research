from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower27_hereditary_residual_audit.py"

SPEC = importlib.util.spec_from_file_location("n6_lower27_hereditary", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the hereditary-residual audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6Lower27HereditaryResidualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_maximum_single_term_rank_is_twenty(self) -> None:
        self.assertEqual(
            self.payload["maximum_individual_middle_rank_forced"],
            20,
        )
        branches = self.payload["low_maximum_rank_branches"]
        self.assertEqual(
            [branch["maximum_individual_middle_rank"] for branch in branches],
            [17, 18],
        )
        self.assertTrue(
            all(
                branch["shadow_lower"]
                > branch["fixed_six_quadratic_projection_cap"]
                for branch in branches
            )
        )

    def test_high_intersection_layers_force_residual_384(self) -> None:
        layers = self.payload["fixed_six_high_layer_table"]
        self.assertEqual([row["b"] for row in layers], list(range(52, 65)))
        self.assertTrue(all(row["margin"] >= 0 for row in layers))
        self.assertEqual(
            self.payload["twenty_term_residual_middle_rank_lower"],
            384,
        )

    def test_hereditary_strict_middle_certificates(self) -> None:
        rows = self.payload["hereditary_subset_middle_rank_bounds"]
        self.assertEqual([row["subset_size"] for row in rows], list(range(1, 21)))
        self.assertTrue(all(row["strict_margin"] == 4 for row in rows))
        self.assertEqual(
            self.payload["twenty_term_residual_exact_chow_rank"],
            20,
        )
        self.assertEqual(
            self.payload["minimum_number_of_full_middle_rank_residual_terms"],
            12,
        )

    def test_residual_incidence_window(self) -> None:
        self.assertEqual(
            self.payload["residual_permanent_middle_intersection_window"],
            [336, 380],
        )
        self.assertEqual(
            self.payload["residual_literal_quotient_dimension_window"],
            [20, 64],
        )
        self.assertEqual(
            self.payload["residual_colored_relations_mod_permanent_lower"],
            320,
        )

    def test_claim_boundary(self) -> None:
        self.assertIn(
            "does not prove ChowRank(perm_6)>=27",
            self.payload["claim_boundary"],
        )

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (
                ROOT
                / "data"
                / "n6_lower27_hereditary_residual_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
