from __future__ import annotations

import json
import subprocess
import sys
import unittest
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data" / "general_full_quotient_koszul_cubic_duality.json"
sys.path.insert(0, str(SCRIPTS))

import general_full_quotient_koszul_cubic_duality as theorem


class FullQuotientKoszulCubicDualityTests(unittest.TestCase):
    def test_tor_positions(self) -> None:
        for n in range(5, 13):
            positions = theorem.tor_positions(n, n - 1)
            self.assertEqual(positions["gorenstein_last_shift"], 2 * n - 1)
            self.assertEqual(positions["high_tor_homological_degree"], n - 2)
            self.assertEqual(positions["high_tor_internal_degree"], 2 * n - 4)
            self.assertEqual(positions["dual_low_tor_internal_degree"], 3)

    def test_one_relation_classification(self) -> None:
        self.assertEqual(theorem.one_relation_cubic_generators(1), 1)
        self.assertEqual(theorem.one_relation_cubic_generators(2), 1)
        self.assertEqual(theorem.one_relation_cubic_generators(3), 7)
        for support_size in range(4, 13):
            self.assertEqual(
                theorem.one_relation_cubic_generators(support_size),
                comb(support_size + 1, 2),
            )

    def test_full_support_rows(self) -> None:
        for n in range(5, 13):
            row = theorem.one_relation_row(n)
            self.assertEqual(row["full_support_h1"], comb(n, 2))
            self.assertEqual(row["full_support_independent_cap"], n - 1)
            self.assertEqual(row["full_support_gap"], comb(n - 1, 2))

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text()), theorem.payload())

    def test_primary_optimized_mode(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-O",
                str(SCRIPTS / "general_full_quotient_koszul_cubic_duality.py"),
                "--verify-json",
                str(DATA),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("KOSZUL_CUBIC_DUALITY_PASS", completed.stdout)

    def test_independent_apolar_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "general_full_quotient_koszul_cubic_duality_independent.py"),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn("DUALITY_INDEPENDENT_PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
