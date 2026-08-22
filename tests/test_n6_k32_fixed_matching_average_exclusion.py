import json
import unittest

from scripts.n6_k32_fixed_matching_average_exclusion import DEFAULT_JSON, build_payload


class FixedMatchingAverageExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = build_payload()

    def test_frozen_payload(self):
        expected = json.loads(DEFAULT_JSON.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)

    def test_skew_exceptional_space(self):
        skew = self.payload["skew_exceptional_subspace"]
        self.assertEqual(skew["exact_QQ_rank"], 30)
        self.assertEqual(skew["exact_QQ_nullity"], 6)
        self.assertIn("common", skew["exceptional_form"])

    def test_pair_minor_logic(self):
        pair = self.payload["row_edge_pair_certificate"]
        self.assertEqual(pair["rank_at_zero"], 2)
        self.assertEqual(pair["constant_rank_two_minor"]["value"], 2)
        self.assertEqual(len(pair["rank_three_minors"]), 5)
        self.assertEqual(pair["rank_le_two_implication"], "u=v=delta_i=delta_j=tau=0")

    def test_scope_is_restricted(self):
        boundary = self.payload["claim_boundary"]
        self.assertIn("arbitrary invertible relative graph T", boundary)
        self.assertIn("does not prove lower 29", boundary)


if __name__ == "__main__":
    unittest.main()
