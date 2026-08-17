from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_fitting_betti_subquotient_barrier.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_fitting_betti_subquotient_barrier_independent.py"
)
FROZEN = ROOT / "data" / "general_fitting_betti_subquotient_barrier.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_fitting_betti_subquotient_barrier", SCRIPT)


class GeneralFittingBettiSubquotientBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_status_and_hash(self) -> None:
        self.assertEqual(self.payload["status"], self.frozen["status"])
        self.assertEqual(len(self.payload["core_sha256"]), 64)
        int(self.payload["core_sha256"], 16)

    def test_fitting_examples(self) -> None:
        fitting = self.payload["fitting_examples"]
        expected = self.frozen["expected"]
        self.assertEqual(
            fitting["colength_Fitt0_k"], expected["colength_Fitt0_k"]
        )
        self.assertEqual(
            fitting["colength_Fitt0_k2"], expected["colength_Fitt0_k2"]
        )
        self.assertEqual(fitting["Fitt_k"]["1"], [[0, 0]])
        self.assertEqual(fitting["Fitt_k2"]["1"], [[0, 1], [1, 0]])
        self.assertEqual(fitting["Fitt_R_mod_m2"]["1"], [[0, 0]])

    def test_betti_counterexamples(self) -> None:
        actual = self.payload["betti_examples"]
        expected = self.frozen["expected"]
        self.assertEqual(
            actual["quotient_source_R_mod_s2_t2"],
            expected["quotient_source_betti"],
        )
        self.assertEqual(
            actual["quotient_target_R_mod_m2"],
            expected["quotient_target_betti"],
        )
        self.assertEqual(
            actual["submodule_k2_shift1"], expected["submodule_betti"]
        )
        self.assertEqual(actual["ambient_R_mod_m2"], expected["ambient_betti"])

    def test_linewise_fitting_jordan_replay(self) -> None:
        actual = self.payload["linewise_replay"]
        expected = self.frozen["expected"]
        self.assertEqual(actual["partition_checks"], expected["partition_checks"])
        self.assertEqual(
            actual["jordan_ratio_checks"], expected["jordan_ratio_checks"]
        )
        self.assertEqual(actual["route_maxima"], expected["route_maxima"])

    def test_optimized_mode(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(SCRIPT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(
            "GENERAL_FITTING_BETTI_SUBQUOTIENT_BARRIER_AUDIT_PASS",
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
            "GENERAL_FITTING_BETTI_SUBQUOTIENT_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_partition_checks=271", completed.stdout)


if __name__ == "__main__":
    unittest.main()
