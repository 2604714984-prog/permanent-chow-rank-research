from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class Lower50SlopeReplayTests(unittest.TestCase):
    def test_rank_six_profiles_match_frozen_payload(self) -> None:
        module = load_script("n7_rank6_normal_form_profiles.py")
        payload = module.build_certificate()
        frozen = json.loads(
            (ROOT / "data" / "n7_rank6_normal_form_profiles.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload, frozen)
        self.assertEqual(
            [row["hilbert_profile"][3] for row in payload["normal_forms"]],
            [25, 25, 31, 34, 35, 35],
        )

    def test_slope_tables_match_frozen_payload(self) -> None:
        module = load_script("n7_slope10_coordinate_symbol_table.py")
        payload = module.build_certificate()
        frozen = json.loads(
            (ROOT / "data" / "n7_slope10_coordinate_symbol_table.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(payload, frozen)
        self.assertEqual(
            payload["rank_six"]["minimum_combined_rank_by_quotient_rank"],
            [0, 22, 33, 37, 41, 44, 48],
        )
        self.assertEqual(
            payload["rank_seven"]["minimum_combined_rank_by_quotient_rank"],
            [0, 32, 49, 56, 57, 64, 67, 69],
        )

    def test_independent_replays(self) -> None:
        cases = (
            (
                "n7_rank6_normal_form_profiles_independent.py",
                "PASS independent rank-six normal-form replay",
            ),
            (
                "n7_slope10_coordinate_symbol_table_independent.py",
                "PASS independent slope-ten coordinate-table audit",
            ),
        )
        for script, marker in cases:
            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / script)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn(marker, completed.stdout)


if __name__ == "__main__":
    unittest.main()
