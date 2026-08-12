from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_minimum_six_permutation_collision_audit.py"
DATA = ROOT / "data" / "n6_minimum_six_permutation_collision_audit.json"


def load_script():
    spec = importlib.util.spec_from_file_location("minimum_six_collision", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6MinimumSixPermutationCollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_script()
        cls.payload = cls.module.build_payload()

    def test_middle_catalectic_certifies_minimum_six(self) -> None:
        self.assertEqual(
            self.payload["six_term_central_catalectic_rank_over_Q"], 120
        )
        self.assertEqual(self.payload["certificate_minor_absolute_determinant"], 1)
        self.assertEqual(self.payload["exact_chow_rank"], 6)
        self.assertEqual(self.payload["central_relation_dimension_rho"], 0)

    def test_exact_minimum_collision(self) -> None:
        self.assertEqual(self.payload["internal_output_relation_dimension_eta"], 0)
        self.assertEqual(self.payload["aggregate_collision_dimension_j"], 72)
        self.assertEqual(
            self.payload["ordinary_six_output_span_rank_over_Q"], 4_230
        )
        self.assertEqual(
            self.payload["quotient_six_output_span_rank_over_Q"], 4_158
        )
        self.assertTrue(self.payload["explicit_collision_is_full_intersection"])

    def test_central_intersection_misses_lower26_frontier(self) -> None:
        self.assertEqual(
            self.payload["permanent_central_derivative_intersection_dimension_b"],
            2,
        )
        self.assertEqual(
            self.payload["hypothetical_25_term_q6_required_minimum_b"], 20
        )
        self.assertFalse(
            self.payload["compatible_with_q6_central_necessary_condition"]
        )

    def test_all_six_permutation_monomial_fibers_have_b_at_most_two(self) -> None:
        self.assertEqual(
            self.payload["normalized_six_permutation_fibers_checked"], 46_656
        )
        self.assertEqual(
            self.payload["normalized_fiber_intersection_histogram"],
            {"1": 45_936, "2": 720},
        )
        self.assertEqual(
            self.payload["general_six_permutation_monomial_intersection_cap_b"],
            2,
        )
        self.assertEqual(
            self.payload["enumeration_role"],
            "independent exact diagnostic, not a theorem premise",
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)

    def test_scope_is_fail_closed(self) -> None:
        self.assertFalse(self.payload["finite_field_or_random_input"])
        self.assertIn("does not change the 25..32 interval", self.payload["scope"])


if __name__ == "__main__":
    unittest.main()
