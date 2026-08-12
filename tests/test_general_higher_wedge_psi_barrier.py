from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from general_higher_wedge_psi_barrier import build_payload  # noqa: E402


class GeneralHigherWedgePsiBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_payload()

    def test_exact_profiles(self) -> None:
        self.assertEqual(
            self.payload["base_koszul_ranks"],
            [9, 80, 315, 720, 934, 720, 315, 80, 9],
        )
        self.assertEqual(
            self.payload["quotient_gains"],
            [1, 8, 28, 47, 32, 0, 0, 0, 0],
        )

    def test_naive_p3_extrapolation_fails(self) -> None:
        self.assertEqual(self.payload["p3_new_source_dimension"], 56)
        self.assertEqual(self.payload["p3_exact_gain"], 47)
        self.assertLess(
            self.payload["p3_exact_gain"],
            self.payload["naive_binomial_extrapolation"][3],
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "general_higher_wedge_psi_barrier.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
