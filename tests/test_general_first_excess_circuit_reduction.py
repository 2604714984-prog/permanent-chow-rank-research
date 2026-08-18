from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_first_excess_circuit_reduction.py"
INDEPENDENT = SCRIPTS / "general_first_excess_circuit_reduction_independent.py"
FROZEN = ROOT / "data" / "general_first_excess_circuit_reduction.json"
PROOF = ROOT / "docs" / "general_first_excess_circuit_reduction.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_first_excess_circuit_reduction", PRIMARY)


class GeneralFirstExcessCircuitReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_theorem_boundary(self) -> None:
        for key in (
            "status",
            "theorem",
            "ledger_branches",
            "selected_rows",
            "claim_boundary",
        ):
            self.assertEqual(self.payload[key], self.frozen[key], key)

    def test_unique_cubic_exception(self) -> None:
        cubic = [
            row
            for row in self.payload["scan"]["rows"]
            if row["m"] == 3
        ]
        self.assertEqual(
            cubic,
            [
                {
                    "n": 5,
                    "m": 3,
                    "q": 2,
                    "first_excess": 10,
                    "derivative_gap": False,
                }
            ],
        )

    def test_every_m_ge_four_row_has_strict_derivative_gap(self) -> None:
        for row in self.payload["scan"]["rows"]:
            if row["m"] >= 4:
                self.assertTrue(row["derivative_gap"], row)
                self.assertLess(row["n"], (row["m"] - 1) ** 2, row)

    def test_selected_first_excess_rows(self) -> None:
        rows = self.payload["selected_rows"]
        self.assertEqual(rows["5"], [{"n": 13, "q": 2}])
        self.assertEqual(
            rows["7"],
            [{"n": 10, "q": 5}, {"n": 25, "q": 2}],
        )
        self.assertEqual(rows["8"], [{"n": 13, "q": 5}])
        self.assertEqual(
            rows["13"],
            [
                {"n": 17, "q": 10},
                {"n": 34, "q": 5},
                {"n": 85, "q": 2},
            ],
        )

    def test_enlarged_zero_block_examples(self) -> None:
        self.assertEqual(AUDIT.zeta_plus(13, 5), 2)
        self.assertEqual(AUDIT.zeta_plus(10, 7), 5)
        self.assertEqual(AUDIT.zeta_plus(25, 7), 2)
        self.assertEqual(AUDIT.zeta_plus(13, 8), 5)

    def test_ledger_is_exactly_one_hot(self) -> None:
        for name, branch in self.payload["ledger_branches"].items():
            self.assertEqual(
                sum(branch[key] for key in ("a", "b", "c", "d")),
                1,
                name,
            )

    def test_proof_keeps_the_cubic_boundary_open(self) -> None:
        text = PROOF.read_text(encoding="utf-8")
        self.assertIn("(5,3,2)", text)
        self.assertIn("m\\ge4", text.replace(" ", ""))
        self.assertIn("full-support linear circuit", text)
        self.assertNotIn("border-rank improvement", text.lower())

    def test_primary_cli_under_optimized_python(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_FIRST_EXCESS_CIRCUIT_REDUCTION_AUDIT_PASS",
            completed.stdout,
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
            "GENERAL_FIRST_EXCESS_CIRCUIT_REDUCTION_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_cubic_exception=(5,3,2)", completed.stdout)


if __name__ == "__main__":
    unittest.main()
