from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_global_t15_prolongation_cap.py"
FROZEN = ROOT / "data" / "n6_global_t15_prolongation_cap.json"


class N6GlobalT15ProlongationCapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_coverage_counts(self) -> None:
        self.assertEqual(self.payload["fixed_W_count"], 18_564)
        self.assertEqual(self.payload["fixed_W_orbit_representative_count"], 1_683)
        self.assertEqual(self.payload["extra_axis_triples_per_W"], 13_067_054)
        self.assertEqual(self.payload["interacting_axis_pair_count"], 19_980)
        self.assertEqual(self.payload["common_block_axis_triple_count"], 57_240)

    def test_cap_and_state_partition(self) -> None:
        self.assertEqual(
            self.payload["characteristic_zero_prolongation_upper_cap_t15"],
            458,
        )
        pruning = self.payload["state_pruning"]
        self.assertEqual(
            (
                pruning["input_t15_frontier_count"],
                pruning["excluded_by_extremal_t15_cap_count"],
                pruning["excluded_by_alpha1_t15_closure_count"],
                pruning["remaining_count"],
            ),
            (84, 56, 21, 7),
        )

    def test_remaining_profiles(self) -> None:
        profiles = self.payload["state_pruning"]["remaining_epsilon_alpha_pairs"]
        self.assertEqual(len(profiles), 7)
        self.assertTrue(
            all(
                all(epsilon == 0 and alpha in (2, 3) for epsilon, alpha in row)
                for row in profiles
            )
        )

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to rebuild the global t15 certificate",
    )
    def test_full_serial_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--workers",
                "1",
                "--verify-json",
                str(FROZEN),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=1_800,
        )
        self.assertIn("t15_cap=458", completed.stdout)
        self.assertIn("N6_GLOBAL_T15_PROLONGATION_CAP_PASS", completed.stdout)

    def test_claim_boundary(self) -> None:
        self.assertIn("one-rectangle alpha-two", self.payload["claim_boundary"])
        self.assertIn("does not yet exclude", self.payload["claim_boundary"])
        self.assertIn("border-rank", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
