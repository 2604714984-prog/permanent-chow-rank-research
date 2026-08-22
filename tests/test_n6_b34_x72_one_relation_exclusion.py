import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b34_x72_one_relation_exclusion.py"
DATA = ROOT / "data" / "n6_b34_x72_one_relation_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6094_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6B34X72OneRelationExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_pair_graph(self):
        graph = self.payload["pair_difference_graph"]
        self.assertEqual(graph["kernel_line_positions"], 22)
        self.assertEqual(graph["minimum_good_degree"], 5)
        self.assertTrue(graph["every_vertex_has_two_good_neighbors_joined_by_a_good_edge"])

    def test_invertible_branch(self):
        branch = self.payload["invertible_block_branch"]
        self.assertEqual((branch["resulting_total_row_span_upper"], branch["required_total_row_span"]), (3, 4))
        self.assertEqual(branch["observed_remainder_modulo_15"], 14)
        self.assertTrue(branch["excluded"])

    def test_all_singular_and_boundary(self):
        branch = self.payload["all_singular_branch"]
        self.assertEqual((branch["frame_rank_upper"], branch["required_frame_rank"]), (4, 6))
        self.assertTrue(self.payload["actual_packet_excluded"])
        self.assertEqual(
            self.payload["updated_x72_frontier"],
            ["direct_t16_packet", "one_defective_term_t15_packet"],
        )

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
