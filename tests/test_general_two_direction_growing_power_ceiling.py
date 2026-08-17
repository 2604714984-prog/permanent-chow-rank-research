from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_two_direction_growing_power_ceiling.py"
INDEPENDENT = SCRIPTS / "general_two_direction_growing_power_ceiling_independent.py"
FROZEN = ROOT / "data" / "general_two_direction_growing_power_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_growing_power_ceiling", SCRIPT)


class GeneralTwoDirectionGrowingPowerCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_route_cells(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["route_cells"], 91_877)
        self.assertEqual(replay["pointwise_binomial_decay_checks"], 3_318)
        self.assertEqual(replay["finite_block_family_checks"], 79)

    def test_known_cells(self) -> None:
        self.assertEqual(AUDIT.route_ceiling(6, 0, 3), 20)
        self.assertEqual(AUDIT.route_ceiling(6, 2, 3), 18)
        self.assertEqual(AUDIT.route_ceiling(10, 5, 5), 6)

    def test_frozen_theorem_boundary(self) -> None:
        self.assertEqual(self.frozen["status"], self.payload["status"])
        self.assertEqual(self.frozen["theorem"], self.payload["theorem"])
        self.assertEqual(
            self.frozen["claim_boundary"],
            self.payload["claim_boundary"],
        )
        self.assertEqual(
            self.frozen["exact_replay"]["primary_route_cells"],
            self.payload["exact_replay"]["route_cells"],
        )

    def test_every_recorded_maximum_is_below_frozen_envelope(self) -> None:
        for n_text, row in self.payload["exact_replay"]["maxima"].items():
            self.assertLessEqual(
                row["maximum_exact_route_ceiling"],
                row["explicit_polynomial_bound"],
                n_text,
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
            "GENERAL_TWO_DIRECTION_GROWING_POWER_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_route_cells=17292", completed.stdout)


if __name__ == "__main__":
    unittest.main()
