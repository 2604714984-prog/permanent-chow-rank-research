from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_common_base_mixed_split_glynn_rigidity.py"
INDEPENDENT = ROOT / "scripts" / "general_common_base_mixed_split_glynn_rigidity_independent.py"
DATA = ROOT / "data" / "general_common_base_mixed_split_glynn_rigidity.json"
CORE = "b060620eec6f6a4dc016024ffec05230494b280af9275e8b4693be3a042ff93b"


def load_module():
    spec = importlib.util.spec_from_file_location("common_base_mixed_split", PRIMARY)
    if spec is None or spec.loader is None:
        raise RuntimeError(PRIMARY)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class CommonBaseMixedSplitGlynnRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        core = cls.module.build_core()
        cls.payload = dict(core)
        cls.payload["core_sha256"] = CORE

    def test_frozen_payload(self) -> None:
        self.assertEqual(cls_payload := self.payload, json.loads(DATA.read_text(encoding="utf-8")))
        self.assertEqual(cls_payload["core_sha256"], CORE)

    def test_general_threshold(self) -> None:
        for row in self.payload["rows"]:
            self.assertEqual(row["minimum_atom_count"], row["sign_count"] - 1)
            self.assertEqual(row["degree_m_quotient_rank"], row["sign_count"] - 1)
            self.assertEqual(row["degree_m_minus_two_defect_relation_dimension"], 1)
            self.assertEqual(row["defect_relation_support"], row["sign_count"] - 1)

    def test_quartic_equality_classification(self) -> None:
        scan = self.payload["quartic_exhaustive_equality_scan"]
        self.assertEqual(scan["assignments_checked"], 279936)
        self.assertEqual(scan["solutions"], 6)
        self.assertTrue(scan["all_solutions_uniform"])
        self.assertEqual(scan["solution_split_indices"], [[index] * 7 for index in range(6)])

    def test_quartic_boundary(self) -> None:
        quartic = self.payload["quartic_application"]
        self.assertEqual(quartic["fixed_base_dictionary_atoms"], 42)
        self.assertEqual(quartic["minimum_blocks"], 7)
        self.assertEqual(quartic["all_base_and_split_equality_families"], 48)
        self.assertEqual(quartic["six_block_representation"], "IMPOSSIBLE")
        self.assertEqual(quartic["mu_6_4"], "OPEN_IN_[6,7]")

    def test_independent_replay(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--expected-core", CORE],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("GENERAL_COMMON_BASE_MIXED_SPLIT_GLYNN_RIGIDITY_INDEPENDENT_PASS", result.stdout)

    def test_no_bare_assert(self) -> None:
        for path in (PRIMARY, INDEPENDENT):
            self.assertNotIn("assert ", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
