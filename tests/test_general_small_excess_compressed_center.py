from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_small_excess_compressed_center.py"
INDEPENDENT = ROOT / "scripts" / "general_small_excess_compressed_center_independent.py"
FROZEN = ROOT / "data" / "general_small_excess_compressed_center.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_small_excess_compressed_center", SCRIPT)


class GeneralSmallExcessCompressedCenterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_exact_replay_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["matrix_cases"], 240)
        self.assertEqual(replay["operator_checks"], 645)
        self.assertEqual(replay["ordered_cross_checks"], 1_140)
        self.assertEqual(replay["eigenspace_checks"], 645)
        self.assertEqual(replay["near_endpoint_rows"], 908)
        self.assertEqual(replay["first_excess_rows"], 48)

    def test_frozen_payload_and_core_hash(self) -> None:
        self.assertEqual(self.frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "20fdf39cf1976ce9f11b10ebccb19398dc34313ed6b09ebff9362b42a1f2f578",
        )

    def test_sharp_linear_algebra_witness(self) -> None:
        row = AUDIT.audit_case(4, 1, (2, 1, 1))
        self.assertEqual(row["essential_dimension"], 3)
        self.assertEqual(row["operator_ranks"], [2, 1, 1])
        self.assertEqual(row["rank_excess"], 1)
        self.assertEqual(max(row["idempotence_defects"]), 1)
        self.assertEqual(row["maximum_cross_defect"], 1)
        self.assertEqual(max(row["center_defects"]), 2)

    def test_first_excess_arithmetic(self) -> None:
        rows = AUDIT.near_endpoint_rows()
        target = next(
            row
            for row in rows
            if (row["n"], row["m"], row["q"], row["excess"])
            == (5, 3, 2, 1)
        )
        self.assertEqual(target["one_eigenspace_floor"], 4)
        self.assertEqual(target["zero_eigenspace_floor"], 4)
        self.assertEqual(target["missing_dimension_cap"], 1)
        self.assertEqual(target["mixed_hessian_rank_cap"], 2)

    def test_endpoint_and_claim_boundary(self) -> None:
        theorem = self.payload["theorem"]
        self.assertIn("orthogonal idempotents", theorem["endpoint_recovery"])
        self.assertIn("codimension-one", theorem["first_excess"])
        self.assertIn("does not yet exclude", self.payload["claim_boundary"])

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        self.assertIn("independent_matrix_cases=240", completed.stdout)
        self.assertIn("independent_operator_checks=645", completed.stdout)
        self.assertIn(
            "GENERAL_SMALL_EXCESS_COMPRESSED_CENTER_INDEPENDENT_PASS",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
