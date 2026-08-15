from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_nested_shadow_removal.py"
FROZEN = ROOT / "data" / "general_nested_shadow_removal.json"

SPEC = importlib.util.spec_from_file_location(
    "general_nested_shadow_removal",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralNestedShadowRemovalTests(unittest.TestCase):
    def test_existing_zero_intersection_blocks(self) -> None:
        expected = {
            (7, 3): (1, 2, 1),
            (11, 5): (2, 4, 1),
            (15, 7): (4, 5, 2),
            (16, 7): (3, 6, 1),
        }
        observed = {}
        for key in expected:
            row = MODULE.zero_intersection_block(*key)
            observed[key] = (
                row["safe_terms"],
                row["derivative_order"],
                row["zero_intersection_output_degree"],
            )
        self.assertEqual(observed, expected)

    def test_general_certificate_reuse(self) -> None:
        rows = MODULE.general_rows()
        self.assertEqual(
            {row["n"]: row["nested_shadow_lower_bound"] for row in rows},
            {
                7: 42,
                8: 77,
                9: 142,
                10: 268,
                11: 508,
                12: 970,
                13: 1855,
                14: 3570,
                15: 6883,
                16: 13315,
            },
        )
        n15 = next(row for row in rows if row["n"] == 15)
        self.assertEqual(n15["safe_terms"], 4)
        self.assertEqual(n15["zero_intersection_output_degree"], 2)
        for row in rows:
            self.assertLessEqual(
                row["enlarged_fixed_terms"],
                row["global_first_koszul_bound"],
            )

    def test_exact_product_shadow_reuse(self) -> None:
        rows = MODULE.exact_rows()
        self.assertEqual(
            {row["n"]: row["nested_exact_shadow_bound"] for row in rows},
            {7: 43, 8: 78},
        )
        self.assertEqual(
            {row["n"]: row["enlarged_fixed_terms"] for row in rows},
            {7: 14, 8: 15},
        )

    def test_asymptotic_block_table(self) -> None:
        rows = MODULE.asymptotic_rows()
        self.assertEqual(
            {row["n"]: row["safe_terms"] for row in rows},
            {16: 3, 20: 6, 24: 13, 32: 51, 40: 205, 50: 1199, 64: 14757},
        )

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, MODULE.build_payload())
        self.assertEqual(
            frozen["core_sha256"],
            "7cda45adc0a8610d4703d868b2d0dec0fdc9319e7b24e69daa8187c9b6691b35",
        )


if __name__ == "__main__":
    unittest.main()
