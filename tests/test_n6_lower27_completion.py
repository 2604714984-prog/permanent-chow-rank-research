from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower27_completion.py"
FROZEN = ROOT / "data" / "n6_lower27_completion.json"
SPEC = importlib.util.spec_from_file_location("n6_lower27_completion", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6LowerTwentySevenCompletionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_all_low_layers_are_strict(self) -> None:
        self.assertEqual([row["b"] for row in self.payload["low_layers"]], list(range(45, 53)))
        self.assertTrue(all(row["strict_margin"] > 0 for row in self.payload["low_layers"]))

    def test_exact_minima_and_margins(self) -> None:
        observed = {
            row["b"]: (
                row["minimum_coupled_middle_rank_lower"],
                row["twenty_term_residual_middle_rank_upper"],
                row["strict_margin"],
            )
            for row in self.payload["low_layers"]
        }
        self.assertEqual(
            observed,
            {
                45: (98, 90, 8), 46: (98, 92, 6),
                47: (112, 94, 18), 48: (112, 96, 16),
                49: (112, 98, 14), 50: (112, 100, 12),
                51: (120, 102, 18), 52: (120, 104, 16),
            },
        )

    def test_every_stored_profile_obeys_its_layer_constraints(self) -> None:
        for layer in self.payload["low_layers"]:
            for row in layer["profiles"]:
                epsilon = row["epsilon"]
                self.assertLessEqual(sum(epsilon) - min(epsilon), layer["defect_budget"])
                self.assertGreaterEqual(
                    row["coupled_middle_rank_lower"],
                    layer["minimum_coupled_middle_rank_lower"],
                )

    def test_rank_interval_and_boundary(self) -> None:
        self.assertEqual(self.payload["ordinary_rank_interval"], [27, 32])
        self.assertIn("does not prove border", self.payload["claim_boundary"])
        self.assertIn("does not determine", self.payload["claim_boundary"])

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
