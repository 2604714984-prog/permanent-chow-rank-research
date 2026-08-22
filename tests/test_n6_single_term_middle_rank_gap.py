from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_single_term_middle_rank_gap.py"

SPEC = importlib.util.spec_from_file_location("n6_single_term_middle_rank_gap", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the single-term rank-gap audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N6SingleTermMiddleRankGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_span_four_determinant_witness(self) -> None:
        span_four = self.payload["factor_span_four"]
        self.assertEqual(span_four["witness_rank"], 20)
        self.assertEqual(span_four["witness_determinant"], 440301256704)
        self.assertEqual(span_four["bracket_product_squared"], 82944)
        self.assertEqual(span_four["formula_constant"], 2304**2)
        self.assertEqual(span_four["dependent_witness_rank"], 18)

    def test_span_five_normal_forms(self) -> None:
        self.assertEqual(
            self.payload["factor_span_five_support_profiles"],
            {"1": 14, "2": 14, "3": 18, "4": 20, "5": 20},
        )

    def test_rank_nineteen_is_excluded(self) -> None:
        self.assertEqual(self.payload["factor_span_at_most_three_rank_cap"], 10)
        self.assertEqual(self.payload["factor_span_six_rank"], 20)
        self.assertEqual(self.payload["excluded_middle_rank"], 19)

    def test_claim_boundary(self) -> None:
        self.assertIn(
            "does not prove ChowRank(perm_6)>=27",
            self.payload["claim_boundary"],
        )

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n6_single_term_middle_rank_gap.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
