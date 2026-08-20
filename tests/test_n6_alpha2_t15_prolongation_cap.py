from __future__ import annotations

import json
import importlib.util
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha2_t15_prolongation_cap.py"
FROZEN = ROOT / "data" / "n6_alpha2_t15_prolongation_cap.json"


def load_audit():
    spec = importlib.util.spec_from_file_location("n6_alpha2_t15_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_audit()


class N6Alpha2T15ProlongationCapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_complete_orbit_coverage(self) -> None:
        self.assertEqual(self.payload["one_rectangle_support_orbit_count"], 12)
        self.assertEqual(
            self.payload["raw_local_qF_count_per_support_orbit"], 38_760
        )
        self.assertEqual(
            self.payload["raw_support_orbit_qF_configuration_count"], 465_120
        )
        self.assertEqual(
            self.payload["qF_orbit_representative_count_across_shapes"],
            173_388,
        )
        self.assertEqual(
            self.payload["reduced_qF_extra_axis_evaluations"], 74_036_676
        )

    def test_caps(self) -> None:
        self.assertEqual(
            [
                row["prolongation_upper_cap"]
                for row in self.payload["one_rectangle_support_rows"]
            ],
            [458, 447, 450, 445, 445, 445, 458, 447, 445, 438, 438, 438],
        )
        self.assertEqual(
            self.payload["universal_alpha2_t15_prolongation_upper_cap"], 458
        )

    def test_shape_local_indices_restore_historical_global_indices(self) -> None:
        raw = [
            {
                "support_index": 2,
                "checked_representatives": 4,
                "sample": {"local_representative_index": 0},
            },
            {
                "support_index": 0,
                "checked_representatives": 2,
                "sample": {"local_representative_index": 1},
            },
            {
                "support_index": 1,
                "checked_representatives": 3,
                "sample": {"local_representative_index": 2},
            },
        ]
        rows = AUDIT.globalize_support_rows(raw)
        self.assertEqual([row["support_index"] for row in rows], [0, 1, 2])
        self.assertEqual(
            [row["sample"]["global_representative_index"] for row in rows],
            [1, 4, 5],
        )
        self.assertTrue(
            all("local_representative_index" not in row["sample"] for row in rows)
        )

    def test_frozen_samples_stay_inside_shape_prefixes(self) -> None:
        offset = 0
        for row in self.payload["one_rectangle_support_rows"]:
            count = row["qF_orbit_representative_count"]
            sample = row["sample_maximizer"]["global_representative_index"]
            self.assertLessEqual(offset, sample)
            self.assertLess(sample, offset + count)
            offset += count
        self.assertEqual(offset, 173_388)

    def test_state_partition(self) -> None:
        pruning = self.payload["state_pruning"]
        self.assertEqual(
            (
                pruning["input_state_count"],
                pruning["excluded_by_alpha2_t15_cap_count"],
                pruning["remaining_state_count"],
                pruning["remaining_state_ids"],
            ),
            (7, 6, 1, ["b60_state_366"]),
        )
        self.assertEqual(pruning["remaining_profile"], [[0, 3]] * 6)

    @unittest.skipUnless(
        os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1",
        "set RUN_EXPENSIVE_REPLAYS=1 to rebuild the 74,036,676-evaluation certificate",
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
            timeout=7_200,
        )
        self.assertIn("alpha2_t15_cap=458", completed.stdout)
        self.assertIn("N6_ALPHA2_T15_PROLONGATION_CAP_PASS", completed.stdout)

    def test_claim_boundary(self) -> None:
        self.assertIn("all-alpha-three", self.payload["claim_boundary"])
        self.assertIn("does not exclude", self.payload["claim_boundary"])
        self.assertIn("border-rank", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
