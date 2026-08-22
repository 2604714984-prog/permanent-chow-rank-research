import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_overlap_three_33_nilpotent_shear_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap_three_33", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapThree33NilpotentShearTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlap_three_33_nilpotent_shear_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_parametrization_is_nilpotent(self):
        a, b, t, q = sp.symbols("a b t q")
        pairing = 1 * t * (-a - b * q) + a * t + b * t * q
        self.assertEqual(sp.expand(pairing), 0)
        self.assertEqual(
            self.payload["dense_full_support_condition"],
            "a*b*t*q*(a+b*q) != 0",
        )

    def test_complete_support_and_split_coverage(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAP_THREE_33_NILPOTENT_SHEAR_INVALID_TAIL_MINORS",
        )
        self.assertEqual(self.payload["candidate_count"], 100)
        self.assertEqual(len(self.payload["rows"]), 100)
        self.assertEqual(
            {
                (tuple(row["support"]), row["identity_count"])
                for row in self.payload["rows"]
            },
            {
                (support, identity_count)
                for support in itertools.combinations(range(6), 3)
                for identity_count in range(1, 6)
            },
        )

    def test_exact_gcds_have_only_allowed_boundary_factors(self):
        parameters = sp.symbols("a b t q")
        factor_sets = {}
        for row in self.payload["rows"]:
            polynomial = sp.Poly(
                sp.sympify(row["gcd_factorization"]),
                *parameters,
                domain=sp.ZZ,
            )
            covered, exponents, unresolved = (
                self.module.allowed_boundary_factorization(polynomial, parameters)
            )
            self.assertTrue(covered)
            self.assertEqual(unresolved, [])
            self.assertEqual(exponents, row["allowed_boundary_factor_exponents"])
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            self.assertEqual(row["minor_count"], 1)
            self.assertEqual(row["minors"][0]["determinant_term_count"], 1)
            labels = tuple(sorted(exponents))
            factor_sets[labels] = factor_sets.get(labels, 0) + 1
        self.assertEqual(factor_sets, {("a", "q", "t"): 50, ("q", "t"): 50})


if __name__ == "__main__":
    unittest.main()
