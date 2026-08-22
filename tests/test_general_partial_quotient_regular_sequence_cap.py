from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_partial_quotient_regular_sequence_cap.py"
INDEPENDENT = ROOT / "scripts" / "general_partial_quotient_regular_sequence_cap_independent.py"
FROZEN = ROOT / "data" / "general_partial_quotient_regular_sequence_cap.json"

spec = importlib.util.spec_from_file_location("regular_cap", PRIMARY)
module = importlib.util.module_from_spec(spec)
if spec.loader is None:
    raise RuntimeError("loader unavailable")
spec.loader.exec_module(module)


class RegularSequenceCapTests(unittest.TestCase):
    def test_frozen(self) -> None:
        self.assertEqual(module.payload(), json.loads(FROZEN.read_text()))

    def test_formula(self) -> None:
        for r in range(1, 30):
            for q in range(r + 1):
                for d in range(r + 1):
                    self.assertEqual(module.cap(r, q, d), (r - d) * min(q, d))

    def test_independent_scale(self) -> None:
        for r in range(1, 30):
            for q in range(r + 1):
                for d in range(r + 1):
                    self.assertLessEqual(module.cap(r, q, d), d * (r - d))

    def test_entry_points(self) -> None:
        for script in (PRIMARY, INDEPENDENT):
            completed = subprocess.run(
                [sys.executable, "-O", str(script)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PASS", completed.stdout)

    def test_no_bare_assert(self) -> None:
        for script in (PRIMARY, INDEPENDENT):
            self.assertNotIn("assert ", script.read_text())


if __name__ == "__main__":
    unittest.main()
