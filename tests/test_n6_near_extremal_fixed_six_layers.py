from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_near_extremal_fixed_six_layers.py"
FROZEN = ROOT / "data" / "n6_near_extremal_fixed_six_layers.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_near_extremal", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class NearExtremalFixedSixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_state_counts_and_profiles(self) -> None:
        layers = {row["middle_intersection_b"]: row for row in self.payload["layers"]}
        self.assertEqual(layers[61]["canonical_scalar_state_count"], 73)
        self.assertEqual(layers[62]["canonical_scalar_state_count"], 11)
        self.assertEqual(layers[63]["canonical_scalar_state_count"], 11)
        self.assertEqual(
            [row["sorted_epsilon_profile"] for row in layers[61]["profile_summary"]],
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 1, 1],
            ],
        )

    def test_middle_ranks_are_exact(self) -> None:
        conclusions = self.payload["strict_conclusions"]
        self.assertEqual(conclusions["b62_b63_fixed_middle_rank"], 120)
        self.assertEqual(conclusions["b61_fixed_middle_rank_possibilities"], [118, 120])
        self.assertEqual(
            conclusions["b61_rank118_unique_epsilon_profile"],
            [0, 0, 0, 0, 0, 2],
        )

    def test_kappa_two_forces_six_extremal_terms(self) -> None:
        for layer in self.payload["layers"]:
            for state in layer["states"]:
                if state["quadratic_relation_dimension_kappa2"] == 2:
                    self.assertEqual(state["extremal_rectangle_term_count"], 6)
                    self.assertTrue(
                        all(pair == [0, 0] for pair in state["epsilon_alpha_pairs"])
                    )

    def test_highlighted_states_have_common_twelve_quotient(self) -> None:
        highlighted = self.payload["highlighted_common_quotient_states"]
        self.assertTrue(highlighted)
        for state in highlighted:
            self.assertEqual(state["common_quotient_dimension"], 12)
            self.assertGreaterEqual(state["extremal_rectangle_term_count"], 4)

    def test_residual_rank_and_full_term_counts(self) -> None:
        conclusions = self.payload["strict_conclusions"]
        self.assertEqual(conclusions["b61_h120_residual_middle_lower"], 398)
        self.assertEqual(conclusions["b61_h118_residual_middle_lower"], 396)
        self.assertEqual(conclusions["b62_residual_middle_lower"], 396)
        self.assertEqual(conclusions["b63_residual_middle_lower"], 394)
        self.assertEqual(
            conclusions["minimum_full_rank_residual_terms"],
            {"b61_h120": 19, "b61_h118": 18, "b62": 18, "b63": 17},
        )


if __name__ == "__main__":
    unittest.main()
