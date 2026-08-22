from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_variable_base_glynn_compression_rigidity.py"
INDEPENDENT = ROOT / "scripts" / "general_variable_base_glynn_compression_rigidity_independent.py"
DATA = ROOT / "data" / "general_variable_base_glynn_compression_rigidity.json"
CORE = "6d45f40e47ad3e150a9e62224f0f93145ce137db92fc3229c2ef9cc8d0c6aaca"

spec = importlib.util.spec_from_file_location("variable_base_glynn", PRIMARY)
if spec is None or spec.loader is None:
    raise RuntimeError(PRIMARY)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class VariableBaseGlynnCompressionRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.core = module.build_core()
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload["core_sha256"], CORE)
        live = dict(self.core)
        live["core_sha256"] = CORE
        self.assertEqual(live, self.payload)

    def test_general_rows(self) -> None:
        for row in self.core["rows"]:
            count = row["sign_count"]
            self.assertEqual(row["left_tensor_rank"], count - 1)
            self.assertEqual(row["minimum_dictionary_atoms"], count - 1)
            self.assertEqual(row["equality_families"], count)
            self.assertEqual(row["directed_dictionary_atoms"], count * (count - 1))

    def test_quartic_threshold(self) -> None:
        quartic = self.core["quartic"]
        self.assertEqual(quartic["directed_atoms"], 56)
        self.assertEqual(quartic["minimum_atoms"], 7)
        self.assertEqual(quartic["equality_families"], 8)
        self.assertEqual(
            quartic["consequence"],
            "SIX_ATOMS_IMPOSSIBLE_IN_VARIABLE_BASE_FIXED_SPLIT_FAMILY",
        )

    def test_direct_reconstructions(self) -> None:
        self.assertEqual(
            {key: value["omitted_bases_checked"] for key, value in self.core["direct_reconstructions"].items()},
            {"3": 4, "4": 8, "5": 16, "6": 32},
        )

    def test_independent_replay_and_no_bare_assert(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--expected-core", CORE],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn(
            "GENERAL_VARIABLE_BASE_GLYNN_COMPRESSION_RIGIDITY_INDEPENDENT_PASS",
            completed.stdout,
        )
        for path in (PRIMARY, INDEPENDENT):
            self.assertNotIn("assert ", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
