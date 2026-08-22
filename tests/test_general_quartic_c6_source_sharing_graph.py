from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_c6_source_sharing_graph.py"
DATA = ROOT / "data" / "general_quartic_c6_source_sharing_graph.json"

spec = importlib.util.spec_from_file_location("c6_source_sharing_graph", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load C6 source-sharing graph replay")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class C6SourceSharingGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(cls_payload := self.payload, json.loads(DATA.read_text(encoding="utf-8")))
        self.assertEqual(cls_payload["six_frame_kernel_dimension_upper_bound"], 9)

    def test_graph_structure(self) -> None:
        self.assertEqual(self.payload["frame_count"], 96)
        self.assertEqual(self.payload["source_sharing_edges"], 432)
        self.assertEqual(self.payload["source_sharing_degree"], 9)
        self.assertEqual(self.payload["triangle_count"], 0)

    def test_maximal_six_frame_states(self) -> None:
        self.assertEqual(self.payload["six_frame_equality_graph"], "K3,3")
        self.assertEqual(self.payload["labeled_k33_six_sets"], 112)
        self.assertEqual(self.payload["row_column_orbits"], 3)
        self.assertEqual(self.payload["orbit_sizes"], [16, 48, 48])


if __name__ == "__main__":
    unittest.main()
