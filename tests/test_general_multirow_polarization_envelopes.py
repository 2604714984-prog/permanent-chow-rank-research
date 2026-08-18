from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_multirow_polarization_envelopes.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_multirow_polarization_envelopes_independent.py"
)
FROZEN = ROOT / "data" / "general_multirow_polarization_envelopes.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_multirow_polarization_envelopes_test_module",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load multirow-envelope module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class MultirowPolarizationEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_cubic_fourier_selector(self) -> None:
        self.assertEqual(
            self.module.selector_coefficient(3, (0, 1, 2)),
            Fraction(1),
        )
        self.assertEqual(
            self.module.selector_coefficient(3, (2, 0, 1)),
            Fraction(1),
        )
        self.assertEqual(
            self.module.selector_coefficient(3, (0, 0, 1)),
            Fraction(0),
        )

    def test_staircase_endpoints_and_intermediate_rows(self) -> None:
        self.assertEqual(self.module.threshold_degree(6, 1), 36)
        self.assertEqual(self.module.dyadic_terms(1), 1)
        self.assertEqual(self.module.threshold_degree(6, 2), 30)
        self.assertEqual(self.module.dyadic_terms(2), 2)
        self.assertEqual(self.module.threshold_degree(6, 3), 24)
        self.assertEqual(self.module.dyadic_terms(3), 4)
        self.assertEqual(self.module.threshold_degree(6, 6), 6)
        self.assertEqual(self.module.dyadic_terms(6), 32)

    def test_arbitrary_q_and_fixed_degree_forms(self) -> None:
        self.assertEqual(
            self.module.construction_degree_for_terms(8, 7),
            8 * 6,
        )
        self.assertEqual(
            self.module.construction_degree_for_terms(8, 8),
            8 * 5,
        )
        self.assertEqual(
            self.module.construction_terms_for_degree(40, 8),
            8,
        )
        self.assertEqual(
            self.module.construction_terms_for_degree(56, 8),
            2,
        )
        self.assertEqual(
            self.module.construction_terms_for_degree(64, 8),
            1,
        )

    def test_frozen_payload(self) -> None:
        generated = self.module.build_payload()
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(generated, frozen)
        self.assertEqual(
            generated["core_sha256"],
            "88ff9229d4e176292d6211685aa3e7c901484904ea19d0578c01c073f195783e",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(
            "GENERAL_MULTIROW_POLARIZATION_ENVELOPES_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
