from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_multiblock_polar_descent.py"
INDEPENDENT = ROOT / "scripts" / "general_multiblock_polar_descent_independent.py"
FROZEN = ROOT / "data" / "general_multiblock_polar_descent.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_multiblock_polar_descent_test",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GeneralMultiblockPolarDescentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()
        cls.frozen = json.loads(FROZEN.read_text(encoding="utf-8"))

    def test_frozen_payload(self) -> None:
        self.assertEqual(self.payload, self.frozen)
        self.assertEqual(
            self.payload["core_sha256"],
            "bee52542fdaf272923cd937d97397a64670ee68e23c6b656f070b14abbcb2794",
        )

    def test_selected_zero_counts(self) -> None:
        observed = {
            (row["n"], row["degree"]): row["guaranteed_zero_terms"]
            for row in self.payload["finite_replay"]["selected_degree_rows"]
        }
        self.assertEqual(
            observed,
            {
                (8, 5): 5,
                (9, 6): 6,
                (10, 8): 16,
                (12, 8): 14,
                (16, 12): 35,
                (20, 10): 15,
                (32, 16): 40,
                (64, 32): 164,
                (100, 50): 404,
            },
        )

    def test_exact_small_order_regression(self) -> None:
        self.assertEqual(self.module.top_rank_lower_bound(3), 4)
        self.assertEqual(self.module.top_rank_lower_bound(4), 6)
        self.assertEqual(self.module.top_rank_lower_bound(5), 9)

    def test_descent_trace(self) -> None:
        trace = self.module.descent_trace(16, 12, 35)
        self.assertEqual(trace[0]["output_degree"], 12)
        self.assertEqual(trace[0]["discarded_labels"], 8)
        self.assertEqual(trace[-1]["term_count_after"], 0)

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT)],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        self.assertIn(
            "GENERAL_MULTIBLOCK_POLAR_DESCENT_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_increment_checks=130816", completed.stdout)
        self.assertIn(
            "independent_exhaustive_peeling_checks=1066768",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
