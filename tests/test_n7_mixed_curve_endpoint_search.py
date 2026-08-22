#!/usr/bin/env python3

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "n7_mixed_curve_endpoint_search",
    ROOT / "scripts" / "n7_mixed_curve_endpoint_search.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MixedCurveEndpointTest(unittest.TestCase):
    def test_known_endpoint_weight(self) -> None:
        weights = (1, 2, 3, 4, 5, 12)
        self.assertEqual(MODULE.exact_curve_rank(weights, 3), 30)
        self.assertEqual(MODULE.exact_curve_rank(weights, 4), 42)
        self.assertEqual(MODULE.exact_curve_rank(weights, 6), 42)

    def test_frozen_summary(self) -> None:
        payload = json.loads(
            (ROOT / "data" / "n7_mixed_curve_endpoint_search.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload["weight_candidate_count"], 134596)
        self.assertEqual(payload["exact_endpoint_profile_count"], 130)
        self.assertEqual(payload["endpoint_middle_rank_sum"], 2870)
        self.assertEqual(payload["graph_point_code_middle_profile_sum"], 72)
        self.assertEqual(payload["zero_degree_six_increment_count"], 0)
        self.assertEqual(payload["minimum_degree_six_target_increment"], 49)
        self.assertTrue(
            all(sum(row["point_code_hilbert_3_to_6"][:2]) == 72 for row in payload["results"])
        )
        self.assertTrue(
            all(row["rectangular_middle_rank_sum"] == 2870 for row in payload["results"])
        )


if __name__ == "__main__":
    unittest.main()
