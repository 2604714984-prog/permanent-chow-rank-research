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
        / "n7_mixed_glynn_singleton_overlap_rank_one_update_tail_rank.py"
    )
    spec = importlib.util.spec_from_file_location("n7_singleton_overlap", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SingletonOverlapRankOneUpdateTailRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_singleton_overlap_rank_one_update_tail_rank.json"
            ).read_text(encoding="utf-8")
        )

    def test_candidate_inventory_covers_both_orientations(self):
        self.assertEqual(self.module.CANDIDATE_COUNT, 300)
        self.assertEqual(self.payload["candidate_count"], 300)
        actual = {
            (
                row["orientation"],
                row["shared_coordinate"],
                row["extra_coordinate"],
                row["identity_count"],
            )
            for row in self.payload["rows"]
        }
        expected = {
            (orientation, shared, extra, identity_count)
            for (orientation, shared, extra), identity_count in self.module.candidates()
        }
        self.assertEqual(actual, expected)
        self.assertEqual(
            {
                orientation: sum(row["orientation"] == orientation for row in self.payload["rows"])
                for orientation in ("left_singleton", "right_singleton")
            },
            {"left_singleton": 150, "right_singleton": 150},
        )

    def test_rank_one_determinant_identities(self):
        s, t = self.module.parameter_symbols()
        left_matrix = sp.eye(2) + sp.Matrix([1, 0]) * sp.Matrix(
            [[t * s, t]]
        )
        right_matrix = sp.eye(2) + sp.Matrix([1, s]) * sp.Matrix(
            [[t, 0]]
        )
        self.assertEqual(sp.expand(left_matrix.det() - (1 + s * t)), 0)
        self.assertEqual(sp.expand(right_matrix.det() - (1 + t)), 0)

    def test_every_row_uses_one_allowed_exact_minor(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_ORIENTED_SINGLETON_OVERLAP_INVERTIBLE_RANK_ONE_UPDATE_MINORS",
        )
        s, t = self.module.parameter_symbols()
        for row in self.payload["rows"]:
            self.assertEqual(row["status"], self.module.ROW_STATUS)
            self.assertEqual(row["attempt_count"], 1)
            self.assertEqual(row["failed_attempts"], [])
            minor = row["selected_minor"]
            polynomial = sp.Poly(
                sp.sympify(minor["determinant_factorization"]),
                s,
                t,
                domain=sp.QQ,
            )
            covered, exponents, unresolved = (
                self.module.allowed_boundary_factorization(
                    polynomial, row["orientation"]
                )
            )
            self.assertTrue(covered)
            self.assertEqual(unresolved, [])
            self.assertEqual(
                exponents, minor["allowed_boundary_factor_exponents"]
            )

    def test_face_certificates_and_claim_boundary(self):
        self.assertEqual(
            self.payload["face_certificates"],
            {
                "elementary_shear": "EXACT_ALL_ELEMENTARY_SHEAR_INVALID_TAIL_MINORS",
                "invertible_monomial": "EXACT_MONOMIAL_TRANSFORM_PACKET_CLASSIFICATION",
            },
        )
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("both orientations", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
