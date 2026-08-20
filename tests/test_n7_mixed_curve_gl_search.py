#!/usr/bin/env python3

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MixedCurveGLSearchTest(unittest.TestCase):
    def test_frozen_summary(self) -> None:
        payload = json.loads(
            (ROOT / "data" / "n7_mixed_curve_gl_search.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload["endpoint_weight_profile_count"], 304)
        self.assertEqual(payload["trial_count"], 2000)
        self.assertEqual(payload["degree_six_increment_histogram"], {"49": 2000})
        self.assertEqual(payload["degree_seven_increment_histogram"], {"1": 2000})


if __name__ == "__main__":
    unittest.main()
