import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_two_transposition_join_obstruction.py"
DATA = ROOT / "data" / "n7_b2_two_transposition_join_obstruction.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_two_transposition_join_obstruction", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TwoTranspositionJoinTests(unittest.TestCase):
    def test_shared_row_half_join(self) -> None:
        row = MODULE.join_control("shared", ((0, 1), (0, 2)), sp.Rational(1, 2))
        self.assertTrue(row["polynomial_identity_holds"])
        self.assertEqual(
            tuple(row["unprojected_11_variable_complex"][key] for key in ("rank_B", "rank_C", "rank_BC", "kernel_image_defect")),
            (111, 94, 75, 10),
        )

    def test_disjoint_half_join(self) -> None:
        row = MODULE.join_control("disjoint", ((0, 1), (2, 3)), sp.Rational(1, 2))
        self.assertTrue(row["polynomial_identity_holds"])
        self.assertEqual(
            tuple(row["unprojected_11_variable_complex"][key] for key in ("rank_B", "rank_C", "rank_BC", "kernel_image_defect")),
            (114, 95, 81, 12),
        )

    def test_bounded_weight_scan_has_no_survivor(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(len(payload["rows"]), 10)
        self.assertTrue(all(not row["unprojected_11_variable_complex"]["sylvester_equality_holds"] for row in payload["rows"]))

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
