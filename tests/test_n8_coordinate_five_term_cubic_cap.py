from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n8_coordinate_five_term_cubic_cap.py"
DATA = ROOT / "data" / "n8_coordinate_five_term_cubic_cap.json"


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class N8CoordinateFiveTermCubicCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_core_hash(self) -> None:
        core = dict(self.payload)
        expected = core.pop("core_sha256")
        self.assertEqual(
            expected,
            "194ad847df5d43e122a6a702c6594648ad9f1194dd6f93ec75d47f86d7da5e89",
        )
        self.assertEqual(canonical_sha256(core), expected)

    def test_exact_extension_counts_and_maxima(self) -> None:
        cases = self.payload["canonical_extension_cases"]
        shared = cases["shared_edge_pair"]
        disjoint = cases["disjoint_pair"]
        self.assertEqual(shared["extension_count"], 32_509)
        self.assertEqual(disjoint["extension_count"], 1_653)
        self.assertEqual(shared["maximum_matching_pair_count"], 8)
        self.assertEqual(shared["maximum_multi_rectangle_count"], 8)
        self.assertEqual(disjoint["maximum_matching_pair_count"], 6)
        self.assertEqual(disjoint["maximum_multi_rectangle_count"], 4)

    def test_five_term_coordinate_cap(self) -> None:
        consequence = self.payload["five_term_coordinate_consequence"]
        self.assertEqual(consequence["coordinate_chow_terms"], 5)
        self.assertEqual(consequence["matching_count_per_permanent"], 6)
        self.assertTrue(consequence["pigeonhole_required_pair_in_one_term"])
        self.assertEqual(consequence["coordinate_permanent_subspace_cap"], 40)

    def test_flat_sum_gap(self) -> None:
        comparison = self.payload["general_target_comparison"]
        self.assertEqual(comparison["general_recursive_block_cap"], 160)
        self.assertEqual(comparison["required_chow_cap_for_lower_80"], 146)
        self.assertEqual(comparison["coordinate_fixed_term_cap"], 40)
        self.assertEqual(
            comparison[
                "minimum_nonliteral_flat_sum_directions_if_dimension_147_persists"
            ],
            107,
        )

    def test_full_replay_matches_frozen_payload(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "replay.json"
            completed = subprocess.run(
                [sys.executable, "-O", str(SCRIPT), "--json", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn(
                "N8_COORDINATE_FIVE_TERM_CUBIC_CAP_PASS",
                completed.stdout,
            )
            replay = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(replay, self.payload)


if __name__ == "__main__":
    unittest.main()
