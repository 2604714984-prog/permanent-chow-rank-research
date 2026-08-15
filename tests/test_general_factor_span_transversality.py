from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_factor_span_transversality.py"
FROZEN = ROOT / "data" / "general_factor_span_transversality.json"

SPEC = importlib.util.spec_from_file_location(
    "general_factor_span_transversality",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralFactorSpanTransversalityTests(unittest.TestCase):
    def test_safe_omission_counts(self) -> None:
        expected = {
            (7, 3): 1,
            (8, 3): 1,
            (9, 4): 1,
            (10, 4): 1,
            (11, 5): 2,
            (12, 5): 2,
            (13, 6): 2,
            (14, 6): 2,
            (15, 7): 3,
            (16, 7): 3,
        }
        self.assertEqual(
            {
                key: MODULE.safe_omission_count(*key)
                for key in expected
            },
            expected,
        )

    def test_general_certificate_table(self) -> None:
        rows = MODULE.general_certificate_rows()
        self.assertEqual(
            {
                row["n"]: row["factor_span_refined_lower_bound"]
                for row in rows
            },
            {
                7: 42,
                8: 77,
                9: 142,
                10: 268,
                11: 508,
                12: 970,
                13: 1855,
                14: 3570,
                15: 6882,
                16: 13315,
            },
        )
        for row in rows:
            self.assertLess(
                row["factor_span_dimension_cap"],
                row["square_support_requirement"],
            )
            self.assertLessEqual(
                row["new_fixed_terms"],
                row["global_first_koszul_bound"],
            )

    def test_exact_product_shadow_refinements(self) -> None:
        rows = MODULE.exact_shadow_rows()
        self.assertEqual(
            {row["n"]: row["factor_span_exact_shadow_bound"] for row in rows},
            {7: 43, 8: 78},
        )
        self.assertEqual(
            {row["n"]: row["new_fixed_terms"] for row in rows},
            {7: 14, 8: 15},
        )

    def test_perfect_matching_support_sanity(self) -> None:
        result = MODULE.verify_perfect_matching_union(8)
        self.assertEqual(result["checked_cells"], 203)
        self.assertEqual(result["checked_matchings"], 46232)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, MODULE.build_payload())
        self.assertEqual(
            frozen["core_sha256"],
            "2097bb3dd6e35c8c2af422c655c807629770ae0f9384e56bef74281b2f57337d",
        )


if __name__ == "__main__":
    unittest.main()
