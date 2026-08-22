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
PRIMARY = ROOT / "scripts" / "general_seven_block_glynn_local_rigidity.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_seven_block_glynn_local_rigidity_independent.py"
)
DATA = ROOT / "data" / "general_seven_block_glynn_local_rigidity.json"
EXPECTED = "7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710"
PRIMARY_MARKER = "GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_PASS"
INDEPENDENT_MARKER = (
    "GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_INDEPENDENT_PASS"
)


def load_primary():
    spec = importlib.util.spec_from_file_location(
        "seven_block_local_rigidity",
        PRIMARY,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load primary local-rigidity module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SevenBlockGlynnLocalRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_primary()
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        core = self.module.build_core()
        digest = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        self.assertEqual(digest, EXPECTED)
        self.assertEqual(self.payload["core_sha256"], EXPECTED)
        expected_payload = dict(core)
        expected_payload["core_sha256"] = EXPECTED
        self.assertEqual(self.payload, expected_payload)

    def test_direct_pair_merge_obstruction(self) -> None:
        result = self.payload["direct_pair_merge"]
        self.assertEqual(result["pairs_checked"], 21)
        self.assertEqual(result["uniform_mode_rank_profile"], [2, 2, 3, 3])
        self.assertEqual(result["uniform_essential_dimension"], 10)
        self.assertEqual(result["degree_six_chow_derivative_essential_cap"], 6)
        self.assertFalse(result["direct_pair_merge_possible"])

    def test_all_deletions_have_rank_jump(self) -> None:
        tangent = self.payload["projected_tangent"]
        self.assertEqual(tangent["raw_projected_generators_per_block"], 28)
        self.assertEqual(tangent["exact_tangent_dimension_per_block"], 18)
        self.assertEqual(len(tangent["deletion_checks"]), 7)
        for check in tangent["deletion_checks"]:
            self.assertEqual(check["six_projected_tangent_rank"], [108, 108])
            self.assertEqual(
                check["augmented_with_missing_summand_rank"],
                [109, 109],
            )
        self.assertEqual(tangent["all_seven_projected_tangent_rank"], [123, 123])

    def test_claim_boundary(self) -> None:
        conclusion = self.payload["conclusion"]
        self.assertEqual(
            conclusion["direct_merge_of_two_standard_summands"],
            "IMPOSSIBLE",
        )
        self.assertEqual(
            conclusion["first_order_absorption_of_deleted_summand_by_other_six"],
            "IMPOSSIBLE",
        )
        boundary = self.payload["claim_boundary"]
        self.assertEqual(boundary["global_six_block_literal_sum"], "OPEN")
        self.assertEqual(boundary["mu_6_4"], "OPEN_IN_[6,7]")
        self.assertFalse(boundary["unrestricted_chow_rank_improvement"])

    def test_primary_and_independent_cli(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "payload.json"
            completed = subprocess.run(
                [sys.executable, "-O", str(PRIMARY), "--json", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=60,
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
            timeout=60,
        )
        self.assertIn(INDEPENDENT_MARKER, independent.stdout)
        self.assertIn(EXPECTED, independent.stdout)

    def test_proof_scripts_have_no_bare_assert(self) -> None:
        for path in (PRIMARY, INDEPENDENT):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            self.assertFalse(
                any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
                path,
            )


if __name__ == "__main__":
    unittest.main()
