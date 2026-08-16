from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "general_factor_span_zero_blocks.py"
INDEPENDENT_PATH = (
    ROOT / "scripts" / "general_factor_span_zero_blocks_independent.py"
)
DATA_PATH = ROOT / "data" / "general_factor_span_zero_blocks.json"

SPEC = importlib.util.spec_from_file_location(
    "general_factor_span_zero_blocks",
    MODULE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralFactorSpanZeroBlocksTests(unittest.TestCase):
    def test_strict_boundary(self) -> None:
        self.assertTrue(MODULE.factor_span_zero(4, 15))
        self.assertFalse(MODULE.factor_span_zero(4, 16))
        self.assertFalse(MODULE.factor_span_zero(4, 17))

    def test_central_tables(self) -> None:
        rows = MODULE.central_table()
        self.assertEqual(
            [row["n"] for row in rows if row["same_span_cluster_zero"]],
            [3] + list(range(5, 21)),
        )
        self.assertEqual(
            [row["n"] for row in rows if row["every_pair_quotient_exact"]],
            [7] + list(range(9, 21)),
        )

    def test_pair_exactness(self) -> None:
        n8 = MODULE.pair_table(8, 4)
        self.assertFalse(n8[0]["quotient_exact"])
        self.assertTrue(all(row["quotient_exact"] for row in n8[1:]))
        self.assertEqual(
            [row["literal_overlap_cap"] for row in n8[:5]],
            [0, 0, 0, 0, 1],
        )

        n6 = MODULE.pair_table(6, 3)
        self.assertEqual(
            [row["quotient_exact"] for row in n6],
            [False, False, False, False, True, True, True],
        )

    def test_projection_capacity(self) -> None:
        self.assertEqual(
            MODULE.projected_capacity(
                n=8,
                output_degree=4,
                total_term_count=20,
                removed_block_size=5,
                removed_block_span_dimension=8,
            ),
            1050,
        )
        with self.assertRaises(RuntimeError):
            MODULE.projected_capacity(
                n=8,
                output_degree=4,
                total_term_count=20,
                removed_block_size=5,
                removed_block_span_dimension=16,
            )

    def test_frozen_payload_matches_generator(self) -> None:
        generated = MODULE.build_payload()
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(generated, frozen)
        self.assertEqual(
            generated["core_sha256"],
            "cced4ddfe03f661634a5c5553944fd8cce48e027451e647a9b331ea9cd79b945",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_FACTOR_SPAN_ZERO_BLOCKS_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_n8_positive_intersection_exact=PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
