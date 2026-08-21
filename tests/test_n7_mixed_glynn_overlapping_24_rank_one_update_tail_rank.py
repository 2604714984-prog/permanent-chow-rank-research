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
        / "n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlapping_24", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Overlapping24RankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory_covers_both_orientations(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 900)
        self.assertEqual(self.payload["candidate_count"], 900)
        actual = {
            (
                row["shape"],
                tuple(row["core_support"]),
                tuple(row["extra_coordinates"]),
                row["identity_count"],
            )
            for row in self.payload["rows"]
        }
        expected = {
            (shape, core, extras, identity_count)
            for ((shape, core, extras), identity_count) in self.module.candidates()
        }
        self.assertEqual(actual, expected)
        self.assertEqual(
            {
                shape: sum(row["shape"] == shape for row in self.payload["rows"])
                for shape in ("extra_left", "extra_right")
            },
            {"extra_left": 450, "extra_right": 450},
        )

    def test_rank_one_determinant_and_face_substitutions(self):
        r, s, t, w, x = self.module.parameter_symbols()
        extra_right = sp.eye(4) + sp.Matrix([1, r, 0, 0]) * sp.Matrix(
            [[t * s, t, t * w, t * x]]
        )
        extra_left = sp.eye(4) + sp.Matrix([1, r, w, x]) * sp.Matrix(
            [[t * s, t, 0, 0]]
        )
        for matrix in (extra_right, extra_left):
            self.assertEqual(
                sp.expand(matrix.det() - (1 + t * (r + s))), 0
            )

        supports = (
            ("extra_right", (0, 1), (2, 3)),
            ("extra_left", (0, 1), (2, 3)),
        )
        for support in supports:
            for coordinate in range(6):
                assignment = (0, 0, 0, 0, 0, coordinate + 1)
                original = self.module.assignment_feature(
                    assignment, 5, support, r, s, t, w, x
                )
                pivot = self.module.pivot_face_assignment_feature(
                    assignment, 5, support, r, t, w, x
                )
                self.assertTrue(
                    all(
                        sp.cancel(sp.sympify(left).subs(s, -1 / t) - right) == 0
                        for left, right in zip(original, pivot)
                    )
                )
                double = self.module.double_pivot_face_assignment_feature(
                    assignment, 5, support, t, w, x
                )
                power = int(coordinate == support[1][1])
                self.assertTrue(
                    all(
                        sp.cancel(
                            t**power
                            * sp.sympify(left).subs({s: -1 / t, r: -1 / t})
                            - right
                        )
                        == 0
                        for left, right in zip(original, double)
                    )
                )

    def test_every_dense_row_has_exact_stratified_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAPPING_24_42_DENSE_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        r, s, t, w, x = self.module.parameter_symbols()
        counts = {"primary": 0, "pivot": 0, "double": 0}
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            primary = row["primary_minor"]
            primary_poly = sp.Poly(
                sp.sympify(primary["determinant_factorization"]),
                r,
                s,
                t,
                w,
                x,
                domain=sp.QQ,
            )
            primary_covered, exponents, unresolved, _factorization = (
                self.module.factorization_record(primary_poly)
            )
            self.assertEqual(
                exponents, primary["allowed_boundary_factor_exponents"]
            )
            self.assertEqual(unresolved, primary["unresolved_factors"])

            face = row["pivot_face_minor"]
            double_face = row["double_pivot_face_minor"]
            if face is None:
                counts["primary"] += 1
                self.assertTrue(primary_covered)
                self.assertIsNone(double_face)
                continue
            self.assertFalse(primary_covered)
            face_poly = sp.Poly(
                sp.sympify(face["determinant_factorization"]),
                r,
                t,
                w,
                x,
                domain=sp.QQ,
            )
            face_covered, face_exponents, face_unresolved, _factorization = (
                self.module.pivot_face_factorization(face_poly)
            )
            self.assertEqual(
                face_exponents, face["allowed_boundary_factor_exponents"]
            )
            self.assertEqual(face_unresolved, face["unresolved_factors"])
            if double_face is None:
                counts["pivot"] += 1
                self.assertTrue(face_covered)
                continue
            counts["double"] += 1
            self.assertFalse(face_covered)
            double_poly = sp.Poly(
                sp.sympify(double_face["determinant_factorization"]),
                t,
                w,
                x,
                domain=sp.QQ,
            )
            covered, double_exponents, double_unresolved, _factorization = (
                self.module.double_pivot_face_factorization(double_poly)
            )
            self.assertTrue(covered)
            self.assertEqual(
                double_exponents,
                double_face["allowed_boundary_factor_exponents"],
            )
            self.assertEqual(double_unresolved, [])
        self.assertEqual(counts, {"primary": 325, "pivot": 527, "double": 48})

    def test_dense_nilpotent_faces_are_imported_exactly(self):
        self.assertEqual(
            self.payload["dense_face_certificates"],
            self.module.dense_face_certificates(),
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("Laurent-torus audit", boundary)
        self.assertIn("projective support faces", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
