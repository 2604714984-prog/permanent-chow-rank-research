from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_all_singular_hook_exclusion.py"
FROZEN = ROOT / "data" / "n6_all_singular_hook_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_all_singular_hook", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class AllSingularHookExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_s0_action_has_rank_at_least_five(self):
        profile = self.payload["s0_action_rank_profile"]
        self.assertEqual([row["exact_rank_of_S0_times_y"] for row in profile], [5, 5, 6, 6, 6, 6])

    def test_three_wedge_spaces_have_zero_intersection(self):
        intersection = self.payload["wedge_space_intersections"]
        self.assertEqual(intersection["pair_intersection_dimension"], 1)
        self.assertEqual(intersection["triple_intersection_dimension"], 0)

    def test_finite_hook_cases_are_exhausted(self):
        cases = self.payload["finite_hook_case_routing"]
        self.assertEqual([case["full_row_count_m"] for case in cases], [3, 4, 5, 6])
        self.assertEqual([case["label_class_count_q"] for case in cases], [3, 4, 5, 6])
        self.assertEqual(
            [case["proof_branch"] for case in cases],
            [
                "requires_m3_parallel_argument",
                "requires_m4_column_argument",
                "excluded_by_q_le_4",
                "excluded_by_q_le_4",
            ],
        )

    def test_claim_boundary(self):
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not prove exact rank 32", boundary)
        self.assertIn("does not give a border-rank lower bound", boundary)
        self.assertIn("does not prove the general conjecture", boundary)


if __name__ == "__main__":
    unittest.main()
