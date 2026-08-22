import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_join_completion_gap.py"
DATA = ROOT / "data" / "n7_b2_join_completion_gap.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_join_completion_gap", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class JoinCompletionGapTests(unittest.TestCase):
    def test_explicit_gap_dimensions_and_cross_block_support(self) -> None:
        rows = {name: MODULE.quotient_gap(name, pairs) for name, pairs in MODULE.join.JOIN_TYPES.items()}
        self.assertEqual(rows["shared_row_01_02"]["quotient_gap_dimension"], 10)
        self.assertEqual(rows["disjoint_01_23"]["quotient_gap_dimension"], 12)
        for row in rows.values():
            self.assertTrue(all(all(count > 0 for count in representative["support_by_35_column_term_block"]) for representative in row["sparse_gap_representatives"]))

    def test_generic_fifth_term_keeps_defect(self) -> None:
        expected = {"shared_row_01_02": 10, "disjoint_01_23": 12}
        for name, pairs in MODULE.join.JOIN_TYPES.items():
            row = MODULE.fifth_term_control(name, pairs, "dense_vandermonde")
            self.assertEqual(row["rank_increments_B_C_BC"], [35, 35, 35])
            self.assertEqual(row["new_defect"], expected[name])
            self.assertFalse(row["polynomial_identity_preserved_by_direct_append"])

    def test_structured_degenerations_do_not_repair(self) -> None:
        for name, pairs in MODULE.join.JOIN_TYPES.items():
            for kind in ("zero_graph", "diagonal"):
                self.assertFalse(MODULE.fifth_term_control(name, pairs, kind)["defect_eliminated"])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.build_payload(), expected)


if __name__ == "__main__":
    unittest.main()
