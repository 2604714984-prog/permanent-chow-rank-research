from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_bounded_matrix_ceiling.py"
INDEPENDENT = SCRIPTS / "general_two_direction_bounded_matrix_ceiling_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_bounded_matrix_ceiling", PRIMARY)


class GeneralTwoDirectionBoundedMatrixCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_theorem_boundary(self) -> None:
        theorem = self.payload["theorem"]
        self.assertIn("normal rank", theorem["boolean_denominator"])
        self.assertIn("K_n", theorem["bounded_size"])
        self.assertIn("sqrt(n)", theorem["complexity_barrier"])

    def test_finite_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["lefschetz_power_rank_checks"], 119)
        self.assertEqual(replay["arithmetic_route_ceiling_checks"], 3_870)

    def test_sample_arithmetic(self) -> None:
        samples = self.payload["finite_replay"]["samples"]
        self.assertEqual(len(samples), 4)
        for row in samples.values():
            self.assertLessEqual(
                row["exact_route_ceiling"],
                row["coarse_central_ceiling"],
            )
            self.assertGreater(row["normal_rank_denominator"], 0)

    def test_matrix_size_diagnostic(self) -> None:
        rows = self.payload["finite_replay"]["matrix_size_diagnostics"]
        self.assertEqual(rows["3"]["minimum_integer_K_not_excluded"], 2)
        self.assertGreaterEqual(rows["30"]["minimum_integer_K_not_excluded"], 3)
        for row in rows.values():
            self.assertGreaterEqual(row["minimum_integer_K_not_excluded"], 1)

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_BOUNDED_MATRIX_CEILING_AUDIT_PASS",
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
            "GENERAL_TWO_DIRECTION_BOUNDED_MATRIX_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_lefschetz_power_cells=83", completed.stdout)
        self.assertIn("independent_arithmetic_ceiling_cells=1134", completed.stdout)


if __name__ == "__main__":
    unittest.main()
