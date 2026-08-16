from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_shadow_incidence_entropy_barrier.py"
FROZEN = ROOT / "data" / "general_shadow_incidence_entropy_barrier.json"

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


AUDIT = load_module("general_shadow_incidence_entropy_barrier", SCRIPT)


class GeneralShadowIncidenceEntropyBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["shadow_sandwich_checks"], 17_378)
        self.assertEqual(replay["inverse_sandwich_checks"], 17_378)

    def test_normalization_boundary(self) -> None:
        rows = self.payload["normalization_diagnostics"]
        self.assertEqual(rows["7"]["theta"], 49)
        self.assertEqual(rows["8"]["theta"], 90)
        self.assertEqual(rows["9"]["theta"], 164)
        self.assertEqual(rows["10"]["theta"], 307)
        for row in rows.values():
            self.assertGreaterEqual(row["theta"], row["central_binomial"])
            self.assertLessEqual(row["theta"], row["glynn_upper"])

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "3abb3cc354c8de4511bddb75d7e3477fb5de5a7871c02adcaa038230e2754741",
        )


if __name__ == "__main__":
    unittest.main()
