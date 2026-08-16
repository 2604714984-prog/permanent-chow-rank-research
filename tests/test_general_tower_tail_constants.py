from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_tower_tail_constants.py"
INDEPENDENT = SCRIPTS / "general_tower_tail_constants_independent.py"
FROZEN = ROOT / "data" / "general_tower_tail_constants.json"

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


AUDIT = load_module("general_tower_tail_constants", SCRIPT)


class GeneralTowerTailConstantsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_tail_constants(self) -> None:
        constants = self.payload["tail_constants"]
        self.assertEqual(
            [constants[str(k)]["value"] for k in range(2, 9)],
            [1, 5, 20, 83, 362, 1572, 7513],
        )

    def test_threshold_monotonicity_and_top_gap(self) -> None:
        for row in self.payload["threshold_replay"].values():
            values = row["by_degree"]
            self.assertTrue(
                all(left <= right for left, right in zip(values, values[1:]))
            )
            self.assertIn(row["top_gap"], (0, 1))
            self.assertEqual(row["theta"], values[-1])

    def test_top_row_criterion(self) -> None:
        expected = {"3": 4, "4": 8, "5": 15, "6": 27, "7": 49, "8": 90}
        self.assertEqual(
            {
                key: row["criterion_value"]
                for key, row in self.payload["top_row_criteria"].items()
            },
            expected,
        )

    def test_exact_replay_counts(self) -> None:
        replay = self.payload["exhaustive_replay"]
        self.assertEqual(replay["capacity_lipschitz_checks"], 1_151)
        self.assertEqual(replay["threshold_monotonicity_checks"], 21)
        self.assertEqual(replay["rectangular_shadow_checks"], 32_373)
        self.assertEqual(replay["tail_transport_checks"], 430)
        self.assertEqual(replay["tail_threshold_checks"], 9)
        self.assertEqual(replay["bipartite_graphs_enumerated"], 66_048)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "562ef480c5c3b9c95112ea5c3a3dab9ef36be019489251611e5f4855a6df0bf7",
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
            "GENERAL_TOWER_TAIL_CONSTANTS_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_tail_constants=1,5,20,83,362,1572,7513",
            completed.stdout,
        )
        self.assertIn(
            "independent_top_thresholds=4,8,15,27,49,90",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
