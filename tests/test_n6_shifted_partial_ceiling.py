from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_shifted_partial_ceiling.py"
FROZEN = ROOT / "data" / "n6_shifted_partial_ceiling.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "n6_shifted_partial_ceiling",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ShiftedPartialCeilingTests(unittest.TestCase):
    def test_exact_one_term_examples(self) -> None:
        self.assertEqual(AUDIT.single_term_rank(3, 0), 20)
        self.assertEqual(AUDIT.single_term_rank(3, 3), 140_036)
        self.assertEqual(AUDIT.single_term_rank(6, 0), 1)

    def test_finite_maximum_and_tail(self) -> None:
        payload = AUDIT.build_payload()
        self.assertEqual(
            (
                payload["maximizing_state"]["output_degree"],
                payload["maximizing_state"]["shift"],
            ),
            (3, 3),
        )
        self.assertEqual(
            Fraction(*payload["global_ratio_upper"]),
            Fraction(843_600, 35_009),
        )
        self.assertLess(Fraction(*payload["global_ratio_upper"]), 25)
        self.assertLess(
            Fraction(*payload["tail_ratio_at_start"]),
            Fraction(*payload["global_ratio_upper"]),
        )

    def test_symbolic_tail_monotonicity(self) -> None:
        # After cancellation, R(D+1)/R(D)<1 differs by the constant 210.
        for total_degree in (53, 54, 100, 1_000_000):
            left = (total_degree + 36) * (total_degree - 5)
            right = (total_degree + 1) * (total_degree + 30)
            self.assertEqual(right - left, 210)

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        actual = json.loads(json.dumps(AUDIT.build_payload()))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
