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
    raise RuntimeError("could not load W-01 through W-03 evaluator")
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
        self.assertFalse(row["no_coordinate_vector_in_schur_span_mod_prime"])

    def test_dense_weight_control(self) -> None:
        relation3 = np.asarray([[1], [1], [1]], dtype=np.int64)
        relation4 = np.asarray([[1], [1], [1]], dtype=np.int64)
        row = MODULE.evaluate_relations(relation3, relation4, 65521)
        self.assertEqual(row["coordinate_membership_indices"], [])
        self.assertEqual(row["weight_space_dimension"], 2)
        self.assertTrue(row["no_coordinate_vector_in_schur_span_mod_prime"])

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


if __name__ == "__main__":
    unittest.main()
