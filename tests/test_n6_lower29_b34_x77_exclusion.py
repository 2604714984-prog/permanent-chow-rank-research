from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x77_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b34_x77_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6089_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B34X77ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_literal_floors_and_endpoint(self) -> None:
        floors = self.payload["improved_literal_floors"]
        self.assertEqual(
            (
                floors["every_fifteen_set_literal_dimension_floor"],
                floors["every_seven_set_literal_dimension_floor"],
            ),
            (289, 129),
        )
        row = self.payload["conditional_x77_packet"]
        self.assertEqual(
            (row["required_prolongation_lower"], row["alpha_at_most_two_cap"]),
            (463, 458),
        )
        self.assertTrue(row["excluded"])

    def test_strict_conclusion_and_boundary(self) -> None:
        self.assertIn("x_A<=76 and f_A<=76", self.payload["strict_conclusion"])
        self.assertIn("does not exclude global b=34", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
