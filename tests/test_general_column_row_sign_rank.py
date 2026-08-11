from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_column_row_sign_rank_audit.py"
FROZEN = ROOT / "data" / "general_column_row_sign_rank_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_column_row_sign_rank_audit", SCRIPT)


class GeneralColumnRowSignRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_rank_and_full_fourier_support(self) -> None:
        for row in self.payload["degrees"]:
            expected = 1 << (row["n"] - 1)
            self.assertEqual(row["boolean_slice_size"], expected)
            self.assertEqual(row["walsh_character_count"], expected)
            self.assertEqual(row["nonzero_fourier_coefficients"], expected)
            self.assertEqual(row["column_sign_rank"], expected)
            self.assertEqual(row["row_sign_rank"], expected)

    def test_normalized_term_collapse(self) -> None:
        for row in self.payload["degrees"]:
            n = row["n"]
            self.assertEqual(
                row["normalized_column_sign_term_count"],
                1 << (n * (n - 1)),
            )
            self.assertEqual(
                row["terms_per_diagonal_signature"],
                1 << ((n - 1) ** 2),
            )
            self.assertEqual(
                row["walsh_character_count"] * row["terms_per_diagonal_signature"],
                row["normalized_column_sign_term_count"],
            )

    def test_n6_and_claim_boundary(self) -> None:
        n6 = next(row for row in self.payload["degrees"] if row["n"] == 6)
        self.assertEqual(n6["column_sign_rank"], 32)
        self.assertEqual(n6["row_sign_rank"], 32)
        self.assertIn(
            "unrestricted Chow terms are not controlled",
            self.payload["claim_boundary"],
        )

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
