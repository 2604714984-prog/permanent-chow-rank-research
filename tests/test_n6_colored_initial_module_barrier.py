from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_colored_initial_module_barrier.py"
SPEC = importlib.util.spec_from_file_location("n6_colored_initial_module_barrier", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ColoredInitialModuleBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = MODULE.build_certificate()

    def test_capacity_inverse_endpoints(self) -> None:
        rows = {
            row["cubic_target"]: row
            for row in self.certificate["capacity_constrained_inverse_rows"]
        }
        self.assertEqual(rows[320]["unrestricted_minimum_quadratic_dimension"], 160)
        self.assertEqual(rows[320]["all_labels_active_minimum_quadratic_dimension"], 163)
        self.assertEqual(rows[336]["unrestricted_minimum_quadratic_dimension"], 169)
        self.assertEqual(rows[336]["all_labels_active_minimum_quadratic_dimension"], 171)

    def test_active_model_dimensions(self) -> None:
        model = self.certificate["explicit_all_labels_active_model"]
        self.assertEqual(sum(model["cubic_relation_profile"]), 336)
        self.assertEqual(sum(model["quadratic_relation_profile_before_slack"]), 171)
        self.assertEqual(sum(model["quadratic_relation_profile_after_slack"]), 203)
        self.assertTrue(model["all_twenty_labels_active"])
        self.assertLessEqual(max(model["cubic_relation_profile"]), 20)
        self.assertLessEqual(max(model["quadratic_relation_profile_after_slack"]), 15)
        self.assertEqual(model["formal_middle_intersection_dimension"], 336)
        self.assertEqual(model["formal_quadratic_intersection_dimension"], 203)
        self.assertEqual(model["quadratic_label_ambient_dimensions"], [15] * 20)
        self.assertEqual(model["formal_quadratic_colored_ambient_dimension"], 300)
        self.assertEqual(
            model["formal_quadratic_intersection_dimension"]
            + model["external_quadratic_complement_dimension"],
            model["formal_quadratic_permanent_dimension"],
        )

    def test_sharp_lex_prolongations(self) -> None:
        rows = {
            row["quadratic_dimension"]: row["cubic_prolongation_dimension"]
            for row in self.certificate["sharp_lex_monomial_spaces"]
        }
        self.assertEqual(rows, {1: 1, 8: 13, 9: 16, 10: 20})

    def test_hereditary_defect_is_zero(self) -> None:
        model = self.certificate["explicit_all_labels_active_model"]
        self.assertEqual(model["ordinary_central_defect_of_every_nonempty_subset"], 0)

    def test_claim_boundary_is_fail_closed(self) -> None:
        boundary = self.certificate["claim_boundary"]
        self.assertIn("not a Chow decomposition", boundary)
        self.assertIn("not asserted to be realizable", boundary)


if __name__ == "__main__":
    unittest.main()
