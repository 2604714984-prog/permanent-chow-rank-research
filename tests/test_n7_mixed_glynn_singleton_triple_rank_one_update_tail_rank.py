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
        / "n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_singleton_triple", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SingletonTripleRankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory_covers_both_orientations(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 600)
        self.assertEqual(self.payload["candidate_count"], 600)
        actual = {
            (
                row["orientation"],
                row["shared_coordinate"],
                tuple(row["extra_coordinates"]),
                row["identity_count"],
            )
            for row in self.payload["rows"]
        }
        expected = {
            (orientation, shared, extras, identity_count)
            for (orientation, shared, extras), identity_count in self.module.candidates()
        }
        self.assertEqual(actual, expected)
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

    def test_rank_one_determinant_identity(self):
        s, t, w = self.module.parameter_symbols()
        left_matrix = sp.eye(3) + sp.Matrix([1, 0, 0]) * sp.Matrix(
            [[t, t * s, t * w]]
        )
        right_matrix = sp.eye(3) + sp.Matrix([1, s, w]) * sp.Matrix(
            [[t, 0, 0]]
        )
        for matrix in (left_matrix, right_matrix):
            self.assertEqual(sp.expand(matrix.det() - (1 + t)), 0)

    def test_every_row_uses_one_allowed_exact_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_SINGLETON_TRIPLE_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        s, t, w = self.module.parameter_symbols()
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

    def test_projective_faces_are_imported_exactly(self):
        self.assertEqual(
            self.payload["face_certificates"],
            {
                "disjoint_two_direction": (
                    "EXACT_ALL_TWO_DIRECTION_SHEAR_INVALID_TAIL_MINORS"
                ),
                "oriented_singleton_overlap": (
                    "EXACT_ALL_ORIENTED_SINGLETON_OVERLAP_INVERTIBLE_RANK_ONE_UPDATE_MINORS"
                ),
            },
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("projective singleton-versus-triple support closure", boundary)
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
