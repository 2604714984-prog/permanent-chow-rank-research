from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_hook_plane_projection_barrier.py"
FROZEN = ROOT / "data" / "n6_hook_plane_projection_barrier.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_hook_barrier", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class HookPlaneProjectionBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_frozen_payload(self):
        self.assertEqual(self.payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_six_planes_are_pairwise_transverse_and_span_hook(self):
        self.assertEqual(self.payload["individual_plane_ranks"], [6] * 6)
        self.assertEqual(self.payload["pair_sum_ranks"], [12] * 15)
        self.assertEqual(self.payload["total_span_rank"], 23)

    def test_all_potentially_full_projections_are_singular(self):
        rows = self.payload["potentially_full_two_row_projection_audit"]
        self.assertEqual(len(rows), 45)
        self.assertEqual({row["exact_QQ_projection_rank"] for row in rows}, {10})
        self.assertFalse(any(row["full_rank_twelve"] for row in rows))


if __name__ == "__main__":
    unittest.main()
