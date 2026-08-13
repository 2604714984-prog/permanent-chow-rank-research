import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x73_76_exclusion.py"
DATA = ROOT / "data" / "n6_lower29_b34_x73_76_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6091_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Lower29B34X7376ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_descending_plateau(self):
        rows = self.payload["descending_plateau_exclusions"]
        self.assertEqual([row["dimension"] for row in rows], [76, 75, 74, 73])
        self.assertTrue(all(row["excluded"] for row in rows))
        self.assertEqual([row["required_prolongation_lower"] for row in rows], [464, 465, 466, 467])

    def test_unique_endpoint(self):
        for row in self.payload["descending_plateau_exclusions"]:
            self.assertEqual(row["relation_state_count"], 11)
            self.assertEqual(row["t_at_most_14_states_excluded_count"], 10)
            self.assertEqual(row["forced_alpha"], [3] * 7)
            self.assertTrue(row["forced_common_W15"])

    def test_strict_conclusion_and_boundary(self):
        self.assertIn("x_A<=72 and f_A<=72", self.payload["strict_conclusion"])
        self.assertIn("does not classify the new 72-to-89 equality locus", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
