from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b1_hilbert_triples.py"
FROZEN = ROOT / "data" / "n7_b1_hilbert_triples.json"
SPEC = importlib.util.spec_from_file_location("n7_b1_hilbert_triples", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load B1F-01 module")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class B1HilbertTripleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(
            self.payload,
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_counts_and_s6_exclusion(self) -> None:
        rows = {row["label"]: row for row in self.payload["rows"]}
        self.assertEqual(
            [rows[f"S{index}"]["formal_o_sequence_count"] for index in range(1, 7)],
            [12, 12, 24, 12, 24, 0],
        )
        self.assertEqual(self.payload["formal_o_sequence_count"], 84)
        self.assertEqual(rows["S6"]["status"], "MACAULAY-EXCLUDED")

    def test_macaulay_zero_and_decisive_growth(self) -> None:
        self.assertEqual(MODULE.macaulay_successor(0, 4), 0)
        self.assertEqual(MODULE.macaulay_successor(2, 4), 2)
        self.assertLess(MODULE.macaulay_successor(2, 4), 3)

    def test_every_vector_is_an_o_sequence_of_length_42(self) -> None:
        for row in self.payload["rows"]:
            triple = tuple(row["hilbert_3_4_5"])
            for vector in row["first_differences"]:
                self.assertEqual(sum(vector), 42)
                self.assertEqual(vector[:2], [1, 6])
                self.assertEqual(
                    tuple(sum(vector[: degree + 1]) for degree in range(3, 6)),
                    triple,
                )
                for degree, (left, right) in enumerate(
                    zip(vector[1:], vector[2:]), start=1
                ):
                    self.assertGreater(right, 0)
                    self.assertLessEqual(right, MODULE.macaulay_successor(left, degree))

    def test_tail_shapes_are_complete(self) -> None:
        rows = {row["label"]: row for row in self.payload["rows"]}
        expected = {
            "S1": {(1, 1)},
            "S2": {(1, 1, 1)},
            "S3": {(2,), (1, 1)},
            "S4": {(1, 1, 1, 1)},
            "S5": {(2, 1), (1, 1, 1)},
        }
        for label, tails in expected.items():
            observed = {
                tuple(vector[6:]) for vector in rows[label]["first_differences"]
            }
            self.assertEqual(observed, tails)

    def test_prefix_boundary_is_exact(self) -> None:
        rows = {row["label"]: row for row in self.payload["rows"]}
        for label in ("S1", "S2", "S3", "S4", "S5"):
            delta2_values = {
                vector[2] for vector in rows[label]["first_differences"]
            }
            self.assertEqual(delta2_values, set(range(10, 22)))
        self.assertLess(
            MODULE.macaulay_successor(9, 2),
            33 - 7 - 9,
        )


if __name__ == "__main__":
    unittest.main()
