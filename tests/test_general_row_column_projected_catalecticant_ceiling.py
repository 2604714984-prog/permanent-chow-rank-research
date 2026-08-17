from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_row_column_projected_catalecticant_ceiling.py"
INDEPENDENT = SCRIPTS / "general_row_column_projected_catalecticant_ceiling_independent.py"
FROZEN = ROOT / "data" / "general_row_column_projected_catalecticant_ceiling.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("general_row_column_projected_catalecticant_ceiling", SCRIPT)


class GeneralRowColumnProjectedCatalecticantCeilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_exact_counts(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["projector_rank_checks"], 44)
        self.assertEqual(replay["projector_orthogonality_checks"], 49)
        self.assertEqual(replay["irreducible_pair_checks"], 142)
        self.assertEqual(replay["stable_sum_checks"], 142)
        self.assertEqual(replay["gl_pieri_checks"], 600)

    def test_selected_subset_modules(self) -> None:
        selected = self.payload["exact_replay"]["selected_rows"]
        self.assertEqual(selected["n6_m3"]["module_dimension"], 20)
        self.assertEqual(selected["n6_m3"]["specht_dimensions"], [1, 5, 9, 5])
        self.assertEqual(selected["n8_m4"]["module_dimension"], 70)
        self.assertEqual(selected["n8_m4"]["specht_dimensions"], [1, 7, 20, 28, 14])

    def test_selected_route_ceiling(self) -> None:
        row = self.payload["exact_replay"]["selected_rows"]["n8_m4"]
        module_dimension = row["module_dimension"]
        dims = row["specht_dimensions"]
        for key, rank in row["pair_ranks_mod_prime"].items():
            i, j = map(int, key.split(","))
            self.assertGreaterEqual(module_dimension * rank, dims[i] * dims[j])

    def test_frozen_payload(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.payload)
        self.assertEqual(
            self.payload["core_sha256"],
            "21b695309c3009ee3eade7ed553faeeefa60b061b2652430d5e48486f9e93cc4",
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
            "GENERAL_ROW_COLUMN_PROJECTED_CATALECTICANT_CEILING_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_eigenspace_checks=44", completed.stdout)
        self.assertIn("independent_multiplication_injection_checks=284", completed.stdout)


if __name__ == "__main__":
    unittest.main()
