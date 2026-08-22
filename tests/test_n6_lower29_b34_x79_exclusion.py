from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x79_exclusion.py"
FROZEN = ROOT / "data" / "n6_lower29_b34_x79_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6085_test", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Lower29B34X79ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_improved_literal_floors(self) -> None:
        row = self.payload["improved_literal_floors"]
        self.assertEqual((row["every_fifteen_set_literal_dimension_floor"], row["every_seven_set_literal_dimension_floor"]), (287, 127))

    def test_both_endpoint_rows(self) -> None:
        rows = self.payload["x79_x80_endpoint_rows"]
        self.assertEqual([row["central_dimension_x"] for row in rows], [80, 79])
        self.assertEqual([row["required_prolongation_lower"] for row in rows], [460, 461])
        self.assertTrue(all(row["forced_alpha"] == [3] * 7 for row in rows))
        self.assertTrue(all(row["actual_endpoint_excluded_by_n6083_block_dichotomy"] for row in rows))

    def test_strict_conclusion_and_boundary(self) -> None:
        self.assertIn("x_A<=78 and f_A<=78", self.payload["strict_conclusion"])
        boundary = self.payload["claim_boundary"]
        self.assertIn("does not exclude global b=34", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=29", boundary)


if __name__ == "__main__":
    unittest.main()
