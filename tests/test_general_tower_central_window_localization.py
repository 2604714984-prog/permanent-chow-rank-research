from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_tower_central_window_localization.py"
FROZEN = ROOT / "data" / "general_tower_central_window_localization.json"

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


AUDIT = load_module("general_tower_central_window_localization", SCRIPT)


class GeneralTowerCentralWindowLocalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_check_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["transition_checks"], 16)
        self.assertEqual(replay["binomial_constant_checks"], 16)
        self.assertEqual(replay["tail_bound_checks"], 16)

    def test_n8_interfaces(self) -> None:
        row = self.payload["finite_replay"]["table"]["8"]
        self.assertEqual(
            {
                key: value["c_nk"]
                for key, value in row["transition_constants"].items()
            },
            {"2": 1, "3": 5, "4": 20},
        )
        self.assertEqual(row["tail_bounds"]["4"]["actual_top_tail"], 10)
        self.assertEqual(row["tail_bounds"]["4"]["binomial_bound"], 92)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "334116f082662e53f35d7f634ab75cd3106f9e96b8303901c5e9c6d7823c4749",
        )


if __name__ == "__main__":
    unittest.main()
