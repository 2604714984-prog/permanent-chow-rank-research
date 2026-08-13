from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_all_singular_true_quotient_screen.py"
FROZEN = ROOT / "data" / "n6_all_singular_true_quotient_screen.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_all_singular_screen", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class AllSingularTrueQuotientScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_true_quotient_csp_is_empty_in_all_four_cycle_types(self):
        self.assertEqual(self.payload["ambient_quotient_axis_count"], 441)
        self.assertEqual(
            [row["common_true_quotient_pairs"]
             for row in self.payload["csp_screens"].values()],
            [0, 0, 0, 0],
        )

    def test_all_1848_coordinate_splits_are_screened(self):
        self.assertEqual(self.payload["coordinate_splits_tested_total"], 1848)
        self.assertTrue(all(
            row["common_true_quotient_splits"] == 0
            for row in self.payload["coordinate_split_screens"].values()
        ))

    def test_wedge_axes_remove_a_diagonal_only_false_positive(self):
        guard = self.payload["diagonal_only_false_positive_guard"]
        self.assertEqual(guard["diagonal_projections_equal_out_of_15"], 15)
        self.assertEqual(guard["nonzero_diagonal_equal_out_of_15"], 1)
        self.assertEqual(guard["full_diag_plus_wedge_lines_equal_out_of_15"], 2)

    def test_claim_is_strictly_bounded(self):
        self.assertIn("FINITE_FIELD_BOUNDED_DIAGNOSTIC", self.payload["status"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("not a characteristic-zero theorem", boundary)
        self.assertIn("does not exclude the b=50 endpoint", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=28", boundary)


if __name__ == "__main__":
    unittest.main()
