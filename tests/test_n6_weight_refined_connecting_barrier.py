from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_weight_refined_connecting_barrier.py"
SPEC = importlib.util.spec_from_file_location("n6_g040", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class WeightRefinedConnectingBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_exact_permanent_weight_decomposition(self) -> None:
        homology = self.payload["permanent_homology"]
        self.assertEqual(len(homology["row_heavy_weights"]), 20)
        self.assertEqual(len(homology["column_heavy_weights"]), 20)
        self.assertEqual(homology["weight_line_count"], 40)
        self.assertEqual(homology["preceding_boundary_on_all_forty_weights"], 0)
        self.assertEqual(
            homology["representative_exact_QQ_audit"]["exact_rational_rank"],
            119,
        )

    def test_candidate_has_only_trivial_unconditional_caps(self) -> None:
        self.assertEqual(
            self.payload["unconditional_candidate_bounds"],
            {
                "row_projection_rank": [0, 20],
                "column_projection_rank": [0, 20],
                "total_rank": [0, 40],
            },
        )

    def test_permanent_quotient_matching_erasure(self) -> None:
        row = self.payload["permanent_apolar_quotient_matching_erasure"]
        self.assertGreaterEqual(row["F3_dimension"], row["required_F3_lower"])
        self.assertGreaterEqual(row["F2_dimension"], row["required_F2_lower"])
        self.assertEqual(row["representative_retained_column_count"], 114)
        self.assertEqual(row["representative_retained_exact_QQ_rank"], 114)
        self.assertEqual(row["row_heavy_classes_in_image"], 0)
        self.assertEqual(row["column_heavy_classes_in_image"], 0)
        self.assertEqual(row["projected_connecting_kernel_rank"], 40)

    def test_g034_g037_stress_rows(self) -> None:
        rows = self.payload["g034_g037_exact_stress_rows"]
        self.assertEqual(
            [
                (row["ordinary_middle_relation_dimension"], row["labelled_presentation_kernel"])
                for row in rows
            ],
            [(4, 0), (4, 7), (2, 12)],
        )


if __name__ == "__main__":
    unittest.main()
