from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_equality_locus_gradient.py"
DATA = ROOT / "data" / "n7_packet_a_equality_locus_gradient.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_equality_locus_gradient", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAEqualityLocusGradientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_forced_transport_uses_factor_coefficients(self) -> None:
        point = (1, 2, 3, 4, 5, 6, 7)
        term = MODULE.block.column_uniform_factors(point)
        transport = MODULE.forced_transport_block((term,), (MODULE.sp.Rational(3, 5),), 6)
        self.assertEqual(transport.shape, (7, 7))
        nonzero_rows = [row for row in range(7) if any(transport[row, column] for column in range(7))]
        self.assertEqual(nonzero_rows, [0])
        self.assertEqual(list(transport.row(0)), [MODULE.sp.Rational(3 * value, 5) for value in point])

    def test_glynn49_forced_gradient_defect(self) -> None:
        row = self.payload["mandatory_existing_controls"]["glynn49_truncation"]
        self.assertEqual(row["one_omitted_column_residual_rank"], 5)
        self.assertEqual(row["seven_disjoint_column_blocks_total_residual_rank"], 35)
        self.assertFalse(row["forced_gradient_equations_hold"])

    def test_glynn64_forced_gradient_survivor(self) -> None:
        row = self.payload["mandatory_existing_controls"]["glynn64_identity_control"]
        self.assertEqual(row["one_omitted_column_residual_rank"], 0)
        self.assertTrue(row["forced_gradient_equations_hold"])

    def test_residual_component_and_missing_invariant_are_explicit(self) -> None:
        schema = self.payload["exact_incidence_schema"]
        self.assertEqual(schema["forced_gradient_component"]["name"], "Z_A_grad")
        self.assertEqual(
            schema["forced_gradient_component"]["displayed_scalar_equation_count_before_dependencies"],
            45276,
        )
        self.assertTrue(schema["aggregate_relation_capacity"]["both_maps_can_be_injective_by_dimension"])
        self.assertIn("syzygy", schema["smallest_missing_invariant"])
        self.assertEqual(
            self.payload["universal_block_defect_decision"],
            "NOT_DERIVED_FROM_CURRENT_HYPOTHESES",
        )

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
