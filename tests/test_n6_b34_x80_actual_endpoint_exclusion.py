from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b34_x80_actual_endpoint_exclusion.py"
FROZEN = ROOT / "data" / "n6_b34_x80_actual_endpoint_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6083_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6B34X80ActualEndpointExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_endpoint_inputs(self) -> None:
        row = self.payload["endpoint_input"]
        self.assertEqual((row["central_dimension"], row["first_shadow_dimension"], row["second_shadow_dimension"]), (80, 90, 24))
        self.assertTrue(row["second_shadow_is_partitioned_4_by_6_product_or_transpose"])

    def test_sign_cube_exact_rank(self) -> None:
        row = self.payload["invertible_block_branch"]["sign_cube_exact_certificate"]
        self.assertEqual((row["projective_sign_line_count"], row["seven_of_eight_case_count"]), (8, 8))
        self.assertTrue(row["all_cases_have_rank_signature_7_6_7_3"])
        self.assertTrue(all(case["cubic_squarefree_intersection_dimension"] == 3 for case in row["rows"]))

    def test_two_block_branches_are_excluded(self) -> None:
        invertible = self.payload["invertible_block_branch"]
        singular = self.payload["all_singular_branch"]
        self.assertEqual((invertible["resulting_cubic_permanent_intersection_dimension"], invertible["contradicts_required_dimension"]), (60, 80))
        self.assertEqual((singular["factor_frame_rank_upper"], singular["required_factor_frame_rank"]), (4, 6))
        self.assertTrue(singular["contradiction"])

    def test_strict_boundary(self) -> None:
        self.assertIn("f_A<=79", self.payload["strict_conclusion"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude global b=34", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)


if __name__ == "__main__":
    unittest.main()
