from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_fixed_four_coupled_frontier.py"
FROZEN = ROOT / "data" / "n6_fixed_four_coupled_frontier.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_fixed_four_coupled_frontier",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load fixed-four frontier generator")
FRONTIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FRONTIER)


class N6FixedFourCoupledFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = FRONTIER.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_separator_and_projection_cap(self) -> None:
        self.assertEqual(
            self.payload["quadratic_intersection_projection_cap"],
            48,
        )
        certificate = self.payload["bukh_separator_certificate"]
        self.assertEqual(certificate["separator"], "427/100")
        self.assertTrue(
            certificate["binom_separator_3_squared_is_less_than_28"]
        )
        self.assertTrue(
            certificate["binom_separator_2_squared_is_greater_than_48"]
        )

    def test_exact_shadow_and_defect_budgets(self) -> None:
        table = self.payload["exact_shadow_lower_table"]
        expected_separators = {
            "20": "41/10",
            "21": "103/25",
            "22": "207/50",
            "23": "104/25",
            "24": "209/50",
            "25": "21/5",
            "26": "211/50",
            "27": "106/25",
        }
        self.assertEqual(set(table), set(expected_separators))
        for key, separator in expected_separators.items():
            dimension = int(key)
            self.assertEqual(table[key]["separator"], separator)
            self.assertEqual(
                table[key]["integer_shadow_lower_bound"],
                dimension + 21,
            )
            self.assertEqual(
                table[key]["per_omitted_factor_defect_budget"],
                27 - dimension,
            )

        for row in self.payload["states"]:
            dimension = row["central_intersection_b"]
            self.assertEqual(
                row["quadratic_shadow_lower_bound"],
                dimension + 21,
            )
            self.assertEqual(
                row["per_omitted_factor_defect_budget"],
                27 - dimension,
            )

    def test_state_partition(self) -> None:
        self.assertEqual(self.payload["central_intersection_range"], [20, 27])
        self.assertEqual(self.payload["state_count"], 36)
        self.assertEqual(
            self.payload["route_histogram"],
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 12,
                "structural_exclusion_or_stronger_invariant_required": 21,
            },
        )
        self.assertEqual(
            self.payload["relative_prolongation_cap_histogram"],
            {"23": 6, "59": 6},
        )

    def test_frozen_summary_matches_generator(self) -> None:
        route_map = {
            "rank_budget_already_strict": "automatic",
            "relative_prolongation_cap_can_close": "p_cap",
            "structural_exclusion_or_stronger_invariant_required": "structural",
        }
        compact_states = [
            [
                row["central_intersection_b"],
                row["central_quotient_dimension_d"],
                row["central_rank_h"],
                route_map[row["route"]],
                row["relative_prolongation_cap_sufficient_for_closure"],
            ]
            for row in self.payload["states"]
        ]
        self.assertEqual(compact_states, self.frozen["states"])
        self.assertEqual(self.frozen["projection_cap"], 48)
        self.assertEqual(self.frozen["b_range"], [20, 27])
        self.assertEqual(self.frozen["state_count"], 36)
        self.assertEqual(
            self.frozen["route_counts"],
            {"automatic": 3, "p_cap": 12, "structural": 21},
        )
        self.assertEqual(self.frozen["p_cap_counts"], {"23": 6, "59": 6})

    def test_no_state_is_silently_promoted(self) -> None:
        structural = [
            row
            for row in self.payload["states"]
            if row["route"]
            == "structural_exclusion_or_stronger_invariant_required"
        ]
        self.assertEqual(len(structural), 21)
        self.assertIn("does not exclude", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
