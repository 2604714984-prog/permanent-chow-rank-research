from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY = SCRIPTS / "general_koszul_young_route_ceiling.py"
INDEPENDENT = SCRIPTS / "general_koszul_young_route_ceiling_independent.py"
FROZEN = ROOT / "data" / "general_koszul_young_route_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_koszul_young_route_ceiling", PRIMARY)


class GeneralKoszulYoungRouteCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["active_half_rank_checks"], 726)
        self.assertEqual(replay["term_quarter_rank_checks"], 6_083)
        self.assertEqual(replay["transpose_duality_checks"], 6_083)
        self.assertEqual(replay["route_ceiling_checks"], 6_083)

    def test_finite_maxima(self) -> None:
        maxima = self.payload["exact_replay"]["finite_maxima"]
        self.assertEqual(
            [maxima[str(n)]["maximum_dimension_route_ceiling"] for n in range(2, 13)],
            [2, 5, 8, 17, 30, 61, 110, 225, 413, 840, 1565],
        )
        for row in maxima.values():
            self.assertLessEqual(
                row["maximum_dimension_route_ceiling"],
                row["four_central_ceiling"],
            )

    def test_component_formula(self) -> None:
        self.assertEqual(AUDIT.active_component_rank(6, 3, 2), 216)
        self.assertEqual(AUDIT.active_component_rank(7, 4, 3), 832)

    def test_quarter_rank_boundary(self) -> None:
        for n, m, p in [(5, 3, 12), (8, 4, 28), (10, 5, 45)]:
            rank = AUDIT.term_rank(n, m, p)
            source, target = AUDIT.term_dimensions(n, m, p)
            self.assertGreaterEqual(4 * rank, min(source, target))

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "12c52a1ae78bd4f7526dfb78cd18a0fc56bae2bd97f5736526a5ec262cfa39d4",
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
            "GENERAL_KOSZUL_YOUNG_ROUTE_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_term_quarter_rank_checks=3024", completed.stdout)


if __name__ == "__main__":
    unittest.main()
