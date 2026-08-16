from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_full_degree_tower_envelope.py"
INDEPENDENT = SCRIPTS / "general_full_degree_tower_envelope_independent.py"
FROZEN = ROOT / "data" / "general_full_degree_tower_envelope.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_full_degree_tower_envelope", SCRIPT)


class GeneralFullDegreeTowerEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_threshold_rows(self) -> None:
        self.assertEqual(
            self.payload["thresholds"],
            {
                "3": {"by_degree": [3, 4], "theta": 4},
                "4": {"by_degree": [4, 7, 8], "theta": 8},
                "5": {"by_degree": [5, 11, 14, 15], "theta": 15},
                "6": {"by_degree": [6, 16, 24, 26, 27], "theta": 27},
                "7": {"by_degree": [7, 22, 39, 46, 48, 49], "theta": 49},
                "8": {"by_degree": [8, 29, 59, 80, 87, 89, 90], "theta": 90},
                "9": {"by_degree": [9, 37, 87, 136, 155, 161, 163, 164], "theta": 164},
                "10": {
                    "by_degree": [10, 46, 123, 219, 280, 299, 305, 307, 307],
                    "theta": 307,
                },
            },
        )

    def test_new_rank_bounds(self) -> None:
        expected = {"7": 49, "8": 90, "9": 164, "10": 307}
        self.assertEqual(
            {
                key: value["tower_lower_bound"]
                for key, value in self.payload["new_bounds"].items()
            },
            expected,
        )

    def test_full_degree_boundaries(self) -> None:
        rows = self.payload["boundary_capacities"]
        self.assertEqual(rows["7"], {
            "degree": 6,
            "before_q": 48,
            "before": 44,
            "threshold_q": 49,
            "ambient": 49,
        })
        self.assertEqual(rows["8"], {
            "degree": 7,
            "before_q": 89,
            "before": 60,
            "threshold_q": 90,
            "ambient": 64,
        })
        self.assertEqual(rows["9"], {
            "degree": 8,
            "before_q": 163,
            "before": 74,
            "threshold_q": 164,
            "ambient": 81,
        })

    def test_small_n_fail_closed_regressions(self) -> None:
        self.assertEqual(self.payload["thresholds"]["5"]["theta"], 15)
        self.assertEqual(self.payload["thresholds"]["6"]["theta"], 27)
        self.assertLess(self.payload["thresholds"]["5"]["theta"], 16)
        self.assertLess(self.payload["thresholds"]["6"]["theta"], 28)

    def test_frozen_payload_matches_generator(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "679a8749388313fc558cc5bc7543d0585c728105c0c83985edcfba97d2cfb21f",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn(
            "GENERAL_FULL_DEGREE_TOWER_ENVELOPE_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_perm7_lower_bound=49", completed.stdout)
        self.assertIn("independent_perm8_lower_bound=90", completed.stdout)


if __name__ == "__main__":
    unittest.main()
