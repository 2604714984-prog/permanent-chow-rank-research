from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_alpha1_prolongation_closure.py"
FROZEN = ROOT / "data" / "n6_alpha1_prolongation_closure.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_alpha1_closure", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6AlphaOneProlongationClosureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_alpha_one_cap(self) -> None:
        self.assertEqual(
            self.payload["pure_alpha1_prolongation_caps"],
            {"13": 440, "14": 448},
        )

    def test_layer_counts(self) -> None:
        self.assertEqual(
            [
                (
                    row["b"],
                    row["canonical_state_count"],
                    row["excluded_state_count"],
                    row["remaining_state_count"],
                )
                for row in self.payload["layers"]
            ],
            [(61, 73, 72, 1), (62, 11, 11, 0), (63, 11, 11, 0)],
        )

    def test_exact_b61_survivors(self) -> None:
        self.assertEqual(
            [
                row["state_id"]
                for row in self.payload["layers"][0]["remaining_states"]
            ],
            ["b61_state_072"],
        )

    def test_claim_boundary(self) -> None:
        self.assertIn("One canonical", self.payload["strict_conclusion"])
        self.assertIn("does not exclude", self.payload["claim_boundary"])
        self.assertIn("border-rank", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
