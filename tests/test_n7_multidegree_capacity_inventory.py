from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_multidegree_capacity_inventory.py"
SPEC = importlib.util.spec_from_file_location("n7_multidegree_capacity_inventory", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N7MultidegreeCapacityInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_towers(self) -> None:
        self.assertEqual(self.payload["derivative_tower"], [1, 49, 441, 1225, 1225, 441, 49, 1])
        self.assertEqual(self.payload["independent_chow_term_tower"], [1, 7, 21, 35, 35, 21, 7, 1])

    def test_scalar_route_ceilings(self) -> None:
        self.assertEqual(self.payload["full_apolar_length"]["integer_lower_bound"], 27)
        self.assertEqual(self.payload["first_koszul"]["best_integer_lower_bound"], 36)
        self.assertEqual(self.payload["imported_best_current_ordinary_lower_bound"]["value"], 41)

    def test_single_layer_gap(self) -> None:
        barrier = self.payload["single_middle_layer_barrier"]
        self.assertEqual(barrier, {
            "required_full_quotient_rank": 145,
            "available_full_quotient_capacity": 70,
            "gap": 75,
        })

    def test_all_standard_higher_wedge_ceiling(self) -> None:
        audit = self.payload["all_standard_higher_wedge_koszul_capacity"]
        self.assertEqual(audit["checked_pair_count"], 343)
        self.assertEqual(audit["maximum"]["output_degree"], 4)
        self.assertEqual(audit["maximum"]["wedge_degree"], 24)
        self.assertEqual(audit["maximum"]["ratio_upper_bound"], "24262105/402399")
        self.assertEqual(audit["maximum"]["integer_lower_bound_ceiling"], 61)
        self.assertFalse(self.payload["direct_sum_ceiling"]["reaches_64"])

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_multidegree_capacity_inventory.json").read_text(encoding="utf-8")
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
