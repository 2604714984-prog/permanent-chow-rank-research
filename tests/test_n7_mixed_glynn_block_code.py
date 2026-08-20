from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_mixed_glynn_block_code.py"
SPEC = importlib.util.spec_from_file_location("n7_mixed_glynn_block_code", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class MixedGlynnBlockCodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload(24_681_357, 600)
        AUDIT.validate(cls.payload)

    def test_code_identification(self) -> None:
        self.assertEqual(self.payload["target_quotient_code_rank"], 42)
        self.assertEqual(self.payload["combined_code_rank"], 42)
        self.assertTrue(self.payload["codes_equal"])

    def test_ten_extra_blocks_are_below_the_minimum_support(self) -> None:
        code = self.payload["block_code"]
        self.assertEqual(code["minimum_nonzero_block_support"], 16)
        self.assertEqual(code["available_extra_blocks_in_endpoint_packet"], 10)
        self.assertFalse(code["can_add_target_direction_with_ten_extras"])


if __name__ == "__main__":
    unittest.main()
