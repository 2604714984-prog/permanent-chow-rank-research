from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_colored_differential_barrier.py"
FROZEN = ROOT / "data" / "n6_colored_differential_barrier.json"
SPEC = importlib.util.spec_from_file_location("n6_colored_differential_barrier", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class ColoredDifferentialBarrierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.audit()

    def test_subset_dimensions_respect_b50_caps(self) -> None:
        rows = self.payload["by_color_count"]
        self.assertEqual(
            [rows[str(q)]["S_I_dimension_over_Q"] for q in range(1, 7)],
            [0, 0, 0, 10, 30, 50],
        )
        self.assertTrue(
            all(
                rows[str(q)]["S_I_dimension_over_Q"]
                <= rows[str(q)]["b50_product_shadow_cap"]
                for q in range(1, 7)
            )
        )

    def test_four_five_six_color_shadows_are_surjective(self) -> None:
        rows = self.payload["by_color_count"]
        self.assertEqual(
            [rows[str(q)]["colored_shadow_rank_over_Q"] for q in (4, 5, 6)],
            [45, 60, 75],
        )
        self.assertTrue(
            all(rows[str(q)]["every_subset_shadow_equals_K_I"] for q in (4, 5, 6))
        )

    def test_every_nonempty_subset_is_checked(self) -> None:
        rows = self.payload["by_color_count"]
        self.assertEqual(
            sum(rows[str(q)]["number_of_subsets"] for q in range(1, 7)),
            63,
        )
        self.assertTrue(self.payload["all_63_nonempty_color_subsets_checked"])

    def test_frozen_payload(self) -> None:
        expected = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(self.payload, expected)


if __name__ == "__main__":
    unittest.main()
