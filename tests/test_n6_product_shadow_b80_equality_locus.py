from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_shadow_b80_equality_locus.py"
FROZEN = ROOT / "data" / "n6_product_shadow_b80_equality_locus.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6082_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ProductShadowB80EqualityLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_coordinate_classification(self) -> None:
        row = self.payload["coordinate_fixed_points"]
        self.assertEqual(row["minimum_first_product_shadow"], 90)
        self.assertEqual(row["total_coordinate_fixed_point_count"], 30)
        self.assertTrue(row["original_support_classification_proved_without_reverse_compression"])

    def test_local_initial_ideal(self) -> None:
        for row in self.payload["local_representatives"]:
            self.assertEqual((row["linear_incidence"]["free_dimension"], row["linear_incidence"]["eta_only_root_count"]), (8, 0))
            self.assertEqual(row["linear_incidence"]["free_group_sizes"], [4, 4])
            self.assertEqual(row["grounded_quadratic_initial_forms"]["exact_rank_over_Q"], 12)
            self.assertTrue(row["grounded_quadratic_initial_forms"]["row_span_is_exactly_the_twelve_forbidden_units"])

    def test_symbolic_branches_and_globalization(self) -> None:
        for row in self.payload["local_representatives"]:
            self.assertEqual((row["boolean_branches"]["count"], row["boolean_branches"]["dimension"]), (16, 2))
            self.assertTrue(row["boolean_branches"]["all_first_shadow_symbolic_containments_hold"])
            self.assertTrue(row["boolean_branches"]["all_second_shadow_symbolic_containments_hold"])
        global_row = self.payload["projective_globalization"]
        self.assertEqual((global_row["row_product_component_count"], global_row["transpose_product_component_count"]), (65, 65))

    def test_second_shadow_and_boundary(self) -> None:
        row = self.payload["second_product_shadow"]
        self.assertEqual((row["universal_minimum_at_dimension_90"], row["every_equality_point_has_second_shadow_dimension"]), (24, 24))
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not by itself exclude", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)


if __name__ == "__main__":
    unittest.main()
