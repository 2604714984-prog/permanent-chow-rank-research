from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b24_three_relation_frontier.py"
FROZEN = ROOT / "data" / "n6_b24_three_relation_frontier.json"

SPEC = importlib.util.spec_from_file_location(
    "n6_b24_three_relation_frontier",
    SCRIPT,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load b24 frontier audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6B24ThreeRelationFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_pattern_counts(self) -> None:
        self.assertEqual(self.payload["all_labelled_pattern_count"], 1153)
        self.assertEqual(
            self.payload["all_relation_kernel_cap_histogram"],
            {"0": 940, "1": 189, "2": 23, "3": 1},
        )
        self.assertEqual(
            self.payload["all_total_epsilon_histogram"],
            {"0": 256, "1": 432, "2": 344, "3": 120, "4": 1},
        )

    def test_profile_filter_and_unique_cap_three_pattern(self) -> None:
        self.assertEqual(
            self.payload["quadratic_dimension_twelve_pattern_count"],
            16,
        )
        self.assertEqual(
            self.payload["profile_realizable_pattern_count"],
            1137,
        )
        self.assertEqual(
            self.payload[
                "profile_realizable_relation_kernel_cap_histogram"
            ],
            {"0": 924, "1": 189, "2": 23, "3": 1},
        )
        self.assertEqual(
            self.payload["cap_two_epsilon_type_histogram"],
            {"0,0,0,0": 15, "0,0,0,1": 8},
        )
        self.assertEqual(
            self.payload["unique_three_relation_pattern"],
            {
                "epsilon": [0, 0, 0, 0],
                "alpha": [0, 0, 0, 0],
                "individual_quadratic_dimensions": [15, 15, 15, 15],
                "individual_intersection_dimensions": [3, 3, 3, 3],
                "individual_quotient_dimensions": [12, 12, 12, 12],
                "quadratic_relation_kernel_cap": 3,
            },
        )

    def test_frozen_certificate_matches_live_replay(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_claim_boundary_remains_fail_closed(self) -> None:
        self.assertIn("diagnostic", self.payload["claim_boundary"])
        self.assertIn("do not settle", self.payload["claim_boundary"])
        self.assertNotIn("ChowRank(perm_6)>=24", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
