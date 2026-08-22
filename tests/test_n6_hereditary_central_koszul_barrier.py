from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_hereditary_central_koszul_barrier.py"
FROZEN = ROOT / "data" / "n6_hereditary_central_koszul_barrier.json"

SPEC = importlib.util.spec_from_file_location("n6_central_koszul_barrier", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6HereditaryCentralKoszulBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_three_term_block_has_exact_central_profile(self) -> None:
        self.assertEqual(self.payload["factor_matrix_determinants"], [1, 4, 2])
        self.assertEqual(
            self.payload["three_term_central_rank_profile"],
            [0, 20, 40, 56],
        )
        self.assertNotEqual(self.payload["triple_full_determinant"], 0)
        self.assertTrue(
            all(value != 0 for value in self.payload["pair_minor_determinants"].values())
        )

    def test_supports_make_the_central_sums_direct(self) -> None:
        support = self.payload["support_audit"]
        self.assertLessEqual(
            support["coordinate_support_pair_intersection_maximum"], 2
        )
        self.assertLessEqual(
            support["coordinate_support_to_six_block_intersection_maximum"], 2
        )

    def test_every_nonempty_subset_is_centrally_certified_minimum(self) -> None:
        profile = self.payload["twenty_term_subset_profile"]
        self.assertEqual(
            profile["nonempty_subsets_checked_by_exact_count_profile"],
            2**20 - 1,
        )
        self.assertEqual(
            profile["minimum_margin_over_twenty_times_one_fewer_term"], 4
        )
        self.assertEqual(profile["full_twenty_term_middle_rank"], 384)
        self.assertEqual(profile["full_middle_rank_terms"], 20)

    def test_large_middle_third_koszul_collision(self) -> None:
        self.assertEqual(
            self.payload["full_symmetric_cubic_internal_koszul_ranks"],
            [56, 210, 336, 280, 120, 21, 0],
        )
        self.assertEqual(
            self.payload[
                "completed_three_term_block_ambient_middle_third_koszul_rank"
            ],
            329_070,
        )
        self.assertEqual(self.payload["twenty_term_aggregate_rank_upper"], 2_384_640)
        self.assertEqual(self.payload["aggregate_collision_lower"], 286_260)

    def test_two_sided_overlap_counterexample(self) -> None:
        defect = self.payload["two_sided_defect_example"]
        self.assertEqual(defect["six_term_rank"], 658_140)
        self.assertEqual(defect["column_intersection_c"], 658_140)
        self.assertEqual(defect["row_intersection_s"], 658_140)
        self.assertEqual(defect["c_plus_s_minus_r"], 658_140)

    def test_frozen_payload_matches_lightweight_replay(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        replay = json.loads(json.dumps(self.payload, sort_keys=True))
        self.assertEqual(frozen, replay)


if __name__ == "__main__":
    unittest.main()
