import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_critical_six_scalar_frontier.py"
DATA = ROOT / "data" / "n6_lower29_b34_critical_six_scalar_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6102", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CriticalSixScalarFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_global_epsilon_profiles(self):
        block = self.payload["global_epsilon_profiles"]
        self.assertEqual(block["allowed_profile_count"], 6)
        self.assertTrue(block["every_profile_has_at_least_nineteen_epsilon_zero_terms"])

    def test_ten_scalar_states(self):
        rows = self.payload["critical_six_scalar_states"]
        self.assertEqual(len(rows), 10)
        self.assertEqual(Counter(row["t2"] for row in rows), {15: 4, 16: 3, 17: 2, 18: 1})
        self.assertEqual(Counter(row["a2"] for row in rows), {72: 4, 73: 3, 74: 2, 75: 1})

    def test_cap_and_common_quotient_flags(self):
        rows = self.payload["critical_six_scalar_states"]
        self.assertTrue(all(row["all_six_alpha_equal_three_forced_by_existing_caps"] for row in rows if row["t2"] <= 16))
        self.assertTrue(all(row["common_W15_forced"] == (row["t2"] == 15) for row in rows))

    def test_n6101_interface(self):
        self.assertEqual(
            sum(row["N6_101_second_shadow_classification_applies"] for row in self.payload["critical_six_scalar_states"]),
            4,
        )

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
