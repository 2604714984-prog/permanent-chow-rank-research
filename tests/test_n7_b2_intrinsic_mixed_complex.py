import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_intrinsic_mixed_complex.py"
DATA = ROOT / "data" / "n7_b2_intrinsic_mixed_complex.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_intrinsic_mixed_complex", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class IntrinsicMixedComplexTests(unittest.TestCase):
    def test_rank_six_and_rank_seven_middle_spaces(self) -> None:
        rows = []
        for factors in (
            MODULE.rank_six_s1_factors(),
            MODULE.rank_six_s2_factors(),
            MODULE.rank_seven_factors(),
        ):
            b_hat, c_hat = MODULE.formal_labelled_maps(factors)
            b_i, c_i, catalectic = MODULE.intrinsic_rank_factorization(factors)
            self.assertEqual(b_i * c_i, b_hat * c_hat)
            self.assertEqual(catalectic, b_hat * c_hat)
            rows.append((b_hat.rank(), c_hat.rank(), catalectic.rank()))
        self.assertEqual(rows, [(25, 25, 25), (31, 29, 25), (35, 35, 35)])

    def test_factor_relabelling_preserves_catalectic(self) -> None:
        factors = MODULE.rank_six_s1_factors()
        permuted = [factors[index] for index in (6, 2, 4, 1, 5, 0, 3)]
        b0, c0, _ = MODULE.intrinsic_rank_factorization(factors)
        b1, c1, _ = MODULE.intrinsic_rank_factorization(permuted)
        self.assertEqual(b0 * c0, b1 * c1)

    def test_common_code_requires_extra_synchronization(self) -> None:
        controls = {row["name"]: row for row in MODULE.common_code_residual_controls()}
        self.assertFalse(controls["nonmonomial_factor_frame"]["relative_frame_is_monomial"])
        self.assertFalse(controls["off_block_graph_map"]["block_diagonal_graph_support_holds"])
        mismatch = controls["diagonal_tail_mismatch"]
        self.assertTrue(mismatch["relative_frame_is_monomial"])
        self.assertTrue(mismatch["block_diagonal_graph_support_holds"])
        self.assertFalse(mismatch["seven_diagonal_tails_match"])
        self.assertTrue(all(not row["common_code_morphism_defined"] for row in controls.values()))

    def test_projective_tail_normalization(self) -> None:
        identical = [[1, 2, 0, 0, 0, 0]] * 7
        proportional = [[scale, 0, 0, 0, 0, 0] for scale in range(1, 8)]
        mismatch = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]] + identical[:5]
        self.assertTrue(MODULE.projective_tails_match(identical))
        self.assertTrue(MODULE.projective_tails_match(proportional))
        self.assertFalse(MODULE.projective_tails_match(mismatch))
        self.assertFalse(MODULE.projective_tails_match([[0] * 6] * 7))

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        actual = MODULE.build_payload()
        self.assertEqual(actual["packet_cardinality"]["formal_labelled_middle_dimension"], 1715)
        self.assertEqual(actual["packet_cardinality"]["minimal_intrinsic_middle_dimension"], 1645)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
