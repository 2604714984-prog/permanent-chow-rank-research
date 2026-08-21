import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_overlapping_22_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_rank_one_overlap22", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Coincident22RankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_22_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 75)
        self.assertEqual(len(self.module.candidates()), 75)
        self.assertEqual(
            {
                (tuple(row["support"]), row["identity_count"])
                for row in self.payload["rows"]
            },
            set(self.module.candidates()),
        )

    def test_rank_one_determinant_identity(self):
        r, s, t = self.module.parameter_symbols()
        matrix = sp.eye(2) + sp.Matrix([1, r]) * sp.Matrix([[t * s, t]])
        self.assertEqual(sp.expand(matrix.det() - (1 + t * (r + s))), 0)

    def test_all_generic_and_pivot_face_factors_are_covered(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_COINCIDENT_22_INVERTIBLE_RANK_ONE_UPDATE_INVALID_TAIL_MINORS",
        )
        pivot_count = 0
        monomial_subface_count = 0
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            self.assertEqual(row["minor_count"], 1)
            r, s, t = self.module.parameter_symbols()
            polynomial = sp.Poly(
                sp.sympify(row["gcd_factorization"]), r, s, t, domain=sp.QQ
            )
            covered, exponents, unresolved = (
                self.module.allowed_boundary_factorization(polynomial)
            )
            self.assertTrue(covered)
            self.assertEqual(unresolved, [])
            self.assertEqual(
                exponents, row["allowed_boundary_factor_exponents"]
            )
            face = row["pivot_face_minor"]
            if face is None:
                continue
            pivot_count += 1
            face_polynomial = sp.Poly(
                sp.sympify(face["determinant_factorization"]), r, t, domain=sp.QQ
            )
            face_covered, face_exponents, face_unresolved = (
                self.module.pivot_face_factorization(face_polynomial)
            )
            self.assertTrue(face_covered)
            self.assertEqual(face_unresolved, [])
            self.assertEqual(
                face_exponents, face["allowed_boundary_factor_exponents"]
            )
            if face["monomial_subface_matrix"] is not None:
                monomial_subface_count += 1
                self.assertEqual(
                    face["monomial_subface_matrix"], "[[0,t],[1/t,0]]"
                )
        self.assertEqual(pivot_count, 56)
        self.assertEqual(monomial_subface_count, 20)

    def test_claim_boundary_stays_restricted(self):
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("does not cover larger coincident supports", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
