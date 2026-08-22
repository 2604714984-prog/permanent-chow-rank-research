from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_hessian_relation_kernel.py"
DATA = ROOT / "data" / "n7_packet_a_hessian_relation_kernel.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_hessian_relation_kernel", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAHessianRelationKernelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_diagonal_selector(self) -> None:
        selector = MODULE.diagonal_selector()
        self.assertEqual(selector.shape, (49, 7))
        self.assertEqual(selector.T * selector, sp.eye(7))

    def test_same_row_witness_formula(self) -> None:
        term = MODULE.hessian.permanent_block.column_uniform_factors(
            (1, 2, 3, 4, 5, 6, 7)
        )
        witness = MODULE.same_row_witness_block(
            (term,), (sp.Rational(2, 3),), (0, 1)
        )
        omitted_pair_index = MODULE.hessian.OMITTED_PAIR_TO_SUBSET_INDEX[(0, 1)]
        self.assertEqual(witness.shape, (21, 7))
        self.assertEqual(witness[omitted_pair_index, 0], sp.Rational(2, 3))

    def test_factorwise_zero_is_exactly_streamed(self) -> None:
        factors = tuple(
            tuple(int(variable == row * 7) for variable in range(49))
            for row in range(7)
        )
        equations = MODULE.hard_residual_equations_for_term(factors)
        self.assertEqual(len(equations), 3087)
        self.assertFalse(any(equations))
        self.assertTrue(MODULE.witness_is_zero_factorwise((factors,)))

    def test_payload_dimensions_and_boundary(self) -> None:
        identity = self.payload["universal_global_matrix_identity"]
        self.assertEqual(identity["cross_column_witness_matrix_shape"], [1029, 147])
        hard = self.payload["exact_hard_residual_component"]
        self.assertEqual(hard["factorwise_equation_count_before_dependencies"], 151263)
        boundary = self.payload["torus_projection_boundary"]
        self.assertEqual(boundary["full_A5_row_count"], 2869685)
        self.assertEqual(boundary["one_torus_projection_row_count"], 462)

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
