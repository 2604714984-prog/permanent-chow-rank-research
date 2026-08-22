from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.n7_lower50_hilbert_multiplication_envelopes import (
    build_payload,
    macaulay_successor,
)


ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "data" / "n7_lower50_hilbert_multiplication_envelopes.json"
SIGNATURES = ROOT / "data" / "n7_lower50_hilbert_signatures.json"


class HilbertMultiplicationEnvelopeTests(unittest.TestCase):
    def test_macaulay_controls(self) -> None:
        self.assertEqual(macaulay_successor(39, 4), 61)
        self.assertEqual(macaulay_successor(40, 5), 54)

    def test_counts_and_intervals(self) -> None:
        payload = build_payload(SIGNATURES)
        self.assertEqual(payload["signature_count"], 7)
        self.assertEqual(payload["compressed_cartesian_envelope_candidate_count"], 1894)
        self.assertEqual(payload["expanded_cartesian_envelope_candidate_count"], 22728)
        self.assertEqual(
            [row["cartesian_envelope_candidate_count"] for row in payload["rows"]],
            [308, 273, 280, 260, 273, 260, 240],
        )
        self.assertEqual(
            [
                (row["rank_I4_times_S1_interval"], row["rank_I5_times_S1_interval"])
                for row in payload["rows"]
            ],
            [
                ([401, 422], [870, 883]),
                ([403, 423], [872, 884]),
                ([403, 422], [870, 883]),
                ([403, 422], [870, 882]),
                ([404, 424], [873, 885]),
                ([404, 423], [872, 884]),
                ([404, 423], [872, 883]),
            ],
        )

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            build_payload(SIGNATURES),
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )


if __name__ == "__main__":
    unittest.main()
