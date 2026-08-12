from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_linear_restriction_koszul_ceiling.py"
FROZEN = ROOT / "data" / "n6_linear_restriction_koszul_ceiling.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "n6_linear_restriction_koszul_ceiling",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6LinearRestrictionKoszulCeilingTests(unittest.TestCase):
    def test_every_dimension_is_strictly_below_26(self) -> None:
        payload = AUDIT.build_payload()
        self.assertEqual(payload["ambient_dimensions_covered"], [1, 36])
        self.assertLess(Fraction(*payload["global_ratio_upper"]), 26)
        for row in payload["small_dimension_explicit_term_witnesses"]:
            self.assertLess(Fraction(*row["ratio_upper"]), 26)
        for row in payload["dimension_rows_6_through_35"]:
            self.assertLess(Fraction(*row["ratio_upper"]), 26)
            self.assertGreater(row["margin_below_26"], 0)

    def test_derivative_basis_requires_both_matchings(self) -> None:
        active = AUDIT.active_edges(28)
        counts = []
        for degree in (2, 3, 4):
            subsets = tuple(combinations(range(6), degree))
            counts.append(
                sum(
                    AUDIT.derivative_supported(rows, columns, active)
                    for rows in subsets
                    for columns in subsets
                )
            )
        self.assertEqual(counts, [207, 400, 207])
        self.assertNotEqual(active, AUDIT.target_active_edges(28))

    def test_matching_deletion_witness_has_full_derivative_bases(self) -> None:
        active = AUDIT.active_edges(30)
        counts = []
        for degree in (2, 3, 4):
            subsets = tuple(combinations(range(6), degree))
            counts.append(
                sum(
                    AUDIT.derivative_supported(rows, columns, active)
                    for rows in subsets
                    for columns in subsets
                )
            )
        self.assertEqual(counts, [225, 400, 225])

    def test_small_pure_triangular_replay(self) -> None:
        self.assertEqual(
            AUDIT.replay_leading(19),
            AUDIT.LEADING_EXPECTED[19],
        )

    def test_strict_modular_certificate_values(self) -> None:
        self.assertEqual(
            AUDIT.MODULAR_R23_EXPECTED,
            {
                30: 650_316,
                31: 749_786,
                32: 856_000,
                33: 968_883,
                34: 1_088_402,
                35: 1_214_569,
            },
        )

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        actual = json.loads(json.dumps(AUDIT.build_payload()))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
