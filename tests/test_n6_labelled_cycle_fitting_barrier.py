from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_labelled_cycle_fitting_barrier.py"
DATA = ROOT / "data" / "n6_labelled_cycle_fitting_barrier.json"


def load_module():
    spec = spec_from_file_location("n6_labelled_cycle_fitting_barrier", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class LabelledCycleFittingBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.by_name = {
            row["name"]: row for row in cls.payload["two_term_exact_profiles"]
        }

    def test_frozen_json_is_reconstructed(self) -> None:
        frozen = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)

    def test_two_full_span_pair_has_exact_collision(self) -> None:
        row = self.by_name["two_full_span_terms"]
        self.assertEqual(row["boundary_intersection_dimension"], 0)
        self.assertEqual(row["cycle_intersection_dimension"], 0)
        self.assertEqual(
            row["individual_images_modulo_aggregate_boundary"],
            [19, 17],
        )
        self.assertEqual(row["intersection_of_the_two_quotient_images"], 3)
        self.assertEqual(row["joint_labelled_presentation_rank"], 33)
        self.assertEqual(row["joint_kernel_dimension"], 7)
        self.assertEqual(
            row["verified_derivative_dimensions"],
            [{"D3_dimension": 20, "D4_dimension": 15}] * 2,
        )

    def test_five_full_span_terms_saturate_the_universal_kernel(self) -> None:
        certificate = self.payload["five_full_span_saturation_certificate"]
        self.assertEqual(
            certificate["factor_matrix_integer_determinants"],
            [1, 184, -68, 9, -15],
        )
        self.assertEqual(
            certificate["boundary_rank_progression_mod_prime"],
            [190, 380, 570, 760, 840],
        )
        self.assertEqual(certificate["universal_domain_dimension"], 1120)
        self.assertEqual(certificate["universal_kernel_dimension"], 840)
        self.assertEqual(certificate["selected_boundary_column_count"], 840)
        self.assertNotEqual(
            certificate["triangular_minor_diagonal_product_mod_prime"],
            0,
        )

    def test_all_one_hundred_labelled_cycles_die(self) -> None:
        certificate = self.payload["five_full_span_saturation_certificate"]
        self.assertEqual(certificate["labelled_cycle_count"], 100)
        self.assertEqual(certificate["aggregate_labelled_presentation_rank"], 0)

    def test_claim_boundary_remains_explicit(self) -> None:
        self.assertIn("not a permanent decomposition", self.payload["claim_boundary"])
        self.assertIn("may still work", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
