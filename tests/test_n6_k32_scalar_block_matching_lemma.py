import json
import unittest
from pathlib import Path

from scripts.n6_k32_scalar_block_matching_lemma import (
    DEFAULT_JSON,
    aggregate_formula,
    build_payload,
    direct_cross_matrix,
    exact_rank,
    matching_condition,
)


class ScalarBlockMatchingLemmaTests(unittest.TestCase):
    def test_frozen_payload(self):
        self.assertEqual(build_payload(), json.loads(DEFAULT_JSON.read_text()))

    def test_formula_matches_actual_beta_samples(self):
        for xs, ys in (
            ((1, 1, 1), (-1, -1, -1)),
            ((1, 2, 3), (-1, -2, -3)),
            ((1, 1, 2), (-1, -1, -2)),
            ((1, 2, 3), (4, 5, 6)),
        ):
            self.assertEqual(
                exact_rank(aggregate_formula(xs, ys)),
                int(direct_cross_matrix(xs, ys).rank()),
            )

    def test_rank_six_family(self):
        self.assertTrue(matching_condition((2, 2, 2), (-2, -2, -2)))
        self.assertEqual(exact_rank(aggregate_formula((2, 2, 2), (-2, -2, -2))), 6)
        self.assertFalse(matching_condition((1, 1, 2), (-1, -1, -2)))


if __name__ == "__main__":
    unittest.main()
