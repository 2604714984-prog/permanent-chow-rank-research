from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_excess_m_simplex_reduction.py"
INDEPENDENT = SCRIPTS / "general_excess_m_simplex_reduction_independent.py"
BOUNDARY = ROOT / "data" / "general_excess_m_simplex_reduction_boundary.json"
PROOF = ROOT / "docs" / "general_excess_m_simplex_reduction.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_excess_m_simplex_reduction", PRIMARY)


class GeneralExcessMSimplexReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.boundary = json.loads(BOUNDARY.read_text(encoding="utf-8"))

    def test_frozen_boundary(self) -> None:
        for key in (
            "status",
            "theorem",
            "simplex",
            "quartic_boundary",
            "selected_zero_block_examples",
            "claim_boundary",
        ):
            self.assertEqual(self.payload[key], self.boundary[key], key)

    def test_exact_cubic_boundary_rows(self) -> None:
        rows = self.payload["cubic_rows"]
        self.assertEqual(
            [(row["n"], row["q"]) for row in rows],
            [(3, 4), (4, 3), (6, 2)],
        )
        self.assertTrue(all(row["route"] == "OPEN_CUBIC_BOUNDARY" for row in rows))

    def test_every_m_ge_five_row_has_both_strict_gaps(self) -> None:
        for row in self.payload["scan"]["rows"]:
            if row["m"] >= 5:
                self.assertTrue(row["strict_private_gap"], row)
                self.assertTrue(row["simplex_support_gap"], row)
                self.assertEqual(row["route"], "PRIVATE_STRICT_OR_SIMPLEX_DIFFERENCE")

    def test_quartic_rows_and_private_shadow_boundary(self) -> None:
        rows = [row for row in self.payload["scan"]["rows"] if row["m"] == 4]
        self.assertEqual(
            [(row["n"], row["q"]) for row in rows],
            [(4, 5), (5, 4), (10, 2)],
        )
        quartic = self.payload["quartic_boundary"]
        self.assertEqual(quartic["sum_private_polar_dimension_floor"], 12)
        self.assertEqual(quartic["one_private_polar_dimension_floor"], 6)
        self.assertEqual(quartic["minimum_two_rectangle_union"], 12)
        self.assertGreater(quartic["minimum_two_rectangle_union"], quartic["n"])

    def test_selected_zero_blocks(self) -> None:
        self.assertEqual(
            self.payload["selected_zero_block_examples"],
            [
                {"n": 4, "m": 4, "zeta_m": 5},
                {"n": 5, "m": 4, "zeta_m": 4},
                {"n": 10, "m": 4, "zeta_m": 2},
                {"n": 6, "m": 5, "zeta_m": 5},
                {"n": 10, "m": 5, "zeta_m": 3},
            ],
        )

    def test_proof_states_simplex_and_open_cubic_boundary(self) -> None:
        text = PROOF.read_text(encoding="utf-8")
        compact = text.replace(" ", "")
        self.assertIn("qn\\lem^2+m", compact)
        self.assertIn("vector-space simplex", text)
        self.assertIn("(6,3,2)", text)
        self.assertIn("qn=m^2+m+1", compact)
        self.assertNotIn("exact Chow rank for", text)

    def test_primary_cli_under_optimized_python(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn("GENERAL_EXCESS_M_SIMPLEX_REDUCTION_AUDIT_PASS", completed.stdout)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_EXCESS_M_SIMPLEX_REDUCTION_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_simplex_checks=9", completed.stdout)
        self.assertIn("independent_quartic_minimum_two_rectangle_union=12", completed.stdout)


if __name__ == "__main__":
    unittest.main()
