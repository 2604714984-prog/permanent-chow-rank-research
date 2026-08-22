import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_same_target_rank_one_quadratic_diagnostic.py"
FROZEN = ROOT / "data" / "n6_k32_same_target_rank_one_quadratic_diagnostic.json"

spec = importlib.util.spec_from_file_location(
    "n6_k32_same_target_rank_one_quadratic_diagnostic", SCRIPT
)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class SameTargetRankOneQuadraticDiagnosticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_quadratic_profile(self):
        self.assertEqual(self.payload["base_cross_rank"], 6)
        self.assertEqual(self.payload["jacobian_rank"], 64)
        self.assertEqual(self.payload["kernel_dimension"], 8)
        self.assertEqual(self.payload["quadratic_generator_count"], 16)
        self.assertEqual(self.payload["quadratic_support_components"], 3)

    def test_branch_ranks(self):
        self.assertEqual(
            [item["generic_cross_rank"] for item in self.payload["branches"]],
            [6, 6, 6],
        )
        self.assertEqual(self.payload["generic_integrated_straight_branch_count"], 3)
        self.assertEqual(
            [item["generic_sum_rank"] for item in self.payload["branches"]],
            [7, 8, 7],
        )

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
