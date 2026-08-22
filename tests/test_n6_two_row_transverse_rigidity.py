from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_two_row_transverse_rigidity.py"
FROZEN = ROOT / "data" / "n6_two_row_transverse_rigidity.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_transverse_rigidity", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6TwoRowTransverseRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_scalar_multiplier_lemma(self) -> None:
        self.assertEqual(AUDIT.scalar_multiplier_constraint_rank(), 35)
        self.assertEqual(
            self.payload["regression"]["scalar_multiplier_solution_dimension"], 1
        )

    def test_support_lemma_dimensions(self) -> None:
        self.assertEqual(
            [AUDIT.s0_action_rank(size) for size in range(1, 7)],
            [5, 5, 6, 6, 6, 6],
        )

    def test_sample_general_b0_regression(self) -> None:
        matching = AUDIT.matching_matrix()
        dense = AUDIT.dense_matrix()
        self.assertEqual(AUDIT.determinant(matching), Fraction(-1))
        self.assertEqual(AUDIT.determinant(dense), Fraction(-5))
        self.assertEqual(AUDIT.algebra_dimension(matching), 36)
        self.assertEqual(AUDIT.algebra_dimension(dense), 36)

    def test_six_term_support_propagation(self) -> None:
        self.assertEqual(
            AUDIT.disjoint_nonempty_column_supports(),
            {
                "labelled_assignments": 720,
                "support_size_profiles": [[1, 1, 1, 1, 1, 1]],
            },
        )
        theorem = self.payload["pure_theorem"]
        self.assertTrue(theorem["b50_one_transverse_pair_propagates_to_all_six_terms"])
        self.assertTrue(theorem["b50_one_transverse_pair_excluded_by_N6_059"])

    def test_map_order_and_proof_boundary_are_explicit(self) -> None:
        theorem = self.payload["pure_theorem"]
        self.assertEqual(
            theorem["arbitrary_invertible_B0_algebra"],
            "proved by direct irreducibility plus Burnside",
        )
        boundary = self.payload["claim_boundary"]
        self.assertIn("every term pair is singular remains open", boundary)
        self.assertIn("not by enumeration", boundary)
        self.assertIn("does not prove ChowRank", boundary)


if __name__ == "__main__":
    unittest.main()
