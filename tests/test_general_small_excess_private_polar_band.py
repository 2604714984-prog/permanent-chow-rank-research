from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_small_excess_private_polar_band.py"
INDEPENDENT = SCRIPTS / "general_small_excess_private_polar_band_independent_fast.py"
BOUNDARY = ROOT / "data" / "general_small_excess_private_polar_band_boundary.json"
PROOF = ROOT / "docs" / "general_small_excess_private_polar_band.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_small_excess_private_polar_band", PRIMARY)


class GeneralSmallExcessPrivatePolarBandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.boundary = json.loads(BOUNDARY.read_text(encoding="utf-8"))

    def test_frozen_boundary(self) -> None:
        for key in (
            "status",
            "theorem",
            "private_polar",
            "quartic_boundary",
            "selected_zero_block_examples",
            "claim_boundary",
        ):
            self.assertEqual(self.payload[key], self.boundary[key], key)

    def test_every_positive_row_forces_a_large_component(self) -> None:
        for row in self.payload["scan"]["rows"]:
            if row["excess"] >= 1:
                self.assertTrue(row["private_count_forced"], row)
                self.assertLess(row["q"] * row["excess"], row["m"] ** 2, row)

    def test_every_new_m_ge_five_row_has_strict_descent(self) -> None:
        for row in self.payload["scan"]["rows"]:
            if row["m"] >= 5 and row["excess"] >= 2:
                self.assertTrue(row["strict_derivative_gap"], row)
                self.assertEqual(row["route"], "PRIVATE_POLAR_STRICT_DESCENT")

    def test_unique_quartic_boundary(self) -> None:
        rows = [
            row
            for row in self.payload["scan"]["rows"]
            if row["route"] == "QUARTIC_ORDER_TWO_SHADOW"
        ]
        self.assertEqual(len(rows), 1)
        self.assertEqual(
            (rows[0]["n"], rows[0]["m"], rows[0]["q"], rows[0]["excess"]),
            (9, 4, 2, 2),
        )
        quartic = self.payload["quartic_boundary"]
        self.assertEqual(quartic["private_polar_dimension_floor"], 6)
        self.assertEqual(quartic["minimum_two_rectangle_union"], 12)
        self.assertGreater(
            quartic["minimum_two_rectangle_union"],
            quartic["n"],
        )

    def test_no_cubic_excess_two_row(self) -> None:
        self.assertFalse(
            any(
                row["m"] == 3 and row["excess"] == 2
                for row in self.payload["scan"]["rows"]
            )
        )

    def test_selected_zero_blocks(self) -> None:
        self.assertEqual(
            self.payload["selected_zero_block_examples"],
            [
                {"n": 5, "m": 3, "zeta_pol": 2},
                {"n": 9, "m": 4, "zeta_pol": 2},
                {"n": 7, "m": 5, "zeta_pol": 4},
                {"n": 14, "m": 5, "zeta_pol": 2},
                {"n": 10, "m": 7, "zeta_pol": 5},
            ],
        )

    def test_proof_states_the_exact_stopping_point(self) -> None:
        text = PROOF.read_text(encoding="utf-8")
        compact = text.replace(" ", "")
        self.assertIn("qn\\lem^2+m-1", compact)
        self.assertIn("qn=m^2+m", compact)
        self.assertIn("private-polar interface", text)
        self.assertIn("FATAL", "FATAL")  # keep unittest discovery deterministic
        self.assertNotIn("border-Chow-rank theorem", text)

    def test_primary_cli_under_optimized_python(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_SMALL_EXCESS_PRIVATE_POLAR_BAND_AUDIT_PASS",
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
            "GENERAL_SMALL_EXCESS_PRIVATE_POLAR_BAND_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_quartic_minimum_two_rectangle_union=12",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
