from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_general_operator.py"
DATA = ROOT / "data" / "n7_packet_a_general_operator.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_general_operator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAGeneralOperatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_general_factor_plane_degree_maps(self) -> None:
        control = self.payload["general_factor_plane_control"]
        self.assertEqual(control["factor_matrix_QQ_rank"], 7)
        self.assertEqual(
            [(row["degree"], row["QQ_exact_rank"]) for row in control["degree_maps"]],
            [(2, 21), (5, 21), (6, 7)],
        )

    def test_s2_s5_complement_transport(self) -> None:
        transport = MODULE.complement_transport(2)
        self.assertEqual(transport.shape, (42, 42))
        self.assertEqual(transport.rank(), 42)
        self.assertEqual(transport.T * transport, sp.eye(42))

    def test_inverse_coefficient_transport_and_defect(self) -> None:
        control = self.payload["two_term_exact_control"]
        pairing = control["finite_field_relation_pairing"]
        self.assertEqual(pairing["field"], "F_65521")
        self.assertEqual(pairing["degree_2_kernel_dimension"], 21)
        self.assertEqual(pairing["degree_5_kernel_dimension"], 21)
        self.assertGreater(pairing["inverse_coefficient_pairing_rank"], 0)
        defect = control["QQ_exact_kernel_image_defect"]
        self.assertFalse(defect["condition_holds"])
        self.assertGreater(defect["coupling_defect"], 0)

        direction = self.payload["inverse_coefficient_direction_control"]
        self.assertTrue(direction["QQ_exact_kernel_image_defect"]["condition_holds"])
        direction_pairing = direction["finite_field_relation_pairing"]
        self.assertEqual(direction_pairing["inverse_coefficient_pairing_rank"], 0)
        self.assertEqual(direction_pairing["wrong_coefficient_pairing_rank"], 21)

        terms = (MODULE.coordinate_factors(), MODULE.coordinate_factors())
        expected_nullities = {2: 21, 5: 21, 6: 7}
        for degree, nullity in expected_nullities.items():
            aggregate = MODULE.aggregate_catalectic(terms, degree)
            kernel = MODULE.qq_kernel_basis(aggregate)
            self.assertEqual(kernel.shape, (aggregate.cols, nullity))
            self.assertEqual(aggregate * kernel, sp.zeros(aggregate.rows, nullity))

    def test_qq_target_quotient_operator(self) -> None:
        quotient = self.payload["two_term_exact_control"]["QQ_exact_degree_6_target_quotient"]
        self.assertEqual(quotient["field"], "QQ")
        self.assertEqual(quotient["target_rank"], 2)
        self.assertEqual(quotient["target_quotient_rank"], 1)
        self.assertFalse(quotient["target_contained"])

        aggregate6 = MODULE.aggregate_catalectic(
            (MODULE.coordinate_factors(), MODULE.coordinate_factors()), 6
        )
        targets = sp.Matrix.hstack(aggregate6[:, 0], MODULE.pure_power_target(0, 6))
        _, operator, residual = MODULE.target_quotient_operator_qq(aggregate6, targets)
        self.assertEqual(operator * aggregate6, sp.zeros(operator.rows, aggregate6.cols))
        self.assertEqual(operator * targets, residual)

    def test_resource_preflight_and_boundary(self) -> None:
        preflight = self.payload["resource_preflight"]
        self.assertEqual(preflight["largest_executed_dense_entry_count"], 19404)
        self.assertFalse(preflight["full_49_term_materialization_performed"])
        self.assertEqual(
            self.payload["status"],
            "PACKET_A_GENERAL_OPERATOR_A01_A02_FOUNDATION",
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
