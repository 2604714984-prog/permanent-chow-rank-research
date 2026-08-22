from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_full_first_schur_weight_blocks.py"
FROZEN = ROOT / "data" / "n6_k32_full_first_schur_weight_blocks.json"

spec = importlib.util.spec_from_file_location("n6_k32_full_first_schur_weight_blocks", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-126 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32FullFirstSchurWeightBlocksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_full_jacobian_and_block_counts(self) -> None:
        self.assertEqual(self.payload["coefficient_matrix_shape"], [495, 72])
        self.assertEqual(self.payload["coefficient_matrix_rank"], 72)
        self.assertEqual(self.payload["weight_block_count"], 28)
        self.assertEqual(self.payload["row_changing_block_count"], 24)
        self.assertEqual(self.payload["same_row_block_count"], 4)
        self.assertEqual(self.payload["fixed_direction_count"], 44)

    def test_row_changing_locus(self) -> None:
        profiles = self.payload["row_changing_profiles"]
        self.assertTrue(all(item["generic_rank"] == 4 for item in profiles))
        self.assertTrue(all(item["rank_on_anti_diagonal"] == 3 for item in profiles))
        self.assertTrue(all(item["rank_at_most_three_locus"] == "a+b=0" for item in profiles))
        self.assertEqual(
            profiles[0]["b_zero_witness"],
            "-a**2*(a - b)*(a + b)",
        )

    def test_same_row_sign_lines(self) -> None:
        profiles = self.payload["same_row_profiles"]
        self.assertTrue(all(item["rank_at_most_three_line_count"] == 5 for item in profiles))
        expected = sorted(
            [
                [1, 1, 1, 1, 1, 1],
                [1, -1, -1, 1, -1, -1],
                [1, -1, 1, 1, -1, 1],
                [1, 1, -1, 1, 1, -1],
                [1, 1, 1, -1, -1, -1],
            ]
        )
        self.assertEqual(profiles[0]["rank_at_most_three_lines"], expected)
        for profile in profiles[1:]:
            self.assertEqual(profile["rank_at_most_three_lines"], expected)


if __name__ == "__main__":
    unittest.main()
