from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_affine_segre_slice_rank_audit.py"
FROZEN = ROOT / "data" / "general_affine_segre_slice_rank.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_affine_segre_slice_rank_audit", SCRIPT)


class GeneralAffineSegreSliceRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload(12)
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_lagrange_and_closed_form_weights_agree(self) -> None:
        for d in range(1, 13):
            observed = [
                AUDIT.lagrange_top_coefficient_weight(d, point)
                for point in range(d + 1)
            ]
            expected = [
                AUDIT.closed_form_weight(d, point)
                for point in range(d + 1)
            ]
            self.assertEqual(observed, expected)
            self.assertTrue(all(weight != 0 for weight in observed))

    def test_exact_boolean_reconstruction(self) -> None:
        for d in range(1, 10):
            row = AUDIT.lagrange_construction(d)
            self.assertEqual(row["exact_affine_segre_rank"], d + 1)
            self.assertEqual(row["lower_bound_induction_value"], d + 1)
            self.assertEqual(row["construction_point_count"], d + 1)
            self.assertEqual(row["boolean_assignment_checks"], 1 << d)
            coefficients = row["hamming_weight_coefficients"]
            self.assertEqual(
                coefficients,
                [
                    {"numerator": 0, "denominator": 1}
                    for _ in range(d)
                ]
                + [{"numerator": 1, "denominator": 1}],
            )

    def test_anchored_slice_vectors(self) -> None:
        for parameters in (
            [Fraction(2), Fraction(3)],
            [Fraction(-1), Fraction(2, 3), Fraction(5, 7)],
            [Fraction(0), Fraction(4), Fraction(-3), Fraction(1, 2)],
        ):
            vector = AUDIT.anchored_slice_vector(parameters)
            for mask, coefficient in enumerate(vector):
                expected = Fraction(1)
                for index, parameter in enumerate(parameters):
                    if (mask >> index) & 1:
                        expected *= parameter
                self.assertEqual(coefficient, expected)

    def test_compact_frozen_payload(self) -> None:
        self.assertEqual(self.payload["status"], self.frozen["status"])
        self.assertEqual(self.payload["field"], self.frozen["field"])
        self.assertEqual(
            self.payload["tested_tensor_order_range"],
            self.frozen["tested_tensor_order_range"],
        )
        self.assertEqual(
            self.payload["validated_order_count"],
            self.frozen["validated_order_count"],
        )
        self.assertEqual(
            self.payload["deterministic_anchored_slice_coefficients_checked"],
            self.frozen["deterministic_anchored_slice_coefficients_checked"],
        )
        self.assertEqual(self.payload["theorem"], self.frozen["theorem"])
        self.assertEqual(self.payload["n6"], self.frozen["n6"])
        self.assertEqual(
            self.payload["selected_rows"],
            self.frozen["selected_rows"],
        )

        rows = [AUDIT.lagrange_construction(d) for d in range(1, 13)]
        encoded = (
            json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(encoded).hexdigest(),
            self.frozen["all_rows_sha256"],
        )

    def test_n6_contrast(self) -> None:
        self.assertEqual(
            self.payload["n6"],
            {
                "boolean_dimension": 5,
                "anchored_continuous_slice_rank": 6,
                "column_sign_slice_rank": 32,
                "unrestricted_chow_rank_changed": False,
            },
        )

    def test_no_bare_assert_in_proof_script(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"), filename=str(SCRIPT))
        self.assertEqual(
            [node for node in ast.walk(tree) if isinstance(node, ast.Assert)],
            [],
        )


if __name__ == "__main__":
    unittest.main()
