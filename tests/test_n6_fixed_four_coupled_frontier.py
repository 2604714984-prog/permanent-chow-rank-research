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

        all_rows = (
            self.payload["states"]
            + self.payload["excluded_b27_states"]
        )
        for row in all_rows:
            dimension = row["central_intersection_b"]
            self.assertEqual(
                row["quadratic_shadow_lower_bound"],
                dimension + 21,
            )
            self.assertEqual(
                row["per_omitted_factor_defect_budget"],
                27 - dimension,
            )

    def test_raw_and_current_state_partitions(self) -> None:
        raw = self.payload["raw_projection_frontier"]
        self.assertEqual(raw["central_intersection_range"], [20, 27])
        self.assertEqual(raw["state_count"], 36)
        self.assertEqual(
            raw["route_histogram"],
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 12,
                "structural_exclusion_or_stronger_invariant_required": 21,
            },
        )
        self.assertEqual(
            raw["relative_prolongation_cap_histogram"],
            {"23": 6, "59": 6},
        )

        self.assertEqual(self.payload["central_intersection_range"], [20, 26])
        self.assertEqual(self.payload["state_count"], 28)
        self.assertEqual(
            self.payload["route_histogram"],
            {
                "rank_budget_already_strict": 3,
                "relative_prolongation_cap_can_close": 10,
                "structural_exclusion_or_stronger_invariant_required": 15,
            },
        )
        self.assertEqual(
            self.payload["relative_prolongation_cap_histogram"],
            {"23": 5, "59": 5},
        )
        self.assertEqual(
            self.payload["maximum_remaining_gain_requirement"],
            157,
        )

    def test_b27_common_quotient_exclusion(self) -> None:
        exclusion = self.payload["common_quotient_b27_exclusion"]
        self.assertEqual(exclusion["excluded_central_intersection"], 27)
        self.assertEqual(exclusion["excluded_state_count"], 8)
        self.assertEqual(exclusion["common_quotient_dimension"], 12)
        self.assertEqual(exclusion["forced_quadratic_sum_dimension"], 60)
        self.assertEqual(exclusion["forced_central_catalectic_rank"], 80)
        self.assertEqual(
            exclusion["residual_inequality_upper_bound_on_central_rank"],
            34,
        )
        self.assertEqual(exclusion["contradiction"], "80>34")
        self.assertTrue(
            all(
                row["central_intersection_b"] == 27
                for row in self.payload["excluded_b27_states"]
            )
        )

    def test_b26_defect_pattern_classification(self) -> None:
        certificate = self.payload["b26_defect_patterns"]
        self.assertEqual(certificate["pattern_count"], 24)
        self.assertEqual(
            certificate["family_histogram"],
            {
                "maximal_quadratic_dimensions": 16,
                "one_quadratic_dimension_defect": 8,
            },
        )

        family_a = []
        family_b_masks: set[int] = set()
        for pattern in certificate["patterns"]:
            epsilon = [int(value) for value in pattern["epsilon"]]
            alpha = [int(value) for value in pattern["alpha"]]
            self.assertEqual(len(epsilon), 4)
            self.assertEqual(len(alpha), 4)
            for omitted in range(4):
                self.assertLessEqual(
                    sum(
                        epsilon[index]
                        for index in range(4)
                        if index != omitted
                    )
                    + alpha[omitted],
                    1,
                )

            if pattern["family"] == "one_quadratic_dimension_defect":
                family_a.append((epsilon, alpha))
                self.assertEqual(sum(epsilon), 1)
                index = epsilon.index(1)
                self.assertTrue(
                    all(
                        alpha[other] == 0
                        for other in range(4)
                        if other != index
                    )
                )
                self.assertIn(alpha[index], (0, 1))
            else:
                self.assertEqual(
                    pattern["family"],
                    "maximal_quadratic_dimensions",
                )
                self.assertEqual(epsilon, [0, 0, 0, 0])
                mask = sum(alpha[index] << index for index in range(4))
                family_b_masks.add(mask)

        self.assertEqual(len(family_a), 8)
        self.assertEqual(family_b_masks, set(range(16)))

    def test_frozen_summary_matches_generator(self) -> None:
        route_map = {
            "rank_budget_already_strict": "automatic",
            "relative_prolongation_cap_can_close": "p_cap",
            "structural_exclusion_or_stronger_invariant_required": "structural",
        }

        def compact(rows: list[dict[str, object]]) -> list[list[object]]:
            return [
                [
                    row["central_intersection_b"],
                    row["central_quotient_dimension_d"],
                    row["central_rank_h"],
                    route_map[str(row["route"])],
                    row[
                        "relative_prolongation_cap_sufficient_for_closure"
                    ],
                ]
                for row in rows
            ]

        self.assertEqual(compact(self.payload["states"]), self.frozen["states"])
        self.assertEqual(
            compact(self.payload["excluded_b27_states"]),
            self.frozen["excluded_b27_states"],
        )
        self.assertEqual(self.frozen["projection_cap"], 48)
        self.assertEqual(self.frozen["b_range"], [20, 26])
        self.assertEqual(self.frozen["state_count"], 28)
        self.assertEqual(
            self.frozen["route_counts"],
            {"automatic": 3, "p_cap": 10, "structural": 15},
        )
        self.assertEqual(self.frozen["p_cap_counts"], {"23": 5, "59": 5})
        self.assertEqual(
            self.frozen["maximum_remaining_gain_requirement"],
            157,
        )
        self.assertEqual(
            self.frozen["raw_frontier"],
            {
                "b_range": [20, 27],
                "p_cap_counts": {"23": 6, "59": 6},
                "route_counts": {
                    "automatic": 3,
                    "p_cap": 12,
                    "structural": 21,
                },
                "state_count": 36,
            },
        )
        self.assertEqual(
            self.frozen["b27_exclusion"],
            {
                "common_quotient_dimension": 12,
                "contradiction": "80>34",
                "excluded_state_count": 8,
                "forced_central_catalectic_rank": 80,
                "forced_quadratic_sum_dimension": 60,
                "residual_central_rank_upper_bound": 34,
            },
        )
        self.assertEqual(
            self.frozen["b26_defect_patterns"],
            {
                "family_counts": {
                    "maximal_quadratic_dimensions": 16,
                    "one_quadratic_dimension_defect": 8,
                },
                "pattern_count": 24,
            },
        )

    def test_no_state_is_silently_promoted(self) -> None:
        structural = [
            row
            for row in self.payload["states"]
            if row["route"]
            == "structural_exclusion_or_stronger_invariant_required"
        ]
        self.assertEqual(len(structural), 15)
        self.assertIn("does not exclude", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
