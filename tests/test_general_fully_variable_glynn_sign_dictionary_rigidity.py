from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = (
    ROOT
    / "scripts"
    / "general_fully_variable_glynn_sign_dictionary_rigidity.py"
)
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_fully_variable_glynn_sign_dictionary_rigidity_independent.py"
)
DATA = (
    ROOT
    / "data"
    / "general_fully_variable_glynn_sign_dictionary_rigidity.json"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class FullyVariableGlynnSignDictionaryRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module("fully_variable_sign_primary", PRIMARY)
        cls.payload = cls.module.payload()

    def test_dictionary_and_projection_counts(self) -> None:
        self.assertEqual(self.payload["dictionary"]["raw_atoms"], 336)
        projection = self.payload["diagonal_evaluation"]
        self.assertEqual(projection["unique_projected_directions"], 40)
        self.assertEqual(
            projection["supports_checked_through_six"],
            4_598_478,
        )
        self.assertEqual(projection["minimum_projected_term_count"], 6)
        self.assertEqual(projection["minimal_projected_supports"], 16)

    def test_all_projected_candidates_have_fixed_coefficients(self) -> None:
        candidates = self.module.projected_candidates()
        self.assertEqual(len(candidates), 16)
        self.assertTrue(
            all(
                value["positive_coefficient"] == "1/6"
                for value in candidates
            )
        )
        self.assertTrue(
            all(
                value["negative_coefficient"] == "-1/6"
                for value in candidates
            )
        )

    def test_complete_full_tensor_scan(self) -> None:
        scan = self.payload["full_tensor_scan"]
        self.assertEqual(scan["assignments_checked"], 746_496)
        self.assertEqual(scan["exact_solutions"], 0)
        self.assertEqual(len(scan["candidate_checks"]), 16)

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload,
            json.loads(DATA.read_text(encoding="utf-8")),
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn(
            "GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_"
            "RIGIDITY_INDEPENDENT_PASS",
            completed.stdout,
        )

    def test_claim_boundary(self) -> None:
        conclusion = self.payload["conclusion"]
        boundary = self.payload["claim_boundary"]
        self.assertEqual(
            conclusion["fully_variable_quartic_sign_dictionary_threshold"],
            7,
        )
        self.assertEqual(boundary["global_six_block_literal_sum"], "OPEN")
        self.assertEqual(boundary["mu_6_4"], "OPEN_IN_[6,7]")
        self.assertFalse(boundary["unrestricted_chow_rank_improvement"])


if __name__ == "__main__":
    unittest.main()
