from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_derivative_tower_capacity.py"
INDEPENDENT = SCRIPTS / "general_derivative_tower_capacity_independent.py"
FROZEN = ROOT / "data" / "general_derivative_tower_capacity.json"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_derivative_tower_capacity", SCRIPT)


class GeneralDerivativeTowerCapacityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_n7_capacity_rows(self) -> None:
        self.assertEqual(
            self.payload["n7_capacity_rows"],
            {
                "1": [0, 7, 14, 21, 28, 35],
                "2": [0, 3, 22, 43, 64, 85],
                "3": [0, 0, 4, 17, 40, 64],
            },
        )

    def test_n8_capacity_rows(self) -> None:
        self.assertEqual(
            self.payload["n8_capacity_rows"],
            {
                "1": [0, 8, 16, 24, 32, 40],
                "2": [0, 6, 34, 62, 90, 118],
                "3": [0, 0, 10, 40, 80, 112],
            },
        )

    def test_perm7_lower_46(self) -> None:
        row = self.payload["n7_application"]
        self.assertEqual(row["five_term_cubic_cap"], 64)
        self.assertEqual(row["projected_first_shadow_capacity"], 589)
        self.assertEqual(row["outer_intersection_cap"], 341)
        self.assertEqual(row["residual_terms"], 26)
        self.assertEqual(row["ordinary_lower_bound"], 46)

    def test_perm8_regression(self) -> None:
        row = self.payload["n8_regression"]
        self.assertEqual(row["five_term_cubic_cap"], 112)
        self.assertEqual(row["ordinary_lower_bound"], 80)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "3b697597860980a3130f01d7c9de77917951dddb58a2170727cfd6dd451a3a3c",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_DERIVATIVE_TOWER_CAPACITY_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=46", completed.stdout)


if __name__ == "__main__":
    unittest.main()
