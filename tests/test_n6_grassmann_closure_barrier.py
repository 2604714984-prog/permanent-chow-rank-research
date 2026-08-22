from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_grassmann_closure_barrier.py"
FROZEN = ROOT / "data" / "n6_grassmann_closure_barrier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_grassmann_barrier", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class GrassmannClosureBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_nonzero_fibers_are_actual_complementary_full_frames(self):
        for row in self.payload["family"]["nonzero_parameters_replayed"]:
            self.assertEqual(row["factor_plane_sum_rank"], 12)
            self.assertEqual(row["full_frame_sum_rank"], 30)
            self.assertTrue(row["D_contained_in_full_frame_sum"])
            self.assertEqual(row["symmetric_square_sum_rank"], 42)
            self.assertTrue(row["D_contained_in_symmetric_square_sum"])
            self.assertTrue(row["normalized_section_difference_equals_fixed_D"])
            self.assertTrue(row["quotient_images_are_equal"])

    def test_special_fiber_exhibits_both_nonclosed_incidences(self):
        special = self.payload["family"]["special_fiber"]
        self.assertEqual(special["colliding_factor_plane_rank"], 6)
        self.assertEqual(special["fixed_D_derivative_rank"], 12)
        self.assertFalse(special["derivative_contained_in_actual_plane_sum"])
        self.assertFalse(special["D_contained_in_actual_full_frame_sum"])
        self.assertEqual(special["colliding_symmetric_square_sum_rank"], 21)
        self.assertFalse(special["D_contained_in_actual_symmetric_square_sum"])

    def test_first_order_and_flat_data_repair_this_family(self):
        special = self.payload["family"]["special_fiber"]
        self.assertEqual(special["first_order_relative_graph_map_rank"], 6)
        self.assertEqual(special["flat_limit_factor_sum_rank"], 12)
        self.assertTrue(special["D_derivative_contained_in_flat_factor_sum"])
        self.assertEqual(special["flat_limit_full_frame_sum_rank"], 30)
        self.assertTrue(special["D_contained_in_flat_full_frame_sum"])

    def test_fixed_pair_embeds_in_standard_b50_hook(self):
        hook = self.payload["standard_b50_hook_embedding"]
        self.assertEqual(hook["standard_b50_hook_quadratic_dimension"], 75)
        self.assertTrue(hook["D_is_contained_in_hook"])
        self.assertEqual(hook["standard_b50_hook_second_shadow_dimension"], 23)
        self.assertTrue(hook["D_shadow_is_contained_in_hook_shadow"])


if __name__ == "__main__":
    unittest.main()
