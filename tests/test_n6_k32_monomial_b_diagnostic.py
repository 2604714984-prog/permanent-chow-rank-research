import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_monomial_b_diagnostic.py"
FROZEN = ROOT / "data" / "n6_k32_monomial_b_diagnostic.json"

spec = importlib.util.spec_from_file_location("n6_k32_monomial_b_diagnostic", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class MonomialBDiagnosticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_histogram_and_threshold(self):
        self.assertEqual(self.payload["candidate_count"], 720)
        self.assertEqual(
            self.payload["histogram_by_b"],
            {"0": 112, "1": 360, "2": 72, "3": 96, "4": 36, "5": 24, "6": 12, "7": 6, "9": 2},
        )
        self.assertEqual(self.payload["high_threshold_count"], 2)
        self.assertEqual(self.payload["formula_mismatch_count"], 0)

    def test_high_cases_are_the_two_pair_swaps(self):
        permutations = {
            tuple(row["permutation"])
            for row in self.payload["high_threshold_cases"]
        }
        self.assertEqual(permutations, {(0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)})

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
