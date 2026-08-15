from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT / "scripts" / "general_product_shadow_n8_coordinate_equality.py"
)
DATA_PATH = (
    ROOT / "data" / "general_product_shadow_n8_coordinate_equality.json"
)

SPEC = importlib.util.spec_from_file_location(
    "general_product_shadow_n8_coordinate_equality",
    MODULE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralProductShadowN8CoordinateEqualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()
        cls.frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_family_and_shadow_counts(self) -> None:
        self.assertEqual(
            self.payload["parameter_counts"]["families_per_orientation"],
            3360,
        )
        self.assertEqual(
            self.payload["parameter_counts"]["families_with_transposes"],
            6720,
        )
        self.assertEqual(
            self.payload["family_invariants"]["coordinate_pair_count"],
            560,
        )
        self.assertEqual(
            self.payload["family_invariants"]["simultaneous_shadow_size"],
            784,
        )

    def test_orbit_boundary(self) -> None:
        orbit = self.payload["orbit_invariants"]
        self.assertEqual(orbit["S8xS8_orbits_per_orientation"], 1)
        self.assertEqual(orbit["orbits_after_adjoining_transpose"], 1)
        self.assertTrue(orbit["parameter_map_injective"])
        self.assertTrue(orbit["orientation_sets_disjoint"])


if __name__ == "__main__":
    unittest.main()
