from __future__ import annotations

import importlib.util
import json
import os
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_all_wedge_leading_minor_scan.py"
SPEC = importlib.util.spec_from_file_location("n7_all_wedge_leading_minor_scan", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N7AllWedgeLeadingMinorScanTests(unittest.TestCase):
    def test_signed_histogram_recovers_fixed_size_unions(self) -> None:
        events = (0b0011, 0b0110, 0b1100)
        histogram = AUDIT.signed_union_size_histogram(events)
        for size in range(5):
            recovered = sum(
                coefficient * AUDIT.comb(4 - union_size, size - union_size)
                for union_size, coefficient in enumerate(histogram)
                if coefficient and union_size <= size
            )
            explicit = sum(
                any((subset & event) == event for event in events)
                for subset in range(1 << 4)
                if subset.bit_count() == size
            )
            self.assertEqual(recovered, explicit)

    def test_frozen_summary(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_all_wedge_leading_minor_scan.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(len(frozen["rows"]), 49)
        self.assertEqual(
            frozen["rows"][24]["leading_minor_rank"],
            32_506_369_177_539_449,
        )
        self.assertEqual(frozen["best_row"], max(
            frozen["rows"],
            key=lambda row: (
                row["integer_lower_bound"],
                Fraction(row["ratio_numerator"], row["ratio_denominator"])
                if row["ratio_denominator"]
                else Fraction(-1),
            ),
        ))

    @unittest.skipUnless(os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1", "full replay is opt-in")
    def test_full_replay(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_all_wedge_leading_minor_scan.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(AUDIT.build_payload(1), frozen)


if __name__ == "__main__":
    unittest.main()
