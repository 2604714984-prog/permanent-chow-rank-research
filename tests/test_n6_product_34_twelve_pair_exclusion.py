from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_product_34_twelve_pair_exclusion.py"
FROZEN = ROOT / "data" / "n6_product_34_twelve_pair_exclusion.json"


def load_module():
    spec = importlib.util.spec_from_file_location("n6_product_34_twelve", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module()


class N6Product34TwelvePairExclusionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)

    def test_product_endpoint_counts(self) -> None:
        products = self.payload["products"]
        self.assertEqual(
            {shape: products["standard"][shape]["endpoint_count"] for shape in ("2x6", "3x4", "4x3")},
            {"2x6": 3, "3x4": 30, "4x3": 10},
        )
        self.assertEqual(
            {shape: products["biflag"][shape]["endpoint_count"] for shape in ("2x6", "3x4", "4x3")},
            {"2x6": 0, "3x4": 20, "4x3": 14},
        )

    def test_safe_rectangle_histograms(self) -> None:
        products = self.payload["products"]
        self.assertEqual(
            products["standard"]["3x4"]["histogram_rectangle_count_over_maximum"],
            {"15/9": 6, "18/10": 24},
        )
        self.assertEqual(
            products["standard"]["4x3"]["histogram_rectangle_count_over_maximum"],
            {"18/10": 10},
        )
        self.assertEqual(
            products["biflag"]["3x4"]["histogram_rectangle_count_over_maximum"],
            {"18/10": 20},
        )
        self.assertEqual(
            products["biflag"]["4x3"]["histogram_rectangle_count_over_maximum"],
            {"18/10": 14},
        )

    def test_fixed_point_lemma_and_boundary(self) -> None:
        lemma = self.payload["fixed_point_lemma"]
        self.assertEqual(lemma["three_by_four_and_four_by_three_maximum"], 10)
        self.assertTrue(lemma["twelve_directions_are_required"])
        self.assertIn("No coordinate", lemma["conclusion"])
        self.assertIn("does not by itself close the kappa2=0 incidence", self.payload["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
