from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_tower_saturation_closure.py"
INDEPENDENT = SCRIPTS / "general_tower_saturation_closure_independent.py"
FROZEN = ROOT / "data" / "general_tower_saturation_closure.json"

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


AUDIT = load_module("general_tower_saturation_closure", SCRIPT)


class GeneralTowerSaturationClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_degree_five_saturation(self) -> None:
        row = self.payload["n7"]
        self.assertEqual(row["degree_five_ambient_dimension"], 441)
        self.assertEqual(
            row["degree_five_capacities"],
            {"B_7_5_46": 405, "B_7_5_47": 426, "B_7_5_48": 441},
        )
        self.assertEqual(row["degree_five_saturation_threshold"], 48)

    def test_direct_lower_bound(self) -> None:
        row = self.payload["n7"]
        self.assertTrue(row["all_degree_thresholds_at_most_48"])
        self.assertEqual(row["direct_tower_lower_bound"], 48)
        self.assertEqual(row["ordinary_lower_bound"], 48)

    def test_enhanced_closure(self) -> None:
        row = self.payload["n7"]
        self.assertEqual(row["koszul_only_step_at_36"], 46)
        self.assertEqual(row["koszul_only_step_at_48"], 48)
        self.assertEqual(row["enhanced_sequence"], [36, 48, 48])

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_TOWER_SATURATION_CLOSURE_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=48", completed.stdout)
        self.assertIn("independent_n7_scalar_tower_closure=48", completed.stdout)


if __name__ == "__main__":
    unittest.main()
