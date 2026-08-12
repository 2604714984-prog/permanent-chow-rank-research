from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b59_scalar_frontier.py"
FROZEN = ROOT / "data" / "n6_b59_scalar_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b59_frontier", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6B59ScalarFrontierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_inherited_layer(self) -> None:
        self.assertEqual(
            self.payload["layer_parameters"],
            {
                "middle_intersection_b": 59,
                "quadratic_shadow_lower_m_b": 75,
                "defect_budget_D_b": 3,
            },
        )

    def test_complete_histograms(self) -> None:
        self.assertEqual(self.payload["canonical_state_count"], 367)
        self.assertEqual(
            self.payload["quadratic_relation_dimension_histogram"],
            {"0": 294, "1": 62, "2": 10, "3": 1},
        )
        self.assertEqual(
            self.payload["global_quotient_dimension_histogram"],
            {"12": 32, "13": 111, "14": 140, "15": 84},
        )

    def test_exact_pruning(self) -> None:
        self.assertEqual(
            self.payload["exclusion_histogram"],
            {
                "N6-047 universal extremal-term cap": 226,
                "N6-048 universal alpha-one-term cap": 51,
                "N6-049 universal alpha-two-term cap": 6,
                "N6-051 universal alpha-one-term t15 cap": 21,
                "N6-051 universal extremal-term t15 cap": 56,
                "N6-052 universal alpha-two-term t15 cap": 6,
                "remaining_all_alpha_three": 1,
            },
        )

    def test_honest_kappa3_window_and_survivor(self) -> None:
        self.assertEqual(self.payload["unique_kappa3_state_id"], "b59_state_009")
        self.assertEqual(self.payload["unique_kappa3_middle_rank_window"], [112, 120])
        self.assertEqual(self.payload["remaining_state_ids"], ["b59_state_366"])
        survivor = self.payload["states"][366]
        self.assertEqual(survivor["epsilon_alpha_pairs"], [[0, 3]] * 6)
        self.assertEqual(survivor["required_prolongation_dimension_lower"], 461)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("necessary-state", boundary)
        self.assertIn("does not exclude", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
