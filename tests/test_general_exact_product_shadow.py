from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "general_exact_product_shadow.py"
INDEPENDENT_PATH = (
    ROOT / "scripts" / "general_exact_product_shadow_independent.py"
)
DATA_PATH = ROOT / "data" / "general_exact_product_shadow.json"

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
        self.assertEqual(row_238.partition_count, 2)
        self.assertEqual(row_239.partition_count, 8)
        self.assertEqual(sum(row_238.minimizing_partition), 238)
        self.assertEqual(sum(row_239.minimizing_partition), 239)

    def test_perm7_lower_bound(self) -> None:
        result = MODULE.exact_multishadow_bound(7, 3, 13)
        self.assertEqual(result["derivative_shadow_threshold"], 455)
        self.assertEqual(result["exact_intersection_cap"], 238)
        self.assertEqual(result["first_excluded_size"], 239)
        self.assertEqual(result["selected_output_first_koszul_bound"], 35)
        self.assertEqual(result["global_first_koszul_bound"], 36)
        self.assertEqual(result["residual_term_count"], 29)
        self.assertEqual(result["exact_multishadow_lower_bound"], 42)

    def test_n8_exact_threshold(self) -> None:
        shadow = MODULE.ExactProductShadow(8, 4)
        row_560 = shadow.minimum(560)
        row_561 = shadow.minimum(561)
        self.assertEqual(row_560.shadow_size, 784)
        self.assertEqual(row_561.shadow_size, 793)
        self.assertEqual(row_560.partition_count, 2)
        self.assertEqual(row_561.partition_count, 2)
        self.assertEqual(sum(row_560.minimizing_partition), 560)
        self.assertEqual(sum(row_561.minimizing_partition), 561)

    def test_perm8_lower_bound(self) -> None:
        result = MODULE.exact_multishadow_bound(8, 4, 14)
        self.assertEqual(result["derivative_shadow_threshold"], 784)
        self.assertEqual(result["exact_intersection_cap"], 560)
        self.assertEqual(result["first_excluded_size"], 561)
        self.assertEqual(result["selected_output_first_koszul_bound"], 71)
        self.assertEqual(result["global_first_koszul_bound"], 71)
        self.assertEqual(result["residual_term_count"], 63)
        self.assertEqual(result["exact_multishadow_lower_bound"], 77)

    def test_frozen_payload_matches_generator(self) -> None:
        payload = MODULE.build_payload()
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, payload)
        self.assertEqual(
            payload["n7_application"]["exact_multishadow_lower_bound"],
            42,
        )
        self.assertEqual(
            payload["n8_application"]["exact_multishadow_lower_bound"],
            77,
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_EXACT_PRODUCT_SHADOW_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=42", completed.stdout)
        self.assertIn("independent_perm8_lower_bound=77", completed.stdout)


if __name__ == "__main__":
    unittest.main()
