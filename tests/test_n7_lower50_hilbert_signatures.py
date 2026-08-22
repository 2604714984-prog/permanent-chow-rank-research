from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower50_hilbert_signatures.py"
FROZEN = ROOT / "data" / "n7_lower50_hilbert_signatures.json"
INPUT = ROOT / "data" / "n7_b1_hilbert_triples.json"
SPEC = importlib.util.spec_from_file_location("n7_lower50_hilbert_signatures", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load H-02 signatures")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class Lower50HilbertSignatureTests(unittest.TestCase):
    def test_frozen_payload(self) -> None:
        self.assertEqual(
            MODULE.build_payload(INPUT),
            json.loads(FROZEN.read_text(encoding="utf-8")),
        )

    def test_compression_is_reversible(self) -> None:
        signatures = MODULE.group_signatures(INPUT)
        self.assertEqual(MODULE.reconstruct(signatures), MODULE.frozen_vectors(INPUT))
        self.assertEqual(len(signatures), 7)
        self.assertEqual(len(MODULE.reconstruct(signatures)), 84)

    def test_frontier_q5_q6_rows(self) -> None:
        rows = MODULE.group_signatures(INPUT)
        observed = [
            (row["frontier"], row["q3_q4_q5_q6"][2:]) for row in rows
        ]
        self.assertEqual(
            observed,
            [
                ("F1", [2, 1]),
                ("F2", [3, 2]),
                ("F3", [2, 1]),
                ("F3", [2, 0]),
                ("F4", [4, 3]),
                ("F5", [3, 2]),
                ("F5", [3, 1]),
            ],
        )


if __name__ == "__main__":
    unittest.main()
