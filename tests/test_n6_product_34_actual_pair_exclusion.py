from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_34_actual_pair_exclusion.py"
FROZEN = ROOT / "data" / "n6_product_34_actual_pair_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_product_34_actual", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Product34ActualPairExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_only_two_dimension_branches_survive(self) -> None:
        self.assertEqual(
            self.payload["dimension_gate"]["surviving_pairs"],
            [[3, 5], [3, 6]],
        )

    def test_hyperplane_and_ratio_regressions(self) -> None:
        determinant = self.payload["s0_four_determinant"]
        self.assertTrue(determinant["has_no_coordinate_linear_factor"])
        self.assertEqual(len(determinant["coordinate_absent_matching_monomial"]), 6)
        self.assertEqual(
            self.payload["s0_three_ratio_algebra"]["exact_QQ_algebra_dimension"],
            9,
        )

    def test_q5_projection_is_too_small(self) -> None:
        contradiction = self.payload["q5_projection_contradiction"]
        self.assertEqual(contradiction["actual_projection_rank"], 15)
        self.assertEqual(contradiction["forced_product_projection_upper_bound"], 9)

    def test_boundary_is_explicit(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not classify arbitrary", boundary)
        self.assertIn("does not", boundary)
        self.assertIn("ChowRank", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
