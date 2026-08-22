from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_equality_packet_crossdegree_search.py"
SPEC = importlib.util.spec_from_file_location("n7_equality_packet_crossdegree_search", SCRIPT)
SEARCH = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SEARCH)


class TestN7EqualityPacketCrossdegreeSearch(unittest.TestCase):
    def test_packet_a_forced_defect_still_misses_targets(self) -> None:
        expected = {2: (47, 319), 3: (46, 307), 7: (42, 259)}
        for line_count, (fifth_rank, sixth_rank) in expected.items():
            row = SEARCH.packet_a_trial(20260815 + 100000 * line_count, line_count)
            self.assertEqual(row["fifth_power_rank"], fifth_rank)
            self.assertEqual(row["structural_degree_six_rank_cap"], sixth_rank)
            self.assertEqual(row["degree_six_span_rank"], sixth_rank)
            self.assertEqual(row["degree_six_target_increment"], 7)
            self.assertEqual(row["degree_seven_target_increment"], 1)

    def test_packet_b_random_and_glynn_pilots(self) -> None:
        rng = np.random.default_rng(20260815)
        evaluations = rng.integers(
            0, SEARCH.PRIME, size=(SEARCH.V_DIM, 400), dtype=np.int64
        )
        sixth_targets, seventh_target = SEARCH.permanent_targets(evaluations)
        for family, offset in (("random_graph", 900000), ("glynn_graph", 1200000)):
            row = SEARCH.packet_b_trial(
                20260815 + offset,
                family,
                evaluations,
                sixth_targets,
                seventh_target,
            )
            self.assertEqual(row["degree_six_projected_rank"], 336)
            self.assertEqual(row["degree_six_target_increment"], 49)
            self.assertEqual(row["degree_seven_projected_rank"], 49)
            self.assertEqual(row["degree_seven_target_increment"], 1)


if __name__ == "__main__":
    unittest.main()
