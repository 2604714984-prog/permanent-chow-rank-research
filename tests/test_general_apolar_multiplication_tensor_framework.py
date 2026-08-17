from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_apolar_multiplication_tensor_framework.py"
INDEPENDENT = (
    SCRIPTS / "general_apolar_multiplication_tensor_framework_independent.py"
)
FROZEN = ROOT / "data" / "general_apolar_multiplication_tensor_framework.json"

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


AUDIT = load_module("general_apolar_multiplication_tensor_framework", SCRIPT)


class GeneralApolarMultiplicationTensorFrameworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_factor_pairing_interfaces(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["boolean_top_pairing_checks"], 19)
        rows = {row["name"]: row for row in replay["factor_rows"]}
        self.assertEqual(rows["power_4"]["hilbert"], [1, 1, 1, 1, 1])
        self.assertEqual(
            rows["independent_quartic"]["hilbert"],
            [1, 4, 6, 4, 1],
        )

    def test_permanent_algebra_interfaces(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["multiplication_table_checks"], 84_720)
        self.assertEqual(replay["associativity_checks"], 89_224)
        rows = {row["n"]: row for row in replay["permanent_rows"]}
        self.assertEqual(rows[4]["dimension"], 70)
        self.assertEqual(rows[6]["dimension"], 924)

    def test_bound_arithmetic(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["bound_arithmetic_checks"], 120)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "c08cb4506bea294754c630e8b711747279b68b75fae64b82d8fdae6f66477f41",
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
            "GENERAL_APOLAR_MULTIPLICATION_TENSOR_FRAMEWORK_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_boolean_pairing_checks=23",
            completed.stdout,
        )
        self.assertIn(
            "independent_permanent_multiplication_checks=56540",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
