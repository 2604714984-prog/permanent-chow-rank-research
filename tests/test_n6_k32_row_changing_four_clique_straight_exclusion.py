import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_row_changing_four_clique_straight_exclusion.py"
FROZEN = ROOT / "data" / "n6_k32_row_changing_four_clique_straight_exclusion.json"

spec = importlib.util.spec_from_file_location(
    "n6_k32_row_changing_four_clique_straight_exclusion", SCRIPT
)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class RowChangingFourCliqueStraightExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_rank_profile(self):
        self.assertEqual(self.payload["generic_rank"], 8)
        self.assertEqual(
            self.payload["determinant_zero_chart_ranks"],
            {"a_nonzero": 6, "a_zero_b_zero": 6, "a_zero_c_zero": 6},
        )
        self.assertEqual(self.payload["theorem"]["det_zero_sum_rank_at_most"], 7)

    def test_minor_certificates(self):
        self.assertEqual(
            self.payload["generic_minor"]["factor"], "-2*b*(a*d - b*c)**2"
        )
        self.assertEqual(
            self.payload["b_zero_rank_eight_minor"]["factor"], "-2*a**2*d**3"
        )

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
