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


class FullyVariableGlynnSignDictionaryCorrectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module("fully_variable_sign_correction", PRIMARY)
        cls.payload = cls.module.payload()

    def test_dictionary_and_corrected_projection_counts(self) -> None:
        self.assertEqual(self.payload["dictionary"]["raw_atoms"], 336)
        projection = self.payload["diagonal_evaluation"]
        self.assertEqual(projection["unique_projected_directions"], 40)
        self.assertEqual(
            projection["supports_checked_through_first_survivor"],
            102_090,
        )
        self.assertEqual(projection["minimum_projected_direction_count"], 4)
        self.assertEqual(projection["minimal_projected_supports"], 16)

    def test_four_direction_candidate_coefficients(self) -> None:
        candidates = self.module.projected_candidates()
        self.assertEqual(len(candidates), 16)
        self.assertTrue(
            all(
                value["coefficients"]
                == ["3/2", "-3/2", "-3/2", "3/2"]
                for value in candidates
            )
        )

    def test_complete_four_direction_lift_scan(self) -> None:
        scan = self.payload["four_direction_full_tensor_scan"]
        self.assertEqual(scan["assignments_checked"], 186_624)
        self.assertEqual(scan["exact_solutions"], 0)
        self.assertEqual(scan["candidate_supports"], 16)

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
            "PROJECTION_CORRECTION_INDEPENDENT_PASS",
            completed.stdout,
        )

    def test_claim_boundary_and_retraction(self) -> None:
        conclusion = self.payload["conclusion"]
        boundary = self.payload["claim_boundary"]
        self.assertEqual(
            conclusion["fully_variable_sign_dictionary_threshold"],
            "OPEN_IN_[6,7]",
        )
        self.assertEqual(
            conclusion["six_atom_sign_dictionary_representation"],
            "OPEN",
        )
        self.assertEqual(boundary["global_six_block_literal_sum"], "OPEN")
        self.assertEqual(boundary["mu_6_4"], "OPEN_IN_[6,7]")
        self.assertFalse(boundary["unrestricted_chow_rank_improvement"])
        self.assertEqual(
            self.payload["superseded_claim"]["reason"],
            "the diagonal projection minimum is four, not six",
        )


if __name__ == "__main__":
    unittest.main()
