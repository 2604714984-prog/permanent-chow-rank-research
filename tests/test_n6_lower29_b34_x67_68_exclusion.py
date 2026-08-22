import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_lower29_b34_x67_68_exclusion.py"
DATA = ROOT / "data" / "n6_lower29_b34_x67_68_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6099_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class N6Lower29B34X6768ExclusionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_relation_envelope(self):
        row = self.payload["relation_envelope"]
        self.assertEqual(row["state_count"], 56)
        self.assertEqual(row["old_cap_excluded_count"], 43)
        self.assertEqual(row["open_state_count_before_new_argument"], 13)
        self.assertEqual((row["t15_t16_states"], row["t17_t18_states"]), (10, 3))

    def test_two_layers(self):
        rows = self.payload["layer_exclusions"]
        self.assertEqual([row["central_dimension"] for row in rows], [68, 67])
        self.assertEqual([row["six_term_shortening_dimension"] for row in rows], [48, 47])
        self.assertTrue(all(row["product_shadow_minimum"] == 75 for row in rows))
        self.assertTrue(all(row["excluded"] for row in rows))

    def test_loss_lemma_routes(self):
        self.assertTrue(
            self.payload["high_t_arguments"][
                "therefore_some_six_term_permanent_relation_dimension_is_at_most_75"
            ]
        )
        self.assertIn(
            "sum_j delta_j<=t",
            self.payload["quotient_deletion_loss_lemma"]["statement"],
        )

    def test_strict_boundary(self):
        self.assertEqual(self.payload["updated_residual_seven_set_upper"], 66)
        self.assertIn("x_A<=66", self.payload["strict_conclusion"])
        self.assertIn("global b=34 remain open", self.payload["claim_boundary"])

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
