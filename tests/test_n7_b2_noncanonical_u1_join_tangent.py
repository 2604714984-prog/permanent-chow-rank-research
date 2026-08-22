import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_b2_noncanonical_u1_join_tangent.py"
DATA = ROOT / "data" / "n7_b2_noncanonical_u1_join_tangent.json"
SPEC = importlib.util.spec_from_file_location("n7_b2_noncanonical_u1_join_tangent", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class NoncanonicalU1JoinTangentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_payload()

    def test_membership_pattern(self) -> None:
        for row in self.payload["tangent_memberships"]:
            self.assertEqual(row["full_degree_seven_tangent_membership"], row["factor_index"] in (0, 1))
            self.assertEqual(row["tangent_rank"], 138)

    def test_second_order_representative(self) -> None:
        row = self.payload["second_order_representative"]
        self.assertEqual(row["second_order_residual_support"], 4)
        self.assertTrue(row["second_order_obstruction_vanishes"])

    def test_coupled_chart_has_no_survivor(self) -> None:
        self.assertEqual(self.payload["tangent_and_operator_survivors"], [])

    def test_frozen_payload(self) -> None:
        expected = json.loads(DATA.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
