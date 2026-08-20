import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_rank_one_support_germs.py"
FROZEN = ROOT / "data" / "n6_k32_rank_one_support_germs.json"

spec = importlib.util.spec_from_file_location("n6_k32_rank_one_support_germs", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class RankOneSupportGermsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_two_patterns_have_rank_67_and_three_quadrics(self):
        for item in self.payload["patterns"].values():
            self.assertEqual(item["jacobian_rank"], 67)
            self.assertEqual(item["kernel_dimension"], 5)
            self.assertEqual(item["quadratic_generator_count"], 3)
            self.assertEqual(item["quadratic_coefficient_rank"], 3)

    def test_branches_are_noncomplementary(self):
        for item in self.payload["patterns"].values():
            self.assertEqual(len(item["branches"]), 2)
            for branch in item["branches"]:
                self.assertLessEqual(branch["cross_rank"], 6)
                self.assertLessEqual(branch["operator_rank"], 1)
                self.assertLessEqual(branch["sum_rank"], 7)

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
