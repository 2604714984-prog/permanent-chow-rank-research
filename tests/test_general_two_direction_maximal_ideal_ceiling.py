from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_maximal_ideal_ceiling.py"
INDEPENDENT = SCRIPTS / "general_two_direction_maximal_ideal_ceiling_independent.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_maximal_ideal_ceiling", PRIMARY)


class GeneralTwoDirectionMaximalIdealCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_finite_route_ceilings(self) -> None:
        rows = self.payload["finite_replay"]["rows"]
        self.assertEqual(
            {key: value["route_ceiling"] for key, value in rows.items()},
            {
                "3": 3,
                "4": 7,
                "5": 10,
                "6": 20,
                "7": 35,
                "8": 75,
                "9": 126,
                "10": 252,
            },
        )

    def test_all_ceilings_below_existing_boundaries(self) -> None:
        for row in self.payload["finite_replay"]["rows"].values():
            self.assertLess(row["route_ceiling"], row["existing_boundary"])

    def test_profile_count(self) -> None:
        self.assertEqual(self.payload["finite_replay"]["profile_cells"], 52)

    def test_key_split_quotients(self) -> None:
        rows = self.payload["finite_replay"]["rows"]
        self.assertEqual(rows["4"]["by_degree"]["2"]["split_quotient"], 1)
        self.assertEqual(rows["8"]["by_degree"]["4"]["split_quotient"], 4)
        self.assertEqual(rows["10"]["by_degree"]["5"]["split_quotient"], 0)

    def test_primary_cli(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_MAXIMAL_IDEAL_CEILING_AUDIT_PASS",
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
            "GENERAL_TWO_DIRECTION_MAXIMAL_IDEAL_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_split_boolean_cells=35", completed.stdout)


if __name__ == "__main__":
    unittest.main()
