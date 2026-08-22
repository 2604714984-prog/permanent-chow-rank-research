import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_three_weight_torus_compression.py"
FROZEN = ROOT / "data" / "n6_k32_three_weight_torus_compression.json"

spec = importlib.util.spec_from_file_location("n6_k32_three_weight_torus_compression", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ThreeWeightTorusCompressionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_graph_counts(self):
        self.assertEqual(self.payload["candidate_count"], 44)
        self.assertEqual(self.payload["pair_count"], 946)
        self.assertEqual(self.payload["identically_rank_three_pair_count"], 102)
        self.assertEqual(self.payload["triangle_count"], 52)
        self.assertEqual(self.payload["four_clique_count"], 13)

    def test_weight_and_clique_boundary(self):
        self.assertEqual(self.payload["triangle_affine_rank_histogram"], {"2": 52})
        self.assertEqual(self.payload["degenerate_compatible_triangle_count"], 0)
        self.assertEqual(self.payload["triangles_outside_four_cliques"], 0)
        self.assertEqual(self.payload["four_clique_extension_count"], 0)
        self.assertEqual(self.payload["four_clique_symbolic_ranks"], [3] * 13)

    def test_replay_matches_frozen(self):
        self.assertEqual(module.build_payload(), self.payload)


if __name__ == "__main__":
    unittest.main()
