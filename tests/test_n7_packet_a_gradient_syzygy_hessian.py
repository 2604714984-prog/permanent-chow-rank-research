from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_gradient_syzygy_hessian.py"
DATA = ROOT / "data" / "n7_packet_a_gradient_syzygy_hessian.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_gradient_syzygy_hessian", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAGradientSyzygyHessianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_forced_hessian_transport_has_correct_label(self) -> None:
        term = MODULE.permanent_block.column_uniform_factors((1, 2, 3, 4, 5, 6, 7))
        transport = MODULE.forced_hessian_transport(
            (term,), (sp.Rational(2, 3),), (0, 1)
        )
        omitted_pair_index = MODULE.OMITTED_PAIR_TO_SUBSET_INDEX[(0, 1)]
        target_column = MODULE.ORDERED_ROW_PAIRS.index((0, 1))
        self.assertEqual(transport[omitted_pair_index, target_column], sp.Rational(4, 3))
        self.assertEqual(transport.shape, (21, 49))

    def test_same_row_permanent_targets_are_zero(self) -> None:
        target = MODULE.permanent_hessian_target()
        for row in range(7):
            column = MODULE.ORDERED_ROW_PAIRS.index((row, row))
            self.assertEqual(target[:, column], sp.zeros(462, 1))

    def test_mixed_partial_swap_is_exact(self) -> None:
        row = self.payload["universal_lemma"]["executable_QQ_control"]
        self.assertTrue(row["factor_input_is_non_column_uniform"])
        self.assertTrue(row["mixed_partial_symmetry_holds"])
        self.assertEqual(row["residual_shape"], [462, 49])

    def test_gradient_projection_information_loss(self) -> None:
        row = self.payload["gradient_Jacobian_information_loss"]
        self.assertEqual(row["unsymmetrized_one_omitted_column_row_assignments"], 117649)
        self.assertEqual(row["symmetrized_gradient_block_rows"], 924)
        self.assertEqual(row["forgotten_dimensions_before_factor_relations"], 116725)

    def test_minimal_component_is_bounded(self) -> None:
        row = self.payload["exact_minimal_residual_component"]
        self.assertEqual(row["refined_component"], "Z_A_grad_hess")
        self.assertEqual(row["omitted_column_pair_count"], 21)
        self.assertEqual(row["rows_per_forced_hessian_block"], 462)
        self.assertEqual(row["ordered_row_pair_target_columns"], 49)
        self.assertEqual(row["zero_diagonal_row_pair_targets"], 7)
        self.assertEqual(row["largest_single_49_term_block_shape"], [462, 1029])
        self.assertEqual(row["maximum_DP_state_count_per_labelled_product"], 14784)

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
