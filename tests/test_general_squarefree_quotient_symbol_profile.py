from __future__ import annotations

import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_squarefree_quotient_symbol_profile.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_squarefree_quotient_symbol_profile_independent.py"
)
FROZEN = ROOT / "data" / "general_squarefree_quotient_symbol_profile.json"
PROOF = ROOT / "docs" / "general_squarefree_quotient_symbol_profile.md"


class GeneralSquarefreeQuotientSymbolProfileTests(unittest.TestCase):
    def load_module(self):
        namespace: dict[str, object] = {}
        exec(compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec"), namespace)
        return namespace

    def test_frozen_payload(self) -> None:
        namespace = self.load_module()
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(namespace["payload"](), expected)

    def test_single_degree_formula(self) -> None:
        namespace = self.load_module()
        self.assertEqual(
            [namespace["minimum_symbol_rank"](8, 4, d) for d in range(9)],
            [0, 35, 55, 65, 69, 70, 70, 70, 70],
        )

    def test_adjacent_additivity(self) -> None:
        namespace = self.load_module()
        for n in range(3, 20):
            for k in range(1, n):
                for d in range(n + 1):
                    self.assertEqual(
                        namespace["adjacent_minimum_rank"](n, k, d),
                        namespace["minimum_symbol_rank"](n, k, d)
                        + namespace["minimum_symbol_rank"](n, k + 1, d),
                    )

    def test_all_degree_identity(self) -> None:
        namespace = self.load_module()
        for n in range(2, 20):
            for d in range(n + 1):
                self.assertEqual(
                    sum(
                        namespace["minimum_symbol_rank"](n, k, d)
                        for k in range(1, n + 1)
                    ),
                    (1 << n) - (1 << (n - d)),
                )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--max-n", "9"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_SQUAREFREE_QUOTIENT_SYMBOL_PROFILE_INDEPENDENT_PASS",
            completed.stdout,
        )

    def test_claim_boundary_and_no_bare_assert(self) -> None:
        payload = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertFalse(payload["claim_boundary"]["new_chow_rank_lower_bound"])
        self.assertEqual(
            payload["claim_boundary"]["cross_degree_homology_quotient"],
            "NOT_COVERED",
        )
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        proof = PROOF.read_text(encoding="utf-8")
        self.assertIn("does not create cross-degree\ncompression", proof)


if __name__ == "__main__":
    unittest.main()
