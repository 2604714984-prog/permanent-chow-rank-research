from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_packet_a_wzero_structure.py"
DATA = ROOT / "data" / "n7_packet_a_wzero_structure.json"
SPEC = importlib.util.spec_from_file_location("n7_packet_a_wzero_structure", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PacketAWzeroStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_two_support_exception_is_retained(self) -> None:
        zero = (0,) * 7
        slices = ((1, 1, 0, 0, 0, 0, 0), (1, -1, 0, 0, 0, 0, 0)) + (zero,) * 5
        result = MODULE.classify_wzero_row_slices(slices)
        self.assertEqual(result["type"], "exceptional_two_slice_two_column")
        self.assertEqual(result["active_factor_indices"], [0, 1])
        self.assertTrue(any(MODULE.same_column_witness_coordinates(slices[0], slices[1])))

    def test_three_support_forces_every_other_slice_zero(self) -> None:
        zero = (0,) * 7
        slices = ((1, 2, 3, 0, 0, 0, 0),) + (zero,) * 6
        result = MODULE.classify_wzero_row_slices(slices)
        self.assertEqual(result["type"], "at_most_one_nonzero_slice")

    def test_common_single_column_family(self) -> None:
        zero = (0,) * 7
        slices = ((2, 0, 0, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0, 0)) + (zero,) * 5
        result = MODULE.classify_wzero_row_slices(slices)
        self.assertEqual(result["type"], "common_single_column")
        self.assertTrue(any(MODULE.same_column_witness_coordinates(slices[0], slices[1])))

    def test_all_witnesses_zero_is_row_separated(self) -> None:
        factors = tuple(
            tuple(int(variable == row * 7 + (row + 1) % 7) for variable in range(49))
            for row in range(7)
        )
        self.assertTrue(MODULE.all_same_row_hessian_witnesses_zero(factors))
        self.assertEqual(MODULE.row_separation_permutation(factors), tuple(range(7)))

    def test_payload_and_flattening_boundary(self) -> None:
        row = self.payload["same_column_completion"]
        self.assertEqual(row["additional_witness_columns"], 49)
        self.assertEqual(row["all_same_row_witness_columns"], 196)
        flattening = self.payload["flattening_boundary"]
        self.assertEqual(flattening["row_bipartition_ranks_for_group_sizes_0_to_7"], [1, 7, 21, 35, 35, 21, 7, 1])
        self.assertEqual(flattening["maximum_rank"], 35)

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
