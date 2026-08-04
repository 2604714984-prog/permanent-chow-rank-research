from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_component_prolongation_exclusion.py"
FROZEN = ROOT / "data" / "n6_component_prolongation_exclusion.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_component_prolongation_exclusion",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load n6 component-prolongation audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6ComponentProlongationExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_macaulay_successors(self) -> None:
        self.assertEqual(
            self.payload["macaulay_degree_two_successors"],
            {"0": 0, "1": 1, "2": 2, "3": 4, "4": 5, "5": 7},
        )

    def test_exact_layer_counts(self) -> None:
        by_b = {row["b"]: row for row in self.payload["layers"]}
        self.assertEqual(
            (
                by_b[22]["all_labelled_pattern_count"],
                by_b[22]["quadratic_dimension_twelve_pattern_count"],
                by_b[22]["profile_feasible_pattern_count"],
            ),
            (14877, 1716, 13161),
        )
        self.assertEqual(
            (
                by_b[23]["all_labelled_pattern_count"],
                by_b[23]["quadratic_dimension_twelve_pattern_count"],
                by_b[23]["profile_feasible_pattern_count"],
            ),
            (4599, 256, 4343),
        )
        self.assertEqual(
            (
                by_b[24]["all_labelled_pattern_count"],
                by_b[24]["quadratic_dimension_twelve_pattern_count"],
                by_b[24]["profile_feasible_pattern_count"],
            ),
            (1153, 16, 1137),
        )

    def test_all_high_layers_are_strict(self) -> None:
        by_b = {row["b"]: row for row in self.payload["layers"]}
        self.assertEqual(
            by_b[22]["minimum_coupled_central_rank_lower_bound"],
            38,
        )
        self.assertEqual(by_b[22]["residual_central_rank_upper_bound"], 24)
        self.assertEqual(
            by_b[23]["minimum_coupled_central_rank_lower_bound"],
            50,
        )
        self.assertEqual(by_b[23]["residual_central_rank_upper_bound"], 26)
        self.assertEqual(
            by_b[24]["minimum_coupled_central_rank_lower_bound"],
            56,
        )
        self.assertEqual(by_b[24]["residual_central_rank_upper_bound"], 28)
        self.assertTrue(
            all(
                row["minimum_coupled_central_rank_lower_bound"]
                > row["residual_central_rank_upper_bound"]
                for row in self.payload["layers"]
            )
        )

    def test_low_layers_remain_automatic(self) -> None:
        self.assertEqual(
            self.payload["remaining_low_layers"],
            [
                {
                    "b": 20,
                    "d": 0,
                    "residual_koszul_rank_lower_bound": 13455,
                    "nineteen_term_koszul_cap": 13395,
                    "strict_margin": 60,
                },
                {
                    "b": 21,
                    "d": 0,
                    "residual_koszul_rank_lower_bound": 13419,
                    "nineteen_term_koszul_cap": 13395,
                    "strict_margin": 24,
                },
                {
                    "b": 21,
                    "d": 1,
                    "residual_koszul_rank_lower_bound": 13419,
                    "nineteen_term_koszul_cap": 13395,
                    "strict_margin": 24,
                },
            ],
        )

    def test_frozen_payload_matches_replay(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_claim_boundary(self) -> None:
        self.assertEqual(self.payload["certified_interval"], [24, 32])
        self.assertIn(">=24", self.payload["conclusion"])
        self.assertIn("does not prove", self.payload["claim_boundary"])
        self.assertIn(">=25", self.payload["claim_boundary"])
        self.assertNotIn("=32", self.payload["conclusion"])


if __name__ == "__main__":
    unittest.main()
