from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_exact_ordinary_chow_rank_32_candidate.py"
FROZEN = ROOT / "data" / "n6_exact_ordinary_chow_rank_32_candidate.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_rank32_candidate", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6ExactOrdinaryChowRank32CandidateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_every_half_defect_row_dominates_ten_thirds(self) -> None:
        for encoded in self.payload["half_defect_rows"].values():
            row = tuple(Fraction(value) for value in encoded)
            self.assertTrue(AUDIT.dominates_half_defect(row))

    def test_defect_cancels_at_32(self) -> None:
        self.assertEqual(self.payload["minimum_n"], 32)
        self.assertEqual(self.payload["n31_gap"], 10)
        self.assertEqual(self.payload["n32_gap"], 0)

    def test_claim_is_conditional(self) -> None:
        self.assertEqual(
            self.payload["status"],
            "CONDITIONAL_CANDIDATE_ARITHMETIC_REPLAY",
        )
        self.assertIn("does not prove", self.payload["claim_boundary"])
        self.assertTrue(self.payload["conclusion"].startswith("If "))


if __name__ == "__main__":
    unittest.main()
