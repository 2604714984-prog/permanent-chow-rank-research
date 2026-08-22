import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_equality_locus_reduction.py"
DATA = ROOT / "data" / "n7_b2_equality_locus_reduction.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_equality_locus_reduction", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class EqualityLocusReductionTests(unittest.TestCase):
    def test_permanent_u_degree_profile(self) -> None:
        profile = MODULE.permanent_u_degree_profile()
        self.assertEqual([row["target_monomials"] for row in profile], [1, 0, 21, 70, 315, 924, 1855, 1854])
        self.assertEqual(sum(row["target_monomials"] for row in profile), 5040)

    def test_two_term_shear_identity_and_defect(self) -> None:
        row = MODULE.shear_pencil_control([-1, 1], [sp.Rational(1, 2)] * 2)
        self.assertTrue(row["quotient_polynomial_identity_holds"])
        self.assertTrue(row["contains_nonmonomial_frame"])
        self.assertEqual((row["rank_B"], row["rank_C"], row["rank_BC"]), (45, 40, 35))
        self.assertEqual(row["kernel_image_defect"], 20)
        self.assertFalse(row["projected_sylvester_equality_holds"])

    def test_three_term_shear_identity_and_defect(self) -> None:
        row = MODULE.shear_pencil_control([1, 2, 3], [sp.Integer(3), sp.Integer(-3), sp.Integer(1)])
        self.assertEqual(row["kernel_image_defect"], 55)
        self.assertFalse(row["projected_sylvester_equality_holds"])

    def test_u1_zero_target_residual(self) -> None:
        two = MODULE.shear_u1_operator([-1, 1], [sp.Rational(1, 2)] * 2)
        three = MODULE.shear_u1_operator([1, 2, 3], [sp.Integer(3), sp.Integer(-3), sp.Integer(1)])
        self.assertEqual((two["rank_per_U_coordinate"], two["nullity_per_U_coordinate"]), (12, 2))
        self.assertEqual((three["rank_per_U_coordinate"], three["nullity_per_U_coordinate"]), (12, 9))
        self.assertEqual((two["total_nullity_across_42_U_coordinates"], three["total_nullity_across_42_U_coordinates"]), (84, 378))

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
