from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_row_pure_multigrade_exclusion.py"
FROZEN = ROOT / "data" / "n6_row_pure_multigrade_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_row_pure_multigrade", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RowPureMultigradeExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_squarefree_caps(self):
        rows = self.payload["dimension_rows"]
        self.assertEqual(
            [row["squarefree_row_cap"] for row in rows],
            [0, 1, 3, 6, 10, 15],
        )

    def test_five_plane_forces_shadow_twenty_four(self):
        self.assertEqual(self.payload["minimum_row_support_dimension"], 4)
        self.assertEqual(self.payload["minimum_row_pure_shadow_dimension"], 24)
        self.assertEqual(self.payload["b50_equality_shadow_dimension"], 23)
        self.assertEqual(self.payload["shadow_gap"], 1)

    def test_status_and_conditional_boundary(self):
        self.assertIn(
            "PURE_CONDITIONAL_ROW_PURE_MULTIGRADE_EXCLUSION",
            self.payload["status"],
        )
        scope = self.payload["hypothesis"]["valuation_scope"]
        self.assertIn("Arbitrary valuation levels", scope)
        self.assertIn("only when", scope)
        boundary = self.payload["claim_boundary"]
        self.assertIn("partial-rank Smith packets", boundary)
        self.assertIn("column jets", boundary)
        self.assertIn("arbitrary collision trees", boundary)


if __name__ == "__main__":
    unittest.main()
