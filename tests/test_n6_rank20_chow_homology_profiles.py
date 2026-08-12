from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_rank20_chow_homology_profiles.py"


def load_module():
    spec = spec_from_file_location("n6_rank20_chow_homology_profiles", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class RankTwentyChowHomologyProfilesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.profiles = {
            profile["name"]: profile
            for profile in cls.payload["profiles"]
        }

    def test_exact_scalar_profiles(self) -> None:
        expected = {
            "span6_independent": ([0, 0, 0, 20], 20, 133_545),
            "span5_support5": ([0, 0, 10, 10], 320, 133_245),
            "span5_support4": ([0, 1, 20, 20], 1_105, 133_055),
            "span4_uniform_witness": ([0, 25, 48, 25], 13_961, 122_682),
        }
        for name, wanted in expected.items():
            profile = self.profiles[name]
            observed = (
                profile["active_homology_dimensions_wedge_0_to_3"],
                profile["ambient_36_variable_H_3_6_dimension"],
                profile["ambient_36_variable_middle_third_koszul_rank"],
            )
            self.assertEqual(observed, wanted)

    def test_all_four_terms_have_middle_rank_twenty(self) -> None:
        self.assertTrue(
            all(
                profile["active_derivative_dimensions"]["3"] == 20
                for profile in self.profiles.values()
            )
        )

    def test_labelled_cycle_images(self) -> None:
        expected = {
            "span6_independent": 20,
            "span5_support5": 10,
            "span5_support4": 16,
            "span4_uniform_witness": 20,
        }
        for name, image_rank in expected.items():
            cycle_data = self.profiles[name]["labelled_factor_triple_cycles"]
            self.assertTrue(cycle_data["all_are_cycles"])
            self.assertTrue(cycle_data["all_factor_triple_products_lie_in_D3"])
            self.assertTrue(cycle_data["preceding_image_is_in_the_kernel"])
            self.assertEqual(cycle_data["count"], 20)
            self.assertEqual(cycle_data["factor_triple_product_span_rank"], 20)
            self.assertEqual(cycle_data["cycle_span_rank"], 20)
            self.assertEqual(
                cycle_data["cycle_image_rank_modulo_boundaries"],
                image_rank,
            )

    def test_no_finite_field_or_random_claim(self) -> None:
        self.assertIn("exact Fraction", self.payload["arithmetic"])
        self.assertIn("does not prove", self.payload["claim_boundary"])

    def test_four_span_witness_is_bracket_open(self) -> None:
        certificate = self.profiles["span4_uniform_witness"][
            "four_span_bracket_open_certificate"
        ]
        self.assertEqual(certificate["minor_count"], 15)
        self.assertEqual(len(certificate["determinants"]), 15)
        self.assertTrue(certificate["all_nonzero"])
        self.assertTrue(all(certificate["determinants"].values()))


if __name__ == "__main__":
    unittest.main()
