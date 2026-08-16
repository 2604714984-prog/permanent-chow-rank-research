from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_tower_bootstrap_fixed_point.py"
INDEPENDENT = SCRIPTS / "general_tower_bootstrap_fixed_point_independent.py"
FROZEN = ROOT / "data" / "general_tower_bootstrap_fixed_point.json"

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


AUDIT = load_module("general_tower_bootstrap_fixed_point", SCRIPT)


class GeneralTowerBootstrapFixedPointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_bootstrap_sequence(self) -> None:
        self.assertEqual(
            self.payload["n7"]["bootstrap_sequence"],
            [36, 46, 47, 47],
        )

    def test_decisive_capacities(self) -> None:
        capacities = self.payload["n7"]["key_capacities"]
        self.assertEqual(capacities["B_7_4_20"], 341)
        self.assertEqual(capacities["B_7_5_46"], 405)
        self.assertEqual(capacities["B_7_5_47"], 426)

    def test_lower_47_witness(self) -> None:
        row = self.payload["n7"]["second_promotion"]
        self.assertEqual(row["input_bound"], 46)
        self.assertEqual(row["output_bound"], 47)
        self.assertEqual(
            row["canonical_witness"],
            [2, 5, 46, 405, 20_384, 994, 539, 1, 47],
        )

    def test_named_route_fixed_point(self) -> None:
        row = self.payload["n7"]["fixed_point"]
        self.assertEqual(row["input_bound"], 47)
        self.assertEqual(row["output_bound"], 47)
        self.assertEqual(row["maximizer_count"], 12)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "2f11127a199b52e147090557d2a767c950ad97d4dc478e9f05833fa6580f6872",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_TOWER_BOOTSTRAP_FIXED_POINT_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=47", completed.stdout)
        self.assertIn(
            "independent_n7_scalar_tower_fixed_point=47",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
