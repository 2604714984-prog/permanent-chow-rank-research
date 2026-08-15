from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "general_exact_product_shadow.py"
)
SPEC = importlib.util.spec_from_file_location("general_exact_product_shadow", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralExactProductShadowTests(unittest.TestCase):
    def test_n6_regression(self) -> None:
        shadow = MODULE.ExactProductShadow(6, 3)
        expected = {
            40: 60,
            46: 72,
            50: 75,
            53: 81,
            60: 84,
            65: 87,
        }
        self.assertEqual(
            {value: shadow.minimum(value).shadow_size for value in expected},
            expected,
        )

    def test_n7_exact_threshold(self) -> None:
        shadow = MODULE.ExactProductShadow(7, 4)
        row_238 = shadow.minimum(238)
        row_239 = shadow.minimum(239)
        self.assertEqual(row_238.shadow_size, 452)
        self.assertEqual(row_239.shadow_size, 456)
        self.assertEqual(sum(row_238.minimizing_partition), 238)
        self.assertEqual(sum(row_239.minimizing_partition), 239)

    def test_perm7_lower_bound(self) -> None:
        result = MODULE.exact_multishadow_bound(7, 3, 13)
        self.assertEqual(result["derivative_shadow_threshold"], 455)
        self.assertEqual(result["exact_intersection_cap"], 238)
        self.assertEqual(result["first_excluded_size"], 239)
        self.assertEqual(result["residual_term_count"], 29)
        self.assertEqual(result["exact_multishadow_lower_bound"], 42)

    def test_frozen_payload(self) -> None:
        payload = MODULE.build_payload()
        self.assertIn("core_sha256", payload)
        self.assertEqual(
            payload["n7_application"]["exact_multishadow_lower_bound"],
            42,
        )


if __name__ == "__main__":
    unittest.main()
