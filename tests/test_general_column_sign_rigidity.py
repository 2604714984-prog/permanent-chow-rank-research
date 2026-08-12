from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "general_column_sign_rigidity_audit.py"
INDEPENDENT_PATH = (
    ROOT / "scripts" / "general_column_sign_rigidity_independent.py"
)
FROZEN_PATH = ROOT / "data" / "general_column_sign_rigidity.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PRIMARY = load_module("general_column_sign_rigidity_audit", PRIMARY_PATH)
INDEPENDENT = load_module(
    "general_column_sign_rigidity_independent",
    INDEPENDENT_PATH,
)


class GeneralColumnSignRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = PRIMARY.build_payload()
        cls.independent = INDEPENDENT.build_payload()
        cls.frozen = json.loads(FROZEN_PATH.read_text(encoding="utf-8"))

    def test_boolean_slice_delta(self) -> None:
        for n in range(2, 11):
            target = PRIMARY.slice_target_mask(n)
            observed = [
                PRIMARY.permanent_slice_coefficient(n, mask)
                for mask in range(1 << (n - 1))
            ]
            expected = [0] * (1 << (n - 1))
            expected[target] = 1
            self.assertEqual(observed, expected)

    def test_every_representative_restricts_to_its_character(self) -> None:
        n = 6
        for signature in range(32):
            expected = [
                Fraction(value)
                for value in PRIMARY.slice_vector_from_signature(n, signature)
            ]
            sign_matrix = PRIMARY.representative_normalized_sign_matrix(
                n,
                signature,
                5,
            )
            anchored_matrix = PRIMARY.representative_anchored_matrix(
                n,
                signature,
                4,
            )
            self.assertEqual(PRIMARY.normalized_slice_vector(sign_matrix), expected)
            self.assertEqual(
                PRIMARY.normalized_slice_vector(anchored_matrix),
                expected,
            )

    def test_primary_payload_matches_compact_frozen_summary(self) -> None:
        rows = self.payload["degrees"]
        encoded = (
            json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(encoded).hexdigest(),
            self.frozen["all_degree_rows_sha256"],
        )
        self.assertEqual(self.payload["status"], self.frozen["status"])
        self.assertEqual(self.payload["field"], self.frozen["field"])
        self.assertEqual(
            self.payload["tested_degree_range"],
            self.frozen["tested_degree_range"],
        )
        self.assertEqual(self.payload["theorem"], self.frozen["theorem"])
        self.assertEqual(
            self.payload["n6_consequences"],
            self.frozen["n6_consequences"],
        )
        n6 = next(row for row in rows if row["n"] == 6)
        self.assertEqual(n6, self.frozen["n6"])
        self.assertEqual(len(rows), self.frozen["validated_degree_count"])
        self.assertEqual(
            sum(
                row["normalized_sign_slice_coefficients_checked"]
                for row in rows
            ),
            self.frozen["total_normalized_sign_slice_coefficients_checked"],
        )
        self.assertEqual(
            sum(
                row["anchored_rational_slice_coefficients_checked"]
                for row in rows
            ),
            self.frozen["total_anchored_rational_slice_coefficients_checked"],
        )
        self.assertEqual(
            sum(
                row.get("glynn_full_assignment_check", {}).get(
                    "assignment_checks",
                    0,
                )
                for row in rows
            ),
            self.frozen["total_glynn_assignment_checks_n2_through_n6"],
        )

    def test_n6_exact_restricted_minimum(self) -> None:
        n6 = next(row for row in self.payload["degrees"] if row["n"] == 6)
        self.assertEqual(n6["normalized_column_sign_family_size"], 1 << 30)
        self.assertEqual(n6["diagonal_signature_count"], 32)
        self.assertEqual(n6["terms_per_signature"], 1 << 25)
        self.assertEqual(n6["forced_nonzero_signature_aggregates"], 32)
        self.assertEqual(n6["exact_column_sign_rank"], 32)
        self.assertEqual(n6["exact_row_sign_rank"], 32)
        self.assertEqual(
            n6["glynn_full_assignment_check"],
            {
                "assignment_checks": 46_656,
                "permutation_assignments": 720,
                "zero_nonpermutation_assignments": 45_936,
            },
        )

    def test_independent_replay(self) -> None:
        self.assertEqual(
            self.independent["status"],
            "GENERAL_COLUMN_SIGN_RIGIDITY_INDEPENDENT_PASS",
        )
        self.assertEqual(self.independent["walsh_matrix_shape"], [32, 32])
        self.assertEqual(self.independent["walsh_gram_diagonal"], 32)
        self.assertEqual(self.independent["walsh_gram_off_diagonal"], 0)
        self.assertEqual(
            self.independent["unique_nonzero_aggregate_coefficients"],
            32,
        )
        self.assertEqual(self.independent["exact_restricted_rank"], 32)

    def test_proof_scripts_do_not_use_bare_assert(self) -> None:
        for path in (PRIMARY_PATH, INDEPENDENT_PATH):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            bare_asserts = [
                node for node in ast.walk(tree) if isinstance(node, ast.Assert)
            ]
            self.assertEqual(bare_asserts, [], path)


if __name__ == "__main__":
    unittest.main()
