from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_scalar_tower_polynomial_ceiling.py"
INDEPENDENT = SCRIPTS / "general_scalar_tower_polynomial_ceiling_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_scalar_tower_polynomial_ceiling", PRIMARY)


class GeneralScalarTowerPolynomialCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_theorem_boundary(self) -> None:
        theorem = self.payload["theorem"]
        self.assertEqual(
            theorem["optimized_ceiling"],
            "With w=ceil(n^(3/4)), Theta_n=O(n^(1/4)*binom(n,floor(n/2))).",
        )
        self.assertEqual(theorem["power_form"], "Theta_n=O(2^n/n^(1/4)).")
        self.assertIn("Omega(n^(1/4))", theorem["route_gap"])

    def test_exact_finite_interfaces(self) -> None:
        finite = self.payload["finite_diagnostics"]
        self.assertGreater(finite["hypergeometric_parameter_pairs"], 1000)
        self.assertGreater(finite["adjacent_cdf_checks"], 30000)
        self.assertGreater(
            finite["geometric_start_and_central_binomial_checks"],
            9000,
        )

    def test_pr51_normalization_regression(self) -> None:
        rows = self.payload["finite_diagnostics"]["normalization_rows"]
        self.assertEqual(rows["7"]["theta"], 49)
        self.assertEqual(rows["7"]["central_binomial"], 35)
        self.assertEqual(rows["8"]["theta"], 90)
        self.assertEqual(rows["10"]["theta"], 307)
        self.assertEqual(rows["10"]["central_binomial"], 252)

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_AUDIT_PASS",
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
            "GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_ceiling=O(n^(1/4)*central_binomial)",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
