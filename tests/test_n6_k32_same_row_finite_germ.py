from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_k32_same_row_finite_germ.py"
FROZEN = ROOT / "data" / "n6_k32_same_row_finite_germ.json"

spec = importlib.util.spec_from_file_location("n6_k32_same_row_finite_germ", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load N6-125 script")
AUDIT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AUDIT)


class K32SameRowFiniteGermTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(AUDIT.build_payload(), self.payload)

    def test_linear_and_quadratic_certificate(self) -> None:
        exact = self.payload["exact_certificate"]
        self.assertEqual(exact["base_cross_rank"], 6)
        self.assertEqual(exact["base_sum_rank"], 9)
        self.assertEqual(exact["linear_rank"], 68)
        self.assertEqual(exact["kernel_dimension"], 4)
        self.assertEqual(
            set(exact["quadratic_generators"]),
            {"(x0 - x2)*(x0 + x2)", "x0*x3", "x2*x3"},
        )

    def test_three_branches(self) -> None:
        branches = self.payload["exact_certificate"]["branches"]
        self.assertEqual(branches["plus"], {"cross_rank": 6, "sum_rank": 9})
        self.assertEqual(branches["minus"], {"cross_rank": 6, "sum_rank": 9})
        self.assertEqual(branches["product"], {"cross_rank": 6, "sum_rank": 12})

    def test_product_branch_is_the_common_a_family(self) -> None:
        exact = self.payload["exact_certificate"]
        self.assertEqual(
            exact["complement_determinant_on_product"],
            "64*x3**3*(x1 - 1)**3",
        )
        self.assertTrue(exact["formal_sandwich"])


if __name__ == "__main__":
    unittest.main()
