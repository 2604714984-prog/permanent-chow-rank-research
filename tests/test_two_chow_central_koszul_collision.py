from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "two_chow_central_koszul_collision.py"

SPEC = importlib.util.spec_from_file_location("two_chow_collision", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load the two-Chow collision audit")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class TwoChowCentralKoszulCollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_factors_are_independent(self) -> None:
        determinant = self.payload["three_factor_change_determinant"]
        self.assertEqual(determinant, -2)
        self.assertNotEqual(determinant, 0)

    def test_middle_images_are_disjoint(self) -> None:
        self.assertEqual(self.payload["individual_middle_ranks"], [20, 20])
        self.assertEqual(self.payload["combined_literal_middle_rank"], 40)
        self.assertEqual(self.payload["middle_image_intersection_dimension"], 0)

    def test_prolongation_and_koszul_collision(self) -> None:
        self.assertEqual(self.payload["central_sum_first_prolongation_dimension"], 48)
        self.assertEqual(self.payload["individual_first_koszul_ranks"], [105, 105])
        self.assertEqual(self.payload["combined_first_koszul_image_rank"], 192)
        self.assertEqual(self.payload["first_koszul_image_intersection_dimension"], 18)

    def test_frozen_payload_matches_replay(self) -> None:
        frozen = json.loads(
            (
                ROOT / "data" / "two_chow_central_koszul_collision.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(frozen, self.payload)


if __name__ == "__main__":
    unittest.main()
