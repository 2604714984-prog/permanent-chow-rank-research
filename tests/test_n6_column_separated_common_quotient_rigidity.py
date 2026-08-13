from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_column_separated_common_quotient_rigidity.py"
FROZEN = ROOT / "data" / "n6_column_separated_common_quotient_rigidity.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_column_separated", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ColumnSeparatedCommonQuotientRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_rho_has_kernel_exactly_S0(self) -> None:
        regression = self.payload["regression"]
        self.assertEqual(regression["rho_rank"], 21)
        self.assertEqual(regression["rho_kernel_dimension"], 15)
        self.assertEqual(regression["S0_basis_rank"], 15)
        self.assertTrue(regression["S0_basis_annihilated_by_rho"])

    def test_binary_pair_identities(self) -> None:
        binary = AUDIT.binary_pair_audit()
        self.assertEqual(binary["ordered_pairs"], 3969)
        self.assertEqual(binary["dependent_pairs"], 63)
        self.assertEqual(binary["independent_pairs"], 3906)

    def test_full_tau_rejects_diagonal_only_false_positive(self) -> None:
        false_positive = AUDIT.false_positive_regression()
        self.assertTrue(false_positive["diagonal_proportional"])
        self.assertEqual(false_positive["wedge_01_p"], -1)
        self.assertEqual(false_positive["wedge_01_q"], -2)
        self.assertFalse(false_positive["full_tau_proportional"])

    def test_rank_branches_and_boundary(self) -> None:
        branches = AUDIT.branch_regression()
        self.assertEqual(branches["rank_three_pair_plane_intersection_dimension"], 1)
        self.assertEqual(branches["rank_two_p_family_rank"], 2)
        self.assertEqual(branches["rank_one_combined_plane_rank"], 2)
        boundary = self.payload["claim_boundary"]
        self.assertIn("all-singular nonseparated", boundary)
        self.assertIn("does not replace the pure proof", boundary)
        self.assertIn("prove ChowRank", boundary)


if __name__ == "__main__":
    unittest.main()

