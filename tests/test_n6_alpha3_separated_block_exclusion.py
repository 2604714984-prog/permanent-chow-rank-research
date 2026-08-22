from __future__ import annotations

import importlib.util
import json
import unittest
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha3_separated_block_exclusion.py"
FROZEN = ROOT / "data" / "n6_alpha3_separated_block_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_alpha3_separated", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Alpha3SeparatedBlockExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_independent_small_shadow(self) -> None:
        triples = tuple(combinations(range(6), 3))
        observed = [0]
        for size in range(1, 7):
            observed.append(
                min(
                    len(
                        {
                            pair
                            for triple in family
                            for pair in combinations(triple, 2)
                        }
                    )
                    for family in combinations(triples, size)
                )
            )
        self.assertEqual(observed, [0, 3, 5, 6, 6, 8, 9])

    def test_pure_theorem_constants(self) -> None:
        theorem = self.payload["pure_theorem"]
        self.assertEqual(theorem["quadratic_pair_block_dimension"], 6)
        self.assertEqual(theorem["quadratic_permanent_intersection_per_pair_block"], 5)
        self.assertEqual(theorem["cubic_permanent_intersection_per_triple_upper"], 2)
        self.assertEqual(theorem["global_cubic_permanent_intersection_upper"], 40)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not classify arbitrary", boundary)
        self.assertIn("does not", boundary)
        self.assertIn("border-rank", boundary)


if __name__ == "__main__":
    unittest.main()
