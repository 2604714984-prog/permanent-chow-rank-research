from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "general_permanent_center.py"
INDEPENDENT_PATH = ROOT / "scripts" / "general_permanent_center_independent.py"
DATA_PATH = ROOT / "data" / "general_permanent_center.json"

SPEC = importlib.util.spec_from_file_location("general_permanent_center", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GeneralPermanentCenterTests(unittest.TestCase):
    def test_center_dimension(self) -> None:
        payload = MODULE.build_payload()
        self.assertTrue(
            all(row["center_dimension"] == 1 for row in payload["order_audits"])
        )
        self.assertEqual(
            [row["m"] for row in payload["order_audits"]],
            list(range(3, 11)),
        )

    def test_off_diagonal_coverage(self) -> None:
        for row in MODULE.build_payload()["order_audits"]:
            variables = row["variable_count"]
            self.assertEqual(
                row["ordered_off_diagonal_center_coefficients"],
                variables * (variables - 1),
            )
            self.assertEqual(row["compatibility_graph_components"], 1)

    def test_n8_boundary(self) -> None:
        boundary = MODULE.build_payload()["n8_boundary"]
        self.assertEqual(boundary["joint_factor_span_dimension"], 16)
        self.assertFalse(boundary["strict_low_span_theorem_applies"])
        self.assertTrue(boundary["center_boundary_excludes_nonzero_intersection"])
        self.assertTrue(boundary["quotient_images_disjoint"])

    def test_numerical_bounds(self) -> None:
        payload = MODULE.build_payload()
        self.assertEqual(payload["n7_application"]["ordinary_lower_bound"], 44)
        self.assertEqual(payload["n8_application"]["ordinary_lower_bound"], 79)
        self.assertEqual(payload["n8_application"]["residual_terms"], 63)

    def test_frozen_payload(self) -> None:
        generated = MODULE.build_payload()
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(generated, frozen)
        self.assertEqual(
            generated["core_sha256"],
            "01ec7b368a872e0ffb2d27113045b27a808c4f275a50c68fc8b6908c7ae4f808",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_PERMANENT_CENTER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("m=4 variables=256", completed.stdout)


if __name__ == "__main__":
    unittest.main()
