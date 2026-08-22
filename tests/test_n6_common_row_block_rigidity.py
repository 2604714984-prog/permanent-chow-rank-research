from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_common_row_block_rigidity.py"
FROZEN = ROOT / "data" / "n6_common_row_block_rigidity.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_common_row_block", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6CommonRowBlockRigidityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_three_exact_linear_systems(self) -> None:
        ranks = self.payload["regression"]["linear_system_ranks"]
        self.assertEqual(
            ranks,
            {
                "TZ_equals_ZT_transpose": 35,
                "RZ_plus_ZR_transpose": 36,
                "CZ_in_S0": 35,
            },
        )

    def test_monomial_normalizer_sample(self) -> None:
        sample = AUDIT.monomial_normalizer_sample()
        self.assertTrue(sample["preserves_S0"])
        self.assertEqual(sample["image_rank"], 15)

    def test_boundary_is_explicit(self) -> None:
        theorem = self.payload["pure_theorem"]
        self.assertTrue(theorem["survivor_all_row_and_column_blocks_singular"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("remains open", boundary)
        self.assertIn("does not prove ChowRank", boundary)
        self.assertIn("no border-rank claim", boundary)


if __name__ == "__main__":
    unittest.main()

