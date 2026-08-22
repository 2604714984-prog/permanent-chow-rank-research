from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b1_hilbert_triples_independent.py"
SPEC = importlib.util.spec_from_file_location("n7_b1_hilbert_independent", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load independent B1F-01 replay")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class IndependentB1HilbertTripleTests(unittest.TestCase):
    def test_independent_inventory_matches_frozen(self) -> None:
        self.assertEqual(
            MODULE.independent_inventory(),
            MODULE.frozen_inventory(ROOT / "data" / "n7_b1_hilbert_triples.json"),
        )

    def test_compositions_are_complete_and_unique(self) -> None:
        self.assertEqual(
            [len(MODULE.positive_compositions(total)) for total in range(5)],
            [1, 1, 2, 4, 8],
        )
        for total in range(5):
            rows = MODULE.positive_compositions(total)
            self.assertEqual(len(rows), len(set(rows)))
            self.assertTrue(all(sum(row) == total for row in rows))

    def test_decisive_s6_macaulay_failure(self) -> None:
        self.assertEqual(MODULE.successor(2, 4), 2)
        self.assertFalse(MODULE.is_o_sequence((1, 6, 10, 18, 2, 3, 2)))


if __name__ == "__main__":
    unittest.main()
