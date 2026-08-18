from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_recursive_zero_seeded_tower.py"
INDEPENDENT = ROOT / "scripts" / "general_recursive_zero_seeded_tower_independent.py"
FROZEN = ROOT / "data" / "general_recursive_zero_seeded_tower.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_recursive_zero_seeded_tower_test",
        PRIMARY,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(PRIMARY)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GeneralRecursiveZeroSeededTowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)
        self.assertEqual(
            self.payload["core_sha256"],
            "db770e0622813e208dbedaef03c83dd70e43c1cfff42e3d71729183515da1312",
        )

    def test_thresholds_unchanged(self) -> None:
        expected = self.module.expected_thresholds()
        for n_text, row in self.payload["exact_result"]["rows"].items():
            self.assertEqual(row["thresholds"], expected[n_text])

    def test_zero_counts(self) -> None:
        expected = self.module.expected_zero_counts()
        for n_text, row in self.payload["exact_result"]["rows"].items():
            self.assertEqual(row["zero_counts"], expected[n_text])

    def test_capacity_changes_are_small(self) -> None:
        self.assertEqual(
            self.payload["exact_result"]["maximum_changed_capacity_cells"],
            4,
        )
        self.assertEqual(
            self.payload["exact_result"]["maximum_capacity_reduction"],
            2,
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--maximum-n", "7"],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_RECURSIVE_ZERO_SEEDED_TOWER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_thresholds_unchanged=true", completed.stdout)


if __name__ == "__main__":
    unittest.main()
