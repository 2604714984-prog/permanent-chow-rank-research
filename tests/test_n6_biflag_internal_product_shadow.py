from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_biflag_internal_product_shadow.py"
DATA = ROOT / "data" / "n6_biflag_internal_product_shadow.json"
SPEC = importlib.util.spec_from_file_location("n6105", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestN6105(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_canonical_biflag(self) -> None:
        cells = MODULE.canonical_biflag_cells()
        self.assertEqual(len(cells), 23)
        self.assertEqual(len(MODULE.rectangle_supports(cells)), 72)

    def test_complete_coordinate_enumeration(self) -> None:
        coordinate = self.payload["coordinate_enumeration"]
        self.assertEqual(coordinate["enumerated_twelve_cell_support_count"], 1_352_078)
        self.assertEqual(coordinate["supports_with_intersection_dimension_at_least_15"], 34)

    def test_only_product_survivors(self) -> None:
        coordinate = self.payload["coordinate_enumeration"]
        self.assertEqual(coordinate["survivor_product_shape_counts"], {"3x4": 20, "4x3": 14})
        self.assertTrue(coordinate["every_survivor_is_a_complete_product_support"])
        self.assertTrue(coordinate["every_survivor_has_intersection_dimension_18"])

    def test_intrinsic_interface(self) -> None:
        intrinsic = self.payload["intrinsic_biflag_space"]
        self.assertEqual(intrinsic["torus_specialization_upper_bound"], 72)
        self.assertEqual(intrinsic["conclusion"], "K=E2 intersect Sym^2(M)")

    def test_first_leakage_gap(self) -> None:
        leakage = self.payload["coordinate_first_leakage"]
        self.assertEqual(leakage["stabilizer_orbit_count"], 6)
        self.assertEqual(leakage["kernel_dimensions"], [7, 7, 10, 6, 6, 4])
        self.assertEqual(leakage["minimum_rank_outside_every_kernel"], 6)
        self.assertEqual(leakage["rank_allowed_by_retaining_a_15_plane_inside_an_18_plane"], 3)

    def test_core_chart_reduction(self) -> None:
        core = self.payload["core_chart"]
        self.assertEqual(core["mixed_graph_intersection_upper_bound"], 12)
        self.assertEqual(core["required_intersection_dimension"], 15)
        self.assertIn("product", core["conclusion"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(json.loads(DATA.read_text(encoding="utf-8")), self.payload)


if __name__ == "__main__":
    unittest.main()
