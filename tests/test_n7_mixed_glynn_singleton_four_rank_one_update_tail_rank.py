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
        / "n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_singleton_four", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SingletonFourRankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory_and_determinant_identity(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 600)
        self.assertEqual(self.payload["candidate_count"], 600)
        self.assertEqual(
            {
                orientation: sum(
                    row["orientation"] == orientation
                    for row in self.payload["rows"]
                )
                for orientation in ("left_singleton", "right_singleton")
            },
            {"left_singleton": 300, "right_singleton": 300},
        )
        s, t, w, x = self.module.parameter_symbols()
        left = sp.eye(4) + sp.Matrix([1, 0, 0, 0]) * sp.Matrix(
            [[t, t * s, t * w, t * x]]
        )
        right = sp.eye(4) + sp.Matrix([1, s, w, x]) * sp.Matrix(
            [[t, 0, 0, 0]]
        )
        for matrix in (left, right):
            self.assertEqual(sp.expand(matrix.det() - (1 + t)), 0)

    def test_every_row_uses_first_allowed_exact_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_SINGLETON_FOUR_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        s, t, w, x = self.module.parameter_symbols()
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            self.assertEqual(row["attempt_count"], 1)
            self.assertEqual(row["failed_attempts"], [])
            minor = row["selected_minor"]
            polynomial = sp.Poly(
                sp.sympify(minor["determinant_factorization"]),
                s,
                t,
                w,
                x,
                domain=sp.QQ,
            )
            covered, exponents, unresolved, _factorization = (
                self.module.allowed_boundary_factorization(polynomial)
            )
            self.assertTrue(covered)
            self.assertEqual(unresolved, [])
            self.assertEqual(
                exponents, minor["allowed_boundary_factor_exponents"]
            )

    def test_projective_faces_are_imported_exactly(self):
        self.assertEqual(
            self.payload["face_certificates"], self.module.face_certificates()
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("projective singleton-versus-four support closure", boundary)
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
