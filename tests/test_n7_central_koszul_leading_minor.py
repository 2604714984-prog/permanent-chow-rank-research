from __future__ import annotations

import importlib.util
import json
import os
import unittest
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_central_koszul_leading_minor.py"
SPEC = importlib.util.spec_from_file_location("n7_central_koszul_leading_minor", SCRIPT)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def explicit_leading_rows(n: int, output_degree: int, wedge_degree: int) -> int:
    subsets = tuple(combinations(range(n), output_degree))
    outputs = set()
    for rows in subsets:
        for columns in subsets:
            candidates = []
            for row in rows:
                for column in columns:
                    candidates.append(
                        (
                            tuple(entry for entry in rows if entry != row),
                            tuple(entry for entry in columns if entry != column),
                            n * row + column,
                        )
                    )
            candidates.sort()
            for wedge in combinations(range(n * n), wedge_degree):
                wedge_set = set(wedge)
                for position, (out_rows, out_columns, variable) in enumerate(candidates):
                    if variable in wedge_set:
                        continue
                    if all(candidate[2] in wedge_set for candidate in candidates[:position]):
                        outputs.add((out_rows, out_columns, tuple(sorted((*wedge, variable)))))
                        break
    return len(outputs)


class N7CentralKoszulLeadingMinorTests(unittest.TestCase):
    def test_inclusion_exclusion_matches_explicit_toy(self) -> None:
        exact = AUDIT.leading_minor_rank(4, 3, 2, 1)
        self.assertEqual(exact, explicit_leading_rows(4, 3, 2))

    def test_term_rank(self) -> None:
        self.assertEqual(AUDIT.one_term_rank(), 1_284_156_702_075_780)

    def test_frozen_arithmetic(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_central_koszul_leading_minor.json").read_text(encoding="utf-8")
        )
        rank = frozen["leading_minor_rank"]
        term = frozen["one_independent_chow_term_rank"]["rank"]
        self.assertEqual(frozen["lower_50_test"]["strict_gap"], rank - 50 * term)
        self.assertEqual(frozen["lower_50_test"]["passes"], rank > 50 * term)
        self.assertEqual(frozen["ordinary_chow_consequence"]["integer_lower_bound"], 26)
        self.assertFalse(frozen["lower_50_test"]["passes"])

    @unittest.skipUnless(os.environ.get("RUN_EXPENSIVE_REPLAYS") == "1", "full replay is opt-in")
    def test_full_replay(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_central_koszul_leading_minor.json").read_text(encoding="utf-8")
        )
        self.assertEqual(AUDIT.build_payload(1), frozen)


if __name__ == "__main__":
    unittest.main()
