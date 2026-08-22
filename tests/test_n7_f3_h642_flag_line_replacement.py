from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_f3_h642_flag_line_replacement.py"
FROZEN = ROOT / "data" / "n7_f3_h642_flag_line_replacement.json"
SPEC = importlib.util.spec_from_file_location("n7_f3_h642_flag", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load F3,H6=42 flag replacement replay")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class F3H642FlagLineReplacementTests(unittest.TestCase):
    def test_frozen_payload(self) -> None:
        self.assertEqual(MODULE.build_payload(), json.loads(FROZEN.read_text()))

    def test_span_one_support_bound(self) -> None:
        costs = [MODULE.span_one_total_cost(size) for size in range(7, 43)]
        self.assertEqual(max(costs), 42)
        self.assertEqual(min(costs), 7)

    def test_flag_bounds_are_support_independent(self) -> None:
        self.assertEqual(
            {MODULE.flag_total_cost(size, False) for size in range(1, 43)}, {43}
        )
        self.assertEqual(
            {MODULE.flag_total_cost(size, True) for size in range(1, 43)}, {48}
        )

    def test_exceptional_residual_transverse_derivative(self) -> None:
        derivative = MODULE.residual_derivative_coefficients(kappa=11)
        self.assertEqual(derivative["dQ_dM"], (0, 6))
        self.assertEqual(derivative["dQ_dP"], (30, 66))

    def test_exceptional_primitive_full_gradient(self) -> None:
        self.assertEqual(
            MODULE.exceptional_primitive_gradient(),
            {"dF_dP": (6, 5), "dF_dM": (0, 1)},
        )

    def test_every_branch_contradicts_rank_64(self) -> None:
        bounds = MODULE.build_payload()["branch_replacement_bounds"]
        self.assertLess(max(bounds.values()), MODULE.PERMANENT_WARING_RANK)


if __name__ == "__main__":
    unittest.main()
