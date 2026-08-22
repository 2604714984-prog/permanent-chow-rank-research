from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_near_extremal_six_plane_frontier.py"
SPEC = importlib.util.spec_from_file_location("n6_near_extremal_frontier", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NearExtremalSixPlaneFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_coordinate_positive_rectangle_types(self) -> None:
        coordinate = self.payload["coordinate_fixed_supports"]
        self.assertEqual(
            coordinate["oriented_positive_rectangle_isomorphism_histogram"],
            {"1": 12, "3": 2},
        )
        self.assertEqual(
            coordinate["unoriented_positive_rectangle_isomorphism_histogram"],
            {"1": 7, "3": 1},
        )
        self.assertEqual(coordinate["five_edge_maximum_rectangle_count"], 1)

    def test_correct_rank_le_19_leading_cone(self) -> None:
        local = self.payload["k23_rank_le_19_local_diagnostic"]
        self.assertEqual(local["rank_le_19_zariski_tangent_dimension"], 180)
        rows = {row["name"]: row for row in local["exact_direction_rows"]}
        self.assertEqual(rows["row_bad_pair"]["normal_schur_quadratic_rank"], 3)
        self.assertEqual(rows["row_bad_pair"]["linear_normal_schur_rank"], 0)
        self.assertTrue(rows["row_bad_pair"]["belongs_to_rank_le_19_ordinary_tangent_cone"])
        self.assertFalse(
            rows["row_bad_pair"][
                "zero_second_correction_straight_arc_passes_first_nonzero_schur_rank_condition"
            ]
        )
        self.assertEqual(rows["column_bad_pair"]["normal_schur_quadratic_rank"], 1)
        self.assertEqual(rows["column_bad_pair"]["linear_normal_schur_rank"], 0)
        self.assertTrue(rows["column_bad_pair"]["belongs_to_rank_le_19_ordinary_tangent_cone"])
        self.assertTrue(
            rows["column_bad_pair"][
                "zero_second_correction_straight_arc_passes_first_nonzero_schur_rank_condition"
            ]
        )

    def test_integrable_rank_two_family(self) -> None:
        rows = self.payload["k23_rank_le_19_local_diagnostic"][
            "integrable_column_family_exact_rows"
        ]
        self.assertEqual(len(rows), 4)
        for row in rows:
            self.assertEqual(row["exact_mu_ranks_at_parameters_1_and_2"], [19, 19])
            self.assertEqual(
                row["exact_intersection_dimensions_at_parameters_1_and_2"],
                [2, 2],
            )


if __name__ == "__main__":
    unittest.main()
