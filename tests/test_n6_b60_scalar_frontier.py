from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b60_scalar_frontier.py"
FROZEN = ROOT / "data" / "n6_b60_scalar_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b60_scalar_frontier", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6B60ScalarFrontierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

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

    def test_exact_cap_partition(self) -> None:
        self.assertEqual(
            self.payload["exclusion_histogram"],
            {
                "N6-047 universal extremal-term cap": 226,
                "N6-048 universal alpha-one-term cap": 51,
                "N6-049 universal alpha-two-term cap": 6,
                "remaining_t15_frontier": 84,
            },
        )

    def test_unique_kappa_three_window(self) -> None:
        self.assertEqual(self.payload["unique_kappa3_state_id"], "b60_state_009")
        self.assertEqual(self.payload["unique_kappa3_middle_rank_window"], [112, 120])
        state = self.payload["states"][9]
        self.assertIsNone(state["fixed_middle_rank_h_exact"])
        self.assertEqual(state["cubic_relation_dimension_upper_rho3"], 4)

    def test_remaining_frontier_is_exactly_t15(self) -> None:
        remaining = [
            state
            for state in self.payload["states"]
            if not state["excluded_by_existing_cap"]
        ]
        self.assertEqual(len(remaining), 84)
        self.assertTrue(
            all(
                state["fixed_quadratic_quotient_t2"] == 15
                and state["quadratic_relation_dimension_kappa2"] == 0
                and state["fixed_middle_rank_h_exact"] == 120
                for state in remaining
            )
        )

    def test_claim_boundary(self) -> None:
        self.assertIn("necessary-state", self.payload["claim_boundary"])
        self.assertIn("does not exclude", self.payload["claim_boundary"])
        self.assertIn("border-rank", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
