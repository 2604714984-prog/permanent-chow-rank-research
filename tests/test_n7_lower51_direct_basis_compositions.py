from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower51_direct_basis_compositions.py"
SPEC = importlib.util.spec_from_file_location("n7_lower51_direct_basis_compositions", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DirectBasisCompositionTests(unittest.TestCase):
    def test_independent_enumerations_agree(self) -> None:
        recursive = MODULE.enumerate_recursive()
        independent = tuple(
            row
            for row in MODULE.enumerate_dp(1, 49, 35)
            if MODULE.subset_floor_ok(row)
        )
        self.assertEqual(recursive, independent)

    def test_frozen_counts(self) -> None:
        payload = MODULE.build()
        self.assertEqual(payload["surviving_compositions"], 69)
        self.assertEqual(payload["low_rank_compositions"], 67)
        self.assertEqual(payload["rank5_equality_near_typed_rows"], 240)

    def test_every_row_satisfies_gates(self) -> None:
        payload = MODULE.build()
        for row in payload["rows"]:
            counts = row["counts_rank_1_through_7"]
            self.assertEqual(sum(rank * count for rank, count in enumerate(counts, 1)), 49)
            self.assertLessEqual(
                sum(a * b for a, b in zip(counts, MODULE.FULL_INCREMENT_FLOOR)),
                35,
            )
            self.assertTrue(MODULE.subset_floor_ok(counts))
            self.assertEqual(
                row["maximum_residual_middle_cap"],
                35 - row["full_increment_surplus_floor"],
            )
            self.assertLessEqual(
                3 * row["maximum_rank5_near_equality_terms"],
                row["maximum_residual_middle_cap"],
            )


if __name__ == "__main__":
    unittest.main()
