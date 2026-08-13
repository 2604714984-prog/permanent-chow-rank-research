from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_global_t16_prolongation_cap.py"
FROZEN = ROOT / "data" / "n6_global_t16_prolongation_cap.json"


class N6GlobalT16ProlongationCapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_complete_fixed_coverage(self) -> None:
        self.assertEqual(self.payload["fixed_W_count"], 18_564)
        self.assertEqual(
            self.payload["fixed_W_orbit_representative_count"], 1_683
        )
        self.assertEqual(self.payload["extra_axis_count"], 4)
        self.assertEqual(
            self.payload["extra_axis_quadruples_per_W"], 1_391_641_251
        )

    def test_cap_and_sample(self) -> None:
        self.assertEqual(
            self.payload["characteristic_zero_prolongation_upper_cap_t16"],
            462,
        )
        sample = self.payload["sample_maximizer"]
        self.assertEqual(sample["base_prolongation_dimension"], 432)
        self.assertEqual(sample["four_axis_increment"], 30)
        self.assertEqual(len(sample["extra_axes"]), 4)

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
            timeout=300,
        )
        self.assertIn("t16_cap=462", completed.stdout)
        self.assertIn("N6_GLOBAL_T16_PROLONGATION_CAP_PASS", completed.stdout)

    def test_claim_boundary(self) -> None:
        self.assertIn("alpha-one", self.payload["strict_conclusion"])
        self.assertIn("one-rectangle alpha-two", self.payload["claim_boundary"])
        self.assertIn("lower29", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
