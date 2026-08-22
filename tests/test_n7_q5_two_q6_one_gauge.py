from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_q5_two_q6_one_gauge.py"
FROZEN = ROOT / "data" / "n7_q5_two_q6_one_gauge.json"
SPEC = importlib.util.spec_from_file_location("n7_q5_two_q6_one", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load q5=2,q6=1 gauge replay")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Q5TwoQ6OneGaugeTests(unittest.TestCase):
    def test_frozen_payload(self) -> None:
        self.assertEqual(MODULE.build_payload(), json.loads(FROZEN.read_text()))

    def test_gauge_dimensions(self) -> None:
        self.assertEqual(MODULE.WEDGE_DIMENSION, 21)
        self.assertEqual(MODULE.TARGET_DIMENSION, 42)
        self.assertEqual(MODULE.GAUGE_RANK, 7)
        self.assertEqual(MODULE.CANONICAL_COKERNEL_DIMENSION, 35)

    def test_relation_support_separation_bound(self) -> None:
        self.assertEqual(MODULE.minimum_veronese_relation_support(5), 7)
        self.assertEqual(MODULE.minimum_veronese_relation_support(6), 8)

    def test_sparse_cost_bound_exhaustively(self) -> None:
        costs = []
        for first_size in range(7, 43):
            for second_size in range(7, 43 - first_size):
                for first_binary in (False, True):
                    for second_binary in (False, True):
                        costs.append(
                            MODULE.sparse_two_block_cost(
                                first_size,
                                second_size,
                                first_binary,
                                second_binary,
                            )
                        )
        self.assertEqual(max(costs), 42)
        self.assertEqual(len(costs), 1740)

    def test_all_branch_bounds_contradict_rank_64(self) -> None:
        bounds = MODULE.build_payload()["branch_replacement_bounds"]
        self.assertLess(max(bounds.values()), MODULE.PERMANENT_WARING_RANK)


if __name__ == "__main__":
    unittest.main()
