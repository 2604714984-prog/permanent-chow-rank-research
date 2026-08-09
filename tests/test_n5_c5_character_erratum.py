import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = (
    ROOT
    / "evidence"
    / "small_n"
    / "n5_c5_character_certificate_corrected_summary.json"
)


class N5C5CharacterErratumTests(unittest.TestCase):
    def test_corrected_summary_and_claim_boundary(self):
        payload = json.loads(SUMMARY.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"], "CORRECTED_EXTERNAL_ROUTE_DIAGNOSTIC"
        )
        self.assertEqual(payload["block_shapes"]["trivial"], [12360, 9900])
        self.assertEqual(
            payload["block_shapes"]["nontrivial"], [12354, 9900]
        )

        upper = 11 * payload["single_chow_term_rank_upper_bound"]
        self.assertEqual(payload["eleven_term_rank_upper_bound"], upper)
        for residual in ("residual_0", "residual_1"):
            total = payload["corrected_total_ranks"][residual]
            self.assertGreater(total, upper)
            self.assertEqual(payload["margins"][residual], total - upper)

        boundary = payload["evidence_boundary"]
        self.assertFalse(boundary["large_sms_matrices_embedded"])
        self.assertFalse(boundary["unrestricted_chow_rank_consequence"])
        self.assertFalse(boundary["changes_S5_001_status"])
        self.assertNotEqual(
            payload["corrected_aggregate"]["sha256"],
            payload["superseded_aggregate"]["sha256"],
        )


if __name__ == "__main__":
    unittest.main()
