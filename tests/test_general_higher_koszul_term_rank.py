from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_higher_koszul_term_rank.py"
INDEPENDENT = SCRIPTS / "general_higher_koszul_term_rank_independent.py"
FROZEN = ROOT / "data" / "general_higher_koszul_term_rank.json"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_higher_koszul_term_rank", SCRIPT)


class GeneralHigherKoszulTermRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_replay_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["formula_recurrence_checks"], 6_083)
        self.assertEqual(replay["duality_checks"], 6_083)
        self.assertEqual(replay["first_koszul_checks"], 435)
        self.assertEqual(replay["diagnostic_cells"], 14_391)
        self.assertEqual(replay["low_wedge_cells"], 7_356)

    def test_n6_p2_exact_resolution(self) -> None:
        self.assertEqual(
            self.payload["n6_p2_exact_resolution"],
            {
                "2": {
                    "exact_term_rank": 8_730,
                    "source_target_route_ceiling": 17,
                },
                "3": {
                    "exact_term_rank": 12_066,
                    "source_target_route_ceiling": 21,
                },
                "4": {
                    "exact_term_rank": 9_235,
                    "source_target_route_ceiling": 16,
                },
            },
        )

    def test_formula_small_cell(self) -> None:
        self.assertEqual(AUDIT.chow_higher_koszul_rank(5, 3, 7), 3_927_129)
        self.assertEqual(
            AUDIT.chow_higher_koszul_rank(5, 3, 7),
            AUDIT.chow_higher_koszul_rank_from_homology(5, 3, 7),
        )

    def test_gorenstein_duality(self) -> None:
        n, d, p = 7, 4, 19
        self.assertEqual(
            AUDIT.chow_higher_koszul_rank(n, d, p),
            AUDIT.chow_higher_koszul_rank(
                n,
                n - d + 1,
                n * n - p - 1,
            ),
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "bb4b8829b06a6d3fe81e35aa4619606fb77e160a60ad7f89da6d0297225ce324",
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
            "GENERAL_HIGHER_KOSZUL_TERM_RANK_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn(
            "independent_n6_p2_exact=8730,12066,9235",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
