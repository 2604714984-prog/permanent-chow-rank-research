from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_nonuniform_shifted_matrix_ceiling.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_nonuniform_shifted_matrix_ceiling_independent.py"
)
FROZEN = ROOT / "data" / "general_nonuniform_shifted_matrix_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_nonuniform_shifted_matrix_ceiling", SCRIPT)


class GeneralNonuniformShiftedMatrixCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_primary_counts(self) -> None:
        replay = self.payload["finite_replay"]
        self.assertEqual(replay["pattern_checks"], 6_599)
        self.assertEqual(replay["degree_checks"], 442_386)
        self.assertEqual(replay["active_block_checks"], 1_013_292)
        self.assertEqual(replay["maximum_support_area_ratio"], [1, 1])

    def test_core_hash(self) -> None:
        self.assertEqual(
            self.payload["core_sha256"],
            "8402c0aefdd9c2bde28e7b2ec631f78faaf1ac35c7f0387801e6fe7d51dc8601",
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)

    def test_explicit_multiblock_case(self) -> None:
        source = (2, 1, 1)
        target = (1, 2)
        blocks = (
            AUDIT.ShiftBlock(0, 0, 2, 1, 1),
            AUDIT.ShiftBlock(1, 0, 1, 1, 1),
            AUDIT.ShiftBlock(1, 1, 1, 2, 1),
            AUDIT.ShiftBlock(2, 1, 1, 2, 1),
        )
        result = AUDIT.full_route_bounds(9, 5, source, target, blocks)
        self.assertLessEqual(
            result["direct_ratio_ceiling"],
            result["block_ceiling_sum"],
        )
        self.assertLessEqual(
            result["block_ceiling_sum"],
            result["coarse_pq_ceiling"],
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_NONUNIFORM_SHIFTED_MATRIX_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_assignment_checks=14400", completed.stdout)
        self.assertIn("independent_degree_checks=3604272", completed.stdout)


if __name__ == "__main__":
    unittest.main()
