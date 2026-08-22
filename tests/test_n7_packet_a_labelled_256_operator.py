from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_labelled_256_operator.py"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_labelled_256_operator", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7PacketALabelled256Operator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.controls = cls.payload["mandatory_controls"]

    def test_labelled_dimensions_and_preflight(self) -> None:
        module = self.payload["one_term_module"]
        self.assertEqual((module["D2_dimension"], module["D5_dimension"], module["D6_dimension"]), (21, 21, 7))
        self.assertEqual(module["retained_labelled_dimension_per_term"], 49)
        self.assertEqual(self.payload["largest_materialized_matrix_shape"], [64, 64])

    def test_glynn49_negative_control(self) -> None:
        row = self.controls["glynn_49_truncation_negative_control"]
        self.assertEqual(row["degree_profiles"]["2"]["aggregate_kernel_dimension"], 21 * 27)
        self.assertEqual(row["degree_profiles"]["5"]["aggregate_kernel_dimension"], 0)
        quotient = row["degree_6_permanent_target_quotient"]
        self.assertEqual(quotient["target_intersection_dimension_per_block"], 2)
        self.assertEqual(quotient["total_target_quotient_rank"], 35)
        self.assertFalse(quotient["target_contained"])

    def test_non_tensor_sylvester_equality_control(self) -> None:
        row = self.controls["non_tensor_sylvester_equality_control"]
        self.assertTrue(row["condition_holds"])
        self.assertEqual(row["coupling_defect"], 0)
        self.assertFalse(row["tensor_split"])

    def test_glynn64_positive_control(self) -> None:
        row = self.controls["known_glynn_64_identity_span_positive_control"]
        self.assertEqual(row["degree_profiles"]["6"]["aggregate_rank_per_block"], 64)
        self.assertEqual(
            row["complementary_2_5_relation_pairing"]["restricted_relation_pairing_rank_per_block"],
            0,
        )
        self.assertTrue(row["complementary_2_5_relation_pairing"]["relation_orthogonality_condition_holds"])
        self.assertTrue(row["degree_6_permanent_target_quotient"]["target_contained"])

    def test_inverse_external_coefficient_direction_is_forced(self) -> None:
        rows = self.controls["non_self_inverse_external_coefficient_direction_controls"]
        self.assertEqual([row["coefficients"] for row in rows], [[2, 3], [3, 5], [5, 7]])
        for row in rows:
            self.assertEqual(row["inverse_coefficient_pairing_rank"], 0)
            self.assertEqual(row["wrong_coefficient_pairing_rank"], 1)
            self.assertTrue(row["wrong_direction_changes_condition"])
            self.assertEqual(row["kernel_image_condition"]["coupling_defect"], 0)
            self.assertTrue(row["kernel_image_condition"]["condition_holds"])

    def test_action_metadata_keys_are_unique(self) -> None:
        module = self.payload["one_term_module"]
        self.assertEqual(module["ambient_basis_action"], "Sym^d(g) on the degree-d aggregate target")
        self.assertIn("permutation", module["factor_relabelling_action"])
        self.assertIn("product", module["factor_rescaling_action"])

    def test_scope_is_schema_smoke_not_packet_completion(self) -> None:
        self.assertEqual(
            self.payload["status"],
            "PACKET_A_LABELLED_SCHEMA_AND_MANDATORY_CONTROLS_SMOKE",
        )
        self.assertNotIn("characteristic_zero_ranks", self.payload)
        self.assertEqual(
            self.payload["rank_fields"],
            {
                "Walsh_aggregate_and_target_span_ranks": "Q exact elimination",
                "relation_pairing_and_Sylvester_ranks": "F_65521",
            },
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads((ROOT / "data" / "n7_packet_a_labelled_256_operator.json").read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
