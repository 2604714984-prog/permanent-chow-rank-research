from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "general_same_span_chow_overlap.py"
INDEPENDENT_PATH = (
    ROOT / "scripts" / "general_same_span_chow_overlap_independent.py"
)
DATA_PATH = ROOT / "data" / "general_same_span_chow_overlap.json"

SPEC = importlib.util.spec_from_file_location(
    "general_same_span_chow_overlap",
    PRIMARY_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(PRIMARY_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralSameSpanChowOverlapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_sharp_quadratic_bound(self) -> None:
        self.assertEqual(self.payload["sharp_construction_case_count"], 88)
        self.assertEqual(
            self.payload["sharp_construction_table_sha256"],
            "b518dd2828afd2a1148eeb8673b5b8931e0f23feb0b69ecad2c3bb64423e2c6a",
        )
        for row in self.payload["sharp_selected_rows"]:
            self.assertEqual(
                row["common_quadratic_dimension"],
                MODULE.quadratic_bound(row["n"], row["dual_shared"]),
            )

    def test_dual_primal_distinction(self) -> None:
        self.assertEqual(
            self.payload["dual_primal_distinction"],
            {
                "dual_shared_direction_count": 3,
                "primal_shared_factor_count": 1,
                "common_quadratic_dimension": 5,
            },
        )

    def test_higher_degree_central_caps(self) -> None:
        observed = {
            row["n"]: row["higher_degree_overlap_cap"]
            for row in self.payload["central_no_dual_shared_rows"]
        }
        self.assertEqual(observed[6], 11)
        self.assertEqual(observed[8], 36)
        self.assertEqual(observed[10], 127)

    def test_frozen_payload_matches(self) -> None:
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "c0abb6ccda4733ac15a64af6ee8655b45f77d8eb6e3dd81ac43bde2bd7c9d8be",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_SAME_SPAN_CHOW_OVERLAP_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_n8_m4_overlap_cap=36", completed.stdout)


if __name__ == "__main__":
    unittest.main()
