from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_shadow12_nonproduct_collision_exclusion.py"
DATA = ROOT / "data" / "n6_shadow12_nonproduct_collision_exclusion.json"
SPEC = importlib.util.spec_from_file_location("n6_shadow12_nonproduct", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class N6Shadow12NonproductCollisionExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text())
        cls.by_hook = {row["hook"]: row for row in cls.payload["hooks"]}

    def test_frozen_scope_and_counts(self) -> None:
        self.assertEqual(
            self.payload["status"],
            "EXACT_PROJECTIVE_NONPRODUCT_E12_PAIR_COMPONENT_EXCLUSION",
        )
        self.assertEqual(
            self.payload["arithmetic"]["coordinate_twelve_subsets_per_hook"],
            1_352_078,
        )
        self.assertEqual(
            self.by_hook["standard"][
                "intersection_dimension_histogram_for_at_least_twelve"
            ],
            {"12": 4872, "14": 3, "15": 6, "18": 34},
        )
        self.assertEqual(
            self.by_hook["biflag"][
                "intersection_dimension_histogram_for_at_least_twelve"
            ],
            {"12": 5124, "18": 34},
        )

    def test_all_e12_fixed_pairs_are_unique_diagonal_or_absent(self) -> None:
        self.assertEqual(
            self.by_hook["standard"][
                "e12_coordinate_crossfree_ordered_pair_count_histogram"
            ],
            {"0": 168, "1": 4704},
        )
        self.assertEqual(
            self.by_hook["biflag"][
                "e12_coordinate_crossfree_ordered_pair_count_histogram"
            ],
            {"0": 204, "1": 4920},
        )
        for row in self.payload["hooks"]:
            self.assertEqual(row["coordinate_complementary_partition_count"], 0)

    def test_full_rank_histograms(self) -> None:
        self.assertEqual(
            self.by_hook["standard"][
                "pair_variable_jacobian_rank_over_F2_histogram"
            ],
            {"72": 4704},
        )
        self.assertEqual(
            self.by_hook["biflag"][
                "pair_variable_jacobian_rank_over_F2_histogram"
            ],
            {"72": 4920},
        )
        self.assertTrue(
            self.payload["arithmetic"][
                "full_column_rank_over_F2_implies_full_rank_over_Q"
            ]
        )

    def test_one_representative_per_hook_replays_locally(self) -> None:
        for kind, frozen in self.by_hook.items():
            cells, rectangles = MODULE.hook_data(kind)
            representative = frozen["fixed_endpoint_representative"]
            u_cells = {tuple(cell) for cell in representative["U_cells"]}
            p_cells = {tuple(cell) for cell in representative["P_equals_Q_cells"]}
            support_mask = sum(
                1 << index for index, cell in enumerate(cells) if cell in u_cells
            )
            adjacency, quadrics = MODULE.edge_masks(support_mask, cells, rectangles)
            local_cells = tuple(cell for cell in cells if cell in u_cells)
            plane_mask = sum(
                1 << index for index, cell in enumerate(local_cells) if cell in p_cells
            )
            pair_count, unique_plane, diagonal = MODULE.coordinate_crossfree_pairs(
                adjacency
            )
            self.assertEqual(pair_count, 1)
            self.assertEqual(unique_plane, plane_mask)
            self.assertTrue(diagonal)
            self.assertEqual(MODULE.pair_jacobian_rank(quadrics, plane_mask), 72)

    def test_formal_conclusion_and_boundary(self) -> None:
        formal = self.payload["formal_argument"]
        self.assertTrue(formal["formal_relative_uniqueness_and_swap_force_P_equals_Q"])
        self.assertTrue(
            self.payload["conclusion"][
                "all_nonproduct_e12_fixed_endpoint_components_are_excluded"
            ]
        )
        boundary = self.payload["boundary"]
        self.assertIn("fourteen, fifteen, or eighteen remain", boundary)
        self.assertIn("does not by itself exclude the kappa2=0", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
