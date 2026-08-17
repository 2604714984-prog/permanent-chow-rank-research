from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_principal_ideal_barrier.py"
INDEPENDENT = SCRIPTS / "general_two_direction_principal_ideal_barrier_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_principal_ideal_barrier", PRIMARY)


class GeneralTwoDirectionPrincipalIdealBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_theorem_boundary(self) -> None:
        theorem = self.payload["theorem"]
        self.assertEqual(
            theorem["boolean_envelope"],
            "beta_pr(n,p,d)=min(binom(n,d-p),binom(n,d)).",
        )
        self.assertIn("central", theorem["route_ceiling"].lower())
        self.assertIn("two", theorem["first_open_interface"].lower())

    def test_finite_replay_count(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["principal_profile_cells"], 119)
        self.assertEqual(replay["n_min"], 2)
        self.assertEqual(replay["n_max"], 8)

    def test_closed_formula_samples(self) -> None:
        rows = self.payload["finite_replay"]["boolean_envelopes"]
        self.assertEqual(rows["4"]["p1_d2"], 4)
        self.assertEqual(rows["5"]["p1_d3"], 10)
        self.assertEqual(rows["6"]["p2_d4"], 15)
        self.assertEqual(rows["8"]["p4_d6"], min(comb(8, 2), comb(8, 6)))

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_PRINCIPAL_IDEAL_BARRIER_AUDIT_PASS",
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
            "GENERAL_TWO_DIRECTION_PRINCIPAL_IDEAL_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_principal_profile_cells=83", completed.stdout)


if __name__ == "__main__":
    unittest.main()
