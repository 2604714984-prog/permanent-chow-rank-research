from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_two_direction_power_profiles.py"
INDEPENDENT = SCRIPTS / "general_two_direction_power_profiles_independent.py"
FROZEN = ROOT / "data" / "general_two_direction_power_profiles.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_two_direction_power_profiles", PRIMARY)


class GeneralTwoDirectionPowerProfilesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["profile_checks"], 52)
        self.assertEqual(replay["rank_cap_matches"], 104)
        self.assertEqual(replay["prime"], 1_000_003)

    def test_best_bounds(self) -> None:
        tables = self.payload["finite_replay"]["tables"]
        self.assertEqual(
            {key: value["best_certified_lower_bound"] for key, value in tables.items()},
            {"3": 3, "4": 6, "5": 10, "6": 20},
        )
        for value in tables.values():
            self.assertLess(
                value["best_certified_lower_bound"],
                value["existing_repository_lower_bound"],
            )

    def test_decisive_profiles(self) -> None:
        tables = self.payload["finite_replay"]["tables"]
        self.assertEqual(
            (
                tables["3"]["best_ratio_numerator"],
                tables["4"]["best_ratio_numerator"],
                tables["5"]["best_ratio_numerator"],
                tables["6"]["best_ratio_numerator"],
            ),
            (9, 31, 100, 400),
        )
        self.assertEqual(
            (
                tables["3"]["best_ratio_denominator"],
                tables["4"]["best_ratio_denominator"],
                tables["5"]["best_ratio_denominator"],
                tables["6"]["best_ratio_denominator"],
            ),
            (3, 6, 10, 20),
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "e6086e5cb2f884adbd17135fd41738610c11185830100007a22605e03a003b47",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(
            "GENERAL_TWO_DIRECTION_POWER_PROFILES_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_certified_bounds=3,6,10,20", completed.stdout)
        self.assertIn("independent_higher_power_checks=3", completed.stdout)


if __name__ == "__main__":
    unittest.main()
