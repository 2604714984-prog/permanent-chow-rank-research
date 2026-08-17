from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SCRIPT = SCRIPTS / "general_graded_k0_syzygy_barrier.py"
INDEPENDENT = SCRIPTS / "general_graded_k0_syzygy_barrier_independent.py"
FROZEN = ROOT / "data" / "general_graded_k0_syzygy_barrier.json"

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


AUDIT = load_module("general_graded_k0_syzygy_barrier", SCRIPT)


class GeneralGradedK0SyzygyBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_staircase_interfaces(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["monomial_staircase_modules"], 923)
        self.assertEqual(replay["hilbert_betti_numerator_checks"], 923)
        self.assertEqual(replay["corner_short_exact_checks"], 2_772)
        self.assertEqual(replay["composition_factor_cells"], 16_632)

    def test_weighted_ratio_interfaces(self) -> None:
        replay = self.payload["exact_replay"]
        self.assertEqual(replay["weighted_ratio_checks"], 2_183)
        self.assertEqual(replay["exhaustive_boolean_weight_supports"], 4_079)
        for numerator, denominator, central in replay["ratio_diagnostics"].values():
            self.assertLessEqual(numerator, central * denominator)

    def test_frozen_theorem_core_and_counts(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(frozen["core_sha256"], self.payload["core_sha256"])
        self.assertEqual(frozen["status"], self.payload["status"])
        self.assertEqual(frozen["theorem"], self.payload["theorem"])
        self.assertEqual(frozen["claim_boundary"], self.payload["claim_boundary"])
        for key, value in frozen["exact_replay"].items():
            self.assertEqual(value, self.payload["exact_replay"][key])
        self.assertEqual(
            self.payload["core_sha256"],
            "8cabf216e75c6a3b83b56827f57d3689524cd94ef92120feecdd451743b6d23e",
        )

    def test_resolution_identity_on_named_examples(self) -> None:
        for partition in ((1,), (4, 2), (6, 6, 3, 1), (5, 4, 4, 2, 1)):
            hilbert = AUDIT.hilbert_function(partition)
            self.assertEqual(
                AUDIT.hilbert_numerator(hilbert),
                AUDIT.resolution_numerator(partition),
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
            "GENERAL_GRADED_K0_SYZYGY_BARRIER_INDEPENDENT_PASS",
            completed.stdout,
        )
        self.assertIn("independent_cell_filtration_checks=13860", completed.stdout)
        self.assertIn("independent_boolean_supports=12286", completed.stdout)


if __name__ == "__main__":
    unittest.main()
