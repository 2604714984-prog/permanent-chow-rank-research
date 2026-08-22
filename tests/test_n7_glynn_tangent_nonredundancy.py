from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_glynn_tangent_nonredundancy.py"
SPEC = importlib.util.spec_from_file_location("n7_glynn_tangent_nonredundancy", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class N7GlynnTangentNonredundancyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_base_walsh_ranks(self) -> None:
        rows = self.payload["walsh_blocks"]["base_multidegree_representatives_by_parity_weight"]
        self.assertEqual([row["modular_rank_lower_bound"] for row in rows], [43] * 6 + [37])
        self.assertEqual(self.payload["walsh_blocks"]["base_multidegree_total_rank"], 2746)

    def test_off_diagonal_blocks(self) -> None:
        blocks = self.payload["walsh_blocks"]
        self.assertEqual(blocks["off_diagonal_multidegree_count"], 42)
        self.assertEqual(blocks["off_diagonal_parity_ranks"], [7] * 64)
        self.assertEqual(blocks["one_off_diagonal_multidegree_rank"], 448)

    def test_only_stabilizer_kernel_remains(self) -> None:
        self.assertEqual(self.payload["effective_source_dimension_after_intrinsic_factor_gauge"], 21568)
        self.assertEqual(self.payload["sum_map_tangent_rank"], 21562)
        self.assertEqual(self.payload["kernel_after_intrinsic_factor_gauge"], 6)
        self.assertEqual(self.payload["identified_kernel"]["dimension"], 6)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_glynn_tangent_nonredundancy.json").read_text(encoding="utf-8")
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
