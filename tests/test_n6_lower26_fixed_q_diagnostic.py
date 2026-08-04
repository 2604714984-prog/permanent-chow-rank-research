from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower26_fixed_q_diagnostic.py"
FROZEN = ROOT / "data" / "n6_lower26_fixed_q_diagnostic.json"

SPEC = importlib.util.spec_from_file_location("n6_lower26_fixed_q", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load fixed-q diagnostic")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6Lower26FixedQDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.full = AUDIT.build_full_payload()
        cls.compact = AUDIT.compact_payload(cls.full)
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.compact, self.frozen)

    def test_exact_summary_counts(self) -> None:
        rows = {
            row["fixed_terms"]: row
            for row in self.compact["fixed_q_summaries"]
        }
        expected = {
            6: (1_035, 708, 327, 3, 55, 269),
            7: (1_225, 870, 355, 3, 62, 290),
            8: (1_520, 885, 635, 1, 50, 584),
        }
        for fixed_terms, values in expected.items():
            row = rows[fixed_terms]
            observed = (
                row["initial_state_count"],
                row["vector_macaulay_central_excluded_state_count"],
                row["state_count_after_central_pruning"],
                row["quotient_koszul_already_strict_state_count"],
                row["relative_prolongation_state_count"],
                row["structural_state_count"],
            )
            self.assertEqual(observed, values, fixed_terms)

    def test_shadow_endpoints(self) -> None:
        rows = {
            row["fixed_terms"]: row
            for row in self.compact["fixed_q_summaries"]
        }
        self.assertEqual(rows[6]["central_intersection_range"], [20, 64])
        self.assertEqual(rows[6]["first_shadow_excluded_lower_bound"], 79)
        self.assertEqual(rows[7]["central_intersection_range"], [40, 88])
        self.assertEqual(rows[7]["first_shadow_excluded_lower_bound"], 94)
        self.assertEqual(rows[8]["central_intersection_range"], [60, 114])
        self.assertEqual(rows[8]["first_shadow_excluded_lower_bound"], 109)

    def test_route_is_fail_closed(self) -> None:
        decision = self.compact["route_decision"]
        self.assertEqual(decision["arithmetically_smallest_fixed_count"], 6)
        self.assertIsNone(decision["selected_for_proof_program"])
        self.assertIn("does not exclude", self.compact["claim_boundary"])

    def test_partition_interface_ranges(self) -> None:
        rows = {
            row["fixed_terms"]: row
            for row in self.compact["fixed_q_summaries"]
        }
        self.assertEqual(
            rows[6]["module_partition_identity_verified_through"],
            37,
        )
        self.assertEqual(
            rows[7]["module_partition_identity_verified_through"],
            33,
        )
        self.assertEqual(
            rows[8]["module_partition_identity_verified_through"],
            33,
        )


if __name__ == "__main__":
    unittest.main()
