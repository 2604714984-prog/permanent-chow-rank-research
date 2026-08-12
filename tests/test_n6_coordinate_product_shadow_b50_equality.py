from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_coordinate_product_shadow_b50_equality.py"
FROZEN = ROOT / "data" / "n6_coordinate_product_shadow_b50_equality.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_coordinate_b50", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CoordinateProductShadowB50EqualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_ferrers_and_original_degree_profiles(self):
        self.assertEqual(self.payload["minimum_first_product_shadow"], 75)
        self.assertEqual(len(self.payload["minimizing_ferrers_partitions"]), 2)
        self.assertEqual(
            {tuple(row) for row in self.payload["minimizing_ferrers_partitions"]},
            {
                tuple(row)
                for row in self.payload[
                    "original_row_degree_profiles_preserved_by_double_compression"
                ]
            },
        )

    def test_small_kk_equalities(self):
        replay = self.payload["small_equality_replay"]
        self.assertEqual(replay["four_triples_shadow_six_family_count"], 15)
        self.assertTrue(replay["all_four_triple_families_are_complete_on_four_vertices"])
        self.assertEqual(replay["ten_triples_shadow_ten_family_count"], 6)
        self.assertTrue(replay["all_ten_triple_families_are_complete_on_five_vertices"])

    def test_both_hooks_have_50_75_23(self):
        self.assertEqual(
            {
                (
                    row["support_size"],
                    row["first_product_shadow_size"],
                    row["second_product_shadow_size"],
                )
                for row in self.payload["hook_replays"]
            },
            {(50, 75, 23)},
        )


if __name__ == "__main__":
    unittest.main()
