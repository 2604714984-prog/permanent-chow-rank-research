from __future__ import annotations

import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_even_middle_symbol_capacity_ceiling.py"
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_even_middle_symbol_capacity_ceiling_independent.py"
)
FROZEN = ROOT / "data" / "general_even_middle_symbol_capacity_ceiling.json"
PROOF = ROOT / "docs" / "general_even_middle_symbol_capacity_ceiling.md"


class GeneralEvenMiddleSymbolCapacityCeilingTests(unittest.TestCase):
    def load_module(self):
        namespace: dict[str, object] = {}
        exec(
            compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec"),
            namespace,
        )
        return namespace

    def test_frozen_payload(self) -> None:
        namespace = self.load_module()
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(namespace["payload"](64), expected)

    def test_n6_exact_saturation(self) -> None:
        namespace = self.load_module()
        row = namespace["row"](6)
        self.assertEqual(row["one_term_middle_rank_cap"], 20)
        self.assertEqual(row["route_ceiling"], 32)
        self.assertEqual(row["glynn_target"], 32)
        self.assertTrue(row["route_reaches_glynn_capacity"])

    def test_strict_failure_from_n8(self) -> None:
        namespace = self.load_module()
        for n in range(8, 202, 2):
            self.assertLess(namespace["route_ceiling"](n), namespace["glynn_target"](n))

    def test_normalized_ratio_decreases(self) -> None:
        namespace = self.load_module()
        rows = [namespace["row"](n) for n in range(8, 202, 2)]
        for left, right in zip(rows, rows[1:]):
            self.assertLess(
                right["route_ceiling"] * left["glynn_target"],
                left["route_ceiling"] * right["glynn_target"],
            )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--max-n", "64"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_EVEN_MIDDLE_SYMBOL_CAPACITY_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )

    def test_claim_boundary_and_no_bare_assert(self) -> None:
        payload = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertFalse(payload["claim_boundary"]["new_chow_rank_lower_bound"])
        self.assertEqual(
            payload["claim_boundary"]["multi_degree_coupled_symbols"],
            "NOT_COVERED",
        )
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        proof = PROOF.read_text(encoding="utf-8")
        self.assertIn("not a Chow-rank upper bound", proof)
        self.assertIn("constant-slope", proof)


if __name__ == "__main__":
    unittest.main()
