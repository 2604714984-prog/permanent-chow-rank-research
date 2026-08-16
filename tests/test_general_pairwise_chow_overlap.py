from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / "scripts" / "general_pairwise_chow_overlap.py"
INDEPENDENT_PATH = (
    ROOT / "scripts" / "general_pairwise_chow_overlap_independent.py"
)
DATA_PATH = ROOT / "data" / "general_pairwise_chow_overlap.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PRIMARY = load_module("general_pairwise_chow_overlap", PRIMARY_PATH)


class GeneralPairwiseChowOverlapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = PRIMARY.build_payload()

    def test_transverse_formula(self) -> None:
        for n in range(3, 9):
            for shared in range(n + 1):
                for m in range(n + 1):
                    observed = PRIMARY.transversal_intersection_dimension(
                        n,
                        shared,
                        m,
                    )
                    expected = PRIMARY.comb(shared, m) if m <= shared else 0
                    self.assertEqual(observed, expected)

    def test_rotation_formula(self) -> None:
        expected_examples = {
            (4, 2): 4,
            (6, 3): 8,
            (8, 4): 16,
            (10, 5): 32,
        }
        for (n, m), expected in expected_examples.items():
            self.assertEqual(
                PRIMARY.rotation_intersection_dimension(n, m),
                expected,
            )

    def test_no_rank_promotion(self) -> None:
        decision = self.payload["route_decision"]
        self.assertFalse(
            decision["shared_factor_count_alone_controls_literal_overlap"]
        )
        self.assertFalse(decision["new_unrestricted_chow_rank_bound"])
        self.assertTrue(decision["transverse_frame_formula_is_exact"])

    def test_frozen_payload(self) -> None:
        frozen = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "ee041eb8476f13a643a4829c042a03d02e046d755960344edb06eb565e14a8a5",
        )

    def test_independent_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(INDEPENDENT_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn(
            "GENERAL_PAIRWISE_CHOW_OVERLAP_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_n6_m3_intersection=8", completed.stdout)
        self.assertIn("independent_n8_m4_intersection=16", completed.stdout)


if __name__ == "__main__":
    unittest.main()
