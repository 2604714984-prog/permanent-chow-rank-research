from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_b64_prolongation_exclusion.py"
FROZEN = ROOT / "data" / "n6_b64_prolongation_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_b64_prolongation", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6B64ProlongationExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_complete_fixed_point_count(self) -> None:
        self.assertEqual(self.payload["fixed_F_count"], 18_564)
        self.assertEqual(
            self.payload["fixed_F_count_by_full_rectangle_blocks"],
            {"0": 455, "1": 4095, "2": 9009, "3": 5005},
        )

    def test_strict_prolongation_gap(self) -> None:
        self.assertEqual(
            self.payload["maximum_prolongation_dimension_upper_bound"], 436
        )
        self.assertEqual(self.payload["b64_required_dimension"], 456)
        self.assertEqual(self.payload["strict_gap"], 20)
        self.assertEqual(self.payload["maximizer_count"], 3)

    def test_histogram_is_complete(self) -> None:
        histogram = self.payload["prolongation_component_upper_histogram"]
        self.assertEqual(sum(histogram.values()), 18_564)
        self.assertEqual(max(map(int, histogram)), 436)

    def test_claim_boundary(self) -> None:
        boundary = self.payload["claim_boundary"]
        self.assertIn("upper bound, not exact", boundary)
        self.assertIn("excludes only the b=64 endpoint", boundary)
        self.assertIn("does not prove ChowRank(perm_6)>=27", boundary)


if __name__ == "__main__":
    unittest.main()
