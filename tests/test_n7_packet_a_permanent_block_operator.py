from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_permanent_block_operator.py"
DATA = ROOT / "data" / "n7_packet_a_permanent_block_operator.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_permanent_block_operator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAPermanentBlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.controls = cls.payload["labelled_equality_incidence_controls"]

    def test_general_projection_matches_column_uniform_formula(self) -> None:
        row = self.payload["general_factor_plane_projection_control"]
        self.assertEqual(row["projected_block_shape"], [924, 7])
        self.assertEqual(row["nonzero_labelled_subset_columns"], [0])
        self.assertEqual(row["non_column_uniform_nonzero_subset_columns"], [0, 6])
        self.assertTrue(row["column_uniform_formula_matches_general_projection"])
        self.assertTrue(row["off_column_factor_coefficient_exercised"])

    def test_glynn49_has_permanent_specific_defect(self) -> None:
        row = self.controls["glynn49_truncation"]
        self.assertEqual(row["QQ_exact_Walsh_target_quotient_rank"], 35)
        self.assertEqual(
            row["finite_field_streamed_target_incidence"]["target_quotient_rank"], 35
        )
        self.assertEqual(row["decision"], "PERMANENT_SPECIFIC_NONZERO_TARGET_DEFECT")

    def test_glynn64_is_only_a_projected_survivor(self) -> None:
        row = self.controls["glynn64_positive_span_control"]
        self.assertEqual(row["QQ_exact_Walsh_target_quotient_rank"], 0)
        self.assertTrue(
            row["finite_field_streamed_target_incidence"]["projected_survivor"]
        )
        self.assertEqual(row["decision"], "PROJECTED_EXACT_CONTROL_SURVIVOR")

    def test_streaming_and_resource_bound(self) -> None:
        preflight = self.payload["resource_preflight"]
        self.assertEqual(preflight["symmetrized_rows_per_block"], 924)
        self.assertFalse(preflight["vertical_6468_row_matrix_materialized"])
        for name in ("glynn49_truncation", "glynn64_positive_span_control"):
            streamed = self.controls[name]["finite_field_streamed_target_incidence"]
            self.assertTrue(streamed["streamed_without_vertical_materialization"])
            self.assertEqual(len(streamed["blocks"]), 7)

    def test_non_tensor_boundary_control(self) -> None:
        row = self.controls["non_tensor_sylvester_control"]
        self.assertTrue(row["condition_holds"])
        self.assertFalse(row["tensor_split"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
