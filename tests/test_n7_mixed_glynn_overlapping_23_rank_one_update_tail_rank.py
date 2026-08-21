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
        / "n7_mixed_glynn_overlapping_23_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_rank_one_overlap23", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Overlapping23RankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_23_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 600)
        self.assertEqual(self.payload["candidate_count"], 600)
        actual = {
            (
                row["shape"],
                tuple(row["core_support"]),
                row["extra_coordinate"],
                row["identity_count"],
            )
            for row in self.payload["rows"]
        }
        expected = {
            (shape, core, extra, identity_count)
            for (shape, core, extra), identity_count in self.module.candidates()
        }
        self.assertEqual(actual, expected)
        self.assertEqual(
            {shape: sum(row["shape"] == shape for row in self.payload["rows"])
             for shape in ("extra_left", "extra_right")},
            {"extra_left": 300, "extra_right": 300},
        )

    def test_rank_one_determinant_identity_and_pivot_face(self):
        r, s, t, w = self.module.parameter_symbols()
        extra_right = sp.eye(3) + sp.Matrix([1, r, 0]) * sp.Matrix(
            [[t * s, t, t * w]]
        )
        extra_left = sp.eye(3) + sp.Matrix([1, r, w]) * sp.Matrix(
            [[t * s, t, 0]]
        )
        expected = 1 + t * (r + s)
        self.assertEqual(sp.expand(extra_right.det() - expected), 0)
        self.assertEqual(sp.expand(extra_left.det() - expected), 0)
        for matrix in (extra_right, extra_left):
            self.assertEqual(
                sp.expand(matrix.det().subs(s, -1 / t) - r * t), 0
            )

    def test_double_pivot_laurent_column_scaling_is_rank_preserving(self):
        r, s, t, w = self.module.parameter_symbols()
        support = ("extra_right", (0, 1), 2)
        identity_count = 2
        assignment = (2, 2, 2, 2, 2, 2)
        original = self.module.assignment_feature(
            assignment, identity_count, support, -1 / t, -1 / t, t, w
        )
        scaled = self.module.double_pivot_face_assignment_feature(
            assignment, identity_count, support, t, w
        )
        updated_second_count = 4
        self.assertTrue(
            all(
                sp.expand(
                    scaled_value - t**updated_second_count * original_value
                )
                == 0
                for scaled_value, original_value in zip(scaled, original)
            )
        )

    def test_every_dense_row_has_single_minor_or_exact_pivot_face_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAPPING_23_32_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        r, s, t, w = self.module.parameter_symbols()
        pivot = sp.Poly(1 + s * t, r, s, t, w, domain=sp.QQ).monic()
        direct_count = 0
        pivot_count = 0
        double_pivot_count = 0
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            primary = row["primary_minor"]
            polynomial = sp.Poly(
                sp.sympify(primary["determinant_factorization"]),
                r,
                s,
                t,
                w,
                domain=sp.QQ,
            )
            covered, exponents, unresolved = (
                self.module.allowed_boundary_factorization(polynomial)
            )
            self.assertEqual(
                exponents, primary["allowed_boundary_factor_exponents"]
            )
            self.assertEqual(unresolved, primary["unresolved_factors"])
            face = row["pivot_face_minor"]
            if covered:
                direct_count += 1
                self.assertIsNone(face)
                self.assertIsNone(row["double_pivot_face_minor"])
                continue
            self.assertTrue(unresolved)
            self.assertTrue(
                all(
                    sp.Poly(
                        sp.sympify(item["factor"]),
                        r,
                        s,
                        t,
                        w,
                        domain=sp.QQ,
                    ).monic()
                    == pivot
                    for item in unresolved
                )
            )
            self.assertIsNotNone(face)
            face_polynomial = sp.Poly(
                sp.sympify(face["determinant_factorization"]),
                r,
                t,
                w,
                domain=sp.QQ,
            )
            face_covered, face_exponents, face_unresolved = (
                self.module.pivot_face_factorization(face_polynomial)
            )
            self.assertEqual(
                face_exponents, face["allowed_boundary_factor_exponents"]
            )
            self.assertEqual(face_unresolved, face["unresolved_factors"])
            double_face = row["double_pivot_face_minor"]
            if face_covered:
                pivot_count += 1
                self.assertIsNone(double_face)
                continue
            double_pivot_count += 1
            double_factor = sp.Poly(
                1 + r * t, r, t, w, domain=sp.QQ
            ).monic()
            self.assertTrue(face_unresolved)
            self.assertTrue(
                all(
                    sp.Poly(
                        sp.sympify(item["factor"]),
                        r,
                        t,
                        w,
                        domain=sp.QQ,
                    ).monic()
                    == double_factor
                    for item in face_unresolved
                )
            )
            self.assertIsNotNone(double_face)
            double_polynomial = sp.Poly(
                sp.sympify(double_face["determinant_factorization"]),
                t,
                w,
                domain=sp.QQ,
            )
            double_covered, double_exponents, double_unresolved = (
                self.module.double_pivot_face_factorization(double_polynomial)
            )
            self.assertTrue(double_covered)
            self.assertEqual(double_unresolved, [])
            self.assertEqual(
                double_exponents,
                double_face["allowed_boundary_factor_exponents"],
            )
        self.assertEqual(
            (direct_count, pivot_count, double_pivot_count), (193, 357, 50)
        )

    def test_internal_nilpotent_face_is_imported_and_boundary_is_explicit(self):
        self.assertEqual(
            self.payload["face_certificates"],
            {
                "nilpotent_overlapping_23_32": (
                    "EXACT_ALL_OVERLAPPING_23_32_NILPOTENT_SHEAR_INVALID_TAIL_MINORS"
                )
            },
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("singleton-versus-triple", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
