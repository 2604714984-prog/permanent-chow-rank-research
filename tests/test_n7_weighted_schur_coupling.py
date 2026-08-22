from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_weighted_schur_coupling.py"
FROZEN = ROOT / "data" / "n7_weighted_schur_coupling.json"
SPEC = importlib.util.spec_from_file_location("n7_weighted_schur_coupling", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the W-01 through W-04 fixed-code evaluator")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class WeightedSchurCouplingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload,
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_coordinate_obstruction_control(self) -> None:
        relation3 = np.asarray([[1], [0], [0]], dtype=np.int64)
        relation4 = np.asarray([[1], [0], [0]], dtype=np.int64)
        row = MODULE.evaluate_relations(relation3, relation4, 65521)
        self.assertEqual(row["coordinate_membership_indices"], [0])
        self.assertEqual(row["puncture_rank_drop_indices"], [0])
        self.assertFalse(row["no_coordinate_vector_in_schur_span_mod_prime"])

    def test_dense_weight_control(self) -> None:
        relation3 = np.asarray([[1], [1], [1]], dtype=np.int64)
        relation4 = np.asarray([[1], [1], [1]], dtype=np.int64)
        row = MODULE.evaluate_relations(relation3, relation4, 65521)
        self.assertEqual(row["coordinate_membership_indices"], [])
        self.assertEqual(row["weight_space_dimension"], 2)
        self.assertTrue(row["no_coordinate_vector_in_schur_span_mod_prime"])

    def test_degree_four_separator_control(self) -> None:
        relation3 = np.asarray([[1, 0], [0, 1], [0, 0]], dtype=np.int64)
        relation4 = np.asarray([[1], [0], [0]], dtype=np.int64)
        row = MODULE.evaluate_relations(relation3, relation4, 65521)
        self.assertEqual(row["degree4_separator_indices_mod_prime"], [1, 2])
        self.assertEqual(row["relation3_coordinate_zero_indices"], [2])
        self.assertNotIn(1, row["coordinate_membership_indices"])
        self.assertNotIn(2, row["coordinate_membership_indices"])

    def test_nested_code_gate(self) -> None:
        relation3 = np.asarray([[1], [1], [0]], dtype=np.int64)
        relation4 = np.asarray([[1], [0], [0]], dtype=np.int64)
        with self.assertRaises(ValueError):
            MODULE.evaluate_relations(relation3, relation4, 65521)

    def test_separator_equivalence_from_evaluation_code(self) -> None:
        prime = 65521
        evaluation4 = np.asarray([[1, 0], [0, 1], [0, 1]], dtype=np.int64)
        relation4 = MODULE.coupled.modular_nullspace_columns(evaluation4.T, prime)
        zero_indices = MODULE.coordinate_zero_indices(relation4, prime)
        membership = []
        base_rank = MODULE.coupled.modular_rank(evaluation4, prime)
        for index in range(3):
            unit = np.zeros((3, 1), dtype=np.int64)
            unit[index, 0] = 1
            if MODULE.coupled.modular_rank(
                np.column_stack((evaluation4, unit)), prime
            ) == base_rank:
                membership.append(index)
        self.assertEqual(zero_indices, membership)
        self.assertEqual(membership, [0])

    def test_stabilizer_controls(self) -> None:
        prime = 65521
        empty = np.zeros((4, 0), dtype=np.int64)
        full = np.eye(4, dtype=np.int64)
        ones = np.ones((4, 1), dtype=np.int64)
        coordinate_ideal = np.asarray(
            [[1, 0], [0, 1], [0, 0], [0, 0]], dtype=np.int64
        )
        blocks = np.asarray([[1, 0], [1, 0], [0, 1], [0, 1]], dtype=np.int64)
        self.assertEqual(MODULE.coordinate_stabilizer_dimension(empty, prime), 4)
        self.assertEqual(MODULE.coordinate_stabilizer_dimension(full, prime), 4)
        self.assertEqual(MODULE.coordinate_stabilizer_dimension(ones, prime), 1)
        self.assertEqual(
            MODULE.coordinate_stabilizer_dimension(coordinate_ideal, prime), 4
        )
        self.assertEqual(MODULE.coordinate_stabilizer_dimension(blocks, prime), 2)
        changed_basis = blocks @ np.asarray([[1, 1], [0, 1]], dtype=np.int64)
        self.assertEqual(
            MODULE.coordinate_stabilizer_dimension(changed_basis, prime), 2
        )

    def test_active_shapes_and_profiles(self) -> None:
        expected = {
            "F1": (9, 3, 27),
            "F2-F3": (8, 4, 32),
            "F4-F5": (7, 5, 35),
        }
        for control in self.payload["controls"]:
            for row in control["prime_rows"]:
                self.assertEqual(
                    (row["q3"], row["q4"], row["schur_generator_count"]),
                    expected[control["frontier_profiles"]],
                )
                stabilizers = {
                    "F1": (15, 14, 28, 1),
                    "F2-F3": (22, 21, 21, 1),
                    "F4-F5": (29, 28, 14, 1),
                }
                ambient, zero_count, support_size, effective = stabilizers[
                    control["frontier_profiles"]
                ]
                self.assertEqual(
                    row["ambient_stabilizer_dimension_mod_prime"], ambient
                )
                self.assertEqual(
                    len(row["schur_zero_coordinate_indices_mod_prime"]), zero_count
                )
                self.assertEqual(
                    row["effective_support_size_mod_prime"], support_size
                )
                self.assertEqual(
                    row["effective_support_stabilizer_dimension_mod_prime"], effective
                )
                self.assertEqual(
                    row["effective_support_kneser_lower_bound_mod_prime"], 11
                )
                self.assertTrue(row["effective_support_kneser_equality_mod_prime"])


if __name__ == "__main__":
    unittest.main()
