from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_excess_m_plus_four_band.py"
INDEPENDENT = ROOT / "scripts" / "general_excess_m_plus_four_band_independent.py"
FROZEN = ROOT / "data" / "general_excess_m_plus_four_band_boundary.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_excess_m_plus_four_band_test",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GeneralExcessMPlusFourBandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)
        self.assertEqual(
            self.payload["core_sha256"],
            "22459deec3fadc4cff91ae9cc6aa731414dc733ade453093bdd91812d2bcb25d",
        )

    def test_private_shadow_exceptions(self) -> None:
        rows = self.payload["private_branch"]["exceptions"]
        self.assertEqual(
            [(row["m"], row["excess"], row["n"], row["q"]) for row in rows],
            [(4, 6, 11, 2), (5, 7, 16, 2), (5, 9, 17, 2)],
        )
        self.assertTrue(
            all(row["two_plane_iterated_shadow"] > row["component_variable_cap"] for row in rows)
        )

    def test_pair_supported_exceptions(self) -> None:
        rows = self.payload["no_private_branch"]["exceptions"]
        self.assertEqual(
            [(row["m"], row["excess"], row["n"], row["q"]) for row in rows],
            [(6, 9, 9, 5), (7, 11, 10, 6), (12, 16, 16, 10)],
        )
        self.assertTrue(all(row["pair_annihilator_margin"] > 0 for row in rows))
        self.assertTrue(
            all(row["two_block_support"] < row["lower_output_shadow_floor"] for row in rows)
        )

    def test_selected_zero_blocks(self) -> None:
        expected = {
            (7, 4): 3,
            (11, 4): 2,
            (8, 5): 4,
            (16, 5): 2,
            (9, 6): 5,
            (10, 7): 6,
            (16, 12): 10,
        }
        observed = {
            (row["n"], row["m"]): row["guaranteed_terms"]
            for row in self.payload["selected_zero_blocks"]
        }
        self.assertEqual(observed, expected)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_EXCESS_M_PLUS_FOUR_BAND_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_private_exceptions=3", completed.stdout)
        self.assertIn("independent_pair_supported_exceptions=3", completed.stdout)


if __name__ == "__main__":
    unittest.main()
