from __future__ import annotations

import json
import subprocess
import sys
import unittest
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data" / "general_one_relation_koszul_homology_counterexample.json"
sys.path.insert(0, str(SCRIPTS))

import general_one_relation_koszul_homology_counterexample as theorem


class OneRelationKoszulHomologyCounterexampleTests(unittest.TestCase):
    def test_hilbert_function(self) -> None:
        for n in range(5, 13):
            values = theorem.full_circuit_hilbert(n)
            self.assertEqual(values[0], 1)
            self.assertEqual(values[-1], 1)
            self.assertEqual(values[1], n - 1)
            self.assertEqual(values[-2], n - 1)
            for degree in range(2, n - 1):
                self.assertEqual(values[degree], comb(n, degree))

    def test_exact_homology_and_gap(self) -> None:
        for n in range(5, 13):
            item = theorem.row(n)
            self.assertEqual(item["actual_h1_dimension"], comb(n, 2))
            self.assertEqual(item["independent_term_cap"], n - 1)
            self.assertEqual(item["violation_gap"], comb(n - 1, 2))

    def test_differential_rank_identity(self) -> None:
        for n in range(5, 13):
            item = theorem.row(n)
            self.assertEqual(item["source_dimension_and_rank"], comb(n, 3))
            self.assertEqual(item["right_differential_rank"], 2 * comb(n, 3))
            self.assertEqual(
                item["source_dimension_and_rank"]
                + item["right_differential_rank"]
                + item["actual_h1_dimension"],
                item["middle_dimension"],
            )

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text()), theorem.payload())

    def test_primary_optimized_mode(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-O",
                str(SCRIPTS / "general_one_relation_koszul_homology_counterexample.py"),
                "--verify-json",
                str(DATA),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("COUNTEREXAMPLE_PASS", completed.stdout)

    def test_independent_sparse_replay(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "general_one_relation_koszul_homology_counterexample_independent.py"),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn("INDEPENDENT_PASS", completed.stdout)


if __name__ == "__main__":
    unittest.main()
