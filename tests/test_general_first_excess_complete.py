from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_first_excess_complete.py"
INDEPENDENT = SCRIPTS / "general_first_excess_complete_independent.py"
BOUNDARY = ROOT / "data" / "general_first_excess_complete_boundary.json"
PROOF = ROOT / "docs" / "general_first_excess_complete.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_first_excess_complete", PRIMARY)


class GeneralFirstExcessCompleteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.boundary = json.loads(BOUNDARY.read_text(encoding="utf-8"))

    def test_frozen_boundary(self) -> None:
        for key in (
            "status",
            "theorem",
            "cubic_interface",
            "selected_zero_block_examples",
            "claim_boundary",
        ):
            self.assertEqual(self.payload[key], self.boundary[key], key)

    def test_exact_quadratic_shadow_transition(self) -> None:
        cubic = self.payload["cubic_interface"]
        self.assertEqual(cubic["minimum_shadow_size_1"], 4)
        self.assertEqual(cubic["minimum_shadow_size_2"], 6)
        self.assertEqual(cubic["inverse_shadow_capacity"], 1)
        self.assertGreater(
            cubic["circuit_private_polar_dimension"],
            cubic["inverse_shadow_capacity"],
        )
        self.assertGreater(
            cubic["direct_polar_dimension"],
            cubic["inverse_shadow_capacity"],
        )

    def test_parent_exception_is_exactly_the_closed_triple(self) -> None:
        parent = self.payload["parent_boundary"]
        self.assertIn("(n,m,q)=(5,3,2)", parent["parent_cubic_exception"])

    def test_enlarged_zero_block_examples(self) -> None:
        rows = self.payload["selected_zero_block_examples"]
        self.assertEqual(
            rows,
            [
                {"n": 5, "m": 3, "zeta_plus": 2},
                {"n": 13, "m": 5, "zeta_plus": 2},
                {"n": 10, "m": 7, "zeta_plus": 5},
                {"n": 13, "m": 8, "zeta_plus": 5},
            ],
        )

    def test_proof_closes_the_cubic_boundary_only_at_first_excess(self) -> None:
        text = PROOF.read_text(encoding="utf-8")
        compact = text.replace(" ", "")
        self.assertIn("(5,3,2)", text)
        self.assertIn("m\\ge3", compact)
        self.assertIn("F_{5,2}(2)=6", compact)
        self.assertIn("qn=m^2+2", compact)
        self.assertNotIn("exact Chow rank for", text)

    def test_primary_cli_under_optimized_python(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(PRIMARY)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn("GENERAL_FIRST_EXCESS_COMPLETE_AUDIT_PASS", completed.stdout)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_FIRST_EXCESS_COMPLETE_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_minimum_two_rectangle_union=6",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
