from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_quartic_c6_source_multiplicity_cap.py"
INDEPENDENT = ROOT / "scripts" / "general_quartic_c6_source_multiplicity_cap_independent.py"
DATA = ROOT / "data" / "general_quartic_c6_source_multiplicity_cap.json"

spec = importlib.util.spec_from_file_location("c6_source_multiplicity", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class C6SourceMultiplicityCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = module.payload()

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, json.loads(DATA.read_text(encoding="utf-8")))

    def test_global_counts(self) -> None:
        self.assertEqual(self.payload["labeled_c6_frames"], 96)
        self.assertEqual(self.payload["source_incidences"], 1440)
        self.assertEqual(self.payload["distinct_sources"], 1008)
        self.assertEqual(
            self.payload["source_multiplicity_distribution"],
            {"1": 576, "2": 432},
        )
        self.assertEqual(self.payload["maximum_distinct_frame_multiplicity"], 2)

    def test_shape_extensions(self) -> None:
        table = self.payload["shape_table"]
        self.assertEqual(table["P5"]["extension_count"], 2)
        self.assertEqual(table["P4_DISJOINT_P2"]["extension_count"], 1)
        self.assertEqual(table["P3_DISJOINT_P3"]["extension_count"], 2)
        self.assertEqual(table["P5"]["distinct_sources"], 288)
        self.assertEqual(table["P4_DISJOINT_P2"]["distinct_sources"], 576)
        self.assertEqual(table["P3_DISJOINT_P3"]["distinct_sources"], 144)

    def test_claim_boundary(self) -> None:
        conclusion = self.payload["conclusion"]
        self.assertEqual(
            conclusion["triple_source_across_distinct_c6_frames"],
            "IMPOSSIBLE",
        )
        self.assertTrue(conclusion["triple_source_requires_repeated_frame_copy"])
        self.assertEqual(conclusion["general_second_order_lift"], "OPEN")

    def test_independent_replay(self) -> None:
        result = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_QUARTIC_C6_SOURCE_MULTIPLICITY_CAP_INDEPENDENT_PASS",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
