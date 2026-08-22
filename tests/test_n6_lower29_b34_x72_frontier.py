import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x72_frontier.py"
DATA = ROOT / "data" / "n6_lower29_b34_x72_frontier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6093_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Lower29B34X72FrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_state_counts(self):
        self.assertEqual(self.payload["scalar_state_count"], 21)
        self.assertEqual(self.payload["existing_cap_excluded_count"], 18)
        self.assertEqual(self.payload["open_packet_count"], 3)

    def test_open_packets(self):
        names = [row["actual_refinement"]["name"] for row in self.payload["open_actual_packets"]]
        self.assertEqual(
            names,
            [
                "direct_t16_packet",
                "one_quadratic_relation_common_W15_packet",
                "one_defective_term_t15_packet",
            ],
        )

    def test_geometry_and_boundary(self):
        geometry = self.payload["x72_geometry_from_n6092"]
        self.assertEqual((geometry["first_shadow_dimension"], geometry["second_shadow_dimension"]), (89, 24))
        self.assertIn("not excluded", self.payload["strict_conclusion"])
        self.assertIn("not an exclusion", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
