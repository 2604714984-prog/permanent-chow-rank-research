from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower51_residual_redundancy.py"
SPEC = importlib.util.spec_from_file_location("n7_lower51_residual_redundancy", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ResidualRedundancyTests(unittest.TestCase):
    def test_every_strict_cap_is_excluded(self) -> None:
        for cap in range(35):
            self.assertEqual(
                MODULE.consequence(cap),
                "EXCLUDED_BY_REDUNDANT_IMAGE_PROPAGATION",
            )

    def test_cap_35_is_an_equality_boundary(self) -> None:
        self.assertEqual(MODULE.consequence(35), "FORCED_K3_0_K4_35")

    def test_invalid_caps_are_rejected(self) -> None:
        for cap in (-1, 36):
            with self.assertRaises(ValueError):
                MODULE.consequence(cap)


if __name__ == "__main__":
    unittest.main()
