from __future__ import annotations

import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_squarefree_quotient_koszul_homology.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_squarefree_quotient_koszul_homology_independent.py"
)
FROZEN = ROOT / "data" / "general_squarefree_quotient_koszul_homology.json"
PROOF = ROOT / "docs" / "general_squarefree_quotient_koszul_homology.md"


class GeneralSquarefreeQuotientKoszulHomologyTests(unittest.TestCase):
    def load_module(self):
        namespace: dict[str, object] = {}
        exec(compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec"), namespace)
        return namespace

    def test_frozen_payload(self) -> None:
        namespace = self.load_module()
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(namespace["payload"](), expected)

    def test_middle_profiles(self) -> None:
        namespace = self.load_module()
        self.assertEqual(
            [namespace["maximum_h1"](8, 4, d) for d in range(9)],
            [0, 35, 40, 30, 16, 5, 0, 0, 0],
        )

    def test_adjacent_pascal_identity(self) -> None:
        namespace = self.load_module()
        for n in range(3, 25):
            for d in range(n + 1):
                for k in range(1, n):
                    self.assertEqual(
                        namespace["adjacent_maximum_h1"](n, k, d),
                        d * namespace["c"](n - d + 1, k),
                    )

    def test_all_degree_identity(self) -> None:
        namespace = self.load_module()
        for n in range(2, 25):
            for d in range(n + 1):
                self.assertEqual(
                    sum(namespace["maximum_h1"](n, k, d) for k in range(1, n + 1)),
                    d * (1 << (n - d)),
                )

    def test_independent_sparse_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT), "--max-n", "6"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn(
            "GENERAL_SQUAREFREE_QUOTIENT_KOSZUL_HOMOLOGY_INDEPENDENT_PASS",
            completed.stdout,
        )

    def test_claim_boundary_and_no_bare_assert(self) -> None:
        payload = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertFalse(payload["claim_boundary"]["new_chow_rank_lower_bound"])
        self.assertEqual(
            payload["claim_boundary"]["arbitrary_dependent_or_repeated_term"],
            "OPEN",
        )
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        proof = PROOF.read_text(encoding="utf-8")
        self.assertIn("upper semicontinuous", proof)
        self.assertIn("does not establish a uniform cap", (ROOT / "docs" / "general_squarefree_quotient_koszul_homology_adversarial_review.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
