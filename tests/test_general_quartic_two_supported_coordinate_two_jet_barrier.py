from __future__ import annotations

import json
import lzma
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_quartic_two_supported_coordinate_two_jet_barrier.py"
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_quartic_two_supported_coordinate_two_jet_barrier_independent.py"
)
CERTIFICATE = (
    ROOT
    / "data"
    / "general_quartic_two_supported_coordinate_two_jet_symbolic_kernel_v2"
)
DATA = ROOT / "data" / "general_quartic_two_supported_coordinate_two_jet_barrier.json.xz"
EXPECTED_HASH = "0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9"
PRIMARY_MARKER = "GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_PASS"
INDEPENDENT_MARKER = (
    "GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_INDEPENDENT_PASS"
)


class QuarticTwoSupportedCoordinateTwoJetBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(lzma.decompress(DATA.read_bytes()).decode("utf-8"))
        cls.core = cls.payload["theorem_core"]

    def test_support_classification(self) -> None:
        classification = self.core["support_classification"]
        self.assertEqual(classification["five_vertex_abstract_multigraph_types"], 7)
        self.assertEqual(
            classification["embeddable_five_vertex_types"],
            ["loose_handcuff", "theta", "tight_handcuff"],
        )
        self.assertEqual(
            classification["embedding_orbit_counts"],
            {"loose_handcuff": 18, "theta": 1, "tight_handcuff": 5},
        )
        self.assertEqual(
            classification["embedding_counts_fixed_identity"],
            {"loose_handcuff": 696, "theta": 48, "tight_handcuff": 216},
        )
        self.assertEqual(self.core["simple_cycle"]["row_column_cycle_orbits"], 13)

    def test_matching_character_rank_strata(self) -> None:
        self.assertEqual(
            self.core["matching_character_ranks"],
            {
                "loose_handcuff": {"4": 1, "5": 17},
                "six_cycle": {"5": 4, "6": 9},
                "theta": {"5": 1},
                "tight_handcuff": {"4": 1, "5": 4},
            },
        )
        names = {chart["name"] for chart in self.core["symbolic_gain_charts"]}
        self.assertEqual(
            names,
            {
                "tight_handcuff_full_character_rank",
                "tight_handcuff_deficient_character_rank",
                "loose_handcuff_full_character_rank",
                "loose_handcuff_deficient_character_rank",
                "theta_full_character_rank",
                "six_cycle_deficient_character_rank",
            },
        )

    def test_two_jet_support_barrier_and_claim_boundary(self) -> None:
        self.assertEqual(self.core["global_maximum_two_jet_matching_support"], 8)
        self.assertEqual(self.core["perm4_matching_support"], 24)
        self.assertEqual(
            self.core["theorem"]["regular_second_order_perm4_lift"],
            "IMPOSSIBLE",
        )
        self.assertFalse(self.core["claim_boundary"]["six_block_exclusion"])
        self.assertEqual(
            self.core["claim_boundary"]["mu_6_4_exact_value"],
            "OPEN_IN_[6,8]",
        )
        self.assertEqual(self.payload["theorem_core_sha256"], EXPECTED_HASH)

    def test_primary_optimized_mode_reproduces_frozen_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "payload.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    "-O",
                    str(PRIMARY),
                    "--certificate",
                    str(CERTIFICATE),
                    "--json",
                    str(output),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=90,
            )
            self.assertIn(PRIMARY_MARKER, completed.stdout)
            self.assertIn(EXPECTED_HASH, completed.stdout)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")),
                self.payload,
            )

    def test_independent_optimized_mode_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=90,
        )
        self.assertIn(INDEPENDENT_MARKER, completed.stdout)


if __name__ == "__main__":
    unittest.main()
