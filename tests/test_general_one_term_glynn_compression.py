from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts" / "general_one_term_glynn_compression.py"
INDEPENDENT = ROOT / "scripts" / "general_one_term_glynn_compression_independent.py"
DATA = ROOT / "data" / "general_one_term_glynn_compression.json"
EXPECTED_CORE = "045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e"


def load_primary():
    spec = importlib.util.spec_from_file_location("one_term_glynn_primary", PRIMARY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load primary script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class OneTermGlynnCompressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_primary()
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_general_construction_rows(self) -> None:
        rows = self.payload["exact_replay"]["construction_rows"]
        for m in range(3, 11):
            row = rows[str(m)]
            self.assertEqual(row["sign_terms_before_compression"], 2 ** (m - 1))
            self.assertEqual(row["blocks_after_compression"], 2 ** (m - 1) - 1)
            self.assertEqual(row["degree_of_chow_envelope"], m + 2)
            self.assertEqual(row["source_subsets_used_per_block"], 2)

    def test_exact_coefficient_replays(self) -> None:
        rows = self.payload["exact_replay"]["coefficient_rows"]
        self.assertEqual(rows["3"]["permanent_coefficients"], 6)
        self.assertEqual(rows["4"]["permanent_coefficients"], 24)
        self.assertEqual(rows["5"]["permanent_coefficients"], 120)
        self.assertEqual(rows["6"]["permanent_coefficients"], 720)
        self.assertEqual(rows["4"]["zero_coefficients"], 232)
        self.assertTrue(all(self.payload["exact_replay"]["walsh_relation_rows"].values()))

    def test_quartic_boundary(self) -> None:
        quartic = self.payload["quartic_n6_application"]
        self.assertEqual(quartic["blocks"], 7)
        self.assertEqual(quartic["previous_interval"], [6, 8])
        self.assertEqual(quartic["new_interval"], [6, 7])
        self.assertTrue(quartic["seven_block_literal_sum_nonzero"])
        boundary = self.payload["claim_boundary"]
        self.assertEqual(boundary["six_block_literal_sum"], "OPEN")
        self.assertEqual(boundary["seven_block_literal_sum"], "NONZERO")
        self.assertEqual(boundary["mu_6_4"], "OPEN_IN_[6,7]")

    def test_paired_column_sharpness(self) -> None:
        paired = self.payload["paired_column_sharpness"]
        self.assertEqual(paired["grouped_flattening_rank"], 6)
        self.assertEqual(paired["retained_sign_outer_product_span_rank"], 7)
        self.assertFalse(paired["rank_one_matrix_inside_zero_diagonal_symmetric_space"])
        self.assertEqual(paired["paired_column_minimum_terms"], 7)
        self.assertEqual(paired["paired_column_construction_terms"], 7)

    def test_frozen_payload_and_entry_points(self) -> None:
        self.assertEqual(self.payload["core_sha256"], EXPECTED_CORE)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "payload.json"
            primary = subprocess.run(
                [sys.executable, "-O", str(PRIMARY), "--json", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=60,
            )
            self.assertIn("GENERAL_ONE_TERM_GLYNN_COMPRESSION_PASS", primary.stdout)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.payload)
        independent = subprocess.run(
            [sys.executable, "-O", str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertIn("GENERAL_ONE_TERM_GLYNN_COMPRESSION_INDEPENDENT_PASS", independent.stdout)
        self.assertIn(EXPECTED_CORE, independent.stdout)


if __name__ == "__main__":
    unittest.main()
