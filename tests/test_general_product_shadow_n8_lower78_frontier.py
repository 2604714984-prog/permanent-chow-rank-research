from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
MODULE_PATH = SCRIPTS / "general_product_shadow_n8_lower78_frontier.py"
DATA_PATH = ROOT / "data" / "general_product_shadow_n8_lower78_frontier.json"

SPEC = importlib.util.spec_from_file_location(
    "general_product_shadow_n8_lower78_frontier",
    MODULE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralProductShadowN8Lower78FrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_complete_scalar_scan(self) -> None:
        summary = self.payload["scan_summary"]
        self.assertEqual(summary["global_first_koszul_bound"], 71)
        self.assertEqual(summary["evaluated_nonvacuous_rows"], 213)
        self.assertEqual(self.payload["maximum_exact_shadow_lower_bound"], 77)
        self.assertEqual(
            summary["per_output_degree"]["4"]["maximizing_fixed_counts"],
            [14, 15, 16, 17, 18, 19],
        )

    def test_selected_frontier(self) -> None:
        selected = self.payload["selected_frontier"]
        self.assertEqual(selected["output_degree"], 4)
        self.assertEqual(selected["fixed_count"], 17)
        self.assertEqual(selected["intersection_cap"], 725)
        self.assertEqual(selected["deficit_to_77_term_contradiction"], 1376)
        self.assertEqual(selected["required_additional_integer_gain"], 1377)
        self.assertEqual(selected["sufficient_realizable_intersection_cap"], 703)

    def test_selected_minimizer_counts(self) -> None:
        minimizers = self.payload["selected_ferrers_minimizers"]
        self.assertEqual(minimizers["cap_size"], 725)
        self.assertEqual(minimizers["cap_shadow"], 950)
        self.assertEqual(minimizers["cap_minimizer_count"], 4)
        self.assertEqual(minimizers["first_excluded_size"], 726)
        self.assertEqual(minimizers["first_excluded_shadow"], 956)
        self.assertEqual(minimizers["first_excluded_minimizer_count"], 4)


if __name__ == "__main__":
    unittest.main()
