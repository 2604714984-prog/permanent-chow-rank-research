from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_q5_two_pencil_dichotomy.py"
FROZEN = ROOT / "data" / "n7_q5_two_pencil_dichotomy.json"
SPEC = importlib.util.spec_from_file_location("n7_q5_two_pencil", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load q5=2 pencil replay")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Q5TwoPencilDichotomyTests(unittest.TestCase):
    def test_frozen_payload(self) -> None:
        self.assertEqual(
            MODULE.build_payload(),
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_flag_normal_form_is_contained(self) -> None:
        beta0 = MODULE.basis_bivector(0, 1)
        beta1 = MODULE.basis_bivector(0, 2)
        self.assertTrue(MODULE.line_is_contained(beta0, beta1))

    def test_transverse_control_has_exactly_two_endpoints(self) -> None:
        beta0 = MODULE.basis_bivector(0, 1)
        beta1 = MODULE.basis_bivector(2, 3)
        quadrics = MODULE.restricted_plucker_quadrics(beta0, beta1)
        self.assertFalse(MODULE.line_is_contained(beta0, beta1))
        self.assertEqual(
            {key: value for key, value in quadrics.items() if any(value)},
            {(0, 1, 2, 3): (0, 1, 0)},
        )

    def test_three_zeros_force_a_binary_quadric_to_vanish(self) -> None:
        # The evaluation matrix at [1:0], [0:1], [1:1] has determinant -1.
        matrix = ((1, 0, 0), (0, 0, 1), (1, 1, 1))
        determinant = (
            matrix[0][0]
            * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1]
            * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2]
            * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
        self.assertEqual(determinant, -1)


if __name__ == "__main__":
    unittest.main()
