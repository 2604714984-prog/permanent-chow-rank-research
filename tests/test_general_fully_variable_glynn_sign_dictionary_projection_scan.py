from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "scripts"
    / "general_fully_variable_glynn_sign_dictionary_projection_scan.cpp"
)


class FullyVariableGlynnProjectionCorrectionTests(unittest.TestCase):
    def test_complete_characteristic_zero_projection_correction(self) -> None:
        compiler = shutil.which("g++")
        if compiler is None:
            self.skipTest("g++ is required for the exhaustive projection replay")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "projection_scan"
            output = root / "projection_scan.json"
            subprocess.run(
                [
                    compiler,
                    "-O3",
                    "-std=c++20",
                    str(SOURCE),
                    "-o",
                    str(executable),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            completed = subprocess.run(
                [str(executable), str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=600,
            )
            self.assertIn(
                "GENERAL_FULLY_VARIABLE_GLYNN_SIGN_"
                "PROJECTION_CORRECTION_PASS",
                completed.stdout,
            )
            payload = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(payload["prime"], 2_305_843_009_213_693_951)
        self.assertEqual(payload["unique_directions"], 40)
        self.assertEqual(payload["supports_checked"], 102_090)
        self.assertEqual(payload["minimum"], 4)
        self.assertEqual(payload["minimal_supports"], 16)
        self.assertEqual(len(payload["solutions"]), 16)
        self.assertEqual(
            payload["solutions"][0],
            ["L0", "L1", "C0_1", "C1_0"],
        )


if __name__ == "__main__":
    unittest.main()
