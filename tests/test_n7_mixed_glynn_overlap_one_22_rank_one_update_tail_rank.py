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
        / "n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap_one_22", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OverlapOne22RankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 600)
        self.assertEqual(self.payload["candidate_count"], 600)
        actual = {
            (
                (
                    row["shared_coordinate"],
                    row["left_extra_coordinate"],
                    row["right_extra_coordinate"],
                ),
                row["identity_count"],
            )
            for row in self.payload["rows"]
        }
        self.assertEqual(actual, set(self.module.candidates()))
        self.assertTrue(
            all(len(set(support)) == 3 for support, _count in actual)
        )

    def test_rank_one_determinant_identity(self):
        r, s, t = self.module.parameter_symbols()
        matrix = sp.eye(3) + sp.Matrix([1, r, 0]) * sp.Matrix(
            [[t * s, 0, t]]
        )
        self.assertEqual(sp.expand(matrix.det() - (1 + s * t)), 0)

    def test_every_dense_row_uses_one_allowed_exact_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAP_ONE_22_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        r, s, t = self.module.parameter_symbols()
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
                domain=sp.QQ,
            )
            covered, exponents, unresolved = (
                self.module.allowed_boundary_factorization(polynomial)
            )
            self.assertTrue(covered)
            self.assertEqual(unresolved, [])
            self.assertEqual(
                exponents, minor["allowed_boundary_factor_exponents"]
            )

    def test_projective_support_faces_are_imported_exactly(self):
        self.assertEqual(
            self.payload["face_certificates"],
            {
                "disjoint_coordinate_star": "EXACT_ALL_TWO_DIRECTION_SHEAR_INVALID_TAIL_MINORS",
                "oriented_singleton_overlap": "EXACT_ALL_ORIENTED_SINGLETON_OVERLAP_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
            },
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("projective v_c=0", boundary)
        self.assertIn("projective u_a=0", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
