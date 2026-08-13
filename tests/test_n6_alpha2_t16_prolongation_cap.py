from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha2_t16_prolongation_cap.py"
FROZEN = ROOT / "data" / "n6_alpha2_t16_prolongation_cap.json"


class N6Alpha2T16ProlongationCapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_complete_one_rectangle_coverage(self) -> None:
        self.assertEqual(self.payload["one_rectangle_support_orbit_count"], 12)
        self.assertEqual(
            self.payload["checked_one_rectangle_qF_representatives"], 173_388
        )
        self.assertEqual(
            self.payload["evaluated_interacting_pairs_after_pruning"],
            3_849_632,
        )

    def test_pair_correction_certificate(self) -> None:
        certificate = self.payload["pair_correction_bound_certificate"]
        self.assertEqual(
            certificate["maximum_pair_correction_per_shared_block"], 1
        )
        self.assertEqual(
            certificate["checked_block_mask_axis_pairs"], 8_618_400
        )

    def test_caps_and_packet_gap(self) -> None:
        self.assertEqual(
            [
                row["prolongation_upper_cap"]
                for row in self.payload["one_rectangle_support_rows"]
            ],
            [464, 455, 456, 453, 453, 453, 464, 455, 453, 445, 445, 445],
        )
        self.assertEqual(
            self.payload["universal_alpha2_t16_prolongation_upper_cap"], 464
        )
        self.assertEqual(self.payload["direct_packet_gap_when_alpha_at_most_two"], 4)

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to rebuild the 8,618,400-pair certificate",
    )
    def test_full_parallel_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--workers",
                "10",
                "--verify-json",
                str(FROZEN),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=360,
        )
        self.assertIn("alpha2_t16_cap=464", completed.stdout)
        self.assertIn("N6_ALPHA2_T16_PROLONGATION_CAP_PASS", completed.stdout)

    def test_claim_boundary(self) -> None:
        self.assertIn("alpha three", self.payload["strict_conclusion"])
        self.assertIn("one-defective", self.payload["claim_boundary"])
        self.assertIn("lower29", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
