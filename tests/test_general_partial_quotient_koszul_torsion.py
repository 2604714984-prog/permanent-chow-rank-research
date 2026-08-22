from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_partial_quotient_koszul_torsion.py"
INDEPENDENT = (
    ROOT / "scripts" / "general_partial_quotient_koszul_torsion_independent.py"
)
FROZEN = ROOT / "data" / "general_partial_quotient_koszul_torsion.json"

spec = importlib.util.spec_from_file_location("partial_torsion", SCRIPT)
module = importlib.util.module_from_spec(spec)
if spec.loader is None:
    raise RuntimeError("failed to load primary module")
spec.loader.exec_module(module)


class PartialQuotientKoszulTorsionTests(unittest.TestCase):
    def test_frozen_payload(self) -> None:
        self.assertEqual(module.payload(), json.loads(FROZEN.read_text()))

    def test_fixed_point_formula(self) -> None:
        for r in range(1, 9):
            for q in range(r + 1):
                for d in range(r + 1):
                    self.assertEqual(
                        module.exhaustive_fixed_point_maximum(r, q, d),
                        (r - d) * min(q, d),
                    )

    def test_one_relation_quadratic_dimensions(self) -> None:
        for r in range(2, 13):
            for support_size in range(1, r + 1):
                self.assertEqual(
                    module.one_relation_quadratic_count(r, support_size),
                    r - support_size + (1 if support_size == 2 else 0),
                )

    def test_one_relation_independent_scale(self) -> None:
        for r in range(2, 13):
            for support_size in range(1, r + 1):
                for d, value in enumerate(
                    module.one_relation_caps(r, support_size)
                ):
                    self.assertLessEqual(value, d * (r - d))

    def test_optimized_entry_points(self) -> None:
        for target in (SCRIPT, INDEPENDENT):
            completed = subprocess.run(
                [sys.executable, "-O", str(target)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("PASS", completed.stdout)

    def test_no_bare_assert_in_proof_scripts(self) -> None:
        for target in (SCRIPT, INDEPENDENT):
            self.assertNotIn("assert ", target.read_text())


if __name__ == "__main__":
    unittest.main()
