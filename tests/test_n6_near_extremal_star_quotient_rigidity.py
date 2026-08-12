from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_near_extremal_star_quotient_rigidity.py"
FROZEN = ROOT / "data" / "n6_near_extremal_star_quotient_rigidity.json"
SPEC = importlib.util.spec_from_file_location("n6_star_quotient_rigidity", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NearExtremalStarQuotientRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload,
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_exact_qq_standard_family(self) -> None:
        replay = self.payload["exact_qq_regression"]
        self.assertEqual(replay["standard_support_case_count"], 16)
        self.assertEqual(replay["distinct_quotient_spaces"], 16)
        self.assertEqual(replay["full_quadratic_dimensions"], [15])
        self.assertEqual(replay["quotient_dimensions"], [13])
        self.assertEqual(
            replay["pairwise_quotient_intersection_histogram"],
            {"5": 78, "7": 42},
        )
        self.assertEqual(
            replay["pairwise_full_intersection_histogram"],
            {"4": 78, "6": 42},
        )

    def test_state_contingent_counts(self) -> None:
        rows = self.payload["state_contingent_sublocus_counts"]
        self.assertEqual(
            [
                (
                    row["b"],
                    row["all_canonical_scalar_states"],
                    row["states_with_at_least_two_epsilon0_alpha1_entries"],
                    row["selected_t2_histogram"],
                )
                for row in rows
            ],
            [
                (61, 73, 37, {"13": 22, "14": 15}),
                (62, 11, 5, {"13": 5}),
                (63, 11, 5, {"13": 5}),
            ],
        )

    def test_claim_boundary_is_conditional(self) -> None:
        boundary = self.payload["strict_boundary"]
        self.assertIn("do not exclude complete scalar states", boundary)
        self.assertIn("general alpha-one component", boundary)


if __name__ == "__main__":
    unittest.main()
