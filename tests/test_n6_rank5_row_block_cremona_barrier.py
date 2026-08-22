from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_rank5_row_block_cremona_barrier.py"
FROZEN = ROOT / "data" / "n6_rank5_row_block_cremona_barrier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_rank5_cremona", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RankFiveRowBlockCremonaBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = load_module().build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_two_full_support_compressions_are_isomorphisms(self):
        barrier = self.payload["exact_local_barrier"]
        self.assertEqual((barrier["rank_a"], barrier["rank_b"]), (5, 5))
        self.assertEqual(barrier["determinant_mu_a"], -32)
        self.assertEqual(barrier["determinant_mu_b"], "-40/81")

    def test_induced_map_is_not_a_monomial_congruence(self):
        barrier = self.payload["exact_local_barrier"]
        self.assertEqual(barrier["fixed_edge_count"], 10)
        self.assertEqual(len(barrier["phi_F05"]), 5)
        self.assertEqual(
            [entry["coefficient"] for entry in barrier["phi_F05"]],
            [1, 2, 3, 4, 6],
        )

    def test_full_cross_row_system_excludes_this_explicit_extension(self):
        self.assertIn(
            "EXACT_QQ_EXPLICIT_CROSS_ROW_NONEXTENSION", self.payload["status"]
        )
        extension = self.payload["exact_local_barrier"]["full_cross_row_extension"]
        self.assertEqual(extension["system_shape"], [315, 72])
        self.assertEqual(extension["system_rank_over_Q"], 42)
        self.assertEqual(extension["system_nullity"], 30)
        self.assertEqual(extension["displayed_kernel_rank_over_Q"], 30)
        self.assertEqual(
            extension["system_times_displayed_kernel_rank_over_Q"], 0
        )
        self.assertIn("rank(X)<=5", extension["strict_conclusion"])
        self.assertIn("actual injective pair", extension["strict_conclusion"])

    def test_boundary_is_local(self):
        boundary = self.payload["claim_boundary"]
        self.assertIn("specific to the displayed rational", boundary)
        self.assertIn("not a theorem for every rank-five", boundary)
        self.assertIn("general all-singular", boundary)
        self.assertIn("does not contradict N6-069", boundary)
        self.assertIn("diagonal and wedge axes", boundary)


if __name__ == "__main__":
    unittest.main()
