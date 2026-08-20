from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_first_schur_weight_blocks.py"
FROZEN = ROOT / "data" / "n6_k32_first_schur_weight_blocks.json"


spec = importlib.util.spec_from_file_location(
    "n6_k32_first_schur_weight_blocks", SCRIPT
)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-124 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32FirstSchurWeightBlocksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_singleton_blocks(self) -> None:
        exact = self.payload["exact_certificate"]
        self.assertEqual(exact["singleton_count"], 24)
        self.assertTrue(
            all(item["schur_rank"] == 3 for item in exact["singleton_profiles"])
        )

    def test_same_row_loci(self) -> None:
        profiles = self.payload["exact_certificate"]["same_row_profiles"]
        self.assertEqual(len(profiles), 4)
        self.assertTrue(
            all(
                item["locus"]["generic_rank"] == 6
                and item["locus"]["equal_coefficient_rank"] == 3
                and item["locus"]["rank_at_most_three_locus"] == "a0=a1=a2"
                for item in profiles
            )
        )


if __name__ == "__main__":
    unittest.main()
