from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k34_rank_nine_fano_exclusion.py"
FROZEN = ROOT / "data" / "n6_k34_rank_nine_fano_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_k34_fano", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6K34RankNineFanoExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_coordinate_fano_fixed_points(self) -> None:
        scan = self.payload["fixed_support_scan"]
        self.assertEqual(scan["total_coordinate_six_planes"], 924)
        self.assertEqual(scan["rectangle_count"], 18)
        self.assertEqual(scan["rank_histogram"], {"9": 18, "10": 84, "12": 822})
        self.assertEqual(len(scan["rank_at_most_nine_supports"]), 18)

    def test_tangent_certificates_kill_every_weight(self) -> None:
        tangent = self.payload["tangent_certificates"]
        self.assertEqual(tangent["two_by_three"]["certified_tangent_dimension"], 0)
        self.assertEqual(tangent["three_by_two"]["certified_tangent_dimension"], 0)
        self.assertEqual(
            2 * tangent["two_by_three"]["two_dimensional_weight_blocks"]
            + 3 * tangent["two_by_three"]["three_dimensional_weight_blocks"]
            + tangent["two_by_three"]["singleton_weight_spaces"],
            36,
        )
        self.assertEqual(
            3 * tangent["three_by_two"]["three_dimensional_weight_blocks"]
            + tangent["three_by_two"]["singleton_weight_spaces"],
            36,
        )

    def test_rectangle_pair_incidence(self) -> None:
        pairs = self.payload["rectangle_pair_incidence"]
        self.assertEqual(pairs["ordered_pair_count"], 324)
        self.assertEqual(
            pairs["cross_image_dimension_histogram"],
            {"3": 18, "6": 36, "9": 120, "12": 6, "15": 72, "18": 72},
        )
        self.assertTrue(pairs["dimension_at_most_three_is_exactly_diagonal"])

    def test_boundary_is_explicit(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("complementary six-planes may collide", boundary)
        self.assertIn("does not exclude b=50", boundary)
        self.assertIn("or prove ChowRank", boundary)


if __name__ == "__main__":
    unittest.main()
