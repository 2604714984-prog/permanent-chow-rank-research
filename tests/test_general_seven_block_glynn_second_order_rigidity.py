from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = (
    ROOT / "scripts" / "general_seven_block_glynn_second_order_rigidity.py"
)
INDEPENDENT = (
    ROOT
    / "scripts"
    / "general_seven_block_glynn_second_order_rigidity_independent.py"
)
DATA = ROOT / "data" / "general_seven_block_glynn_second_order_rigidity.json"
EXPECTED = "e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c"
PRIMARY_MARKER = "GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_PASS"
INDEPENDENT_MARKER = (
    "GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_INDEPENDENT_PASS"
)


def load_primary():
    spec = importlib.util.spec_from_file_location(
        "seven_block_second_order",
        PRIMARY,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load second-order rigidity module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SevenBlockGlynnSecondOrderRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_primary()
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        core = self.module.build_core()
        digest = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode(
                "utf-8"
            )
        ).hexdigest()
        self.assertEqual(digest, EXPECTED)
        expected = dict(core)
        expected["core_sha256"] = EXPECTED
        self.assertEqual(self.payload, expected)

    def test_uniform_kernel_and_curvature_data(self) -> None:
        uniform = self.payload["uniform_exact_data"]
        self.assertEqual(uniform["full_first_order_rank"], 574)
        self.assertEqual(uniform["full_first_order_kernel_dimension"], 92)
        self.assertEqual(uniform["projected_tangent_rank"], 108)
        self.assertEqual(uniform["kernel_pair_count"], 4278)
        self.assertEqual(
            uniform["nonzero_polarized_curvature_pairs"],
            306,
        )
        self.assertEqual(uniform["curvature_span_rank"], 24)
        self.assertEqual(uniform["curvature_quotient_rank"], 0)
        self.assertEqual(uniform["missing_augmented_projected_rank"], 109)

    def test_all_seven_deletions(self) -> None:
        checks = self.payload["deletion_checks"]
        self.assertEqual(len(checks), 7)
        self.assertEqual(
            sorted(check["missing_sign_bits"] for check in checks),
            list(range(1, 8)),
        )
        for check in checks:
            self.assertEqual(check["full_first_order_rank"], 574)
            self.assertEqual(
                check["full_first_order_kernel_dimension"],
                92,
            )
            self.assertEqual(check["projected_tangent_rank"], 108)
            self.assertEqual(check["kernel_pair_count"], 4278)
            self.assertEqual(
                check["nonzero_polarized_curvature_pairs"],
                306,
            )
            self.assertEqual(check["curvature_span_rank"], 24)
            self.assertEqual(check["curvature_quotient_rank"], 0)
            self.assertTrue(
                check["missing_summand_outside_projected_tangent"]
            )

    def test_claim_boundary(self) -> None:
        conclusion = self.payload["conclusion"]
        self.assertEqual(conclusion["first_order_absorption"], "IMPOSSIBLE")
        self.assertEqual(conclusion["second_order_absorption"], "IMPOSSIBLE")
        self.assertTrue(
            conclusion[
                "standard_seven_block_witness_locally_six_irreducible_through_order_two"
            ]
        )
        boundary = self.payload["claim_boundary"]
        self.assertEqual(boundary["global_six_block_literal_sum"], "OPEN")
        self.assertEqual(boundary["mu_6_4"], "OPEN_IN_[6,7]")

    def test_primary_and_independent_cli(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "payload.json"
            completed = subprocess.run(
                [sys.executable, "-O", str(PRIMARY), "--json", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertIn(PRIMARY_MARKER, completed.stdout)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")),
                self.payload,
            )

        independent = subprocess.run(
            [
                sys.executable,
                "-O",
                str(INDEPENDENT),
                "--expected-core",
                EXPECTED,
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertIn(INDEPENDENT_MARKER, independent.stdout)
        self.assertIn(EXPECTED, independent.stdout)

    def test_proof_scripts_have_no_bare_assert(self) -> None:
        for path in (PRIMARY, INDEPENDENT):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            self.assertFalse(
                any(isinstance(node, ast.Assert) for node in ast.walk(tree))
            )


if __name__ == "__main__":
    unittest.main()
