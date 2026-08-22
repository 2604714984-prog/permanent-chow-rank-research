#!/usr/bin/env python3

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MixedGlynnGraphSearchTest(unittest.TestCase):
    def test_frozen_summary(self) -> None:
        payload = json.loads(
            (ROOT / "data" / "n7_mixed_glynn_graph_search.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload["trial_count"], 5000)
        self.assertEqual(payload["identity_control"]["degree_six_target_intersection"], 7)
        self.assertEqual(payload["degree_six_intersection_histogram"], {"0": 5000})
        self.assertEqual(payload["maximum_degree_six_target_intersection"], 0)


if __name__ == "__main__":
    unittest.main()
