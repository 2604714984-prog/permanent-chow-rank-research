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
        / "n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap_one_23", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapOne23RankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory_and_determinant_identity(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 1800)
        self.assertEqual(self.payload["candidate_count"], 1800)
        self.assertEqual(
            {
                orientation: sum(
                    row["orientation"] == orientation
                    for row in self.payload["rows"]
                )
                for orientation in ("extra_left", "extra_right")
            },
            {"extra_left": 900, "extra_right": 900},
        )
        r, s, t, w = self.module.parameter_symbols()
        extra_right = sp.eye(4) + sp.Matrix([1, r, 0, 0]) * sp.Matrix(
            [[t * s, 0, t, t * w]]
        )
        extra_left = sp.eye(4) + sp.Matrix([1, r, w, 0]) * sp.Matrix(
            [[t * s, 0, 0, t]]
        )
        for matrix in (extra_right, extra_left):
            self.assertEqual(sp.expand(matrix.det() - (1 + s * t)), 0)

    def test_every_row_uses_first_allowed_exact_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAP_ONE_23_32_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        r, s, t, w = self.module.parameter_symbols()
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            self.assertEqual(row["attempt_count"], 1)
            self.assertEqual(row["failed_attempts"], [])
            minor = row["selected_minor"]
            polynomial = sp.Poly(
                sp.sympify(minor["determinant_factorization"]),
                r,
                s,
                t,
                w,
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
        self.assertIn("projective overlap-one (2,3)/(3,2) support closure", boundary)
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
