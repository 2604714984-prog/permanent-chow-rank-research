from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x78_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b34_x78_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6087_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B34X78ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_literal_floors_and_endpoint(self) -> None:
        floors = self.payload["improved_literal_floors"]
        self.assertEqual((floors["every_fifteen_set_literal_dimension_floor"], floors["every_seven_set_literal_dimension_floor"]), (288, 128))
        row = self.payload["conditional_x78_packet"]
        self.assertEqual((row["relation_state_count"], row["t_at_most_14_states_excluded_count"]), (11, 10))
        self.assertEqual((row["required_prolongation_lower"], row["alpha_at_most_two_cap"]), (462, 458))
        self.assertTrue(row["excluded"])

    def test_strict_conclusion_and_boundary(self) -> None:
        self.assertIn("x_A<=77 and f_A<=77", self.payload["strict_conclusion"])
        self.assertIn("does not exclude global b=34", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
