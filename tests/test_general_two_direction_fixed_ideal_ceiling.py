from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_fixed_ideal_ceiling.py"
INDEPENDENT = SCRIPTS / "general_two_direction_fixed_ideal_ceiling_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_fixed_ideal_ceiling", PRIMARY)


class GeneralTwoDirectionFixedIdealCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_theorem_boundary(self) -> None:
        theorem = self.payload["theorem"]
        self.assertIn("m-primary", theorem["fixed_ideal_ceiling"])
        self.assertIn("n^(-1/2)", theorem["fixed_ideal_ceiling"])
        self.assertIn("sqrt(n)", theorem["glynn_gap"])

    def test_finite_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["one_factor_total_bound_checks"], 371)
        self.assertEqual(replay["split_tensor_bound_checks"], 334)

    def test_sample_bounds(self) -> None:
        samples = self.payload["finite_replay"]["samples"]
        self.assertEqual(set(samples), {"n8_N2", "n10_N3", "n20_N4", "n50_N8"})
        for row in samples.values():
            self.assertLessEqual(row["total_split_quotient"], row["certified_bound"])
            self.assertLessEqual(row["maximum_graded_piece"], row["total_split_quotient"])

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_FIXED_IDEAL_CEILING_AUDIT_PASS",
            completed.stdout,
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_FIXED_IDEAL_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_boolean_power_quotient_cells=158", completed.stdout)


if __name__ == "__main__":
    unittest.main()
