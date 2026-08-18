from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_sharp_pair_threshold.py"
INDEPENDENT = ROOT / "scripts" / "general_sharp_pair_threshold_independent.py"
FROZEN = ROOT / "data" / "general_sharp_pair_threshold.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_sharp_pair_threshold_test_module",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load sharp-pair module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SharpPairThresholdTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_two_row_identity(self) -> None:
        for m in (2, 3, 4, 5):
            with self.subTest(m=m):
                self.assertEqual(
                    self.module.transformed_permanent(m),
                    self.module.split_rhs(m),
                )

    def test_threshold_rows(self) -> None:
        payload = self.module.build_payload()
        rows = {
            row["m"]: row
            for row in payload["exact_replay"]["threshold_rows"]
        }
        self.assertEqual(rows[3]["universal_zero_maximum_n"], 5)
        self.assertEqual(rows[3]["first_nonzero_n"], 6)
        self.assertEqual(rows[4]["first_nonzero_n"], 12)
        self.assertEqual(rows[10]["first_nonzero_n"], 90)

    def test_frozen_payload(self) -> None:
        generated = self.module.build_payload()
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(generated, frozen)
        self.assertEqual(
            generated["core_sha256"],
            "764ec72551012125c7f948df161795a93f2c34e3eaf9917dd45055464cd1ddc6",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_SHARP_PAIR_THRESHOLD_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
