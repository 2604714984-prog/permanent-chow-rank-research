from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_glynn49_quadratic_interface_counterexample.py"
SPEC = importlib.util.spec_from_file_location(
    "n7_glynn49_quadratic_interface_counterexample", SCRIPT
)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TestN7Glynn49QuadraticInterfaceCounterexample(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_profiles(self) -> None:
        self.assertEqual(
            self.payload["H_profile_degrees_1_through_6"],
            [49, 462, 1330, 1645, 1029, 343],
        )
        self.assertEqual(
            self.payload["E_intersection_profile_degrees_1_through_6"],
            [49, 441, 1085, 875, 231, 14],
        )

    def test_quadratic_interface_counterexample(self) -> None:
        row = self.payload["quadratic_interface"]
        self.assertEqual(row["explicit_minor_determinant"], 2**36)
        self.assertTrue(row["E2_contained_in_H2"])
        self.assertEqual(row["rho_rank"], 21)
        self.assertEqual(row["degree_two_defect"], 0)

    def test_full_identity_failures_are_explicit(self) -> None:
        self.assertEqual(
            self.payload["complementary_sums"]["2_5"],
            {"actual": 1491, "permanent_upper": 1470},
        )
        self.assertEqual(
            self.payload["complementary_sums"]["3_4"],
            {"actual": 2975, "permanent_upper": 2940},
        )
        self.assertFalse(self.payload["E6_contained_in_H6"])
        self.assertEqual(self.payload["E6_intersection_dimension"], 14)

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (
                ROOT
                / "data"
                / "n7_glynn49_quadratic_interface_counterexample.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
