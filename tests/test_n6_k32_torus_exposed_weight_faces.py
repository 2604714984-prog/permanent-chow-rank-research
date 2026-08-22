import json
import unittest
from pathlib import Path

from scripts.n6_k32_torus_exposed_weight_faces import build_payload


ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / "data" / "n6_k32_torus_exposed_weight_faces.json"


class TorusExposedWeightFacesTest(unittest.TestCase):
    def test_counts_and_frozen_payload(self):
        payload = build_payload()
        self.assertEqual(payload["character_count"], 28)
        self.assertEqual(payload["row_changing_exposed_count"], 24)
        self.assertEqual(payload["same_row_non_exposed_count"], 4)
        self.assertEqual(payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_all_row_witnesses_are_strict(self):
        payload = build_payload()
        self.assertTrue(
            all(
                item["top_score"] == 4
                and item["second_score"] <= 3
                and item["strict_gap"] >= 1
                for item in payload["row_changing_profiles"]
            )
        )

    def test_same_row_reason_is_explicit(self):
        payload = build_payload()
        self.assertTrue(
            all("row potentials" in item["non_exposure_reason"] for item in payload["same_row_profiles"])
        )


if __name__ == "__main__":
    unittest.main()
