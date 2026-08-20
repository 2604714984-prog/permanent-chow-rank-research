from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_single_cross_determinant_weight.py"
FROZEN = ROOT / "data" / "n6_k32_single_cross_determinant_weight.json"


spec = importlib.util.spec_from_file_location(
    "n6_k32_single_cross_determinant_weight", SCRIPT
)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-123 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32SingleCrossDeterminantWeightTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_weight_obstruction(self) -> None:
        exact = self.payload["exact_certificate"]
        self.assertEqual(exact["determinant_weight"], [0, 0, -3, -3, 3, 3])
        self.assertEqual(exact["positive_c3_variables"], [1])
        self.assertTrue(exact["no_surviving_determinant_weight_monomial"])

    def test_all_four_facets_are_obstructed(self) -> None:
        obstructions = self.payload["exact_certificate"]["facet_obstructions"]
        self.assertEqual(len(obstructions), 4)
        self.assertTrue(all(item["reason"] for item in obstructions))

    def test_symmetry_orbit_scope(self) -> None:
        orbit = self.payload["symmetry_orbit"]
        self.assertEqual(orbit["unit_directions_covered"], 24)
        self.assertTrue(orbit["nonzero_coefficient_torus_orbit"])


if __name__ == "__main__":
    unittest.main()
