from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_row_column_coupling_exclusion.py"
FROZEN = ROOT / "data" / "n6_alpha3_row_column_coupling_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6053", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Alpha3RowColumnCouplingExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_exact_QQ_example(self) -> None:
        example = self.payload["exact_QQ_sign_example"]
        self.assertEqual(
            (
                example["exact_QQ_sign_matrix_rank"],
                example["exact_QQ_rank_one_square_span_rank"],
                example["exact_QQ_rank_one_cube_span_rank"],
                example["total_twenty_column_triple_intersection_dimension"],
            ),
            (4, 6, 6, 40),
        )

    def test_coordinate_differential_diagnostic(self) -> None:
        diagnostic = self.payload["coordinate_quotient_differential_diagnostic"]
        self.assertEqual(diagnostic["rank_histogram"], {"205": 2, "210": 74})
        self.assertEqual(
            [row["row_masks"] for row in diagnostic["exceptional_orbits"]],
            [[0, 0, 0, 0, 0, 63], [1, 1, 1, 1, 1, 1]],
        )

    def test_strict_coupled_gap(self) -> None:
        theorem = self.payload["pure_coupling_theorem"]
        self.assertEqual(
            (
                theorem["total_intersection_upper_bound"],
                theorem["required_intersection_b"],
                theorem["strict_gap"],
            ),
            (40, 60, 20),
        )

    def test_claim_boundary(self) -> None:
        self.assertIn("not every", self.payload["claim_boundary"])
        self.assertIn("does not yet exclude", self.payload["claim_boundary"])
        self.assertIn("border-rank", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
