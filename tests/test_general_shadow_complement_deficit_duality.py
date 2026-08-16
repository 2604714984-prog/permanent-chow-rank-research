from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_shadow_complement_deficit_duality.py"
INDEPENDENT = SCRIPTS / "general_shadow_complement_deficit_duality_independent.py"
FROZEN = ROOT / "data" / "general_shadow_complement_deficit_duality.json"

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


AUDIT = load_module("general_shadow_complement_deficit_duality", SCRIPT)


class GeneralShadowComplementDeficitDualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exhaustive_counts(self) -> None:
        replay = self.payload["exhaustive_replay"]
        self.assertEqual(replay["duality_identity_checks"], 17_378)
        self.assertEqual(replay["tower_deficit_entry_checks"], 1_178)

    def test_threshold_rows(self) -> None:
        self.assertEqual(
            self.payload["exhaustive_replay"]["thresholds"],
            {
                "3": [3, 4],
                "4": [4, 7, 8],
                "5": [5, 11, 14, 15],
                "6": [6, 16, 24, 26, 27],
                "7": [7, 22, 39, 46, 48, 49],
                "8": [8, 29, 59, 80, 87, 89, 90],
            },
        )

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)

    def test_small_exact_identity(self) -> None:
        tables = {
            degree: AUDIT.ExactInverseShadow(5, degree)
            for degree in range(2, 5)
        }
        # One nontrivial central jump, checked directly from the complete
        # tables rather than inferred from the frozen payload.
        degree = 3
        missing = 17
        lower_ambient = 100
        upper_ambient = 100
        self.assertEqual(
            tables[degree].gamma[lower_ambient - missing],
            upper_ambient - tables[3].minimum[missing],
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
            "GENERAL_SHADOW_COMPLEMENT_DEFICIT_DUALITY_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_duality_identity_checks=17378", completed.stdout)
        self.assertIn("independent_tower_deficit_entry_checks=1178", completed.stdout)


if __name__ == "__main__":
    unittest.main()
