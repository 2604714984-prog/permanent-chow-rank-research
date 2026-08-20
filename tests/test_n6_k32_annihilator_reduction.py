import importlib.util
import json
import unittest
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_annihilator_reduction.py"
FROZEN = ROOT / "data" / "n6_k32_annihilator_reduction.json"

spec = importlib.util.spec_from_file_location("n6_k32_annihilator_reduction", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class AnnihilatorReductionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_dimensions(self):
        rows = {row["name"]: row for row in self.payload["examples"]}
        self.assertEqual((rows["identity"]["cross_rank_over_QQ"], rows["identity"]["b_dimension"], rows["identity"]["c_dimension"]), (6, 9, 3))
        self.assertEqual((rows["matching_diagonal"]["cross_rank_over_QQ"], rows["matching_diagonal"]["b_dimension"], rows["matching_diagonal"]["c_dimension"]), (6, 9, 3))
        self.assertEqual(rows["row_shear"]["cross_rank_over_QQ"], 12)
        self.assertEqual(rows["column_row_permutation"]["cross_rank_over_QQ"], 14)

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)

    def test_c_space_uses_linear_membership_not_support_only(self):
        # This permutation mixes two row-edge components inside the same
        # support pattern.  A support-only quotient incorrectly reports
        # c=1; the exact A-space quotient gives the direct rank identity.
        mixed = sp.Matrix(
            [
                [1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
            ]
        )
        cross, annihilator, b_dim, c_dim = module.reduction_dimensions(mixed)
        self.assertEqual((cross, annihilator, b_dim, c_dim), (16, 2, 2, 0))

    def test_diagonal_block_b_formula(self):
        for entries in (
            (1, 1, 1, 1, 1, 1),
            (1, 2, 1, 2, 1, 2),
            (1, 2, 3, 4, 5, 6),
        ):
            matrix = sp.diag(*entries)
            _, _, b_dim, _ = module.reduction_dimensions(matrix)
            self.assertEqual(b_dim, module.diagonal_block_b_dimension(entries))
        self.assertEqual(module.diagonal_block_b_dimension((1, 2, 1, 2, 1, 2)), 9)

    def test_common_two_by_two_block_subfamily(self):
        non_monomial = sp.Matrix([[1, 2], [3, 4]])
        monomial = sp.Matrix([[0, 1], [2, 0]])
        for block, expected in (
            (non_monomial, (9, 9, 9, 0)),
            (monomial, (6, 12, 9, 3)),
        ):
            cross, annihilator, b_dim, c_dim = module.reduction_dimensions(
                sp.diag(block, block, block)
            )
            self.assertEqual((cross, annihilator, b_dim, c_dim), expected)

    def test_single_off_diagonal_block_is_excluded(self):
        for block in (sp.eye(2), sp.Matrix([[1, 2], [3, 4]])):
            matrix = sp.eye(6)
            matrix[0:2, 2:4] = block
            cross, _, b_dim, _ = module.reduction_dimensions(matrix)
            self.assertLessEqual(b_dim, 6)
            self.assertGreaterEqual(cross, 9)

    def test_unit_upper_triangular_three_block_slice_is_excluded(self):
        cases = (
            (sp.zeros(2), sp.eye(2)),
            (sp.eye(2), sp.eye(2)),
            (sp.Matrix([[1, 2], [3, 4]]), sp.Matrix([[0, 1], [2, 0]])),
        )
        for first, second in cases:
            matrix = sp.eye(6)
            matrix[0:2, 2:4] = first
            matrix[2:4, 4:6] = second
            cross, _, b_dim, _ = module.reduction_dimensions(matrix)
            self.assertLess(b_dim, 9)
            self.assertGreaterEqual(cross, 9)

    def test_general_block_upper_triangular_slice_is_excluded(self):
        diagonal = sp.Matrix([[1, 2], [3, 4]])
        off_diagonal = (
            (0, 1, sp.eye(2)),
            (0, 2, sp.Matrix([[0, 1], [2, 0]])),
            (1, 2, sp.Matrix([[1, 1], [0, 1]])),
        )
        matrix = sp.zeros(6)
        for index in range(3):
            matrix[2 * index : 2 * index + 2, 2 * index : 2 * index + 2] = diagonal
        for row, column, block in off_diagonal:
            matrix[2 * row : 2 * row + 2, 2 * column : 2 * column + 2] = block
        cross, _, b_dim, _ = module.reduction_dimensions(matrix)
        self.assertEqual((cross, b_dim), (16, 2))

    def test_common_diagonal_block_cycles_are_excluded(self):
        diagonal = sp.Matrix([[1, 2], [3, 4]])
        reciprocal = sp.zeros(6)
        cycle = sp.zeros(6)
        for index in range(3):
            reciprocal[2 * index : 2 * index + 2, 2 * index : 2 * index + 2] = diagonal
            cycle[2 * index : 2 * index + 2, 2 * index : 2 * index + 2] = diagonal
        reciprocal[0:2, 2:4] = sp.Matrix([[1, 0], [0, 0]])
        reciprocal[2:4, 0:2] = sp.Matrix([[0, 1], [0, 0]])
        cycle[0:2, 2:4] = sp.Matrix([[1, 0], [0, 0]])
        cycle[2:4, 4:6] = sp.Matrix([[0, 1], [0, 0]])
        cycle[4:6, 0:2] = sp.Matrix([[0, 0], [1, 0]])
        for matrix in (reciprocal, cycle):
            cross, _, b_dim, _ = module.reduction_dimensions(matrix)
            self.assertLess(b_dim, 9)
            self.assertGreaterEqual(cross, 9)

    def test_cycle_edges_force_off_diagonal_projection_rank(self):
        rank_one = sp.Matrix([[1, 0], [0, 0]])
        edge_positions = {
            "D": (0, 1),
            "G": (0, 2),
            "H": (1, 0),
            "E": (1, 2),
            "K": (2, 0),
            "L": (2, 1),
        }

        def with_edges(names):
            matrix = sp.eye(6)
            for name in names:
                row, column = edge_positions[name]
                matrix[2 * row : 2 * row + 2, 2 * column : 2 * column + 2] = rank_one
            return matrix

        for names in (("D", "H"), ("G", "K"), ("E", "L"), ("D", "E", "K"), ("G", "H", "L")):
            self.assertGreaterEqual(module.off_diagonal_projection_rank(with_edges(names)), 4)


if __name__ == "__main__":
    unittest.main()
