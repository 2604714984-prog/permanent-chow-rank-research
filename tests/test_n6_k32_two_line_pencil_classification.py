import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_two_line_pencil_classification.py"
FROZEN = ROOT / "data" / "n6_k32_two_line_pencil_classification.json"

spec = importlib.util.spec_from_file_location("n6_k32_two_line_pencil_classification", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class TwoLinePencilClassificationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_counts(self):
        self.assertEqual(self.payload["candidate_count"], 44)
        self.assertEqual(self.payload["pair_count"], 946)
        self.assertEqual(self.payload["identically_rank_three_pair_count"], 102)
        self.assertEqual(self.payload["no_nonzero_finite_root_pair_count"], 844)
        self.assertEqual(self.payload["exceptional_ratio_pair_count"], 0)

    def test_exceptional_lines_are_existing(self):
        for item in self.payload["exceptional_pairs"]:
            self.assertEqual(item["ratio"], -1)
            self.assertIn(item["resulting_line"], range(44))

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
