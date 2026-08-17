from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_fitt0_order_jordan_barrier.py"
INDEPENDENT = ROOT / "scripts" / "general_fitt0_order_jordan_barrier_independent.py"
FROZEN = ROOT / "data" / "general_fitt0_order_jordan_barrier.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_fitt0_order_jordan_barrier", SCRIPT)


class GeneralFitt0OrderJordanBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_status_and_hash(self) -> None:
        self.assertEqual(self.payload["status"], self.frozen["status"])
        self.assertEqual(len(self.payload["core_sha256"]), 64)
        int(self.payload["core_sha256"], 16)

    def test_finite_counts(self) -> None:
        replay = self.payload["finite_replay"]
        expected = self.frozen["expected"]
        self.assertEqual(
            replay["monomial_modules_checked"],
            expected["monomial_modules_checked"],
        )
        self.assertEqual(
            replay["finite_direct_sums_checked"],
            expected["finite_direct_sums_checked"],
        )
        self.assertEqual(
            replay["line_specializations_checked"],
            expected["line_specializations_checked"],
        )
        self.assertEqual(
            replay["permanent_boolean_ratio_cells"],
            expected["permanent_boolean_ratio_cells"],
        )

    def test_route_maxima(self) -> None:
        self.assertEqual(
            self.payload["finite_replay"]["route_maxima"],
            self.frozen["expected"]["route_maxima"],
        )

    def test_selected_nontrivial_staircases(self) -> None:
        for partition in ((2, 1), (3, 2, 1), (4, 4), (5, 3, 1)):
            self.assertEqual(
                AUDIT.fitting_order(partition),
                AUDIT.generic_line_block_count(partition),
            )

    def test_optimized_mode(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(SCRIPT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(
            "GENERAL_FITT0_ORDER_JORDAN_BARRIER_AUDIT_PASS",
            completed.stdout,
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
            "GENERAL_FITT0_ORDER_JORDAN_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_line_specializations_checked=337", completed.stdout)


if __name__ == "__main__":
    unittest.main()
