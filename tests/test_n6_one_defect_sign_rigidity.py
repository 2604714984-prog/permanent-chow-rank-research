from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_one_defect_sign_rigidity_audit.py"
FROZEN = ROOT / "data" / "n6_one_defect_sign_rigidity_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_one_defect_sign_rigidity_audit", SCRIPT)


class N6OneDefectSignRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_family_and_sign_span(self) -> None:
        family = self.payload["family"]
        self.assertEqual(family["normalized_sign_vector_count"], 32)
        self.assertEqual(family["unique_term_count"], 5_984)
        self.assertEqual(
            family["indexed_term_count_with_uniform_duplicates"],
            6_144,
        )
        certificate = family["sign_span_certificate"]
        self.assertEqual(certificate["rank_lower_bound"], 6)
        self.assertEqual(certificate["minor_determinant"], -32)

    def test_parity_feature_ranks_and_span(self) -> None:
        certificate = self.payload["parity_fiber_certificate"]
        self.assertEqual(
            certificate["feature_rank_histogram"],
            {"26": 1, "31": 31},
        )
        self.assertEqual(certificate["one_defect_span_dimension"], 987)
        self.assertEqual(certificate["target_parity"], 31)
        self.assertEqual(certificate["target_fiber_size"], 720)
        self.assertTrue(
            certificate["target_fiber_is_exactly_the_permutation_support"]
        )
        rows = certificate["canonical_integer_minor_certificates"]
        self.assertEqual(
            [row["minor_determinant"] for row in rows],
            [-32, 32, -32, -32, -32, 1],
        )
        self.assertEqual(
            [row["rank_lower_bound"] for row in rows],
            [31, 31, 31, 31, 31, 26],
        )

    def test_glynn_identity_and_exact_restricted_rank(self) -> None:
        glynn = self.payload["glynn_upper_bound_certificate"]
        self.assertEqual(glynn["coefficient_denominator"], 32)
        self.assertEqual(glynn["identity_verified_on_all_assignments"], 46_656)
        self.assertEqual(glynn["nonzero_target_coefficients"], 720)
        self.assertEqual(glynn["zero_non_target_coefficients"], 45_936)

        theorem = self.payload["restricted_support_theorem"]
        self.assertEqual(theorem["lower_bound"], 32)
        self.assertEqual(theorem["upper_bound"], 32)
        self.assertEqual(theorem["exact_minimum_nonzero_summands"], 32)

    def test_claim_boundary_is_fail_closed(self) -> None:
        decision = self.payload["route_decision"]
        self.assertEqual(
            decision["one_defect_sign_decomposition_with_at_most_25_terms"],
            "impossible",
        )
        self.assertEqual(
            decision["one_defect_sign_decomposition_with_at_most_31_terms"],
            "impossible",
        )
        self.assertEqual(decision["minimum_inside_restricted_family"], 32)
        self.assertFalse(decision["general_chow_rank_changed"])
        self.assertEqual(decision["full_column_sign_family"], "open")
        self.assertEqual(decision["row_homogeneous_tensor_rank"], "open")

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
