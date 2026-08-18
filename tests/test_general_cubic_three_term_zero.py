from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "general_cubic_three_term_zero.py"
INDEPENDENT_PATH = ROOT / "scripts" / "general_cubic_three_term_zero_independent.py"
DATA_PATH = ROOT / "data" / "general_cubic_three_term_zero.json"


def load_primary():
    spec = importlib.util.spec_from_file_location("general_cubic_three_term_zero", PRIMARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(PRIMARY_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GeneralCubicThreeTermZeroTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primary = load_primary()

    def test_unique_private_polar_state(self) -> None:
        states = self.primary.private_states()
        self.assertEqual(len(states), 1)
        self.assertEqual(states[0]["ambient_dimension"], 9)
        self.assertEqual(states[0]["relation_defect"], 3)
        self.assertEqual(states[0]["component_ranks"], [4, 4, 4])
        self.assertEqual(states[0]["private_dimensions"], [1, 1, 1])

    def test_rank_four_rectangle_interfaces(self) -> None:
        result = self.primary.support_models()
        self.assertEqual(result["support_models_checked"], 25)
        self.assertEqual(result["restriction_dimension"], 1)

    def test_tensor_plane_parity(self) -> None:
        cases = self.primary.projection_cases()
        totals = sorted({value for row in cases for value in row["total_dimensions"]})
        self.assertEqual(totals, [8, 10, 12])
        self.assertNotIn(9, totals)
        
    def test_direct_three_four_term_frontiers(self) -> None:
        rows = {
            (row["m"], row["q"]): row
            for row in [self.primary.boundary_row(m, q) for m in range(3, 13) for q in (3, 4)]
        }
        self.assertEqual(rows[(3, 3)]["direct_zero_endpoint"], 4)
        self.assertEqual(rows[(3, 3)]["explicit_nonzero_start"], 6)
        self.assertEqual(rows[(3, 3)]["open_count"], 1)
        self.assertIsNone(rows[(3, 4)]["direct_zero_endpoint"])
        self.assertEqual(rows[(3, 4)]["explicit_nonzero_start"], 3)
        self.assertEqual(rows[(6, 4)]["direct_zero_endpoint"], 12)
        self.assertEqual(rows[(6, 4)]["zero_source"], "shifted equality theorem")

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(self.primary.build_payload(), expected)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_CUBIC_THREE_TERM_ZERO_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
