from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_common_rowslice_collision_exclusion.py"
FROZEN = ROOT / "data" / "n6_common_rowslice_collision_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_rowslice_collision", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CommonRowsliceCollisionExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_exact_normal_graph_kernel(self):
        system = self.payload["normal_graph_system"]
        self.assertEqual(system["unknown_count"], 180)
        self.assertEqual(system["equation_count"], 825)
        self.assertEqual(system["exact_QQ_rank"], 175)
        self.assertEqual(system["exact_QQ_nullity"], 5)

    def test_five_direct_leading_spaces_have_shadow_thirty_six(self):
        counts = self.payload["five_color_support_audit"]
        self.assertEqual(counts["five_space_direct_sum_dimension"], 75)
        self.assertEqual(counts["joint_derivative_shadow_dimension"], 36)
        self.assertGreater(
            counts["joint_derivative_shadow_dimension"],
            counts["b50_equality_shadow_dimension"],
        )

    def test_status_and_boundary_are_single_grade(self):
        self.assertIn(
            "PURE_SINGLE_GRADE_COMMON_ROWSLICE_EXCLUSION",
            self.payload["status"],
        )
        scope = self.payload["single_grade_scope"]
        self.assertIn("forces A=0", scope["quotient_gauge_is_eliminated"])
        self.assertIn("flat limit K0", scope["flat_limit_hypothesis"])
        self.assertIn("exactly twenty-three", scope["shadow_twenty_three_is_derived"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("only the shared-grade layer", boundary)
        self.assertIn("leading spaces are dependent", boundary)
        self.assertIn("collision trees", boundary)
        self.assertIn("does not exclude every common-row-slice collision", boundary)


if __name__ == "__main__":
    unittest.main()
