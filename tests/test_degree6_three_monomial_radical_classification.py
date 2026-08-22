from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "degree6_three_monomial_radical_classification.py"
FROZEN = ROOT / "data" / "degree6_three_monomial_radical_classification.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("degree6_three_monomial_radical_classification", SCRIPT)


class DegreeSixThreeMonomialRadicalClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_type_counts_and_bound(self) -> None:
        self.assertEqual(self.payload["valid_ordered_venn_types"], 237)
        self.assertEqual(
            self.payload[
                "types_with_central_rank_strictly_above_two_term_cap"
            ],
            180,
        )
        self.assertEqual(
            self.payload["maximum_radical_dimension_among_strict_types"], 8
        )

    def test_equality_and_rho_nine_boundaries(self) -> None:
        self.assertEqual(self.payload["equality_type_count"], 4)
        for item in self.payload["equality_types"]:
            self.assertEqual(item["central_rank"], 44)
            self.assertEqual(item["radical_dimension"], 8)
        self.assertEqual(self.payload["rho_nine_type_count"], 3)
        for item in self.payload["rho_nine_types"]:
            self.assertEqual(item["pairing_rank_over_Q"], 4)
            self.assertEqual(item["radical_dimension"], 5)

    def test_pure_proof_unimodular_rho_nine_block(self) -> None:
        supports = AUDIT.canonical_supports((1, 2, 2, 2))
        self.assertIsNotNone(supports)
        rho, matrix = AUDIT.relation_pairing_matrix(supports)
        self.assertEqual(rho, 9)
        indices = [1, 2, 5, 6]
        block = [[matrix[row][column] for column in indices] for row in indices]
        self.assertEqual(
            block,
            [
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0],
            ],
        )

    def test_sharpness_witness_direct_rank(self) -> None:
        self.assertEqual(
            self.payload["equality_witness_direct_central_rank_over_Q"], 44
        )

    def test_scope_is_restricted(self) -> None:
        self.assertIn("coordinate-squarefree", self.payload["scope"])
        self.assertIn("q>=4", self.payload["scope"])

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)


if __name__ == "__main__":
    unittest.main()
